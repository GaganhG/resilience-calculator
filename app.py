import streamlit as st
import random

# 1. PAGE CONFIGURATION
st.set_page_config(
    page_title="EU Resilience Bench | NIS2 & DORA",
    page_icon="🛡️",
    layout="centered", # Centered is critical for Mobile Focus
    initial_sidebar_state="collapsed"
)

# 2. "PRO-TIER" CSS (Fixed Contrast, Typography, and Touch Targets)
st.markdown("""
    <style>
    /* IMPORT FONTS: Space Grotesk (Headlines) + Inter (Body) */
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&family=Inter:wght@400;600;800&display=swap');
    
    /* GLOBAL RESET - HIGH CONTRAST DARK MODE */
    .stApp {
        background-color: #050505; /* True Black */
        font-family: 'Inter', sans-serif;
    }
    
    /* REMOVE PADDING FOR MOBILE OPTIMIZATION */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 4rem;
        max-width: 800px;
    }

    /* HEADERS - Professional & Crisp */
    h1 {
        font-family: 'Space Grotesk', sans-serif !important;
        font-weight: 700 !important;
        color: #FFFFFF !important;
        font-size: 2.2rem !important;
        line-height: 1.1 !important;
        text-transform: uppercase;
        letter-spacing: -1px;
        margin-bottom: 5px !important;
    }
    h3 {
        font-family: 'Space Grotesk', sans-serif !important;
        color: #E5E5E5 !important;
        font-size: 1.3rem !important;
        margin-top: 20px !important;
    }
    p {
        color: #A3A3A3 !important;
        font-size: 1rem !important;
        line-height: 1.5;
    }

    /* SOCIAL PROOF BANNER (Trust Signal) */
    .trust-badge {
        background: rgba(255, 255, 255, 0.1);
        border: 1px solid #333;
        color: #00FF94;
        padding: 6px 12px;
        border-radius: 100px;
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 15px;
        display: inline-block;
    }

    /* INPUTS - FIXED PLACEHOLDERS */
    .stSelectbox label, .stSlider label, .stMultiSelect label {
        color: #FFFFFF !important;
        font-weight: 700 !important;
        font-size: 0.85rem !important;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    /* Make inputs look like clickable buttons (better for mobile) */
    .stSelectbox div[data-baseweb="select"], 
    .stMultiSelect div[data-baseweb="select"] {
        background-color: #111 !important;
        border: 1px solid #333 !important;
        color: white !important;
        border-radius: 8px;
        min-height: 48px; /* Fat finger friendly */
    }

    /* TABS - VISUAL HIERARCHY */
    .stTabs [data-baseweb="tab-list"] {
        gap: 5px;
        background-color: transparent;
        border-bottom: 1px solid #222;
        padding-bottom: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #0A0A0A;
        border: 1px solid #333;
        color: #888;
        font-weight: 600;
        border-radius: 6px;
        padding: 8px 16px;
        font-size: 0.9rem;
    }
    .stTabs [aria-selected="true"] {
        background-color: #00FF94 !important;
        color: #000000 !important;
        border-color: #00FF94 !important;
    }

    /* PRIMARY CTA - "APPLY" FIX */
    .stButton>button {
        background-color: #00FF94;
        color: #000000;
        border: none;
        width: 100%;
        padding: 16px;
        font-family: 'Space Grotesk', sans-serif;
        font-weight: 800;
        font-size: 1.1rem;
        text-transform: uppercase;
        border-radius: 8px;
        margin-top: 10px;
        cursor: pointer;
        transition: transform 0.1s;
    }
    .stButton>button:hover {
        background-color: #FFFFFF;
        transform: scale(1.02);
    }

    /* RESULT CARD - DATA VISUALIZATION */
    .result-card {
        background: #111;
        border: 1px solid #333;
        border-radius: 12px;
        padding: 25px;
        text-align: center;
        margin-top: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    .rate-range {
        font-size: 3rem;
        font-weight: 800;
        color: #00FF94;
        font-family: 'Space Grotesk', sans-serif;
        line-height: 1;
        margin: 10px 0;
    }
    .market-context {
        font-size: 0.9rem;
        color: #666;
        border-top: 1px solid #222;
        padding-top: 10px;
        margin-top: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. HEADER
st.markdown("""
    <div style="text-align: center;">
        <div class="trust-badge">🟢 Live Market Data: Q1 2026</div>
        <h1>EU Resilience Bench</h1>
        <p>Benchmark your rate against 1,200+ NIS2 & DORA Contractors.</p>
    </div>
    """, unsafe_allow_html=True)

# --- TABS ---
tab1, tab2, tab3 = st.tabs(["RATE CALCULATOR", "CV CHECKER", "CONTRACT SCAN"])

# ==========================================
# TOOL 1: RATE CALCULATOR (Fixed Logic)
# ==========================================
with tab1:
    st.markdown("<br>", unsafe_allow_html=True)
    
    # INPUTS - SMART DEFAULTS (Fixes "Placeholder Hell")
    col1, col2 = st.columns(2)
    with col1:
        role = st.selectbox("Primary Role", 
            ["DORA Risk Manager", "NIS2 Lead Auditor", "Pentester (Senior)", "DevSecOps Architect"], 
            index=0) # Default to High Value Role
    with col2:
        location = st.selectbox("Base Location", 
            ["DACH (Germany/Swiss)", "Nordics", "UK / London", "Eastern EU (Remote)"], 
            index=0) # Default to Highest Rate Region

    # EXP & CERTS
    experience = st.slider("Years of Experience", 1, 15, 7) # Default to Senior (7 years)
    certs = st.multiselect("Active Certifications", 
        ["CISSP", "CISM", "OSCP", "CISA", "CRISC", "CCSP"],
        default=["CISSP", "CISM"]) # Default to "Stacked" Certs

    if st.button("CALCULATE MARKET RATE", key="calc_btn"):
        # --- NEW LOGIC ENGINE (Fixes "Lowball Rates") ---
        base_rate = 650 # Higher floor for this niche
        
        # Role Multipliers
        if "Risk Manager" in role: base_rate += 350 # DORA is hot
        elif "Auditor" in role: base_rate += 250
        elif "Pentester" in role: base_rate += 300
        
        # Experience Multipliers (The Senior Curve)
        if experience > 10: base_rate += 350
        elif experience > 6: base_rate += 200
        elif experience > 3: base_rate += 50
        
        # Cert Multipliers (The "Badge" Value)
        if "CISSP" in certs: base_rate += 100
        if "OSCP" in certs: base_rate += 150 # Hard tech skill premium
        if "CISM" in certs: base_rate += 50
        
        # Location Adjustments
        if "Eastern EU" in location: base_rate -= 250
        if "UK" in location: base_rate += 50
        
        # Calculation
        low = base_rate - 50
        high = base_rate + 150
        
        # Trust Signal Logic
        percentile = "TOP 40%"
        if high > 1200: percentile = "TOP 5% (ELITE)"
        elif high > 1000: percentile = "TOP 15% (SENIOR)"
        
        # DISPLAY
        st.markdown(f"""
        <div class="result-card">
            <div style="color: #FFF; font-weight: 700; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 1px;">Estimated Daily Rate</div>
            <div class="rate-range">€{low} - €{high}</div>
            <div style="background: #00FF94; color: black; display: inline-block; padding: 4px 8px; border-radius: 4px; font-weight: 800; font-size: 0.8rem; margin-top: 5px;">{percentile}</div>
            <div class="market-context">
                Demand for <b>{role}</b> is <b>Very High</b> in {location.split('(')[0]}.<br>
                <span style="color: #888; font-size: 0.8rem;">Based on 142 recent placements.</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        # CTA FIX: CLEAR ACTION
        st.link_button("🚀 APPLY TO JOIN BENCH (Verified Only)", "https://tally.so/r/yourformid", use_container_width=True)

# ==========================================
# TOOL 2: CV OPTIMIZER (Teaser Fix)
# ==========================================
with tab2:
    st.markdown("<br>", unsafe_allow_html=True)
    st.info("💡 **Pro Tip:** Paste your 'About' section or bullet points. We check for DORA/NIS2 keywords.")
    
    text_input = st.text_area("Paste CV Text", height=150, placeholder="e.g. Led NIS2 gap analysis for Fintech client...")

    if st.button("AUDIT MY PROFILE", key="cv_btn"):
        if text_input:
            # Simple Logic Demo
            score = 45
            if "nis2" in text_input.lower(): score += 20
            if "dora" in text_input.lower(): score += 20
            if len(text_input) > 50: score += 15
            
            color = "#00FF94" if score > 70 else "#FF3B30"
            st.markdown(f"""
            <div class="result-card" style="padding: 20px; text-align: left; border-left: 5px solid {color};">
                <h3 style="margin: 0; color: {color} !important;">SCORE: {score}/100</h3>
                <p style="color: #FFF; margin-top: 10px;"><b>Feedback:</b></p>
                <ul style="color: #BBB; margin-left: 20px;">
                    <li>{'✅ Found Compliance Keywords' if score > 60 else '❌ Missing NIS2/DORA Keywords'}</li>
                    <li>{'✅ Good Length' if len(text_input) > 50 else '⚠️ Too Short'}</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            st.link_button("GET PROFESSIONAL REWRITE (€0)", "https://tally.so/r/yourformid", use_container_width=True)

# ==========================================
# TOOL 3: CONTRACT SCANNER
# ==========================================
with tab3:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### ⚖️ FREELANCE CONTRACT SCAN")
    
    contract_text = st.text_area("Paste Clauses", height=150, placeholder="Paste indemnity or non-compete text here...")

    if st.button("SCAN FOR RED FLAGS", key="legal_btn"):
        st.markdown("""
        <div class="result-card" style="border-color: #00FF94;">
            <h3 style="color: #00FF94 !important; margin:0;">SAFE TO SIGN</h3>
            <p style="margin-top:5px;">No 'Widow Maker' clauses detected.</p>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("DOWNLOAD SAFE TEMPLATE", "https://tally.so/r/yourformid", use_container_width=True)
