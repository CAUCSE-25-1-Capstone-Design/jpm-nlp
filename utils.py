# print + flush 작업 필요(실시간 반응 위해)

import time
import tiktoken
import sys

#encoding = tiktoken.encoding_for_model("gpt-4")


def print_debug(string):
   
    print("[Debug:"+ str(time.strftime(' %X'))+"] " + str(string))

def print_ui(string):
    print(string, flush=True)


def read_last_n_chars(file_path="log.txt", n_chars=2500):
    with open(file_path, 'rb') as f:
        f.seek(0, 2)  # 파일 끝으로 이동
        file_size = f.tell()

        # 읽을 만큼 뒤로 가기
        seek_pos = max(file_size - n_chars, 0)
        f.seek(seek_pos)
        data = f.read().decode(errors='ignore')

        #debug_print(data)
        #debug_print("input token length: " + len(encoding.encode(data)))

        return data
    

def read_all():
    f= open("log.txt", "r")

    r=f.read()



    f.close

    return r

# 지금까지의 대화 로그를 저장
# 시간, 날짜도 같이 저장하기
def save(string):
    f= open("log.txt","a")

    f.write("["+str(time.strftime('%x %X'))+"] "+str(string)+"\n")
   

    f.close()

def save_gpt(string):
    save("GPT: "+ str(string))

def save_user(string):
    save("USER: "+ str(string))