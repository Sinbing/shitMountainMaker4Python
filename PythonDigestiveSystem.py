# -*- coding: utf-8 -*-
# credit chino_debu
# Buri by Sinbing
import base64
from os import read



def userInput():
    # global userInputFile, fileName
    userInputFile = input('请输入食用进去的代码文件路径（相对路径/绝对路径都OK）')
    try:
        # resolve filename.
        same_userinput = userInputFile.replace('/', '\\')
        fileName = (mid_fileName:=(same_userinput.split('\\')[-1]))[:mid_fileName.index('.py')]
        return userInputFile, fileName
    except:
        print('Bug in get fileName.')


def outputFile(outputFile_str, output_fileName):
    with open('./shit_{0}.py'.format(output_fileName), mode="w", encoding="utf-8") as outputFile:
        outputFile.write (outputFile_str)


def readUserInputFile(readedFileName):
    global userInputFile_str
    with open (readedFileName,'r', encoding = 'utf-8') as readedFile:
        userInputFile_str = str(readedFile.read())
    return userInputFile_str


def b64_encode(b64_encodeFile):
    global b64_encode_output_str
    userInputFile_b64 = base64.b64encode(str(b64_encodeFile).encode('utf-8'))
    b64_encode_output_str = ('import base64;exec(base64.b64decode({0}))'.format(userInputFile_b64))


if __name__ == '__main__':
    userInputFile, fileName = userInput()
    userInputFile_str = readUserInputFile(userInputFile)
    # b64_encode(userInputFile)


