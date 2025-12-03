# ============================================
# INNOVATION MENTOR APP
# PAGE: Financing Options
# FUNCTION: Stage-Based Funding Guidance (Tile Edition)
# ============================================

import streamlit as st

# ----------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------
st.set_page_config(
    page_title="Financing Options",
    page_icon="💰",
    layout="wide"
)

# ----------------------------------------------------
# LOAD GLOBAL CSS
# ----------------------------------------------------
def local_css(file_name: str):
    with open(file_name, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("styles.css")

# ----------------------------------------------------
# HERO BANNER
# ----------------------------------------------------
hero_html = """
<div class="hero sub-hero">
<div class="hero-glow"></div>
<div class="hero-particles"></div>

<div class="hero-content">
<h1 class="hero-title">Financing Options</h1>
<p class="hero-sub">Identify funding pathways aligned to your innovation's maturity and capital needs.</p>
</div>
</div>
"""
st.markdown(hero_html, unsafe_allow_html=True)

# ----------------------------------------------------
# SECTION WRAPPER
# ----------------------------------------------------
st.markdown("<div class='section-block'>", unsafe_allow_html=True)

st.caption("This guide gives stage-aligned funding options — not formal financial advice.")



st.markdown("---")

# ----------------------------------------------------
# STAGE SELECTOR (inside tile)
# ----------------------------------------------------
st.markdown("<div class='im-tile'>", unsafe_allow_html=True)

stage = st.selectbox(
    "Select your current stage:",
    ["Ideation", "Prototype / TRL 3–5", "Pilot / TRL 6–7",
     "Commercialisation / TRL 8–9", "Scaling / Growth"]
)

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")

# ----------------------------------------------------
# FINANCING RECOMMENDATIONS (tile)
# ----------------------------------------------------
st.subheader("Recommended Financing Options")

recommendations = {
    "Ideation": [
        "Small / micro grants",
        "Research grants or innovation challenges",
        "University / government pre-seed support",
        "Founder-funded (low burn)",
    ],
    "Prototype / TRL 3–5": [
        "Proof-of-concept (PoC) grants",
        "Conditional grants tied to milestones",
        "Early blended finance (grant + loan or soft equity)",
        "Incubator / accelerator micro-funding",
    ],
    "Pilot / TRL 6–7": [
        "Pilot demonstration grants",
        "Concessional loans",
        "Sector-focused venture capital",
        "Corporate partnerships / co-development funding",
    ],
    "Commercialisation / TRL 8–9": [
        "Revenue-based finance",
        "Convertible notes / early equity",
        "Project finance (if infrastructure-linked)",
        "Commercial venture funds",
    ],
    "Scaling / Growth": [
        "Private equity / strategic investors",
        "Development finance institutions (DFIs)",
        "Blended finance structures",
        "Long-term concessionary loans (infrastructure)",
    ],
}

# Build tile content
items_html = "<ul>" + "".join([f"<li>{i}</li>" for i in recommendations[stage]]) + "</ul>"

st.markdown(f"""
<div class="im-tile">
    <h3>📌 Stage: {stage}</h3>
    <h4>Relevant Financing Options</h4>
    {items_html}
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ----------------------------------------------------
# REFLECTION TILE
# ----------------------------------------------------
st.markdown("""
<div class='im-tile'>
    <h3>Reflection</h3>
    <p>How does this influence your funding and capital strategy?</p>
</div>
""", unsafe_allow_html=True)

reflection = st.text_area(
    "",
    height=150,
    key="finance_reflection"
)

# ----------------------------------------------------
# CLOSE SECTION WRAPPER
# ----------------------------------------------------
st.markdown("</div>", unsafe_allow_html=True)
