#!/usr/bin/env python3
# -*- coding: utf-8 -*-

f = open("log.txt",'r',encoding='utf-8')
readlist = []
i = 0
i=i+1
filename = "test_{0}.txt".format(i)
wf=open(filename, 'w', encoding='utf-8')
linecount=0
while 1:
    try:
        line = f.readline()
        wf.write(line)
        linecount=linecount+1
        if(linecount >= 1000):
            linecount = 0
            print(filename)
            i=i+1
            wf.close()
            filename = "test_{0}.txt".format(i)
            wf=open(filename, 'w', encoding='utf-8')
        if not line:
            break
    except Exception as e:
        print("read except:" + str(e))
        continue
        #print("read except:" + str(e))

f.close()

print(filename)
wf.close()
