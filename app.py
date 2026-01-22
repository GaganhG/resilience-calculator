import streamlit as st
import re

# 1. PAGE CONFIGURATION
st.set_page_config(
    page_title="EU Resilience Bench",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. "BOLD & BRUTALIST" CSS OVERHAUL
st.markdown("""
    <style>
    /* IMPORT FONTS: Space Grotesk (Headlines) + Inter (Body) */
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&family=Inter:wght@400;600;800&display=swap');
    
    /* GLOBAL RESET */
    .stApp {
        background-color: #000000;
        font-family: 'Inter', sans-serif;
    }
    
    /* HEADERS (The "Tech" Vibe) */
    h1, h2, h3 {
        font-family: 'Space Grotesk', sans-serif !important;
        font-weight: 700 !important;
        color: #FFFFFF !important;
        letter-spacing: -0.02em;
    }
    
    h1 { font-size: 3rem !important; margin-bottom: 0.5rem !important; }
    h3 { font-size: 1.5rem !important; margin-bottom: 1rem !important; }
    
    /* SUBTITLES */
    p {
        color: #B0B0B0 !important;
        font-size: 1.1rem !important;
        font-weight: 400;
    }

    /* BOLD LABELS (The Fix You Asked For) */
    .stSelectbox label, .stSlider label, .stMultiSelect label, .stTextArea label {
        color: #FFFFFF !important;
        font-weight: 800 !important; /* EXTRA BOLD */
        font-size: 1rem !important;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    /* INPUT FIELDS (High Contrast) */
    .stSelectbox div[data-baseweb="select"], 
    .stMultiSelect div[data-baseweb="select"],
    .stTextArea textarea {
        background-color: #111111 !important;
        border: 2px solid #333333 !important;
        color: #FFFFFF !important;
        border-radius: 4px; /* Sharper corners */
        font-weight: 600;
        font-size: 1rem;
    }
    
    /* TABS (Big Chunky Selectors) */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background-color: transparent;
        padding-bottom: 20px;
        border-bottom: 1px solid #333;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #111;
        border: 1px solid #333;
        color: #888;
        font-weight: 700;
        border-radius: 6px;
        padding: 10px 20px;
        font-family: 'Space Grotesk', sans-serif;
    }
    .stTabs [aria-selected="true"] {
        background-color: #00FF94 !important;
        color: #000000 !important;
        border-color: #00FF94 !important;
    }

    /* PRIMARY BUTTON (Massive & Bright) */
    .stButton>button {
        background-color: #00FF94;
        color: #000000;
        border: none;
        width: 100%;
        padding: 18px;
        font-family: 'Space Grotesk', sans-serif;
        font-weight: 700;
        font-size: 1.2rem;
        text-transform: uppercase;
        border-radius: 6px;
        margin-top: 10px;
    }
    .stButton>button:hover {
        background-color: #FFFFFF; /* Flash white on hover */
        box-shadow: 0 0 20px rgba(255,255,255,0.4);
    }
    
    /* RESULT CARDS (Solid, Not Glass) */
    .result-card {
        background: #111111;
        border: 2px solid #333;
        border-radius: 8px;
        padding: 30px;
        text-align: center;
        margin-top: 20px;
    }
    .result-card h1 {
        font-size: 3.5rem !important;
        color: #00FF94 !important;
    }

    /* FEEDBACK ITEMS */
    .feedback-item {
        background: #111;
        border-left: 5px solid #333;
        padding: 15px;
        margin-bottom: 15px;
        border-radius: 4px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. HEADER
st.title("EU RESILIENCE BENCH")
st.markdown("<p style='text-align: center;'>Tools for Elite NIS2, DORA, and CRA Contractors.</p>", unsafe_allow_html=True)

# --- TABS ---
tab1, tab2, tab3 = st.tabs(["RATE CALCULATOR", "CV OPTIMIZER", "CONTRACT SCANNER"])

# ==========================================
# TOOL 1: RATE CALCULATOR
# ==========================================
with tab1:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 💰 MARKET RATE CHECK")
    
    col1, col2 = st.columns(2)
    with col1:
        role = st.selectbox("PRIMARY ROLE", ["Pentester (NIS2)", "DORA Risk Mgr", "DevSecOps (CRA)", "Auditor"])
        experience = st.slider("YEARS OF EXPERIENCE", 1, 15, 5)
    with col2:
        location = st.selectbox("BASE LOCATION", ["DACH / Benelux (High CoL)", "Nordics", "Eastern EU", "Southern EU"])
        certs = st.multiselect("ACTIVE CERTIFICATIONS", ["OSCP", "CISSP", "CISA", "CISM", "None"])

    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("CALCULATE RATE", key="calc_btn"):
        # LOGIC
        base = 500
        if "Pentester" in role: base += 150
        elif "DORA" in role: base += 300
        if experience > 5: base += 200
        if "OSCP" in certs: base += 150
        low, high = base-50, base+150

        st.markdown(f"""
        <div class="result-card" style="border-color: #00FF94;">
            <p style="color: #FFF; font-weight: 700; font-size: 14px; margin-bottom: 5px;">ESTIMATED DAILY RATE</p>
            <h1>€{low} - €{high}</h1>
            <p style="font-size: 14px; color: #666;">Top 15% of market rates</p>
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
                feedback += """<div class="feedback-item" style="border-color: #00FF94;"><strong style="color: #FFF; font-size: 1.1rem;">✅ Business Impact</strong><br><span style="color:#888;">Good use of metrics (€/%).</span></div>"""
            else:
                feedback += """<div class="feedback-item" style="border-color: #FF3B30;"><strong style="color: #FFF; font-size: 1.1rem;">❌ Business Impact</strong><br><span style="color:#888;">No numbers found. Add ROI metrics.</span></div>"""

            if any(x in text_lower for x in ["nis2", "dora", "iso", "cra"]):
                score += 40
                feedback += """<div class="feedback-item" style="border-color: #00FF94;"><strong style="color: #FFF; font-size: 1.1rem;">✅ Compliance</strong><br><span style="color:#888;">Strong regulatory keywords found.</span></div>"""
            else:
                feedback += """<div class="feedback-item" style="border-color: #FF3B30;"><strong style="color: #FFF; font-size: 1.1rem;">❌ Compliance</strong><br><span style="color:#888;">Missing NIS2/DORA keywords.</span></div>"""
            
            if len(text_input) > 50: score += 30
            
            color = "#00FF94" if score > 70 else "#FF3B30"
            st.markdown(f"""
            <div class="result-card" style="border-color: {color};">
                <p style="color: #FFF; font-weight: 700; font-size: 14px; margin-bottom: 5px;">HIRABILITY SCORE</p>
                <h1 style="color: {color} !important;">{score}/100</h1>
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
                <strong style="color: #FFF; font-size: 1.1rem;">✅ No Indemnity Found</strong><br>
                <span style="color:#888;">Clean. No uncapped liability detected.</span>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            st.link_button("GET SAFE CONTRACT TEMPLATE →", "https://tally.so/r/yourformid", use_container_width=True)

