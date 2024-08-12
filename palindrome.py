list1= [1,2,1]

copy_list1 = list1.copy()
copy_list1.reverse()

if copy_list1==list1:
    print("Its a palindrome")
else:
    print("Its not a palindrome")

'''
can also be written as,
list1 = [1,2,1]
if list1==list1[::-1]
     print("Its a palindrome")
else:
     print("Its not a palindrome")
'''
