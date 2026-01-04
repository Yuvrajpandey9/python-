s=open(r"C:/Users/yuvraj pandey/Downloads/OneDrive/Desktop/path/file1.txt","r")
s=f.read()
print(s)
#no. of lines
s=readlines()
print(len(s))

#3.to rename a file
import os
os.rename(r"C:/Users/yuvraj pandey/Downloads/OneDrive/Desktop/path/file1.txt",r"C:/Users/yuvraj pandey/Downloads/OneDrive/Desktop/path/file2.txt")
#4.to remove a file
import os 
os.remove(r"C:/Users/yuvraj pandey/Downloads/OneDrive/Desktop/path/file")