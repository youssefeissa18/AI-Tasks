# 60 python exercise
# ---------------------------------------------------------------------------------------------------------
# problem 1
# str = input("Enter your string : ")
# print(len(str)) # Way 1
# count = 0
# for i in str: # Way 2
#     count += 1
# print(count)
# ---------------------------------------------------------------------------------------------------------
# problem 2
# str1 = input("Enter string one : ")
# if len(str1) < 2:
#     print("The len is Smaller than 2")
#
# else:
#     print(str1[:2] + str1[-2:])
# ---------------------------------------------------------------------------------------------------------
# problem 3
# str1 = input("Enter string  : ")
# if len(str1) < 3:
#     print("The len is Smaller than 3")
# else:
#     if str1.endswith("ing"):
#         str2 = str1.replace("ing","ly")
#         print(str2)
#     else:
#         print(str1 + "ing")
# ---------------------------------------------------------------------------------------------------------
# problem 4
# def words(words):
#     maxlen = words[0]
#     for i in words:
#         if words[0] < i:
#             maxlen = i
#     print(maxlen)
#
# word = ["Nada", "Youssef", "Ahmed","w3resource"]
# words(word)
# ---------------------------------------------------------------------------------------------------------
# problem 5
# str1 = input("Enter string one : ")
# str2 = str1.replace(str1[0],str1[-1])
# print(str2)
# print(str1[-1] + str1[1:-1] + str1[0])
# ---------------------------------------------------------------------------------------------------------
# problem 6
# str1 = input("Enter string one : ")
# result = ""
# for i in range(len(str1)):
#     if i % 2 == 0:
#         result = result + str1[i]
# print(result)
# ---------------------------------------------------------------------------------------------------------
# problem 7
# def word_count(str):
#     counts = dict()
#     words = str.split()
#
#     for word in words:
#         if word in counts:
#             counts[word] += 1
#         else:
#             counts[word] = 1
#
#     return counts
#
# print( word_count('youssef go to course in 2 days in week and youssef go to collage 2 days in week.'))
#
# str1 = input("Enter string one : ")
# counts = 0
# for i in str1:
#     if i in str1:
#         counts += 1
#     else:
#         counts = 1
# print(counts)
# ---------------------------------------------------------------------------------------------------------
# problem 8
# str1 = input("Enter string one : ")
# print(str1.lower())
# print(str1.upper())
# ---------------------------------------------------------------------------------------------------------
# problem 9
# str1 = input("Enter string one : ")
# if len(str1) % 4 == 0:
#     str2 = ''.join(reversed(str1))
#     print(str2)
# else:
#     print("Can't multiple by 4")
# ---------------------------------------------------------------------------------------------------------
# problem 10
# str1 = "Youssef Eisa \n"
# print(str1)
# print(str1.strip('\n'))
# print(str1)
# ---------------------------------------------------------------------------------------------------------
# problem 11
# str1 = input("String one : ")
# specified = input("specified char : ")
# if str1.startswith(specified):
#     print("specified is : " + specified)
# ---------------------------------------------------------------------------------------------------------
# problem 12
# import textwrap
# sample_text ='''
#     Python is a widely used high-level, general-purpose, interpreted,
#     dynamic programming language. Its design philosophy emphasizes
#     code readability, and its syntax allows programmers to express
#     concepts in fewer lines of code than possible in languages such
#     as C++ or Java.
#     '''
# text_without_Indentation = textwrap.dedent(sample_text)
# wrapped = textwrap.fill(text_without_Indentation, width=50)
# #wrapped += '\n\nSecond paragraph after a blank line.'
# final_result = textwrap.indent(wrapped, '>')
# print()
# print(final_result)
# print()
# ---------------------------------------------------------------------------------------------------------
# problem 13
# num = 12.502451
# print("{:.2f}".format(num))
# ---------------------------------------------------------------------------------------------------------
# problem 14
# num = float(input("Enter Number : "))
# if num > 0:
#     print("{:+.2f}".format(num))
# else:
#     print("{:-.2f}".format(num))
# ---------------------------------------------------------------------------------------------------------
# problem 15
# number = int(input("enter number : "))
# print("{:,}".format(number))
# ---------------------------------------------------------------------------------------------------------
# problem 16
# str1 = input("Enter string : ")
# print(str1)
# str2 = ''.join(reversed(str1))
# print(str2)
# ---------------------------------------------------------------------------------------------------------
# problem 17
# str1 = input("Enter string : ")
# count = 0
# for i in str1:
#     count += 1
# print(count)
# for c in sorted(count, key=count.get, reverse=True):
#   if count[c] > 1:
#       print('%s %d' % (c, count[c]))
# ---------------------------------------------------------------------------------------------------------
# problem 18
# char_count = {}
# def first_non_repeating_char(input_str):
#     char_count = {}
#     for char in input_str:
#         if char in char_count:
#             char_count[char] += 1
#         else:
#             char_count[char] = 1
#     for char in input_str:
#         if char_count[char] == 1:
#             return char
# input_string = "Youssef eissa"
# result = first_non_repeating_char(input_string)
# print("The first non-repeating is:", result)
# ---------------------------------------------------------------------------------------------------------
# problem 19
# str1 = input("Enter String : ")
# print(str1.replace(" ", ""))
# ---------------------------------------------------------------------------------------------------------
# problem 20
# def number_of_substrings(str):
# 	str_len = len(str);
# 	return int(str_len * (str_len + 1) / 2);
# str1 = input("Input a string: ")
# print("number_of_substrings",number_of_substrings(str1))
# ---------------------------------------------------------------------------------------------------------
# problem 21
# str1 = [13,5431,45,53,353,32]
# str1[0], str1[-1] = str1[-1], str1[0]
# print(str1)
# ---------------------------------------------------------------------------------------------------------
# problem 22
# list1 = [23, 65, 19, 90]
# pos1 = int(input("pos1 : "))
# pos2 = int(input("pos2 : "))
# list1[pos1], list1[pos2] = list1[pos2], list1[pos1]
# print(list1)
# ---------------------------------------------------------------------------------------------------------
# problem 23
# str1 = ["glbmdlgm", 5455, 4, 45, 4, 54, 24, 5, 4, 24, 5, 2, 45, "lmkbg", ";bmlcb"]
# print(len(str1))
# count = 0
# for i in str1:
#     count += 1
# print(count)
# ---------------------------------------------------------------------------------------------------------
# problem 24
# number = [15, 23, 465, 1, 454, 12, 41, 2]
# print(max(number))
# mxnum = number[0]
# for i in number:
#     if i > mxnum:
#         mxnum = i
# print(mxnum)
# ---------------------------------------------------------------------------------------------------------
# problem 25
# number = [15, 23, 465, 1, 454, 12, 41, 2]
# print(min(number))
# mxnum = number[0]
# for i in number:
#     if i < mxnum:
#         mxnum = i
# print(mxnum)
# ---------------------------------------------------------------------------------------------------------
# problem 26
# numbers = [4,51,3,48,2,865,2,3]
# num = int(input("Number you want to check : "))
# if num in numbers:
#     print("Founded")
# else:
#     print("Not Founded")
# ---------------------------------------------------------------------------------------------------------
# problem 27
# number = ["youssef",97596,45154,51,2,45,12,"eissa"]
# print(number)
# number.clear()
# print(number)
# number = ["youssef",97596,45154,51,2,45,12,"eissa"]
# print(number)
# for i in range(len(number)):
#     number.pop()
# print(number)
# ---------------------------------------------------------------------------------------------------------
# problem 28
# number = [1,2,5,31,45,12,10,10,21,0,41,12,31,1,23]
# print(set(number))
#
# number = [1,2,5,31,45,12,10,10,21,0,41,12,31,1,23]
# unique_list = []
# for item in number:
#     if item not in unique_list:
#         unique_list.append(item)
#
# print(unique_list)
# ---------------------------------------------------------------------------------------------------------
# problem 29 Ask about this
# my_list = ["name", "Alice", "age", 30, "city", "New York"]
# my_dict = {}
# for i in range(0, len(my_list), 2):
#     key = my_list[i]
#     value = my_list[i + 1]
#     my_dict[key] = value
# my_dict = {my_list[i]: my_list[i + 1] for i in range(0, len(my_list), 2)}
# print(my_dict)
# ---------------------------------------------------------------------------------------------------------
# problem 30
# list1 = [[1, 1, 2, 2, 5, 8, 4, 4, 8]]
# count = 0
# list2 = []
# for i in list1:
#     if i not in list2:
#         count += 1
#         list2.append(i)
# print(count)
# ---------------------------------------------------------------------------------------------------------
# problem 31
# test_list = [4, 6, 4, 3, 3, 4, 3, 7, 8, 8]
# print("The original list : " + str(test_list))
# K = 2
# res = []
# for i in test_list:
#     freq = test_list.count(i)
#     if freq > K and i not in res:
#         res.append(i)
# print("The required elements : " + str(res))
# ---------------------------------------------------------------------------------------------------------
# problem 32 Ask about that
# def find_strongest_neighbor(arr):
#     n = len(arr)
#     if n < 3:
#         return []
#     strongest_neighbors = []
#     for i in range(1, n - 1):
#         if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
#             strongest_neighbors.append(arr[i])
#     return strongest_neighbors
#
# input_list = [1, 2, 2, 3, 4, 5]
# result = find_strongest_neighbor(input_list)
# print(result)
# ---------------------------------------------------------------------------------------------------------
# problem 33
# import random
# from math import factorial
# input_list = [1, 2, 3]
# n = factorial(len(input_list))
# # Generate and print random permutations
# for i in range(n):  # You want 6 combinations, as there are 3! = 6 permutations
#     random.shuffle(input_list)
#     print(*input_list, end='\n')
# ---------------------------------------------------------------------------------------------------------
# problem 34
# import random
# from math import factorial
# input_list = [1, 2, 3]
# n = factorial(len(input_list))
# # Generate and print random permutations
# for i in range(n):  # You want 6 combinations, as there are 3! = 6 permutations
#     random.shuffle(input_list)
#     print(input_list, end=' ')
# Ask for this code
# import random
# test_list = [1, 2, 3]
# combinations_list = []
# n = len(test_list)
# for i in range(6):  # Generating 6 random combinations
#     random.shuffle(test_list)  # Shuffle the input list randomly
#     for r in range(1, n + 1):
#         combo = random.sample(test_list, r)
#         if sum(combo) % 2 == 0:
#             combinations_list.append(combo)
# for combo in combinations_list:
#     print(combo)
# ---------------------------------------------------------------------------------------------------------
# problem 35
# List_1 = ["a", "b"]
# List_2 = [1, 2]
# list3 = []
# for item1 in List_1:
#     for item2 in List_2:
#         if item1 != item2:
#             list3.append((item1, item2))
# print(list3)
# ---------------------------------------------------------------------------------------------------------
# problem 36
# list1 = [1, 1, 2, 3, 4, 5, 1, 2, 1]
# num = 1
# for i in list1:
#     if num in list1:
#         list1.remove(num)
# print(list1)
# ---------------------------------------------------------------------------------------------------------
# problem 37
# list1 = ['Gfg', 'is', 'best']
# list2 = [0, 1, 2, 1, 0, 0, 0, 2, 1, 1, 2, 0]
# # List to store the result
# result_list = []
# # Replace index elements with elements from list2
# for index in list2:
#     result_list.append(list1[index])
# print("The lists : ", result_list)
# ---------------------------------------------------------------------------------------------------------
# problem 38
# msh fahmha
# ---------------------------------------------------------------------------------------------------------
# problem 39 Ask about this code
# array = [[1, 3, 3], [2, 1, 2], [3, 2, 1]]
# # Sort the array based on a specific column using lambda
# for column in range(len(array[0])):
#     sorted_array = sorted(array, key=lambda x: x[column])
#     print(f"Sorted array specific to column {column}, {sorted_array}")
# ---------------------------------------------------------------------------------------------------------
# problem 40
# input_dict = {'youssef': 10, 'nada': 9, 'ahmed': 15, 'mohamed': 2, 'maged': 32}
# # Sort the dictionary by values in ascending order
# sorted_dict = dict(sorted(input_dict.items(), key=lambda item: item[1]))
# print(sorted_dict)
# ---------------------------------------------------------------------------------------------------------
# problem 41
# test_dict = {'Gfg': 3, 'is': 7, 'best': 10, 'for': 6, 'geeks': 'CS'}
# K = 7
# # Remove keys with values greater than K
# result_dict = {}
# for key, value in test_dict.items():
#     if isinstance(value, int) and value < K:
#         result_dict[key] = value
# print(result_dict)
# ---------------------------------------------------------------------------------------------------------
# problem 42
# dic1 = {1: 10, 2: 20}
# dic2 = {3: 30, 4: 40}
# dic3 = {5: 50, 6: 60}
# dic4 = dic1.copy()
# dic4.update(dic2)
# dic4.update(dic3)
# print(dic4)
# ---------------------------------------------------------------------------------------------------------
# problem 43
# test_dict = {'Gfg': 3, 'is': 7, 'best': 10, 'for': 6, 'geeks': 'CS'}
# for key, value in test_dict.items():
#     print(f"Key: {key} \t Value: {value}")
# ---------------------------------------------------------------------------------------------------------
# problem 44
# dic1 = {1: 10, 2: 20}
# dic2 = {3: 30, 4: 40}
# dic1.update(dic2)
# print(dic1)
# ---------------------------------------------------------------------------------------------------------
# problem 45
# test_dict = {'Gfg': 3, 'is': 7, 'best': 10, 'for': 6, 'geeks': 15}
# print(max(test_dict.values()))
# ---------------------------------------------------------------------------------------------------------
# problem 46
# original_dict = {'c1': 'Red', 'c2': 'Green', 'c3': None}
# for key, value in list(original_dict.items()):
#     if value is None:
#         original_dict.pop(key)
# print(original_dict)
# ---------------------------------------------------------------------------------------------------------
# problem 47
# tuple1 = (1,351,1,5,12,15,3)
# print(tuple1[3])
# ---------------------------------------------------------------------------------------------------------
# problem 48
# my_tuple = (1, 2, 3)
# a, b, c = my_tuple
# print(my_tuple)
# print("variables:", a, b, c)
# ---------------------------------------------------------------------------------------------------------
# problem 49
# original_tuple = (1, 2, 3)
# new_item = 4
# # Create a new tuple by combining the original tuple and the new item
# new_tuple = original_tuple + (new_item,)
# print("Original Tuple:", original_tuple)
# print("New Tuple with Added Item:", new_tuple)
# ---------------------------------------------------------------------------------------------------------
# problem 50
# original_tuple = (1, 2, 3)
# print(str(original_tuple))
# ---------------------------------------------------------------------------------------------------------
# problem 51
# list1 = [6513,21,5,31,1,3512]
# tuple1 = tuple(list1)
# print(tuple1)
# ---------------------------------------------------------------------------------------------------------
# problem 52
# original_tuple = (1, 2, 3)
# tuple2 = ''.join(reversed(str(original_tuple)))
# print(original_tuple[0:])
# print(original_tuple)
# print(tuple2)
# ---------------------------------------------------------------------------------------------------------
# problem 53 lsa
# Sample_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# for i in Sample_list:
#     Sample_list[0] = 100
# print(Sample_list)
# Sample_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# for i in range(len(Sample_list)):
#     temp_list = list(Sample_list[i])
#     temp_list[-1] = 100
#     Sample_list[i] = tuple(temp_list)
# print(Sample_list)
# ---------------------------------------------------------------------------------------------------------
# problem 54
# str1 = "Youssef eissa"
# tuple1 = tuple(str1)
# print(tuple1)
# ---------------------------------------------------------------------------------------------------------
# problem 55
# numbers_tuple = ((10, 20, 30), (40, 50, 60), (70, 80, 90))
# sum1 = 0
# for i in numbers_tuple:
#     for k in i:
#         sum1 += k
# print(sum1)
# print(sum1/ len(numbers_tuple))
# ---------------------------------------------------------------------------------------------------------
# problem 56
# my_set = {1, 2, 3}
# # Add a single member to the set
# my_set.add(4)
# # Add multiple members to the set
# my_set.update([5, 6])
# # Print the updated set
# print("Updated set:", my_set)
# ---------------------------------------------------------------------------------------------------------
# problem 57
# my_set = {1, 2, 3, 4, 5, 6}
# num = int(input("Enter number you want to remove from set : "))
# if num in my_set:
#     my_set.remove(num)
# print(my_set)
# ---------------------------------------------------------------------------------------------------------
# problem 58
# set1 = {1, 2, 3, 4, 5}
# set2 = {3, 4, 5, 6, 7}
# print("intersection", set1.intersection(set2))
# print("union", set1.union(set2))
# print("difference", set1.difference(set2))
# ---------------------------------------------------------------------------------------------------------
# problem 59
# set1 = {512, 5, 312, 23, 5, 2, 413, 41, 4, 561, 212, 56, 18, 41, 5612, 5, 31, 21}
# print(max(set1))
# print(min(set1))
# ---------------------------------------------------------------------------------------------------------
# problem 60 msh fahm el code
# def findPairs(lst, K):
#     res = []
#     while lst:
#         num = lst.pop()
#         diff = K - num
#         if diff in lst:
#             res.append((diff, num))
#     res.reverse()
#     return res
# lst = [1, 5, 3, 7, 9]
# K = 12
# print(findPairs(lst, K))
# ---------------------------------------------------------------------------------------------------------





# 150 problem
# problem 1
# print("Twinkle, twinkle, little star,")
# print("\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.")
# print("Twinkle, twinkle, little star,")
# print("\tHow I wonder what you are!")
# ---------------------------------------------------------------------------------------------------------
# problem 2
# import sys
# print("The Version is : ", sys.version)
# ---------------------------------------------------------------------------------------------------------
# problem 3
# import datetime
# print(datetime.datetime.now())
# ---------------------------------------------------------------------------------------------------------
# problem 4
# R = float(input("Enter your Radius : "))
# print(R*R*22/7)
# ---------------------------------------------------------------------------------------------------------
# problem 5
# firstname = input("Enter first name :\n")
# secondname = input("Enter second name :\n")
# listname = []
# listname.append(firstname)
# listname.append(secondname)
# print(listname)
# print(listname.reverse())
# print(listname)
# # another solution
# firstname = input("Enter first name :\n")
# secondname = input("Enter second name :\n")
# print(secondname+" "+ firstname)
# ---------------------------------------------------------------------------------------------------------
# problem 6
# number = input("Enter numbers : ")
# list = number.split(',')
# print("list =", list)
# numtuple = tuple(list)
# print("Tuple =",numtuple)
# ---------------------------------------------------------------------------------------------------------