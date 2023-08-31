import streamlit as st

def f_lar(n1, n2, n3):
    return max(n1, n2, n3)

def main():
    
    st.title("Find the Largest Number out of the three numbers")
    
    n1 = st.number_input("Enter your first number:")
    n2 = st.number_input("Enter your second number:")
    n3 = st.number_input("Enter your third number:")
    
    if st.button("Find Largest out of the three."):
        biggest = f_lar(n1, n2, n3)
        st.write(f"The largest number out of the three is: {biggest}")

main()
