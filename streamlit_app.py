import streamlit as st

# Set the title of the application
st.title("Home Decor Website Project")

# Custom CSS to style the sidebar
sidebar_style = """
    <style>
    .sidebar .sidebar-content {
        background-color: #f8f9fa;  /* Light background color */
        border-radius: 10px;         /* Rounded corners */
        padding: 10px;               /* Padding */
        box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);  /* Subtle shadow effect */
    }
    </style>
"""
st.markdown(sidebar_style, unsafe_allow_html=True)

# Define the sidebar selection options with emojis for better visuals
selection = st.sidebar.selectbox(
    "🗂️ Select an option:", 
    ["🏠 Introduction", "👥 Team members", "📁 Figma file", 
     "📝 Assignment 1", "📝 Assignment 2", "📝 Assignment 3", 
     "📝 Assignment 4", "📝 Assignment 5"]
)

# Content displayed based on selection
if selection == "🏠 Introduction":
    st.subheader("Home Decor Website")
    st.write("""
    Welcome to the Home Decor Website project! This project aims to provide an online platform for users to explore 
    various home decor products, including furniture, wall art, and accessories. The website features user-friendly 
    navigation, detailed product descriptions, and the ability to add items to a virtual shopping cart.
    
    ### Key Features:
    - **User Authentication**: Users can create accounts and log in to save their favorite products.
    - **Product Categories**: Explore a wide range of categories, from modern to classic decor styles.
    - **Shopping Cart**: Easily add products to your cart and proceed to checkout.
    - **Responsive Design**: The website is designed to work on both desktop and mobile devices.
    - **Search Functionality**: Quickly find products with a robust search feature.
    """)

elif selection == "👥 Team members":
    st.subheader("Meet Our Team")
    st.write("Meet our amazing team of developers and designers working on this project:")

    # Create three columns for three team members
    col1, col2, col3 = st.columns(3)

    # Define CSS to center the content
    center_style = """
        <style>
        .centered-content {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }
        </style>
    """

    # Inject the CSS style into the Streamlit app
    st.markdown(center_style, unsafe_allow_html=True)

    with col1:
        st.markdown('<div class="centered-content">', unsafe_allow_html=True)
        st.subheader("Member 1")
        st.write("""
        - **Name**: John Doe
        - **PRN Number**: 123456789
        - **Roll Number**: 01
        - **Year**: 4th Year
        - **Division**: A
        - **Email**: john.doe@example.com
        """)
        img_url1 = "https://raw.githubusercontent.com/Onkar-Shahapurkar/HCI-Project/main/dev1.jpg"
        st.image(img_url1, caption="John Doe", width=150)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="centered-content">', unsafe_allow_html=True)
        st.subheader("Member 2")
        st.write("""
        - **Name**: Jane Smith
        - **PRN Number**: 987654321
        - **Roll Number**: 02
        - **Year**: 4th Year
        - **Division**: A
        - **Email**: jane.smith@example.com
        """)
        img_url2 = "https://raw.githubusercontent.com/Onkar-Shahapurkar/HCI-Project/main/dev2.jpg"
        st.image(img_url2, caption="Jane Smith", width=150)
        st.markdown('</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="centered-content">', unsafe_allow_html=True)
        st.subheader("Member 3")
        st.write("""
        - **Name**: Alex Brown
        - **PRN Number**: 456789123
        - **Roll Number**: 03
        - **Year**: 4th Year
        - **Division**: A
        - **Email**: alex.brown@example.com
        """)
        img_url3 = "https://raw.githubusercontent.com/Onkar-Shahapurkar/HCI-Project/main/dev3.jpg"
        st.image(img_url3, caption="Alex Brown", width=150)
        st.markdown('</div>', unsafe_allow_html=True)

elif selection == "📁 Figma file":
    st.subheader("Figma Design")
    st.write("Click the link below to open the Figma design file:")
    st.markdown("[Open Figma File](https://www.figma.com/file/your-figma-file-url)", unsafe_allow_html=True)

elif selection == "📝 Assignment 1":
    st.subheader("Assignment 1")
    st.write("""
    - **Title**: Introduction to Home Decor
    - **Description**: Research the latest trends in home decor and present your findings.
    """)

elif selection == "📝 Assignment 2":
    st.subheader("Assignment 2")
    st.write("""
    - **Title**: User Persona Development
    - **Description**: Create user personas based on your target audience for the Home Decor Website.
    """)

elif selection == "📝 Assignment 3":
    st.subheader("Assignment 3")
    st.write("""
    - **Title**: Wireframe Creation
    - **Description**: Develop wireframes for key pages of the Home Decor Website using Figma or other design tools.
    """)

elif selection == "📝 Assignment 4":
    st.subheader("Assignment 4")
    st.write("""
    - **Title**: Prototype Development
    - **Description**: Build a prototype of the Home Decor Website using your wireframes.
    """)

elif selection == "📝 Assignment 5":
    st.subheader("Assignment 5")
    st.write("""
    - **Title**: Final Presentation
    - **Description**: Prepare and present the final project presentation to showcase the Home Decor Website.
    """)
    
