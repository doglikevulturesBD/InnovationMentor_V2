import streamlit as st

# -------------------------------------
# PAGE CONFIG
# -------------------------------------
st.set_page_config(
    page_title="Innovation Mentor",
    page_icon="💡",
    layout="wide"
)

# -------------------------------------
# LOAD STYLESHEET CSS
# -------------------------------------
def local_css(file_name):
    with open(file_name) as f:
        css = f"<style>{f.read()}</style>"
        st.markdown(css, unsafe_allow_html=True)

local_css("styles.css")      # ← ensure styles.css is next to this file


# -------------------------------------
# HERO BANNER
# -------------------------------------
st.markdown("""
<div class="hero">
    <div class="hero-glow"></div>
    <div class="hero-particles"></div>

    <div class="hero-content">
        <h1 class="hero-title">Innovation Mentor</h1>
        <p class="hero-sub">A future-ready platform for innovators, startups, and portfolio managers.</p>
    </div>
</div>
""", unsafe_allow_html=True)


# -------------------------------------
# FEATURE TILES
# -------------------------------------
st.markdown("""
<div class="tile-container">

    <a href="01_TRL_Assessment" class="glow-tile">TRL Assessment</a>
    <a href="02_Business_Models" class="glow-tile">Business Models</a>
    <a href="03_Finance_Tools" class="glow-tile">Financial Tools</a>
    <a href="04_Marketing_Strategy" class="glow-tile">Marketing Strategy</a>
    <a href="05_Risk_Dashboard" class="glow-tile">Risk Dashboard</a>
    <a href="06_Export_Tools" class="glow-tile">Export Tools</a>

</div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)


# -------------------------------------
# ABOUT SECTION
# -------------------------------------
st.markdown("""
<div class="section-block">
    <h2 class="section-title">About the Platform</h2>
    <p class="section-text">
        The Innovation Mentor Platform is designed to support innovators, researchers, entrepreneurs,
        and portfolio managers with structured tools for clarity and strong decision-making.
        It simplifies complex processes such as TRL assessment, business model selection,
        financial outlooks, risk analysis, and early commercialisation strategy development.
    </p>
</div>
""", unsafe_allow_html=True)


# -------------------------------------
# MODULE OVERVIEW
# -------------------------------------
st.markdown("""
<div class="section-block">
    <h2 class="section-title">What’s Inside</h2>

    <ul class="feature-list">
        <li><b>TRL Assessment:</b> A structured guide aligned with global TRL definitions.</li>
        <li><b>Business Model Logic:</b> Matches innovations to 70+ business model patterns.</li>
        <li><b>Financial Tools:</b> Helps explore revenue, costs, and viability.</li>
        <li><b>Marketing Strategy:</b> Market segmentation, value prop and channels.</li>
        <li><b>Risk Dashboard:</b> Evaluates technical, operational, market and financial risks.</li>
        <li><b>Export Tools:</b> Generate summaries and shareable formats.</li>
    </ul>
</div>
""", unsafe_allow_html=True)


# -------------------------------------
# MVP DISCLAIMER
# -------------------------------------
st.markdown("""
<div class="section-block">
    <h2 class="section-title">MVP Notice</h2>
    <p class="section-text">
        This platform is currently an MVP. Features, logic, scoring and AI guidance
        will evolve over time as real users test and provide input.
    </p>
</div>
""", unsafe_allow_html=True)


# -------------------------------------
# FOOTER
# -------------------------------------
st.markdown("""
<div class="footer">
    <p>© 2025 Innovation Mentor</p>
    <p class="footer-links">
        <a href="https://innovationmentor.streamlit.app" target="_blank">App</a> •
        <a href="https://linkedin.com" target="_blank">LinkedIn</a>
    </p>
</div>
""", unsafe_allow_html=True)
