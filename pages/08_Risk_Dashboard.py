# ============================================
# INNOVATION MENTOR APP
# PAGE: 07_Risk_Dashboard.py
# FUNCTION: Hybrid Dynamic Risk Dashboard (Tile Edition)
# ============================================

import json
from pathlib import Path
from collections import defaultdict
import pandas as pd
import streamlit as st

# ----------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------
st.set_page_config(
    page_title="Risk Dashboard",
    page_icon="⚠️",
    layout="wide"
)

# ----------------------------------------------------
# GLOBAL CSS (same as other modules)
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
<h1 class="hero-title">Innovation Risk Dashboard</h1>
<p class="hero-sub">Identify, quantify, and mitigate the main risks limiting your innovation’s readiness.</p>
</div>
</div>
"""
st.markdown(hero_html, unsafe_allow_html=True)

# ----------------------------------------------------
# WRAP CONTENT
# ----------------------------------------------------
st.markdown("<div class='section-block'>", unsafe_allow_html=True)

st.markdown("---")

# ----------------------------------------------------
# Load JSON Assets
# ----------------------------------------------------
def load_json(path: str):
    p = Path(path)
    if not p.exists():
        st.error(f"❌ Missing file: `{path}`")
        st.stop()
    with p.open("r", encoding="utf-8") as f:
        return json.load(f)

engine = load_json("data/risk_engine.json")
library = load_json("data/risk_library.json")

weighting_rules = engine.get("weighting_rules", [])
questions = engine.get("questionnaire", [])
base_points = engine.get("scoring", {}).get("base_points_per_hit", 10)
top_n = engine.get("scoring", {}).get("top_n", 5)

# ----------------------------------------------------
# Read context (from other modules)
# ----------------------------------------------------
trl      = st.session_state.get("trl_level", 6)
bm       = st.session_state.get("selected_business_model", None)
funding  = st.session_state.get("funding_stage", "Seed")
mkt_str  = st.session_state.get("marketing_top_strategies", [])
comm     = st.session_state.get("commercialisation_pathway", None)

# ----------------------------------------------------
# Context Tile (inside expander)
# ----------------------------------------------------
with st.expander("ℹ️ Detected project context (editable)"):
    st.markdown("<div class='im-tile'>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.number_input("TRL", 1, 9, int(trl), key="ctx_trl")
        st.selectbox(
            "Funding stage",
            ["Pre-seed", "Seed", "Series A", "Series B", "Revenue"],
            index=["Pre-seed","Seed","Series A","Series B","Revenue"].index(funding) if funding in ["Pre-seed","Seed","Series A","Series B","Revenue"] else 1,
            key="ctx_funding"
        )
    with col2:
        st.selectbox(
            "Business model",
            ["Licensing", "Direct Sales", "Subscription",
             "Franchising / Replication Model", "Marketplace", "Other"],
            index=0 if not bm else 0,
            key="ctx_bm"
        )
        st.selectbox(
            "Commercialisation pathway",
            ["Public-Private Pilot", "Direct Sales", "Licensing",
             "Partnership / JV", "Franchising",
             "Digital Platform", "Co-Development", "Unknown"],
            index=7 if comm is None else 7,
            key="ctx_comm"
        )
    with col3:
        st.multiselect(
            "Top marketing strategies",
            ["Product Differentiation", "Cost / Value Leadership", "Niche / Community Focus",
             "Partnership & Co-Creation", "Digital-First", "Engagement / Experience",
             "Impact Branding", "Community Growth", "Ecosystem Storytelling"],
            default=mkt_str,
            key="ctx_mkt"
        )

    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")

# ----------------------------------------------------
# Questionnaire (Tile-style)
# ----------------------------------------------------
st.subheader("Quick Risk Questionnaire")

base_scores = defaultdict(int)
answers = {}
total_q = len(questions)

for i, q in enumerate(questions, start=1):
    st.markdown(f"<div class='im-tile'>", unsafe_allow_html=True)

    st.markdown(f"### Question {i} of {total_q}")
    st.markdown(f"**{q['question']}**")

    opts = [o["text"] for o in q["options"]]
    choice = st.radio("", opts, key=f"risk_q_{q['id']}")
    answers[q["id"]] = choice

    selected_option = next(o for o in q["options"] if o["text"] == choice)
    for risk_type in selected_option.get("adds", []):
        base_scores[risk_type] += base_points

    st.progress(i / total_q)

    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("")

# ----------------------------------------------------
# Apply Contextual Weighting Rules
# ----------------------------------------------------
ctx = {
    "trl": int(st.session_state["ctx_trl"]),
    "business_model": st.session_state["ctx_bm"],
    "funding_stage": st.session_state["ctx_funding"],
    "marketing": set(st.session_state["ctx_mkt"]),
    "commercialisation": st.session_state["ctx_comm"]
}

weighted_scores = defaultdict(int, base_scores)
rule_hits = defaultdict(list)

def rule_matches(rule_when: dict) -> bool:
    if "trl_max" in rule_when and ctx["trl"] > rule_when["trl_max"]:
        return False
    if "business_model_any" in rule_when and ctx["business_model"] not in rule_when["business_model_any"]:
        return False
    if "funding_stage_any" in rule_when and ctx["funding_stage"] not in rule_when["funding_stage_any"]:
        return False
    if "marketing_any" in rule_when and not (ctx["marketing"] & set(rule_when["marketing_any"])):
        return False
    if "commercialisation_any" in rule_when and ctx["commercialisation"] not in rule_when["commercialisation_any"]:
        return False
    return True

for rule in weighting_rules:
    if rule_matches(rule.get("when", {})):
        for risk_type, bonus in rule.get("weights", {}).items():
            weighted_scores[risk_type] += bonus
            rule_hits[risk_type].append(rule.get("name", "context_rule"))

# ----------------------------------------------------
# Top Risks
# ----------------------------------------------------
sorted_risks = sorted(weighted_scores.items(), key=lambda x: x[1], reverse=True)
top_risks = [(r, s) for r, s in sorted_risks if s > 0][:top_n]

st.subheader("Top Risks")

if not top_risks:
    st.info("No major risks detected yet — adjust questionnaire or context.")
else:
    # Chart in tile
    st.markdown("<div class='im-tile'>", unsafe_allow_html=True)
    st.markdown("#### Risk Score Overview")

    chart_df = pd.DataFrame(top_risks, columns=["Risk", "Score"]).set_index("Risk")
    st.bar_chart(chart_df)

    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("---")

  # Detailed tiles per risk
for risk_type, score in top_risks:
    entry = library.get(risk_type, {})

    indicators = entry.get("indicators", [])
    mitigation = entry.get("mitigation", [])
    severity = entry.get("severity", "—")
    category = entry.get("category", "—")

    # Build sections cleanly (avoid inline f-string conditions)
    indicators_block = ""
    if indicators:
        indicators_block = "<h4>Indicators</h4><ul>" + "".join([f"<li>{i}</li>" for i in indicators]) + "</ul>"

    mitigation_block = ""
    if mitigation:
        mitigation_block = "<h4>Mitigation</h4><ul>" + "".join([f"<li>{m}</li>" for m in mitigation]) + "</ul>"

    why_block = ""
    if rule_hits.get(risk_type):
        why_block = "<h4>Why this scored high</h4><ul>" + "".join([f"<li>{h}</li>" for h in rule_hits[risk_type]]) + "</ul>"

    # Now build full tile
    tile_html = f"""
    <div class="im-tile">
    <h3>⚠️ {risk_type} — Score {score}</h3>
    <p><b>Category:</b> {category} &nbsp; | &nbsp; <b>Baseline Severity:</b> {severity}</p>

    <h4>Description</h4>
    <p>{entry.get("description", "—")}</p>

    {indicators_block}
    {mitigation_block}
    {why_block}
    </div>
    """

    st.markdown(tile_html, unsafe_allow_html=True)

# ----------------------------------------------------
# Download Risk Register
# ----------------------------------------------------
if top_risks:
    rows = []
    for r, score in top_risks:
        e = library.get(r, {})
        mit = e.get("mitigation", [])
        rows.append({
            "Risk": r,
            "Score": score,
            "Category": e.get("category", ""),
            "Severity": e.get("severity", ""),
            "Description": e.get("description", ""),
            "Mitigation 1": mit[0] if len(mit) > 0 else "",
            "Mitigation 2": mit[1] if len(mit) > 1 else "",
            "Mitigation 3": mit[2] if len(mit) > 2 else "",
        })

    df = pd.DataFrame(rows)
    csv = df.to_csv(index=False).encode("utf-8")

    st.markdown("<div class='im-tile'>", unsafe_allow_html=True)
    st.markdown("### 📥 Export Risk Register")
    st.download_button(
        "⬇️ Download Risk Register (CSV)",
        csv,
        file_name="risk_register.csv",
        mime="text/csv",
        use_container_width=True
    )
    st.markdown("</div>", unsafe_allow_html=True)

st.caption("This dashboard adapts as other modules are completed. Fill in TRL, Market, Financial, Business Model, Strategy and IP for richer insights.")

# ----------------------------------------------------
# CLOSE WRAPPER
# ----------------------------------------------------
st.markdown("</div>", unsafe_allow_html=True)

