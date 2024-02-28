import streamlit as st

def main():
    st.title("Streamlit App")
    
    # Create a button for "Contact Us" in the top-right corner
    contact_button_clicked = st.button("Contact Us", key='contact_button', help='Click to contact us', anchor='top-right')
    
    if contact_button_clicked:
        # Display contact form or any contact information here
        st.write("""
        Please fill out the form below to get in touch with us.
        """)

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
