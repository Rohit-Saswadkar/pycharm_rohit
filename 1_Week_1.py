# get factorial using iteration
# Input:
# 5

# Output:
# Factorial of 5 is 120

# Example 2:
# Input:
# -1

# Output:
# Factorial can't be calculated for negative number

# Write your code here
# CORRECT CODE
def factorial(n):
    if n < 0:
        return "Factorial can't be calculated for negative number"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return f"Factorial of {n} is {result}"


num = 5 #int(input())
print(factorial(num))

# 2] check number is armstrong or not
# Input:
# 153

# Output:
# Number is Armstrong

# Example 2:
# Input:
# 450

# Output:
# Number is not Armstrong

# CORRECT CODE
def armstrong(n):
    order = len(str(n))
    temp = n
    sumx = 0
    while temp > 0:
        digit = temp % 10
        sumx += digit ** order
        temp //= 10
    if n == sumx:
        return "Number is Armstrong"
    else:
        return "Number is not Armstrong"
mint = 371 #int(input())
print(armstrong(mint))

# PRIME NUMBER
# Given two positive integers start and end. The task is to write a
# Python program to print all Prime numbers in an Interval. 
# Definition: A prime number is a natural number greater than 1 that has 
# no positive divisors other than 1 and itself. The first few prime numbers
# are {2, 3, 5, 7, 11, ….}


# ERROR
# Write your code here
# Write your code here
def is_prime(num):
    if num < 2:
        return False
    for i in range(2 , int(num ** 0.5)+1 ):
        if num % i == 0:
            return False
    return True
def prime_intervals(start , end):
    if end < start:
        return []
    intervals = []
    for num in range(start , end ):
        if is_prime(num):
            intervals.append(num)
    
    return intervals
start = 2#int(input())
end = 7#int(input())
# print(prime_intervals(start , end))

if len(prime_intervals(start,end)) == 0:
    print("There are no prime numbers in this range")
else:
    print("The prime numbers in this range are: ", prime_intervals(start,end))


# fibonaci number
# ERROR
# Write your code here
def fib_list(n):
    if n <=0:
        print('incorrect')
    elif n == 1:
        return 0
    elif n==2:
        return 1
    else:
        return fib_list(n-1) + fib_list(n-2)

n = 10 #int(input())
result = fib_list(n)
print(result)


# is number palindrome
# Write your code here
# CORRECT CODE
def is_palindrome(n):
  if not n:
    return False
  return n == n[::-1]
palindrome = 'racecar' #input()
print(is_palindrome(palindrome))

# You are given a large integer represented as an integer array digits,
#  where each digits[i] is the ith digit of the integer. The digits are
#  ordered from most significant to least significant in left-to-right 
# order. The large integer does not contain any leading 0's.

# Write a python program to increment the large integer by one and 
# return the resulting array of digits.

# Example 1:
# Input:
# [1,2,3]

# Output:
# [1, 2, 4]

# Explanation:
# The array represents the integer 123. Incrementing by one gives 123 + 1 = 124.

# Thus, the result should be [1,2,4].
# CORRECT CODE
def increment(digits, n): 
	carry = 1
	for i in range(n - 1, -1, -1): 
		temp = digits[i] + carry 
		digits[i] = temp % 10
		carry = temp // 10
	if (carry): 
		return [1] + digits 
	return digits 
digits = [1,2,3] #eval(input())
n = len(digits) 
print(increment(digits, n))

# pascals triangle
# CORRECT CODE
def pascal_triangle(n): 
	if (n == 0): 
		return []
	triangle = [[1]]
	for i in range(1, n): 
		row = [1] 
		for j in range(1, i): 
			row.append(triangle[i - 1][j - 1] + triangle[i - 1][j]) 
		row.append(1) 
		triangle.append(row) 
	return triangle 
n = 6 #int(input())
print(pascal_triangle(n))


# Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

# John, a data analyst, was tasked with analyzing sales data and 
# representing it in an Excel sheet. He decided to use alphabets as
# column titles. While assigning column numbers, he got stuck after column 
# 26 and named it "Z". He then named the 27th column "AB" as the combination
# of alphabets.

# Can you help John write a function to return the corresponding column 
# number when a columnTitle is given?
# Input:
# A

# Output:
# 1

# Example 2:
# Input:
# ZY

# Output:
# 701
# Write your code here
# Constraints:
# - 1 <= columnTitle.length <= 7
# - columnTitle consists only of uppercase English letters.
# - columnTitle is in the range ["A", "FXSHRXW"]

# CORRECT CODE
import pandas as pd
def title_to_number(s):
    result = 0
    for i in range(len(s)):
        result += (ord(s[i]) - ord('A') + 1) * 26 ** (len(s) - i - 1)
    return result
column = 'YZ' #input()
print(title_to_number(column))

# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of
#  the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), 
# or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

# Example 1:
# Input:
# 19

# Output:
# true

# CORRECT CODE

# Write your code here
def isHappy(n):
    seen = set()
    while n != 1:
        if n in seen:
            return False
        seen.add(n)
        n = sum(int(d) * int(d) for d in str(n))
    return True,n

n =19 # int(input())
print(isHappy(n))

# Given an integer n, return true if it is a power of two. Otherwise, return false.

# An integer n is a power of two, if there exists an integer x such that n == 2^x.

# Example 1:
# Input:
# 1

# Output:
# True

# Explanation:
# 2^0 = 1

# CORRECT CODE
def is_power_of_two(n):
    if n <= 0:
        return False
    else:
        return (n & (n - 1)) == 0

n = 1 #int(input())
print(is_power_of_two(n))

# Build an Array
# Medium
# Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.

# A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).

# Example 1:
# Input:
# [0,2,1,5,3,4]

# Output:
# [0,1,2,4,5,3]

# Explanation:
# The array ans is built as follows:

# ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]

# = [nums[0], nums[2], nums[1], nums[5], nums[3], nums[4]]

# = [0,1,2,4,5,3]

def permutations(mlist):
    perms = []
    if not mlist:
        return perms

    for i in range(len(mlist)):
        perms.append(mlist[mlist[i]])
    return perms
perms = eval(input())
pixel = permutations(perms)

print(pixel)

# Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

# Specifically, ans is the concatenation of two nums arrays.

# Return the array ans.

# Example 1:
# Input:
# [1,2,1]

# Output:
# [1,2,1,1,2,1]

# Explanation:
# The array ans is formed as follows:

# ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]

# ans = [1,2,1,1,2,1]
# Write your code here
def extends(mlist):
  mlist.extend(mlist)
  return mlist
inputs = [1,2,1] #eval(input())
print(extends(inputs))

# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

# Return the array in the form [x1,y1,x2,y2,...,xn,yn].

# Example 1:
# Input:
# [2,5,1,3,4,7]

# 3

# Output:
# [2,3,5,4,1,7]

# Explanation:
# Write your code here
def formation(mlst,n):
    if not mlst:
        return []
    x = mlst[:int(len(mlst)/2)]
    y = mlst[int(len(mlst)/2):]
    z = []
    
    for i in range(len(x)):
        z.append(x[i])
        z.append(y[i])
    return z
mlist = [2,5,1,3,4,7] #eval(input())
n = 3 #int(input())
print(formation(mlist,n))


# There are n employees in a company, numbered from 0 to n - 1. 
# Each employee i has worked for hours[i] hours in the company.

# The company requires each employee to work for at least target hours.

# You are given a 0-indexed array of non-negative integers hours of 
# length n and a non-negative integer target.

# Return the integer denoting the number of employees who worked at 
# least target hours.

# Example 1:
# Input:
# [0,1,2,3,4]

# 2

# Output:
# 3
# Write your code here
# CORRECT CODE
def target(emp,n):
  if not emp or n<=0 :
    return 0
  count = 0
  for i in emp:
    if i >= n:
      count += 1
  return count
emps = eval(input())
n = int(input())
print(target(emps,n))

# There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

# Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

# Note that multiple kids can have the greatest number of candies.

# Example 1:
# Input:
# [2,3,5,1,3]

# 3

# Output:
# [true,true,true,false,true]

# CORRECT CODE
# Write your code here
def max_candies(candy , n):
  maxc = max(candy)
  kids = []
  for can in candy:
    kids.append(can + n >=maxc)
  return kids
candies = eval(input())
n = int(input())
print(max_candies(candies , n))

# Given an array nums. We define a running sum of an array as
#  runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.

# Example 1:
# Input:
# [1,2,3,4]

# Output:
# [1,3,6,10]

# Explanation:
# Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

# CORRECT CODE
# Write your code here
def running_sum(mlist):
  result = []
  if not mlist:
    return result
  for i in range(len(mlist)):
    result.append(sum(mlist[:i+1]))
  return result

mlist = eval(input())
print(running_sum(mlist))
  
# How Many Numbers Are Smaller Than the Current Number
# Medium
# Given the array nums, for each nums[i] find out how many numbers
#  in the array are smaller than it. That is, for each nums[i] you
# \ have to count the number of valid j's such that j != i and
#  nums[j] < nums[i].

# Return the answer in an array.

# Example 1:
# Input:
# [8,1,2,2,3]

# Output:
# [4,0,1,1,3]

# CORRECT CODE
# Write your code here
def count_smaller(nums):
  if not nums:
    return 0
  result = []
  for i in range(len(nums)):
    count = 0
    for j in range(len(nums)):
      if nums[i]>nums[j]:
        count += 1
    result.append(count)
  return result
mlist = eval(input())
print(count_smaller(mlist))

# Counting Favorable Pairs
# Easy
# Given an array of integers nums, return the number of good pairs.

# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

# Example 1:
# Input:
# [1,2,3,1,1,3]

# Output:
# 4

# Explanation:
# There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

# CORRECT CODE
# Write your code here
def good_pairs(num):
  result = []
  if not num:
    return 0
  for i in range(len(num)):
    for j in range(i+1 , len(num)):
      if num[i] == num[j]:
        result.append([i,j])
  return len(result)
pairs = eval(input())
print(good_pairs(pairs))

# Customer with Maximum Wealth
# Hard
# You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the ith customer has in the jth bank. Return the wealth that the richest customer has.

# A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

# Example 1:
# Input:
# [[1,2,3],[3,2,1]]

# Output:
# 6

# Explanation:
# Write your code here
def max_wealth(wealth):
  maxw = 0
  if not wealth:
    return maxw
  for i in wealth:
    cust = sum(i)
    maxw = max(cust , maxw)
  return maxw
wealth = eval(input())
print(max_wealth(wealth))