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


def display_intermediate_tutorials():
    st.subheader("Intermediate Python Tutorials")
    st.write("""
    Welcome to the Intermediate Python Tutorials section! This section is for those who have some experience with Python and want to deepen their knowledge.

    **Tutorials:**
    - [Intermediate Python - Real Python](https://realpython.com/tutorials/intermediate/)
    - [Python Intermediate Tutorial - Javatpoint](https://www.javatpoint.com/python-intermediate)
    - [Python Tutorial - Programiz](https://www.programiz.com/python-programming)
    - [Intermediate Python - DataCamp](https://www.datacamp.com/courses/intermediate-python)

    **Examples and Explanations:**
    #### Reading and Printing Contents of a File:
    This example demonstrates reading and printing the contents of a file line by line using a `with` statement.
    ```python
    # Example: Reading and printing contents of a file
    with open("example.txt", "r") as f:
        for line in f:
            print(line.strip())
    ```

    #### Using List Comprehension:
    List comprehension is a concise way to create lists in Python. This example demonstrates using list comprehension to generate a list of squared numbers.
    ```python
    # Example: Using list comprehension
    numbers = [1, 2, 3, 4, 5]
    squares = [x**2 for x in numbers]
    print("Squares:", squares)
    ```
    
    **Additional Links:**
    - [Python Intermediate - YouTube Playlist](https://www.youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU)
    - [Python Intermediate - LinkedIn Learning](https://www.linkedin.com/learning/topics/intermediate-python)
    """, unsafe_allow_html=True)

    st.subheader("Try it Yourself!")
    st.write("Enter your Python code below and click the 'Run Code' button to see the output.")
    code = st.text_area("Enter Python code here", height=400)
    if st.button("Run Code"):
        with st_redirect():
            try:
                exec(code)
            except Exception as e:
                st.write("Error:", e)
