import streamlit as st

# Set the title of the application
st.title("Home Decor Website Project")

# Custom CSS to style the sidebar
sidebar_style = """
    <style>
    .sidebar .sidebar-content {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 10px;
        box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1)
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
    # center_style = """
    #     <style>
    #     .centered-content {
    #         display: flex;
    #         flex-direction: column;
    #         align-items: center;
    #         justify-content: center;
    #     }
    #     </style>
    # """

    # Inject the CSS style into the Streamlit app
    # st.markdown(center_style, unsafe_allow_html=True)

    with col1:
        st.markdown('<div class="centered-content">', unsafe_allow_html=True)
        img_url1 = "https://raw.githubusercontent.com/Onkar-Shahapurkar/HCI-Project/main/dev1.jpg"
        st.image(img_url1, caption="Akshita Shambharkar", width=200)
        st.subheader("Akshita Shambharkar")
        st.write("""
        - **PRN Number**: 123456789
        - **Roll Number**: 332071
        - **Year**: TY
        - **Division**: B
        - **Email**: john.doe@example.com
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="centered-content">', unsafe_allow_html=True)
        img_url2 = "https://raw.githubusercontent.com/Onkar-Shahapurkar/HCI-Project/main/dev1.jpg"
        st.image(img_url2, caption="Ambika Pankaj Surwase", width=200)
        st.subheader("Ambika     Surwase")
        st.write("""
        - **PRN Number**: 22320076
        - **Roll Number**: 332072
        - **Year**: TY
        - **Division**: B
        - **Email**: ambika.22320076@viit.ac.in
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="centered-content">', unsafe_allow_html=True)
        img_url2 = "https://raw.githubusercontent.com/Onkar-Shahapurkar/HCI-Project/main/dev1.jpg"
        st.image(img_url2, caption="Onkar Shahapurkar", width=200)
        st.subheader("Onkar Shahapurkar")
        st.write("""
        - **PRN Number**: 22320147
        - **Roll Number**: 332076
        - **Year**: TY
        - **Division**: B
        - **Email**: onkar.22320147@viit.ac.in
        """)
        st.markdown('</div>', unsafe_allow_html=True)

elif selection == "📁 Figma file":
    st.subheader("Figma Design")
    st.write("Click the link below to open the Figma design file:")
    st.markdown("[Open Figma File](https://www.figma.com/file/your-figma-file-url)", unsafe_allow_html=True)

elif selection == "📝 Assignment 1":
    st.subheader("Assignment 1")
    st.write("""
    - **Title**: User Persona Development
    - **Description**: User Personas based on the target audience of the Project.
    """)

    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        img_persona1 = "https://raw.githubusercontent.com/Onkar-Shahapurkar/HCI-Project/main/Vikram Singh.png"  # Update this with the actual image URL
        st.image(img_persona1, caption="Vikram Singh", width=175)

    with col2:
        img_persona2 = "https://raw.githubusercontent.com/Onkar-Shahapurkar/HCI-Project/main/Rohan Mehta.png"  # Update this with the actual image URL
        st.image(img_persona2, caption="Rohan Mehta", width=175)

    with col3:
        img_persona3 = "https://raw.githubusercontent.com/Onkar-Shahapurkar/HCI-Project/main/Priya Kapoor.png"  # Update this with the actual image URL
        st.image(img_persona3, caption="Priya Kapoor", width=175)

    col4, col5 = st.columns([1, 1])

    with col4:
        img_persona4 = "https://raw.githubusercontent.com/Onkar-Shahapurkar/HCI-Project/main/Maya Desai.png"  # Update this with the actual image URL
        st.image(img_persona4, caption="Maya Desai", width=175)

    with col5:
        img_persona5 = "https://raw.githubusercontent.com/Onkar-Shahapurkar/HCI-Project/main/Aditi Sharma.png"  # Update this with the actual image URL
        st.image(img_persona5, caption="Aditi Sharma", width=175)


elif selection == "📝 Assignment 2":
    st.subheader("Assignment 2")
    st.write("""
    - **Title**: User Journey Map
    - **Description**: Develop a user journey map to visualize the steps taken by a user while interacting with the Home Decor Website.
    """)

    # First row: Displaying first 3 journey maps in a row with some space
    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        img_journey1 = "https://raw.githubusercontent.com/Onkar-Shahapurkar/HCI-Project/main/Rohan Mehta uj.jpg"
        st.image(img_journey1, caption="Rohan Mehta", width=250)

    with col2:
        img_journey2 = "https://raw.githubusercontent.com/Onkar-Shahapurkar/HCI-Project/main/ADITI SHARMA uj.jpg"
        st.image(img_journey2, caption="ADITI SHARMA", width=250)

    with col3:
        img_journey3 = "https://raw.githubusercontent.com/Onkar-Shahapurkar/HCI-Project/main/Maya Desai uj.jpg"
        st.image(img_journey3, caption="Maya Desai", width=250)

    # Second row: Displaying the last 2 journey maps, centered in a row with some space
    col4, _, col5 = st.columns([1, 0.5, 1])

    with col4:
        img_journey4 = "https://raw.githubusercontent.com/Onkar-Shahapurkar/HCI-Project/main/Vikram Singh uj.jpg"
        st.image(img_journey4, caption="Vikram Singh", width=250)

    with col5:
        img_journey5 = "https://raw.githubusercontent.com/Onkar-Shahapurkar/HCI-Project/main/Priya Kappor uj.jpg"
        st.image(img_journey5, caption="Priya Kappor", width=250)


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
    
