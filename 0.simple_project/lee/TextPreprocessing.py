import os, glob
import re

def sample_line(directory, filename):
    cur_filename = filename.split("/")[-1]
    file_n = directory + '/result/'+"(result)"+cur_filename
    file = open(file_n, 'a+t')
    original = open(filename)

    p = original.readlines()

    for i in range(len(p)):
        line = p[i].split('.')
        line = list(map(lambda x: x.strip(), line))
        line = list(filter(lambda x: x != '', line))
        for new_line in line[:-3]:
            new_line += "."
            new_line = re.sub('// flash 오류를 우회하기 위한 함수 추가','',new_line)
            new_line = re.sub('function _flash_removeCallback','',new_line)
            new_line = re.sub('\(.*\)', "", new_line)
            new_line = re.sub('\[.*\]', '', new_line)
            new_line = re.sub('\{.*\}', '', new_line)
            new_line = re.sub("사진.*", '', new_line)
            new_line = re.sub("기자.*", '', new_line)
            new_line = re.sub("▶.*","",new_line)
            new_line = re.sub("【.*】","",new_line)
            if new_line != '':
                file.write(new_line + "\n")


if __name__ == '__main__':
    directory = "/Users/seungeonlee/Desktop/NLP/sample"

    filelist = glob.glob("/Users/seungeonlee/Desktop/NLP/sample/*.txt")
    for i in filelist:
        if os.path.isfile(i):
            sample_line(directory, i)

# [^가-힝0-9a-zA-Z\\s]d