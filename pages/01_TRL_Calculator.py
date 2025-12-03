import streamlit as st
from utils.reflection_manager import enforce_reflection
from utils.comments_manager import comments_box
from utils.trl_logic import (
    questions, calculate_trl, trl_description,
    trl_descriptions, next_trl_description
)

# ------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------
st.set_page_config(page_title="TRL Calculator", page_icon="🚦", layout="wide")

# ------------------------------------------------------
# LOAD GLOBAL CSS (same as homepage)
# ------------------------------------------------------
def local_css(file_name: str):
    with open(file_name, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("styles.css")


# ------------------------------------------------------
# HERO BANNER — SAME STYLE AS HOME PAGE
# ------------------------------------------------------
hero_html = """
<div class="hero sub-hero">
<div class="hero-glow"></div>
<div class="hero-particles"></div>

<div class="hero-content">
<h1 class="hero-title">TRL Assessment</h1>
<p class="hero-sub">Determine your true technology readiness level.</p>
</div>
</div>
"""
st.markdown(hero_html, unsafe_allow_html=True)


# ------------------------------------------------------
# TRL LOGIC + UI
# ------------------------------------------------------
st.markdown("<div class='section-block'>", unsafe_allow_html=True)

st.caption("Answer each question honestly. A single ‘No’ will stop the assessment and assign the appropriate TRL.")

# ---------- Session State ----------
if "step" not in st.session_state:
    st.session_state.step = 0
if "answers" not in st.session_state:
    st.session_state.answers = []
if "finished" not in st.session_state:
    st.session_state.finished = False


def handle_answer(answer: bool):
    st.session_state.answers.append(answer)
    if not answer:
        st.session_state.finished = True
        return

    st.session_state.step += 1

    if st.session_state.step >= len(questions):
        st.session_state.finished = True


def restart():
    st.session_state.step = 0
    st.session_state.answers = []
    st.session_state.finished = False


# Sidebar restart button
with st.sidebar:
    st.header("TRL Tool")
    if st.button("🔄 Restart Assessment"):
        restart()
        st.experimental_rerun()


# ---------- Progress Bar ----------
progress = st.session_state.step / len(questions)
st.progress(progress)


# ---------- Question Flow ----------
if not st.session_state.finished and st.session_state.step < len(questions):

    q = questions[st.session_state.step]

    st.markdown(f"<h3>Step {st.session_state.step + 1} / {len(questions)}</h3>", unsafe_allow_html=True)
    st.markdown(f"<div class='section-text'><b>{q['text']}</b></div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    col1.button("🟩 Yes", key=f"yes_{st.session_state.step}", use_container_width=True,
                on_click=handle_answer, args=(True,))
    col2.button("🟥 No", key=f"no_{st.session_state.step}", use_container_width=True,
                on_click=handle_answer, args=(False,))

else:
    # ---------- Final Result ----------
    trl = calculate_trl(st.session_state.answers)
    label = "TRL 0 (pre-TRL)" if trl == 0 else f"TRL {trl} / 9"

    st.success(f"### Your Technology Readiness Level: **{label}**")

    st.markdown("### What This Means")
    st.write(trl_description(trl))

    st.markdown("### 📝 Your Responses")
    for i, ans in enumerate(st.session_state.answers):
        emoji = "🟩 Yes" if ans else "🟥 No"
        st.write(f"**Step {i+1}:** {emoji}")

    if trl < 9:
        st.markdown("### 🛠 How to Reach the Next TRL")
        st.info(f"**TRL {trl + 1}:** {next_trl_description(trl)}")
    else:
        st.balloons()
        st.success("🎉 TRL 9 achieved — proven commercial operation!")

    st.divider()
    st.markdown("### 📘 TRL Reference Overview")

    for lvl in range(0, 10):
        if lvl not in trl_descriptions:
            continue
        marker = "🟩" if lvl == trl else "⬜"
        name = "TRL 0 (pre-TRL)" if lvl == 0 else f"TRL {lvl}"
        st.markdown(f"{marker} **{name}:** {trl_descriptions[lvl]}")



    st.button("🔁 Restart", on_click=restart, use_container_width=True)

st.markdown("</div>", unsafe_allow_html=True)
