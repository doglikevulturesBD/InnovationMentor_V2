# ============================================================
# INNOVATION MENTOR APP
# PAGE: 07_IP_Management.py
# ============================================================

import streamlit as st
import json
from pathlib import Path

# ------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------
st.set_page_config(
    page_title="IP Management",
    page_icon="🔐",
    layout="wide"
)

# ------------------------------------------------------
# LOAD GLOBAL CSS (same as all other modules)
# ------------------------------------------------------
def local_css(file_name: str):
    with open(file_name, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("styles.css")


# ------------------------------------------------------
# HERO BANNER (Unified Innovation Mentor style)
# ------------------------------------------------------
hero_html = """
<div class="hero sub-hero">
<div class="hero-glow"></div>
<div class="hero-particles"></div>

<div class="hero-content">
<h1 class="hero-title">Intellectual Property Management</h1>
<p class="hero-sub">Determine the best IP protection pathway for your innovation.</p>
</div>
</div>
"""
st.markdown(hero_html, unsafe_allow_html=True)


# ------------------------------------------------------
# OPEN SECTION WRAPPER
# ------------------------------------------------------
st.markdown("<div class='section-block'>", unsafe_allow_html=True)

st.caption("A guided tool to help innovators determine the best IP protection strategy.")

st.markdown("""
This module evaluates the nature of your innovation and recommends the most suitable form  
of **intellectual property protection** — including patents, designs, trademarks, and more.
""")

st.markdown("---")


# ------------------------------------------------------
# LOAD QUESTIONNAIRE JSON
# ------------------------------------------------------
q_path = Path("data/ip_questionnaire.json")
if not q_path.exists():
    st.error("❌ Missing file: `ip_questionnaire.json` in /data")
    st.stop()

try:
    with open(q_path, "r", encoding="utf-8") as f:
        questions = json.load(f)["questions"]
except Exception as e:
    st.error(f"❌ Error loading ip_questionnaire.json: {e}")
    st.stop()


# ------------------------------------------------------
# LOAD RATIONALE JSON
# ------------------------------------------------------
r_path = Path("data/ip_rationale.json")
if not r_path.exists():
    st.error("❌ Missing file: `ip_rationale.json` in /data")
    st.stop()

try:
    with open(r_path, "r", encoding="utf-8") as f:
        rationale_data = json.load(f)
except Exception as e:
    st.error(f"❌ Error loading ip_rationale.json: {e}")
    st.stop()


# ------------------------------------------------------
# RENDER QUESTIONNAIRE
# ------------------------------------------------------
st.header("📋 IP Questionnaire")

for q in questions:
    st.radio(
        q["question"],
        list(q["options"].keys()),
        key=q["id"]
    )


# ------------------------------------------------------
# SCORING ENGINE
# ------------------------------------------------------
ip_types = ["Patent", "Design", "Trademark", "Copyright", "Trade Secret"]
ip_scores = {ip: 0 for ip in ip_types}

for q in questions:
    user_choice = st.session_state.get(q["id"])
    if user_choice:
        weight_map = q["options"][user_choice]  # dict: ip → score
        for ip_type, score in weight_map.items():
            ip_scores[ip_type] += score

sorted_scores = sorted(ip_scores.items(), key=lambda x: x[1], reverse=True)


# ------------------------------------------------------
# RESULTS DISPLAY
# ------------------------------------------------------
st.markdown("---")
if st.button("🔍 Show My IP Recommendation", use_container_width=True):

    primary_ip, primary_score = sorted_scores[0]
    secondary_ip, secondary_score = sorted_scores[1]

    # ----------------------------
    # MAIN RESULTS
    # ----------------------------
    st.success(f"🏆 Primary Recommendation: **{primary_ip}** (score {primary_score})")
    st.info(f"✨ Secondary Consideration: **{secondary_ip}** (score {secondary_score})")

    st.markdown("---")

    # ----------------------------
    # DETAILS FOR PRIMARY IP TYPE
    # ----------------------------
    ip_info = rationale_data.get(primary_ip, {})

    st.write("### 📘 Description")
    st.write(ip_info.get("description", "No description available."))

    st.write("### 🧭 Recommended Next Steps")
    for step in ip_info.get("next_steps", []):
        st.write(f"- {step}")

    st.write("### 💰 Approximate Cost")
    st.write(ip_info.get("approx_cost", "No cost information available."))

    st.markdown("---")

    # ----------------------------
    # RISK WARNINGS
    # ----------------------------
    st.write("### ⚠️ Key Risks & Limitations")

    risk_map = {
        "Patent": [
            "Public disclosure before filing destroys novelty.",
            "International filings become expensive quickly.",
            "Maintenance fees required to keep protection active."
        ],
        "Design": [
            "Protects appearance, not function.",
            "Disclosure before filing destroys novelty."
        ],
        "Trademark": [
            "Descriptive or generic names cannot be registered.",
            "Prior conflicting trademarks may block approval."
        ],
        "Copyright": [
            "Protects only expression, not ideas or algorithms.",
            "Does not protect underlying concepts or logic."
        ],
        "Trade Secret": [
            "Protection ends if secrecy is lost.",
            "Must implement strict internal confidentiality processes."
        ]
    }

    for risk in risk_map.get(primary_ip, []):
        st.write(f"- {risk}")

    st.markdown("---")

    # ----------------------------
    # DISCLAIMER
    # ----------------------------
    st.info(
        "This tool provides early-stage guidance only. For formal legal advice, "
        "consult a registered IP attorney or IP specialist."
    )


# ------------------------------------------------------
# CLOSE SECTION WRAPPER
# ------------------------------------------------------
st.markdown("</div>", unsafe_allow_html=True)
