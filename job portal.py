import streamlit as st
def main():
st.title("Job Portal")
# Add image
st.image("path_to_image/image.jpg", use_column_width=True)
location = st.sidebar.selectbox("Select Location", ["All", "Karachi", "Lahore", "Dubai"])
filtered_jobs = get_jobs(location)
show_jobs(filtered_jobs)
st.sidebar.title("Add a Job")
new_title = st.sidebar.text_input("Title")
new_company = st.sidebar.text_input("Company")
new_location = st.sidebar.text_input("Location")
new_description = st.sidebar.text_area("Description")
if st.sidebar.button("Add Job"):
add_job(new_title, new_company, new_location, new_description) st.sidebar.success("Job added successfully!")
st.sidebar.write("### Navigate")
if st.sidebar.button("Home"):
st.write("Welcome to the Home Page!")
if st.sidebar.button("Contact Us"):
st.write("Please contact us at contact@jobportal.com")
if st.sidebar.button("About"):
st.write("This is a simple job portal application created using Streamlit.")
if name="main__":
main()
