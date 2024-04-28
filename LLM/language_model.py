from dotenv import load_dotenv
load_dotenv()

from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_core.messages import HumanMessage, SystemMessage

import warnings
warnings.filterwarnings("ignore")

def get_model_list():
    return ChatNVIDIA.get_available_models()

def get_llm(model):
    llm=ChatNVIDIA(model=model)
    return llm

def get_llm_response(human_mesage,model="ai-llama3-70b"):
    messages=[
        SystemMessage(content="You are language translater"),
        HumanMessage(content=human_mesage)
    ]
    llm=get_llm(model)
    return llm.invoke(messages).content

output_language="Hindi"
text="Who the hell are you ?"
human_mesage=f"""
        Given the input sentence and output language below:
        Input Sentence : {text}
        Output Language : {output_language}
        
        Please translate the input sentence into {output_language} without giving any explanation.
        
        Also write a story in the tranlated language.
        Translation: 
    """


# result=get_llm_response(human_mesage)
# print(result)

# print(get_model_list())

