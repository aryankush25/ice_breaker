from dotenv import load_dotenv
# import os

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
# from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from third_parties.linkedin import scrape_linkedin_profile

if __name__ == "__main__":
    load_dotenv()
    print("Hello LangChain!")

    summary_template = """
        given the LinkedIn information {information} about a person from I want you to create:
        1. a short summary
        2. two interesting facts about them
    """

    input_variables = ["information"]

    summary_prompt_template = PromptTemplate(
        input_variables=input_variables, template=summary_template
    )

    # llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    llm = ChatOllama(model="mistral")

    chain = summary_prompt_template | llm | StrOutputParser()

    information = scrape_linkedin_profile("https://www.linkedin.com/in/aryankush25")

    print('information')
    print(information)

    res = chain.invoke({"information": information})

    print('result')
    print(res)
