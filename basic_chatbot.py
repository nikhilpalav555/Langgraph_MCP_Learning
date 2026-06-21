from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from langchain_tavily import TavilySearch
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.memory import MemorySaver

memory=MemorySaver()

load_dotenv()


# config={"configurable":{"thread_id":"1"}}


class State(TypedDict):
    messages:Annotated[list, add_messages]
    
    
graphbuilder=StateGraph(State)


llm=ChatOllama(model="qwen3.5:0.8b", temperature=0.0)

def chatbot(state:State):
    return {"messages":[llm.invoke(state["messages"])]}

graphbuilder.add_node("llmchatbot",chatbot)
graphbuilder.add_edge(START, "llmchatbot")
graphbuilder.add_edge("llmchatbot", END)

graph=graphbuilder.compile()

# response=graph.invoke({"messages":"Hi"})
# print(response["messages"][-1].content)

for event in graph.stream({"messages":"Hii how are you"}):
    for value in event.values():
        print(value["messages"][-1].content)
        
tool=TavilySearch(max_results=2)
# print(tool.invoke("What is langgraph"))

def multiply(a:int, b:int)->int:
    """Multiply a and b.

    Args:
        a (int): First integer.
        b (int): Second integer.

    Returns:
        int: Multiplied result.
    """
    return a * b
    
tools=[tool,multiply]


llm_with_tools=llm.bind_tools(tools, tool_choice="required")
# print(llm_with_tools)


# def tool_calling_llm(state:State):
#     return {"messages":[llm_with_tools.invoke(state["messages"])]}

# buildergraph=StateGraph(State)

# ##crearing node 
# buildergraph.add_node("tool_calling_llm", tool_calling_llm)
# buildergraph.add_node("tools", ToolNode(tools))

# ##creating edges
# buildergraph.add_edge(START,"tool_calling_llm")
# buildergraph.add_conditional_edges(
#     "tool_calling_llm",
#     tools_condition
    
# )

# buildergraph.add_edge("tools", END)

# builder=buildergraph.compile()

# # print(builder)

# # response=builder.invoke({"messages":"What is the recent ai news"})

# # print(response["messages"])

# response2=builder.invoke({"messages":"What is 2 multiply by 3"})

# print(response2["messages"])

###### Agentic AI LLM
tool=TavilySearch(max_results=2)
# print(tool.invoke("What is langgraph"))

def multiply(a:int, b:int)->int:
    """Multiply a and b.

    Args:
        a (int): First integer.
        b (int): Second integer.

    Returns:
        int: Multiplied result.
    """
    return a * b
    
tools=[tool,multiply]


llm_with_tools=llm.bind_tools(tools, tool_choice="auto")
# print(llm_with_tools)


def tool_calling_llm(state:State):
    return {"messages":[llm_with_tools.invoke(state["messages"])]}

buildergraph=StateGraph(State)

##crearing node 
buildergraph.add_node("tool_calling_llm", tool_calling_llm)
buildergraph.add_node("tools", ToolNode(tools))

##creating edges
buildergraph.add_edge(START,"tool_calling_llm")
buildergraph.add_conditional_edges(
    "tool_calling_llm",
    tools_condition
    
)

buildergraph.add_edge("tools", "tool_calling_llm")

builder=buildergraph.compile(checkpointer=memory)

# print(builder)

# response=builder.invoke({"messages":"What is the recent ai news"})

# print(response["messages"])

# response2=builder.invoke({"messages":"What is the latest AI news and What is 2 multiply by 3"})
# for m in response2["messages"]:
#     m.pretty_print()

# print(response2["messages"])



# response=builder.invoke({"messages":"Hello My name is Nikhil"}, config=config)
# print(response)


# ##Adding Memory in Agentic Graph 

# response2=builder.invoke({"messages":"Hey what is my name"}, config=config)

# print(response2["messages"])

# response_2=builder.invoke({"messages":"Do you remember my name?"}, config= config)

# print(response_2["messages"][-1].content)

# ##Streaming

def superbot(state:State):
    return {"messages":llm.invoke(state["messages"])}


new_graph=StateGraph(State)

#Nodes
new_graph.add_node("superbot", superbot)

##Edges

new_graph.add_edge(START, "superbot")
new_graph.add_edge("superbot", END)

new_graph_builder=new_graph.compile(checkpointer=memory)

config={"configurable":{"thread_id":"1"}}

response_3=new_graph_builder.invoke({"messages":"Hello My name is Nikhil and i like playing cricket"}, config = config)

(response_3["messages"][-1].content)


config={"configurable":{"thread_id":"3"}}

# for chunk in new_graph_builder.stream({"messages":"My name is Nikhil and i Like playing Cricket"}, config, stream_mode="updates"):
#     print(chunk)
    
    
for chunk in new_graph_builder.stream({"messages":"My name is Nikhil and i Like playing Cricket"}, config, stream_mode="values"):
    chunk
    
    
##Human in the loop

    
        
        

