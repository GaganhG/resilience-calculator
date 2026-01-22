import streamlit as st
import re

# 1. PAGE CONFIGURATION
st.set_page_config(
    page_title="EU Resilience Bench Tools",
    page_icon="🛡️",
    layout="centered"
)

# 2. GLOBAL STYLING (The "Hacker" Vibe)
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background-color: #0E1117;
        color: #00FF41;
        font-family: 'Courier New', Courier, monospace;
    }
    
    /* Headlines */
    h1, h2, h3 {
        color: #00FF41 !important;
    }

    /* Labels */
    .stSelectbox label, .stSlider label, .stMultiSelect label, .stRadio label, .stTextArea label {
        color: #FFFFFF !important;
        font-weight: bold;
    }

    /* Tabs Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: #1c2229;
        border-radius: 5px;
        color: #ffffff;
        font-weight: bold;
    }
    .stTabs [aria-selected="true"] {
        background-color: #00FF41 !important;
        color: #000000 !important;
    }

    /* Button Styling */
    .stButton>button {
        background-color: #00FF41;
        color: #000000;
        border-radius: 5px;
        font-weight: bold;
        border: none;
        width: 100%;
        padding: 10px;
    }
    .stButton>button:hover {
        background-color: #00cc33;
        color: #000000;
    }

    /* Alert Box */
    .stAlert {
        background-color: #1c2229;
        color: #ffffff;
        border: 1px solid #00FF41;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. HEADER
st.title("🛡️ EU Resilience Bench")
st.write("Tools for Elite NIS2, DORA, and CRA Contractors.")

# --- TABS CONFIGURATION ---
tab1, tab2 = st.tabs(["💰 RATE CALCULATOR", "📝 CV OPTIMIZER"])

# ==========================================
# TOOL 1: RATE CALCULATOR (Inside Tab 1)
# ==========================================
with tab1:
    st.header("Check Your Market Rate")
    
    col1, col2 = st.columns(2)
    with col1:
        role = st.selectbox(
            "Primary Role",
            ["Pentester (NIS2)", "DORA Risk Mgr", "DevSecOps (CRA)", "Auditor", "SOC Analyst"]
        )
        experience = st.slider("Years of Exp", 1, 15, 5)

    with col2:
        location = st.selectbox(
            "Base Location",
            ["DACH / Benelux (High CoL)", "Nordics", "Eastern EU", "Southern EU", "UK / Non-EU"]
        )
        certs = st.multiselect(
            "Certifications",
            ["OSCP", "CISSP", "CISA", "CISM", "None"]
        )

    if st.button("CALCULATE RATE", key="calc_btn"):
        base_rate = 500
        
        # Logic
        if "Pentester" in role: base_rate += 150
        elif "DORA" in role: base_rate += 300
        elif "CRA" in role: base_rate += 200
        elif "Auditor" in role: base_rate += 250

        if experience > 10: base_rate += 300
        elif experience > 5: base_rate += 150
        
        if "OSCP" in certs: base_rate += 150
        if "CISSP" in certs: base_rate += 100
        
        if "DACH" in location: base_rate += 150
        elif "Eastern EU" in location: base_rate -= 50

        low = base_rate - 50
        high = base_rate + 150

        st.success(f"💶 ESTIMATED DAILY RATE: €{low} - €{high}")
        st.info("💡 We have clients looking for this profile.")
        # REPLACE THIS LINK with your actual Tally form
        st.link_button("JOIN THE BENCH", "https://tally.so/r/yourformid")

# ==========================================
# TOOL 2: CV OPTIMIZER (Inside Tab 2)
# ==========================================
with tab2:
    st.header("Roast My Profile")
    st.write("Does your CV speak 'Engineer' or 'Consultant'?")
    
    text_input = st.text_area("Paste your LinkedIn 'About' or CV bullets:", height=150)

    if st.button("ANALYZE TEXT", key="cv_btn"):
        if not text_input:
            st.error("Paste some text first.")
        else:
            score = 0
            feedback = []
            
            # Logic
            if re.search(r"(\$|€|%|budget|saved|ROI)", text_input, re.IGNORECASE):
                score += 30
                feedback.append("✅ **Business Impact:** Good usage of money metrics.")
            else:
                feedback.append("❌ **Business Impact:** No money found. Add € or %.")

            if re.search(r"(nis2|dora|iso|compliance|audit)", text_input.lower()):
                score += 40
                feedback.append("✅ **Regulation:** Strong compliance keywords.")
            else:
                feedback.append("❌ **Regulation:** Missing NIS2/DORA keywords.")

            if len(text_input.split()) < 20:
                feedback.append("⚠️ **Length:** Too short.")
            else:
                score += 30

            st.metric("Hirability Score", f"{score}/100")
            for f in feedback:
                st.write(f)
            
            # REPLACE THIS LINK with your actual Tally form
            st.link_button("GET A REWRITE (JOIN BENCH)", "https://tally.so/r/yourformid")
