
import subprocess
import json

#tool_call을 받아서 파싱한 후 jpm 호출
def jpm_caller(tool_call):
    name=tool_call.name
    args = json.loads(tool_call.arguments)
    print("함수명:" + name)

    #  함수명에 따라 jpm-core 호출해야 함.
    match name:
        case "installPkg":

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
        case "deletePkg":
            
            return "패키지를 삭제했습니다."
        
        case "updatePkg":

            return
        
        case "listPkg":

            return
        case "build":

            return
        
        case "init":

            return
        
        case "test":

            return
        
        case "run":

            return
        

    return "잘못된 행동입니다.."    
