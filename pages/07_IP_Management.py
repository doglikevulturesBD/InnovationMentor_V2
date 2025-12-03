# ============================================================
# INNOVATION MENTOR APP — IP MANAGEMENT (TILE EDITION)
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
# GLOBAL CSS
# ------------------------------------------------------
def local_css(file_name: str):
    with open(file_name, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("styles.css")


# ------------------------------------------------------
# HERO SECTION
# ------------------------------------------------------
hero_html = """
<div class="hero sub-hero">
<div class="hero-glow"></div>
<div class="hero-particles"></div>

<div class="hero-content">
<h1 class="hero-title">Intellectual Property Management</h1>
<p class="hero-sub">Suggests a basic IP management strategy</p>
</div>
</div>
"""
st.markdown(hero_html, unsafe_allow_html=True)


# ------------------------------------------------------
# SECTION WRAPPER
# ------------------------------------------------------
st.markdown("<div class='section-block'>", unsafe_allow_html=True)



# ------------------------------------------------------
# LOAD QUESTIONNAIRE
# ------------------------------------------------------
q_path = Path("data/ip_questionnaire.json")
if not q_path.exists():
    st.error("❌ Missing file: ip_questionnaire.json")
    st.stop()

with open(q_path, "r", encoding="utf-8") as f:
    questions = json.load(f)["questions"]


# ------------------------------------------------------
# LOAD RATIONALE
# ------------------------------------------------------
r_path = Path("data/ip_rationale.json")
if not r_path.exists():
    st.error("❌ Missing file: ip_rationale.json")
    st.stop()

with open(r_path, "r", encoding="utf-8") as f:
    rationale_data = json.load(f)


# ------------------------------------------------------
# QUESTIONNAIRE
# ------------------------------------------------------
st.header("IP Questionnaire")

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
scores = {ip: 0 for ip in ip_types}

for q in questions:
    answer = st.session_state.get(q["id"])
    if answer:
        for ip_type, val in q["options"][answer].items():
            scores[ip_type] += val

sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)


# ------------------------------------------------------
# RESULTS SECTION
# ------------------------------------------------------
st.markdown("---")
if st.button("Show My IP Recommendation", use_container_width=True):

    primary_ip, p_score = sorted_scores[0]
    secondary_ip, s_score = sorted_scores[1]

    # ------------------------------
    # TILE: PRIMARY RECOMMENDATION
    # ------------------------------
    st.markdown(f"""
    <div class="im-tile">
        <h3>Primary Recommendation</h3>
        <h2 style="margin-top:-5px;">{primary_ip}</h2>
        <p><b>Score:</b> {p_score}</p>
    </div>
    """, unsafe_allow_html=True)

    # ------------------------------
    # TILE: SECONDARY RECOMMENDATION
    # ------------------------------
    st.markdown(f"""
    <div class="im-tile">
        <h3>Secondary Consideration</h3>
        <h3 style="margin-top:-5px;">{secondary_ip}</h3>
        <p><b>Score:</b> {s_score}</p>
    </div>
    """, unsafe_allow_html=True)


    # LOAD PRIMARY DETAILS
    info = rationale_data.get(primary_ip, {})

    # ------------------------------
    # TILE: DESCRIPTION
    # ------------------------------
    st.markdown(f"""
    <div class="im-tile">
        <h3>Description</h3>
        <p>{info.get('description', 'No description available.')}</p>
    </div>
    """, unsafe_allow_html=True)


    # ------------------------------
    # TILE: NEXT STEPS
    # ------------------------------
    steps_html = "<ul>" + "".join([f"<li>{step}</li>" for step in info.get("next_steps", [])]) + "</ul>"

    st.markdown(f"""
    <div class="im-tile">
        <h3>Recommended Next Steps</h3>
        {steps_html}
    </div>
    """, unsafe_allow_html=True)


    # ------------------------------
    # TILE: COST
    # ------------------------------
    st.markdown(f"""
    <div class="im-tile">
        <h3>Estimated Cost</h3>
        <p>{info.get('approx_cost', 'Cost information not available.')}</p>
    </div>
    """, unsafe_allow_html=True)


    # ------------------------------
    # TILE: RISKS
    # ------------------------------
    risk_map = {
        "Patent": [
            "Public disclosure before filing destroys novelty.",
            "International filings are expensive.",
            "Requires maintenance fees to stay active."
        ],
        "Design": [
            "Protects appearance only, not function.",
            "Disclosure before filing removes eligibility."
        ],
        "Trademark": [
            "Generic/descriptive names cannot be registered.",
            "Existing marks can block your application."
        ],
        "Copyright": [
            "Protects expression, not ideas or algorithms.",
            "Does not protect underlying concepts."
        ],
        "Trade Secret": [
            "Protection ends if secrecy is lost.",
            "Requires strong internal confidentiality systems."
        ]
    }

    risk_html = "<ul>" + "".join([f"<li>{r}</li>" for r in risk_map.get(primary_ip, [])]) + "</ul>"

    st.markdown(f"""
    <div class="im-tile">
        <h3>Risks & Limitations</h3>
        {risk_html}
    </div>
    """, unsafe_allow_html=True)


    # ------------------------------
    # TILE: DISCLAIMER
    # ------------------------------
    st.markdown("""
    <div class="im-tile">
        <h3> Disclaimer</h3>
        <p>This tool provides early-stage guidance only.  
        For formal legal advice, consult a <b>registered IP attorney</b> or specialist.</p>
    </div>
    """, unsafe_allow_html=True)


# ------------------------------------------------------
# CLOSE SECTION WRAPPER
# ------------------------------------------------------
st.markdown("</div>", unsafe_allow_html=True)
