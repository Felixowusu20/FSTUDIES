import streamlit as st
from beginners import display_beginner_tutorials
from intermediates import display_intermediate_tutorials
from advanced import display_advanced_tutorials
from problems import problems_solving
# from playground import try_yourself

def main():
    st.set_page_config("FSTUDIES" , ':book:')
    st.title("Python Programming Tutorials")

    # Sidebar for selecting Python course level
    level = st.sidebar.selectbox("PYTHON", ["Beginner", "Intermediate", "Advanced"  ,"problems"])


    if level == "Beginner":
        display_beginner_tutorials()
    elif level == "Intermediate":
        display_intermediate_tutorials()
    elif level == "Advanced":
        display_advanced_tutorials()
    elif level == "problems":
        problems_solving()
    # else:
    #     try_yourself()
    

if __name__ == "__main__":
    main()
