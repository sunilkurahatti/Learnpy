import sys
import os
from os import walk
from sys import path

a=os.getcwd()
b=os.listdir(a)
# os.sort(b)
print(b)
# for dirpath,dirnames,filenames in os.walk(a):
# 	print("PATH: ",dirpath)
# 	print("D NAME: ",dirnames)
# 	print("FILE: ",filenames)
# # print(os.walk(a))
# print(a)
# # print(dir(path))

for f in b:
	print(f)