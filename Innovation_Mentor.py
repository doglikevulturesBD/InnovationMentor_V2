import streamlit as st
import textwrap
from streamlit_extras.switch_page_button import switch_page
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

# ---- HOLOGRAM TILES WITH FULL-PAGE NAVIGATION ----

cols = st.columns(3)

with cols[0]:
    if st.button("🔬  TRL Calculator", key="tile_trl"):
        switch_page("TRL_Calculator")

with cols[1]:
    if st.button("📦  Business Models", key="tile_bm"):
        switch_page("Business_Model_Selector")

with cols[2]:
    if st.button("💸  Financial Projection", key="tile_fin"):
        switch_page("Financial_Projection")

cols = st.columns(3)

with cols[0]:
    if st.button("📢  Marketing Strategy", key="tile_market"):
        switch_page("Market_Study_Guide")

with cols[1]:
    if st.button("🚀  Commercialisation Strategy", key="tile_comm"):
        switch_page("Commercialisation_Strategy")

with cols[2]:
    if st.button("💡  IP Management", key="tile_ip"):
        switch_page("IP_Management")

cols = st.columns(3)

with cols[0]:
    if st.button("⚠️  Risk Dashboard", key="tile_risk"):
        switch_page("Risk_Dashboard")

with cols[1]:
    if st.button("🔧  Financial Options", key="tile_opt"):
        switch_page("Financial_Options")

with cols[2]:
    if st.button("📜  Legal & Compliance", key="tile_legal"):
        switch_page("Legal_and_Compliance")

cols = st.columns(3)

with cols[0]:
    if st.button("💬  Feedback", key="tile_fb"):
        switch_page("Feedback")

with cols[1]:
    if st.button("📤  Export Tools", key="tile_export"):
        switch_page("Export_Report")



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
