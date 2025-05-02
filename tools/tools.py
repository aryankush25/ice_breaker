from langchain_community.tools.tavily_search import TavilySearchResults


def get_profile_url_tavily(name: str) -> str:
    """
    Searches for the linkedin profile url of a person using Tavily.
    """
    search = TavilySearchResults()
    res = search.run(f"{name}")
    return res
