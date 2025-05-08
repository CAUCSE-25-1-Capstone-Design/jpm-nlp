tools = [
        {
      "type": "function",
      "name": "installPkg",
      "description": "하나의 패키지를 프로젝트에 설치합니다.",
      "parameters": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "패키지 이름"
          },
          "organization": {
            "type": "string",
            "description": "패키지를 배포한 기관명"
          }
        },
        "required": ["name", "organization"],
        "additionalProperties": False
      }
    },

    {
        "type": "function",
        "name": "deletePkg",
        "description": "주어진 패키지 리스트를 프로젝트에서 삭제합니다.",
        "parameters": {
            "type": "object",
            "properties": {
                "packageList": {
                    "type": "array",
                    "items": { "type": "string" },
                    "description": "삭제할 패키지 이름 리스트"
                }
            },
            "required": ["packageList"],
            "additionalProperties": False
        }
    },
    {
        "type": "function",
        "name": "updatePkg",
        "description": "주어진 패키지 리스트를 업데이트합니다.",
        "parameters": {
            "type": "object",
            "properties": {
                "packageList": {
                    "type": "array",
                    "items": { "type": "string" },
                    "description": "업데이트할 패키지 이름 리스트"
                }
            },
            "required": ["packageList"],
            "additionalProperties": False
        }
    },
    {
        "type": "function",
        "name": "listPkg",
        "description": "현재 프로젝트에 설치된 모든 패키지를 조회합니다.",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": [],
            "additionalProperties": False
        }
    },
    {
        "type": "function",
        "name": "build",
        "description": "프로젝트를 빌드합니다.",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": [],
            "additionalProperties": False
        }
    },
    {
        "type": "function",
        "name": "init",
        "description": "프로젝트를 초기화합니다.",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": [],
            "additionalProperties": False
        }
    },
    {
        "type": "function",
        "name": "test",
        "description": "프로젝트 테스트를 수행합니다.",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": [],
            "additionalProperties": False
        }
    },
    {
        "type": "function",
        "name": "run",
        "description": "프로젝트를 실행합니다.",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": [],
            "additionalProperties": False
        }
    },

   
]
