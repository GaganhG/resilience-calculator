import streamlit as st
import re

# 1. PAGE CONFIGURATION
st.set_page_config(
    page_title="EU Resilience Bench",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. "STEALTH MODE" CSS (Dark, Professional, "Cyber-Luxury")
st.markdown("""
    <style>
    /* IMPORT INTER FONT */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&display=swap');

    /* GLOBAL DARK THEME */
    .stApp {
        background-color: #0A0A0A;
        font-family: 'Inter', sans-serif;
        color: #E5E7EB;
    }

    /* REMOVE PADDING */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1000px;
    }

    /* HEADERS */
    h1, h2, h3 {
        color: #FFFFFF !important;
        font-weight: 700;
        letter-spacing: -0.5px;
    }
    p { color: #9CA3AF; font-size: 16px; }

    /* GLASSMORPHISM CARDS */
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 12px;
        padding: 25px;
        margin-bottom: 20px;
    }

    /* INPUT FIELDS */
    .stSelectbox div[data-baseweb="select"], 
    .stMultiSelect div[data-baseweb="select"],
    .stTextArea textarea {
        background-color: #111111 !important;
        border: 1px solid #333333 !important;
        color: #FFFFFF !important;
        border-radius: 8px;
    }
    
    /* TABS */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: transparent;
        border-bottom: 1px solid #333;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: transparent;
        color: #6B7280;
        border: none;
        font-weight: 600;
    }
    .stTabs [aria-selected="true"] {
        color: #00FF94 !important;
        border-bottom: 2px solid #00FF94;
    }

    /* BUTTONS */
    .stButton>button {
        background: linear-gradient(135deg, #00FF94 0%, #00CC76 100%);
        color: #000000;
        border: none;
        border-radius: 6px;
        font-weight: 700;
        padding: 12px 24px;
        text-transform: uppercase;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        box-shadow: 0 0 15px rgba(0, 255, 148, 0.4);
        transform: translateY(-1px);
        color: #000000;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. HEADER
col1, col2 = st.columns([2, 1])
with col1:
    st.title("EU Resilience Bench")
    st.markdown("Tools for Elite NIS2, DORA, and CRA Contractors.")

# --- TABS CONFIGURATION ---
tab1, tab2, tab3 = st.tabs(["💰 Rate Calculator", "📝 CV Optimizer", "⚖️ Contract Scanner"])

# ==========================================
# TOOL 1: RATE CALCULATOR (Tab 1)
# ==========================================
with tab1:
    st.markdown("<br>", unsafe_allow_html=True)
    with st.container():
        st.markdown("""
        <div class="glass-card">
            <h3 style="margin-top:0;">💰 Market Rate Assessment</h3>
            <p style="margin-bottom:0;">German & Dutch market data (Q1 2026)</p>
        </div>
        """, unsafe_allow_html=True)

        col_a, col_b = st.columns(2)
        with col_a:
            role = st.selectbox("Primary Role", ["Pentester (NIS2)", "DORA Risk Mgr", "DevSecOps (CRA)", "Auditor", "SOC Analyst"])
            experience = st.slider("Years of Experience", 1, 15, 5)
        with col_b:
            location = st.selectbox("Base Location", ["DACH / Benelux (High CoL)", "Nordics", "Eastern EU", "Southern EU", "UK / Non-EU"])
            certs = st.multiselect("Active Certifications", ["OSCP", "CISSP", "CISA", "CISM", "None"])

        st.markdown("<br>", unsafe_allow_html=True)
        
        if st.button("Calculate Rate", key="calc_btn", use_container_width=True):
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

            st.markdown(f"""
            <div style="background: rgba(0, 255, 148, 0.05); border: 1px solid #00FF94; border-radius: 8px; padding: 20px; text-align: center;">
                <p style="color: #00FF94; font-weight: 700; margin: 0; text-transform: uppercase; font-size: 12px;">ESTIMATED DAILY RATE</p>
                <h1 style="color: #FFFFFF; font-size: 48px; margin: 10px 0; text-shadow: 0 0 20px rgba(0,255,148,0.2);">€{low} - €{high}</h1>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
            st.link_button("Apply to Join Bench →", "https://tally.so/r/yourformid", use_container_width=True)

# ==========================================
# TOOL 2: CV OPTIMIZER (Tab 2)
# ==========================================
with tab2:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div class="glass-card">
        <h3 style="margin-top:0;">📝 Profile Screening</h3>
        <p>Paste your CV bullets. We check for CISO triggers.</p>
    </div>
    """, unsafe_allow_html=True)

    text_input = st.text_area("Paste CV Text", height=200, label_visibility="collapsed", placeholder="Example: Led NIS2 audit...")

    if st.button("Analyze Profile", key="cv_btn", use_container_width=True):
        if not text_input:
            st.error("Please enter text to analyze.")
        else:
            score = 0
            feedback_html = ""
            text_lower = text_input.lower()
            
            # LOGIC
            # 1. Impact
            if re.search(r"(\d+(?:%|k|m|bn)|€\$?\d+)", text_lower):
                score += 25
                feedback_html += """<div style='margin: 10px 0; padding: 15px; background: rgba(0, 255, 148, 0.1); border-left: 3px solid #00FF94; border-radius: 4px;'><strong style='color: #00FF94;'>✅ Business Impact</strong><br><span style='color: #ccc; font-size: 14px;'>Good metrics detected.</span></div>"""
            else:
                feedback_html += """<div style='margin: 10px 0; padding: 15px; background: rgba(255, 59, 48, 0.1); border-left: 3px solid #FF3B30; border-radius: 4px;'><strong style='color: #FF3B30;'>❌ Business Impact</strong><br><span style='color: #ccc; font-size: 14px;'>No numbers found. Add ROI (€, %).</span></div>"""

            # 2. Compliance
            comp_stack = ["nis2", "dora", "gdpr", "iso 27001", "tisax", "cra"]
            if any(x in text_lower for x in comp_stack):
                score += 25
                feedback_html += """<div style='margin: 10px 0; padding: 15px; background: rgba(0, 255, 148, 0.1); border-left: 3px solid #00FF94; border-radius: 4px;'><strong style='color: #00FF94;'>✅ Regulation</strong><br><span style='color: #ccc; font-size: 14px;'>Compliance keywords found.</span></div>"""
            else:
                feedback_html += """<div style='margin: 10px 0; padding: 15px; background: rgba(255, 59, 48, 0.1); border-left: 3px solid #FF3B30; border-radius: 4px;'><strong style='color: #FF3B30;'>❌ Regulation</strong><br><span style='color: #ccc; font-size: 14px;'>Missing NIS2/DORA keywords.</span></div>"""

            # 3. Tech
            tech_stack = ["burp", "nessus", "splunk", "kubernetes", "docker", "python"]
            if sum(1 for x in tech_stack if x in text_lower) >= 2:
                score += 20
                feedback_html += """<div style='margin: 10px 0; padding: 15px; background: rgba(0, 255, 148, 0.1); border-left: 3px solid #00FF94; border-radius: 4px;'><strong style='color: #00FF94;'>✅ Tech Stack</strong><br><span style='color: #ccc; font-size: 14px;'>Good tool depth.</span></div>"""
            else:
                feedback_html += """<div style='margin: 10px 0; padding: 15px; background: rgba(255, 204, 0, 0.1); border-left: 3px solid #FFCC00; border-radius: 4px;'><strong style='color: #FFCC00;'>⚠️ Tech Stack</strong><br><span style='color: #ccc; font-size: 14px;'>Mention specific tools (Burp, Splunk).</span></div>"""

            # 4. Voice
            if any(x in text_lower for x in ["helped", "assisted", "responsible for"]):
                score -= 10
                feedback_html += """<div style='margin: 10px 0; padding: 15px; background: rgba(255, 204, 0, 0.1); border-left: 3px solid #FFCC00; border-radius: 4px;'><strong style='color: #FFCC00;'>⚠️ Passive Voice</strong><br><span style='color: #ccc; font-size: 14px;'>Use 'Led' or 'Deployed', not 'helped'.</span></div>"""
            else:
                score += 15

            score = max(0, min(100, score))
            
            st.markdown("---")
            c1, c2 = st.columns([1, 2])
            with c1:
                color = "#00FF94" if score > 70 else "#FFCC00" if score > 40 else "#FF3B30"
                st.markdown(f"""<div style="background: rgba(255,255,255,0.05); border: 1px solid {color}; padding: 30px; border-radius: 12px; text-align: center;"><div style="font-size: 60px; font-weight: 800; color: {color};">{score}</div></div>""", unsafe_allow_html=True)
            with c2:
                st.markdown(feedback_html, unsafe_allow_html=True)
            st.link_button("Get Professional Rewrite →", "https://tally.so/r/yourformid", use_container_width=True)

# ==========================================
# TOOL 3: CONTRACT SCANNER (Tab 3 - NEW!)
# ==========================================
with tab3:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div class="glass-card">
        <h3 style="margin-top:0; color:#FF3B30;">⚖️ The 'Widow Maker' Scanner</h3>
        <p>We hunt for the <b>3 clauses</b> that bankrupt freelancers. (Indemnity, Non-Competes, IP Theft)</p>
        <p style="font-size: 12px; color: #666;">*Not legal advice. Educational only.*</p>
    </div>
    """, unsafe_allow_html=True)

    contract_text = st.text_area("Paste Contract Clauses", height=250, label_visibility="collapsed", placeholder="Paste the legal text here...")

    if st.button("Scan for Traps", key="legal_btn", use_container_width=True):
        if not contract_text:
            st.error("Paste text first.")
        else:
            score = 100
            flags = []
            text_lower = contract_text.lower()

            # TRAP 1: INDEMNITY
            if "indemnify" in text_lower or "hold harmless" in text_lower:
                if "cap" not in text_lower and "limit" not in text_lower:
                    score -= 50
                    flags.append("""<div style="border: 1px solid #FF3B30; background: rgba(255, 59, 48, 0.1); padding: 15px; border-radius: 8px; margin-bottom: 10px;"><strong style="color: #FF3B30;">☠️ UNCAPPED INDEMNITY</strong><br><span style="color: #ccc; font-size: 14px;">Dangerous. Demand a 'Liability Cap' equal to 12 months fees.</span></div>""")

            # TRAP 2: NON-COMPETE
            if "non-solicit" in text_lower or "non-compete" in text_lower:
                score -= 30
                flags.append("""<div style="border: 1px solid #FFCC00; background: rgba(255, 204, 0, 0.1); padding: 15px; border-radius: 8px; margin-bottom: 10px;"><strong style="color: #FFCC00;">🔒 NON-COMPETE</strong><br><span style="color: #ccc; font-size: 14px;">Ensure it only applies to direct competitors and lasts < 6 months.</span></div>""")

            # TRAP 3: PAYMENT TERMS
            if "net 60" in text_lower or "paid when paid" in text_lower:
                score -= 20
                flags.append("""<div style="border: 1px solid #FFCC00; background: rgba(255, 204, 0, 0.1); padding: 15px; border-radius: 8px; margin-bottom: 10px;"><strong style="color: #FFCC00;">🚩 BAD PAYMENT TERMS</strong><br><span style="color: #ccc; font-size: 14px;">'Net 60' or 'Paid when Paid' is abusive. Demand Net 14 or Net 30.</span></div>""")

            # RESULT
            color = "#00FF94" if score > 80 else "#FF3B30"
            verdict = "SAFE" if score > 80 else "RISKY"
            
            st.markdown("---")
            c1, c2 = st.columns([1, 2])
            with c1:
                st.markdown(f"""<div style="background: rgba(255,255,255,0.05); border: 1px solid {color}; padding: 20px; border-radius: 12px; text-align: center;"><div style="color: {color}; font-size: 60px; font-weight: 900;">{score}</div><div style="color: #ccc;">{verdict}</div></div>""", unsafe_allow_html=True)
            with c2:
                if flags:
                    for f in flags: st.markdown(f, unsafe_allow_html=True)
                else:
                    st.markdown("""<div style='border: 1px solid #00FF94; background: rgba(0, 255, 148, 0.1); padding: 15px; border-radius: 8px;'><strong style='color: #00FF94;'>✅ No 'Widow Makers' Found</strong></div>""", unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)
            st.link_button("Get 'Safe' Contract Template →", "https://tally.so/r/yourformid", use_container_width=True)

