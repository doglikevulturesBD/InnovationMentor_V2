# ============================================
# INNOVATION MENTOR APP
# PAGE: 06_Commercialisation_Strategy.py
# ============================================

import streamlit as st
import json
from pathlib import Path
from collections import defaultdict

# ------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------
st.set_page_config(
    page_title="Commercialisation & Marketing Strategy",
    page_icon="🚀",
    layout="wide"
)

# ------------------------------------------------------
# LOAD GLOBAL CSS (same as TRL, Market, Financial pages)
# ------------------------------------------------------
def local_css(file_name: str):
    with open(file_name, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("styles.css")


# ------------------------------------------------------
# HERO BANNER (Unified Innovation Mentor theme)
# ------------------------------------------------------
hero_html = """
<div class="hero sub-hero">
<div class="hero-glow"></div>
<div class="hero-particles"></div>

<div class="hero-content">
<h1 class="hero-title">Commercialisation Strategy</h1>
<p class="hero-sub">Discover the most effective pathway and marketing system to take your innovation to market.</p>
</div>
</div>
"""
st.markdown(hero_html, unsafe_allow_html=True)


# ------------------------------------------------------
# SECTION WRAPPER OPEN
# ------------------------------------------------------
st.markdown("<div class='section-block'>", unsafe_allow_html=True)




# ------------------------------------------------------
# LOAD QUESTIONNAIRE
# ------------------------------------------------------
data_path = Path("data/commercialisation_questionnaire.json")

if not data_path.exists():
    st.error("❌ Missing file: `commercialisation_questionnaire.json` in `/data` folder.")
    st.stop()

with open(data_path, "r", encoding="utf-8") as f:
    questions = json.load(f)["questions"]

# ------------------------------------------------------
# INITIALISE SCORING
# ------------------------------------------------------
commercialisation_scores = defaultdict(int)
marketing_scores = defaultdict(int)


# ------------------------------------------------------
# QUESTIONNAIRE SECTION
# ------------------------------------------------------
st.subheader("📝 Questionnaire")

for i, q in enumerate(questions, start=1):
    st.markdown(f"**{i}. {q['question']}**")
    options = [opt["text"] for opt in q["options"]]

    answer = st.radio(
        label="",
        options=options,
        key=f"q{q['id']}",
        horizontal=False
    )
    st.write("")  # spacing

    # Apply scoring
    for opt in q["options"]:
        if opt["text"] == answer:
            for c_item in opt["adds"]["commercialisation"]:
                commercialisation_scores[c_item] += 1
            for m_item in opt["adds"]["marketing"]:
                marketing_scores[m_item] += 1

    st.divider()


# ------------------------------------------------------
# GENERATE STRATEGY OUTPUT
# ------------------------------------------------------
if st.button("🔍 Generate My Strategy Mix", use_container_width=True):
    st.markdown("---")
    st.subheader("📊 Your Strategy Mix")

    # Sort results
    sorted_c = sorted(commercialisation_scores.items(), key=lambda x: x[1], reverse=True)
    sorted_m = sorted(marketing_scores.items(), key=lambda x: x[1], reverse=True)

    if not sorted_c:
        st.warning("No commercialisation signals detected — complete the questionnaire first.")
        st.stop()

    top_pathway = sorted_c[0][0]
    top3_marketing = [m for m, s in sorted_m[:3]]

    # --------------------------------------------------
    # MAIN RECOMMENDATIONS
    # --------------------------------------------------
    st.success(f"**Recommended Commercialisation Pathway:** {top_pathway}")
    st.info(f"**Top 3 Marketing Strategies:** {', '.join(top3_marketing)}")

    st.markdown("---")
    st.subheader("🧩 Detailed Strategy Breakdown")

    # Load rationale
    rationale_path = Path("data/commercialisation_rationale.json")
    rationale_data = {}

    if rationale_path.exists():
        with open(rationale_path, "r", encoding="utf-8") as f:
            rationale_data = json.load(f)

    # Commercialisation detail
    if top_pathway in rationale_data:
        block = rationale_data[top_pathway]

        with st.expander(f"🚀 {top_pathway} – Commercialisation Detail"):
            st.markdown(f"**Description:** {block['description']}")
            st.markdown("**Next Steps:**")
            for step in block["next_steps"]:
                st.markdown(f"- {step}")
            st.markdown(f"**Cost / Complexity:** {block['cost']}")

    # Marketing detail
    for m in top3_marketing:
        if m in rationale_data:
            blk = rationale_data[m]
            with st.expander(f"🎯 {m} – Marketing Strategy Detail"):
                st.markdown(f"**Description:** {blk['description']}")
                st.markdown("**Tactics:**")
                for t in blk["tactics"]:
                    st.markdown(f"- {t}")
                st.markdown(f"**Innovation Fit:** {blk['innovation']}")



# ------------------------------------------------------
# SECTION WRAPPER CLOSE
# ------------------------------------------------------
st.markdown("</div>", unsafe_allow_html=True)
