import streamlit as st
import textwrap

# -------------------------------------
# PAGE CONFIG
# -------------------------------------
st.set_page_config(
    page_title="Innovation Mentor",
    page_icon="💡",
    layout="wide"
)

# -------------------------------------
# LOAD CSS FROM FILE
# -------------------------------------
def local_css(file_name: str):
    with open(file_name, "r") as f:
        css = f"<style>{f.read()}</style>"
        st.markdown(css, unsafe_allow_html=True)

# styles.css must be in the same folder as this file
local_css("styles.css")

# -------------------------------------
# HERO BANNER
# -------------------------------------
hero_html = textwrap.dedent("""
<div class="hero">
<div class="hero-glow"></div>
<div class="hero-particles"></div>

<div class="hero-content">
<h1 class="hero-title">Innovation Mentor</h1>
<p class="hero-sub">A future-ready space for innovators, startups, and portfolio managers.</p>
</div>
</div>
""")

st.markdown(hero_html, unsafe_allow_html=True)

# -------------------------------------
# FEATURE TILES
# -------------------------------------
tiles_html = textwrap.dedent("""
<div class="tile-container">
<div class="glow-tile">{trl}</div>
<div class="glow-tile">{models}</div>
<div class="glow-tile">{finance}</div>
<div class="glow-tile">{marketing}</div>
<div class="glow-tile">{risk}</div>
<div class="glow-tile">{export}</div>
</div>
"""

tiles_html = tiles_html.format(
    trl=st.page_link("pages/01_TRL_Assessment.py", label="TRL Assessment", icon="🔬"),
    models=st.page_link("pages/02_Business_Models.py", label="Business Models", icon="📦"),
    finance=st.page_link("pages/03_Finance_Tools.py", label="Financial Tools", icon="💸"),
    marketing=st.page_link("pages/04_Marketing_Strategy.py", label="Marketing Strategy", icon="📢"),
    risk=st.page_link("pages/05_Risk_Dashboard.py", label="Risk Dashboard", icon="⚠️"),
    export=st.page_link("pages/06_Export_Tools.py", label="Export Tools", icon="📤"),
)

st.markdown(tiles_html, unsafe_allow_html=True)

# -------------------------------------
# ABOUT SECTION
# -------------------------------------
about_html = textwrap.dedent("""
<div class="section-block">
    <h2 class="section-title">About the Platform</h2>
    <p class="section-text">
        The Innovation Mentor Platform supports innovators, entrepreneurs, researchers,
        and portfolio managers with structured thinking tools. It focuses on clarity in TRL,
        business models, early-stage financial thinking, commercialisation logic and risk framing.
    </p>
</div>
""")
st.markdown(about_html, unsafe_allow_html=True)

# -------------------------------------
# MVP SECTION
# -------------------------------------
mvp_html = textwrap.dedent("""
<div class="section-block">
    <h2 class="section-title">MVP Status</h2>
    <p class="section-text">
        This is an MVP (Minimum Viable Product). Logic, scoring and guidance will evolve as
        real-world usage, feedback and validation data are collected.
    </p>
</div>
""")
st.markdown(mvp_html, unsafe_allow_html=True)

# -------------------------------------
# FOOTER
# -------------------------------------
footer_html = textwrap.dedent("""
<div class="footer">
    <p>© 2025 Innovation Mentor</p>
</div>
""")
st.markdown(footer_html, unsafe_allow_html=True)
