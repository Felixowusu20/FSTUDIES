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
# Function to display tutorials and links for advanced Python level
def display_advanced_tutorials():
    st.subheader("Advanced Python Tutorials")
    st.write("""
    Welcome to the Advanced Python Tutorials section! This section is for experienced Python programmers who want to master advanced concepts.

    **Tutorials:**
    - [Advanced Python Programming - Udemy](https://www.udemy.com/course/python-beyond-the-basics-object-oriented-programming/)
    - [Advanced Python - Tutorials Point](https://www.tutorialspoint.com/advanced_python/index.htm)
    - [Advanced Python - Pluralsight](https://www.pluralsight.com/courses/python-advanced)
    - [Python Advanced - HackerRank](https://www.hackerrank.com/domains/python)

    **Examples and Explanations:**
    #### Using NumPy for Matrix Multiplication:
    NumPy is a powerful library for numerical computing in Python. This example demonstrates using NumPy to perform matrix multiplication.
    ```python
    # Example: Using NumPy to perform matrix multiplication
    import numpy as np
    
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    C = np.dot(A, B)
    print(C)
    ```

    #### Creating a Custom Decorator:
    Decorators are a powerful feature in Python. This example demonstrates creating a custom decorator that prints messages before and after calling a function.
    ```python
    # Example: Creating a custom decorator
    def my_decorator(func):
        def wrapper():
            print("Something is happening before the function is called.")
            func()
            print("Something is happening after the function is called.")
        return wrapper

    @my_decorator
    def say_hello():
        print("Hello!")

    say_hello()
    ```
    
    **Additional Links:**
    - [Advanced Python - YouTube Playlist](https://www.youtube.com/playlist?list=PLqM7alHXFySF8B9KqOy6yz4vggu4tiNMP)
    - [Advanced Python - LinkedIn Learning](https://www.linkedin.com/learning/topics/advanced-python)
    """, unsafe_allow_html=True)

    st.subheader("Try it Yourself!")
    st.write("Enter your Python code below and click the 'Run Code' button to see the output.")
    code = st.text_area("Enter Python code here", height=200)
    if st.button("Run Code"):
        with st_redirect():
            try:
                exec(code)
            except Exception as e:
                st.write("Error:", e)
