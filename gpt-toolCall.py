import jpm_core.jpm_core_function
from openai import OpenAI
import os
import tools, arrays_tool
import json
from jpm_core import jpm_core_function
import sys


myTools=tools.tools
def query_process(query):
#나중에 환경변수로 처리하기
    os.environ['OPENAI_API_KEY'] = "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"

    client = OpenAI()

    tools=myTools

    input_messages=[{"role": "system", 
                     "content": '''
                    너는 사용자의 자연어 명령을 받아 알맞은 java 함수(tool)를 호출하는 시스템이다. 
                    만약 패키지명이 완전하지 않다면 maven central에서 가장 유사한 패키지명으로 검색해.
                    또한 패키지를 설치할 때 패키지를 배포한 기관명(organization)을 maven central에서 검색해.
                    이외의 질문은 무시해.
                    '''},
                    {"role": "user", 
                    "content": query}
                    ]
        
        ## 기관명이랑 버전도 가져와야 함.

    response = client.responses.create(
        model="gpt-4.1",
        input=input_messages,
        tools=tools,
        tool_choice="auto",
        temperature=0
    )

    print(response.output)

    for tool_call in response.output:
        #print(tool_call)
        args=json.loads(tool_call.arguments)
        print(args)
        
        result=jpm_core_function.jpm_caller(tool_call)

        print(result)

        input_messages.append(tool_call)
        input_messages.append({
            "type": "function_call_output",
            "call_id": tool_call.call_id,
            "output": str(result)
        })


        response_2 = client.responses.create(
        model="gpt-4.1",
        input=input_messages,
        tools=tools,
            )
        
        return response_2.output_text


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("No input provided")
        sys.exit(1)

    query = sys.argv[1]
    result = query_process(query)
    print(result)