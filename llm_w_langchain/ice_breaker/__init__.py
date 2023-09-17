import re

from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI

from ice_breaker.linkedin import linkedin_lookup_agent
from ice_breaker.linkedin_scraper import scrape_linkedin_profile


def main():
    summary_template = """
        Given the LinkedIn information {information} about a person from I want you to create:
        1. Show a summary
        2. Two interesting facts about them
    """  # noqa: E501

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    url_pattern = r"https?://\S+|www\.\S+"

    linkedin_profile_url = linkedin_lookup_agent(name="Eden Marco")
    urls = re.findall(url_pattern, linkedin_profile_url)

    print(linkedin_profile_url)
    print(urls[0])

    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=urls[0])

    print(chain.run(information=linkedin_data))
