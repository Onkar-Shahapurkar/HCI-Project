import streamlit as st
from PIL import Image  # For loading images

# Set up the page layout
st.set_page_config(layout="wide")

# Sidebar with options
st.sidebar.title("Navigation")
options = ["Introduction", "Team members", "Figma File", 
           "Assignment 1", "Assignment 2", "Assignment 3", 
           "Assignment 4", "Assignment 5"]
selection = st.sidebar.radio("Go to:", options)

# Content based on selection
if selection == "Introduction":
    st.title("Introduction")
    st.write("""
    Welcome to the project. This app provides an overview of the team and assignments. 
    You can navigate through the options to view specific content.
    """)

    # Example image (load your own image here)
    img = Image.open("path/to/introduction_image.jpg")
    st.image(img, caption="Project Overview")

elif selection == "Team members":
    st.title("Team Members")
    st.write("Meet our amazing team of developers and designers working on this project:")

    # Create three columns for three team members
    col1, col2, col3 = st.columns(3)

    with col1:
        img_url1 = "https://raw.githubusercontent.com/Onkar-Shahapurkar/HCI-Project/main/dev1.jpg"
        st.image(img_url1, caption="John Doe", width=150)
               
        st.subheader("Member 1")
        st.write("""
        - **Name**: John Doe
        - **PRN Number**: 123456789
        - **Roll Number**: 01
        - **Year**: 4th Year
        - **Division**: A
        - **Email**: john.doe@example.com
        """)

    with col2: 
        img_url2 = "https://raw.githubusercontent.com/Onkar-Shahapurkar/HCI-Project/main/dev1.jpg"
        st.image(img_url2, caption="Jane Smith", width=150)
               
        st.subheader("Member 2")
        st.write("""
        - **Name**: Jane Smith
        - **PRN Number**: 987654321
        - **Roll Number**: 02
        - **Year**: 4th Year
        - **Division**: A
        - **Email**: jane.smith@example.com
        """)

    with col3:
        img_url3 = "https://raw.githubusercontent.com/Onkar-Shahapurkar/HCI-Project/main/dev1.jpg"
        st.image(img_url3, caption="Alex Brown", width=150)
        st.subheader("Member 3")
        st.write("""
        - **Name**: Alex Brown
        - **PRN Number**: 456789123
        - **Roll Number**: 03
        - **Year**: 4th Year
        - **Division**: A
        - **Email**: alex.brown@example.com
        """)


elif selection == "Figma File":
    st.title("Figma Design")
    st.write("Click the link below to view the Figma file:")
    
    figma_url = "https://www.figma.com/file/xyz123"  # Replace with your actual Figma file URL
    st.markdown(f"[Open Figma File]({figma_url})")

elif selection == "Assignment 1":
    st.title("Assignment 1")
    st.write("Details about Assignment 1")
    # Example image (load your own image here)
    img = Image.open("path/to/assignment1_image.jpg")
    st.image(img, caption="Assignment 1")

elif selection == "Assignment 2":
    st.title("Assignment 2")
    st.write("Details about Assignment 2")
    img = Image.open("path/to/assignment2_image.jpg")
    st.image(img, caption="Assignment 2")

elif selection == "Assignment 3":
    st.title("Assignment 3")
    st.write("Details about Assignment 3")
    img = Image.open("path/to/assignment3_image.jpg")
    st.image(img, caption="Assignment 3")

elif selection == "Assignment 4":
    st.title("Assignment 4")
    st.write("Details about Assignment 4")
    img = Image.open("path/to/assignment4_image.jpg")
    st.image(img, caption="Assignment 4")

elif selection == "Assignment 5":
    st.title("Assignment 5")
    st.write("Details about Assignment 5")
    img = Image.open("path/to/assignment5_image.jpg")
    st.image(img, caption="Assignment 5")
