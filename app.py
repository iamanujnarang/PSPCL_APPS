import streamlit as st
import pandas as pd

# ==========================================
# 1. PAGE CONFIG & ASSETS
# ==========================================
st.set_page_config(page_title="PSPCL Rate Pro 2026", page_icon="💰", layout="wide")

# Assets
PSPCL_LOGO = "https://pspcl.in/assets/images/logo.png"
BEECLUE_LOGO_PNG = "https://raw.githubusercontent.com/iamanujnarang/LDHF/e5748e037b76a52a47d610a88c3a3c70f72f1c9a/BEECLUE.png"
INSTA_ICON = "https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png"
FB_ICON = "https://upload.wikimedia.org/wikipedia/commons/1/1b/Facebook_icon.svg"
X_ICON = "https://upload.wikimedia.org/wikipedia/commons/b/b7/X_logo.jpg"
LINKEDIN_ICON = "https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png"

# Custom CSS for Premium UI
st.markdown(f"""
    <style>
    .main {{ background-color: #f1f5f9; }}
    .header-box {{ text-align: center; padding: 30px; background: white; border-radius: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); margin-bottom: 30px; border-bottom: 5px solid #0b79d0; }}
    .stNumberInput, .stSelectbox, .stRadio {{ background: white; border-radius: 10px; }}
    
    /* Result Cards */
    .total-card {{ background: linear-gradient(135deg, #0b79d0 0%, #08538f 100%); color: white; padding: 35px; border-radius: 25px; text-align: center; box-shadow: 0 15px 30px -10px rgba(11, 121, 208, 0.5); }}
    .calc-card {{ background: white; padding: 20px; border-radius: 15px; border-left: 6px solid #0b79d0; margin-bottom: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.02); }}
    .formula-text {{ font-family: 'Courier New', monospace; color: #1e293b; background: #f8fafc; padding: 10px; border-radius: 8px; font-size: 0.9rem; border: 1px dashed #cbd5e1; }}
    
    /* Footer */
    .footer-container {{ text-align: center; margin-top: 80px; padding: 40px 20px; border-top: 1px solid #ddd; }}
    .social-icon {{ width: 30px; margin: 0 10px; transition: 0.3s; }}
    .social-icon:hover {{ transform: scale(1.2); }}
    .beeclue-img {{ width: 180px; height: auto; margin-top: 15px; }}
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. CALCULATION CORE (RESEARCHED DATA)
# ==========================================
def format_inr(number):
    s = str(int(round(number)))
    if len(s) <= 3: return s
    last_three = s[-3:]
    remaining = s[:-3]
    remaining = ",".join([remaining[max(i-2, 0):i] for i in range(len(remaining), 0, -2)][::-1])
    return remaining + "," + last_three

def get_rates(cat, load):
    # Data from CC 51/2024 & CC 25/2025
    year_factor = 1.06 # 6% Compounded for 2026
    res = {"p_fee": 0, "acd": 0, "scc": 0, "m_sec": 0, "logic": {}}
    
    # 1. PROCESSING FEE (CC 25/2025 Page 4)
    if load <= 7: 
        res["p_fee"] = 35 if cat == "DS" else 85
    elif load <= 100: 
        res["p_fee"] = 180
    elif load <= 150: 
        res["p_fee"] = 1000
    else: 
        res["p_fee"] = min(load * 12, 4000)
    res["logic"]["PF"] = f"Load Slab Based Processing Fee"

    # 2. SECURITY CONSUMPTION / ACD (CC 25/2025 Page 5)
    if cat == "DS":
        if load <= 7: rate = 600; formula = f"{load} kW x ₹600 (Bimonthly)"
        elif load <= 20: rate = 300; formula = f"{load} kW x ₹300"
        else: rate = 500; formula = f"{load} kVA x ₹500"
    elif cat == "NRS":
        if load <= 7: rate = 880; formula = f"{load} kW x ₹880 (Bimonthly)"
        elif load <= 20: rate = 470; formula = f"{load} kW x ₹470"
        else: rate = 700; formula = f"{load} kVA x ₹700"
    elif cat == "SP": rate = 650; formula = f"{load} kVA x ₹650"
    elif cat == "MS": rate = 900; formula = f"{load} kVA x ₹900"
    elif cat == "LS": rate = 1900; formula = f"{load} kVA x ₹1,900"
    
    res["acd"] = load * rate
    res["logic"]["ACD"] = formula

    # 3. SCC / SERVICE CONNECTION CHARGES (CC 51/2024 Annexure-1)
    if load <= 100:
        if cat == "DS":
            if load <= 2: s_rate = 550
            elif load <= 7: s_rate = 1250
            elif load <= 50: s_rate = 1900
            else: s_rate = 2100
        elif cat == "NRS":
            if load <= 7: s_rate = 1250
            elif load <= 20: s_rate = 2000
            else: s_rate = 2300
        else: s_rate = 3250 # SP/MS
        res["scc"] = load * s_rate
        res["logic"]["SCC"] = f"{load} units x ₹{s_rate} (Fixed Slab Charges)"
    elif load <= 150:
        res["scc"] = load * 1400
        res["logic"]["SCC"] = f"{load} kVA x ₹1,400 (Normative Cost 100-150)"
    else:
        # Proportionate Cost + 6% Compounded for 2026 (CC 51/2024 Page 7)
        base_prop = 1230 * year_factor
        res["scc"] = load * base_prop
        res["logic"]["SCC"] = f"{load} kVA x (₹1,230 x 1.06 Yearly Increment)"

    # 4. METER SECURITY (CC 25/2025 Page 6)
    if load <= 7: res["m_sec"] = 680; m_txt = "Single Phase Static/Smart"
    elif load <= 20: res["m_sec"] = 1290; m_txt = "Three Phase Whole Current"
    elif load <= 100: res["m_sec"] = 2460; m_txt = "LT CT Operated Meter"
    else: res["m_sec"] = 83240; m_txt = "11kV CT/PT Unit (Initial Security)"
    res["logic"]["MS"] = m_txt

    return res

# ==========================================
# 3. MAIN UI
# ==========================================
st.markdown(f"""
    <div class="header-box">
        <img src="{PSPCL_LOGO}" width="150">
        <h1 style="color: #1e293b; margin-top: 10px;">New Connection Rate Calculator</h1>
        <p style="color: #64748b; font-size: 1.1rem;">Based on CC 51/2024 & CC 25/2025 | <b>Projected Rates for 2026</b></p>
    </div>
""", unsafe_allow_html=True)

main_col1, main_col2 = st.columns([1, 1.2], gap="large")

with main_col1:
    st.subheader("📝 Connection Details")
    with st.container(border=True):
        category = st.selectbox("Consumer Category", ["DS", "NRS", "SP", "MS", "LS"], help="DS: Domestic, NRS: Commercial, LS: Large Supply")
        load_val = st.number_input("Enter Load / Contract Demand (kW/kVA)", min_value=0.1, value=5.0, step=1.0)
        st.write("---")
        st.caption("ℹ️ For loads above 100, kVA values are considered. For loads above 150, Proportionate Costing is applied with a 6% annual increment as per PSERC guidelines.")

with main_col2:
    data = get_rates(category, load_val)
    grand_total = data["p_fee"] + data["acd"] + data["scc"] + data["m_sec"]
    
    st.markdown(f"""
        <div class="total-card">
            <p style="font-size: 1.2rem; opacity: 0.9;">Total Estimated Demand Amount</p>
            <h1 style="font-size: 3.5rem; margin: 10px 0;">₹ {format_inr(grand_total)}</h1>
            <p style="font-size: 0.9rem; opacity: 0.8;">(Rounding applied as per PSPCL norms)</p>
        </div>
    """, unsafe_allow_html=True)

st.divider()

# Breakdown Sections
st.subheader("🔍 Calculation Breakdown")
b_col1, b_col2 = st.columns(2)

with b_col1:
    with st.container():
        st.markdown(f"""
            <div class="calc-card">
                <p style="color: #64748b; margin-bottom: 5px;">Service Connection Charges (SCC)</p>
                <h3 style="margin-top: 0;">₹ {format_inr(data["scc"])}</h3>
                <div class="formula-text">{data["logic"]["SCC"]}</div>
            </div>
            <div class="calc-card">
                <p style="color: #64748b; margin-bottom: 5px;">Security Consumption (ACD)</p>
                <h3 style="margin-top: 0;">₹ {format_inr(data["acd"])}</h3>
                <div class="formula-text">{data["logic"]["ACD"]}</div>
            </div>
        """, unsafe_allow_html=True)

with b_col2:
    with st.container():
        st.markdown(f"""
            <div class="calc-card">
                <p style="color: #64748b; margin-bottom: 5px;">Meter / Equipment Security</p>
                <h3 style="margin-top: 0;">₹ {format_inr(data["m_sec"])}</h3>
                <div class="formula-text">Category: {data["logic"]["MS"]}</div>
            </div>
            <div class="calc-card">
                <p style="color: #64748b; margin-bottom: 5px;">Processing Fee</p>
                <h3 style="margin-top: 0;">₹ {format_inr(data["p_fee"])}</h3>
                <div class="formula-text">{data["logic"]["PF"]}</div>
            </div>
        """, unsafe_allow_html=True)

# ==========================================
# 4. FOOTER
# ==========================================
st.markdown(f"""
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
    <div style="color: #94a3b8; font-size: 0.85rem; margin-top: 25px;">© 2026 | PSPCL Guidelines | CC 51/2024 & CC 25/2025</div>
</div>
""", unsafe_allow_html=True)
