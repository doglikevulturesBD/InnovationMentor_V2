# ============================================
# INNOVATION MENTOR APP
# PAGE: Feedback (Tile Edition)
# ============================================

import streamlit as st

# ----------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------
st.set_page_config(
    page_title="Feedback",
    page_icon="💬",
    layout="wide"
)

# ----------------------------------------------------
# LOAD GLOBAL CSS
# ----------------------------------------------------
def local_css(file_name: str):
    try:
        with open(file_name, "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except:
        pass

local_css("styles.css")

# ----------------------------------------------------
# HERO BANNER
# ----------------------------------------------------
hero_html = """
<div class="hero sub-hero">
<div class="hero-glow"></div>
<div class="hero-particles"></div>

<div class="hero-content">
<h1 class="hero-title">💬 Feedback & Suggestions</h1>
<p class="hero-sub">
            Your input directly shapes the future development of the Innovation Mentor platform.
</p>
</div>
</div>
"""
st.markdown(hero_html, unsafe_allow_html=True)

# ----------------------------------------------------
# CONTENT WRAPPER
# ----------------------------------------------------
st.markdown("<div class='section-block'>", unsafe_allow_html=True)

st.caption("Help us improve this MVP by sharing your insights, suggestions, and feature requests.")
st.markdown("---")

# ----------------------------------------------------
# TILE: GOOGLE FORM EMBED
# ----------------------------------------------------
st.markdown("<div class='im-tile'>", unsafe_allow_html=True)

st.markdown("## Full Feedback Form")
st.markdown("Please complete the detailed form below:")

st.components.v1.html(
    '''
    <iframe src="https://docs.google.com/forms/d/e/1FAIpQLSc61A8kolpNa1NxKwR1eoYF7MLSwp-rofJTOS9XSaw30fwnWg/viewform?embedded=true"
    width="100%" height="1800" frameborder="0" marginheight="0" marginwidth="0">
    Loading…
    </iframe>
    ''',
    height=1850,
    scrolling=True
)

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")

# ----------------------------------------------------
# FOOTER IN TILE
# ----------------------------------------------------
st.markdown("<div class='im-tile' style='text-align:center;'>", unsafe_allow_html=True)

st.markdown("""
### ℹ️ Transparency Notice

Feedback submitted through this form is securely stored via **Google Forms / Google Workspace**.  
No personal identifying information is collected unless you explicitly choose to provide it.

For legal details, please refer to the **Legal & Compliance** section of the platform.
""")

st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------
# CLOSE WRAPPER
# ----------------------------------------------------
st.markdown("</div>", unsafe_allow_html=True)
