from langchain_groq import ChatGroq
from dotenv import load_dotenv
#! initialize agents
from langchain.agents import initialize_agent, AgentType
from langchain_community.tools import TavilySearchResults




load_dotenv()


llm = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct")

search_tool=TavilySearchResults(search_depth="basic")

# ! creating agent takes few parameters like tools, llm , agent_type, verbose , etc....!!!
#todo:  ReAct patters is a combination of Think, Action and Observation

agent =initialize_agent(tools=[search_tool], llm=llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

agent.invoke({"input": "present situation between India & pakistan ? "})