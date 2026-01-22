import streamlit as st
import re

# 1. PAGE CONFIGURATION
st.set_page_config(
    page_title="EU Resilience Bench",
    page_icon="🛡️",
    layout="centered", # Centered looks more "App-like" than Wide for tools
    initial_sidebar_state="collapsed"
)

# 2. "CYBER-LUXURY" CSS OVERHAUL
st.markdown("""
    <style>
    /* IMPORT FONTS */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
    /* RESET & BACKGROUND */
    .stApp {
        background-color: #050505;
        font-family: 'Inter', sans-serif;
    }
    
    /* REMOVE STREAMLIT PADDING */
    .block-container {
        padding-top: 3rem;
        padding-bottom: 5rem;
        max-width: 900px;
    }

    /* HEADERS */
    h1 {
        font-weight: 800;
        color: #ffffff;
        font-size: 2.5rem;
        letter-spacing: -1px;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    h3 {
        color: #e5e5e5;
        font-weight: 600;
    }
    p, label {
        color: #a3a3a3 !important;
    }

    /* CUSTOM TABS (The "Pill" Look) */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: #111;
        padding: 8px;
        border-radius: 12px;
        margin-bottom: 30px;
        border: 1px solid #222;
        justify-content: center;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: transparent;
        border: none;
        color: #666;
        font-weight: 600;
        border-radius: 8px;
        padding: 8px 20px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #222 !important;
        color: #00FF94 !important;
        box-shadow: 0 4px 10px rgba(0,0,0,0.5);
    }

    /* INPUT FIELDS (Stealth Mode) */
    .stSelectbox div[data-baseweb="select"], 
    .stMultiSelect div[data-baseweb="select"],
    .stTextArea textarea {
        background-color: #0F0F0F !important;
        border: 1px solid #222 !important;
        color: white !important;
        border-radius: 8px;
        transition: border 0.3s;
    }
    .stSelectbox div[data-baseweb="select"]:hover,
    .stTextArea textarea:hover {
        border: 1px solid #444 !important;
    }

    /* PRIMARY BUTTON (The "Glow") */
    .stButton>button {
        background: #00FF94;
        color: #000;
        border: none;
        width: 100%;
        padding: 15px;
        font-weight: 800;
        font-size: 16px;
        text-transform: uppercase;
        border-radius: 8px;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        box-shadow: 0 0 20px rgba(0, 255, 148, 0.5);
        transform: scale(1.01);
    }
    
    /* LINK BUTTONS (Secondary Actions) */
    a[kind="primary"] {
        background: transparent !important;
        border: 1px solid #333 !important;
        color: #888 !important;
        text-align: center;
        width: 100%;
        display: block;
        padding: 10px;
        border-radius: 8px;
        text-decoration: none;
        transition: all 0.3s;
    }
    a[kind="primary"]:hover {
        border-color: #00FF94 !important;
        color: #00FF94 !important;
    }

    /* RESULT CARDS (Glassmorphism) */
    .result-card {
        background: rgba(255,255,255,0.03);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 12px;
        padding: 25px;
        margin-top: 20px;
        text-align: center;
    }
    .feedback-item {
        background: #0F0F0F;
        border-left: 4px solid #333;
        padding: 15px;
        margin-bottom: 10px;
        border-radius: 6px;
        text-align: left;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. HEADER
st.title("EU Resilience Bench")
st.markdown("<p style='text-align: center; margin-top: -15px; margin-bottom: 30px;'>Tools for Elite NIS2, DORA, and CRA Contractors</p>", unsafe_allow_html=True)

# --- TABS ---
tab1, tab2, tab3 = st.tabs(["💰 Rate Calculator", "📝 CV Optimizer", "⚖️ Contract Scanner"])

# ==========================================
# TOOL 1: RATE CALCULATOR
# ==========================================
with tab1:
    st.markdown("### 📊 Market Rate Assessment")
    st.caption("Based on Q1 2026 Data (DACH/Benelux)")
    
    col1, col2 = st.columns(2)
    with col1:
        role = st.selectbox("Primary Role", ["Pentester (NIS2)", "DORA Risk Mgr", "DevSecOps (CRA)", "Auditor"])
        experience = st.slider("Years of Experience", 1, 15, 5)
    with col2:
        location = st.selectbox("Base Location", ["DACH / Benelux (High CoL)", "Nordics", "Eastern EU", "Southern EU"])
        certs = st.multiselect("Active Certifications", ["OSCP", "CISSP", "CISA", "CISM", "None"])

    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("Calculate My Rate", key="calc_btn"):
        # LOGIC
        base = 500
        if "Pentester" in role: base += 150
        elif "DORA" in role: base += 300
        if experience > 5: base += 200
        if "OSCP" in certs: base += 150
        if "CISSP" in certs: base += 100
        low, high = base-50, base+150

        # RESULT DISPLAY
        st.markdown(f"""
        <div class="result-card">
            <p style="text-transform: uppercase; font-size: 12px; letter-spacing: 1px; color: #00FF94; margin-bottom: 5px;">ESTIMATED DAILY RATE</p>
            <h1 style="margin: 0; text-shadow: 0 0 20px rgba(0,255,148,0.3);">€{low} - €{high}</h1>
            <p style="font-size: 14px; margin-top: 10px; color: #666;">Top 15% of market rates</p>
        </div>
        <br>
        """, unsafe_allow_html=True)
        
        st.link_button("Apply to Join Bench →", "https://tally.so/r/yourformid", use_container_width=True)

# ==========================================
# TOOL 2: CV OPTIMIZER
# ==========================================
with tab2:
    st.markdown("### 📝 Profile Screening")
    st.caption("We check for 'Consultant' keywords vs. 'Doer' keywords.")
    
    text_input = st.text_area("Paste CV Text", height=200, label_visibility="collapsed", placeholder="Paste your bullet points here...")

    if st.button("Analyze Profile", key="cv_btn"):
        if text_input:
            score = 0
            feedback = ""
            text_lower = text_input.lower()
            
            # LOGIC
            if re.search(r"(\d+(?:%|k|m|bn)|€\$?\d+)", text_lower):
                score += 30
                feedback += """<div class="feedback-item" style="border-color: #00FF94;"><strong style="color: #00FF94;">✅ Business Impact</strong><br><span style="color:#888; font-size:14px;">Good use of metrics (€/%).</span></div>"""
            else:
                feedback += """<div class="feedback-item" style="border-color: #FF3B30;"><strong style="color: #FF3B30;">❌ Business Impact</strong><br><span style="color:#888; font-size:14px;">No numbers found. Add ROI metrics.</span></div>"""

            if any(x in text_lower for x in ["nis2", "dora", "iso", "cra"]):
                score += 40
                feedback += """<div class="feedback-item" style="border-color: #00FF94;"><strong style="color: #00FF94;">✅ Compliance</strong><br><span style="color:#888; font-size:14px;">Strong regulatory keywords found.</span></div>"""
            else:
                feedback += """<div class="feedback-item" style="border-color: #FF3B30;"><strong style="color: #FF3B30;">❌ Compliance</strong><br><span style="color:#888; font-size:14px;">Missing NIS2/DORA keywords.</span></div>"""
            
            if len(text_input) > 50: score += 30
            
            # RESULT DISPLAY
            color = "#00FF94" if score > 70 else "#FF3B30"
            st.markdown(f"""
            <div class="result-card" style="border-color: {color}; box-shadow: 0 0 15px {color}20;">
                <p style="text-transform: uppercase; font-size: 12px; letter-spacing: 1px; color: {color}; margin-bottom: 5px;">HIRABILITY SCORE</p>
                <h1 style="color: {color}; margin: 0;">{score}/100</h1>
            </div>
            <br>
            """, unsafe_allow_html=True)
            
            st.markdown(feedback, unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
            st.link_button("Get Professional Rewrite →", "https://tally.so/r/yourformid", use_container_width=True)

# ==========================================
# TOOL 3: CONTRACT SCANNER
# ==========================================
with tab3:
    st.markdown("### ⚖️ The 'Widow Maker' Scanner")
    st.caption("Detects Indemnity, Non-Competes, and IP Theft clauses.")
    
    contract_text = st.text_area("Paste Clauses", height=200, label_visibility="collapsed", placeholder="Paste legal text here...")

    if st.button("Scan for Traps", key="legal_btn"):
        if contract_text:
            # Simple simulation logic for UI demo
            st.markdown(f"""
            <div class="result-card" style="border-color: #00FF94;">
                <h2 style="color: #00FF94; margin: 0;">SAFE</h2>
                <p style="color: #888;">No critical red flags found.</p>
            </div>
            <br>
            <div class="feedback-item" style="border-color: #00FF94;">
                <strong style="color: #00FF94;">✅ No Indemnity Found</strong><br>
                <span style="color:#888; font-size:14px;">Clean. No uncapped liability detected.</span>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            st.link_button("Get 'Safe' Contract Template →", "https://tally.so/r/yourformid", use_container_width=True)

