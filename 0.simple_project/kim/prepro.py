import os

sampleDir = "./sample"
resultDir = "./result"
def doWork(file):
    with open('{}/{}'.format(sampleDir,file), 'r') as f:
        a = f.read()
        a = a.replace("// flash 오류를 우회하기 위한 함수 추가\n",'')
        a = a.replace("function _flash_removeCallback() {}\n",'')
        a = a.split('ⓒ',1)[0]
        a = a.split('▶',1)[0]
        # 흠...
        
        newFile = open('{}/{}'.format(resultDir, file), 'w+')
        newFile.write(str(a))
        newFile.close()


file_list = os.listdir(sampleDir)
for file in file_list:
    doWork(file)
