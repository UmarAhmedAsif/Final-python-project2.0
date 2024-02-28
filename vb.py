import streamlit as st

def main():
    st.title("Streamlit App")

    # Use CSS to position the button in the top-right corner
    st.markdown(
        """
        <style>
        .about-us-button {
            position: absolute;
            top: 10px;
            right: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Create a button for "About Us" in the top-right corner
    about_us_button_clicked = st.button("About Us", key='about_us_button', help='Click to learn more about us', class_='about-us-button')

    if about_us_button_clicked:
        # Display information about your organization or project
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
