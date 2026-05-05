import streamlit as st

def header_home():
    logo_url ="https://i.ibb.co/YTYGn5qV/logo.png"
    st.markdown(f"""
        <div style ="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:10px; margin-top:10px">        
            <img src ="{logo_url}" style ="height:100px;" />
            <h1 style ="text-align:center;  color:#e0e3ff">SNAP<br/>CLASS</h1>
        </div>    
""",unsafe_allow_html=True)
    
def header_dashboard():
    logo_url ="https://i.ibb.co/YTYGn5qV/logo.png"
    st.markdown(f"""
        <div style ="display:flex; align-items:center; justify-content:center;gap:10px;">        
            <img src ="{logo_url}" style ="height:80px;" />
            <h2 style ="text-align:left;  color:#5845f2; font-size:10px">SNAP<br/>CLASS</h2>
        </div>    
""",unsafe_allow_html=True)