# ============================================
# INNOVATION MENTOR APP
# PAGE: Legal & Compliance (Updated Edition)
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
<h1 class="hero-title">Legal & Compliance</h1>
<p class="hero-sub">Clarity on purpose, boundaries, privacy and responsible use.</p>
</div>
</div>
"""
st.markdown(hero_html, unsafe_allow_html=True)

# ----------------------------------------------------
st.title("⚖️ Legal & Compliance")
st.markdown("---")

tab1, tab2, tab3, tab4 = st.tabs([
    "Terms of Use",
    "Licence Summary",
    "Privacy & POPIA",
    "POPIA Memo"
])

# ----------------------------------------------------
# 1. TERMS OF USE
# ----------------------------------------------------
with tab1:
    st.markdown("<div class='im-tile'>", unsafe_allow_html=True)
    st.markdown(
        """
        <h2>Terms of Use</h2>
        <p>The <b>Innovation Mentor</b> platform is a personal, independent project created by the developer.  
        It is <b>not affiliated with, endorsed by, or connected to any employer, agency, or organisation</b>.  
        All content is provided in a personal capacity only.</p>

        <h4>1. Purpose of the Platform</h4>
        <p>This platform is an educational and reflective tool designed to support innovators with 
        early thinking, structure, and frameworks.  
        It is <b>not</b> an official assessment tool of any institution.</p>

        <h4>2. No Professional or Official Advice</h4>
        <p>The platform does <b>not</b> provide:</p>
        <ul>
            <li>legal advice</li>
            <li>financial or investment advice</li>
            <li>IP, engineering or technical certification</li>
            <li>funding recommendations or due diligence outputs</li>
            <li>formal organisational evaluations</li>
        </ul>
        <p>All insights are general, educational, and high-level.</p>

        <h4>3. Acceptable Use</h4>
        <ul>
            <li>Do not misuse, reverse-engineer, or attempt to access backend systems.</li>
            <li>Do not upload harmful content.</li>
            <li>Do not bypass reflection gates or alter scoring logic.</li>
            <li>Use the platform in a lawful, ethical manner.</li>
        </ul>

        <h4>4. Intellectual Property</h4>
        <p>All logic, frameworks, design systems, content, and educational material belong to the creator.  
        Unauthorised commercial reuse is not permitted.</p>

        <h4>5. Liability Limitation</h4>
        <p>The creator accepts no responsibility for decisions, interpretations, losses, or actions taken 
        using this tool. Users must apply their own judgement.</p>

        <h4>6. Updates</h4>
        <p>These Terms may be updated as the platform grows.</p>

        <p><br>© 2025 Innovation Mentor — Personal, independent project.</p>
        """,
        unsafe_allow_html=True
    )
    st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------
# 2. LICENCE SUMMARY
# ----------------------------------------------------
with tab2:
    st.markdown("<div class='im-tile'>", unsafe_allow_html=True)
    st.markdown(
        """
        <h2>Licence Summary</h2>
        <p>Innovation Mentor is released under the 
        <b>Creative Commons Attribution–NonCommercial 4.0 (CC BY–NC 4.0)</b> licence.</p>

        <h4>You May:</h4>
        <ul>
            <li>Share the platform</li>
            <li>Adapt or remix concepts</li>
            <li>Use for non-commercial learning</li>
        </ul>

        <h4>Conditions:</h4>
        <ul>
            <li>Clear attribution required</li>
            <li>No commercial use without written permission</li>
        </ul>

        <h4>You May Not:</h4>
        <ul>
            <li>Sell access or resell the tool</li>
            <li>Charge for services based solely on this tool</li>
            <li>Claim proprietary ownership</li>
        </ul>

        <p>For commercial permissions, please contact the creator directly.</p>
        """,
        unsafe_allow_html=True
    )
    st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------
# 3. PRIVACY & POPIA NOTICE
# ----------------------------------------------------
with tab3:
    st.markdown("<div class='im-tile'>", unsafe_allow_html=True)
    st.markdown(
        """
        <h2>Privacy & POPIA Notice</h2>
        <p>This platform follows <b>purpose limitation</b>, <b>data minimisation</b>, 
        and <b>transparency</b> principles.</p>

        <h4>Data Collected (Inside the App)</h4>
        <ul>
            <li>Anonymous reflections (if enabled)</li>
            <li>Optional comments</li>
        </ul>
        <p>No identifying fields (name, email, ID number) are requested.</p>

        <h4>Feedback Form (External)</h4>
        <p>The feedback page uses an embedded <b>Google Forms</b> questionnaire.</p>

        <ul>
            <li>Responses are securely stored by Google</li>
            <li>Google may process IP addresses and device data for security</li>
            <li>The creator only views the written responses</li>
            <li>No profiling or cross-linking is performed</li>
        </ul>

        <h4>Not Collected by the App</h4>
        <ul>
            <li>Account login details</li>
            <li>ID numbers</li>
            <li>Emails (unless you type them voluntarily)</li>
            <li>Geolocation</li>
        </ul>

        <p><b>Please avoid including personal or sensitive information in free-text responses.</b></p>

        <h4>User Rights</h4>
        <p>You may request deletion of your reflections or feedback entries at any time 
        by contacting the creator and describing the item to be removed.</p>

        <h4>Security</h4>
        <p>Data is kept minimal, isolated, and not used for identification or profiling.</p>

        <p><br>Overall, this is a <b>low-risk POPIA environment</b>.</p>
        """,
        unsafe_allow_html=True
    )
    st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------
# 4. POPIA MEMO
# ----------------------------------------------------
with tab4:
    st.markdown("<div class='im-tile'>", unsafe_allow_html=True)
    st.markdown(
        """
        <h2>POPIA Compliance Memo</h2>

        <h4>1. Minimal Data Collection</h4>
        <p>The platform collects only anonymous reflections and optional comments.  
        Feedback via Google Forms is stored externally by Google.</p>

        <h4>2. Purpose Limitation</h4>
        <p>All data is used solely for learning, improvement, and platform refinement.</p>

        <h4>3. External Processors</h4>
        <p>Google Forms may process technical information (e.g., IP address, device details).  
        This is separate from the app and handled by Google’s infrastructure.</p>

        <h4>4. Safeguards</h4>
        <p>No profiling, tracking, or identification is performed.  
        No cross-linking with any employer or external database.</p>

        <h4>5. Deletion Rights</h4>
        <p>Users may request deletion of any reflection or feedback entry.</p>

        <h4>6. Risk Assessment</h4>
        <p>Due to minimal data capture and no identifiers, the platform constitutes a 
        <b>low-risk POPIA system</b>.</p>

        <h4>7. Independence Statement</h4>
        <p>This platform is a personal project by the creator and has 
        <b>no connection to any employer, agency, or organisation</b>.  
        No employer information, databases, or systems are used.</p>

        """
        ,
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)

