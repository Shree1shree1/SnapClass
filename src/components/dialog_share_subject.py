import streamlit as st
import segno
import io

@st.dialog("Share Class Link")
def share_subject_dialog(subject_name,subject_code):
    app_domain ="snaproll-main.streamlit.app"
    join_url =f"{app_domain}/?join-code={subject_code}"

    st.header("Scan to Join")

    qr =segno.make(join_url)
    out =io.BytesIO()
    qr.save(out,kind ="png",scale =10,border =1)
    out.seek(0)

    col1,col2 =st.columns(2)

    with col1:
        st.markdown("### Copy Link")
        st.markdown(f"""
            <div style="
                background: #f4f4fb;
                border: 1.5px solid #c8caff;
                border-radius: 0.75rem;
                padding: 10px 14px;
                font-family: monospace;
                font-size: 0.85rem;
                color: #1a1a2e;
                word-break: break-all;
                margin-bottom: 8px;
            ">{join_url}</div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
            <div style="
                background: #f4f4fb;
                border: 1.5px solid #c8caff;
                border-radius: 0.75rem;
                padding: 10px 14px;
                font-family: monospace;
                font-size: 0.85rem;
                color: #1a1a2e;
                margin-bottom: 8px;
            ">{subject_code}</div>
        """, unsafe_allow_html=True)

        # ✅ REPLACE st.info() with styled box
        st.markdown(f"""
            <div style="
                background: #eef0ff;
                border: 1.5px solid #c8caff;
                border-radius: 0.75rem;
                padding: 12px 14px;
                color: #5865f2;
                font-size: 0.9rem;
                margin-top: 4px;
            ">
                📋 Copy this link to share on WhatsApp or Email
            </div>
        """, unsafe_allow_html=True)

        # ✅ Copy button
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("📋 Copy Link", type="primary", width="stretch"):
            st.write(f"`{join_url}`")
            st.toast("Link ready — copy it above!")

    with col2:
       st.markdown("### Scan to Join") 
       st.image(out.getvalue(),caption="QRCODE for class joining")