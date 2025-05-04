tools = [
    {
        "type": "function",
        "name": "installPkg",
        "description": "주어진 패키지 리스트를 프로젝트에 설치합니다.",
        "parameters": {
            "type": "object",
            "properties": {
                "packageList": {
                    "type": "array",
                    "items": { "type": "string" },
                    "description": "설치할 패키지 이름 리스트"
                }
            },
            "required": ["packageList"],
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

    ## arrays
    {
    "type": "function",
    "name": "sortArray",
    "description": "주어진 정수 배열을 오름차순으로 정렬합니다.",
    "parameters": {
      "type": "object",
      "properties": {
        "array": {
          "type": "array",
          "items": { "type": "integer" },
          "description": "정렬할 정수 배열"
        }
      },
      "required": ["array"],
      "additionalProperties": False
    }
  },
  {
    "type": "function",
    "name": "copyArray",
    "description": "지정된 길이로 배열을 복사합니다. (Arrays.copyOf)",
    "parameters": {
      "type": "object",
      "properties": {
        "array": {
          "type": "array",
          "items": { "type": "integer" },
          "description": "복사할 원본 배열"
        },
        "newLength": {
          "type": "integer",
          "description": "복사할 배열의 새로운 길이"
        }
      },
      "required": ["array", "newLength"],
      "additionalProperties": False
    }
  },
  {
    "type": "function",
    "name": "copyArrayRange",
    "description": "지정된 시작~끝 범위의 배열을 복사합니다. (Arrays.copyOfRange)",
    "parameters": {
      "type": "object",
      "properties": {
        "array": {
          "type": "array",
          "items": { "type": "integer" },
          "description": "복사할 원본 배열"
        },
        "from": {
          "type": "integer",
          "description": "시작 인덱스 (포함)"
        },
        "to": {
          "type": "integer",
          "description": "끝 인덱스 (제외)"
        }
      },
      "required": ["array", "from", "to"],
      "additionalProperties": False
    }
  },
  {
    "type": "function",
    "name": "fillArray",
    "description": "배열의 모든 요소를 지정된 값으로 채웁니다. (Arrays.fill)",
    "parameters": {
      "type": "object",
      "properties": {
        "array": {
          "type": "array",
          "items": { "type": "integer" },
          "description": "채울 배열"
        },
        "value": {
          "type": "integer",
          "description": "채울 값"
        }
      },
      "required": ["array", "value"],
      "additionalProperties": False
    }
  },
  {
    "type": "function",
    "name": "equalsArrays",
    "description": "두 배열이 같은지 비교합니다. (Arrays.equals)",
    "parameters": {
      "type": "object",
      "properties": {
        "array1": {
          "type": "array",
          "items": { "type": "integer" },
          "description": "첫 번째 배열"
        },
        "array2": {
          "type": "array",
          "items": { "type": "integer" },
          "description": "두 번째 배열"
        }
      },
      "required": ["array1", "array2"],
      "additionalProperties": False
    }
  },
  {
    "type": "function",
    "name": "deepEqualsArrays",
    "description": "다차원 배열이 동일한지 비교합니다. (Arrays.deepEquals)",
    "parameters": {
      "type": "object",
      "properties": {
        "array1": {
          "type": "array",
          "items": { "type": "array", "items": { "type": "integer" } },
          "description": "첫 번째 다차원 배열"
        },
        "array2": {
          "type": "array",
          "items": { "type": "array", "items": { "type": "integer" } },
          "description": "두 번째 다차원 배열"
        }
      },
      "required": ["array1", "array2"],
      "additionalProperties": False
    }
  },
  {
    "type": "function",
    "name": "arrayToString",
    "description": "배열을 문자열로 변환합니다. (Arrays.toString)",
    "parameters": {
      "type": "object",
      "properties": {
        "array": {
          "type": "array",
          "items": { "type": "integer" },
          "description": "변환할 배열"
        }
      },
      "required": ["array"],
      "additionalProperties": False
    }
  },
  {
    "type": "function",
    "name": "deepArrayToString",
    "description": "다차원 배열을 문자열로 변환합니다. (Arrays.deepToString)",
    "parameters": {
      "type": "object",
      "properties": {
        "array": {
          "type": "array",
          "items": { "type": "array", "items": { "type": "integer" } },
          "description": "변환할 다차원 배열"
        }
      },
      "required": ["array"],
      "additionalProperties": False
    }
  },
  {
    "type": "function",
    "name": "binarySearchArray",
    "description": "배열에서 주어진 값을 이진 검색합니다. (Arrays.binarySearch)",
    "parameters": {
      "type": "object",
      "properties": {
        "array": {
          "type": "array",
          "items": { "type": "integer" },
          "description": "검색할 정렬된 배열"
        },
        "target": {
          "type": "integer",
          "description": "찾을 값"
        }
      },
      "required": ["array", "target"],
      "additionalProperties": False
    }
  },
  {
    "type": "function",
    "name": "arrayToList",
    "description": "배열을 List로 변환합니다. (Arrays.asList)",
    "parameters": {
      "type": "object",
      "properties": {
        "array": {
          "type": "array",
          "items": { "type": "string" },
          "description": "변환할 문자열 배열"
        }
      },
      "required": ["array"],
      "additionalProperties": False
    }
  }
]
