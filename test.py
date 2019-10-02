#!/usr/bin/env python3
# Leap year

# year = 100

# if year%4==0:
# 	if year%400==0:
# 		print(f'{year} is a leap year')
# 	elif year%100==0:
# 		print(f'{year} is not a leap year')
# 	else:
# 		print(f'{year} is a leap year')
# else:
# 	print(f'{year} is not a leap year')



# year = 1904

# if (year % 4) == 0:
#    if (year % 100) == 0:
#        if (year % 400) == 0:
#            print(f'{year} is a leap year')
#        else:
#            print("{0} is not a leap year".format(year))
#    else:
#        print("{0} is a leap year".format(year))
# else:
#    print("{0} is not a leap year".format(year))


# Mapping decode:

# dic = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}

# data1 = '1214'
# data2 = '12345'


# def num_ways(data):
# 	l = len(data)

# 	def single_digit_process(data):
# 	for i in data:
# 		i=int(i)
# 		for k,v in dic.items():
# 			if i==v:
# 				print(k, end=' ', flush=True)
# 	print()

# 	for

# num_ways(data1)

# HCF / GCD

# def get_numbers(*args):
# 	nums=[]

# 	for i in args:
# 		nums.append(i)

# 	return nums

# numbers = get_numbers(150, 168, 270, 546, 730)
# count = len(numbers)

# smallest = min(numbers)

# divisors = []

# for j in range(2,smallest+1):
# 	passs = 0
# 	for i in numbers:
# 		if i%j!=0:
# 			break
# 		else:
# 			passs+=1
# 	if passs==count:
# 		divisors.append(j)


# print(f'HCF for numbers:{numbers} is {max(divisors)}')


# LCM:

# n1 = 72
# n2 = 64

# if n1>n2:
# 	largest = n1
# else:
# 	largest = n2

# multiplier = 1

# while n1==1 and n2==1:
# 	for i in range(2, largest+1):
# 		if n1%i==0 and n2%i==0:
# 			n1=n1/i
# 			n2=n2/i
# 			multiplier = multiplier * i
# 			print(f'{n1}, {n2}, {multiplier}')
# 			break


# print(f'LCM is {multiplier}')


# Factors of a number:

# num = 320

# def print_factors(x):
# 	for i in range(1,num+1):
# 		if num%i==0:
# 			print(i)

# print_factors(num)


# def add(x,y):
# 	return (x+y)

# def sub(x,y):
# 	return (x-y)

# def mul(x,y):
# 	return (x*y)

# def div(x,y):
# 	return (x/y)

# num1 = 24
# num2 = 3

# choice = 2

# if choice==2:
	# print(f'Subtraction of {num1} and {num2} is = {sub(num1,num2)}')

# Deck of cards:

# import itertools, random

# deck = list(itertools.product(range(1,13), ['spade', 'heart', 'diamond', 'club']))

# random.shuffle(deck)

# print("You got: ")
# for i in range(5):
# 	print(deck[i][0], "of",  deck[i][1])

# calendar:

# import calendar

# yy = 2019
# mm = 7

# # To ask month and year from the user
# # yy = int(input("Enter year: "))
# # mm = int(input("Enter month: "))

# # display the calendar
# print(calendar.month(yy, mm, w=10, l=2))


# Fibonacci series:
# a=0
# b=1
# for i in range(11):
# 	a,b = b,b+a
# 	print(b)



# add 2 matrices

# a= [[1,2,3],
# 	[4,5,6],
# 	[7,8,9]]

# b= [[1,2,3],
# 	[4,5,6],
# 	[7,8,9]]

# res= [[0,0,0],
# 	[0,0,0],
# 	[0,0,0]]

# for i in range(len(res)):
# 	for j in range(len(res[i])):
# 		res[i][j] = a[i][j]+b[i][j]
# print(res)

# String is palindrome:
# method1:
# string1 = "madam"
# string2 = "madan"

# if list(string2) == list(reversed(list(string2))):
# 	print('Palindrome')
# else:
# 	print('Not palindowme')


# method2:
# string = "madan"

# rev_str = string[::-1]

# print(rev_str)


# python to remove punctuations:

# string = "Hello, World.!!"

# # for i in string:
# # 	if i==',' or i=='.' or i=='!':
# # 		continue
# # 	else:
# # 		print(i, end="", flush=True)

# # print()



# punctuations = '''
# 				!@£$%^&*()_:"<>?/.,"
# 				'''
# filtered=''
# for i in string:
# 	if i not in punctuations:
# 		filtered = filtered + i

# print(filtered)



# string = "Hello, my name is Lokesh kannan. I am 30 years old. "
# words = string.split()

# words.sort()

# for word in words:
# 	print(word)

# Set operations

# E = {0, 2, 4, 6, 8};
# O = {1, 2,3,4,5};

# print('Union: ', E | O)
# print('Intersection: ', E & O)
# print('Difference: ', E - O)
# print('Sym Diff: ', E ^ O)



# count the no. of Vowel:
# vowels = 'aeiou'
#
# string = "I scored a century again. I am awesome. Leading run scorer of the season. yaay!!"
#
# string = string.casefold()
#
# count = {}.fromkeys(vowels,0)
#
# for char in string:
# 	if char in vowels:
# 		count[char] += 1
#
# print(count)


# count the no. of Vowel:
# vowels = 'aeiou'
#
# string = "I scored a century again biatch. I am awesome. Leading run scorer of the season. yaay!!"
#
# string = string.casefold()
#
# count = {}.fromkeys(vowels,0)
#
# for char in string:
# 	if char in vowels:
# 		count[char] += 1
#
# print(count)

'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''


# number = 1
# dividers = range(1,11)
# len = len(dividers)
# count = 0
#
# print(dividers)
#
# while count<len:
#     count = 0
#     for i in dividers:
#         if number%i==0:
#             count += 1
#             if count==len:
#                 print(number)
#                 break
#         else:
#             break
#     number+=1





# for number in range(10,300000000):
#     # for n in range(2,11):
#     if number%2==0 and number%3==0 and number%4==0 and number%5==0 and number%6==0 and number%7==0 and number%8==0 and number%9==0 and number%10==0 and number%11==0 and number%12==0 and number%13==0 and number%14==0 and number%15==0 and number%16==0 and number%17==0 and number%18==0 and number%19==0 and number%20==0:
#         print(number)
#         break




# Find the Fibonacci series:

# n=2
# memo=[]
# # A memoized solution
# def fib_2(n, memo):
#     if memo[n] is not None:
#         return memo[n]
#     if n == 1 or n == 2:
#         result = 1
#     else:
#         result = fib_2(n-1, memo) + fib_2(n-2, memo)
#     memo[n] = result
#     return result
#
# def fib_memo(n):
#     memo = [None] * (n + 1)
#     return fib_2(n, memo)
#
# print(fib_2(n,memo))


# n=1
# memo = []
#
# def recur_fibo(n, memo):
#     if memo[n] is not None:
#         return memo[n]
#     if n==2 or n==1:
#         return n
#     elif n==0:
#         return n
#     else:
#         result = recur_fibo(n-1, memo)+recur_fibo(n-2, memo)
#         memo[n] = result
#         return result

# print(recur_fibo(n,memo))


# method 1:
# def second_largest(given_list):
#
#     length = len(given_list)
#
#     if length<2:
#         return None
#
#     else:
#         largest = None
#         sec_largest = None
#
#         for i in given_list:
#             if largest==None and sec_largest==None:
#                 largest = i
#                 sec_largest = i
#
#             else:
#                 if i>=largest:
#                     sec_largest = largest
#                     largest = i
#
#         return sec_largest


# method 2:
# def second_largest(given_list):
#
#     length = len(given_list)
#
#     given_list.sort(reverse=True)
#
#     if length>1:
#         return given_list[1]
#     else:
#         return None

# print(second_largest([1, 3, 4,5, 5, 0, 2]))

# Method 1: (easy)
# def largest_num(str1, str2):
#     str1 = int(str1)
#     str2 = int(str2)
#
#     if str1 > str2:
#         return True
#
#     return False


# Method 2:
# def remove_leading_zeroes(str):
#     for i in str:
#         if str[0]=='0':
#             str=str[1:]
#     return str
#
#
# def largest_num(str1, str2):
#
#     str1 = remove_leading_zeroes(str1)
#     str2 = remove_leading_zeroes(str2)
#
#     len_str1 = len(str1)
#     len_str2 = len(str2)
#
#     if len(str1) > len(str2):
#         return True
#
#     elif len(str1)<len(str2):
#         return False
#
#     elif len(str1)==len(str2):
#         for i in range(len(str1)):
#             if str1[i]>str2[i]:
#                 return True
#                 break
#             elif str1[i]<str2[i]:
#                 return False
#                 break
#             elif str1[i]==str2[i]:
#                 continue
#
#         return False
#
#
# str1= "1224"
# str2= "1223"
#
#
#
# print(largest_num(str1, str2))

# print(largest_num(str1, str2))

# Array - Rooks in chess :
# def rooks_are_safe(array):
#     n = len(array)
#
#     for row in range(n):
#         row_count = 0
#         col_count = 0
#         for col in range(n):
#             row_count += array[row][col]
#             col_count += array[col][row]
#         if row_count>1 or col_count>1:
#             return False
#
#     return True
#
# array = [[1,0,0,0],
#         [0,0,1,0],
#         [0,0,0,1],
#         [1,0,0,0]]
#
# print(rooks_are_safe(array))


# counting the negative numbers in an array:

# def count_negatives(input):
#     l = len(input)
#
# # Big-O: optimize(n^2)
#
#     count = 0
#     for row in range(l):
#         for item in input[row]:
#             if item <= -1:
#                 count += 1
#                 if item>-1:
#                     break
#
#     return count
#
# print(count_negatives([[-2,-1,1],[1,2,3],[-1,0,1]]))


# def appears_twice(list):
#     count =0
#     dict = {}
#     for name in list:
#         if name in dict:
#             return name
#         else:
#             dict[name] = count+1
#     return 'No names appears twice.'
#
#     print(dict)
#
# list = ['George', 'Tom', 'Emily', 'Jenny', 'Jenny']
#
# print(appears_twice(list))

# Solution 1:
# def pair10(list):
#     dict = {}
#
#     for i in list:
#         dict[i]=0
#
#     result = False
#     for i in range(len(dict.keys())):
#         for j in range(i+1,len(list)):
#
#             if result == False:
#                 if list[i]+list[j]==10:
#                     result = True
#                     print(f'Sum of ({list[i]},{list[j]}) is 10')
#                     break
#     if result == False:
#         print("There is no pair that adds up to 10.")

# Solution 2:

# def pair10(list):
#     dict = {}
#
#     for item in list:
#         if (10-item) in dict:
#             print(f'{10-item}, {item}')
#             return
#         else:
#             dict[item]=1
#
#     print('There is no pair that adds up to 10.')
#
#
# print(pair10([1, 1, 1, 2, 3, 4, 5]))

# #### Inheritance:

# class BasicOperations:
# 	def __init__(self, n1, n2):
# 		self.n1 = n1
# 		self.n2 = n2
#
# 	def add(self):
# 		return(self.n1+self.n2)
#
# 	def sub(self):
# 		return self.n1 - self.n2
#
# # object = BasicOperations(2,4)
# # print(object.sub())
#
# class FullBasicOperations(BasicOperations):
# 	def __init__(self, n1, n2):
# 	# 	self.n1 = n1
# 	# 	self.n2 = n2
# 		super().__init__(n1, n2)
#
# 	def mul(self):
# 		return self.n1 * self.n2
#
# 	def div(self):
# 		return self.n1 / self.n2
#
# object = FullBasicOperations(2,4)
# print(object.add())

# import sys
#
# n=10
#
# data = []
#
# for i in range(n):
# 	a = len(data)
#
# 	b = sys.getsizeof(data)
#
# 	print('Length: {0:2d}; Size in Bytes: {1:4d}'.format(a,b))
# 	data.append(n)


# import ctypes
# import sys
#
# class DynamicArray(object):
#     '''
#     DYNAMIC ARRAY CLASS (Similar to Python List)
#     '''
#
#     def __init__(self):
#         self.n = 0 # Count actual elements (Default is 0)
#         self.capacity = 1 # Default Capacity
#         self.A = self.make_array(self.capacity)
#
#     def __len__(self):
#         """
#         Return number of elements sorted in array
#         """
#         return self.n
#
#     def __getitem__(self,k):
#         """
#         Return element at index k
#         """
#         if not 0 <= k <self.n:
#             return IndexError('K is out of bounds!') # Check it k index is in bounds of array
#
#         return self.A[k] #Retrieve from array at index k
#
#     def append(self, ele):
#         """
#         Add element to end of the array
#         """
#         if self.n == self.capacity:
#             self._resize(2*self.capacity) #Double capacity if not enough room
#
#         self.A[self.n] = ele #Set self.n index to element
#         self.n += 1
#
#     def _resize(self,new_cap):
#         """
#         Resize internal array to capacity new_cap
#         """
#
#         B = self.make_array(new_cap) # New bigger array
#
#         for k in range(self.n): # Reference all existing values
#             B[k] = self.A[k]
#
#         self.A = B # Call A the new bigger array
#         self.capacity = new_cap # Reset the capacity
#
#     def make_array(self,new_cap):
#         """
#         Returns a new array with new_cap capacity
#         """
#         return (new_cap * ctypes.py_object)()
#
#
# A = DynamicArray()
#
# A.append('1')
# print(f'{len(A)}: {sys.getsizeof(A)}')
#
# for i in range(10):
#     A.append(i)
#
# print(f'{len(A)}: {sys.getsizeof(A)}')


# Anagram:
# a = "god"
# b = "dog"
#
#
# A = list(a.lower().strip(' '))
# B = list(b.lower().strip(' '))
#
#
# len_a = len(A)
# len_b = len(B)
#
# if len_a == len_b:
#     for i in A:
#         counter = 0
#         for j in B:
#             if i==j:
#                 B.remove(j)
#                 break
#             counter += 1
#         if counter == len(B):
#             print('Strings are not Anagram. A char mismatch occurred.')
#             break
#         else:
#             print('All checked. Strings are Anagram')
#
#
# else:
#     print("Not anagram - diff lengths")



# Array pair sum:
# def pair_sum_check(L,V):
#
#     # Sets for tracking
#     seen = set()
#     output = set()
#
#     for i in L:
#
#         target = V-i
#
#         if target in L:
#             if i not in seen:
#                 seen.add(i)
#                 seen.add(target)
#                 output.add((i,target))
#     return output
#
# print(pair_sum_check([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10))


def missing_element(A, B):
    
