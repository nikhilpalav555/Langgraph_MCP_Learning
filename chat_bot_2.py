from langchain_ollama import ChatOllama
import os
from langchain_core.tools import tool
from typing import Annotated, TypedDict
from langgraph.graph.message import add_messages
from langgraph.graph.state import START,END, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_tavily import TavilySearch
from langgraph.checkpoint.memory import MemorySaver
from langgraph.types import Command, interrupt
from dotenv import load_dotenv

load_dotenv()


memory=MemorySaver()

config={"configurable":{"thread_id":"1"}}

llm=ChatOllama(model="qwen3.5:0.8b", temperature=0.0)


class State(TypedDict):
    messages:Annotated[list,add_messages]
    
    
graph_builder=StateGraph(State)

@tool
def human_assistance(query:str):
    """Request Assistance from human"""
    human_response=interrupt({"query":query})
    return human_response["data"]

tool=TavilySearch(max_results=2)
tools=[tool, human_assistance]

llm_bind_tools=llm.bind_tools(tools)

def chatbot(state:State):
    message= llm_bind_tools.invoke(state["messages"])
    
    return {"messages":[message]}

graph_builder.add_node("chatbot",chatbot)

tools_node=ToolNode(tools=tools)
graph_builder.add_node("tools", tools_node)

graph_builder.add_conditional_edges(
    "chatbot",
    tools_condition)

graph_builder.add_edge("tools", "chatbot")
graph_builder.add_edge(START, "chatbot")

graph=graph_builder.compile(checkpointer=memory)


user_input="I need some expert guidence and assistance for building an AI agent. Could you request assistance for me? "

events=graph.stream(
    {"messages":user_input},
    config,
    stream_mode="values"
)

for event in events:
    if "messages" in event:
        event["messages"][-1].pretty_print()
        
        
human_response=("We the experts are here to help! We would recommend to check your langgraph to build your agent"
"its much more reliable and extensible that simple autonomous agent")

human_command=Command(resume={"data":human_response})


events=graph.stream(human_command, config, stream_mode="values")
for event in events:
    if "messages" in event:
        event["messages"][-1].pretty_print()
        
    
