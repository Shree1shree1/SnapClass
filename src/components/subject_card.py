import streamlit as st

def subject_card(name, code, section, stats=None, footer_callback=None):
    
    # ✅ Build stats HTML separately as a plain string
    stats_html = ""
    if stats:
        stats_html = '<div style="display:flex; gap:8px; flex-wrap:wrap;">'
        for icon, label, value in stats:
            stats_html += f'<div style="background:#eb459e18; padding:5px 12px; border-radius:12px; font-size:0.9rem;">{icon} <b>{value}</b> {label}</div>'
        stats_html += '</div>'

    # ✅ Single f-string with stats injected inside
    html = f"""
        <div style="background:white; border-left:8px solid #eb459e; padding:20px 25px;
                    border-radius:16px; border:1px solid #e2e8f0; margin-bottom:16px; max-width:480px;">
            <h3 style="margin:0 0 6px 0; color:#1e293b; font-size:1.2rem;">{name}</h3>
            <p style="color:#64748b; margin:0 0 12px 0;">
                Code: <span style="background:#e0e3ff; color:#5865f2; padding:2px 8px; border-radius:5px;">{code}</span>
                &nbsp;| Section: {section}
            </p>
            {stats_html}
        </div>
    """

    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()