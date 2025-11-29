# ============================================
# INNOVATION MENTOR APP
# PAGE: Legal & Compliance (Tile Edition)
# ============================================

import streamlit as st

# ----------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------
st.set_page_config(
    page_title="Legal & Compliance",
    page_icon="⚖️",
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
<h1 class="hero-title">Legal & Compliance</h1>
<p class="hero-sub">Clear guidance on terms, licensing, privacy and POPIA alignment.</p>
</div>
</div>
"""
st.markdown(hero_html, unsafe_allow_html=True)

# ----------------------------------------------------
st.set_page_config(page_title="Legal & Compliance", layout="wide")

st.title("⚖️ Legal & Compliance")
st.markdown("---")

tab1, tab2, tab3, tab4 = st.tabs([
    "Terms of Use",
    "Licence Summary",
    "Privacy & POPIA",
    "POPIA Memo"
])

# -------------------------------------------------
# 1. TERMS OF USE (Tile)
# -------------------------------------------------
with tab1:
    st.markdown("<div class='im-tile'>", unsafe_allow_html=True)

    st.markdown(
        """
        <h2>Terms of Use</h2>
        <p>These Terms of Use govern access to and use of the <b>Innovation Mentor</b> platform.</p>

        <h4>1. Purpose of the Platform</h4>
        <p>The platform is an independent educational tool.  
        It is <b>not affiliated</b> with any organisation, employer, or agency.</p>

        <h4>2. No Professional or Official Advice</h4>
        <p>This tool does <b>not</b> provide legal, financial, engineering, IP, or funding advice.  
        It must not be used for:</p>
        <ul>
            <li>official assessments</li>
            <li>funding or investment decisions</li>
            <li>due diligence</li>
            <li>organisational evaluation</li>
        </ul>

        <h4>3. Acceptable Use</h4>
        <ul>
            <li>Do not misuse or reverse-engineer the system.</li>
            <li>Do not upload harmful content or malicious code.</li>
            <li>Do not bypass reflection gates.</li>
            <li>Do not use the platform unlawfully.</li>
        </ul>

        <h4>4. Intellectual Property</h4>
        <p>All logic, frameworks, and content belong to the creator.</p>

        <h4>5. Liability Limitation</h4>
        <p>The creator is not liable for losses, decisions, or misinterpretations.</p>

        <h4>6. Updates</h4>
        <p>Terms may change as the platform evolves.</p>

        <p><br>© 2025 Innovation Mentor Platform — Educational use only.</p>
        """,
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------------------------
# 2. LICENCE SUMMARY
# -------------------------------------------------
with tab2:
    st.markdown("<div class='im-tile'>", unsafe_allow_html=True)

    st.markdown(
        """
        <h2>Licence Summary</h2>
        <p>The platform is licensed under the 
        <b>Creative Commons Attribution–NonCommercial 4.0 (CC BY–NC 4.0)</b>.</p>

        <h4>You May:</h4>
        <ul>
            <li>Share</li>
            <li>Adapt</li>
            <li>Remix</li>
            <li>Use for non-commercial education</li>
        </ul>

        <h4>Conditions:</h4>
        <ul>
            <li>Clear attribution required</li>
            <li>Strictly non-commercial use</li>
        </ul>

        <h4>You May Not:</h4>
        <ul>
            <li>Sell the tool</li>
            <li>Charge for access or services</li>
            <li>Claim proprietary ownership</li>
        </ul>

        <p>For commercial permissions, contact the creator directly.</p>
        """,
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------------------------
# 3. PRIVACY & POPIA NOTICE
# -------------------------------------------------
with tab3:
    st.markdown("<div class='im-tile'>", unsafe_allow_html=True)

    st.markdown(
        """
        <h2>Privacy & POPIA Notice</h2>
        <p>This platform follows <b>data minimisation</b> and <b>purpose limitation</b>.</p>

        <h4>Data Collected</h4>
        <ul>
            <li>Anonymous reflections</li>
            <li>Optional comments</li>
            <li>No cookies or analytics</li>
        </ul>

        <h4>Not Collected</h4>
        <ul>
            <li>Names</li>
            <li>Email addresses</li>
            <li>ID numbers</li>
            <li>IP addresses</li>
            <li>Device info</li>
        </ul>

        <h4>Data Storage</h4>
        <ul>
            <li><i>reflections.json</i></li>
            <li><i>comments.json</i></li>
        </ul>

        <h4>User Rights</h4>
        <p>Users may request deletion of reflections or comments.</p>

        <h4>Security</h4>
        <p>Designed to prevent profiling or identification.</p>
        """,
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------------------------
# 4. POPIA MEMO
# -------------------------------------------------
with tab4:
    st.markdown("<div class='im-tile'>", unsafe_allow_html=True)

    st.markdown(
        """
        <h2>POPIA Compliance Memo</h2>

        <h4>1. Minimal Data Collection</h4>
        <p>Only anonymous, non-personal data is stored.</p>

        <h4>2. Purpose Limitation</h4>
        <p>Used only for reflection and educational insight.</p>

        <h4>3. Storage & Safeguards</h4>
        <p>JSON files contain no personal identifiers.</p>

        <h4>4. Transparency</h4>
        <p>Users are fully informed at all times.</p>

        <h4>5. Data Quality</h4>
        <p>No external sharing, no cross-linking.</p>

        <h4>6. Risk Level</h4>
        <p>This is a <b>low-risk POPIA system</b>.</p>

        <h4>7. Compliance Summary</h4>
        <ul>
            <li>Purpose Limitation</li>
            <li>Data Minimisation</li>
            <li>Collection Limitation</li>
            <li>Security Safeguards</li>
            <li>Openness</li>
        </ul>
        """,
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)
