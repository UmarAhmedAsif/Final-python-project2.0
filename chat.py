import streamlit as st
import pandas as pd

# Sample job listings data
job_listings_data = {
    'Job Title': ['Software Engineer', 'Data Scientist', 'Product Manager'],
    'Company': ['Tech Co.', 'Data Corp.', 'Product Inc.'],
    'Location': ['San Francisco, CA', 'New York, NY', 'Seattle, WA'],
    'Description': ['We are seeking a talented software engineer...', 
                    'Data Corp. is looking for a skilled data scientist...', 
                    'Product Inc. is hiring a product manager...']
}

# Create DataFrame
job_listings_df = pd.DataFrame(job_listings_data)

def main():
    st.title("Job Portal")
    
    st.header("Job Listings")
    st.dataframe(job_listings_df)
    
    # Search functionality
    st.sidebar.header("Search")
    job_title = st.sidebar.text_input("Job Title")
    location = st.sidebar.text_input("Location")
    
    filtered_df = job_listings_df
    if job_title:
        filtered_df = filtered_df[filtered_df['Job Title'].str.contains(job_title, case=False)]
    if location:
        filtered_df = filtered_df[filtered_df['Location'].str.contains(location, case=False)]
    
    st.header("Filtered Job Listings")
    st.dataframe(filtered_df)
    
    # Apply functionality
    st.sidebar.header("Apply")
    selected_job_index = st.sidebar.selectbox("Select a job to apply", filtered_df.index)
    if st.sidebar.button("Apply"):
        selected_job = filtered_df.iloc[selected_job_index]
        st.success(f"Successfully applied to '{selected_job['Job Title']}' at {selected_job['Company']}!")
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

if __name__ == "__main__":
    main()
