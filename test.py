#!/usr/bin/env python3
# Leap year:

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

# Flames:

# flames_dict = {'F':'Flower', 'L': 'Lover', 'A': 'Affection', 'M':'Marriage', 'E': 'Enemy', 'S': 'Sister'  }
# flames_list = ['f','l','a','m','e','s']
#
# dict = {}
# man = 'Lokesh'
# woman = 'Priya'
#
# man = list(man.lower().replace(' ', ''))
# woman = list(woman.lower().replace(' ', ''))
#
# for letter in man:
#     if letter not in dict:
#         dict[letter]=1
#     else:
#         dict[letter]+=1
# # print(dict)
#
# for letter in woman:
#     if letter not in dict:
#         dict[letter]=1
#     else:
#         dict[letter]-=1
#         # print(dict)
#
# print(len(dict))
#
# print(flames_list)

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


# missing element:
# def missing_element(A, B):
#     missing = []
#     for i in A:
#         if i in B:
#             B.remove(i)
#         else:
#             missing.append(i)
#
#     for i in missing:
#         print(i)
#
# def missing_element2(A, B):
#     A = sorted(A)
#     B = sorted(B)
#
#     for i,j in zip(A,B):
#         if i!=j:
#             return i
#
# def missing_element3(arr1,arr2):
#     arr1 = sorted(arr1)
#     arr2 = sorted(arr2)
#
#     dict = {}
#     missing = []
#     for i in arr1:
#         if i not in dict:
#             dict[i]=1
#         else:
#             dict[i]+=1
#
#     for j in arr2:
#         if j in dict:
#             dict[j]-=1
#
#
#     for k,v in dict.items():
#         if dict[k]!=0:
#             missing.append(k)
#
#     return missing
#
# arr1 = [1,3,2,4,5,6,7,8]
# arr2 = [3,7,2,1,4,6]
#
# print(missing_element3(arr1,arr2))

# new challenge:

# Largest Continious Sum:

# list = [-3,1,2,-1,3,4,10,10,-10,-1]
# # soln1:
# sum_till_now = largest_sum = list[0]
# pointer_start = 0
# pointer_end = 0
# max_list = []
# counter = 0
# sum = 0
# for i in list[1:]:
#     counter+=1
#     sum_till_now += i
#     if sum_till_now > largest_sum:
#         largest_sum = sum_till_now
#         pointer_end = i
#         max_list = list[0:counter+1]
# print(largest_sum)
#
# for j in max_list[::-1]:
#     sum+=j
#     print(sum)
#     if sum==largest_sum:
#         print(j)
#         break
# print(pointer_start)
# print(pointer_end)
# print(max_list)


# soln2:
# current_sum = max_sum = list[0]
#
# for i in list[1:]:
#     current_sum = max(current_sum+i,i)
#     max_sum = max(max_sum, current_sum)
#
# print(max_sum)

# Sentence reversal:

# s = "   this is a sample text    "

# Soln - Easy method:
# string1 = string.strip().split()
#
# for i in string1[::-1]:
#     print(i, end=" ")
#

# Soln2 - using while:
# words = []
# length = len(s)
# i=0
#
# while i<length:
#     if s[i]!=' ':
#         word_start = i
#
#         while i<length and s[i]!=' ':
#             i+=1
#
#         words.append(s[word_start:i])
#     i+=1
#
# print(words)

# soln2 - Using for:

# s = "   this is a sample text "
#
# words = []
# l = len(s)
# word_initialized=False
#
# for i in range(l):
#     if s[i] != ' ' and word_initialized==False:
#         word_initialized = True
#         word_start = i
#
#     elif (word_initialized==True and s[i]==" "):
#         word_end = i
#         word_initialized = False
#         words.append(s[word_start:word_end])
#
# if word_initialized==True:
#         words.append(s[word_start:])

# words.append(s[3:7])
# print(words)

# String Compression:
# s = "AAAAaaBCccAA"
#
# Expected result:
# A8B1C3
#
# def str_comp(s):
#     s = s.upper()
#
#     dict = {}
#     length = len(s)
#     c=''
#
#     for i in s:
#         if i in dict:
#             dict[i] += 1
#
#         else:
#             dict[i] = 1
#
#     for k,v in dict.items():
#         c+=k
#         c+=str(v)
#
#     return (c)
#
# # print(dict)
#
# print(str_comp(s))

# s = "AAAAaaBCccAA"
#
# # Expected result:
# # A6B1C3 but without using dict
#
# count = ''
# store= ''
# output = ''
#
# for i in s:
#
#     if store != i:
#         output += store + str(count)
#         store = i
#         count = 1
#
#     elif store == i:
#         store = i
#         count += 1
#
# output += store + str(count)
#
# print(output)

# Unique Characters in string:
# Using for loop:
#     s = "I love  u"
#     def is_unique_ignore_spaces(s):
#         store = ''
#         for i in s:
#             if i!=' ' and i not in store:
#                 store+=i
#             else:
#                 return False
#         return True
#
#     print(is_unique_ignore_spaces(s))

# Using while loop:
# s = "I love yu  "
#
# def is_unique(s):
#     leng = len(s)
#     i=0
#     cont = ''
#
#     while i<leng:
#         if s[i]==' ':
#             i+=1
#             continue
#         if s[i] not in cont:
#             cont+=s[i]
#         else:
#             return False
#
#         i+=1
#
#     return True
#
# print(is_unique(s))

                                                    # Stack / Queue / Deque data structures #
# Stack data structure:
# class Stack(object):
#     def __init__(self):
#         # self.item = item
#         self.list = []
#
#     def push(self, item):
#         self.item = item
#         self.list.append(self.item)
#         return ('''item inserted.''')
#
#     def viewList(self):
#         return (self.list)
#
#     def peek(self):
#         self.l = len(self.list)
#         if self.l>0:
#             return (self.list[(self.l)-1])
#
#     def pop(self):
#         self.list.pop(-1)
#         print(self.list)
#
#     def count(self):
#         self.l = len(self.list)
#         return self.l
#
#     def isEmpty(self):
#         self.l = len(self.list)
#         if self.l == 0:
#             return True
#         else:
#             return False
#
#     def popAll(self):
#         while len(self.list)>0:
#             print('---- Popping ----')
#             self.list.pop(0)
#             print(self.list)
#
# # so = Stack()
# # print(so.push('first'))
# # print(so.push('second'))
# # print(so.viewList())
# # print(so.count())
# # so.popAll()

# Queue data structure:
# class Queue():
#     def __init__(self):
#         self.list = []
#
#     def enqueue(self, item):
#         self.list.insert(0,item)
#
#     def dequeue(self):
#         return (self.list.pop())
#
#     def peek(self):
#         print (self.list[0])
#
#     def size(self):
#         print(len(self.list))
#
#     def isEmpty(self):
#         if self.list == []:
#             return True
#         else:
#             return False
#
#     def viewFullQueue(self):
#         print(self.list)
#
#
# q = Queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# q.viewFullQueue()
# q.peek()
# q.dequeue()
# q.viewFullQueue()

# Implementation of Deque data structure:

# class Deque():
#     def __init__(self):
#         self.list = []
#
#     def addToFront(self, item):
#         self.list.insert(0,item)
#
#     def addToBack(self, item):
#         self.list.append(item)
#
#     def DeleteFromFront(self):
#         self.list.pop(0)
#
#     def DeleteFromBack(self):
#         self.list.pop()
#
#     def isEmpty(self):
#         if self.list==[]:
#             return True
#         else:
#             return False
#
#     def size(self):
#         return (len(self.list))
#
#     def viewDeque(self):
#         print(self.list)
#
#     def peekFront(self):
#         return self.list[0]
#
# string = "()(){}(}{)"
#
# def balancedBracketsChecker(s):
#     open, closed, closed_dict = '{[(' , '}])', {'}':'{', ']':'[', ')':"("}
#
#     if len(string)%2 != 0:
#         return False
#
#     else:
#         openstorage = Deque()
#
#         for i in string:
#
#             if i in open:
#                 openstorage.addToFront(i)
#             elif i in closed:
#                 if openstorage.size()>0 and (str(closed_dict[i]) == openstorage.peekFront()):
#                     openstorage.DeleteFromFront()
#                 else:
#                     return False
#
#         if openstorage.size() == 0:
#             return True
#         else:
#             return False
#
# print(balancedBracketsChecker(string))


# class Queue2Stacks():
#     def __init__(self):
#         self.instack = []
#         self.outstack = []
#
#     def enqueue(self, item):
#         self.item = item
#         self.instack.append(self.item)
#
#     def dequeue(self):
#         self.outstack = self.instack
#         return self.outstack.pop(0)
#
# q = Queue2Stacks()
#
# for i in range(5):
#     q.enqueue(i)
#
# for i in range(5):
#     print (q.dequeue())

                                                            #-- Linked Lists: --#

# Singly linked list:

# class Node(object):
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#
# a = Node(1)
# b = Node(2)
# c = Node(3)
# d = Node(4)
# e = Node(5)
#
# a.next = b
# b.next = c
# c.next = d
# d.next = e
#
#
# def nth_from_last(node, n):
#     start_node = node
#     total_ele_in_node = 0
#
#     while node:
#         total_ele_in_node += 1
#         node = node.next
#
#     nth_ele = total_ele_in_node - (n-1)
#
#     count = 0
#     node = start_node
#     while node:
#         count += 1
#
#         if count == nth_ele:
#             return node
#         node = node.next
#
# print(nth_from_last(a,4))

#-- End of Linked list --#



# Linked list - Reversal:

# Desired output(Reversal):
# d.next = c
# c.next = b
# b.next = a

# def reverse(node):
#     current = node
#     prev = None
#     next = None
#
#     while current:
#         next = current.next
#         current.next = prev
#         prev = current
#         current = next
#
#     return prev
#
# print(reverse(a))
#
# print (d.next.value)
# print (c.next.value)
# print (b.next.value)

# Singly linked list cycle check:
# def cycleCheck(node):
#     node_list = []
#
#     while node.next != None:
#
#         node_list.append(node)
#
#         if node.next in node_list:
#             return True
#
#         node = node.next
#
#     return False

# print(cycleCheck(a))

# Doubly-Linked List:
# class DoublyLinkedList(object):
#     def __init__(self, data):
#         self.data = data
#         self.prev = None
#         self.next = None
#
# a = DoublyLinkedList(3)
# b = DoublyLinkedList(6)
# c = DoublyLinkedList(9)
#
# a.next = b
# b.prev = a
# b.next = c
#
# print(b.next.data)
# print(b.prev.data)

                                                                        #-- Recursion --#


# Factorial:
# def fact(n):
#     # base case
#     if n==0:
#         return 1
#     else:
#         return n*fact(n-1)
#
# print(fact(100))

# Factorial using Memoization:
# fact_memo = {}
# def fact(n):
#     # base case
#     if n<2:
#         return 1
#     else:
#         if n not in fact_memo:
#             fact_memo[n] = n*fact(n-1)
#
#     return fact_memo[n]
#
# print(fact(100))
# print(fact_memo[20])

# Creating memoization data structure:

# class Memoization(object):
#     def __init__(self,function):
#         self.function = function
#         self.memo = {}
#
#     def __call__(self, *args):
#         if args not in self.memo:
#             self.memo[args]=self.function(*args)
#         return self.memo[args]
#
# def fact_to_be_memod(n):
#     if n==0:
#         return 1
#     else:
#         return n*fact_to_be_memod(n-1)
#
# memo = Memoization(fact_to_be_memod(5))
# print(memo.__call__())


# Cumulative sum:
# def cum_sum(n):
#     if n==0:
#         return 0
#     else:
#         return n+cum_sum(n-1)
#
# print(cum_sum(10))

# sum of all the individual digits in an integer
# def sum_of_digits(n):
#     r=n%10
#     if n==0:
#         return 0
#     else:
#     # n=n//10
#         return r+sum_of_digits(n//10)
#
#
# n=1111
#
# print(sum_of_digits(n))

# def word_split(string, list, out=[]):
#
#     for word in list:
#         if word in string:
#             out.append(word)
#             string=string.replace(word,'')
#             return word_split(string, list, out)
#
#     if string =="":
#         return out
#     else:
#         return (f'"{string}" is left out.')
#
# print(word_split('ilovedogsJohn',['i','am','a','dogs','lover','love','John']))

# String Reversal - Recursion:
# def str_rev(s):
#     l=''
#
#     for i in s:
#         l=i+l
#
#     print(l)
#
# def str_rev_rec(s):
#     if len(s)<=1:
#         return s
#     else:
#         return str_rev_rec(s[1:])+s[0]
#
# print(str_rev_rec("Cow"))

#Fibonacci sequence - simple iterative soln:
# def fib_it(n):
#     a=0
#     b=1
#     for i in range(n+1):
#        a,b = b,b+a #Tuple unpacking method, python feature
#         print(b)
#
# fib_it(100)

# Fibonacci Recursive:
# def fib_rec(n):
#     if n==0 or n==1:
#         return n
#     else:
#         return fib_rec(n-1)+fib_rec(n-2)
#
# Fibonacci Recursive using Memoization:
# n=1000
# cache = {}
# def fib_rec_mem(n):
#     if n==0 or n==1:
#         return n
#     else:
#         if n not in cache:
#             cache[n] = fib_rec_mem(n-1)+fib_rec_mem(n-2)
#         return cache[n]
#
# for i in range(n+1):
#     print(fib_rec_mem(i))


# Coin change problem:
# n=1
# change = {0.01,0.02,0.05,0.10,0.50}
# change = [10,5,2,1]
# out = []
#
# def coin_change(n,change_list):
#     change_dict = {}
#     for i in change_list:
#         change_dict[i] = 0
#         # print(change_dict)
#
#     if n!=0:
#         for i in change:
#             if n/i>0:
#                 change_dict[i] = n//i
#                 n=n%i
#
#     else:
#         return ('n should be > 0.')
#
#     if n==0:
#         for k,v in change_dict.items():
#             print(v)
#             if v>0:
#                 for i in range(v):
#                     out.append(k)
#
#     return out, len(out)
#
# print(coin_change(n,change))

# Coin change problem using Recursion:
# n = 63
# change = [1,5,10,25,21]
# def rec_coin(m, change_list, out=[]):
#
#     change_list = sorted(change_list, reverse=True)
#     if m==0:
#         return len(out)
#     else:
#         i=change_list[0]
#
#         if m//i>=1:
#             times = m//i
#             for j in range(times):
#                 out.append(i)
#             m=m%i
#             change_list.pop(0)
#         elif m//i<1:
#             change_list.pop(0)
#         else:
#             return ('!!Double check the change list as exact change is not possible.')
#
#         return rec_coin(m,change_list)
#
# print(rec_coin(n,change))
# tree = [ 'a',['b',['d',[], []],['e',[], []]],        ['c', ['f',[], []], []]]


# def rec_coin(target,coins,known_results):
#     '''
#     INPUT: Target change amount and list of coin values
#     OUTPUT: Minimum coins needed to make change
#
#     Note, this solution is not optimized.
#     '''
#
#     # Default to target value
#     min_coins = target
#
#     # Check to see if we have a single coin match (BASE CASE)
#     if target in coins:
#         known_results[target] = 1
#         return 1
#
#     elif known_results[target] > 0:
#         return known_results[target]
#     else:
#         # for every coin value that is <= than target
#         for i in [c for c in coins if c <= target]:
#
#             # Recursive Call (add a count coin and subtract from the target)
#             num_coins = 1 + rec_coin(target-i,coins,known_results)
#
#             # Reset Minimum if we have a new minimum
#             if num_coins < min_coins:
#
#                 min_coins = num_coins
#                 known_results[target] = min_coins
#
#     return min_coins
# target = 63
# known_results = [0]*(target+1)
# print(rec_coin(target,[1,5,10,25,21], known_results))
# --Needs optimisation-- #
# --Optimised-- #

                                                                            # Trees

# tree = ['a',['b',['d',[],[]],['e',[],[]]],['c',['f',[],[]],[]]]
# print(tree)

# Tree Implementation using Functional programming:

# def createBinaryTree(r):
#     return [r, [], []]
#
# def insertLeft(root, newBranch):
#     t = root.pop(1)
#     if len(t)>1:
#         root.insert(1,[newBranch,t,[]])
#     else:
#         root.insert(1,[newBranch,[],[]])
#     return root
#
# def insertRight(root, newBranch):
#     t = root.pop(2)
#     if len(t)>1:
#         root.insert(2,[newBranch,[],t])
#     else:
#         root.insert(2,[newBranch,[],[]])
#     return root
#
# def getRootVal(root):
#     return root[0]
#
# def setRootVal(root, newVal):
#     root[0]=newVal
#
# def getLeftChild(root):
#     return root[1]
#
# def getRightChild(root):
#     return root[2]
#
# r=createBinaryTree(4)
# print(r)
#
# print(insertLeft(r, 5))
# print(insertLeft(r, 6))
# print(insertRight(r, 7))
# print(insertRight(r, 8))
#
# print(setRootVal(r,1))
# print(getRootVal(r))
#
# print(getLeftChild(r))


# Tree Implementation using OOP:

# class BinaryTree():
#     def __init__(self, root):
#         self.key = root
#         self.leftchild = None
#         self.rightchild = None
#
#     def insertLeft(self,newNode):
#         if self.leftchild == None:
#             self.leftchild = BinaryTree(newNode)
#         else:
#             new = BinaryTree(newNode)
#             old = self.leftchild
#             new.leftchild = old
#             self.leftchild = new
#         return self.leftchild
#
#     def insertRight(self, newNode):
#         if self.rightchild == None:
#             self.rightchild = BinaryTree(newNode)
#         else:
#             new = BinaryTree(newNode)
#             old = self.rightchild
#             new.rightchild = old
#             self.rightchild = new
#         return self.rightchild
#
#     def getLeftChild(self):
#         return self.leftchild
#
#     def getRightChild(self):
#         return self.rightchild
#
#     def getRootValue(self):
#         return self.key
#
#     def setRootValue(self, newVal):
#         self.key = newVal
#
# tree = BinaryTree(7)
# tree.insertLeft(4)
# tree.insertLeft(5).insertRight(6)
# tree.insertRight(10)
# tree.insertRight(8)
# print(tree.getLeftChild().getLeftChild().getRightChild().getRootValue())
#
#                                                         # Tree Traversals within Binary Tree
# def preorder(obj):
#     if obj != None:
#         print(obj.getRootValue(), end="")
#         preorder(obj.getLeftChild())
#         preorder(obj.getRightChild())
#
#
# preorder(obj)
# print()
#
# def postorder(obj):
#     if obj != None:
#         postorder(obj.getLeftChild())
#         postorder(obj.getRightChild())
#         print(obj.getRootValue(), end="")
#
# postorder(obj)
# print()

# def inorder(tree):
#     if tree != None:
#         inorder(tree.getLeftChild())
#         print(tree.getRootValue(), end="")
#         inorder(tree.getRightChild())
#
# inorder(tree)

# class newNode:
#
#     # Construct to create a new node
#     def __init__(self, key):
#         self.data = key
#         self.left = None
#         self.right = None
#
# # Returns true if given tree is BST.
# def isBST(root, l = None, r = None):
#
#     # Base condition
#     if (root == None) :
#         return True
#
#
#     if (l != None and root.data <= l.data) :
#         return False
#
#     if (r != None and root.data >= r.data) :
#         return False
#
#     return isBST(root.left, l, root) and isBST(root.right, root, r)
#
# def printLevels(root):
#
#     print(root.data)
#     while root.left != None:
#         return printLevels(root.left)
#     while root.left != None:
#         return printLevels(root.left)
#
#
#
# # Driver Code
# root = newNode(7)
# root.left = newNode(5)
# root.right = newNode(9)
# root.left.left = newNode(4)
# root.left.right = newNode(6)
# root.right.left = newNode(8)
# root.right.right = newNode(10)
# #root.right.left.left = newNode(40)
# # print(isBST(root))
# print(printLevels(root))

                                                                            # searching and sorting algorithms
# def ordered_seq_search(array, num):
#     pos=0
#     loop = 0
#     while pos<len(array) and array[pos]<=num:
#         loop += 1
#         if array[pos]==num:
#             return True, loop
#         pos += 1
#     return False, loop
#
# array = [1,2,3,4,5,6,8,9,10]
# num = 7
# print(ordered_seq_search(array, num))


# Bubble sort algorithm:
# list = [100,98,97,96]
#
#
# def bubbleSort(list):
#     l = len(list)
#     pointer = 0
#     sort_count = 0
#
#     while pointer<l-1:
#         if list[pointer] > list[pointer+1]:
#             list[pointer], list[pointer+1] = list[pointer+1], list[pointer]
#             sort_count = 0
#         else:
#             sort_count+=1
#
#         if sort_count == l-1:
#             return list
#
#         if pointer == l-2:
#             pointer = 0
#             continue
#
#         pointer += 1
#
# # Using Recursion:
# list = [100,98,97,96,2,3,1]
# def rec_bubbleSort(list, sort_count = None):
#     if sort_count == None:
#         sort_count = 1
#     l=len(list)
#     # base case
#
#     if sort_count==0:
#         return list
#
#     else:
#         sort_count = 0
#         for i in range(l-1):
#             if list[i]>list[i+1]:
#                 list[i], list[i+1] = list[i+1], list[i]
#                 sort_count += 1
#
#         return rec_bubbleSort(list, sort_count)
#
# print(rec_bubbleSort(list))


# Selection Sort:
# list = [5,2,1,9,5,6]
# l = len(list)
# pointer1 = 0
#
# while pointer1<l-1:
#     lowest = list[pointer1]
#     pointer2=pointer1+1
#     while pointer2<l:
#         if list[pointer2]<lowest:
#             lowest = list[pointer2]
#             list[pointer1], list[pointer2]  = lowest, list[pointer1]
#         pointer2+=1
#
#     pointer1 +=1
#
# print(list)
#
#
# # Insertion sort:
# list = [5,2,1,9,7,6]
# l = len(list)
# pointer1 = 1
#
# while pointer1<l:
#     temp=pointer1
#     while list[pointer1] < list[pointer1-1] and pointer1>0:
#         list[pointer1], list[pointer1-1] = list[pointer1-1], list[pointer1]
#         pointer1 = pointer1-1
#
#     pointer1 = temp+1
#
# print(list)

# Merge sort:
# list = [5,2,1,3,7,6,8,4]
#
# def merge_sort(list):
#     if len(list)>1:
#         mid = len(list)//2
#         L = list[:mid]
#         R = list[mid:]
#
#         merge_sort(L)
#         merge_sort(R)
#
#         i,j,k=0,0,0
#
#         # Merge happens here
#         while i<len(L) and j<len(R):
#
#             if L[i]<R[j]:
#                 list[k]=L[i]
#                 i+=1
#             else:
#                 list[k]=R[j]
#                 j+=1
#             k+=1
#
#         while i<len(L):
#             list[k]=L[i]
#             i+=1
#             k+=1
#
#         while j<len(R):
#             list[k]=R[j]
#             j+=1
#             k+=1
#
#     return list
#
#
# print(merge_sort(list))

# Amazon1 find the highest profit from the stock prices:
# def maxprofit(list):
#     l = len(list)
#     max_profit, buying, selling = float('-inf'),None,None
#
#     for i in range(l-1):
#         for j in range(i+1,l):
#             if list[j]-list[i]>max_profit:
#                 max_profit = list[j]-list[i]
#                 buying, selling = list[i], list[j]
#     return (max_profit, buying, selling)
#
# list = [30,22,21,5]
# print(maxprofit(list))


#Amazon2 - product of all elements except that element:
# list = [1,2,3,4]
#
# def products_of_rest(l):
#     l = len(l)
#     out=[]
#
#     for i in range(l):
#         mul = 1
#         for j in range(l):
#             if i!=j:
#                 mul = mul * list[j]
#         out.append(mul)
#     return out
#
# print(products_of_rest(list))

# def fib(n):
#     a=0
#     b=1
#     while n>=0:
#         c=b+a
#         print(b)
#         a=b
#         b=c
#         n=n-1
#
# def rec_fib(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return rec_fib(n-1)+rec_fib(n-2)
# # print(rec_fib(10))
#
# n=10
# while n!=0:
#     print(rec_fib(n))
#     n=n-1

# string = 'here'
#
#
# def rev_str(st, out=""):
#     l=len(st)
#
#     if l==1:
#         out = out+st
#         return out
#
#     else:
#         out = out+st[-1]
#         # print(out)
#         st = st[0:-1]
#         return rev_str(st, out)
#
# print(rev_str(string))
# import math
# print(math.sqrt(8))

# n=99
# i =1
# while i*i<=n:
#     res = i
#     i += 1
#
# print(res)

# Coin and denominations:
# def solution(n, coins):
#
#     # Set up our array for trakcing results
#     arr = [1] + [0] * n
#
#     for coin in coins:
#         for i in range(coin, n + 1):
#             arr[i] += arr[i - coin]
#
#     if n == 0:
#         return 0
#     else:
#         return arr[n]
#
# print(solution(100, [1,2,5]))

# Binary search tree check:



# Remove duplicates in a string:
# def remove_duplicates(string):
#     if len(string)==0:
#         return ('omg string is null')
#     elif len(string)==1:
#         return (string)
#     else:
#         string = string.lower()
#         out = ""
#         for i in string:
#             if i not in out:
#                 out = out+i
#
#         return out
#
# string = "tree traversal"
# print(remove_duplicates(string))

# Given a list of integers and a target number, write a function that returns a boolean indicating if its possible to sum two integers from the list to reach the target number
# list = [1,2,3,5,6,7]
# target = 5
#
# def check_sum(list, target):
#     l=len(list)
#     for i in range(l):
#         for j in range(l):
#             if i!=j:
#                 if list[i]+list[j] == target:
#                     return ((list[i], list[j]))
#
#     return False
#
# # print(check_sum(list, target))
#
# # another: solution:
# def check_sum1(list, target):
#     seen = []
#     for i in list:
#         num2  = target - i
#         seen.append(num2)
#         if i in seen:
#             return True
#
# print(check_sum1(list, target))




# Given a list of account ID numbers (integers) which contains duplicates, find the one unique integer. (the list is guaranteed to only have one unique (non-duplicated) integer

# list = [22,23,23,9,9,5,5,21,22]
#
# def find_unique(list):
#     l=len(list)
#     found = {}
#     for i in list:
#         if i not in found:
#             found[i]=1
#         else:
#             found[i]+=1
#
#     for i,j in found.items():
#         if j ==1:
#             return(i)
#
# print(find_unique(list))


# c = [0, 0, 1, 0, 0, 1, 0]
#
# def jumpingOnClouds(c):
#     n=len(c)
#     i,count=0,0
#     while i<n-1:
#         if i+2<=n-1 and c[i+2]!=1:
#             i+=2
#             count+=1
#         else:
#             i+=1
#             count+=1
#
#     return(count)
#
# print(jumpingOnClouds(c))

# def repeatedString(s, n):
#     i,count=0,0
#     l=len(s)
#     if l==1:
#         return n
#     else:
#         while l<n:
#             s+=s[i]
#             i+=1
#             l+=1
#             if i>l-1:
#                 i=0
#         for i in s:
#             if i == 'a':
#                 count+=1
#
#         return count


# def repeatedString(s,n):
#     count = 0
#     l=len(s)
#
#     if l==1 and s=='a':
#         return n
#
#     elif l==1 and s!='a':
#         return 0
#
#     elif l==0:
#         return 0
#
#     elif l>1:
#         if n<l:
#             s=s[:n]
#             for i in s:
#                 if i =='a':
#                     count+=1
#             return count
#
#         else:
#
#             for i in s:
#                 if i =='a':
#                     count+=1
#
#             mul = n//l
#             count *= mul
#
#             for i in range(n%l):
#                 if s[i]=='a':
#                     count += 1
#
#             return count
#
# s='ojowrdcpavatfacuunxycyrmpbkvaxyrsgquwehhurnicgicmrpmgegftjszgvsgqavcrvdtsxlkxjpqtlnkjuyraknwxmnthfpt'
# n=685118368975
# print(repeatedString(s,n))

# out = ""
# st = "here"
# out = out + st[-1]
# print(st[0:-1])
# print(out)

# from collections import defaultdict
#
# d=defaultdict(lambda:'a')
#
# for i in range(10):
#     d[i]=d[i]+str(i)
#
# print(d)

# Arrays:
# a=[[1,2,3],[1,2,3],[1,2,3]]
# print(a[0][1])

# def plusMinus(arr):
#     pos,neg,neut = 0,0,0
#     l=len(arr)
#     for i in arr:
#         if i>0:
#             pos+=1
#         elif i<0:
#             neg+=1
#         else:
#             neut+=1
#
#     f_pos=float(pos/l)
#     f_neg=float(neg)
#     f_neut=float(neut/l)
#     print (f"%.{l}f" % f_pos)
#     print (f"%.{l}f" % f_neg)
#     print (f"%.{l}f" % f_neut)
# plusMinus([-4,3,-9,0,4,1])

#
# L=[5,5,5,5,5]
#
# def minmax(L):
#     max=max(L)
#     count=0
#     for i in L:
#         if i == max:
#             count+=1
#     return count
# minmax(L)

# def timeConversion(s):
#     suffix = s[-2] + s[-1]
#     s=s[0:8]
#     L=s.split(':')
#     h=int(L[0])
#     m=L[1]
#     s=L[2]
#
#     if suffix=='PM' and h>=1 and h<12:
#         h=h+12
#     elif suffix=='AM':
#         if h==12:
#             h=0
#
#     print(f'{h:02d}:{m}:{s}')
#
# timeConversion('12:45:54PM')
#
# def dayOfProgrammer(year):
#     out=''
#     leapyear=0
#     if year > 1918:
#         if year%4==0:
#             if year%100==0:
#                 if year%400==0:
#                     leapyear=1
#                 else:
#                     leapyear = 0
#             else:leapyear=1
#
#         else:leapyear=0
#
#     elif year<1918:
#         if year%4==0:
#             leapyear=1
#         else:
#             leapyear=0
#
#     if year==1918:
#         return ('26.09.'+str(year))
#
#     if leapyear==1:
#         out+='12.09.'+str(year)
#     else:
#         out+='13.09.'+str(year)
#     return out
# print(dayOfProgrammer(2020))


# def asd(bill, k, b):
#     count=0
#     for i in range(len(bill)):
#         if i==k:
#             continue
#         else:
#             count+=bill[i]
#
#     if b==count/2:
#         return ('asd')
#
#     return int(b-(count/2))
#
# print(asd([3,10,2,9],1,7))

# def pageCount(n,p):
#     i,j,c1,c2=1,n,0,0
#
#     while i!=p or j!=p:
#         i+=1
#         if i%2==0:
#             c1+=1
#
#         j-=1
#         if j%2==1:
#             c2+=1
#
#     if c1>c2:
#         return c2
#
#     return c1
#
# print(pageCount(3,0))

# n=4
# if n%2!=0:
#     print('Weird')
# elif n%2==0:
#     if n in range(2,6):
#         print('Not Weird')
#     elif n in range(6,21):
#         print('Weird')
#     elif n>20:
        # print('Not Weird')


# def getMoneySpent(b,keyboards, drives):
#     b=b[0]
#     i,count=0,0
#     while i<len(keyboards):
#         j=0
#         while j<len(drives):
#             if keyboards[i]+drives[j]<=b and keyboards[i]+drives[j]>count:
#                 count = keyboards[i]+drives[j]
#             j+=1
#         i+=1
#
#     return -1 if count==0 else count
#
# print(getMoneySpent([10,2,3], [3,1], [5,2,8]))

# def countApplesAndOranges(s, t, a, b, apples, oranges):
#     counta, counto = 0,0
#     for i in apples:
#         if a+i>=s and a+i<=t:
#             counta+=1
#
#     for i in oranges:
#         if b+i>=s and b+i<=t:
#             counto+=1
#
#     print(counta)
#     print(counto)
#
# countApplesAndOranges(7,11,6,13,[-2,2,1],[5,-6])

# def breakingRecords(scores):
#     min, max, count_max, count_min = float('inf'),0,-1,-1
#     for i in scores:
#         if i>max:
#             count_max+=1
#             max=i
#         if i<min:
#             count_min+=1
#             min=i
#     return (count_max, count_min)
#
# print(breakingRecords([0, 9, 3, 10, 2, 20]))

# def birthday(s, d, m):
#     count=0
#     for i in range(len(s)-m+1):
#
#         if sum(s[i:i+m])==d:
#             count+=1
#     return count
#
# print(birthday([1,4,2,3,1,1],6,3))

# def insertionSort1(n, arr):
#     to_sort=arr[n-1]
#     i=n-1
#     # print(arr[n-1])
#     sortedd = False
#     while i>=0 and sortedd==False:
#         i-=1
#         if arr[i]>to_sort:
#             arr[i+1]=arr[i]
#         else:
#             arr[i+1]=to_sort
#             sortedd=True
#         if i==-1:
#             arr[i+1]=to_sort
#         for z in arr:
#             print(z, end=' ')
#         print()
#
# insertionSort1(10,[2, 3, 4, 5, 6, 7, 8, 9, 10, 1])

# def camelcase(s):
#     n=len(s)
#     out,word_start,list = '',0,[]
#     for i in range(n):
#         if s[i].upper()==s[i]:
#             list.append(s[word_start:i])
#             word_start=i
#     list.append(s[word_start:n])
#     out = len(list)
#     return out
#
# print(camelcase('thisIsString'))

# Map:
# def func(a):
#     a+=a
#     return a
#
# b=[1,2,3,4]
#
# m=map(func,b)
# print(list(m))

# def myfunc(a):
#   return len(a)
#
# x = map(myfunc, ('apple', 'banana', 'cherry'))
#
# print(x)
#
# #convert the map into a list, for readability:
# print(list(x))

# Filter:
# ages = [5, 12, 17, 18, 24, 32]
#
# def myFunc(x):
#   if x < 18:
#     return False
#   else:
#     return True
#
# adults = filter(myFunc, ages)
#
# for x in adults:
#   print(x)

# 1.
# def nums1():
#     x=11
#     for i in range(x):
#         if i%2==0:
#             yield i
#
# for i in nums1():
#     print(i, end='')
# print('\n')
#
# # 2.
# def nums2(x):
#     for i in range(x):
#         if i%2==0:
#             yield i
#
# for i in nums2(11):
#     print(i, end='')

# Lambda:
# a=2
# b=4
#
# l= lambda a,b: a+b
# print(l(a,b))

# import sys
#
# dict = {}
#
# def makedict(string):
#     l = string.split()
#     dict[l[0]]=l[1]
#
# n=int(sys.stdin.readline())
#
# for i in range(n):
#     makedict(str(sys.stdin.readline()))
#
# inp = sys.stdin.readline().strip()
# while inp:
#     if inp in dict:
#         print(f'{inp}={dict[inp]}')
#     else:
#         print('Not found')
#     inp = sys.stdin.readline().strip()

# List Comprehensions:

# even = [i for i in range(1,100) if i%2==0]
# odd = [i for i in range(1,100) if i%3==0]
#
# print([(x,y) for x in even for y in odd if x%10==0 if y%10==0])

# def minimumNumber(n, password):
#     # Return the minimum number of characters to make the password strong
#     numbers = "0123456789"
#     lower_case = "abcdefghijklmnopqrstuvwxyz"
#     upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     special = "!@#$%^&*()-+"
#     d={}
#     d['n'], d['l'], d['u'], d['s'] = 0,0,0,0
#     count = 0
#
#     if len(password)>=6:
#         for i in password:
#             if i in numbers:
#                 d['n']+=1
#             if i in lower_case:
#                 d['l']+=1
#             if i in upper_case:
#                 d['u']+=1
#             if i in special:
#                 d['s']+=1
#
#         for k,v in d.items():
#             print(d[k])
#             if d[k]==0:
#                 count+=1
#         return count
#     else:
#         for i in password:
#             if i in numbers:
#                 d['n']+=1
#             if i in lower_case:
#                 d['l']+=1
#             if i in upper_case:
#                 d['u']+=1
#             if i in special:
#                 d['s']+=1
#         for k,v in d.items():
#             if d[k]==0:
#                 count+=1
#         l = len(password)
#         needed = 6-l
#         if needed>=count:
#             return needed
#         else:
#             return count
#
# print(minimumNumber(6, '4b*A'))


# def alternate(s):
#     filtered=list(set(s))
#     l=len(s)
#     flist=list(set(s))
#     large_count = 0
#     for i in s:
#         for j in s:
#             current = ''
#             alt = s
#
#             if i != j:
#                 current += i
#                 current += j
#                 for z in flist:
#                     if z not in current:
#                         alt=alt.replace(z,'')
#
#
#                 if len(alt)>1:
#                     # print(alt)
#                     p=0
#                     count=0
#                     while p!=len(alt)-1:
#                         if alt[p]!=alt[p+1]:
#                             count+=1
#                             if count>=large_count:
#                                 large_count=count+1
#                                 # print(large_count)
#                         else:
#                             count=0
#                         p+=1
#
#     return large_count
#
#
# print(alternate('asvkugfiugsalddlasguifgukvsa'))

# def hurdleRace(k, height):
#     n=len(height)
#     max=0
#     for i in height:
#         if i>max:
#             max=i
#     diff = max-k
#     if diff>0:
#         return diff
#     else:
#         return 0
#
# print(hurdleRace(4, [1,6, 3, 5, 2]))


# def saveThePrisoner(n, m, s):
#     if (m%n)+(s-1)%n==0:
#         return n
#     else:
#         return ((m%n)+(s-1)%n)
#
# print(saveThePrisoner(7, 7, 1))


# n = 5
# s=''
# while n/2!=0:
#     s+=str(n%2)
#     n=int(n/2)
#
# count=0
# max=0
#
# for i in s:
#     if i=='1':
#         count+=1
#         if count > max:
#             max=count
#     else:
#         count = 0
# print(max)

# a=[[1,1,1,0,0,0],[0,1,0,0,0,0],[1,1,1,0,0,0],[0,0,0,2,2,2],[0,0,0,0,2,0],[0,0,0,2,2,2]]
#
# x,sum,max=0,0,float('-inf')
#
# while x<4:
#     for i in range(len(a[x])-2):
#         sum = a[x][i] + a[x][i+1] + a[x][i+2] + a[x+1][i+1] + a[x+2][i] + a[x+2][i+1] +a[x+2][i+2]
#         if sum>max:
#             max=sum
#
#     x+=1
# print(max)

# def circularArrayRotation(a, k, queries):
#     mod_k = k%len(a)
#     # print(mod_k)
#     rotation = 0
#     while rotation!=mod_k:
#         # print(1)
#         temp=0
#         for i in range(len(a)):
#             if i==len(a)-1:
#                 a[i],a[0]=temp,a[i]
#                 # print(a,temp)
#             else:
#                 a[i],temp = temp,a[i]
#                 # print(a,temp)
#         rotation+=1
#     res=[]
#     for i in queries:
#         res.append(a[i])
#     return res

# append and delete:

# l = list('abcd')
# res=l.pop(2)
#
# print(l[2])

# s='aba'
# t='aba'
# k=7
#
# def appendAndDelete(s, t, k):
#     if len(t)>len(s):
#         n=len(s)
#     else:
#         n=len(t)
#
#     for i in range(n):
#         if s[i]!=t[i]:
#             ptr=i
#             break
#         else:
#             ptr = i+1
#
#     unmatched = s[ptr:]
#     # print(unmatched)
#     del_count = len(unmatched)
#     to_add = t[ptr:]
#     add_count = len(to_add)
#
#     total_count = del_count+add_count
#     # print(add_count)
#     # print(del_count)
#     # print(total_count)
#     if s==t:
#
#     if total_count == k:
#         return 'Yes'
#     else:
#         return 'No'


# print(appendAndDelete(s, t, k))

# def libraryFine(d1, m1, y1, d2, m2, y2):
#     if y1>y2:
#         late=y1-y2
#         return late*10000
#     elif(y1==y2):
#         if m1>m2:
#             late=m1-m2
#             return late*500
#         elif (m1==m2):
#             if d1>d2:
#                 late=d1-d2
#                 return (late*15)
#             else:
#                 return 0
#         else:
#             return 0
#     else:
#         return 0
#
# print(libraryFine(2, 7, 1014, 1, 1, 1015))

# def cutTheSticks(arr):
#     l=[]
#     while len(arr)!=0:
#         minn = min(arr)
#         l.append(len(arr))
#         for i in range(len(arr)):
#             arr[i]=arr[i]-minn
#
#         while 0 in arr:
#             arr.remove(0)
#     return l
#
# arr=[5, 4, 4, 2, 2, 8]
# print(cutTheSticks(arr))

# def solution(N):
#     count = 0
#     n=2
#
#     while 2*N +n-n**2>0:
#         a=(2*N+n-n**2)/(2*n)
#         if a - int(a) == 0:
#             print(a,n)
#             count+=1
#         n+=1
#
#     return count
#
# print(solution(6))

# def vowelReverse(string):
#     string =list(string)
#     strings=''
#     vowels = 'aeiou'
#     v_list = []
#     for i in string:
#         if i in vowels:
#             v_list.insert(0,i)
#
#     for i in range(len(string)):
#         if string[i] in vowels:
#             string[i]=v_list.pop(0)
#
#     for i in string:
#         strings+=i
#     return strings
#
# s='apple'
# print(vowelReverse(s))

# def flatlandSpaceStations(n, c):
#     c=sorted(c)
#     if len(c)==n:
#         return 0
#     else:
#         res=[]
#         for i in range(n):
#             dist=[]
#             for j in c:
#                 dist.append(abs(i-j))
#             res.append(min(dist))
#
#         return max(res)

# def hackerrankInString(s):
#     word='hackerrank'
#     l=len(s)
#     j,checked=0,0
#     for i in word:
#         while j<l:
#             if i==s[j]:
#                 j+=1
#                 checked+=1
#                 break
#             j+=1
#
#     return 'YES' if checked == len(word) else 'NO'
#
# print(hackerrankInString('hereiamstackerrank'))

# def weightedUniformStrings(s, queries):
#     letters = 'abcdefghijklmnopqrstuvwxyz'
#     dict={}
#     j=0
#     s_dict = {}
#     for i in letters:
#         j+=1
#         dict[i]=j
#
#     for i in range(len(s)):
#         if s[i] not in s_dict:
#             j=i+1
#             counter=1
#             if j<len(s)-1:
#                 while s[i]==s[j]:
#                     counter+=1
#                     j=j+1
#                     if j>len(s)-1:
#                         break
#             for z in range(1,counter+1):
#                 s_dict[s[i]*z]=dict[s[i]]*z
#
#     for i in queries:
#         if i in s_dict.values():
#             print('Yes')
#         else:
#             print('No')
#
# weightedUniformStrings('aaabbbbcccddd', [9,7,8,12,5])

# def weightedUniformStrings(s, queries):
#     dict={}
#
#     f=set(s)
#     for i in f:
#         dict[i]=0
#     i=0
#     j=i+1
#     try:
#         while i<len(s)-1:
#             if s[i]==s[j]:
#                 j+=1
#             else:
#                 if (j-i)>dict[s[i]]:
#                     dict[s[i]]=j-i
#                 i=j
#                 j=i+1
#             if j==len(s)-1:
#                 if s[j]==s[i]:
#                     dict[s[i]]=j+1-i
#                 else:
#                     if dict[s[j]]==0:
#                         dict[s[j]]=1
#     except(IndexError):
#         pass
#
#     for k,v in dict.items():
#         print(f'{k}:{v}')
#
# weightedUniformStrings('aaabbbbcccdddaa', [9,7,8,12,5])
# Done

# class C:
#     dangerous = 2
#
# c1 = C()
# c2 = C()
# print(c1.dangerous)
#
# c1.dangerous = 3
# print (c1.dangerous)
# print (c2.dangerous)
#
# del(c1.dangerous)
# print (c1.dangerous)

# a= 'stasd'
# a=2
# print(a)





# a=2
# def add():
# b=3
# c=a+b
# print(c)
# add()

# def is_palindrome(x):
#     x=str(x)
#     return 1 if x==x[::-1] else 0
#
# x = -121
# print(is_palindrome(x))


# dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
# def romanToInt(s):
#     sum = 0
#     for i in range(len(s)):
#         if i!=len(s)-1:
#             if dict[s[i]]<dict[s[i+1]]:
#                 sum-=dict[s[i]]
#             else:
#                 sum+=dict[s[i]]
#
#         else:
#             sum+=dict[s[i]]
#
#         # print(sum)
#
#     return sum
#
#
# print(romanToInt('MMMCMXCIX'))

def validParanthesis(s):
    dict = {'{':'}', '[':']', '(':')'}
    open='{[('
    opened = []
    if len(s)>0:
        for i in s:
            if i in open:
                opened += i
            else:
                if len(opened)>0 and i==dict[opened[-1]]:
                    opened.pop()
                else:
                    return False

    else:
        return True
    if len(opened)==0:
        return True
    else:
        return False

print(validParanthesis('['))
