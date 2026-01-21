import streamlit as st

# 1. PAGE CONFIGURATION (Dark Mode / Cyber Vibe)
st.set_page_config(
    page_title="EU Resilience Rate Calculator",
    page_icon="🛡️",
    layout="centered"
)

# Custom CSS to force the "Hacker" aesthetic
st.markdown("""
    <style>
    .stApp {
        background-color: #0E1117;
        color: #00FF41;
        font-family: 'Courier New', Courier, monospace;
    }
    h1, h2, h3 {
        color: #00FF41 !important;
    }
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
    .stAlert {
        background-color: #1c2229;
        color: #ffffff;
        border: 1px solid #00FF41;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. HEADER
st.title("🛡️ EU Resilience Rate Calculator")
st.markdown("**Check your market value for NIS2, DORA, and CRA projects.**")
st.markdown("---")

# 3. INPUTS (The Funnel)
col1, col2 = st.columns(2)

with col1:
    role = st.selectbox(
        "Select Your Primary Role",
        [
            "Pentester / Ethical Hacker (NIS2)",
            "Operational Resilience Mgr (DORA)",
            "DevSecOps / Product Security (CRA)",
            "ISO 27001 Auditor",
            "SOC Analyst"
        ]
    )
    experience = st.slider("Years of Experience", 1, 15, 5)

with col2:
    location = st.selectbox(
        "Your Base Location",
        [
            "DACH / Benelux (High CoL)",
            "Nordics (High CoL)",
            "Eastern EU (Poland/Romania/Estonia)",
            "Southern EU (Spain/Portugal)",
            "UK / Non-EU"
        ]
    )
    certs = st.multiselect(
        "Certifications (Select all that apply)",
        ["OSCP", "CISSP", "CISA", "CISM", "AWS Security", "None"]
    )

# 4. CALCULATION LOGIC (The Secret Sauce)
if st.button("CALCULATE MY RATE"):
    
    # Base Rates (Conservative Market Averages)
    base_rate = 500  

    # Role Multipliers
    if "Pentester" in role:
        base_rate += 150 # High demand for NIS2
    elif "DORA" in role:
        base_rate += 300 # Finance pays the most
    elif "CRA" in role:
        base_rate += 200 # Shortage of developers
    elif "Auditor" in role:
        base_rate += 250
    elif "SOC" in role:
        base_rate += 50

    # Experience Multiplier
    if experience > 10:
        base_rate += 300
    elif experience > 5:
        base_rate += 150
    elif experience > 2:
        base_rate += 50

    # Certification Premium
    if "OSCP" in certs: base_rate += 150 # The "Gold" standard for technical
    if "CISSP" in certs: base_rate += 100 # The "Gold" standard for management
    if "CISA" in certs: base_rate += 100

    # Location Adjustment (Arbitrage)
    if "DACH" in location or "Nordics" in location:
        base_rate += 150
    elif "Eastern EU" in location:
        base_rate -= 50 # Competitive pricing strategy
    elif "Southern EU" in location:
        base_rate -= 50

    # Range Calculation
    low_end = base_rate - 50
    high_end = base_rate + 150

    # 5. OUTPUT (The Hook)
    st.markdown("---")
    st.success(f"💶 **ESTIMATED DAILY RATE: €{low_end} - €{high_end}**")
    
    # Dynamic Marketing Text
    if "DORA" in role:
        st.info("💡 **Insight:** Banks are currently paying premium rates for DORA specialists to meet the Jan 2025 deadline.")
    elif "Pentester" in role:
        st.info("💡 **Insight:** Manufacturing companies are scrambling for NIS2 audits. Demand exceeds supply.")
    
    st.markdown("### 🚀 Want a contract at this rate?")
    st.markdown("We have 3 clients looking for this exact profile.")
    
    # CTA Button (Link to your Tally Form)
    # Replace the link below with your actual Tally URL
    st.link_button("JOIN THE BENCH (FREE)", "https://tally.so/r/yourformid")