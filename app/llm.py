import json
from openai import AsyncOpenAI
from app.config import GROK_API_CLOUD_KEY
from app.tools import tools, execute_tool

client = AsyncOpenAI(
    api_key=GROK_API_CLOUD_KEY,
    base_url="https://api.groq.com/openai/v1"
)


async def chat(message):
    messages = [
        {
            "role": "user",
            "content": message
        }
    ]

    response = await client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        tools=tools,
    )
    assistant = response.choices[0].message

    if assistant.tool_calls:
        tool_call = assistant.tool_calls[0]
        args = json.loads(tool_call.function.arguments)
        result = await execute_tool(
            tool_call.function.name,
            args,
        )

        messages.append(assistant.model_dump(exclude_none=True))
        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": json.dumps(result),
        })
        final = await client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
        )
        return final.choices[0].message.content

    return assistant.content

