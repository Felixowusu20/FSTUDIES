import streamlit as st 
import io
import contextlib

@contextlib.contextmanager
def st_redirect():
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        yield output
    st.write(output.getvalue())



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
st.write(try_yourself())
