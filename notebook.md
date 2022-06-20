

# introduction to programming with python and java specialization 

# Introduction to python

1. 直接一个一个vedio按部就班地看下来，不要快进不要跳
2. 下载module resource 时，只要下载handouts就够了、
3. 把视频中所有出现过的代码，特别是coding demonstration中的，全部自己敲一遍
4. quiz就是考语文，assignment难度一般，week4的作业主要第二个cell的条件不要看错
5. 一个星期基本能搞定这个course

## 单词

specialization 专门化的

console 仪表盘

script 脚本

conferencing platform 会议平台

layout 布局

syllabus 教学大纲；摘要

shortcut 捷径；快捷键

toggle 切换，转换

concatenate 连接

semantics 语义学，语法论

client-side programs 客户端程序

intuitive 直觉的

module 模件，组件，功能块

cursor 指针

assertion 断言，明确肯定；使用，主张

comma 逗号

colon 冒号

trivial 琐碎的；不重要的；容易解决的

substitute 替代品；替代

iterate 迭代

prime number 素数

composite 复数

## All the Python functions

```python
# this is a list of Python functions

# create a list with random strings NOTE: the list begin with 0
list1 = ['1', 'dog', 'cat', '789']

# print the list
print(list1)

# get the length of the list
print(len(list1))

# get the 2nd item in the list
print(list1[1])

# add items to a list
list1.append('hello')

# remove the last item in the list
list1.pop()

# remove the 2nd item in the list
list1.pop(1)

# check if an item is in the list
print('dog' in list1)

# for loop in a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    print(number)

# to store even numbers
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = []
even_count = 0
for number in numbers:
    if (number % 2 == 0):
        even_numbers.append(number)
        even_count += 1
print(even_numbers)
print("There are ", even_count, "bunmers in the even list")

# find the minimum value
numbers = [5, 3, 9, 10, -1]
min_number = [0]
for number in numbers:
    if (number < min_number):
    min_number = number
print(min_number, "is the min value")

# iterate over strings
planets = ["sun", "mercury", "earth"]
for planet in planets:
    if (planet == "sun"):
    	print(planet, "is not a planet")
    else:
        print(planet, "is a planet")

# iterate over the string itself
month = 'februrary'
print(month, "is spelled: ")
for x in month:
    print(x, sep = ' ')
    
    
# using range
# iterate over a sequence of 6 numbers, counting backwards from 5 - 0
for x in range(5, -1, -1):
    prints(x)
    
# find the odd numbers between 1 and 1200
odd_numbers = []
for number in range(1, 1201, 1):
    if (number % 2 == 1):
        odd_numbers.append(number)
print(odd_numbers)

# getting user input until the input is hello by while loops
inp = input("Please say hello: ")
while inp != "hello":
    inp = input("Please say hello: ")
print('now it\'s about time!')

# test whether a password is right
password = ''
while password != 'secret':
    password = input("Please enter the pass word: ")
    if password == 'secret':
        print('welcome!')
    else:
        print('sorry, please try again!')
        
# exit a loop using break
x = 1
while x < 10:
    if x == 5:
        break
    print(x)
    x += 1
    
# find the odd numbers between 1-20 except those are multiples of 3
for numbers in range(1, 21):
    if numbers % 2 != 0:
        if numbers % 3 == 0:
            continue
        print(numbers)

# nested loops
# multiplication tables
for i in range(1, 11):
    for j in range(1, 11):
        print("{} * {} = {}".format(i, j, i * j))
        
# 让玩家一直输入整数，直到输入-1退出程序，然后计算输入整数的平均值
num_list = []
num_count = 0
playing = True
sum = 0
avg = 0
while (playing == True):
    num = int(input("Pleas enter an integer: "))
    if num == -1:
        playing = False
    else:
        num_list.append(num)
        num_count += 1

for num in num_list:
    sum += num

avg = sum / num_count

print("the average is", avg)

# reverse a string
before = input('waht\'s the string you want to reverse? ')
reverse = ''

for i in range(len(before) - 1, -1, -1):
    reverse += before[i]
print(reverse)

# squre function by def
def square(x):
    y = x * x
    return y
result = square(10)
print(result)

# define a greater than function
def greater_than(x, y):
    """ Returns True if x is greater than y, otherwise Flase. -- this is a docstring
    """
    if x > y:
        return True
    else:
        return False

a = 2
b = 3
result = greater_than(a, b)
print("{} is greater than {}: {}".format(a, b, result))
help(greater_than)
# Retruns a list of factors of given number x
def get_factors(x):
    """ Retruns a list of factors of given number x"""
    factors = []
    for number in range(1, x+1):
        if x % number == 0:
            factors.append(number)
    return factors
result = get_factors(135)
print(result)
# Returns a list of unique values from given list l
def unique_list(l):
    """Returns a list of unique values from given list l"""
    x = []
    for i in l:
        if i not in x:
            x.append(i)
    return x
print(unique_list([1, 2, 3, 3, 3, 4, 5, 6]))

# removes whitespaces from the beginning and end of sentence
sentence.strip()

# word count and vowel count 
# 1. count vowels in a string
# 2. count how many word in a string

def count_instance(string1, string2):
    count = 0
    for char in string1:
        if char in string2:
            count += 1
    return count

def vowel_counter(string):
    vowel_count = count_instance(string, 'aeiou')
    return vowel_count

def word_counter(string):
    string = string.strip()
    word_count = count_instance(string, ' ') + 1
    return word_count

def main():
    while 1 == 1:
        sentence = input("enter a string: ")
        if sentence == '-1':
            break
        print('there are ', word_counter(sentence), ' words and ', vowel_counter(sentence), ' vowels in ', sentence)

if __name__ == '__main__':
    main()
# return tuple containing max and min of list
def max_and_min(lst):
    return(max(lst), min(lst))
def main():
    list1 = [1, 2, 3, 4, 5]
    max, min = max_and_min(list1)
    print(max, min)
if __name__ == "__main__":
    main()
    
```



## week 1

### 2. introduction to programming

common client-side programming languages are HTML, CSS, and JavaScript (they run on client side like on a web browser)

server-side programs run on a server (or computer)

common server-side programming languages are Python, java, php, and ASP.NET

### 3. introduction to python

python is a high-level programming language:

1. provides abstraction from the details of the computer

python is an object-oriented programming language (OOP):

1. runs around objects rather than actions.

python is an interpreted programming language / Java is a compiled programming language

python is an open-source program



#### jupyter notebook shortcuts

- To execute code in a cell in a notebook
  Select the cell and press CTRL + Enter
- To execute code in a cell in a notebook, and select the next cell
  Select the cell and press Shift + Enter
- To insert a cell above
  Select the cell and press a
-  To insert a cell below
  Select the cell and press b
-  To delete a cell
  Select the cell and press dd
- To get help with Jupyter Notebook (Keyboard shortcuts)
  Anywhere outside of a cell, press hst
-  To get help with a Python function
  Put cursor inside parenthesis of function, and press Shift + Tab

### 4. configuring python and tools

### 5. the python language

print()里面单引号双引号都可以

print('', end = ' ') 将这一句以end的字符为结尾，然后直接连上下一行的句子

print('', sep = ' ') 改变两字符串之间的间隔符号

arithmetic operator:

`+` additon

`-` subtraction

`*` mutiplication

`/` division



### Assignment 1A

// integer division 3//2 = 1

** exponent 2**3 = 8

% modulus 7%5=2 can calculate the remainder of 

round() 取四舍五入

比零大的是true

type()用来判断一个变量的类型

用Int()来强制转换成整数、

q12 = "4 % 2 = " + str(4 % 2)

将string 类型*2 意味着将整个string 重复2遍

```python
fav_movie = input("what's your favorite movie?")
fav_singer = input("who's your favorite singer?")
favs = "Your favoirte movie is {} and your favorite singer is {}".format(fav_movie, fav_singer)
```

```python
grade = input("enter your grade: ")
grade = int(grade)
if grade >= 90:
    print('A')
elif grade >= 80:
    print('B')
elif grade >= 70:
    print('C')
elif grade >= 60:
    print('D')
else :
    print('F')
```

```python
number = input("what's your number")
try:
    number = int(number)
except ValueError as e:
    print("your input is not an integer.")
    print(e)
else:
    print(str(number) + "is indeed an integer")
    
```

```python
number = input('please enter an integer.')
try: 
    number = int(number)
    if (number > 20)
        print("your input:" + str(number) +">20")
    if (number > 10)
        print("your input:" + str(number) +">10")
    if (number > 0)
        print("your input:" + str(number) +">0")
except ValueError as e:
    print("your input is not an integer")
```

### Assignment 1B

```python
import traceback

def calculator():
    
    # Get dog age
    age = input("Input dog years: ")

    try:
        # Cast to float
        d_age = float(age)

        # If user enters negative number, print message
        # Otherwise, calculate dog's age in human years
        # your code here
        if d_age < 0:
            print("Age cannot be a negative number.")
            return
        elif d_age <= 1:
            human_age = 15 * d_age
        elif d_age <=2:
            human_age = 12 * d_age
        elif d_age <=3:
            human_age = 9.3 * d_age
        elif d_age <=4:
            human_age = 8 * d_age
        elif d_age <=5:
            human_age = 7.2 * d_age
        else:
            human_age = 36 + (d_age - 5) * 7 
        h_age = round(human_age, 2)
        print("The given dog age " + str(d_age) + " is " + str(h_age) + " in human years.")

    except ValueError as e:
        print(age, "is an invalid age.")
        print(traceback.format_exc())
    
calculator() # This line calls the calculator function
```

## week 2

learn about data structures, loops,  and functions

### lists

### loops

for loops : Run a piece of code for a given number of times

while loops: Run a piece of code indefinitely while a condition is met

number is a dummy variable (哑变量)

Format: range(start, up_to, step) 注意up_to是不包含这个总数值的的

### functions

def functio_name(parameter1, parameter2, ...):

​	statements

​	return

### docstring

A docstring describes the operation of the function

A docstring is for someone who is using your function to know "what it does", but not like comment on "how it works"

To create a docstring, include a string as the first statement in the function definition

a docstring can be used by using

```python
help(function_name)
# or you can use print function
print(function_name._doc_)
```

### Execution Order

• Before executing code in a module (file), Python will define a few special variables

- If the Python interpreter is running the file as the main program, it sets the special
__name__ variable to have a value "__main__”
- If the file is being imported from another module, __name__ will be set to that module’s
(file’s) name
• To direct the Python interpreter when it first reads a file, add the following conditional (to the
bottom) of your script:
if __name__ == "__main__ ”:
main()
- This will run the main function, if the file is loaded as the main program
- Note:
__name__ has 2 underscores before and after “name”
__main__ has 2 underscores before and after “main”

### Assignment 2

```python
def getFactors(x):
    """Returns a list of factors of the given number x.
    Basically, finds the numbers between 1 and the given integer that divide the number evenly.

    For example:
    - If we call getFactors(2), we'll get [1, 2] in return
    - If we call getFactors(12), we'll get [1, 2, 3, 4, 6, 12] in return
    """

    # your code here
    factors = []
    for i in range(1, x + 1):
        if x % i == 0:
            factors.append(i)
    return factors


def isPrime(x):
    """Returns whether or not the given number x is prime.

    A prime number is a natural number greater than 1 that cannot be formed
    by multiplying two smaller natural numbers.

    For example:
    - Calling isPrime(11) will return True
    - Calling isPrime(71) will return True
    - Calling isPrime(12) will return False
    - Calling isPrime(76) will return False
    """

    # your code here
    factor_count = len(getFactors(x))
    if factor_count == 2:
        return True
    else:
        return False


def isComposite(x):
    """Returns whether or not the given number x is composite.

    A composite number has more than 2 factors.
    A natural number greater than 1 that is not prime is called a composite number.
    Note, the number 1 is neither prime nor composite.

    For example:
    - Calling isComposite(9) will return True
    - Calling isComposite(22) will return True
    - Calling isComposite(3) will return False
    - Calling isComposite(41) will return False
    """

    # your code here
    if isPrime(x) == True:
        return False
    elif x == 1:
        return False
    else:
        return True


def isPerfect(x):
    """Returns whether or not the given number x is perfect.

    A number is said to be perfect if it is equal to the sum of all its
    factors (for obvious reasons the list of factors being considered does
    not include the number itself).

    Example: 6 = 3 + 2 + 1, hence 6 is perfect.
    Example: 28 is another example since 1 + 2 + 4 + 7 + 14 is 28.
    Note, the number 1 is not a perfect number.
    """

    # your code here
    factors_sum = -x
    factors = getFactors(x)
    for i in factors:
        factors_sum += i
    if x == factors_sum:
        return True
    else:
        return False


def isAbundant(x):
    """Returns whether or not the given number x is abundant.

    A number is considered to be abundant if the sum of its factors
    (aside from the number) is greater than the number itself.

    Example: 12 is abundant since 1+2+3+4+6 = 16 > 12.
    However, a number like 15, where the sum of the factors.
    is 1 + 3 + 5 = 9 is not abundant.
    """

    # your code here
    factors_sum = -x
    factors = getFactors(x)
    for i in factors:
        factors_sum += i
    if x < factors_sum:
        return True
    else:
        return False


def isTriangular(x):
    """Returns whether or not a given number x is triangular.

    The triangular number Tn is a number that can be represented in the form of a triangular
    grid of points where the first row contains a single element and each subsequent row contains
    one more element than the previous one.

    We can just use the fact that the nth triangular number can be found by using a formula: Tn = n(n + 1) / 2.

    Example: 3 is triangular since 3 = 2(3) / 2
    3 --> 2nd position: (2 * 3 / 2)

    Example: 15 is triangular since 15 = 5(6) / 2
    15 --> 5th position: (5 * 6 / 2)
    """

    # your code here
    n = (-1 + (1 + 8 * x) ** 0.5) / 2
    if n % 1 == 0:
        return True
    else:
        return False


def isNarcissistic(x):
    """Returns whether or not a given number is Narcissistic.

    A positive integer is called a narcissistic number if it
    is equal to the sum of its own digits each raised to the
    power of the number of digits.

    Example: 153 is narcissistic because 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.
    Note that by this definition all single digit numbers are narcissistic.
    """

    # your code here
    sum = 0
    replace = x
    n = len(str(x))
    for i in range(n - 1, -1, -1):
        sum += (x // (10 ** i)) ** n
        x -= (x // (10 ** i)) * ((10 ** i))
    if replace == sum:
        return True
    else:
        return False


def main():
    playing = True
    while playing == True:

        num_input = input('Give me a number from 1 to 10000.  Type -1 to exit. ')

        try:
            num = int(num_input)

            if (num == -1):
                playing = False
                continue

            if (num <= 0 or num > 10000):
                continue

            factors = getFactors(num)
            print("The factors of", num, "are", factors)

            if isPrime(num):
                print(str(num) + ' is prime')
            if isComposite(num):
                print(str(num) + ' is composite')
            if isPerfect(num):
                print(str(num) + ' is perfect')
            if isAbundant(num):
                print(str(num) + ' is abundant')
            if isTriangular(num):
                print(str(num) + ' is triangular')
            if isNarcissistic(num):
                print(str(num) + ' is narcissistic')

        except ValueError:
            print('Sorry, the input is not an int.  Please try again.')


# This will automatically run the main function in your program
# Don't change this
if __name__ == '__main__':
    main()

```

## week3 lists, sets, tuples and strings

### lists

list.pop()

list.append()

list.insert(2, 'insert item') #将在第三个位置插入insert item

list1 + list2

list1 * 3

list-slice : list[start(included):end(not included)]   比如my_list[2:5]或者mylist[2:]直接到最后或者mylist[:]直接全部

copy_my_list = my_list[:]

name.index('')

- string.capitalize() – capitalizes first letter of string
- string.startswith(prefix) – determines if string starts with prefix 
- string.endswith(suffix) – determines if string ends with suffix 
- string.isupper() – determines if all characters in the string are uppercase 
- string.islower() – determines if all characters in the string are lowercase 
- string.find(str) – determines if str occurs in string
- string.index(str) – determines index of str in string 
- *i love pythonstring.replace(old, new) – replaces all occurrences of old in string with new 
- string.strip() – trims whitespace from beginning and end of string 
- string.upper() - returns uppercased string from given string 
- string.lower() - returns lowercased string from given string

string.split(',')

colors = ','.join(colors_list)

```python
#here is a string with my favorite restaurant
my_restaurant_choice = 'Mcdonalds'

#convert the string to a list
my_restaurant_choice_list = list(my_restaurant_choice)
#update the third item in the list
my_restaurant_choice_list[2] = 'D'
#covert the list back to a string
my_restaurant_choice = ''.join(my_restaurant_choice_list)

print(my_restaurant_choice)
```

### tuples

tuple = ('a', 'b', 'c')

tuple = 'a', 'b', 'c'

tuple = tuple("abc") 会转化成单个item

### sets

a set is an unordered collection

the order doesn't matter and can't be specified

does not allow repeated elements

are mutable

fruit = {'apple', 'orange', 'banana'}



a = 'abcncnijdsifjoldjfl'

a_set = set(a)



a = [1,2,3,4,5]

a_set = setr(a)

empty_set = set()

```python
#create a set from a string with the set function
a = 'abracadabra'
a_set = set(a)

#create a set from a list with the set function
b = [1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10]
b_set = set(b)

#iterate over a_set
for c in a_set:
    print(c, end = ' ')
#iterate over b_set
for n in b_set:
    print(n, end = ' ')

print('')

#add to a_set
a_set.add('c')
print(a_set)

#remove from b_set
b_set.remove(10)
print(b_set)
```

### homework 3

```python
def concatenate(strings):
    """
    Concatenates the given list of strings into a single string.
    Returns the single string.
    If the given list is empty, returns an empty string.

    For example:
    - If we call concatenate(["a","b","c"]), we'll get "abc" in return
    - If we call concatenate([]), we'll get "" in return

    Hint(s):
    - Remember, you can create a single string from a list of multiple strings by using the join() function
    """
    # your code here
    single_string = ''.join(strings)
    return single_string

def all_but_last(seq):
    """
    Returns a new list containing all but the last element in the given list.
    If the list is empty, returns None.

    For example:
    - If we call all_but_last([1,2,3,4,5]), we'll get [1,2,3,4] in return
    - If we call all_but_last(["a","d",1,3,4,None]), we'll get ["a","d",1,3,4] in return
    - If we call all_but_last([]), we'll get None in return
    """
    # your code here
    if seq == []:
        return None
    else:
        seq.pop()
        return seq
    
def remove_duplicates(lst):
    """
    Returns the given list without duplicates.
    The order of the returned list doesn't matter.

    For example:
    - If we call remove_duplicates([1,2,1,3,4]), we'll get [1,2,3,4] in return
    - If we call remove_duplicates([]), we'll get [] in return

    Hint(s):
    - Remember, you can create a set from a string, which will remove the duplicate elements
    """
    
    # your code here
    removed_list = []
    if lst == []:
        return []
    else:
        a = set(lst)
        for x in a:
            removed_list.append(x)
        return removed_list

def reverse_word(word):
    """
    Reverses the order of the characters in the given word.

    For example:
    - If we call reverse_word("abcde"), we'll get "edcba" in return
    - If we call reverse_word("a b c d e"), we'll get "e d c b a" in return
    - If we call reverse_word("a  b"), we'll get "b  a" in return
    - If we call reverse_word(""), we'll get "" in return

    Hint(s):
    - You can iterate over a word in reverse and access each character
    """
    
    # your code here
    n = len(word)
    reverse = ''
    for i in range(n - 1, -1, -1):
        reverse += word[i]
    return reverse

def divisors(n):
    """
    Returns a list with all divisors of the given number n.
    As a reminder, a divisor is a number that evenly divides another number.
    The returned list should include 1 and the given number n itself.
    The order of the returned list doesn't matter.

    For example:
    - If we call divisors(10), we'll get [1,2,5,10] in return
    - If we call divisors(1), we'll get [1] in return
    """
    # your code here
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

def capitalize_or_join_words(sentence):
    """
    If the given sentence starts with *, capitalizes the first and last letters of each word in the sentence,
    and returns the sentence without *.
    Else, joins all the words in the given sentence, separating them with a comma, and returns the result.

    For example:
    - If we call capitalize_or_join_words("*i love python"), we'll get "I LovE PythoN" in return.
    - If we call capitalize_or_join_words("i love python"), we'll get "i,love,python" in return.
    - If we call capitalize_or_join_words("i love    python  "), we'll get "i,love,python" in return.

    Hint(s):
    - The startswith() function checks whether a string starts with a particualr character
    - The capitalize() function capitalizes the first letter of a string
    - The upper() function converts all lowercase characters in a string to uppercase
    - The join() function creates a single string from a list of multiple strings
    """
    # your code here
    if sentence.startswith("*") == True:
        sentence = sentence.replace("*", "")
        sentence = sentence.title()
        result = ''
        for word in sentence.split():
            result += word[:-1] + word[-1].upper() + " "
        return result[:-1]
    else:
        s = sentence.split()
        joined_sentence = ",".join(s)
        return joined_sentence
    
def move_zero(lst):
    """
    Given a list of integers, moves all non-zero numbers to the beginning of the list and
    moves all zeros to the end of the list.  This function returns nothing and changes the given list itself.

    For example:
    - After calling move_zero([0,1,0,2,0,3,0,4]), the given list should be [1,2,3,4,0,0,0,0] and the function returns nothing
    - After calling move_zero([0,1,2,0,1]), the given list should be [1,2,1,0,0] and the function returns nothing
    - After calling move_zero([1,2,3,4,5,6,7,8]), the given list should be [1,2,3,4,5,6,7,8] and the function returns nothing
    - After calling move_zero([]), the given list should be [] and the function returns nothing
    """
    # your code here
    non_zero = []
    only_zero = []

    for number in lst:
        if number != 0:
            non_zero.append(number)
        else:
            only_zero.append(number)
    given_list = non_zero + only_zero
    
    for i in range(0, len(given_list)):
        lst[i] = given_list[i]
    
    return

def main():
    """
    Calls all the functions above to see whether they've been implemented correctly.
    """

    # test concatenate
    print("test concatenate")
    word = concatenate(["b", "e", "a", "t", "l", "e", "s"])
    print(word == "beatles")
    print("=" * 50)

    # test all_but_last
    print("test all_but_last")
    seq = all_but_last(["john", "paul", "george", "ringo", "tommy"])
    print(seq == ["john", "paul", "george", "ringo"])
    print("=" * 50)

    # test remove_duplicates
    print("test remove_duplicates")
    res = remove_duplicates([1, 3, 4, 2, 1])
    print(res == [1, 3, 4, 2])
    print("=" * 50)

    # test reverse_word
    print("test reverse_word")
    res = reverse_word("alphabet")
    print(res == "tebahpla")
    print("=" * 50)

    # test divisors
    print("test divisors")
    res = divisors(120)
    print(set(res) == set([1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 24, 30, 40, 60, 120]))
    print("=" * 50)

    # test capitalize_or_join_words
    print("test capitalize_or_join_words")
    print("Result for String Start With *: ")
    # Should return "I LovE CodinG AnD I'M HavinG FuN"
    res = capitalize_or_join_words("*i love coding and i'm having fun")
    print(res == "I LovE CodinG AnD I'M HavinG FuN")

    print("Result for Other String: ")
    # Should print "I,love,coding,and,I'm,having,fun"
    res = capitalize_or_join_words("I love coding and I'm having fun")
    print(res == "I,love,coding,and,I'm,having,fun")
    print("=" * 50)

    # test move_zero
    print("test move_zero")
    lst = [0, 1, 0, 2, 0, 3, 4, 0]
    print("Before move,the list looks like\n", lst)
    move_zero(lst)
    print("After move,the list looks like\n", lst)
    print("=" * 50)

#This will automatically run the main function in your program
#Don't change this
if __name__ == '__main__':
    main()
```

## week 4 data structure: dictionaries / external files

### dictionaries

A dictionary (dict) is another way to store data, like a list or set, but as unordered key-value pairs.

To create a dict, use comma separated key:value pairs, in between curly braces {}

Dictionaries are mutable, so once defined, elements can be changed

```python
person = {'name': 'Brandon', "age": 45, 'height': 6 * 5 +2}
print(type(person))
print(person['name'])
print(person.get("name"))
print(person.get("country", "AAA")) # 如果country这个key不存在，那么会返回AAA

person = {'name': 'Brandon', "age": 45, 'height': 6 * 5 +2}
print(type(person))
print(person['name'])
print(person.get("name"))
print(person.get("country", "AAA"))
print(person["age"])

"""change the elements in the dictionary"""
person["name"] = "lechi"
person['age'] += 1
person["college"] = "ZJU"
print(person["name"])
print(person.get("age"))
print(person.get("college"))
print("college" in person)
del person["college"]
print(person)
```

```python
# crreate dictionaries for students
billy = {
    'name' : 'Billy',
    'grades': [1, 2, 3, 4, 5],
    'attendance': [True, True, False]
}

sarah = {
    'name' : 'Sarah',
    'grades': [2, 3, 4, 5, 6],
    'attendance': [False, False, False]
}

ben = {
    'name': "Ben",
    'grades': [2, 3, 4, 5, 6],
    'attendance': [False, True, True]
}

students = {'1': billy, '2': sarah, '3':ben}

#get number of students
print(len(students))

#get all keys
print(students.keys())

#iterate over students to get keys
for k in students:
    print('key is ', k)

#get billy's attendance
billy_attendance = students['1']
print(billy_attendance['attendance'])

#get key:value paris for ben
ben = students.get('3')
item = ben.items() #returns sequence of tuples
for key,val in item:
    print(key, val)

#get average student grade for all assignments
grades = []
student_items = students.items()
for key,val in student_items:
    for g in val['grades']:
        grades.append(g)
print(round(sum(grades) / len(grades)))

#another way by using list concatenate
grades_concatenated = []
student_items = students.items()
for key,val in student_items:
    grades_concatenated += val['grades']
print(round(sum(grades_concatenated) / len(grades)))
```

### files

open a file: ` open(path_to_file, mode)`

mode: r-read, w-write to the file, a-append to the end fo an already existing file, r+ - read and write to the file at the same time 

open(<my file>, 'r')   如果文件不存在会报错

open(<my_file>, 'w') 会把里面的旧数据全部删除，如果文件不存在会新建一个

open(<my_file>, 'r+')  如果文件不存在会报错,不会抹除旧数据

You can use a stream to read lines from a file
• read: Reads an entire file as a string
lines = stream.read() #reads all text in the file
• readline: Reads a file line by line. Each line is read as a string.
line = stream.readline() #reads one line in the file
• readlines: Reads all lines in a file as a list. Each line in the list will be a string.
lines_lst = stream.readlines() #reads all lines in the file as a list
• With the above methods, you must remember to close the stream when you’re done
stream.close() #closes the file object

line = stream.readline()

line.strip() #removes all the withspaces, including \n characters

You can also use a stream to write lines to a file
• write: Writes a single string to a file
stream.write(string)
• writelines: Writes a list of strings to a file
stream.writelines(list_of_strings)
• Again, with the above methods, you must remember to close the stream when you’re done
stream.close()

#### close the file

```python
stream = open(<my_file>, 'w')
stream.close()

with open(<my_file>, 'w') as stream # with会自动将文件close
```

```python
"""create an open_read_file function that opens a given file, reads each line and prints it to the console"""
def open_read_file(file):
    f = open(file, 'r')
    print(type(f)) # <class '_io.TextIOWrapper'>

    line_number = 0
    # reads and prints each line in f, while there is a line to read
    line = f.readline() # read the first line in file
    while line:
        print(line, end='')
        line = f.readline()
        line_number += 1
    print('')
    print('there are', line_number, "lines in the file")
    f.close()

"""create an open_read_append_new_file function that opens and reads one file, revers the text,
then appends the reversed text to another file"""
def open_read_append_new_file(file1, file2):
    """opens the first file, and reads all line into a list.
    Reveres the lines, and appends them to the second file."""
    with open(file1) as fin:
        lst = fin.readlines()
        lst.reverse()
        fout = open(file2, "a")
        fout.writelines(lst)
        fout.close()

def open_read_append_same_file(file):
    f = open(file, 'r+')
    lst = f.readlines()
    lst.insert(0, '\n')
    lst.insert(0, 'here is some new lines')
    lst.insert(0, '\n')

    f.writelines(lst)
    f.close()

def open_read_write_new_file(file1, file2):
    """opens the first file and reads all text as a string.
    Copies or writes all text to the second file"""
    with open(file1) as fin:
        text = fin.read()
        fout = open(file2, "w")
        fout.write(text)
        fout.close()

def main():
    #open_read_file('gre.txt')
    #open_read_append_new_file("gre.txt", "gre_out.txt")
    #open_read_append_same_file("gre.txt")
    open_read_write_new_file("gre.txt", "gre2.txt")

if __name__ == '__main__':
    main()
```

```python
def import_and_create_dictionary(filename):
    expenses = {}
    f = open(filename, "r")
    lines = f.readlines()

    for line in lines:
        lst = line.strip().split(",")

        if len(lst) <= 1:
            continue

        key = lst[0].strip()
        value = lst[1].strip()

        try:
            value = float(value)
            expenses[key] = expenses.get(key, 0) + value
        except:
            continue

    f.close()

    return expenses

def main():
    expenses = import_and_create_dictionary("expenses.txt")
    print("expenses: ", expenses)

if __name__ == "__main__":
    main()
```

The method write() writes from the start of the file, so the old first line in the file will be overwritten by the new line.

The readlines() method reads all lines in the file as a list, and the lines should be stored in a list.



### homework 4

```python
"""first cell"""
def import_and_create_bank(filename):
    # create an empty bank dictionary
    bank = {}
    # read the file
    f = open(filename, "r")
    # since every line represents one user, apply readlines() to create a list
    lines = f.readlines()
    # iterate over all the lines
    for line in lines:
        # strip white spaces and split line into list based on ":"
        lst = line.strip().split(":")
        # skip the line with only key or value
        if len(lst) <= 1:
            continue
        # assign name to key and deposit to value
        key = lst[0].strip()
        value = lst[1].strip()
        # skip if the deposit is not number
        try:
            value = float(value)
            bank[key] = bank.get(key, 0) + value
        except:
            continue
    # print(bank)
    # close the file
    f.close()
    return bank

"""second cell"""
def check_upper(password):
    for char in password:
        if char.isupper():
            return True
    return False

def check_lower(password):
    for char in password:
        if char.islower():
            return True
    return False

def check_number(password):
    for char in password:
        if char.isdigit():
            return True
    return False

def validation(user_accounts, username, password):
    """test whether the username and the password are both valid.
    User_accounts is a dictionary contains all user names"""
    if (username not in user_accounts) and len(password) >= 8 and check_upper(password) and check_lower(password) and check_number(password) and username != password:
        return True
    else:
        return False


def signup(user_accounts, log_in, username, password):

    if validation(user_accounts, username, password):
        user_accounts[username] = password
        log_in[username] = False
        return True
    else:
        return False

"""third cell"""
def import_and_create_accounts(filename):
    # Create an empty user accounts dictionary and an empty login dictionary
    user_accounts = {}
    log_in = {}
    # read the file
    f = open(filename, "r")
    # since every line represents one user, apply readlines() to create a list
    lines = f.readlines()
    # iterate over all the lines
    for line in lines:
        # strip white spaces and split line into list based on ":"
        lst = line.strip().split("-")
        # skip the line with only key or value
        if len(lst) <= 1:
            continue
        # assign name to key and deposit to value
        key = lst[0].strip()
        value = lst[1].strip()
        if validation(user_accounts, key, value):
            user_accounts[key] = value
            log_in[key] = False
        else:
            continue
    f.close()
    #print(user_accounts)
    #print(log_in)
    return user_accounts, log_in


"""fourth cell"""
def login(user_accounts, log_in, username, password):
    if (username not in user_accounts) or (password != user_accounts[username]):
        return False
    else:
        log_in[username] = True
        return True

"""fifth cell"""
def update(bank, log_in, username, amount):
    if log_in[username] != True:
        return False

    if username not in bank:
        bank[username] = 0

    if amount + bank[username] < 0:
        return False
    else:
        bank[username] += amount
        return True

"""sixth cell"""
def transfer(bank, log_in, userA, userB, amount):
    if userA not in bank or log_in[userA] != True:
        return False
    if userB not in log_in:
        return False
    if userB not in bank:
        bank[userB] = 0
    if bank[userA] - amount < 0:
        return False
    else:
        bank[userA] -= amount
        bank[userB] += amount
        return True

"""seventh cell"""
def change_password(user_accounts, log_in, username, old_password, new_password):
    if username not in user_accounts:
        return False
    elif log_in[username] != True:
        return False
    elif user_accounts[username] != old_password:
        return False
    elif old_password == new_password:
        return False
    elif len(new_password) >= 8 and check_upper(new_password) and check_lower(new_password) and check_number(new_password) and username != new_password:
        user_accounts[username] = new_password
        return True

"""eighth cell"""
def delete_account(user_accounts, log_in, bank, username, password):
    if username not in user_accounts or password != user_accounts[username] or log_in[username] != True:
        return False
    else:
        del user_accounts[username]
        del log_in[username]
        del bank[username]
        return True



def main():
    '''
    The main function is a skeleton for you to test if your overall programming is working.
    Note we will not test your main function. It is only for you to run and interact with your program.
    '''

    bank = import_and_create_bank("bank.txt")
    user_accounts, log_in = import_and_create_accounts("user.txt")

    while True:
        # for debugging
        print('bank:', bank)
        print('user_accounts:', user_accounts)
        print('log_in:', log_in)
        print('')
        #

        option = input("What do you want to do?  Please enter a numerical option below.\n"
        "1. login\n"
        "2. signup\n"
        "3. change password\n"
        "4. delete account\n"
        "5. update amount\n"
        "6. make a transfer\n"
        "7. exit\n")
        if option == "1":
            username = input("Please input the username\n")
            password = input("Please input the password\n")

            # add code to login
            login(user_accounts, log_in, username, password);
        elif option == "2":
            username = input("Please input the username\n")
            password = input("Please input the password\n")

            # add code to signup
            signup(user_accounts, log_in, username, password)
        elif option == "3":
            username = input("Please input the username\n")
            old_password = input("Please input the old password\n")
            new_password = input("Please input the new password\n")

            # add code to change password
            change_password(user_accounts, log_in, username, old_password, new_password)
        elif option == "4":
            username = input("Please input the username\n")
            password = input("Please input the password\n")

            # add code to delete account
            delete_account(user_accounts, log_in, bank, username, password)
        elif option == "5":
            username = input("Please input the username\n")
            amount = input("Please input the amount\n")
            try:
                amount = float(amount)

                # add code to update amount
                update(bank, log_in, username, amount)
            except:
                print("The amount is invalid. Please reenter the option\n")

        elif option == "6":
            userA = input("Please input the user who will be deducted\n")
            userB = input("Please input the user who will be added\n")
            amount = input("Please input the amount\n")
            try:
                amount = float(amount)

                # add code to transfer amount
                transfer(bank, log_in, userA, userB, amount)
            except:
                print("The amount is invalid. Please re-enter the option.\n")
        elif option == "7":
            break;
        else:
            print("The option is not valid. Please re-enter the option.\n")

#This will automatically run the main function in your program
#Don't change this
if __name__ == '__main__':
    main()









































 
```



comment

```python
def import_and_create_bank(filename):
    '''
    This function is used to create a bank dictionary.  The given argument is the filename to load.
    Every line in the file should be in the following format:
        key: value
    The key is a user's name and the value is an amount to update the user's bank account with.  The value should be a number, however, it is possible that there is no value or that the value is an invalid number.

    What you will do:
    # - Create an empty bank dictionary.
    - Read in the file.
    - Add keys and values to the dictionary from the contents of the file.
    - If the key doesn't exist in the dictionary, create a new key:value pair.
    - If the key does exist in the dictionary, increment its value with the amount.
    - You should also handle the following cases:
    -- When the value is missing or invalid.  If so, ignore that line and don't update the dictionary.
    -- When the line is completely blank.  Again, ignore that line and don't update the dictionary.
    -- When there is whitespace at the beginning or end of a line and/or between the name and value on a line.  You
    should trim any and all whitespace.
    - Return the bank dictionary from this function.

    For example, here's how your code should handle some specific lines in the file:
    The 1st line in the file has a name and valid number:
        Brandon: 5
    Your code will process this line and add the extracted information to the dictionary.  After it does,
    the dictionary will look like this:
        bank = {"Brandon": 5}

    The 2nd line in the file also has a name and valid number:
        Patrick: 18.9
    Your code will also process this line and add the extracted information to the dictionary.  After it does,
    the dictionary will look like this:
        bank = {"Brandon": 5, "Patrick": 18.9}

    The 3rd line in the file has a name but invalid number:
        Brandon: xyz
    Your code will ignore this line and add nothing to the dictionary.  It will still look like this:
        bank = {"Brandon": 5, "Patrick": 18.9}

    The 4th line in the file has a name but missing number:
        Jack:
    Your code will ignore this line and add nothing to the dictionary.  It will still look like this:
        bank = {"Brandon": 5, "Patrick": 18.9}

    The 5th line in the file is completely blank.
    Your code will ignore this line and add nothing to the dictionary.  It will still look like this:
        bank = {"Brandon": 5, "Patrick": 18.9}

    The 8th line in the file has a name and valid number, but with extra whitespace:
        Brandon:       10
    Your code will process this line and update the value associated with the existing key ('Brandon') in the dictionary.
    After it does, the value associated with the key 'Brandon' will be 10:
        bank = {"Brandon": 15, ...}

    After processing every line in the file, the dictionary will look like this:
        bank = {"Brandon": 115.5, "Patrick": 18.9, "Sarah": 827.43, "Jack": 45.0, "James": 128.87}
    Return the dictionary from this function.
    '''
        # open file in read mode
    f = open(filename, "r")

    # get all lines in file as a list
    lines = f.readlines()

    for line in lines:
        # strip white spaces from beginning and end of line
        # split line into list based on ":" separator
        lst = line.strip().split(":")

        # skip line if it does not have a name
        if len(lst) <= 1:
            continue

        key = lst[0].strip()
        value = lst[1].strip()

        try:
            value = float(value)
            bank[key] = bank.get(key, 0) + value
        except:
            continue

    f.close()
    # print(bank)
    
    
    
    
    
    def signup(user_accounts, log_in, username, password):
    '''
    This function allows users to sign up.
    If both username and password meet the requirements:
    - Updates the username and the corresponding password in the user_accounts dictionary.
    - Updates the log_in dictionary, setting the value to False.
    - Returns True.

    If the username and password fail to meet any one of the following requirements, returns False.
    - The username already exists in the user_accounts.
    - The password must be at least 8 characters.
    - The password must contain at least one lowercase character.
    - The password must contain at least one uppercase character.
    - The password must contain at least one number.
    - The username & password cannot be the same.

    For example:
    - Calling signup(user_accounts, log_in, "Brandon", "123abcABCD") will return False
    - Calling signup(user_accounts, log_in, "BrandonK", "123ABCD") will return False
    - Calling signup(user_accounts, log_in, "BrandonK","abcdABCD") will return False
    - Calling signup(user_accounts, log_in, "BrandonK", "123aABCD") will return True. Then calling
    signup(user_accounts, log_in, "BrandonK", "123aABCD") again will return False.

    Hint: Think about defining and using a separate valid(password) function that checks the validity of a given password.
    This will also come in handy when writing the change_password() function.
    '''
    
    def import_and_create_accounts(filename):
    '''
    This function is used to create an user accounts dictionary and another login dictionary.  The given argument is the
    filename to load.
    Every line in the file should be in the following format:
      username - password
    The key is a username and the value is a password.  If the username and password fulfills the requirements,
    add the username and password into the user accounts dictionary.  To make sure that the password fulfills these
    requirements, be sure to use the signup function that you wrote above.

    For the login dictionary, the key is the username, and its value indicates whether the user is logged in, or not.
    Initially, all users are not logged in.

    What you will do:
    - Create an empty user accounts dictionary and an empty login dictionary.
    - Read in the file.
    - If the username and password fulfills the requirements, adds the username and password
    into the user accounts dictionary, and updates the login dictionary.
    - You should also handle the following cases:
    -- When the password is missing.  If so, ignore that line and don't update the dictionaries.
    -- When there is whitespace at the beginning or end of a line and/or between the name and password on a line.  You
    should trim any and all whitespace.
    - Return both the user accounts dictionary and login dictionary from this function.

    For example, here's how your code should handle some specific lines in the file:
    The 1st line in the file has a name and password:
      Brandon - brandon123ABC
    Your code will process this line, and using the signup function, will add the extracted information to the
    dictionaries.  After it does, the dictionaries will look like this:
      user_accounts = {"Brandon": "brandon123ABC"}
      log_in = {"Brandon": False}

    The 2nd line in the file has a name but missing password:
      Jack
    Your code will ignore this line.  The dictionaries will still look like this:
      user_accounts = {"Brandon": "brandon123ABC"}
      log_in = {"Brandon": False}

    The 3rd line in the file has a name and password:
      Jack - jac123
    Your code will process this line, and using the signup function, will not add the extracted information to the
    dictionaries because the password is invalid.  The dictionaries will still look like this:
      user_accounts = {"Brandon": "brandon123ABC"}
      log_in = {"Brandon": False}

    The 4th line in the file has a name and password:
      Jack - jack123POU
    Your code will process this line, and using the signup function, will add the extracted information to the
    dictionaries.  After it does, the dictionaries will look like this:
      user_accounts = {"Brandon": "brandon123ABC, "Jack": "jack123POU"}
      log_in = {"Brandon": False, "Jack": False}

    After processing every line in the file, the dictionaries will look like this:
      user_accounts = {"Brandon": "brandon123ABC, "Jack": "jack123POU", "James": "100jamesABD", "Sarah": "sd896ssfJJH"}
      log_in = {"Brandon": False, "Jack": False, "James": False, "Sarah": False}
    Return the dictionaries from this function.
    '''
    
    
    def login(user_accounts, log_in, username, password):
    '''
    This function allows users to log in with their username and password.
    The user_accounts dictionary stores the username and associated password.
    The log_in dictionary stores the username and associated log-in status.

    If the username does not exist in user_accounts or the password is incorrect:
    - Returns False.
    Otherwise:
    - Updates the user's log-in status in the log_in dictionary, setting the value to True.
    - Returns True.

    For example:
    - Calling login(user_accounts, "Brandon", "123abcAB") will return False
    - Calling login(user_accounts, "Brandon", "brandon123ABC") will return True
    '''

    # your code here
    
    def update(bank, log_in, username, amount):
    '''
    In this function, you will try to update the given user's bank account with the given amount.
    bank is a dictionary where the key is the username and the value is the user's account balance.
    log_in is a dictionary where the key is the username and the value is the user's log-in status.
    amount is the amount to update with, and can either be positive or negative.

    To update the user's account with the amount, the following requirements must be met:
    - The user exists in log_in and his/her status is True, meaning, the user is logged in.

    If the user doesn't exist in the bank, create the user.
    - The given amount can not result in a negative balance in the bank account.

    Return True if the user's account was updated.

    For example, if Brandon has 115.50 in his account:
    - Calling update(bank, log_in, "Brandon", 50) will return False, unless "Brandon" is first logged in.  Then it
    will return True.  Brandon will then have 165.50 in his account.
    - Calling update(bank, log_in, "Brandon", -200) will return False because Brandon does not have enough in his
    account.
    '''

    # your code here
    
    def transfer(bank, log_in, userA, userB, amount):
    '''
    In this function, you will try to make a transfer between two user accounts.
    bank is a dictionary where the key is the username and the value is the user's account balance.
    log_in is a dictionary where the key is the username and the value is the user's log-in status.
    amount is the amount to be transferred between user accounts (userA and userB).  amount is always positive.

    What you will do:
    - Deduct the given amount from userA and add it to userB, which makes a transfer.
    - You should consider some following cases:
      - userA must be in the bank and his/her log-in status in log_in must be True.
      - userB must be in log_in, regardless of log-in status.  userB can be absent in the bank.
      - No user can have a negative amount in their account. He/she must have a positive or zero balance.

    Return True if a transfer is made.

    For example:
    - Calling transfer(bank, log_in, "BrandonK", "Jack", 100) will return False
    - Calling transfer(bank, log_in, "Brandon", "JackC", 100) will return False
    - After logging "Brandon" in, calling transfer(bank, log_in, "Brandon", "Jack", 10) will return True
    - Calling transfer(bank, log_in, "Brandon", "Jack", 200) will return False  
    '''

    # your code here
    
    def change_password(user_accounts, log_in, username, old_password, new_password):
    '''
    This function allows users to change their password.

    If all of the following requirements are met, changes the password and returns True. Otherwise, returns False.
    - The username exists in the user_accounts.
    - The user is logged in (the username is associated with the value True in the log_in dictionary)
    - The old_password is the user's current password.
    - The new_password should be different from the old one.
    - The new_password fulfills the requirement in signup.

    For example:
    - Calling change_password(user_accounts, log_in, "BrandonK", "123abcABC" ,"123abcABCD") will return False
    - Calling change_password(user_accounts, log_in, "Brandon", "123abcABCD", "123abcABCDE") will return False
    - Calling change_password(user_accounts, log_in, "Brandon", "brandon123ABC", "brandon123ABC") will return False
    - Calling change_password(user_accounts, log_in, "Brandon", "brandon123ABC", c"123abcABCD") will return True

    Hint: Think about defining and using a separate valid(password) function that checks the validity of a given password.
    This will also come in handy when writing the signup() function.
    '''

    # your code here
    
    
    def delete_account(user_accounts, log_in, bank, username, password):
    '''
    Completely deletes the user from the online banking system.
    If the user exists in the user_accounts dictionary and the password is correct, and the user 
    is logged in (the username is associated with the value True in the log_in dictionary):
    - Deletes the user from the user_accounts dictionary, the log_in dictionary, and the bank dictionary.
    - Returns True.
    Otherwise:
    - Returns False.

    For example:
    - Calling delete_account(user_accounts, log_in, bank, "BrandonK", "123abcABC") will return False
    - Calling delete_account(user_accounts, log_in, bank, "Brandon", "123abcABDC") will return False
    - If you first log "Brandon" in, calling delete_account(user_accounts, log_in, bank, "Brandon", "brandon123ABC")
    will return True
    '''

    # your code here
```

## Data analysis using Python

## 单词

inspect 检查，审视；检阅

query 质疑，对……表示疑问；询问

aggregation 聚合

## week 1 loading, querying, and filtering data using csv module

1. open file: open(file_name, access_mode)

   access_mode: r, w, a, r+
   
2. the DictReader reads the csv file and maps the information into a dict object

```python
import csv
my_file = open('my_file_path/my_file.csv', 'r')
reader = csv.DictReader(my_file)
my_file.close()

# with cam automatically close the file for you
with open('my_file_path/my_file.csv', 'r') as csvfile:
	reader = csv.DictReader(csvfile)
```

3. close file: my_file.close()

```python
import csv
with open("albumlist.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    print(type(reader))
    print(reader.fieldnames) #这里出现第一行的类别


with open("albumlist.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile) # dictreader只能被读取一次，因为它并不储存在memory里，所以每次最好都dictreader一次
    for row in reader:
        print(row)

with open("albumlist.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    maxrow = 101
    for row in reader:
        maxrow -= 1
        if maxrow > 0:
            print(row)
        else:
            break

with open("albumlist.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    album = []
    for row in reader:
        album.append(row)
    print(len(album))

"""list comprehension is another way to add records to a list.
This consists of an expression, followed by a for loop, inside square brackets[]"""

album_1974 = [row for row in album if row["Year"] == "1974"]
print(len(album_1974))

for album in album_1974:
    print(album['Album'], "by", album["Artist"])

print([row for row in album if row["Year"] == "1974"][:10])

rock_albums = [row for row in album if (row["Genre"] == "Rock"
                                        and ("Pop Rock" in row["Subgenre"] or "Fusion" in row["Subgenre"]))]
for album in rock_albums:
    print(album["Album"], album["Artist"], album["Genre"], album["Subgenre"])


with open("albumlist.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    album = []
    for row in reader:
        album.append(row)


# release_years = [int(row["Year"]) for row in album if row["Year"]]

def is_valid_year(string):
    try:
        year = int(string)
    except ValueError:
        return False
    else:
        return year > 1400
release_years = [int(row["Year"]) for row in album if is_valid_year(row["Year"])]
print(release_years)

min_year = min(release_years)
print(min_year)
albums_sorted = sorted(album, key = lambda x: x["Artist"])
print(albums_sorted)
```

### lambda function

is a one-line mini-function defined on the fly

they can be used anywhere a function is required  

lambda function可以用来在sort、max、min function里面

sorted(list, key)

min(list, key)

max(list, key)

```python
def double(x):
    return x * 2

"""lambda function can be written into"""
double_l = lambda x: x * 2

albums_sorted = sorted(album, key = lambda x: x["Artist"])
或者可以使用
albums_sorted = album.sort(key = lambda x: x["Artist"])
print(albums_sorted)
```

```python
valid_albums = [row for row in albums if is_valid_year(row['Year'])]
album_max = max(valid_albums, key = lambda x: x["Year"])
print(album_max["Album"], album_max["Artist"], album_max["Year"])
```

### homework 1

```csv
# 注意在sort的时候，有reverse = True这个选项，同时在排序时要先将排序的对象（数字）转化为float
```

```python
'''
1. Import the csv module. Load and read the UFO sightings data set, from the ufo-sightings.csv file, 
into a DictReader inside a with statement.  Assume the data file is in the same directory as the code. 

Print the field names of the data set. Iterate over the reader to put the data into a list name "ufosightings".

'''

import csv
filepath = "ufo-sightings.csv"
ufosightings = [] 
with open(filepath, "r") as csvfile:
    reader = csv.DictReader(csvfile)
    print(reader.fieldnames)
    for row in reader:
        ufosightings.append(row)

'''
2. How many sightings were there in total?  Put the count in "ufosightings_count" and print the result.
'''
ufosightings_count = len(ufosightings)
print(ufosightings_count)

'''
3. How many sightings were there in the US?  Put the US sightings in "sightings_us" and print.

Hint: Check for ufo sightings where the country is 'us'.

'''
sightings_us = [row for row in ufosightings if row["country"] == "us"]
print(sightings_us)

'''
4. Let's find the "fireball" sighting(s) that lasted more than ten seconds in US. 
Print the the datetime and state of each.  Put the data in "fball" and print the result.

Note: Consider only the US sightings stored in "sightings_us".

- Cast the duration in seconds to a float (decimal). 
- Check if duration is greater than 10. 
- Check if the shape is "fireball".

'''

#First, define a Python function that checks if a given duration (seconds) is "valid"
def is_valid_duration(duration_as_string):
    try:
        duration = float(duration_as_string)
    except ValueError:
        return False
    else:
        return duration > 10
# your code here
fball = [row for row in sightings_us if is_valid_duration(row["duration (seconds)"]) 
         and row["shape"] == "fireball"]
for fire in fball:
    print(fire["datetime"], fire["state"])

'''
5. Sort the above list by duration. What was the datetime and duration of the longest sighting?  
Put the sorted list in "fballsorted" and print the result.

- Cast the duration in seconds to a float (decimal). 
- Sort in reverse order.

'''
fballsorted = sorted(fball, key = lambda x: float(x["duration (seconds)"]), reverse = True)
fball_max= max(fball, key = lambda x: float(x["duration (seconds)"]))
               
print(fball_max["datetime"], fball_max["duration (seconds)"])

'''
6. What state had the longest lasting "fireball"?   Put the state in "state" and print the result.

- Check if the shape is "fireball".
- Cast the duration in seconds to a float (decimal).
- Get the record with the largest (max) duration in seconds.
- Get the state for the record.

'''
state = fball_max["state"]
print(state)

'''
7. Let's assume that any sighting (of any shape) of 0 seconds is insignificant. 
Write code to filter out these extraneous records and get the shortest sighting overall now.  
Put the minimum duration in "min_duration" and print the result.  
Use ufosightings
Note: Consider all sightings stored in "ufosightings".

'''
min_record = min(ufosightings, key = lambda x: x["duration (seconds)"])
min_duration = float(min_record["duration (seconds)"])
print(min_duration)

'''
8. What are the top 3 shapes sighted, and how many sightings were there for each? 

Note: Consider all sightings stored in "ufosightings".

- Create a new list "sightings_shapes" containing values from the "shape" column in ufosightings.  
- Create a new dictionary "count" with values of that column as keys and the counts as values.
- Get a list of the dictionary keys and values using the items() method.  This will return a list of key:value pairs.
Sort the list of key:value pairs in reverse order, from greatest (most sightings) to least.

Get the top 3 and store in "top3shapes".  Print the result.

'''

#Create a new list containing values from the "shape" column in ufosightings.
# your code here
sightings_shapes = []
for row in ufosightings:
    sightings_shapes.append(row["shape"])
sightings_shapes.sort()
last = sightings_shapes[-1]
for i in range(len(sightings_shapes) - 2, -1, -1):
    if last == sightings_shapes[i]:
        del sightings_shapes[i]
    else: last = sightings_shapes[i]
#Create a new dictionary with values of that column as keys and the counts as values.
# your code here
count = {}
for row in ufosightings:
    count[row["shape"]] = count.get(row["shape"], 0) + 1

        
#Get a list of the dictionary keys and values (use the items() method) and sort them in reverse order, from greatest (most sightings) to least.
#Get and print the top 3.
# your code here

'''
8. What are the top 3 shapes sighted, and how many sightings were there for each? 

Note: Consider all sightings stored in "ufosightings".

- Create a new list "sightings_shapes" containing values from the "shape" column in ufosightings.  
- Create a new dictionary "count" with values of that column as keys and the counts as values.
- Get a list of the dictionary keys and values using the items() method.  This will return a list of key:value pairs.
Sort the list of key:value pairs in reverse order, from greatest (most sightings) to least.

Get the top 3 and store in "top3shapes".  Print the result.

'''

#Create a new list containing values from the "shape" column in ufosightings.
# your code here
sightings_shapes = []
for row in ufosightings:
    sightings_shapes.append(row["shape"])

    

#Create a new dictionary with values of that column as keys and the counts as values.
# your code here
count = {}
for item in sightings_shapes:
    count[item] = count.get(item, 0) + 1

        
#Get a list of the dictionary keys and values (use the items() method) and sort them in reverse order, from greatest (most sightings) to least.
#Get and print the top 3.
# your code here
count_items = count.items()
for key,value in count_items:
    count_items_sorted = sorted(count_items, key = lambda x: x[1], reverse = True)
top3shapes = []
for i in range(3):
    top3shapes.append(count_items_sorted[i])
```




## week 2 loading, querying, joining, and filtering data using pandas









## week 3 summarizing and visualizing data





