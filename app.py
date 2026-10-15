import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Streamlit Basics Demo",
    page_icon="🚀",
    layout="wide"
)

# Title, header, subheader and text
# Title, header, subheader and text
st.title("🚀 Streamlit Basics Demo")
st.header("Explore Streamlit Features")
st.subheader("Interactive widgets, forms, and layouts using Python")

st.write(
    "A beginner-friendly demo showcasing Streamlit widgets, "
    "forms, layouts, and file handling."
)

st.markdown("### Start Exploring")
st.caption("Select options and try the interactive components below.")


# code, json and metric
st.code("print('Hello , Streamlit!!')", language="python")

st.json({
    "Project": "Streamlit Basics Demo",
    "Course": "Python",
    "level": "Beginner"
})
st.metric("Students", 25, "+5")

# Sidebar
st.sidebar.title("🧭 Demo Menu")
st.sidebar.write("Choose a topic to explore:")

topic = st.sidebar.selectbox(
    "Choose a topic",
    ["Python", "Pandas", "NumPy", "AI Applications"]
)

st.write(f"Selected topic: {topic}")


# Text input
name = st.text_input("What is your name?")

if name:
    st.write(f"Hello, {name}")

# Number input
age = st.number_input(
    "Enter your age",
    min_value=1,
    max_value=100,
    value=18
)    

st.write(f"Your age is: {age}")


# slider
confidence = st.slider(
    "Choose a confidence score",
    min_value=0,
    max_value=100,
    value=50
)

st.write(f"Confidence score: {confidence}")

# Checkbox
show_details = st.checkbox("Show project details")

if show_details:
    st.info("This demo showcases common Streamlit components, "
        "including inputs, forms, layouts, and file upload/download.")


# radio buttons
experience = st.radio(
    "Your Python experience",
    ["Beginner", "Intermediate", "Advanced"]
)

st.write(f"Selected experience: {experience}")


# selectedbox and multiselect

language = st.selectbox(
    "Choose a programming language:",
    ["Python", "JAVA", "JavaScript", "C++"]
)

skills = st.multiselect(
    "Choose your skills:",
    ["Python", "Pandas", "Numpy", "Streamlit", "Git"]
)

st.write(f"Language: {language}")
st.write(f"Skills: {skills}")

st.color_picker("Color")


#Button
if st.button("Submit"):
    st.success("Button clicked successfully")

#form
with st.form("Strudent_form"):
    st.write("Student Registration")

    student_name = st.text_input("Student Name")
    studnt_email = st.text_input("Email")
    submitted = st.form_submit_button("Register")

    if submitted:
        st.success(f"Registration received for {student_name}  whose email is {studnt_email}")


#columns

col1,col2, col3 = st.columns(3)

with col1 :
    st.info("Python")

with col2 :
    st.info("Pandas")
    
with col3 :
    st.info("Numpy")


#Expander
with st.expander("Show more info"):
    st.write("Expanders are useful when we want to hide details ")

#Status message
st.success("Success message")
st.info("Information message")
st.warning("Warning message")
st.error("Error message")

#progress bar
st.progress(95)

#file uploder
uploaded_file  = st.file_uploader(
    "Upload a text file",
    type = ["txt"]
)

if uploaded_file is not None:
    content = uploaded_file.read().decode("utf-8")
    st.text_area(f"Uploaded contnet",content,height=200)

#Download button
sample_txt = "Hii, click me for download"
st.download_button(
    label= "Downloaded sample",
    data= sample_txt,
    file_name="sample.txt",
    mime = "text/plain"
)