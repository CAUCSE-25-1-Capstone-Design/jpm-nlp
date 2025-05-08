
#tool_call을 받아서 파싱한 후 jpm 호출
def jpm_caller(tool_call):
    name=tool_call.name
    print("함수명:" + name)

    #  함수명에 따라 jpm-core 호출해야 함.
    match name:
        case "installPkg":

            ## to be implemented

            return "패키지를 설치하였습니다."
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
