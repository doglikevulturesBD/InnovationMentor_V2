import streamlit as st
import json
import textwrap

# -------------------------------
# Load Data
# -------------------------------
with open("data/business_models.json", "r") as f:
    BUSINESS_MODELS = json.load(f)

with open("data/archetype_tags.json", "r") as f:
    ARCHETYPE_TAGS = json.load(f)

MATURITY_MAP = {
    "emerging": 0.3,
    "established": 0.6,
    "dominant": 1.0
}

# -------------------------------
# Scoring Function
# -------------------------------
def score_model(model, archetype_tags):
    tag_overlap = len(set(model["tags"]) & set(archetype_tags)) / len(model["tags"])
    maturity_w = MATURITY_MAP[model["maturity_level"]]
    success = model["success_score"]

    final_score = (0.5 * tag_overlap) + (0.3 * success) + (0.2 * maturity_w)
    return final_score


# -------------------------------
# Page Setup + Hero
# -------------------------------
import streamlit as st
import json
import textwrap

st.set_page_config(page_title="Business Model Selector", layout="wide")

# Load CSS
def local_css(name):
    with open(name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("styles.css")

# ---------------- HERO ----------------
hero_html = """
<div class="hero">
<div class="hero-glow"></div>
<div class="hero-content">
<h1 class="hero-title">Business Model Selector</h1>
<p class="hero-sub">Find the best-fit pathways for taking your innovation forward.</p>
</div>
</div>
"""

st.markdown(hero_html, unsafe_allow_html=True)

# -------------------------------
# Session State
# -------------------------------
if "archetype" not in st.session_state:
    st.session_state["archetype"] = None

if "secondary_done" not in st.session_state:
    st.session_state["secondary_done"] = False


# -------------------------------
# STEP 1 — Archetype Selection
# -------------------------------
if st.session_state["archetype"] is None:

    st.markdown("<div class='section-block'>", unsafe_allow_html=True)
    st.markdown("## 1️⃣ Choose Your Innovator Archetype")
    st.caption("Each archetype carries strategic traits used for matching.")

    choice = st.radio("Select your profile:", list(ARCHETYPE_TAGS.keys()))

    if st.button("Continue ➜", use_container_width=True):
        st.session_state["archetype"] = choice
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)


# -------------------------------
# STEP 2 — Secondary Profiling
# -------------------------------
else:
    archetype = st.session_state["archetype"]
    archetype_tags = ARCHETYPE_TAGS[archetype]

    st.success(f"### Selected Archetype: **{archetype}**")

    if not st.session_state["secondary_done"]:

        st.markdown("<div class='section-block'>", unsafe_allow_html=True)
        st.markdown("## 2️⃣ Refine Your Profile")
        st.caption("These factors influence the scoring.")

        q1 = st.selectbox(
            "How fast do you want to commercialize?",
            ["Slow & Research-heavy", "Moderate", "Fast"]
        )

        q2 = st.selectbox(
            "Which is more important to you?",
            ["Recurring revenue", "Impact outcomes", "User scale", "Technology depth"]
        )

        q3 = st.selectbox(
            "Available startup capital?",
            ["Very low (< R50k)", "Medium", "High"]
        )

        if st.button("Generate Recommendations 🚀", use_container_width=True):
            st.session_state.update({
                "secondary_done": True,
                "q1": q1,
                "q2": q2,
                "q3": q3
            })
            st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)


# -------------------------------
# STEP 3 — Recommendations
# -------------------------------
if st.session_state["secondary_done"]:

    # Score models
    results = [(m, score_model(m, archetype_tags)) for m in BUSINESS_MODELS]
    results.sort(key=lambda x: x[1], reverse=True)
    top5 = results[:5]

    st.markdown("<div class='section-block'>", unsafe_allow_html=True)
    st.markdown("## 🔥 Top 5 Recommended Business Models")

   for bm, score in top5:
    overlap = len(set(bm["tags"]) & set(archetype_tags))

    tile = f"""
    <div class="bm-tile">
    <h3>{bm['name']}</h3>
    <p><b>Score:</b> {score:.2f}</p>
    <p>{bm['description']}</p>
    <p><b>Tag Fit:</b> {overlap} aligned traits</p>
    <p><b>Success Rate:</b> {int(bm['success_score']*100)}%</p>
    <p><b>Maturity:</b> {bm['maturity_level'].title()}</p>
    </div>
    """

    st.markdown(tile, unsafe_allow_html=True)


    # Expand full list
    with st.expander("📚 See all 70 business models"):
        for bm in BUSINESS_MODELS:
            st.markdown(f"### {bm['name']}")
            st.write(bm["description"])
            st.caption(f"Tags: {', '.join(bm['tags'])}")

    st.divider()
    if st.button("🔄 Start Over", use_container_width=True):
        st.session_state.clear()
        st.rerun()

