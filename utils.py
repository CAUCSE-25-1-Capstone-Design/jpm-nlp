# print + flush 작업 필요(실시간 반응 위해)

import time

def debug_print(string):
   
    print("[Debug:"+ str(time.strftime(' %X'))+"] " + str(string))


