import streamlit as st

def main():
    st.title("Contact Us")
    
    st.write("Please fill out the form below to get in touch with us.")
    
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message", height=200)
    
    if st.button("Submit"):
        # You can add your own logic here to handle the submission
        if name and email and message:
            st.success("Thank you for reaching out! We will get back to you soon.")
        else:
            st.error("Please fill out all the fields before submitting.")

if __name__ == "__main__":
    main()
