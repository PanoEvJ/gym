import os
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.agents import load_tools, initialize_agent, AgentType
import streamlit as st

load_dotenv()

llm = OpenAI(temperature=0, streaming=True, openai_api_key=os.getenv("OPENAI_API_KEY"))
tools = load_tools(["ddg-search"])
agent = initialize_agent(agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, llm=llm, tools=tools)


print("Hello world!")