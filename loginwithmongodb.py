import streamlit as st
from pymongo import MongoClient

# MongoDB Connection
MONGO_URI = "mongodb://localhost:27017/"  # Change if using cloud DB
DB_NAME = "staff"
COLLECTION_NAME = "customers"

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

# Streamlit App UI
st.set_page_config(page_title="MongoDB Streamlit App", layout="wide")

# Sidebar Navigation
menu = ["Home", "Add Text", "View Data"]
choice = st.sidebar.selectbox("Navigation", menu)

# Home Page
if choice == "Home":
    st.title("Welcome to the MongoDB Streamlit App")
    
    # Fetch text from MongoDB
    texts = collection.find()
    
    # Display texts with scrolling
    with st.container():
        for text in texts:
            st.write(text["content"])
            st.markdown("---")

# Add Text Page
elif choice == "Add Text":
    st.title("Add New Text")
    text_input = st.text_area("Enter your text")
    
    if st.button("Save to Database"):
        if text_input:
            collection.insert_one({"content": text_input})
            st.success("Text saved successfully!")
        else:
            st.warning("Please enter some text before saving.")

# View Data Page
elif choice == "View Data":
    st.title("View All Texts in Database")
    texts = collection.find()
    
    for text in texts:
        st.text(text["content"])
        st.markdown("---")
