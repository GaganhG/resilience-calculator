import streamlit as st
import re

# 1. PAGE CONFIGURATION (Consistent Cyber Vibe)
st.set_page_config(page_title="CISO Resume Roaster", page_icon="📝")

# Custom CSS (Matches your Main Page)
st.markdown("""
    <style>
    .stApp {background-color: #0E1117; color: #00FF41; font-family: 'Courier New', monospace;}
    .stTextArea textarea {background-color: #1c2229; color: white; border: 1px solid #00FF41;}
    h1, h2, h3 {color: #00FF41 !important;}
    .stButton>button {background-color: #00FF41; color: black; font-weight: bold; border: none;}
    </style>
    """, unsafe_allow_html=True)

st.title("📝 The Profile Polisher")
st.markdown("**Does your CV speak 'Engineer' or 'Consultant'?**")
st.info("Paste your LinkedIn 'About' section or CV bullet points below. We'll tell you if a CISO will hire you.")

# 2. INPUT AREA
text_input = st.text_area("Paste Text Here:", height=200, placeholder="e.g., 'Responsible for network security and firewall configuration...'")

# 3. ANALYSIS LOGIC
def analyze_text(text):
    score = 0
    feedback = []
    
    # Check 1: Money/Impact Words
    money_pattern = r"(\$|€|%|budget|revenue|saved|reduced|cut|increased|ROI|millions)"
    money_matches = re.findall(money_pattern, text, re.IGNORECASE)
    if money_matches:
        score += 25
        feedback.append(f"✅ **Business Impact:** Excellent. You mentioned financial impact {len(money_matches)} times.")
    else:
        feedback.append("❌ **Business Impact:** Missing. CISOs buy 'Risk Reduction' and 'ROI'. Add € or %.")

    # Check 2: Regulatory Keywords (NIS2/DORA)
    comp_keywords = ["nis2", "dora", "iso27001", "gdpr", "audit", "compliance", "governance", "risk", "framework", "cra"]
    found_comp = [word for word in comp_keywords if word in text.lower()]
    if found_comp:
        score += 35
        feedback.append(f"✅ **Regulatory Relevance:** Strong. Found: {', '.join(found_comp)}.")
    else:
        feedback.append("❌ **Regulatory Relevance:** No compliance keywords found. You won't pass the NIS2 screen.")

    # Check 3: Power Verbs
    power_verbs = ["led", "orchestrated", "designed", "architected", "mitigated", "secured", "deployed", "managed"]
    found_verbs = [word for word in power_verbs if word in text.lower()]
    if len(found_verbs) > 1:
        score += 20
        feedback.append("✅ **Leadership:** You use strong action verbs.")
    else:
        feedback.append("⚠️ **Leadership:** You sound passive. Swap 'Helped' with 'Orchestrated'.")

    # Check 4: Conciseness
    word_count = len(text.split())
    if 20 < word_count < 300:
        score += 20
    elif word_count < 20:
        feedback.append("⚠️ **Length:** Too short to analyze.")
    else:
        feedback.append("⚠️ **Length:** Too long. Be concise.")

    return score, feedback

# 4. RESULTS DISPLAY
if st.button("ROAST MY PROFILE"):
    if not text_input:
        st.error("Please paste some text first.")
    else:
        final_score, feedback_list = analyze_text(text_input)
        if final_score > 100: final_score = 100
        
        st.markdown("---")
        col1, col2 = st.columns([1,2])
        
        with col1:
            st.metric(label="HIRABILITY SCORE", value=f"{final_score}/100")
            if final_score > 75:
                st.success("VERDICT: SENIOR")
            elif final_score > 40:
                st.warning("VERDICT: MID-LEVEL")
            else:
                st.error("VERDICT: TECHIE")
        
        with col2:
            st.write("### 🤖 Feedback:")
            for item in feedback_list:
                st.write(item)

        st.markdown("---")
        st.write("### 🚀 Want to get hired?")
        st.write("Join the bench. We rewrite your profile for you.")
        # REPLACE WITH YOUR TALLY LINK
        st.link_button("JOIN BENCH NOW", "https://tally.so/r/YOUR_ID")
