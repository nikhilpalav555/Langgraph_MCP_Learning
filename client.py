from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain.agents import create_agent
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
import asyncio

load_dotenv()

async def main():
    client=MultiServerMCPClient(
        {
            "math":{
                "command":"python",
            "args":["mathserver.py"], 
            "transport":"stdio",
            },
            
            "weather":{
                "url":"http://127.0.0.1:8000/mcp",
                "transport":"streamable-http",
            }
        }
    )
    
    tools=await client.get_tools()
    model=ChatOllama(model="qwen3.5:0.8b ")
    agent=create_react_agent(model, tools)
    
    math_response=await agent.ainvoke( {
        "messages": [
            {"role": "user", "content": "What is (3+5) x 12"}
        ]
    }
)
    
    weather_response= await agent.ainvoke({
        "messages":[{"role":"user", "content":"What is the weather in india"}]
    })
    
    print("Math response",math_response["messages"][-1].content)
    
    print("Weather response,",weather_response["messages"][-1].content)
    
asyncio.run(main())
    

    
    

    

    
