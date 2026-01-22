import streamlit as st
import re

# 1. PAGE CONFIGURATION (Wide Layout, Professional Title)
st.set_page_config(
    page_title="EU Resilience Bench",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. UI/UX OVERHAUL (The "Stripe-Like" Clean Theme)
st.markdown("""
    <style>
    /* IMPORT INTER FONT (Standard for modern UI) */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

    /* GLOBAL RESET */
    .stApp {
        background-color: #F9FAFB; /* Very light grey for contrast */
        font-family: 'Inter', sans-serif;
        color: #1F2937; /* Slate 800 - Softer than black */
    }

    /* REMOVE STREAMLIT PADDING */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }

    /* HEADERS - Clean & Professional */
    h1, h2, h3 {
        color: #111827 !important; /* Almost Black */
        font-weight: 700 !important;
        letter-spacing: -0.02em;
    }
    
    /* SUBHEADERS */
    p {
        font-size: 16px;
        color: #4B5563; /* Slate 600 */
        line-height: 1.6;
    }

    /* CARDS (The "White Box" Effect) */
    div[data-testid="stVerticalBlock"] > div {
        border-radius: 12px;
    }

    /* INPUT FIELDS - Minimalist Borders */
    .stSelectbox div[data-baseweb="select"], 
    .stMultiSelect div[data-baseweb="select"],
    .stTextArea textarea {
        background-color: #FFFFFF;
        border: 1px solid #E5E7EB; /* Light Grey */
        border-radius: 8px;
        color: #1F2937;
        box-shadow: 0 1px 2px rgba(0,0,0,0.05);
    }
    
    /* SLIDERS - Professional Blue */
    div[data-baseweb="slider"] div {
        background-color: #2563EB !important;
    }

    /* TABS - The "Segmented Control" Look */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: transparent;
        border-bottom: 2px solid #E5E7EB;
        padding-bottom: 0px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: transparent;
        border: none;
        color: #6B7280;
        font-weight: 600;
        padding: 10px 20px;
    }
    .stTabs [aria-selected="true"] {
        color: #2563EB !important; /* Tech Blue */
        border-bottom: 2px solid #2563EB;
        background-color: transparent;
    }

    /* BUTTONS - Solid & Trustworthy */
    .stButton>button {
        background-color: #111827; /* Dark Slate */
        color: #FFFFFF;
        border: none;
        border-radius: 8px;
        font-weight: 600;
        padding: 12px 24px;
        transition: all 0.2s;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    .stButton>button:hover {
        background-color: #000000;
        transform: translateY(-1px);
        box-shadow: 0 6px 8px -1px rgba(0, 0, 0, 0.1);
        color: #FFFFFF;
    }

    /* ALERTS / CARDS - Clean Status */
    div[data-testid="stMarkdownContainer"] p {
        font-size: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. HEADER SECTION
col1, col2 = st.columns([2, 1])
with col1:
    st.title("EU Resilience Bench")
    st.markdown("Assess your market value and compliance readiness for NIS2 & DORA projects.")

# --- TABS ---
tab1, tab2 = st.tabs(["Rate Calculator", "CV Optimizer"])

# ==========================================
# TOOL 1: RATE CALCULATOR (Clean Form)
# ==========================================
with tab1:
    st.markdown("<br>", unsafe_allow_html=True)
    
    # CARD CONTAINER
    with st.container():
        st.markdown("""
        <div style="background-color: white; padding: 25px; border-radius: 12px; border: 1px solid #E5E7EB; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);">
            <h3 style="margin-top:0;">💰 Market Rate Assessment</h3>
        </div>
        <br>
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
            # Logic...
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

            # RESULT CARD
            st.markdown(f"""
            <div style="background-color: #F0FDF4; border: 1px solid #BBF7D0; padding: 20px; border-radius: 10px; text-align: center; margin-top: 20px;">
                <p style="color: #166534; font-weight: 600; margin: 0; font-size: 14px; text-transform: uppercase;">Estimated Daily Rate</p>
                <h1 style="color: #15803D; font-size: 42px; margin: 10px 0;">€{low} - €{high}</h1>
                <p style="color: #166534; font-size: 14px;">Based on current demand in {location}</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            st.link_button("Apply to Join Bench →", "https://tally.so/r/yourformid", use_container_width=True)

# ==========================================
# TOOL 2: CV OPTIMIZER (Minimalist Reports)
# ==========================================
with tab2:
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background-color: white; padding: 25px; border-radius: 12px; border: 1px solid #E5E7EB; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);">
        <h3 style="margin-top:0;">📝 Profile Screening</h3>
        <p style="color: #6B7280; font-size: 14px; margin-bottom: 0;">Paste your CV bullet points to check for CISO keywords.</p>
    </div>
    <br>
    """, unsafe_allow_html=True)

    text_input = st.text_area("Paste CV Text", height=200, label_visibility="collapsed", placeholder="Paste your experience bullets here...")

    if st.button("Analyze Profile", key="cv_btn", use_container_width=True):
        if not text_input:
            st.error("Please enter some text to analyze.")
        else:
            score = 0
            feedback_html = ""
            text_lower = text_input.lower()
            
            # --- LOGIC ---
            # 1. Impact
            if re.search(r"(\d+(?:%|k|m|bn)|€\$?\d+)", text_lower):
                score += 25
                feedback_html += """<div style='margin-bottom: 10px; padding: 12px; background: #F0FDF4; border-left: 4px solid #16A34A; color: #166534; font-size: 14px;'><b>✅ Business Impact:</b> Detected quantified metrics.</div>"""
            else:
                feedback_html += """<div style='margin-bottom: 10px; padding: 12px; background: #FEF2F2; border-left: 4px solid #DC2626; color: #991B1B; font-size: 14px;'><b>❌ Business Impact:</b> No numbers found. Add ROI metrics (€, %).</div>"""

            # 2. Compliance
            comp_stack = ["nis2", "dora", "gdpr", "iso 27001", "tisax", "cra"]
            if any(x in text_lower for x in comp_stack):
                score += 25
                feedback_html += """<div style='margin-bottom: 10px; padding: 12px; background: #F0FDF4; border-left: 4px solid #16A34A; color: #166534; font-size: 14px;'><b>✅ Compliance:</b> Found regulatory keywords.</div>"""
            else:
                feedback_html += """<div style='margin-bottom: 10px; padding: 12px; background: #FEF2F2; border-left: 4px solid #DC2626; color: #991B1B; font-size: 14px;'><b>❌ Compliance:</b> Missing critical frameworks (NIS2/DORA).</div>"""

            # 3. Tech
            tech_stack = ["burp", "nessus", "splunk", "kubernetes", "docker", "python"]
            if sum(1 for x in tech_stack if x in text_lower) >= 2:
                score += 20
                feedback_html += """<div style='margin-bottom: 10px; padding: 12px; background: #F0FDF4; border-left: 4px solid #16A34A; color: #166534; font-size: 14px;'><b>✅ Tech Stack:</b> Good technical depth detected.</div>"""
            else:
                feedback_html += """<div style='margin-bottom: 10px; padding: 12px; background: #FFFBEB; border-left: 4px solid #D97706; color: #92400E; font-size: 14px;'><b>⚠️ Tech Stack:</b> Light on specific tools.</div>"""

            # 4. Voice
            if any(x in text_lower for x in ["helped", "assisted", "responsible for"]):
                score -= 10
                feedback_html += """<div style='margin-bottom: 10px; padding: 12px; background: #FFFBEB; border-left: 4px solid #D97706; color: #92400E; font-size: 14px;'><b>⚠️ Passive Voice:</b> Avoid 'helped' or 'assisted'. Use 'Led' or 'Deployed'.</div>"""
            else:
                score += 15

            # Length
            if 30 <= len(text_input.split()) <= 400: score += 15
            
            score = max(0, min(100, score))

            # RESULT DISPLAY
            st.markdown("---")
            c1, c2 = st.columns([1, 2])
            
            with c1:
                color = "#16A34A" if score > 70 else "#D97706" if score > 40 else "#DC2626"
                bg_color = "#F0FDF4" if score > 70 else "#FFFBEB" if score > 40 else "#FEF2F2"
                st.markdown(f"""
                <div style="background-color: {bg_color}; padding: 20px; border-radius: 12px; text-align: center; border: 1px solid {color};">
                    <div style="font-size: 12px; text-transform: uppercase; color: {color}; font-weight: bold; margin-bottom: 5px;">Hirability Score</div>
                    <div style="font-size: 48px; font-weight: 800; color: {color}; line-height: 1;">{score}</div>
                </div>
                """, unsafe_allow_html=True)
            
            with c2:
                st.markdown(feedback_html, unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            st.link_button("Get Professional Rewrite →", "https://tally.so/r/yourformid", use_container_width=True)

