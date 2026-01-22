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
# TOOL 2: CV OPTIMIZER (PRO EDITION)
# ==========================================
with tab2:
    st.header("Roast My Profile (CISO Edition)")
    st.write("Paste your CV bullet points. We check for Impact, Tech, and Compliance.")
    
    text_input = st.text_area("Paste Text Here:", height=200, placeholder="Example: Led NIS2 audit for fintech client, reducing risk by 40%...")

    if st.button("ANALYZE TEXT", key="cv_btn"):
        if not text_input:
            st.error("Paste some text first.")
        else:
            score = 0
            feedback = []
            text_lower = text_input.lower()
            
            # 1. IMPACT ANALYSIS (Contextual)
            # We look for numbers NEAR impact words, not just random % signs.
            impact_pattern = r"(\d+(?:%|k|m|bn)|€\$?\d+)" # Finds 40%, 100k, €500
            if re.search(impact_pattern, text_lower):
                score += 25
                feedback.append("✅ **Business Impact:** Good. You are using numbers/metrics.")
            else:
                feedback.append("❌ **Business Impact:** You sound like a 'Doer' not an 'Achiever'. Add metrics (e.g., 'Reduced scan time by 40%').")

            # 2. COMPLIANCE CHECK (The Money Keywords)
            compliance_stack = ["nis2", "dora", "gdpr", "iso 27001", "tisax", "soc2", "cra"]
            found_comp = [kw for kw in compliance_stack if kw in text_lower]
            if found_comp:
                score += 25
                feedback.append(f"✅ **Regulation:** Strong. Found: {', '.join(found_comp).upper()}.")
            else:
                feedback.append("❌ **Regulation:** Major Red Flag. You must mention specific frameworks (NIS2, DORA) to get hired in EU.")

            # 3. TECH STACK CHECK (New!)
            tech_stack = ["burp", "nessus", "splunk", "sentinel", "kubernetes", "docker", "python", "bash", "wireshark"]
            found_tech = [kw for kw in tech_stack if kw in text_lower]
            if len(found_tech) >= 2:
                score += 20
                feedback.append(f"✅ **Tech Stack:** Solid. You mentioned: {', '.join(found_tech).title()}.")
            else:
                feedback.append("⚠️ **Tech Stack:** Light. Mention specific tools (e.g., Burp Suite, Splunk) to prove hands-on skills.")

            # 4. "PASSIVE" VOICE DETECTOR
            passive_words = ["helped", "assisted", "worked on", "responsible for"]
            found_passive = [kw for kw in passive_words if kw in text_lower]
            if found_passive:
                score -= 10
                feedback.append(f"⚠️ **Weak Language:** Stop using '{found_passive[0]}'. Use 'Orchestrated', 'Deployed', or 'Secured'.")
            else:
                score += 15
                feedback.append("✅ **Tone:** Strong, active leadership voice.")

            # 5. LENGTH CHECK
            word_count = len(text_input.split())
            if 30 <= word_count <= 400:
                score += 15
            else:
                feedback.append("⚠️ **Length:** Keep it between 30-400 words for a LinkedIn summary.")

            # SCORING MATH
            score = max(0, min(100, score)) # Cap at 0-100

            # DISPLAY
            col1, col2 = st.columns([1,2])
            with col1:
                st.metric("Hirability Score", f"{score}/100")
                if score > 80: st.success("VERDICT: ELITE")
                elif score > 50: st.warning("VERDICT: MID")
                else: st.error("VERDICT: WEAK")
            
            with col2:
                for f in feedback:
                    st.write(f)

            st.markdown("---")
            st.info("💡 **Pro Tip:** German clients pay +20% for 'DORA' experience. Add it if you have it.")
            st.link_button("GET A PROFESSIONAL REWRITE", "https://tally.so/r/yourformid")

