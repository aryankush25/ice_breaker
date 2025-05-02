from dotenv import load_dotenv

load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from tools.tools import get_profile_url_tavily


def lookup(name: str) -> str:
    llm = ChatOpenAI(temperature=0, model="gpt-4o-mini")
    template = """
    given the full name {name} I want you to return the linkedin profile url. Your answer should be a valid url and should be in the format https://www.linkedin.com/in/aryankush25.
    """
    prompt_template = PromptTemplate(input_variables=["name"], template=template)
    tools_for_agent = [
        Tool(
            name="Crawl Google 4 linkedin profile page",
            func=get_profile_url_tavily,
            description="Use this tool to lookup the linkedin profile url of a person.",
        )
    ]
    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent)

    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name=name)}
    )

    linkedin_profile_url = result["output"]

    return linkedin_profile_url


if __name__ == "__main__":
    linkedin_url = lookup("Aryan Agarwal")
    print(linkedin_url)
