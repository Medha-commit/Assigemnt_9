# Cortex-R Agent

An intelligent agent system that can process queries, maintain conversation history, and interact with multiple MCP (Multi-Channel Processing) servers.

## Features

- 🧠 Intelligent query processing
- 💾 Conversation history tracking
- 🔄 Multi-server support
- 🛡️ Query safety heuristics
- 📝 Structured logging
- 🔍 Context-aware responses

## Setup

1. Install dependencies:
```bash
pip install pyyaml asyncio

Example interactions:

🧑 What do you want to solve today? → tell me about everest
💡 Final Answer: Mount Everest is the world's highest peak...

🧑 What do you want to solve today? → what is 2+2
💡 Final Answer: {"result": 4}


Project Structure

working_S9/
├── agent.py           # Main agent implementation
├── modules/
│   ├── history.py     # Conversation history management
│   └── tools.py       # Utility functions and tools
├── core/
│   ├── loop.py        # Agent processing loop
│   ├── session.py     # Multi-MCP handling
│   ├── context.py     # Context management
│   └── heuristics.py  # Query safety checks
└── config/
    └── profiles.yaml  # Server configurations



    ## Features
- Query processing with safety checks
- Conversation history storage and retrieval
- Multi-server communication
- Context-aware response generation
- Structured logging and error handling


Adding 3 examples below for logs:

- Q: tell me about everest
A: Started new session with input: tell me about everest at 2025-05-24T05:36:41.978145 
- Q: Tool execution: perception
A: Arguments: {'perception': PerceptionResult(intent='Provide information about Mount Everest.', entities=['Everest', 'Mount Everest'], tool_hint='Could use a document search for prior knowledge, then web search if needed.', tags=[], selected_servers=['documents', 'websearch'])}
Result: {'result': PerceptionResult(intent='Provide information about Mount Everest.', 
entities=['Everest', 'Mount Everest'], tool_hint='Could use a document search for prior knowledge, then web search if needed.', tags=[], selected_servers=['documents', 'websearch'])}
- Q: Tool execution: plan
A: Arguments: {'plan': 'async def solve():\n    """Search DuckDuckGo. Usage: input={"input": {"query": "latest AI developments", "max_results": 5} } result = await mcp.call_tool(\'duckduckgo_search_results\', input)"""\n    input = {"input": {"query": "Mount Everest", "max_results": 5}}\n    result = await mcp.call_tool(\'duckduckgo_search_results\', input)\n\n    # FURTHER_PROCESSING_REQUIRED\n    return f"FURTHER_PROCESSING_REQUIRED: {result}"'}
Result: {'result': 'async def solve():\n    """Search DuckDuckGo. Usage: input={"input": {"query": "latest AI developments", "max_results": 5} } result = await mcp.call_tool(\'duckduckgo_search_results\', input)"""\n    input = {"input": {"query": "Mount Everest", "max_results": 5}}\n    result = await mcp.call_tool(\'duckduckgo_search_results\', input)\n\n    # FURTHER_PROCESSING_REQUIRED\n    return f"FURTHER_PROCESSING_REQUIRED: {result}"'}
- Q: Tool execution: solve_sandbox
A: Arguments: {'plan': 'async def solve():\n    """Search DuckDuckGo. Usage: input={"input": {"query": "latest AI developments", "max_results": 5} } result = await mcp.call_tool(\'duckduckgo_search_results\', input)"""\n    input = {"input": {"query": "Mount Everest", "max_results": 5}}\n    result = await mcp.call_tool(\'duckduckgo_search_results\', input)\n\n    # FURTHER_PROCESSING_REQUIRED\n    return f"FURTHER_PROCESSING_REQUIRED: {result}"'}
Result: {'result': 'FURTHER_PROCESSING_REQUIRED: meta=None content=[TextContent(type=\'text\', text=\'{\\n  "result": "Found 5 search results:\\\\n\\\\n1. Mount Everest - Wikipedia\\\\n   URL: https://en.wikipedia.org/wiki/Mount_Everest\\\\n   Summary: The closest sea toMountEverest\\\'ssummit is the Bay of Bengal, almost 700 km (430 mi) away. To approximate a climb of the entire height ofMountEverest, one would need to start from 
this coastline, a feat accomplished by Tim Macartney-Snape\\\'s team in 1990. Climbers 
usually begin their ascent from base camps above 5,000 m (16,404 ft).\\\\n\\\\n2. Mount Everest | Height, Location, Map, Facts, Climbers, & Deaths ...\\\\n   URL: https://www.britannica.com/place/Mount-Everest\\\\n   Summary: MountEverest, mountain on the crest of the Great Himalayas of southern Asia that lies on the border between Nepal and the 
Tibet Autonomous Region of China. Reaching an elevation of 29,032 feet (8,849 meters),MountEverestis the highest mountain in the world. It has long been revered by local peoples.\\\\n\\\\n3. Mount Everest - National Geographic Society\\\\n   URL: https://education.nationalgeographic.org/resource/mount-everest/\\\\n   Summary: Learn about the highest point on Earth, its history, its people, and its challenges. Find out howMountEverestgot its name, who first climbed it, and what dangers it poses for climbers and the environment.\\\\n\\\\n4. Mount Everest - WorldAtlas\\\\n   URL: https://www.worldatlas.com/mountains/mount-everest.html\\\\n   Summary: Learn about the world\\\'s highest peak, located on the border between China and Nepal, and its geological, climatic, and cultural features. Discover howMountEverestwas named, measured, and explored by various expeditions and surveyors.\\\\n\\\\n5. Mountaineer Tyler Andrews to Attempt Speed Record on Mount Everest\\\\n   URL: https://www.si.com/onsi/adventure/latest-news/mountaineer-tyler-andrews-to-attempt-speed-record-on-mount-everest\\\\n   Summary: With the ascent of Mt.Everest, he successfully completed climbing the highest peak on each of the world\\\'s seven continents, becoming the 58th person to conquer the Seven Summits.\\\\n"\\n}\', annotations=None)] isError=False'}
- Q: Tool execution: perception
A: Arguments: {'perception': PerceptionResult(intent='Provide information about Mount Everest based on a summary.', entities=['Mount Everest'], tool_hint='documents', tags=[], selected_servers=['documents'])}
Result: {'result': PerceptionResult(intent='Provide information about Mount Everest based on a summary.', entities=['Mount Everest'], tool_hint='documents', tags=[], selected_servers=['documents'])}

🎯 Input Summary:
- intent='Provide information about Mount Everest based on a summary.' entities=['Mount Everest'] tool_hint='documents' tags=[] selected_servers=['documents']

🎯 Goal:
Write a valid async Python function named `solve()` that solves the user query using exactly ONE FUNCTION_CALL. Or Summarize answer, if answer
is present in the input.

📏 STRICT RULES:
- Plan exactly ONE FUNCTION_CALL only.
- You must always define a function `async def solve():`
- Each tool call must follow the Usage docstring format exactly.
- You MUST call only those tools that are available in Tool Catalog.
- Call a tool using its tool name string, not function variable.
  E.g., await mcp.call_tool('add', input)
  (NOT await mcp.call_tool(add, input))
- Before each tool call, paste the full tool docstring enclosed in triple quotes (""").- Call the tool exactly as per its function signature: tool(input)
- If one FUNCTION_CALL depends on another, parse the previous result using json.loads(result.content[0].text)["result"] to extract the value from the tool's JSON output.     
-❗Important: Never inline json.loads(...) inside f"" strings. Always assign it to a var
iable first (e.g., parsed = json.loads(...)["result"]) and use that in return f"FINAL_ANSWER: {parsed}".
- End your function by returning a string that starts with 'FINAL_ANSWER: ' or 'FURTHER_PROCESSING_REQUIRED: '
- If the tool result is a document, webpage, or unstructured chunk, DO NOT return it as the FINAL_ANSWER.
- Instead, return it with 'FURTHER_PROCESSING_REQUIRED:' so the agent can interpret and summarize it next.

- No fallback, no multiple options.
- No explanation, no narration — only valid Python code.
- If the user input already includes clean extracted webpage/document content, do NOT call the tool again. Summarize or generate the final answer from it.


✅ Example 1: Output of last function parsed for next function
```python
import json
async def solve():
    # FUNCTION_CALL: 1
    """Convert characters to ASCII values. Usage: input={"input": {"string": "INDIA"}} 
result = await mcp.call_tool('strings_to_chars_to_int', input)"""
    input = {"input": {"string": "INDIA"}}
    result = await mcp.call_tool('strings_to_chars_to_int', input)
    numbers = json.loads(result.content[0].text)["result"]

    # FUNCTION_CALL: 2
    """Sum exponentials of int list. Usage: input={"input": {"numbers": [65, 66, 67]}} 
result = await mcp.call_tool('int_list_to_exponential_sum', input)"""
    input = {"input": {"numbers": numbers}}
    result = await mcp.call_tool('int_list_to_exponential_sum', input)
    final_result = json.loads(result.content[0].text)["result"]

    # FINAL_RESULT
    return f"FINAL_ANSWER: {final_result}"

```

---

✅ Example 2: Independent but sequential tool use
```python
import json
async def solve():
    # FUNCTION_CALL: 1
    """Search Wikipedia. Usage: input={"input": {"query": "Artificial Intelligence"}} result = await mcp.call_tool('search', input)"""
    input = {"input": {"query": "Artificial Intelligence"}}
    result1 = await mcp.call_tool('search', input)
    wiki_text = json.loads(result1.content[0].text)["result"]

    # FUNCTION_CALL: 2
    """Fetch News Articles. Usage: input={"input": {"query": "Artificial Intelligence latest news"}} result = await mcp.call_tool('fetch_news', input)"""
    input = {"input": {"query": "Artificial Intelligence latest news"}}
    result2 = await mcp.call_tool('fetch_news', input)
    news_text = json.loads(result2.content[0].text)["result"]

    # FINAL_RESULT
    return f"FINAL_ANSWER: Wikipedia says {wiki_text}. News says {news_text}."


```

---

✅ Example 3: Fallback logic, parsing not required
```python
import json
async def solve():
    try:
        # FUNCTION_CALL: 1
        """Fetch Company Overview. Usage: input={"company_name": "Tesla"} result = await mcp.call_tool('company_overview', input)"""
        input = {"input": {"company_name": "Tesla"}}
        result = await mcp.call_tool('company_overview', input)

    except Exception:
        try:
            # FUNCTION_CALL: 2
            """Fetch Company Backup Profile. Usage: input={"company_name": "Tesla"} result = await mcp.call_tool('backup_company_profile', input)"""
            input = {"input": {"company_name": "Tesla"}}
            result = await mcp.call_tool('backup_company_profile', input)

        except Exception:
            result = {"content": [{"text": "{\\"result\\": \\"Information not available.\\"}"}], "meta": None}

    # FINAL_RESULT
    if isinstance(result, CallToolResult):
        final_result = json.loads(result.content[0].text)["result"]
    else:
        final_result = json.loads(result["content"][0]["text"])["result"]

    return f"FINAL_ANSWER: {final_result}"


```

---

✅ Example 4: FURTHER_PROCESSING_REQUIRED: Summarize a document or webpage or similar ex
ample where you need information to take next action:
```python
async def solve():
    # FUNCTION_CALL: 1
    """Return clean webpage content. Usage: input={"input": {"url": "https://example.com"}} result = await mcp.call_tool('extract_webpage', input)"""
    input = {"url": "https://www.f1.com"}
    result = await mcp.call_tool(extract_webpage, input)  # from mcp_server_2

    # FURTHER_PROCESSING_REQUIRED
    return f"FURTHER_PROCESSING_REQUIRED: {result}"

```

✅ Example 5: Summarize fetched content
```python
async def solve():
    # FUNCTION_CALL: 1
    """Search documents to get relevant extracts. Usage: input={"input": {"query": "DLF apartment Capbridge"}} result = await mcp.call_tool('search_stored_documents', input)"""
    input = {"input": {"query": "DLF apartment Capbridge"}}
    result = await mcp.call_tool('search_stored_documents', input)

    # FURTHER_PROCESSING_REQUIRED
    return f"FURTHER_PROCESSING_REQUIRED: {result}"

```

💡 Tips:

If the task can be solved by one tool, stop after that.

You must return the result immediately using 'FINAL_ANSWER:' if you got the result for 
the user's task, or 'FURTHER_PROCESSING_REQUIRED:'.

Some times you WILL need to further process the results, like after looking at document, search or webpage parsed, summarizing it. Use 'FURTHER_PROCESSING_REQUIRED:' in those cases.
Use chaining only if necessary, but never plan more than 1 tool call.

"""
[11:06:52] [plan] LLM output: ```python
async def solve():
    """Learn about the world's highest peak, located on the border between China and Nepal, and its geological, climatic, and cultural features. Discover howMountEverestwas named, measured, and explored by various expeditions and surveyors."""
    return f"FINAL_ANSWER: Mount Everest is the world's highest peak, located on the border between China and Nepal. It has geological, climatic, and cultural features and was named, measured, and explored by various expeditions and surveyors."
```
[plan] async def solve():
    """Learn about the world's highest peak, located on the border between China and Nepal, and its geological, climatic, and cultural features. Discover howMountEverestwas named, measured, and explored by various expeditions and surveyors."""
    return f"FINAL_ANSWER: Mount Everest is the world's highest peak, located on the border between China and Nepal. It has geological, climatic, and cultural features and was named, measured, and explored by various expeditions and surveyors."
[loop] Detected solve() plan — running sandboxed...
[action] 🔍 Entered run_python_sandbox()

Result:
 FINAL_ANSWER: Mount Everest is the world's highest peak, located on the border between China and Nepal. It has geological, climatic, and cultural features and was named, measured, and explored by various expeditions and surveyors.

💡 Final Answer: Mount Everest is the world's highest peak, located on the border between China and Nepal. It has geological, climatic, and cultural features and was named, measured, and explored by various expeditions and surveyors.
INFO:modules.history:Added new entry for session 9af13ada-e4a2-4172-85b6-498754646739

***********************************************************
- Q: what is 3+2
A: Started new session with input: what is 3+2 at 2025-05-24T05:38:13.932711
- Q: Tool execution: perception
A: Arguments: {'perception': PerceptionResult(intent='Solve a simple math problem', entities=['3', '2'], tool_hint='python sandbox', tags=[], selected_servers=['math'])}     
Result: {'result': PerceptionResult(intent='Solve a simple math problem', entities=['3', '2'], tool_hint='python sandbox', tags=[], selected_servers=['math'])}

🎯 Input Summary:
- intent='Solve a simple math problem' entities=['3', '2'] tool_hint='python sandbox' tags=[] selected_servers=['math']

🎯 Goal:
Write a valid async Python function named `solve()` that solves the user query using exactly ONE FUNCTION_CALL. Or Summarize answer, if answer
is present in the input.

📏 STRICT RULES:
- Plan exactly ONE FUNCTION_CALL only.
- You must always define a function `async def solve():`
- Each tool call must follow the Usage docstring format exactly.
- You MUST call only those tools that are available in Tool Catalog.
- Call a tool using its tool name string, not function variable.
  E.g., await mcp.call_tool('add', input)
  (NOT await mcp.call_tool(add, input))
- Before each tool call, paste the full tool docstring enclosed in triple quotes (""").- Call the tool exactly as per its function signature: tool(input)
- If one FUNCTION_CALL depends on another, parse the previous result using json.loads(result.content[0].text)["result"] to extract the value from the tool's JSON output.     
-❗Important: Never inline json.loads(...) inside f"" strings. Always assign it to a var
iable first (e.g., parsed = json.loads(...)["result"]) and use that in return f"FINAL_ANSWER: {parsed}".
- End your function by returning a string that starts with 'FINAL_ANSWER: ' or 'FURTHER_PROCESSING_REQUIRED: '
- If the tool result is a document, webpage, or unstructured chunk, DO NOT return it as the FINAL_ANSWER.
- Instead, return it with 'FURTHER_PROCESSING_REQUIRED:' so the agent can interpret and summarize it next.

- No fallback, no multiple options.
- No explanation, no narration — only valid Python code.
- If the user input already includes clean extracted webpage/document content, do NOT call the tool again. Summarize or generate the final answer from it.


✅ Example 1: Output of last function parsed for next function
```python
import json
async def solve():
    # FUNCTION_CALL: 1
    """Convert characters to ASCII values. Usage: input={"input": {"string": "INDIA"}} 
result = await mcp.call_tool('strings_to_chars_to_int', input)"""
    input = {"input": {"string": "INDIA"}}
    result = await mcp.call_tool('strings_to_chars_to_int', input)
    numbers = json.loads(result.content[0].text)["result"]

    # FUNCTION_CALL: 2
    """Sum exponentials of int list. Usage: input={"input": {"numbers": [65, 66, 67]}} 
result = await mcp.call_tool('int_list_to_exponential_sum', input)"""
    input = {"input": {"numbers": numbers}}
    result = await mcp.call_tool('int_list_to_exponential_sum', input)
    final_result = json.loads(result.content[0].text)["result"]

    # FINAL_RESULT
    return f"FINAL_ANSWER: {final_result}"

```

---

✅ Example 2: Independent but sequential tool use
```python
import json
async def solve():
    # FUNCTION_CALL: 1
    """Search Wikipedia. Usage: input={"input": {"query": "Artificial Intelligence"}} result = await mcp.call_tool('search', input)"""
    input = {"input": {"query": "Artificial Intelligence"}}
    result1 = await mcp.call_tool('search', input)
    wiki_text = json.loads(result1.content[0].text)["result"]

    # FUNCTION_CALL: 2
    """Fetch News Articles. Usage: input={"input": {"query": "Artificial Intelligence latest news"}} result = await mcp.call_tool('fetch_news', input)"""
    input = {"input": {"query": "Artificial Intelligence latest news"}}
    result2 = await mcp.call_tool('fetch_news', input)
    news_text = json.loads(result2.content[0].text)["result"]

    # FINAL_RESULT
    return f"FINAL_ANSWER: Wikipedia says {wiki_text}. News says {news_text}."


```

---

✅ Example 3: Fallback logic, parsing not required
```python
import json
async def solve():
    try:
        # FUNCTION_CALL: 1
        """Fetch Company Overview. Usage: input={"company_name": "Tesla"} result = await mcp.call_tool('company_overview', input)"""
        input = {"input": {"company_name": "Tesla"}}
        result = await mcp.call_tool('company_overview', input)

    except Exception:
        try:
            # FUNCTION_CALL: 2
            """Fetch Company Backup Profile. Usage: input={"company_name": "Tesla"} result = await mcp.call_tool('backup_company_profile', input)"""
            input = {"input": {"company_name": "Tesla"}}
            result = await mcp.call_tool('backup_company_profile', input)

        except Exception:
            result = {"content": [{"text": "{\\"result\\": \\"Information not available.\\"}"}], "meta": None}

    # FINAL_RESULT
    if isinstance(result, CallToolResult):
        final_result = json.loads(result.content[0].text)["result"]
    else:
        final_result = json.loads(result["content"][0]["text"])["result"]

    return f"FINAL_ANSWER: {final_result}"


```

---

✅ Example 4: FURTHER_PROCESSING_REQUIRED: Summarize a document or webpage or similar ex
ample where you need information to take next action:
```python
async def solve():
    # FUNCTION_CALL: 1
    """Return clean webpage content. Usage: input={"input": {"url": "https://example.com"}} result = await mcp.call_tool('extract_webpage', input)"""
    input = {"url": "https://www.f1.com"}
    result = await mcp.call_tool(extract_webpage, input)  # from mcp_server_2

    # FURTHER_PROCESSING_REQUIRED
    return f"FURTHER_PROCESSING_REQUIRED: {result}"

```

✅ Example 5: Summarize fetched content
```python
async def solve():
    # FUNCTION_CALL: 1
    """Search documents to get relevant extracts. Usage: input={"input": {"query": "DLF apartment Capbridge"}} result = await mcp.call_tool('search_stored_documents', input)"""
    input = {"input": {"query": "DLF apartment Capbridge"}}
    result = await mcp.call_tool('search_stored_documents', input)

    # FURTHER_PROCESSING_REQUIRED
    return f"FURTHER_PROCESSING_REQUIRED: {result}"

```

💡 Tips:

If the task can be solved by one tool, stop after that.

You must return the result immediately using 'FINAL_ANSWER:' if you got the result for 
the user's task, or 'FURTHER_PROCESSING_REQUIRED:'.

Some times you WILL need to further process the results, like after looking at document, search or webpage parsed, summarizing it. Use 'FURTHER_PROCESSING_REQUIRED:' in those cases.
Use chaining only if necessary, but never plan more than 1 tool call.

"""
[11:08:17] [plan] LLM output: ```python
async def solve():
    # FUNCTION_CALL: 1
    """Add two numbers. Usage: input={"input": {"a": 1, "b": 2}} result = await mcp.call_tool('add', input)"""
    input = {"input": {"a": 3, "b": 2}}
    result = await mcp.call_tool('add', input)
    return f"FINAL_ANSWER: {result.content[0].text}"
```
[plan] async def solve():
    # FUNCTION_CALL: 1
    """Add two numbers. Usage: input={"input": {"a": 1, "b": 2}} result = await mcp.call_tool('add', input)"""
    input = {"input": {"a": 3, "b": 2}}
    result = await mcp.call_tool('add', input)
    return f"FINAL_ANSWER: {result.content[0].text}"
[loop] Detected solve() plan — running sandboxed...
[action] 🔍 Entered run_python_sandbox()

Result:
 FINAL_ANSWER: {
  "result": 5
}

💡 Final Answer: {
  "result": 5
}
INFO:modules.history:Added new entry for session 9af13ada-e4a2-4172-85b6-498754646739

********************************************************************


- Q: what is 2+2
A: Started new session with input: what is 2+2 at 2025-05-24T05:39:15.221502
- Q: Tool execution: perception
A: Arguments: {'perception': PerceptionResult(intent='Simple arithmetic calculation', entities=['2', '2'], tool_hint='python sandbox', tags=[], selected_servers=['math'])}   
Result: {'result': PerceptionResult(intent='Simple arithmetic calculation', entities=['2', '2'], tool_hint='python sandbox', tags=[], selected_servers=['math'])}

🎯 Input Summary:
- intent='Simple arithmetic calculation' entities=['2', '2'] tool_hint='python sandbox' tags=[] selected_servers=['math']

🎯 Goal:
Write a valid async Python function named `solve()` that solves the user query using exactly ONE FUNCTION_CALL. Or Summarize answer, if answer
is present in the input.

📏 STRICT RULES:
- Plan exactly ONE FUNCTION_CALL only.
- You must always define a function `async def solve():`
- Each tool call must follow the Usage docstring format exactly.
- You MUST call only those tools that are available in Tool Catalog.
- Call a tool using its tool name string, not function variable.
  E.g., await mcp.call_tool('add', input)
  (NOT await mcp.call_tool(add, input))
- Before each tool call, paste the full tool docstring enclosed in triple quotes (""").- Call the tool exactly as per its function signature: tool(input)
- If one FUNCTION_CALL depends on another, parse the previous result using json.loads(result.content[0].text)["result"] to extract the value from the tool's JSON output.     
-❗Important: Never inline json.loads(...) inside f"" strings. Always assign it to a var
iable first (e.g., parsed = json.loads(...)["result"]) and use that in return f"FINAL_ANSWER: {parsed}".
- End your function by returning a string that starts with 'FINAL_ANSWER: ' or 'FURTHER_PROCESSING_REQUIRED: '
- If the tool result is a document, webpage, or unstructured chunk, DO NOT return it as the FINAL_ANSWER.
- Instead, return it with 'FURTHER_PROCESSING_REQUIRED:' so the agent can interpret and summarize it next.

- No fallback, no multiple options.
- No explanation, no narration — only valid Python code.
- If the user input already includes clean extracted webpage/document content, do NOT call the tool again. Summarize or generate the final answer from it.


✅ Example 1: Output of last function parsed for next function
```python
import json
async def solve():
    # FUNCTION_CALL: 1
    """Convert characters to ASCII values. Usage: input={"input": {"string": "INDIA"}} 
result = await mcp.call_tool('strings_to_chars_to_int', input)"""
    input = {"input": {"string": "INDIA"}}
    result = await mcp.call_tool('strings_to_chars_to_int', input)
    numbers = json.loads(result.content[0].text)["result"]

    # FUNCTION_CALL: 2
    """Sum exponentials of int list. Usage: input={"input": {"numbers": [65, 66, 67]}} 
result = await mcp.call_tool('int_list_to_exponential_sum', input)"""
    input = {"input": {"numbers": numbers}}
    result = await mcp.call_tool('int_list_to_exponential_sum', input)
    final_result = json.loads(result.content[0].text)["result"]

    # FINAL_RESULT
    return f"FINAL_ANSWER: {final_result}"

```

---

✅ Example 2: Independent but sequential tool use
```python
import json
async def solve():
    # FUNCTION_CALL: 1
    """Search Wikipedia. Usage: input={"input": {"query": "Artificial Intelligence"}} result = await mcp.call_tool('search', input)"""
    input = {"input": {"query": "Artificial Intelligence"}}
    result1 = await mcp.call_tool('search', input)
    wiki_text = json.loads(result1.content[0].text)["result"]

    # FUNCTION_CALL: 2
    """Fetch News Articles. Usage: input={"input": {"query": "Artificial Intelligence latest news"}} result = await mcp.call_tool('fetch_news', input)"""
    input = {"input": {"query": "Artificial Intelligence latest news"}}
    result2 = await mcp.call_tool('fetch_news', input)
    news_text = json.loads(result2.content[0].text)["result"]

    # FINAL_RESULT
    return f"FINAL_ANSWER: Wikipedia says {wiki_text}. News says {news_text}."


```

---

✅ Example 3: Fallback logic, parsing not required
```python
import json
async def solve():
    try:
        # FUNCTION_CALL: 1
        """Fetch Company Overview. Usage: input={"company_name": "Tesla"} result = await mcp.call_tool('company_overview', input)"""
        input = {"input": {"company_name": "Tesla"}}
        result = await mcp.call_tool('company_overview', input)

    except Exception:
        try:
            # FUNCTION_CALL: 2
            """Fetch Company Backup Profile. Usage: input={"company_name": "Tesla"} result = await mcp.call_tool('backup_company_profile', input)"""
            input = {"input": {"company_name": "Tesla"}}
            result = await mcp.call_tool('backup_company_profile', input)

        except Exception:
            result = {"content": [{"text": "{\\"result\\": \\"Information not available.\\"}"}], "meta": None}

    # FINAL_RESULT
    if isinstance(result, CallToolResult):
        final_result = json.loads(result.content[0].text)["result"]
    else:
        final_result = json.loads(result["content"][0]["text"])["result"]

    return f"FINAL_ANSWER: {final_result}"


```

---

✅ Example 4: FURTHER_PROCESSING_REQUIRED: Summarize a document or webpage or similar ex
ample where you need information to take next action:
```python
async def solve():
    # FUNCTION_CALL: 1
    """Return clean webpage content. Usage: input={"input": {"url": "https://example.com"}} result = await mcp.call_tool('extract_webpage', input)"""
    input = {"url": "https://www.f1.com"}
    result = await mcp.call_tool(extract_webpage, input)  # from mcp_server_2

    # FURTHER_PROCESSING_REQUIRED
    return f"FURTHER_PROCESSING_REQUIRED: {result}"

```

✅ Example 5: Summarize fetched content
```python
async def solve():
    # FUNCTION_CALL: 1
    """Search documents to get relevant extracts. Usage: input={"input": {"query": "DLF apartment Capbridge"}} result = await mcp.call_tool('search_stored_documents', input)"""
    input = {"input": {"query": "DLF apartment Capbridge"}}
    result = await mcp.call_tool('search_stored_documents', input)

    # FURTHER_PROCESSING_REQUIRED
    return f"FURTHER_PROCESSING_REQUIRED: {result}"

```

💡 Tips:

If the task can be solved by one tool, stop after that.

You must return the result immediately using 'FINAL_ANSWER:' if you got the result for 
the user's task, or 'FURTHER_PROCESSING_REQUIRED:'.

Some times you WILL need to further process the results, like after looking at document, search or webpage parsed, summarizing it. Use 'FURTHER_PROCESSING_REQUIRED:' in those cases.
Use chaining only if necessary, but never plan more than 1 tool call.

"""
[11:09:19] [plan] LLM output: ```python
async def solve():
    """Add two numbers. Usage: input={"input": {"a": 1, "b": 2}} result = await mcp.call_tool('add', input)"""
    input = {"input": {"a": 2, "b": 2}}
    result = await mcp.call_tool('add', input)
    return f"FINAL_ANSWER: {result.content[0].text}"
```
[plan] async def solve():
    """Add two numbers. Usage: input={"input": {"a": 1, "b": 2}} result = await mcp.call_tool('add', input)"""
    input = {"input": {"a": 2, "b": 2}}
    result = await mcp.call_tool('add', input)
    return f"FINAL_ANSWER: {result.content[0].text}"
[loop] Detected solve() plan — running sandboxed...
[action] 🔍 Entered run_python_sandbox()

Result:
 FINAL_ANSWER: {
  "result": 4
}

💡 Final Answer: {
  "result": 4
}
INFO:modules.history:Added new entry for session 9af13ada-e4a2-4172-85b6-498754646739


