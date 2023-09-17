from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI

information = """
    Elon Reeve Musk (/ˈiːlɒn/ EE-lon; born June 28, 1971) is a business
    magnateand investor. Musk is the founder, chairman, CEO and chief
    technology officer of SpaceX; angel investor, CEO, product architect and
    former chairman of Tesla, Inc.; owner, chairman and CTO of X Corp.; founder
    of the Boring Company; co-founder of Neuralink and OpenAI; and president of
    the Musk Foundation. He is the wealthiest person in the world, with an
    estimated net worth of US$226 billion as of September 2023, according to
    the Bloomberg Billionaires Index, and $249 billion according to Forbes,
    primarily from his ownership stakes in both Tesla and SpaceX.[4][5][6]
"""


def main():
    summary_template = """
        Given the following information about a persion: {information}.

        Do the following:
        1. Describe the person in one sentence
        2. List 2 interesting fact about the person
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    print(chain.run(information=information))
