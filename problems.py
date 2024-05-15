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
#funciton for the problem solving and the solutions attached to it
def problems_solving():
    st.subheader("Solve the following problems")
    st.write(
        '''
         #### Using List Comprehension:
    List comprehension is a concise way to create lists in Python. This example demonstrates using list comprehension to generate a list of squared numbers.
    ```python
    # Example: Using list comprehension
    numbers = [1, 2, 3, 4, 5]
    squares = [x**2 for x in numbers]
    print("Squares:", squares)
    ```

'''
    )
    st.write("Solve  the problems and hit the Run code button to run the codes")
    code = st.text_area("Enter the codes here" , height=200)
    if st.button("Run Codes"):
        with st_redirect():
            try:
                exec(code)
            except Exception as e:
                st.error("Error:" ,e )
