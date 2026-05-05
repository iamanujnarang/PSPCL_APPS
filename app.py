import streamlit as st

# ==========================================
# 1. PAGE CONFIG & STYLING
# ==========================================
st.set_page_config(page_title="PSPCL Utility Hub", page_icon="⚡", layout="wide")

# Assets
PSPCL_LOGO_URL = "https://pspcl.in/assets/images/logo.png"
BEECLUE_LOGO_PNG = "https://beeclue.com/wp-content/uploads/2026/02/b-horizontal-logo-w-2048x506.png"

# Custom CSS for Professional Dashboard Look
st.markdown("""
<style>
    .main { background-color: #f0f2f6; }
    
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
    
    /* Button Styling */
    .launch-btn {
        background-color: #0b79d0;
        color: white !important;
        padding: 12px 25px;
        border-radius: 50px;
        text-decoration: none;
        font-weight: 600;
        display: inline-block;
        margin-top: 20px;
        transition: 0.3s;
    }
    .launch-btn:hover {
        background-color: #085da1;
        box-shadow: 0 5px 15px rgba(11, 121, 208, 0.3);
    }

    /* Footer */
    .footer {
        text-align: center;
        margin-top: 80px;
        padding: 40px;
        border-top: 1px solid #ddd;
    }
    .beeclue-box {
        background: #1e293b;
        padding: 20px;
        border-radius: 12px;
        display: inline-block;
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. HEADER
# ==========================================
col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    st.image(PSPCL_LOGO_URL, width=120)
    st.title("⚡ PSPCL Digital Toolbox")
    st.markdown("#### Official Utility Applications for Junior Engineers & Staff")
    st.write("Streamlining electrical calculations and utility management with precision.")

st.divider()

# ==========================================
# 3. APPLICATIONS GRID
# ==========================================
row1_col1, row1_col2 = st.columns(2)

with row1_col1:
    st.markdown(f"""
    <div class="app-card">
        <h2 style="color: #1e293b; margin-bottom:10px;">⚡ LDHF Calculator</h2>
        <p style="color: #64748b;">Standard Assessment Method as per Annexure-7 for calculating monthly units based on Load, Days, Hours, and Factor.</p>
        <div>
            <a href="https://ldhfcalculator.streamlit.app/" target="_blank" class="launch-btn">Launch App →</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

with row1_col2:
    st.markdown(f"""
    <div class="app-card">
        <h2 style="color: #1e293b; margin-bottom:10px;">📉 VD Calculator</h2>
        <p style="color: #64748b;">Voltage Drop calculation tool for efficient distribution planning and feeder maintenance analysis.</p>
        <div>
            <a href="https://pspclvdcalculator.streamlit.app/" target="_blank" class="launch-btn">Launch App →</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Optional: Add a placeholder for future apps
st.info("💡 More utility tools like 'Transformer Loading' and 'Consumer Billing Abstract' are under development.")

# ==========================================
# 4. FOOTER
# ==========================================
st.markdown(f"""
<div class="footer">
    <p style="font-size: 1.2rem; color: #334155;">Made with ❤️ by <b>Anuj Narang, JE PSPCL</b></p>
    
    <div class="beeclue-box">
        <p style="color: #94a3b8; font-size: 0.7rem; letter-spacing: 2px; margin-bottom:10px;">POWERED BY</p>
        <a href="https://beeclue.com" target="_blank">
            <img src="{BEECLUE_LOGO_PNG}" width="180">
        </a>
    </div>
    
    <p style="color: #94a3b8; margin-top: 20px; font-size: 0.8rem;">
        © 2026 PSPCL Utility Hub | Punjab State Power Corporation Limited
    </p>
</div>
""", unsafe_allow_html=True)
