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
    .main { background-color: #f8fafc; }
    
    /* Header Centering */
    .header-container {
        text-align: center;
        padding-bottom: 20px;
    }

    /* App Card Styling */
    .app-card {
        background: white;
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        border: 1px solid #eef2f6;
        text-align: center;
        transition: all 0.3s ease;
        height: 340px; 
        display: flex;
        flex-direction: column;
        justify-content: space-between;
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
        padding: 10px 20px;
        border-radius: 50px;
        text-decoration: none;
        font-weight: 600;
        display: inline-block;
        font-size: 0.9rem;
    }

    /* Footer Styling */
    .footer-container {
        text-align: center;
        margin-top: 80px;
        padding: 40px 20px;
        border-top: 1px solid #ddd;
    }
    .made-with-love {
        font-size: 1.2rem;
        color: #334155;
        margin-bottom: 20px;
    }
    .heart-symbol { color: #e63946; }
    .social-icon {
        width: 30px;
        margin: 0 10px;
        transition: 0.3s;
    }
    .social-icon:hover { transform: scale(1.2); }

    .powered-text {
        color: #94a3b8;
        font-size: 0.7rem;
        letter-spacing: 2px;
        margin-bottom: 10px;
        text-transform: uppercase;
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
    <p style="font-size: 1.2rem; color: #64748b;">Un-official Utility Applications for Junior Engineers & Staff</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# ==========================================
# 3. APPLICATIONS GRID
# ==========================================
# Row 1 - Three Apps
row1_col1, row1_col2, row1_col3 = st.columns(3)

with row1_col1:
    st.markdown(f"""
    <div class="app-card">
        <div>
            <h2 style="color: #1e293b;">⚡ LDHF Calculator</h2>
            <p style="color: #64748b;">Standard Assessment Method for calculating monthly units based on Load, Days, Hours, and Factor as per Supply Code.</p>
        </div>
        <div><a href="https://ldhfcalculator.streamlit.app/" target="_blank" class="launch-btn">Launch App →</a></div>
    </div>
    """, unsafe_allow_html=True)

with row1_col2:
    st.markdown(f"""
    <div class="app-card">
        <div>
            <h2 style="color: #1e293b;">🏗️ Colony Load Calculator</h2>
            <p style="color: #64748b;">Advanced tool for Colony load assessment including FAR logic, demand factors (40%/50%), and DT capacity planning.</p>
        </div>
        <div><a href="https://colonyload.streamlit.app/" target="_blank" class="launch-btn">Launch App →</a></div>
    </div>
    """, unsafe_allow_html=True)

with row1_col3:
    st.markdown(f"""
    <div class="app-card">
        <div>
            <h2 style="color: #1e293b;">💰 Proportionate Cost Calculator</h2>
            <p style="color: #64748b;">Calculate connectivity charges, SLC, and Bank Guarantee (35%/105%) for new connections and colonies.</p>
        </div>
        <div><a href="https://proratacal.streamlit.app/" target="_blank" class="launch-btn">Launch App →</a></div>
    </div>
    """, unsafe_allow_html=True)

# Row 2 - Two Apps
row2_space1, row2_col4, row2_col5, row2_space2 = st.columns([1, 4, 4, 1])

with row2_col4:
    st.markdown(f"""
    <div class="app-card">
        <div>
            <h2 style="color: #1e293b;">🔌 Load Calculator</h2>
            <p style="color: #64748b;">Automated Connected Load computation for domestic and commercial categories based on Annexure-1 norms.</p>
        </div>
        <div><a href="https://loadcal.streamlit.app/" target="_blank" class="launch-btn">Launch App →</a></div>
    </div>
    """, unsafe_allow_html=True)

with row2_col5:
    st.markdown(f"""
    <div class="app-card">
        <div>
            <h2 style="color: #1e293b;">📉 VD Calculator</h2>
            <p style="color: #64748b;">Voltage Drop calculation tool for efficient distribution planning, line maintenance, and technical feasibility.</p>
        </div>
        <div><a href="https://pspclvdcalculator.streamlit.app/" target="_blank" class="launch-btn">Launch App →</a></div>
    </div>
    """, unsafe_allow_html=True)

st.info("💡 Pro-Tip: These tools are strictly based on Supply Code 2024 and latest Commercial Circulars (CC 45/2024 & CC 35/2025).")

# ==========================================
# 4. FOOTER
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

<div style="margin-top: 25px;">
    <div class="powered-text">In Strategic Collaboration with</div>
    <a href="https://beeclue.com" target="_blank">
        <img src="{BEECLUE_LOGO_PNG}" class="beeclue-img">
    </a>
</div>

<div style="color: #94a3b8; font-size: 0.85rem; margin-top: 25px;">© 2026 | PSPCL Guidelines | CC 45/2024</div>
</div>
"""
st.markdown(footer_html, unsafe_allow_html=True)
