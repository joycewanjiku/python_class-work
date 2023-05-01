


# define a function that accepts a string as input and uses the for loop to iterate through the string and
# count the voels

def word(names):
    count=0
    voels=("a","e","i","o","u")
    for i in names:
        for b in voels:
            if i ==b:
                count+=1
            return count
   
        print(word("beautifu"))
      
# Write a Python function that takes two arguments (a and b) and returns their sum.
def  add_num(a,b):
    
    sum = a+b
    return sum
print(add_num(34,65))

   
  

# Write a Python function that takes a string as input and returns the string reversed.
def reverse_string(string):
    return string[::-1]
print(reverse_string("Python is fun"))
    
# Write a Python function that takes a list of integers as input and returns the sum of all the integers in the list.
def sum_of_mylist(ints):
    sum = 0
    for i in ints:
        sum += i
    return sum
print(sum_of_mylist(45,78,90))

   
# Write a Python function that takes a list of integers as input and returns a new list with all the even numbers removed.
def list_nums(nums):
empty=()
for i in list:
    if i i%:
        list.remove(i)
        print(list)
# Write a Python function that takes a list of integers as input and returns the highest value in the list.
heighst=[150,60,60,500,230]
largest=int()
for large in heighst:
    if large>=large+1:
        largest=large
        print(largest)

# Write a Python function that takes a list of strings as input and returns a new list with all the strings capitalized.
def toUpper(x):
    o=ord(x)
    if o >= 97:
        return chr(o-32)
    else:
        return x