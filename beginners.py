import streamlit as st
import io
import contextlib

# Function to redirect print statements to Streamlit
@contextlib.contextmanager
def st_redirect():
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        yield output
    st.write(output.getvalue())

# Function to display tutorials and links for beginner Python level
def display_beginner_tutorials():
    st.subheader("Beginner Python Tutorials")
    st.write('''
        ## What is Python?

Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.

## It is used for:

    web development (server-side),
    software development,
    mathematics,
    system scripting.

## What can Python do?

    Python can be used on a server to create web applications.
    Python can be used alongside software to create workflows.
    Python can connect to database systems. It can also read and modify files.
    Python can be used to handle big data and perform complex mathematics.
    Python can be used for rapid prototyping, or for production-ready software development.

'''
             '''
## Why Python?

    Python works on different platforms (Windows, Mac, Linux, Raspberry Pi, etc).
    Python has a simple syntax similar to the English language.
    Python has syntax that allows developers to write programs with fewer lines than some other programming languages.
    Python runs on an interpreter system, meaning that code can be executed as soon as it is written. This means that prototyping can be very quick.
    Python can be treated in a procedural way, an object-oriented way or a functional way.

## Good to know

    The most recent major version of Python is Python 3, which we shall be using in this tutorial. However, Python 2, although not being updated with anything other than security updates, is still quite popular.
    In this tutorial Python will be written in a text editor. It is possible to write Python in an Integrated Development Environment, such as Thonny, Pycharm, Netbeans or Eclipse which are particularly useful when managing larger collections of Python files.

   #### Python Syntax compared to other programming languages

    Python was designed for readability, and has some similarities to the English language with influence from mathematics.
    Python uses new lines to complete a command, as opposed to other programming languages which often use semicolons or parentheses.
    Python relies on indentation, using whitespace, to define scope; such as the scope of loops, functions and classes. Other programming languages often use curly-brackets for this purpose.

'''
 )
    st.write(
        """
    Welcome to the Beginner Python Tutorials section! This section is designed for those who are new to programming.
```python

     **Examples and Explanations:**
    #### Hello World Program:
    The "Hello, World!" program is a common first program for beginners. It simply prints the string "Hello, world!" to the console.
    ```python
    # Example: Hello World program
    print("Hello, world!")
    

"""
    )
    st.write(

    '''
     ## Python Indentation

Indentation refers to the spaces at the beginning of a code line.

Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.

Python uses indentation to indicate a block of code.
    
```python 
if 5 > 2:
    print("Five is greater than two!")
### python will give error if you skip the indentation

if 5 > 2:
print("Five is greater than two!")
output :Syntax Error:
'''
)
    st.write(

 """
 #### TRY IT USING THE CODE EDITOR BELOW
```pyhthon
if 5 > 2:
    print("Five is greater than two!") 
if 5 > 2:
    print("Five is greater than two!") 
"""
    )
    # try_yourself(2)

    st.write(
        """
    ***You have to use the same number of spaces in the same block of code, otherwise Python will give you an error***
    ```python
    Example
        if 5 > 2:
        print("Five is greater than two!")
             print("Five is greater than two!") 
        output :Syntax Error

"""
    )

    st.write(
        """
    ### Python Variables

    In Python, variables are created when you assign a value to it
    ```python
        Example

        Variables in Python:
        x = 5
        y = "Hello, World!"
    ```   

"""
    )

    st.write(
        '''
        ### Comments

Python has commenting capability for the purpose of in-code documentation.

Comments start with a #, and Python will render the rest of the line as a comment: 
```python
    Example

Comments in Python:
#This is a comment.
print("Hello, World!")
```
### Multiline Comments

Python does not really have a syntax for multiline comments.

To add a multiline comment you could insert a # for each line:
```python
    Example
    #This is a comment
    #written in
    #more than just one line
    print("Hello, World!")
```
###Python Variables
####Creating Variables

Python has no command for declaring a variable.

A variable is created the moment you first assign a value to it.
```python
        x = 5
    y = "John"
    print(x)
    print(y)
    output: 5
    output:John
```


```python
Variables do not need to be declared with any particular type,
 and can even change type after they have been set.

 Example
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)
Output :Try it in the coding editor below the page.
```



```python

##Casting

If you want to specify the data type of a variable, this can be done with casting.
Example
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0 
```
```python
Get the Type

You can get the data type of a variable with the type() function.
Example
x = 5
y = "John"
print(type(x))
print(type(y)) 
```
```python
Single or Double Quotes?

String variables can be declared either by using single or double quotes:
Example
x = "John"
# is the same as
x = 'John'
```
```python
Case-Sensitive

Variable names are case-sensitive.
Example

This will create two variables:
a = 4
A = "Sally"
#A will not overwrite a 
```
```python
    Variable Names
    A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:

        A variable name must start with a letter or the underscore character
        A variable name cannot start with a number
        A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
        Variable names are case-sensitive (age, Age and AGE are three different variables)
        A variable name cannot be any of the Python keywords.
```
```python
Example
Get your own Python Server

Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John" 

Example

Illegal variable names:
2myvar = "John"
my-var = "John"
my var = "John" 
```
```python
    Multi Words Variable Names

    Variable names with more than one word can be difficult to read.

    There are several techniques you can use to make them more readable:

    ##Camel Case

    Each word, except the first, starts with a capital letter:
    myVariableName = "John"

    ##Pascal Case

    Each word starts with a capital letter:
    MyVariableName = "John"

    
    ##Snake Case

    Each word is separated by an underscore character:
    my_variable_name = "John"
    ```
    ```python
        ###Many Values to Multiple Variables

        Python allows you to assign values to multiple variables in one line:
            Example
        Get your own Python Server
        x, y, z = "Orange", "Banana", "Cherry"
        print(x)
        print(y)
        print(z)
        #####Note: Make sure the number of variables matches the number of values, or else you will get an error.
        ##One Value to Multiple Variables

And you can assign the same value to multiple variables in one line:
Example
x = y = z = "Orange"
print(x)
print(y)
print(z)

##Unpack a Collection

If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

Example

Unpack a list:
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
    ```

```python
##Output Variables

The Python print() function is often used to output variables.
Example
Get your own Python Server
x = "Python is awesome"
print(x)
output:Try all in the Code editor below
In the print() function, you output multiple variables, separated by a comma
Example
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
Output:Try All in the Code editor below
```
```python


You can also use the + operator to output multiple variables:
Example
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
###Notice the space character after "Python " and "is ", without them the result would be "Pythonisawesome".
For numbers, the + character works as a mathematical operator:
Example
x = 5
y = 10
print(x + y)
```
```python
    In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:
Example
x = 5
y = "John"
print(x + y)

```

```python
The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:
Example
x = 5
y = "John"
print(x, y)
```

```python
### Global Variables

Variables that are created outside of a function (as in all of the examples above) are known as global variables.

## Global variables can be used by everyone, both inside of functions and outside.
Example
Get your own Python Server

Create a variable outside of a function, and use it inside the function
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc() 
```

''')
    # try_yourself(key=1)

    st.write("""
    
    #### Calculating the Sum of Two Numbers:
    This example demonstrates basic arithmetic in Python by calculating the sum of two numbers.
    ```python
    # Example: Calculating the sum of two numbers
    num1 = 5
    num2 = 3
    sum_result = num1 + num2
    print("Sum:", sum_result)
    ```
    
             
    
    **Additional Tutorials:**
    #### Using Variables:
    Variables are used to store data values in Python. This example demonstrates declaring and using variables.
    ```python
    # Example: Using variables
    x = 5
    y = 3
    print("x:", x)
    print("y:", y)
    ```

    #### Conditional Statements:
    Conditional statements are used to make decisions in Python. This example demonstrates using `if` statements.
    ```python
    # Example: Conditional statements
    num = 5
    if num > 0:
        print("Positive number")
    elif num < 0:
        print("Negative number")
    else:
        print("Zero")
    ```

    #### Loops:
    Loops are used to repeat a block of code multiple times. This example demonstrates using `for` and `while` loops.
    ```python
    # Example: Loops
    for i in range(5):
        print("Iteration:", i)
    
    num = 0
    while num < 5:
        print("Number:", num)
        num += 1
    ```

    #### Functions:
    Functions are blocks of reusable code. This example demonstrates defining and calling functions.
    ```python
    # Example: Functions
    def greet(name):
        print("Hello,", name)
    
    greet("Alice")
    greet("Bob")
    ```

    #### Lists:
    Lists are used to store multiple items in a single variable. This example demonstrates creating and manipulating lists.
    ```python
    # Example: Lists
    fruits = ["apple", "banana", "cherry"]
    print("Fruits:", fruits)
    print("First fruit:", fruits[0])
    ```

    #### String Manipulation:
    Strings are sequences of characters. This example demonstrates string concatenation and slicing.
    ```python
    # Example: String manipulation
    message = "Hello, "
    name = "Alice"
    full_message = message + name
    print(full_message)
    print("First three characters:", full_message[:3])
    ```

    #### User Input:
    User input allows users to interact with Python programs. This example demonstrates getting user input.
    ```python
    # Example: User input
    name = input("Enter your name: ")
    print("Hello,", name)
    ```

    **Programming Problems:**
    Solve the following problems:
    1. Write a Python program to find the factorial of a number.
    2. Write a Python program to check if a number is prime.
    3. Write a Python program to reverse a string.
    4. Write a Python program to count the number of vowels in a string.
    5. Write a Python program to check if a string is a palindrome.
    6. Write a Python program to find the largest element in a list.
    7. Write a Python program to remove duplicates from a list.
    8. Write a Python program to calculate the Fibonacci sequence.

    **Solutions:** 
    Click the button below to reveal the solutions.
    """)
    with st.expander("You can Read more here"):
        st.write(
        '''
    
    **Tutorials:**
    - [Python Basics Tutorial - W3Schools](https://www.w3schools.com/python/)
    - [Python for Everybody - Coursera](https://www.coursera.org/specializations/python)
    - [Python Tutorial - Tutorialspoint](https://www.tutorialspoint.com/python/index.htm)
    - [Learn Python - Codecademy](https://www.codecademy.com/learn/learn-python-3)
'''
    )   

    # Solutions
    with st.expander("Solutions"):
        st.write("""
        **1. Factorial of a Number:**
        ```python
        def factorial(n):
            if n == 0:
                return 1
            else:
                return n * factorial(n-1)
        
        num = 5
        print("Factorial of", num, "is", factorial(num))
        ```

        **2. Check if a Number is Prime:**
        ```python
        def is_prime(n):
            if n <= 1:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True
        
        num = 7
        if is_prime(num):
            print(num, "is prime")
        else:
            print(num, "is not prime")
        ```

        **3. Reverse a String:**
        ```python
        def reverse_string(s):
            return s[::-1]
        
        string = "hello"
        print("Reversed:", reverse_string(string))
        ```

        **4. Count Vowels in a String:**
        ```python
        def count_vowels(s):
            vowels = "aeiou"
            count = 0
            for char in s:
                if char.lower() in vowels:
                    count += 1
            return count
        
        string = "hello"
        print("Number of vowels:", count_vowels(string))
        ```

        **5. Check Palindrome:**
        ```python
        def is_palindrome(s):
            return s == s[::-1]
        
        string = "radar"
        if is_palindrome(string):
            print(string, "is a palindrome")
        else:
            print(string, "is not a palindrome")
        ```

        **6. Find Largest Element in a List:**
        ```python
        def find_largest_element(lst):
            return max(lst)
        
        numbers = [3, 7, 2, 9, 5]
        print("Largest element:", find_largest_element(numbers))
        ```

        **7. Remove Duplicates from a List:**
        ```python
        def remove_duplicates(lst):
            return list(set(lst))
        
        numbers = [1, 2, 3, 1, 4, 2]
        print("List after removing duplicates:", remove_duplicates(numbers))
        ```

        **8. Fibonacci Sequence:**
        ```python
        def fibonacci(n):
            fib = [0, 1]
            for i in range(2, n):
                fib.append(fib[-1] + fib[-2])
            return fib
        
        num_terms = 10
        print("Fibonacci sequence:", fibonacci(num_terms))
        ```

        """)
    st.write(try_yourself())
def try_yourself():
    st.subheader("Try it Yourself!")
    st.write("Enter your Python code below and click the 'Run Code' button to see the output.")
    code = st.text_area("Enter Python code here", height=400)
    if st.button("Run Code"):
        with st_redirect():
            st.write("Output:")
            try:
                exec(code)
            except Exception as e:
                st.write("Error:", e)


 