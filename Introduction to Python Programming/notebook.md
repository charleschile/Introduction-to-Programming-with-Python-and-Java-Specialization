# introduction to programming with python and java specialization 

# 单词

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

# All the Python functions

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
  Anywhere outside of a cell, press h
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



## Assignment 1A

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

## Assignment 1B

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

## Assignment 2

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

