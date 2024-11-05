from yandex_chain import YandexLLM, YandexGPTModel
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=f"{os.path.join(os.path.dirname(__file__), '.env')}")
print(f"{os.path.join(os.path.dirname(__file__), '.env')}")

YGPT_folder_ip = os.getenv("YGPT_folder_ip")
YGPT_api_key = os.getenv("YGPT_api_key")

def YandexGPT(context, question):

    llm = YandexLLM(folder_id=YGPT_folder_ip,
                api_key=YGPT_api_key,
                model=YandexGPTModel.Pro)

 
    def replace_non_breaking_spaces(text):
        return text.replace('\xa0', ' ')

    def replace_underscore(text):
        return text.replace('_', ' ')

    def join_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)
    
    context_processed = replace_underscore(replace_non_breaking_spaces(join_docs(context)))
    
    
    promt = f"""
    Ты юридический консультант.
    Посмотри на текст ниже и ответь на вопрос, используя информацию из этого текста.
    Если текст не относится к вопросу, составь ответ не учитывая этот текст.
    Если в тексте указана статья, в ответе в самом начале укажи это.
    Ответ составь в формате простого текста, не используя markdown
    Текст:
    -----
    {context_processed}
    -----
    Вопрос:
    {question}"""
    
    answer = llm.invoke(promt)
    
    print('----Ответ----')
    print(answer)
    print('-------------')

    return answer