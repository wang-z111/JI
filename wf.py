# -*- coding: utf-8 -*-

import argparse
import os
import sys

def openFile(filePath):
    with open(filePath, "r", encoding="utf-8") as file:
        filecontent = file.read()
        for replaceChar in '!"#$&()*+,-./:;<=>?@[\\]^_{|}·~“”‘’':
            filecontent = filecontent.replace(replaceChar, " ")
    return filecontent.lower().split()

def sortAndprint(wordList):
    wordDict = {}
    for word in wordList:
        wordDict[word] = wordDict.get(word, 0) + 1
    wordDict_List=list(wordDict.items())
    wordDict_List.sort(key=lambda x:x[1],reverse=True)
    print("{0:<10}{1}".format('total',len(wordDict_List)))
    if(len(wordDict_List) > 10):
        for i in range(10):
            word,count =wordDict_List[i]
            print("{0:<10}{1}".format(word,count))
    else:
        for i in range(len(wordDict_List)):
            word,count =wordDict_List[i]
            print("{0:<10}{1}".format(word,count))
    return


parser = argparse.ArgumentParser()
parser.add_argument('-s',nargs = '?')
parser.add_argument("filePath", nargs = '?')
args = parser.parse_args()
if ((args.filePath == None) and (args.s == None)):
    redi = sys.stdin.read()
    for ch in '!"#$&()*+,-./:;<=>?@[\\]^_{|}·~“”‘’':
        redi = redi.replace(ch, " ")
    txtStr = redi.lower().split()
    sortAndprint(txtStr)
    pass
elif ((args.s != None) and(os.path.isfile(args.s) == True) and (args.filePath == None)):
    #print('File:' + args.s.split('.')[0])
    sortAndprint(openFile(args.s))
    pass
elif ((args.filePath != None) and (os.path.isdir(args.filePath) == True) and (args.s == None)):
    filePathList = os.listdir(args.filePath)
    for file in filePathList:
        print(file.split('.')[0])
        sortAndprint(openFile(args.filePath + '\\' + file))
        print("----")
    pass
elif ((args.filePath != None) and(os.path.isfile(args.filePath) != True) and (args.s == None) and (os.path.isdir(args.filePath) != True)):
    #print('File:' + args.filePath)
    args.filePath=args.filePath+".txt"
    sortAndprint(openFile(args.filePath))
    pass
pass