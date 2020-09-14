
import re
import glob
import os



"""
https://www.it-swarm.dev/ko/python/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%97%90%EC%84%9C-%EC%A0%95%EA%B7%9C-%ED%91%9C%ED%98%84%EC%8B%9D%EC%9D%84-%EC%82%AC%EC%9A%A9%ED%95%98%EC%97%AC-%EC%97%AC%EB%9F%AC-%EB%B2%88-%EB%8C%80%EC%B2%B4-%ED%95%A0-%EC%88%98-%EC%9E%88%EC%8A%B5%EB%8B%88%EA%B9%8C/1070873862/
"""

def multiple_replace(dict, text):

  # Create a regular expression  from the dictionary keys
  regex = re.compile("(%s)" % "|".join(map(re.escape, dict.keys())))

  # For each match, look-up corresponding value in dictionary
  return regex.sub(lambda mo: dict[mo.string[mo.start():mo.end()]], text)


def file_preprocess(infile_name, outfile_name):
    """
     한 문장단위로 READ : 문장형태면 Write 아니면 SKIP
    """
    with open(infile_name, mode="r") as file:
        content = list()

        while True:
            sentence = file.readline()

            if sentence:

                print("입력문장  : "+sentence)

                # TODO - 뉴스기사 내 치환문구 대상 dict
                sub_dict = {
                    "// flash 오류를 우회하기 위한 함수 추가": "",
                    "function _flash_removeCallback() {}": "",
                    "최신 유행 트렌드 총집결 #흥(클릭!)": ""
                }


                # 이메일주소 발췌 sub_dict 추가
                email = []
                email = re.findall('(\S+@\S+)', sentence)

                for i in range(len(email)):
                    sub_dict[email[i]] = ""

                #print(sub_dict)


                # 변환대상 문구 replace
                new_sentence = multiple_replace(sub_dict, sentence)
                print("문구제거후 : "+ new_sentence)


                """
                https://ohgyun.com/781
                """

                # TODO - 일부 영문기사는 문장 split 이 안되는 문제 해결필요 ex) 62.txt
                # 이메일주소에서 나뉘지 않도록함.
                #regex = "(?<=[^0-9][^@A-Za-z])[\.|\n|\;]"
                #regex = "(?<=[^0-9@A-Za-z])[\.|\n|\;]"
                #regex = "(?<=[A-Za-z0-9])[\.|\n]"
                #regex = "(?<=[^0-9][^@])[\.|\n|\;]"
                regex = "(?<=[^0-9])[\.|\n|\;]"



                split_sentence = re.split(regex, new_sentence)

                print(split_sentence)


                for i in range(len(split_sentence)):
                    regex2 = "▶"
                    regex3 = "\t"
                    if len(re.findall(regex2, split_sentence[i])) > 1 or len(re.findall(regex3, split_sentence[i])) > 0:
                        pass
                    else:
                        content.append(split_sentence[i])

            else:
                break

        print(content)


    """
     문장단위로 분리된 content 한줄씩 파일 출력처리
    """
    with open(outfile_name , mode="w") as file:

        print(outfile_name)
        #file.writelines(content)
        for i in range(len(content) - 1):
            if content[i] != '\n':
                file.write(content[i] +'\n')



def file_load(path):
    files = glob.glob(path)

    for file in files:

        file_name = re.split("\.",file)
        print(file_name)

        file_preprocess(str(file_name[0])+'.'+str(file_name[1]), str(file_name[0])+'_out')
        #file_preprocess("1047.txt", "1047_out")

if __name__ == "__main__":

    print(str(os.getcwd())+"/*.txt")
    file_load(str(os.getcwd())+"/*.txt")