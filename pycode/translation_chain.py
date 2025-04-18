from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt_template = ChatPromptTemplate.from_messages([
    ('system', "Translate the following into {language}:"),
    ('user', '{text}')
])
parser = StrOutputParser()

def get_translation_chain(model):
    return prompt_template | model | parser
