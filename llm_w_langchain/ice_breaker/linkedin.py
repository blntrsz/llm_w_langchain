from langchain import PromptTemplate
from langchain.agents import AgentType, Tool, initialize_agent
from langchain.chat_models import ChatOpenAI

from ice_breaker.tools import get_profile_url


def linkedin_lookup_agent(name: str) -> str:
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

    template = """
        given the full name {name_of_person} I want you to get me alink to
        their LinkedIn profile page. The answer should only contain the URL
        without any description
    """

    tools_for_agent = [
        Tool(
            name="Crawl Google for LinkedIn profile page",
            func=get_profile_url,
            description="""
                useful when you want to get the URL of a person LinkedIn page
            """,
        )
    ]

    agent = initialize_agent(
        llm=llm,
        tools=tools_for_agent,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        vebose=True,
    )
    prompt_template = PromptTemplate(
        input_variables=["name_of_person"],
        template=template,
    )

    linkedin_profile_url = agent.run(prompt_template.format_prompt(name_of_person=name))

    return linkedin_profile_url
