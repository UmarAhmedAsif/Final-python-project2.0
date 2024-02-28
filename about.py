import streamlit as st

def main():
    st.title("About Us")
    
    st.write("""
    Welcome to our Streamlit app! This is where you can learn more about us.
    """)
    
    st.header("Our Mission")
    st.write("""
    Our mission is to provide innovative solutions that make life easier for our users.
    """)
    
    st.header("Our Team")
    st.write("""
    Meet the amazing people behind this project:
    - John Doe: Lead Developer
    - Jane Smith: UX Designer
    - Alex Johnson: Data Scientist
    """)
    
    st.header("Contact Us")
    st.write("""
    If you have any questions or feedback, feel free to reach out to us at example@email.com.
    """)
    
if __name__ == "__main__":
    main()
