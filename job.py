import streamlit as st

# Create a list to store the job details
jobs = []

# Add Job page
def add_job():
    st.header("Bano Qabil job portal 2.0")
    st.title("Al Khidmat")
    st.header("Add Job")
    job_title = st.text_input("Job Title")
    job_location = st.text_input("Job Location")
    job_description = st.text_area("Job Description")
    if st.button("Submit"):
        jobs.append({"title": job_title, "location": job_location, "description": job_description})
        st.success("Job added successfully!")

# Home page
def home():
    st.header("Availabe Jobs")
    if len(jobs) == 0:
        st.write("No jobs available yet.")
    else:
        for job in jobs:
            st.write(f"Title: {job['title']}")
            st.write(f"Location: {job['location']}")
            st.write(f"Description: {job['description']}")
            st.write("---")

# Sidebar navigation
page = st.sidebar.radio("Navigation", ["Add Job", "Contact Us", "About Us"])

# Display content based on selected page
if page == "About Us":
    st.title("About Out Team")
    st.write("its our last project of python in bano qabil 2.0")
    st.write("In these we try to provide a plattform to approach a job portal in just one click ")
    st.write("Our team is based on 3 people:")
    st.write("Leader name;Anas Khan,2nd memeber :Ahmed ,3rd member:Rayyan")
    # Add your About Us content here
elif page == "Contact Us":
    st.title("For Contact")
    st.write("Gmail : anaskh0469@gmail.com")
    st.write("contact us :03142551862")
    st.write("Feel free to get in touch with us!")
    # Add your Contact Us content here
elif page == "Add Job":
    add_job()
    home()  # Display the updated job list on the Home page after adding a job
