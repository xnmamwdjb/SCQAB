from openai import OpenAI
import time
import traceback

client=OpenAI()

def generate(prompt,model="gpt-4-turbo-0125",max_tokens=2048,temperature=0):
    '''
        prompt:给模型的输入
        返回模型输出文本
    '''
    messages = [{"role":"user","content":prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=max_tokens,
        temperature=temperature,
    )
    return response.choices[0].message.content

def make_sure_generate(prompt,model="gpt-3.5-turbo-0125",max_tokens=2048,temperature=0):
    '''
        prompt:给模型的输入
        返回模型输出文本
    '''
    while True:
        try:
            res=generate(prompt,model,max_tokens,temperature)
            return res
        except:
            traceback.print_exc()
            time.sleep(6)