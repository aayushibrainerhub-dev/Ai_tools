from app.weather import get_current_weather
from app.config import GROK_API_CLOUD_KEY


tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_weather",
            "description": "Get the current weather for a given city",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                    }
                },
                "required": ["city"],
            },
        },
    }
]


async def execute_tool(name, arguments):
    if name == "get_current_weather":
        return await get_current_weather(arguments.get("city"))
    return {}


def build_langchain_agent():
    try:
        from langchain.agents import AgentExecutor, create_tool_calling_agent
        from langchain.tools import tool
        from langchain_openai import ChatOpenAI
    except ImportError:
        return None

    @tool
    async def weather_tool(city: str) -> dict:
        """Get the current weather for a given city."""
        return await get_current_weather(city)

    llm = ChatOpenAI(
        model="llama-3.3-70b-versatile",
        api_key=GROK_API_CLOUD_KEY,
        base_url="https://api.groq.com/openai/v1",
    )

    agent = create_tool_calling_agent(llm, [weather_tool])
    return AgentExecutor(agent=agent, tools=[weather_tool], verbose=True)