import glob
import re
import os

path = '/Users/kohhyunji/PycharmProjects/PythonTest/sample/*.txt'
files = glob.glob(path)

for file in files:
    f = open(file,'r')
    # with open(file, 'r') as files:    # hello.txt 파일을 읽기 모드(r)로 열기
    line = None    # 변수 line을 None으로 초기화
    cnt = 0
    sent = []


    while True:
        cnt += 1
        line = f.readline()

        if not line: break

        if cnt == 1 :
            print(line)
            continue

        # 날짜 삭제
        pattern = '([0-9]+.[0-9]+.[0-9]+/[가-힣0-9a-zA-Z]+)'
        res = re.sub(pattern, '', line)

        # email 삭제
        pattern = '([a-zA-Z0-9_+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)'
        res = re.sub(pattern, '', res)

        # []내용 삭제
        res = re.sub('\[[^[]*\]', '', res)

        # ▶내용 삭제
        res = re.sub('\▶[^\n]*', '', res)

        # res = re.split("(?<=[\.?!])\s+|(?<=[\.?!])[가-힣a-zA-Z]+|(?<=[\.?!])[^\w]", res)
        res = re.split("(?<=[\.?!])", res)

        for text in res :
            if text != '\n'  :
                text.lstrip()  ###왜 안될까?
                sent.append(text + '\n')
                ##특수문자로 시작하고 \n으로 끝나는 문장 삭제하고싶음

    f.close()

    with open('/Users/kohhyunji/PycharmProjects/PythonTest/sample_result/{}.txt'.format(os.path.basename(file)), 'w') as re_file:  # hello.txt 파일을 쓰기 모드(w)로 열기
        # 마지막 두줄 삭제
        for i in res[:-2] :
            re_file.writelines(i +'\n')
    re_file.close()