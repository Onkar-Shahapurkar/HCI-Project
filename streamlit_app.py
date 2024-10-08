import streamlit as st
import pandas as pd

st.title("Home Decor Website")

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
    ["🏠 Introduction", "👥 Team members", 
     "📝 User Persona", "📝 User Journey Map", "📝 Cognitive Walkthrough", 
     "📝 Figma Prototype", "📝 Low Fidelity Design", "📝 Card Sorting Technique"]
)

# Content displayed based on selection
if selection == "🏠 Introduction":
    st.subheader("Home Decor Website")
    st.write("""
    Welcome to the Home Decor Website project! This project aims to provide an online platform for users to explore 
    various home decor products, including furniture, wall art, and accessories. The website features user-friendly 
    navigation, detailed product descriptions, and the ability to add items to a virtual shopping cart.
    
    ### Key Features:
    - **Product Categories**: Explore a wide range of categories, from modern to classic decor styles.
    - **Shopping Cart**: Easily add products to your cart and proceed to checkout.
    - **Responsive Design**: The website is designed to work on both desktop and mobile devices.
    - **Search Functionality**: Quickly find products with a robust search feature.
    """)

elif selection == "👥 Team members":
    st.subheader("Meet Our Team")
    st.write("Meet our amazing team of developers and designers working on this project:")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<div class="centered-content">', unsafe_allow_html=True)
        img_url1 = "https://raw.githubusercontent.com/Onkar-Shahapurkar/HCI-Project/main/dev1.jpg"
        st.image(img_url1, caption="Akshita Shambharkar", width=200)
        st.subheader("Akshita Shambharkar")
        st.write("""
        - **PRN Number**: 22320034
        - **Roll Number**: 332070
        - **Year**: TY
        - **Division**: B
        - **Email**: akshita.22320034@viit.ac.in
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="centered-content">', unsafe_allow_html=True)
        img_url2 = "https://raw.githubusercontent.com/Onkar-Shahapurkar/HCI-Project/main/dev1.jpg"
        st.image(img_url2, caption="Ambika Pankaj Surwase", width=200)
        st.subheader("Ambika Pankaj Surwase")
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

elif selection == "📝 User Persona":
    st.subheader("User Persona")
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


elif selection == "📝 User Journey Map":
    st.subheader("User Journey Map")
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


elif selection == "📝 Cognitive Walkthrough":
    st.subheader("Cognitive Walkthrough")
    st.write("""
    - **Title**: Cognitive Walkthrough
    - **Description**: This assignment contains a cognitive walkthrough presented.
    """)

    excel_url = "https://docs.google.com/spreadsheets/d/1DyLtZZjNOSh0cheexl7bClN4L4Yq-_fz/edit?usp=sharing&ouid=103448259837151713633&rtpof=true&sd=true"  # Update with the correct URL

    st.markdown(f"""
    <a href="{excel_url}" target="_blank">
        <button style="background-color:#4CAF50; color:white; padding:10px 20px; border:none; border-radius:5px; cursor:pointer;">
            Open Cognitive Walkthrough
        </button>
    </a>
    """, unsafe_allow_html=True)


elif selection == "📝 Figma Prototype":
    st.subheader("Figma Prototype")
    st.write("""
    - **Title**: Prototype Development
    - **Description**: Build a prototype of the Home Decor Website using your wireframes.
    """)

    Figma_url = "https://www.figma.com/proto/Mg4CCrYQxbADQGDYVMyBEw/Homedecor?node-id=0-1&t=MxXbicZIKc9R1k56-1"

    st.markdown(f"""
    <a href="{Figma_url}" target="_blank">
        <button style="background-color:#4CAF50; color:white; padding:10px 20px; border:none; border-radius:5px; cursor:pointer;">
            Open Figma
        </button>
    </a>
    """, unsafe_allow_html=True)

   

elif selection == "📝 Low Fidelity Design":
    st.subheader("Low Fidelity Design")
    st.write("""
    - **Title**: Low Fidelity Design
    - **Description**: Create low-fidelity wireframes that outline the structure of the Home Decor Website.
    """)

    low_Fidelity_url = "https://drive.google.com/file/d/19BpMbNN2Uzano7wKZBlWopDShQnuyJMF/view"

    st.markdown(f"""
    <a href="{low_Fidelity_url}" target="_blank">
        <button style="background-color:#4CAF50; color:white; padding:10px 20px; border:none; border-radius:5px; cursor:pointer;">
            Open Low Fidelity Design
        </button>
    </a>
    """, unsafe_allow_html=True)

elif selection == "📝 Card Sorting Technique":
    st.subheader("Card Sorting Technique")
    st.write("""
    - **Title**: Card Sorting Techniques
    - **Description**: Conduct card sorting to organize the information architecture of the Home Decor Website.
    """)

    # Example PDF or document URL for Card Sorting Techniques
    card_sorting_url = "https://drive.google.com/file/d/1oFCPeFqq7-ufFlzu_R-_XsvSrJfv0Yob/view"

    st.markdown(f"""
    <a href="{card_sorting_url}" target="_blank">
        <button style="background-color:#4CAF50; color:white; padding:10px 20px; border:none; border-radius:5px; cursor:pointer;">
            Open Card Sorting Techniques Document
        </button>
    </a>
    """, unsafe_allow_html=True)
