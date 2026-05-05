import streamlit as st

# ==========================================
# 1. PAGE CONFIG & STYLING
# ==========================================
st.set_page_config(page_title="PSPCL Utility Hub", page_icon="⚡", layout="wide")

# Assets
PSPCL_LOGO_URL = "https://pspcl.in/assets/images/logo.png"
BEECLUE_LOGO_PNG = "https://raw.githubusercontent.com/iamanujnarang/LDHF/e5748e037b76a52a47d610a88c3a3c70f72f1c9a/BEECLUE.png"
INSTA_ICON = "https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png"
FB_ICON = "https://upload.wikimedia.org/wikipedia/commons/1/1b/Facebook_icon.svg"
X_ICON = "https://upload.wikimedia.org/wikipedia/commons/b/b7/X_logo.jpg"
LINKEDIN_ICON = "https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png"

# Custom CSS
st.markdown("""
<style>
    .main { background-color: #f0f2f6; }
    
    /* Header Centering */
    .header-container {
        text-align: center;
        padding-bottom: 20px;
    }

    /* App Card Styling */
    .app-card {
        background: white;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        border: 1px solid #eef2f6;
        text-align: center;
        transition: all 0.3s ease;
        height: 280px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        margin-bottom: 25px;
    }
    .app-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 15px 35px rgba(0,0,0,0.1);
        border-color: #0b79d0;
    }
    
    .launch-btn {
        background-color: #0b79d0;
        color: white !important;
        padding: 12px 25px;
        border-radius: 50px;
        text-decoration: none;
        font-weight: 600;
        display: inline-block;
        margin-top: 20px;
    }

    /* Footer Styling */
    .footer-container {
        text-align: center;
        margin-top: 80px;
        padding: 40px 20px;
        border-top: 1px solid #eee;
        background-color: #ffffff;
    }
    .made-with-love {
        font-size: 1.1rem;
        color: #334155;
        margin-bottom: 20px;
        font-weight: 500;
    }
    .heart-symbol {
        color: #e63946;
        display: inline-block;
        animation: heartbeat 1.5s infinite;
    }
    @keyframes heartbeat {
        0% { transform: scale(1); }
        50% { transform: scale(1.2); }
        100% { transform: scale(1); }
    }
    .social-icon {
        width: 32px;
        margin: 0 12px;
        transition: transform 0.3s ease;
    }
    .social-icon:hover { transform: scale(1.3); }

    .beeclue-box {
        background: #1e293b;
        padding: 20px 35px;
        border-radius: 15px;
        display: inline-block;
        margin-top: 25px;
    }
    .powered-text {
        color: #94a3b8;
        font-size: 0.7rem;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 8px;
    }
    .beeclue-img { width: 180px; height: auto; }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. CENTERED HEADER
# ==========================================
st.markdown(f"""
<div class="header-container">
    <img src="{PSPCL_LOGO_URL}" width="160">
    <h1 style="margin-top: 15px;">⚡ PSPCL Digital Toolbox</h1>
    <p style="font-size: 1.2rem; color: #64748b;">Official Utility Applications for Junior Engineers & Staff</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# ==========================================
# 3. APPLICATIONS GRID
# ==========================================
col_a, col_b = st.columns(2)

with col_a:
    st.markdown(f"""
    <div class="app-card">
        <h2 style="color: #1e293b;">⚡ LDHF Calculator</h2>
        <p style="color: #64748b;">Standard Assessment Method for calculating monthly units based on Load, Days, Hours, and Factor.[cite: 1]</p>
        <div><a href="https://ldhfcalculator.streamlit.app/" target="_blank" class="launch-btn">Launch App →</a></div>
    </div>
    """, unsafe_allow_html=True)

with col_b:
    st.markdown(f"""
    <div class="app-card">
        <h2 style="color: #1e293b;">📉 VD Calculator</h2>
        <p style="color: #64748b;">Voltage Drop calculation tool for efficient distribution planning and feeder maintenance.</p>
        <div><a href="https://pspclvdcalculator.streamlit.app/" target="_blank" class="launch-btn">Launch App →</a></div>
    </div>
    """, unsafe_allow_html=True)

st.info("💡 More utility tools like 'Transformer Loading' and 'Consumer Billing Abstract' are under development.")

# ==========================================
# 4. UPDATED FOOTER
# ==========================================
footer_html = f"""
<div class="footer-container">
<div class="made-with-love">Made with <span class="heart-symbol">❤️</span> by <b>Er. Anuj Narang, JE PSPCL</b></div>
<div style="margin-bottom: 25px;">
<a href="https://instagram.com/iamanujnarang" target="_blank"><img src="{INSTA_ICON}" class="social-icon"></a>
<a href="https://facebook.com/iamanujnarang" target="_blank"><img src="{FB_ICON}" class="social-icon"></a>
<a href="https://x.com/iamanujnarang" target="_blank"><img src="{X_ICON}" class="social-icon"></a>
<a href="https://linkedin.com/in/iamanujnarang" target="_blank"><img src="{LINKEDIN_ICON}" class="social-icon"></a>
</div>

<!-- Beeclue without box -->
<div style="margin-top: 25px;">
    <div class="powered-text">In Strategic Collaboration with</div>
    <a href="https://beeclue.com" target="_blank">
        <img src="{BEECLUE_LOGO_PNG}" class="beeclue-img">
    </a>
</div>

<div style="color: #94a3b8; font-size: 0.85rem; margin-top: 25px;">© 2026 | PSPCL Guidelines</div>
</div>
"""
st.markdown(footer_html, unsafe_allow_html=True)
