import re
import os.path

path = os.getcwd()
fileiist = os.listdir(f"{path}/원본")

for i in fileiist:
    ReadFile = open(f"{path}/원본/{i}", 'r' , encoding='UTF-8')
    ReadFile2 = open(f"{path}/번역본/{i}", 'r' , encoding='UTF-16')
    WriteFile = open(f"{path}/최종 결과물/{i}", 'w', encoding='UTF-8')
    lines = ReadFile.readlines()

    r = re.compile('^[0-9一-鿕ぁ-ゔァ-ヴー].*')
    for j in lines:
        aaa = ReadFile2.readline().strip("\n")
        contents = re.sub(r, aaa, j)
        WriteFile.write(contents)

WriteFile.close()