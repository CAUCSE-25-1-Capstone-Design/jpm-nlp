#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


from openai import OpenAI
import os
from getpass import getpass


# API 키를 환경 변수에 저장
os.environ['OPENAI_API_KEY'] = "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"

def create_chat_completion(system_input, user_input, model="gpt-4o-mini", temperature=1.15, max_tokens=150):
    try:
        # 메시지 목록을 자동으로 생성해요
        messages = [
            {"role": "system", "content": system_input},
            {"role": "user", "content": user_input}
        ]

        response = OpenAI().chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens  # 최대 토큰 수를 지정해요
        )
        # 생성된 응답을 반환해요
        return response
    except Exception as e:
        return f"Error: {str(e)}"
    


# 메시지 입력
system_input = """
너는 사용자의 자연어 명령을 분석하여, 해당 작업을 수행하는 Java 코드를 생성하는 도우미야.

다음은 사용 가능한 명령과 대응되는 Java 메소드다:

기본 함수 매핑:
- 의존성 추가: installPkg(List<String> packageList)
- 의존성 삭제: deletePkg(List<String> packageList)
- 의존성 업데이트: updatePkg(List<String> packageList)
- 의존성 조회: listPkg()
- 프로젝트 빌드: build()
- 프로젝트 초기화: init()
- 프로젝트 테스트: test()
- 프로젝트 실행: run()

규칙:
- 사용자의 명령을 분석하여 위 함수 중 어떤 것을 호출해야 하는지 판단하고
- 해당 함수들을 조합하여 **Java 코드**로 변환해
- 반드시 `Main.java`에 들어갈 수 있는 형태로 작성해
- 필요하다면 여러 줄로 호출해도 돼
- 함수 외의 설명은 쓰지 마. **오직 코드만 출력해**

예:
사용자: 모든 패키지를 업데이트해줘
→ 출력:
```java
updatePkg(List.of("all"));
"""

user_input = '''
설치된 패키지의 개수를 알려줘?
'''
# API 호출 및 결과 출력
responses = create_chat_completion(system_input, user_input)
print(responses.choices[0].message.content)

