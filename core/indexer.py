import json
from pathlib import Path
from typing import List, Dict
from datetime import datetime
import logging
import re

# Configure logging
logging.basicConfig(level=logging.INFO, 
                   format='[%(asctime)s] [%(levelname)s] %(message)s',
                   datefmt='%H:%M:%S')

class ConversationIndexer:
    def __init__(self, history_file: str):
        self.history_file = Path(history_file)
        self.index: Dict[str, List[dict]] = {}
        self.topic_index: Dict[str, List[dict]] = {}
        logging.info(f"Initializing indexer with history file: {history_file}")
        
    def load_conversations(self) -> List[dict]:
        if not self.history_file.exists():
            logging.warning(f"History file not found: {self.history_file}")
            return []
        with open(self.history_file, 'r') as f:
            data = json.load(f)
            conversations = data.get('conversations', [])
            logging.info(f"Loaded {len(conversations)} conversations from history")
            return conversations
            
    def build_index(self):
        conversations = self.load_conversations()
        logging.info("Building conversation index...")
        
        # Clear existing indices
        self.index.clear()
        self.topic_index.clear()
        
        for conv in conversations:
            # Session indexing
            session_id = conv.get('session_id')
            query = conv.get('query', '').lower()
            response = conv.get('response', '')
            
            if session_id:
                if session_id not in self.index:
                    self.index[session_id] = []
                self.index[session_id].append(conv)
                
            # Only index actual queries, not tool executions
            if not query.startswith('tool execution'):
                # Extract final answers
                if 'FINAL_ANSWER:' in response:
                    final_answer = response.split('FINAL_ANSWER:')[1].strip()
                    keywords = self.extract_keywords(query)
                    
                    for keyword in keywords:
                        if keyword not in self.topic_index:
                            self.topic_index[keyword] = []
                        self.topic_index[keyword].append({
                            'query': query,
                            'answer': final_answer,
                            'timestamp': conv.get('timestamp')
                        })
                    logging.info(f"Indexed final answer for query: {query}")

    def extract_keywords(self, text: str) -> List[str]:
        text = text.lower()
        words = re.findall(r'\b\w+\b', text)
        # Filter out common words and keep meaningful ones
        stop_words = {'the', 'is', 'at', 'which', 'on', 'what'}
        return [w for w in words if len(w) > 3 and w not in stop_words]
    
    def find_related_answer(self, query: str) -> str:
        logging.info(f"Searching for related answer to: {query}")
        keywords = self.extract_keywords(query)
        print(f"\n🔍 Keywords extracted: {keywords}")
        
        best_match = None
        max_keyword_matches = 0
        
        for keyword in keywords:
            if keyword in self.topic_index:
                matches = self.topic_index[keyword]
                print(f"✨ Found {len(matches)} matches for keyword: {keyword}")
                
                for match in matches:
                    match_keywords = self.extract_keywords(match['query'])
                    common_keywords = len(set(keywords) & set(match_keywords))
                    
                    if common_keywords > max_keyword_matches:
                        max_keyword_matches = common_keywords
                        best_match = match
        
        if best_match:
            print(f"✅ Found best matching answer from query: {best_match['query']}")
            # Use the actual stored answer from history
            return f"FINAL_ANSWER: {best_match['answer']}"
        
        print("❌ No relevant historical data found")
        return None