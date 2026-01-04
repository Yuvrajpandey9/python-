# n=[1,2,3,4,5,6]
# t=list(map(lambda x:(x*x,'even')if x%2==0 else (x*x*x,'odd'),n))
# print(t)

# reduce func is used to apply  a func when we want to output in a single value to apply reduce func we have  to import it from functools library.
# wap to add all the numbers in a list using reducing func.
# n=[1,2,3,4,5,6,7]
# import functools
# r=functools.reduce(lambda x,y: x+y,n)
# print(r)
# x=[20000,30000,60000]
# t=list(filter(lambda y:y>10000 and y<60000,x))
# print(t)
# wap to cal the words with the lenght greater than 3 
# l=['yash','sam','yuvi','shiuli','th','kj']
# t=list(filter(lambda x:len(x)>2,l))
# print(t)
# wap to capital the first letter of all the string and sort the data then print.
l=["yash","yubvi","sam"]
t=list(map(lambda x:x.title(),l))
t.sort()
print(t)

