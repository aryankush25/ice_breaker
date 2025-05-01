from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain_core.agents import create_react_agent, AgentExecutor


def lookup(name: str) -> str:
    return ""
