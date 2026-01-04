"""list is denotes by [] and it is a connection of different data types  
*list are ordered and it maintain the order of elements based on how they are added 
* duplicate items can be added in list
* list are mutable i.e we can change the elements and modifed it also of list
*we can access the items of list by their index vakue that is startin from 0 to n-1"""
"""pop function is used to remove the last element of list or we can also specify the index value to remove that particular element
remove function is used to remove the specified element from the list
insert function is used to insert the element at specified index value
k.inser(3,"noida") it will insert noida at index value 3
append function is used to add the element at the end of the list
k.append("delhi") it will add delhi at the end of the list
extend function is used to add the elements of one list to another list
clear function is used to clear the entire list
sort function is used to sort the elements of list in ascending order
reverse function is used to reverse the order of elements of list
copy function is used to copy the elements of one list to another list
count function is used to count the number of times an element is present in the list
index function is used to find the index value of an element in the list"""
a=[]
a.append("yuvraj")
a.append("pandey")
a.append(20)
a.append(5.6)
a.append(True)
print(a)
a.insert(2,"noida")
print(a)
a1=["hello","world"]
a.extend(a1)
print(a)
a.pop()
print(a)
a.remove("noida")
print(a)
a[2]="python"
print(a)
sorted_a=sorted(a1)
print(sorted_a)
a.reverse()
print(a)
