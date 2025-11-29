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

<div class="holo-container">
<a class="holo-tile" href="TRL_Calculator"> TRL Calculator</a>
<a class="holo-tile" href="/02_Business_Model_Selector">Business Models</a>
<a class="holo-tile" href="/03_Finanancial_Projection">Financial Projection</a>
<a class="holo-tile" href="/05_Market_Study_Guide">Marketing Strategy</a>
<a class="holo-tile" href="/06_Commercialisation_Strategy">Commercialisation Strategy</a>
<a class="holo-tile" href="/07_IP_Management">IP Management</a>
<a class="holo-tile" href="/08_Risk_Dashboard">Risk Dashboard</a>
<a class="holo-tile" href="/09_Financial_Options">Financial Options</a>
<a class="holo-tile" href="/10_Legal_and_Compliance">Legal Compliance</a>
<a class="holo-tile" href="/11_Feedback">Feedback</a>
<a class="holo-tile" href="/02_Export_Report">Export Tools</a>

</div>
""")

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
