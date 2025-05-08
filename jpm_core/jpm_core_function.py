
import subprocess
import json

#tool_call을 받아서 파싱한 후 jpm 호출
def jpm_caller(tool_call):
    fn_name=tool_call.name
    args = json.loads(tool_call.arguments)
    print("함수명:" + fn_name)

    #  함수명에 따라 jpm-core 호출해야 함.
    match fn_name:
        case "install":

            ## to be implemented
            # organization:name으로 붙여.
            org_and_name=args["organization"]+":"+args["name"]
            result = subprocess.run(
                ['java', '-jar', 'C:\\Users\\PC\\Desktop\\Python\\jpm-nlp\\jpm_core\\jpm.jar', 'install', org_and_name],
                capture_output=True,
                text=True
            )

            # print(result.stdout)

            # print("STDERR:")
            # print(result.stderr)
            # 추후에 예외처리 필요.


            return result.stdout
        case "delete":
            org_and_name=args["organization"]+":"+args["name"]

            return "패키지를 삭제했습니다."
        
        case "update":
            org_and_name=args["organization"]+":"+args["name"]

            return "패키지를 업데이트했습니다."
        
        case "list":

            return '''
                    [org.junit:junit-bom:5.10.0, org.junit.jupiter:junit-jupiter]
                    '''
        case "build"|"init"|"test"|"run":

            return no_args_jpm(fn_name)
        
       
        

    return "잘못된 행동입니다.."    


# 인자가 없는(init, build 등) jpm 호출 프로세스
def no_args_jpm(fn_name):
    result = subprocess.run(
                ['java', '-jar', 'C:\\Users\\PC\\Desktop\\Python\\jpm-nlp\\jpm_core\\jpm.jar', fn_name,],
                capture_output=True,
                text=True
            )

            # print(result.stdout)

            # print("STDERR:")
            # print(result.stderr)
            # 추후에 예외처리 필요.


    return result.stdout