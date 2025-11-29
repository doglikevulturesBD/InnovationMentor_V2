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
# SECTION WRAPPER
# ----------------------------------------------------
st.markdown("<div class='section-block'>", unsafe_allow_html=True)

st.caption("Your quick-reference legal centre — all fully aligned to the Innovation Mentor design system.")
st.markdown("---")

# ----------------------------------------------------
# TABS
# ----------------------------------------------------
tab1, tab2, tab3, tab4 = st.tabs([
    "📘 Terms of Use", 
    "📝 Licence Summary", 
    "🔒 Privacy & POPIA Notice", 
    "📄 POPIA Compliance Memo"
])

# -------------------------
# 1. TERMS OF USE (Tile)
# -------------------------
with tab1:
    st.markdown("<div class='im-tile'>", unsafe_allow_html=True)

    st.markdown("""
    <h2>Terms of Use</h2>
    These Terms of Use govern your access to and use of the <b>Innovation Mentor</b> platform.

    <h4>1. Purpose of the Platform</h4>
    The platform is an independent educational tool.  
    It is <b>not affiliated</b> with any organisation, employer, or agency.

    <h4>2. No Professional or Official Advice</h4>
    This tool does <b>not</b> provide legal, financial, engineering, IP, or funding advice.  
    It must not be used for:
    <ul>
        <li>official assessments</li>
        <li>funding or investment decisions</li>
        <li>due diligence</li>
        <li>internal organisational evaluation</li>
    </ul>

    <h4>3. Acceptable Use</h4>
    You agree not to:
    <ul>
        <li>misuse or reverse-engineer the platform</li>
        <li>use it for unlawful or misleading purposes</li>
        <li>upload harmful content</li>
        <li>bypass reflection gates or modify logic</li>
    </ul>

    <h4>4. Intellectual Property</h4>
    All logic, frameworks and structured content belong to the creator.

    <h4>5. Liability Limitation</h4>
    The creator is not liable for losses, decisions or misinterpretations.

    <h4>6. Updates to These Terms</h4>
    Terms may be updated as the platform evolves.

    <br>© 2025 Innovation Mentor Platform — Educational use only.
    """)

    st.markdown("</div>", unsafe_allow_html=True)

# -------------------------
# 2. LICENCE SUMMARY (Tile)
# -------------------------
with tab2:
    st.markdown("<div class='im-tile'>", unsafe_allow_html=True)

    st.markdown("""
    <h2>Licence Summary</h2>
    The platform is released under the <b>Creative Commons Attribution–NonCommercial 4.0 International (CC BY–NC 4.0)</b> licence.

    <h4>You May:</h4>
    <ul>
        <li>Share the content</li>
        <li>Adapt and remix the templates</li>
        <li>Build upon the logic</li>
        <li>Use for non-commercial educational purposes</li>
    </ul>

    <h4>Conditions:</h4>
    <ul>
        <li>Clear attribution required</li>
        <li>Use must remain strictly non-commercial</li>
    </ul>

    <h4>You May Not:</h4>
    <ul>
        <li>Sell the tool</li>
        <li>Charge for access or services based on the platform</li>
        <li>Represent it as a proprietary product</li>
    </ul>

    For commercial permissions, contact the creator directly.
    """)

    st.markdown("</div>", unsafe_allow_html=True)

# -------------------------
# 3. PRIVACY & POPIA NOTICE (Tile)
# -------------------------
with tab3:
    st.markdown("<div class='im-tile'>", unsafe_allow_html=True)

    st.markdown("""
    <h2>Privacy & POPIA Notice</h2>
    This platform follows <b>data minimisation</b> and <b>purpose limitation</b> principles.

    <h4>What Data is Collected?</h4>
    <ul>
        <li>Anonymous reflections (private)</li>
        <li>Optional user comments</li>
        <li>No tracking, cookies, or analytics</li>
    </ul>

    <h4>What Is Not Collected?</h4>
    No personal identifiers:
    <ul>
        <li>Names</li>
        <li>Email addresses</li>
        <li>ID numbers</li>
        <li>IP addresses</li>
        <li>Device information</li>
    </ul>

    <h4>Why Data Is Collected</h4>
    <ul>
        <li>To support reflection-based learning</li>
        <li>To improve the educational tool</li>
        <li>To track module effectiveness (non-identifying)</li>
    </ul>

    <h4>Storage</h4>
    Locally stored JSON:
    <ul>
        <li><i>reflections.json</i> (private)</li>
        <li><i>comments.json</i> (optional)</li>
    </ul>

    <h4>User Rights</h4>
    Users may request deletion of reflections or comments.

    <h4>Security</h4>
    Designed to prevent identity inference or profiling.
    """)

    st.markdown("</div>", unsafe_allow_html=True)

# -------------------------
# 4. POPIA COMPLIANCE MEMO (Tile)
# -------------------------
with tab4:
    st.markdown("<div class='im-tile'>", unsafe_allow_html=True)

    st.markdown("""
    <h2>POPIA Compliance Memo</h2>

    <h4>1. Minimal Data Collection</h4>
    Only anonymous, non-personal data is collected.

    <h4>2. Purpose Limitation</h4>
    Data supports learning, reflection, and tool improvement only.

    <h4>3. Storage & Safeguards</h4>
    No personal identifiers are stored.  
    JSON files are isolated and low-risk.

    <h4>4. Transparency</h4>
    Users are fully informed on collection and use.

    <h4>5. Data Quality & Access</h4>
    Data is low-risk, anonymous and not shared externally.

    <h4>6. Low-Risk Assessment</h4>
    The platform qualifies as a <b>low-risk POPIA system</b>.

    <h4>7. Compliance</h4>
    Meets POPIA requirements for:
    <ul>
        <li>Purpose Limitation</li>
        <li>Collection Limitation</li>
        <li>Data Minimisation</li>
        <li>Security Safeguards</li>
        <li>Openness</li>
    </ul>
    """)

    st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------
# CLOSE WRAPPER
# ----------------------------------------------------
st.markdown("</div>", unsafe_allow_html=True)
