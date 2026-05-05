import streamlit as st
from src.Database.db import create_subject

@st.dialog("Create new Subject")
def create_subject_dialog(teacher_id):
    st.write("Enter the detail of new subject")
    sub_id = st.text_input("Subject Code")
    sub_name =st.text_input("Subject Name")
    sub_section = st.text_input("Section")

    if st.button("Create Subject Now",type ="primary",width="stretch"):
        if sub_id and sub_name and sub_section:
            try:
                create_subject(sub_id,sub_name,sub_section,teacher_id)
                st.toast("Subject created Successfully!")
                st.rerun()
            except Exception as e:
                st.error(f"Error: {str(e)}")

        else:
            st.warning("Please fill all the fields")


                