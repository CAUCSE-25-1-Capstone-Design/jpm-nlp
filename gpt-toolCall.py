from openai import OpenAI
import os
import tools, arrays_tool

os.environ['OPENAI_API_KEY'] = "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"

client = OpenAI()

tools=tools.tools

input_messages=[{"role": "system", "content": "너는 사용자의 자연어 명령을 받아 알맞은 java 함수(tool)를 호출하는 시스템이다. 이외의 질문은 무시해."},
        {"role": "user", "content": '''
        배열명 array를 정렬해.
        '''}]
    

response = client.responses.create(
    model="gpt-4.1",
    input=input_messages,
    tools=tools,
    tool_choice="auto",
    temperature=0
)

print(response.output[0])