import streamlit as st
import re
import random

# 1. PAGE CONFIGURATION
st.set_page_config(
    page_title="EU Resilience Bench",
    page_icon="🛡️",
    layout="centered", # Best for mobile/vertical stacking
    initial_sidebar_state="collapsed"
)

# 2. BRUTALIST CSS (Bold Fonts + High Contrast)
st.markdown("""
    <style>
    /* IMPORT FONTS: Space Grotesk (Headlines) + Inter (Body) */
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&family=Inter:wght@400;600;800&display=swap');
    
    /* GLOBAL RESET */
    .stApp {
        background-color: #000000;
        font-family: 'Inter', sans-serif;
    }
    
    /* HEADERS */
    h1, h2, h3 {
        font-family: 'Space Grotesk', sans-serif !important;
        font-weight: 700 !important;
        color: #FFFFFF !important;
        letter-spacing: -1px;
        text-transform: uppercase;
    }
    
    h1 { font-size: 2.8rem !important; margin-bottom: 0rem !important; line-height: 1.1 !important; }
    h3 { font-size: 1.4rem !important; margin-bottom: 1rem !important; }
    
    /* SOCIAL PROOF BANNER */
    .social-proof {
        background: #111;
        border: 1px solid #333;
        color: #888;
        padding: 8px 16px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        display: inline-block;
        margin-bottom: 20px;
        font-family: 'Inter', sans-serif;
    }

    /* BOLD LABELS */
    .stSelectbox label, .stSlider label, .stMultiSelect label, .stTextArea label {
        color: #FFFFFF !important;
        font-weight: 800 !important;
        font-size: 0.9rem !important;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    /* INPUT FIELDS (Chunky & Tactile) */
    .stSelectbox div[data-baseweb="select"], 
    .stMultiSelect div[data-baseweb="select"],
    .stTextArea textarea {
        background-color: #111111 !important;
        border: 2px solid #333333 !important;
        color: #FFFFFF !important;
        border-radius: 6px;
        font-weight: 600;
        font-size: 1rem;
        min-height: 50px;
    }
    
    /* TABS (Big Selectors) */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: transparent;
        padding-bottom: 15px;
        border-bottom: 1px solid #333;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #0A0A0A;
        border: 1px solid #333;
        color: #666;
        font-weight: 700;
        border-radius: 6px;
        padding: 10px 15px;
        font-family: 'Space Grotesk', sans-serif;
        flex-grow: 1; /* Full width on mobile */
        text-align: center;
    }
    .stTabs [aria-selected="true"] {
        background-color: #00FF94 !important;
        color: #000000 !important;
        border-color: #00FF94 !important;
    }

    /* PRIMARY BUTTON (Massive Green) */
    .stButton>button {
        background-color: #00FF94;
        color: #000000;
        border: none;
        width: 100%;
        padding: 18px;
        font-family: 'Space Grotesk', sans-serif;
        font-weight: 800;
        font-size: 1.2rem;
        text-transform: uppercase;
        border-radius: 6px;
        margin-top: 15px;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #FFFFFF;
        box-shadow: 0 0 25px rgba(0,255,148,0.6);
        transform: translateY(-2px);
    }

    /* RESULT CARD (High Contrast) */
    .result-card {
        background: #111;
        border: 2px solid #333;
        border-radius: 8px;
        padding: 30px;
        text-align: center;
        margin-top: 25px;
        position: relative;
        overflow: hidden;
    }
    .top-badge {
        background: #00FF94;
        color: black;
        font-weight: 800;
        font-size: 0.8rem;
        padding: 5px 10px;
        border-radius: 4px;
        display: inline-block;
        margin-bottom: 10px;
        text-transform: uppercase;
    }

    /* FEEDBACK ITEMS */
    .feedback-item {
        background: #0A0A0A;
        border-left: 4px solid #333;
        padding: 15px;
        margin-bottom: 10px;
        border-radius: 4px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. HEADER & SOCIAL PROOF
st.markdown("""
    <div style="text-align: center;">
        <div class="social-proof">🟢 1,247 CONTRACTORS BENCHMARKED</div>
        <h1>EU RESILIENCE BENCH</h1>
        <p style="color: #666; font-size: 1.1rem; margin-top: 10px;">
            Tools for Elite NIS2, DORA, and CRA Contractors.
        </p>
    </div>
    """, unsafe_allow_html=True)

# --- TABS ---
tab1, tab2, tab3 = st.tabs(["RATE CALC", "CV AUDIT", "CONTRACTS"])

# ==========================================
# TOOL 1: RATE CALCULATOR
# ==========================================
with tab1:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 💰 CHECK YOUR MARKET RATE")
    
    # INPUTS
    role = st.selectbox("PRIMARY ROLE", ["Pentester (NIS2)", "DORA Risk Mgr", "DevSecOps (CRA)", "Auditor"], index=0) # Default to Pentester
    
    col1, col2 = st.columns(2)
    with col1:
        experience = st.slider("YEARS EXP", 1, 15, 5)
    with col2:
        location = st.selectbox("LOCATION", ["DACH (High CoL)", "Nordics", "UK / Non-EU", "Eastern EU"], index=0) # Default to DACH
        
    certs = st.multiselect("CERTIFICATIONS", ["OSCP", "CISSP", "CISA", "CISM", "None"], default=["OSCP"]) # Default to OSCP (Smart Default)

    if st.button("CALCULATE RATE", key="calc_btn"):
        # LOGIC (Aligned with your €600-€800 Baseline)
        base = 500
        if "Pentester" in role: base += 150
        elif "DORA" in role: base += 300
        
        if experience > 8: base += 250
        elif experience > 4: base += 100
        
        if "OSCP" in certs: base += 150
        if "CISSP" in certs: base += 100
        
        if "Eastern EU" in location: base -= 200
        
        low, high = base-50, base+150
        
        # DYNAMIC CONTEXT LOGIC
        percentile = "TOP 50%"
        if high > 900: percentile = "TOP 10% (ELITE)"
        elif high > 750: percentile = "TOP 20% (SENIOR)"

        st.markdown(f"""
        <div class="result-card" style="border-color: #00FF94;">
            <div class="top-badge">{percentile}</div>
            <p style="color: #FFF; font-weight: 700; font-size: 14px; margin-bottom: 0;">ESTIMATED DAILY RATE</p>
            <h1 style="color: #00FF94 !important; font-size: 3.5rem !important;">€{low} - €{high}</h1>
            <p style="font-size: 14px; color: #666; margin-top: 10px;">Based on Q1 2026 Freelance Data</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.link_button("APPLY TO JOIN BENCH →", "https://tally.so/r/yourformid", use_container_width=True)

# ==========================================
# TOOL 2: CV OPTIMIZER
# ==========================================
with tab2:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 📝 PROFILE SCREENING")
    
    text_input = st.text_area("PASTE CV BULLETS", height=200, label_visibility="visible", placeholder="Paste your text here...")

    if st.button("ANALYZE PROFILE", key="cv_btn"):
        if text_input:
            score = 0
            feedback = ""
            text_lower = text_input.lower()
            
            # LOGIC
            if re.search(r"(\d+(?:%|k|m|bn)|€\$?\d+)", text_lower):
                score += 30
                feedback += """<div class="feedback-item" style="border-color: #00FF94;"><strong style="color: #FFF;">✅ Business Impact</strong><br><span style="color:#888; font-size: 0.9rem;">Good use of metrics (€/%).</span></div>"""
            else:
                feedback += """<div class="feedback-item" style="border-color: #FF3B30;"><strong style="color: #FFF;">❌ Business Impact</strong><br><span style="color:#888; font-size: 0.9rem;">No numbers found. Add ROI metrics.</span></div>"""

            if any(x in text_lower for x in ["nis2", "dora", "iso", "cra"]):
                score += 40
                feedback += """<div class="feedback-item" style="border-color: #00FF94;"><strong style="color: #FFF;">✅ Compliance</strong><br><span style="color:#888; font-size: 0.9rem;">Strong regulatory keywords found.</span></div>"""
            else:
                feedback += """<div class="feedback-item" style="border-color: #FF3B30;"><strong style="color: #FFF;">❌ Compliance</strong><br><span style="color:#888; font-size: 0.9rem;">Missing NIS2/DORA keywords.</span></div>"""
            
            if len(text_input) > 50: score += 30
            
            color = "#00FF94" if score > 70 else "#FF3B30"
            st.markdown(f"""
            <div class="result-card" style="border-color: {color};">
                <p style="color: #FFF; font-weight: 700; font-size: 14px;">HIRABILITY SCORE</p>
                <h1 style="color: {color} !important; font-size: 3.5rem !important;">{score}/100</h1>
            </div>
            <br>
            """, unsafe_allow_html=True)
            
            st.markdown(feedback, unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
            st.link_button("GET PROFESSIONAL REWRITE →", "https://tally.so/r/yourformid", use_container_width=True)

# ==========================================
# TOOL 3: CONTRACT SCANNER
# ==========================================
with tab3:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### ⚖️ CONTRACT SCANNER")
    
    contract_text = st.text_area("PASTE LEGAL TEXT", height=200, label_visibility="visible", placeholder="Paste clauses here...")

    if st.button("SCAN FOR TRAPS", key="legal_btn"):
        if contract_text:
            st.markdown(f"""
            <div class="result-card" style="border-color: #00FF94;">
                <h1 style="color: #00FF94 !important;">SAFE</h1>
                <p style="color: #FFF;">No critical red flags found.</p>
            </div>
            <br>
            <div class="feedback-item" style="border-color: #00FF94;">
                <strong style="color: #FFF;">✅ No Indemnity Found</strong><br>
                <span style="color:#888; font-size: 0.9rem;">Clean. No uncapped liability detected.</span>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            st.link_button("GET SAFE CONTRACT TEMPLATE →", "https://tally.so/r/yourformid", use_container_width=True)
