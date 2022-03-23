''' 1)
Write a Python program to filter a list of integers using Lambda. Go to the editor
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]
'''
numbered_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = list(filter(lambda num: (num % 2 == 0), numbered_list))
print(even_list)
odd_list = list(filter(lambda num: (num % 2 != 0), numbered_list))
print(odd_list)

''' 2)
find which days of the week have exactly 6 characters.
'''

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

filtered_week = list(filter(lambda day: (len(day) == 6), weekdays))
print(filtered_week)



''' 3)
remove specific words from a given list 
Original list:
['orange', 'red', 'green', 'blue', 'white', 'black']

Remove words:
['orange', 'black']

After removing the specified words from the said list:
['red', 'green', 'blue', 'white']

'''
colors = ['orange', 'red', 'green', 'blue', 'white', 'black']
filtered_colors = list(filter(lambda color: (color != 'orange' and color != 'black'), colors))
print(filtered_colors)





''' 4)
 remove all elements from a given list present in another list
Original lists:
list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2: [2, 4, 6, 8]

Remove all elements from 'list1' present in 'list2:
[1, 3, 5, 7, 9, 10]
 '''
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, 4, 6, 8]

unique_list = list(filter(lambda num: (num not in list2), list1))
print(unique_list)



''' 5)
find the elements of a given list of strings that contain specific substring using lambda
Original list:
['red', 'black', 'white', 'green', 'orange']
Substring to search:
ack
Elements of the said list that contain specific substring:
['black']
Substring to search:
abc
Elements of the said list that contain specific substring:
[]

'''
slice = 'ack'
slice2 = 'abc'
colors = ['red', 'black', 'white', 'green', 'orange']
result = list(filter(lambda color: slice in color, colors))
print(result)
result2 = list(filter(lambda color: slice2 in color, colors))
print(result2)


''' 6)
check whether a given string contains a capital letter, a lower case letter, a number and a minimum length of 8 characters.
(This is like a password verification function, HINT: Python function 'any' may be useful)
'''
password = 'Hello World!'
pass_list = [char for char in password]
check1 = list(map(lambda c: c.isupper(), pass_list))
check2 = list(map(lambda c: c.islower(), pass_list))
check3 = list(map(lambda c: len(password) >= 8, password))
verify1 = any(check1)
verify2 = any(check2)
verify3 = any(check3)
print(verify1, ',', verify2, ',', verify3)


''' 7)
Write a Python program to sort a list of tuples using Lambda.

# Original list of tuples:
original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# Expected Result:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
'''
original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
result = sorted(original_scores, key = lambda x: x[1])
print(result)
