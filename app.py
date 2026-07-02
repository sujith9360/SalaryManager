import streamlit as st
import pandas as pd
from datetime import date
import calendar

st.set_page_config(
    page_title="Salary Quest",
    page_icon="⚔️",
    layout="wide",
    initial_sidebar_state="expanded"
)

C = {
    "bg":        "#E8EDF2",
    "bg_warm":   "#EEF1F5",
    "bg_card":   "#E4E9EF",
    "bg_inset":  "#D8DEE6",
    "bg_white":  "#F0F4F8",
    "surface":   "#E8EDF2",
    "neo_light": "#FFFFFF",
    "neo_dark":  "#C8CED6",
    "neo_dark2": "#B8BFC8",
    "primary":      "#6C5CE7",
    "primary_lt":   "#A29BFE",
    "primary_dk":   "#5A4BD1",
    "primary_bg":   "rgba(108,92,231,0.10)",
    "primary_bg2":  "rgba(108,92,231,0.06)",
    "gold":      "#F59E0B",
    "gold_lt":   "#FBBF24",
    "gold_dk":   "#D97706",
    "gold_bg":   "rgba(245,158,11,0.10)",
    "teal":      "#0EA5E9",
    "teal_bg":   "rgba(14,165,233,0.10)",
    "green":     "#10B981",
    "green_lt":  "#34D399",
    "green_bg":  "rgba(16,185,129,0.10)",
    "orange":    "#F97316",
    "orange_bg": "rgba(249,115,22,0.10)",
    "red":       "#EF4444",
    "red_lt":    "#F87171",
    "red_bg":    "rgba(239,68,68,0.08)",
    "text":      "#1E293B",
    "text2":     "#475569",
    "text3":     "#94A3B8",
    "text4":     "#CBD5E1",
    "white":     "#FFFFFF",
}

def neo_raised(radius=20, intensity=1):
    return (f"background: {C['bg']};"
            f"border-radius: {radius}px;"
            f"box-shadow: {6*intensity}px {6*intensity}px {14*intensity}px {C['neo_dark']},"
            f" -{6*intensity}px -{6*intensity}px {14*intensity}px {C['neo_light']};"
            f"border: 1px solid rgba(255,255,255,0.6);")

def neo_inset(radius=14):
    return (f"background: {C['bg_inset']};"
            f"border-radius: {radius}px;"
            f"box-shadow: inset 3px 3px 7px {C['neo_dark']},"
            f" inset -3px -3px 7px {C['neo_light']};"
            f"border: none;")

def neo_flat(radius=16):
    return (f"background: {C['bg']};"
            f"border-radius: {radius}px;"
            f"box-shadow: 4px 4px 10px {C['neo_dark']},"
            f" -4px -4px 10px {C['neo_light']};"
            f"border: 1px solid rgba(255,255,255,0.5);")

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Bricolage+Grotesque:wght@500;600;700;800&family=JetBrains+Mono:wght@500;600;700&display=swap');

*, *::before, *::after {{ box-sizing: border-box; }}

html, body, [class*="css"], .stApp {{
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    color: {C['text']} !important;
    background: {C['bg']} !important;
}}
#MainMenu, footer, header {{ visibility: hidden; }}
::-webkit-scrollbar {{ width: 8px; }}
::-webkit-scrollbar-track {{ background: {C['bg']}; }}
::-webkit-scrollbar-thumb {{ background: {C['neo_dark']}; border-radius: 99px; }}

section[data-testid="stSidebar"] {{
    background: linear-gradient(180deg, {C['bg_warm']} 0%, {C['bg']} 100%) !important;
    border-right: none !important;
    box-shadow: 4px 0 20px rgba(0,0,0,0.06) !important;
    width: 330px !important;
}}
section[data-testid="stSidebar"] > div {{ padding: 0 !important; }}
.main .block-container {{ padding: 1.6rem 2.2rem 3rem !important; max-width: 1460px; }}

h1, h2, h3 {{
    font-family: 'Bricolage Grotesque', sans-serif !important;
    color: {C['text']} !important;
}}

label, div[data-testid="stWidgetLabel"] p, .stRadio label span {{
    color: {C['text2']} !important;
    font-size: 11.5px !important;
    font-weight: 700 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.08em !important;
}}

.stTextInput input, .stNumberInput input, .stDateInput input {{
    {neo_inset(12)}
    color: {C['text']} !important;
    font-size: 14px !important;
    font-weight: 600 !important;
    padding: 11px 14px !important;
    transition: all .2s ease;
}}
.stTextInput input:focus, .stNumberInput input:focus, .stDateInput input:focus {{
    box-shadow: inset 2px 2px 5px {C['neo_dark']}, inset -2px -2px 5px {C['neo_light']}, 0 0 0 3px {C['primary_bg']} !important;
    outline: none !important;
}}
.stTextInput input::placeholder {{ color: {C['text3']} !important; font-weight: 500; }}
.stNumberInput > div > div, .stDateInput > div, .stTextInput > div {{ background: transparent !important; }}
button[data-testid="stNumberInputStepDown"], button[data-testid="stNumberInputStepUp"] {{
    background: {C['bg']} !important;
    color: {C['text2']} !important;
    border: none !important;
    border-radius: 8px !important;
    box-shadow: 2px 2px 5px {C['neo_dark']}, -2px -2px 5px {C['neo_light']};
}}

.stSelectbox > div > div {{
    {neo_inset(12)}
    color: {C['text']} !important;
    font-weight: 600 !important;
}}
.stSelectbox svg {{ fill: {C['text2']} !important; }}
div[data-baseweb="popover"] {{
    background: {C['bg_white']} !important;
    border: 1px solid {C['text4']} !important;
    border-radius: 16px !important;
    box-shadow: 0 12px 40px rgba(0,0,0,0.10) !important;
}}
div[data-baseweb="popover"] li {{ color: {C['text']} !important; font-weight: 600 !important; }}
div[data-baseweb="popover"] li:hover {{ background: {C['primary_bg']} !important; }}

.stRadio [role="radiogroup"] {{ display:flex; gap:10px; flex-wrap:wrap; }}
.stRadio [role="radiogroup"] label {{
    {neo_raised(99, 0.6)}
    padding: 9px 20px !important;
    font-size: 13px !important;
    font-weight: 700 !important;
    color: {C['text2']} !important;
    text-transform: none !important;
    letter-spacing: 0 !important;
    cursor: pointer !important;
    transition: all .15s ease;
}}
.stRadio [role="radiogroup"] label:has(input:checked) {{
    background: linear-gradient(135deg, {C['primary']}, {C['primary_dk']}) !important;
    color: {C['white']} !important;
    border: none !important;
    box-shadow: 3px 3px 8px {C['neo_dark']}, -3px -3px 8px {C['neo_light']};
}}

.stSlider [data-baseweb="slider"] [role="slider"] {{
    background: {C['primary']} !important;
    box-shadow: 0 2px 8px rgba(108,92,231,0.35) !important;
}}
.stSlider [data-baseweb="slider"] > div > div {{
    background: {C['primary_lt']} !important;
}}

.stButton > button {{
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-weight: 800 !important;
    font-size: 14px !important;
    {neo_raised(14, 0.8)}
    color: {C['text']} !important;
    padding: 12px 22px !important;
    width: 100% !important;
    transition: all .15s ease !important;
}}
.stButton > button:hover {{
    box-shadow: 2px 2px 5px {C['neo_dark']}, -2px -2px 5px {C['neo_light']};
    transform: translateY(1px);
}}
.stButton > button[kind="primary"] {{
    background: linear-gradient(135deg, {C['primary']}, {C['primary_dk']}) !important;
    color: {C['white']} !important;
    border: none !important;
    box-shadow: 4px 4px 12px {C['neo_dark']}, -4px -4px 12px {C['neo_light']};
}}

[data-testid="stDataFrame"] {{
    border-radius: 16px !important;
    overflow: hidden !important;
    box-shadow: 4px 4px 10px {C['neo_dark']}, -4px -4px 10px {C['neo_light']};
}}
hr {{ border-color: {C['text4']} !important; margin: 1.4rem 0 !important; }}

details {{
    {neo_raised(16, 0.6)}
    overflow: hidden !important;
    margin-bottom: 8px !important;
}}
details summary {{
    color: {C['text']} !important;
    font-weight: 700 !important;
    padding: 14px 18px !important;
}}

.stTabs [data-baseweb="tab-list"] {{
    {neo_raised(16, 0.5)}
    padding: 6px !important;
    gap: 4px !important;
}}
.stTabs [data-baseweb="tab"] {{
    background: transparent !important;
    border-radius: 12px !important;
    color: {C['text2']} !important;
    font-weight: 700 !important;
    font-size: 13px !important;
    padding: 10px 20px !important;
    border: none !important;
}}
.stTabs [aria-selected="true"] {{
    background: {C['white']} !important;
    color: {C['primary']} !important;
    box-shadow: 2px 2px 6px {C['neo_dark']}, -2px -2px 6px {C['neo_light']};
    font-weight: 800 !important;
}}
.stTabs [data-baseweb="tab-panel"] {{ padding-top: 1.4rem !important; }}

div[data-testid="stMetric"] {{
    {neo_raised(16, 0.6)}
    padding: 16px 18px !important;
}}

/* ══════ CUSTOM COMPONENTS ══════ */
.page-header {{ margin-bottom: 1.8rem; }}
.page-badge {{
    display: inline-flex; align-items: center; gap: 6px;
    background: linear-gradient(135deg, {C['primary']}, {C['primary_dk']});
    color: {C['white']}; border-radius: 99px; padding: 6px 16px;
    font-size: 11px; font-weight: 800; letter-spacing: .07em;
    text-transform: uppercase; margin-bottom: 14px;
    box-shadow: 0 4px 14px rgba(108,92,231,0.30);
}}
.page-title {{
    font-family: 'Bricolage Grotesque', sans-serif;
    font-size: 38px; font-weight: 800; color: {C['text']};
    letter-spacing: -0.01em; line-height: 1.15;
}}
.page-title span {{
    background: linear-gradient(135deg, {C['gold']}, {C['gold_dk']});
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}}
.page-sub {{
    font-size: 14.5px; color: {C['text2']};
    max-width: 640px; line-height: 1.65; margin-top: 8px; font-weight: 500;
}}

.sec-title {{
    font-family: 'Bricolage Grotesque', sans-serif;
    font-size: 17px; font-weight: 700; color: {C['text']};
    margin-bottom: 4px; letter-spacing: -0.01em;
}}
.sec-sub {{ font-size: 12.5px; color: {C['text3']}; margin-bottom: 16px; font-weight: 500; }}

.neo-card {{ {neo_raised(20, 1)} padding: 24px; margin-bottom: 20px; }}
.neo-card-sm {{ {neo_raised(14, 0.6)} padding: 16px; }}
.neo-card.glow-primary {{ box-shadow: 6px 6px 14px {C['neo_dark']}, -6px -6px 14px {C['neo_light']}, 0 0 20px rgba(108,92,231,0.12); }}
.neo-card.glow-gold {{ box-shadow: 6px 6px 14px {C['neo_dark']}, -6px -6px 14px {C['neo_light']}, 0 0 20px rgba(245,158,11,0.12); }}
.neo-card.glow-red {{ box-shadow: 6px 6px 14px {C['neo_dark']}, -6px -6px 14px {C['neo_light']}, 0 0 28px rgba(239,68,68,0.18); }}
.neo-card.glow-green {{ box-shadow: 6px 6px 14px {C['neo_dark']}, -6px -6px 14px {C['neo_light']}, 0 0 22px rgba(16,185,129,0.15); }}
.neo-card.glow-orange {{ box-shadow: 6px 6px 14px {C['neo_dark']}, -6px -6px 14px {C['neo_light']}, 0 0 22px rgba(249,115,22,0.15); }}

.stat-pill {{ {neo_raised(16, 0.7)} padding: 18px; text-align: center; }}
.stat-pill .s-label {{ font-size: 10px; font-weight: 800; text-transform: uppercase; letter-spacing: .08em; color: {C['text3']}; margin-bottom: 8px; }}
.stat-pill .s-value {{ font-family: 'JetBrains Mono', monospace; font-size: 21px; font-weight: 700; color: {C['text']}; }}
.stat-pill .s-sub {{ font-size: 10.5px; color: {C['text3']}; margin-top: 5px; font-weight: 600; }}

.hero-stat {{
    background: linear-gradient(145deg, {C['primary_bg']}, {C['bg']});
    border: 1px solid rgba(108,92,231,0.15); border-radius: 22px; padding: 24px; text-align: center;
    box-shadow: 6px 6px 16px {C['neo_dark']}, -6px -6px 16px {C['neo_light']}, inset 0 1px 0 rgba(255,255,255,0.8);
}}
.hero-stat .hs-label {{ font-size: 11px; font-weight: 800; text-transform: uppercase; letter-spacing: .1em; color: {C['primary']}; margin-bottom: 8px; }}
.hero-stat .hs-value {{ font-family: 'Bricolage Grotesque', sans-serif; font-size: 38px; font-weight: 800; color: {C['text']}; }}
.hero-stat .hs-sub {{ font-size: 12px; color: {C['text2']}; margin-top: 6px; font-weight: 600; }}

/* ═══ BIG WARNING BANNERS ═══ */
.warn-banner {{
    border-radius: 20px; padding: 22px 24px; margin: 12px 0;
    display: flex; align-items: flex-start; gap: 16px;
    border: 2px solid; position: relative; overflow: hidden;
}}
.warn-banner::before {{
    content: ''; position: absolute;
    top: 0; left: 0; right: 0; height: 3px;
    border-radius: 20px 20px 0 0;
}}
.warn-banner.critical {{
    background: linear-gradient(135deg, rgba(239,68,68,0.08), rgba(239,68,68,0.04));
    border-color: rgba(239,68,68,0.35);
    box-shadow: 6px 6px 14px {C['neo_dark']}, -6px -6px 14px {C['neo_light']}, 0 0 30px rgba(239,68,68,0.12);
}}
.warn-banner.critical::before {{ background: linear-gradient(90deg, {C['red']}, {C['red_lt']}); }}
.warn-banner.caution {{
    background: linear-gradient(135deg, rgba(249,115,22,0.08), rgba(249,115,22,0.04));
    border-color: rgba(249,115,22,0.35);
    box-shadow: 6px 6px 14px {C['neo_dark']}, -6px -6px 14px {C['neo_light']}, 0 0 30px rgba(249,115,22,0.10);
}}
.warn-banner.caution::before {{ background: linear-gradient(90deg, {C['orange']}, {C['gold_lt']}); }}
.warn-banner.safe {{
    background: linear-gradient(135deg, rgba(16,185,129,0.08), rgba(16,185,129,0.04));
    border-color: rgba(16,185,129,0.35);
    box-shadow: 6px 6px 14px {C['neo_dark']}, -6px -6px 14px {C['neo_light']}, 0 0 20px rgba(16,185,129,0.10);
}}
.warn-banner.safe::before {{ background: linear-gradient(90deg, {C['green']}, {C['green_lt']}); }}
.warn-banner.info-blue {{
    background: linear-gradient(135deg, rgba(14,165,233,0.08), rgba(14,165,233,0.04));
    border-color: rgba(14,165,233,0.35);
    box-shadow: 6px 6px 14px {C['neo_dark']}, -6px -6px 14px {C['neo_light']}, 0 0 20px rgba(14,165,233,0.10);
}}
.warn-banner.info-blue::before {{ background: linear-gradient(90deg, {C['teal']}, {C['primary_lt']}); }}

.warn-icon {{
    font-size: 32px; flex-shrink: 0; line-height: 1;
    filter: drop-shadow(0 2px 6px rgba(0,0,0,0.15));
}}
.warn-title {{
    font-family: 'Bricolage Grotesque', sans-serif;
    font-size: 17px; font-weight: 800; margin-bottom: 4px;
}}
.warn-body {{ font-size: 13.5px; font-weight: 500; line-height: 1.6; color: {C['text2']}; }}
.warn-body b {{ font-weight: 800; }}

/* Budget meter strip */
.budget-meter {{
    {neo_raised(16, 0.8)}
    padding: 20px; margin: 14px 0;
}}
.budget-meter-label {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; }}
.budget-meter-title {{ font-size: 12px; font-weight: 800; text-transform: uppercase; letter-spacing: .07em; color: {C['text3']}; }}
.budget-meter-value {{ font-family: 'JetBrains Mono', monospace; font-size: 14px; font-weight: 700; }}
.budget-track {{
    height: 18px; {neo_inset(99)} overflow: hidden; position: relative;
}}
.budget-fill {{
    height: 100%; border-radius: 99px; transition: width .4s ease;
    position: relative; overflow: hidden;
}}
.budget-fill::after {{
    content: ''; position: absolute; inset: 0;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.5), transparent);
    width: 40%; animation: shimmer 2s infinite;
}}
@keyframes shimmer {{
    0% {{ transform: translateX(-120%); }}
    100% {{ transform: translateX(340%); }}
}}

/* Live preview card */
.preview-card {{
    border-radius: 18px; padding: 20px;
    border: 2px dashed {C['text4']};
    background: {C['bg_white']};
    box-shadow: inset 3px 3px 8px {C['neo_dark']}, inset -3px -3px 8px {C['neo_light']};
    margin: 14px 0;
    transition: all .3s ease;
}}
.preview-card.has-amount {{
    border-style: solid;
    box-shadow: 4px 4px 12px {C['neo_dark']}, -4px -4px 12px {C['neo_light']};
    background: {C['bg']};
}}
.preview-row {{
    display: flex; justify-content: space-between; align-items: center;
    padding: 8px 0; border-bottom: 1px solid {C['text4']};
    font-size: 13.5px;
}}
.preview-row:last-child {{ border-bottom: none; padding-bottom: 0; }}
.preview-lbl {{ color: {C['text2']}; font-weight: 600; }}
.preview-val {{ font-family: 'JetBrains Mono', monospace; font-weight: 700; color: {C['text']}; }}

/* Pill tags */
.prog-wrap {{ margin: 14px 0; }}
.prog-label {{ display: flex; justify-content: space-between; font-size: 12px; font-weight: 700; margin-bottom: 7px; }}
.prog-bar {{ height: 14px; {neo_inset(99)} overflow: hidden; position: relative; }}
.prog-fill {{ height: 100%; border-radius: 99px; transition: width .5s ease; position: relative; overflow: hidden; }}
.prog-fill::after {{
    content: ''; position: absolute; inset: 0;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.5), transparent);
    width: 40%; animation: shimmer 2.5s infinite;
}}

.exp-row {{ display: flex; align-items: center; gap: 14px; padding: 14px 0; border-bottom: 1px solid {C['text4']}; }}
.exp-row:last-child {{ border-bottom: none; }}
.exp-icon {{ width: 42px; height: 42px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 18px; flex-shrink: 0; {neo_raised(12, 0.4)} }}
.exp-info {{ flex: 1; min-width: 0; }}
.exp-place {{ font-size: 14px; font-weight: 800; color: {C['text']}; }}
.exp-meta {{ font-size: 11px; color: {C['text3']}; margin-top: 3px; font-weight: 600; }}
.exp-amt {{ font-family: 'JetBrains Mono', monospace; font-size: 15px; font-weight: 700; color: {C['gold_dk']}; flex-shrink: 0; }}
.exp-badge {{ font-size: 10px; font-weight: 800; padding: 4px 12px; border-radius: 99px; flex-shrink: 0; }}
.badge-need {{ background: {C['teal_bg']}; color: {C['teal']}; border: 1px solid rgba(14,165,233,0.3); }}
.badge-want {{ background: {C['orange_bg']}; color: {C['orange']}; border: 1px solid rgba(249,115,22,0.3); }}

.tag {{ display: inline-block; padding: 4px 14px; border-radius: 99px; font-size: 11px; font-weight: 800; }}
.tag-green {{ background: {C['green_bg']}; color: {C['green']}; border: 1px solid rgba(16,185,129,0.3); }}
.tag-red {{ background: {C['red_bg']}; color: {C['red']}; border: 1px solid rgba(239,68,68,0.3); }}
.tag-yellow {{ background: {C['orange_bg']}; color: {C['orange']}; border: 1px solid rgba(249,115,22,0.3); }}
.tag-blue {{ background: {C['teal_bg']}; color: {C['teal']}; border: 1px solid rgba(14,165,233,0.3); }}

.bk-row {{ display: flex; justify-content: space-between; align-items: center; padding: 11px 0; border-bottom: 1px solid {C['text4']}; font-size: 13.5px; }}
.bk-row:last-child {{ border-bottom: none; }}
.bk-label {{ color: {C['text2']}; font-weight: 600; }}
.bk-val {{ font-weight: 700; color: {C['text']}; font-family: 'JetBrains Mono', monospace; }}

.alert-strip {{ padding: 14px 18px; border-radius: 16px; font-size: 13.5px; font-weight: 600; margin-bottom: 12px; display: flex; align-items: flex-start; gap: 10px; line-height: 1.5; border: 1px solid; }}
.alert-strip.info {{ background: {C['teal_bg']}; border-color: rgba(14,165,233,0.25); color: {C['teal']}; }}
.alert-strip.success {{ background: {C['green_bg']}; border-color: rgba(16,185,129,0.25); color: {C['green']}; }}
.alert-strip.warning {{ background: {C['orange_bg']}; border-color: rgba(249,115,22,0.25); color: {C['orange']}; }}
.alert-strip.danger {{ background: {C['red_bg']}; border-color: rgba(239,68,68,0.25); color: {C['red']}; }}

.wiz-progress {{ display: flex; gap: 8px; margin-bottom: 28px; }}
.wiz-dot {{ flex: 1; height: 8px; border-radius: 99px; {neo_inset(99)} }}
.wiz-dot.done {{ background: linear-gradient(90deg, {C['green']}, {C['teal']}) !important; box-shadow: none; }}
.wiz-dot.active {{ background: linear-gradient(90deg, {C['primary']}, {C['primary_lt']}) !important; box-shadow: 0 2px 10px rgba(108,92,231,0.35); }}
.wiz-step-label {{ font-family: 'Bricolage Grotesque', sans-serif; font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: .1em; color: {C['primary']}; margin-bottom: 10px; }}

.level-badge {{
    display: flex; align-items: center; gap: 16px; padding: 18px 22px; border-radius: 20px;
    background: linear-gradient(135deg, {C['primary_bg']}, {C['gold_bg']});
    border: 1px solid rgba(108,92,231,0.12);
    box-shadow: 6px 6px 16px {C['neo_dark']}, -6px -6px 16px {C['neo_light']};
}}
.level-badge .lvl-icon {{ font-size: 36px; filter: drop-shadow(0 2px 8px rgba(245,158,11,0.35)); }}
.level-badge .lvl-title {{ font-family: 'Bricolage Grotesque', sans-serif; font-size: 18px; font-weight: 800; color: {C['text']}; }}
.level-badge .lvl-sub {{ font-size: 12.5px; color: {C['text2']}; font-weight: 600; margin-top: 2px; }}

.sb-header {{ background: linear-gradient(150deg, {C['primary_bg']}, {C['bg_warm']}); border-bottom: 1px solid {C['text4']}; padding: 24px 22px; }}
.sb-title {{ font-family: 'Bricolage Grotesque', sans-serif; font-size: 20px; font-weight: 800; color: {C['text']}; }}
.sb-sub {{ font-size: 11.5px; color: {C['primary']}; margin-top: 3px; font-weight: 700; letter-spacing: .02em; }}
.sb-section {{ padding: 16px 22px; }}
.sb-section-title {{ font-size: 11px; font-weight: 800; text-transform: uppercase; letter-spacing: .08em; color: {C['text3']}; margin-bottom: 12px; }}

.tip-row {{ display: flex; gap: 14px; align-items: flex-start; padding: 14px 0; border-bottom: 1px solid {C['text4']}; }}
.tip-row:last-child {{ border-bottom: none; }}
.tip-num {{ width: 30px; height: 30px; background: linear-gradient(135deg, {C['primary']}, {C['primary_dk']}); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 11px; font-weight: 800; color: {C['white']}; flex-shrink: 0; margin-top: 2px; box-shadow: 0 3px 10px rgba(108,92,231,0.30); }}
.tip-title {{ font-size: 14px; font-weight: 800; color: {C['text']}; margin-bottom: 3px; }}
.tip-body {{ font-size: 12.5px; color: {C['text3']}; line-height: 1.6; font-weight: 500; }}
.tip-group-title {{ font-family: 'Bricolage Grotesque', sans-serif; font-size: 12px; font-weight: 700; letter-spacing: .08em; color: {C['gold_dk']}; padding: 18px 0 6px; text-transform: uppercase; }}

section[data-testid="stSidebar"] .stNumberInput,
section[data-testid="stSidebar"] .stSlider {{ margin-bottom: 10px !important; }}
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────
CATEGORY_ICONS = {
    "Food": "🍛", "Tea / Coffee": "☕", "Travel": "🚌",
    "Friends & Social": "👥", "Shopping": "🛍️", "Medical": "💊",
    "Bills & Utilities": "📱", "Entertainment": "🎬",
    "Groceries": "🛒", "Other": "📌",
}
PAYMENT_ICONS = {"UPI": "📲", "Cash": "💵", "Card": "💳", "Net Banking": "🏦", "Wallet": "👝"}

QUICK_ADD_PRESETS = [
    ("Tea / Coffee", "Tea / Coffee", 20, "Need"),
    ("Auto / Cab", "Travel", 60, "Need"),
    ("Lunch", "Food", 150, "Need"),
    ("Snacks", "Food", 80, "Want"),
]

PRESETS = {
    "Metro, living alone": dict(rent=0.28, groceries=0.07, transport=0.03, utilities=0.02, phone=0.01, grooming=0.02, gold=0.05, rd=0.03, mf=0.03, ef=0.02, goal=20),
    "Metro, with family":  dict(rent=0.18, groceries=0.10, transport=0.04, utilities=0.03, phone=0.01, grooming=0.02, gold=0.06, rd=0.04, mf=0.03, ef=0.02, goal=20),
    "Tier-2 city":         dict(rent=0.15, groceries=0.08, transport=0.03, utilities=0.02, phone=0.01, grooming=0.02, gold=0.06, rd=0.04, mf=0.04, ef=0.03, goal=25),
    "Staying with parents":dict(rent=0.00, groceries=0.04, transport=0.03, utilities=0.01, phone=0.01, grooming=0.02, gold=0.10, rd=0.06, mf=0.06, ef=0.04, goal=35),
}

LEVELS = [
    (0,  "🥉", "Novice Adventurer", "Your finances need urgent attention"),
    (25, "🛡️", "Apprentice Saver", "Building the basics of your budget"),
    (50, "⚔️", "Budget Warrior", "Holding steady — keep pushing"),
    (70, "🏹", "Coin Ranger", "Good discipline, refine the details"),
    (85, "👑", "Wealth Wizard", "Elite money management"),
    (95, "🐉", "Legendary Hoarder", "Master of the treasury"),
]

def get_level(score):
    lvl = LEVELS[0]
    for l in LEVELS:
        if score >= l[0]:
            lvl = l
    return lvl

def fmt_inr(n: float) -> str:
    if abs(n) >= 1_00_000: return f"₹{n/1_00_000:.2f}L"
    if abs(n) >= 1_000: return f"₹{n:,.0f}"
    return f"₹{n:.0f}"

def progress_html(label_left, label_right, pct, color, subtext=""):
    clamped = max(0, min(100, pct))
    sub = f'<div style="font-size:11px;color:{C["text3"]};margin-top:5px;font-weight:600">{subtext}</div>' if subtext else ''
    return f"""
    <div class="prog-wrap">
      <div class="prog-label"><span style="color:{C['text2']}">{label_left}</span>
      <span style="color:{color};font-weight:800">{label_right}</span></div>
      <div class="prog-bar"><div class="prog-fill" style="width:{clamped:.1f}%; background:linear-gradient(90deg, {color}, {color}dd);"></div></div>
      {sub}
    </div>"""

def stat_pill(label, value, sub="", color=""):
    style = f"color:{color};" if color else ""
    subd = f'<div class="s-sub">{sub}</div>' if sub else ""
    return f'<div class="stat-pill"><div class="s-label">{label}</div><div class="s-value" style="{style}">{value}</div>{subd}</div>'

def budget_meter_html(spent, total, color, label="Today's Budget"):
    pct = min(100, (spent / total * 100)) if total > 0 else 0
    remaining = max(total - spent, 0)
    over = max(spent - total, 0)
    return f"""
    <div class="budget-meter">
      <div class="budget-meter-label">
        <span class="budget-meter-title">{label}</span>
        <span class="budget-meter-value" style="color:{color}">{pct:.0f}% used</span>
      </div>
      <div class="budget-track">
        <div class="budget-fill" style="width:{pct:.1f}%; background:linear-gradient(90deg,{color},{color}cc);"></div>
      </div>
      <div style="display:flex;justify-content:space-between;margin-top:8px;font-size:12px;font-weight:700">
        <span style="color:{C['text3']}">Spent: <span style="color:{color}">{fmt_inr(spent)}</span></span>
        <span style="color:{C['text3']}">Limit: <span style="color:{C['text2']}">{fmt_inr(total)}</span></span>
        {'<span style="color:'+C['red']+'">Over by: '+fmt_inr(over)+'</span>' if over > 0 else '<span style="color:'+C['green']+'">Left: '+fmt_inr(remaining)+'</span>'}
      </div>
    </div>"""

def warn_banner(level, icon, title, body):
    """level: critical | caution | safe | info-blue"""
    color_map = {
        "critical": C['red'],
        "caution":  C['orange'],
        "safe":     C['green'],
        "info-blue": C['teal'],
    }
    col = color_map.get(level, C['text2'])
    return f"""
    <div class="warn-banner {level}">
      <div class="warn-icon">{icon}</div>
      <div>
        <div class="warn-title" style="color:{col}">{title}</div>
        <div class="warn-body">{body}</div>
      </div>
    </div>"""

def savings_gauge_svg(pct):
    r, cx, cy = 68, 90, 90
    circ = 2 * 3.14159 * r
    clamped = max(0, min(100, pct))
    dash = circ * (clamped / 100)
    gap  = circ - dash
    arc  = C['green'] if pct >= 20 else (C['orange'] if pct >= 10 else C['red'])
    return f"""
    <svg viewBox="0 0 180 180" width="180" height="180" xmlns="http://www.w3.org/2000/svg">
      <circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{C['neo_dark']}" stroke-width="14" opacity="0.4"/>
      <circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{arc}" stroke-width="14" stroke-linecap="round"
              stroke-dasharray="{dash:.2f} {gap:.2f}" transform="rotate(-90 {cx} {cy})"/>
      <text x="{cx}" y="{cy-6}" text-anchor="middle" font-family="Bricolage Grotesque,sans-serif" font-weight="800" font-size="26" fill="{C['text']}">{pct:.1f}%</text>
      <text x="{cx}" y="{cy+16}" text-anchor="middle" font-family="Plus Jakarta Sans,sans-serif" font-size="10.5" font-weight="700" fill="{C['text3']}">saved this month</text>
    </svg>"""


# ─────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────
defaults = {
    "expenses": [], "setup_done": False, "wiz_step": 0,
    "salary": 50000, "rent": 8000, "groceries_fix": 3000, "transport_fix": 500,
    "utilities": 700, "phone": 300, "grooming": 500, "other_fixed": 0,
    "gold_inv": 2000, "rd_inv": 1000, "mutual_fund": 500, "emergency_add": 500,
    "savings_goal_pct": 20, "emergency_months": 6, "current_ef_saved": 5000,
    "ref_date": date.today(),
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

def apply_preset(name):
    p = PRESETS[name]
    s = st.session_state.salary
    st.session_state.rent          = round(s * p["rent"]      / 50) * 50
    st.session_state.groceries_fix = round(s * p["groceries"] / 50) * 50
    st.session_state.transport_fix = round(s * p["transport"] / 50) * 50
    st.session_state.utilities     = round(s * p["utilities"] / 50) * 50
    st.session_state.phone         = round(s * p["phone"]     / 50) * 50
    st.session_state.grooming      = round(s * p["grooming"]  / 50) * 50
    st.session_state.gold_inv      = round(s * p["gold"]      / 50) * 50
    st.session_state.rd_inv        = round(s * p["rd"]        / 50) * 50
    st.session_state.mutual_fund   = round(s * p["mf"]        / 50) * 50
    st.session_state.emergency_add = round(s * p["ef"]        / 50) * 50
    st.session_state.savings_goal_pct = p["goal"]


# ═══════════════════════════════════════════════════════════════
# ONBOARDING WIZARD
# ═══════════════════════════════════════════════════════════════
def render_wizard():
    steps = ["Origin", "Homestead", "Vault", "Ambitions", "Begin"]
    st.markdown(f"""
    <div class="page-header">
      <div class="page-badge">⚔️ Character Creation</div>
      <div class="page-title">Salary <span>Quest</span></div>
      <div class="page-sub">Forge your financial character. A few quick questions — under a minute — and every number can be changed later.</div>
    </div>""", unsafe_allow_html=True)

    dots = "".join(
        f'<div class="wiz-dot {"done" if i < st.session_state.wiz_step else "active" if i == st.session_state.wiz_step else ""}"></div>'
        for i in range(len(steps))
    )
    st.markdown(f'<div class="wiz-progress">{dots}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="wiz-step-label">Chapter {st.session_state.wiz_step+1} of {len(steps)} · {steps[st.session_state.wiz_step]}</div>', unsafe_allow_html=True)

    step = st.session_state.wiz_step

    if step == 0:
        st.markdown('<div class="neo-card glow-primary">', unsafe_allow_html=True)
        st.markdown('<div class="sec-title">💰 What treasure flows into your vault each month?</div>', unsafe_allow_html=True)
        st.markdown('<div class="sec-sub">Your net take-home salary — the gold that actually lands in your account.</div>', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            st.session_state.salary = st.number_input("Monthly take-home salary (₹)", min_value=0, value=st.session_state.salary, step=500)
        with c2:
            st.session_state.ref_date = st.date_input("Today's date", value=st.session_state.ref_date)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="neo-card">', unsafe_allow_html=True)
        st.markdown('<div class="sec-title">🏙️ Choose your starting realm</div>', unsafe_allow_html=True)
        st.markdown('<div class="sec-sub">Pick the closest match to auto-fill sensible numbers — you\'ll review every figure next.</div>', unsafe_allow_html=True)
        pc = st.columns(len(PRESETS))
        for col, name in zip(pc, PRESETS.keys()):
            with col:
                if st.button(name, key=f"preset_{name}", use_container_width=True):
                    apply_preset(name)
                    st.toast(f"⚔️ Filled starting stats for '{name}'")
        st.caption("Or skip and enter everything yourself.")
        st.markdown('</div>', unsafe_allow_html=True)

    elif step == 1:
        st.markdown('<div class="neo-card">', unsafe_allow_html=True)
        st.markdown('<div class="sec-title">🏰 What upkeep does your homestead demand?</div>', unsafe_allow_html=True)
        st.markdown('<div class="sec-sub">Costs that repeat every month no matter what.</div>', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            st.session_state.rent          = st.number_input("Rent / Home loan EMI (₹)", min_value=0, value=st.session_state.rent, step=100)
            st.session_state.groceries_fix = st.number_input("Groceries — staples (₹)", min_value=0, value=st.session_state.groceries_fix, step=100)
            st.session_state.transport_fix = st.number_input("Transport pass / fuel (₹)", min_value=0, value=st.session_state.transport_fix, step=50)
        with c2:
            st.session_state.utilities = st.number_input("Electricity, water, gas (₹)", min_value=0, value=st.session_state.utilities, step=50)
            st.session_state.phone     = st.number_input("Phone / Internet (₹)", min_value=0, value=st.session_state.phone, step=50)
            st.session_state.grooming  = st.number_input("Grooming / personal care (₹)", min_value=0, value=st.session_state.grooming, step=50)
        st.session_state.other_fixed = st.number_input("Anything else fixed? (₹)", min_value=0, value=st.session_state.other_fixed, step=100)
        fixed_total = (st.session_state.rent + st.session_state.groceries_fix + st.session_state.transport_fix
                       + st.session_state.utilities + st.session_state.phone + st.session_state.grooming + st.session_state.other_fixed)
        if st.session_state.salary > 0:
            pct = fixed_total / st.session_state.salary * 100
            col = C['red'] if pct > 60 else C['orange'] if pct > 50 else C['green']
            st.markdown(progress_html("Homestead upkeep so far", f"{fmt_inr(fixed_total)} · {pct:.0f}% of salary", pct, col), unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    elif step == 2:
        st.markdown('<div class="neo-card">', unsafe_allow_html=True)
        st.markdown('<div class="sec-title">💎 What are you already stashing in the vault?</div>', unsafe_allow_html=True)
        st.markdown('<div class="sec-sub">Money that leaves your account into something that grows.</div>', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            st.session_state.gold_inv   = st.number_input("Gold / SIP (₹)", min_value=0, value=st.session_state.gold_inv, step=100)
            st.session_state.rd_inv     = st.number_input("RD / FD (₹)", min_value=0, value=st.session_state.rd_inv, step=100)
        with c2:
            st.session_state.mutual_fund   = st.number_input("Mutual funds (₹)", min_value=0, value=st.session_state.mutual_fund, step=100)
            st.session_state.emergency_add = st.number_input("Added to emergency fund (₹)", min_value=0, value=st.session_state.emergency_add, step=100)
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('<div class="neo-card">', unsafe_allow_html=True)
        st.markdown('<div class="sec-title">🛟 Emergency Vault — current balance?</div>', unsafe_allow_html=True)
        st.session_state.current_ef_saved = st.number_input("Current emergency fund balance (₹)", min_value=0, value=st.session_state.current_ef_saved, step=500)
        st.markdown('</div>', unsafe_allow_html=True)

    elif step == 3:
        st.markdown('<div class="neo-card">', unsafe_allow_html=True)
        st.markdown('<div class="sec-title">🎯 What quests are you chasing?</div>', unsafe_allow_html=True)
        st.markdown('<div class="sec-sub">These targets power your alerts and level score.</div>', unsafe_allow_html=True)
        st.session_state.savings_goal_pct = st.slider("Target savings rate (% of salary)", 5, 50, st.session_state.savings_goal_pct, step=5)
        st.session_state.emergency_months = st.slider("Emergency fund target (months of fixed needs)", 1, 12, st.session_state.emergency_months)
        st.markdown('</div>', unsafe_allow_html=True)

    elif step == 4:
        s = st.session_state
        fixed_total  = s.rent + s.groceries_fix + s.transport_fix + s.utilities + s.phone + s.grooming + s.other_fixed
        invest_total = s.gold_inv + s.rd_inv + s.mutual_fund + s.emergency_add
        free         = s.salary - fixed_total - invest_total
        st.markdown('<div class="neo-card glow-gold">', unsafe_allow_html=True)
        st.markdown('<div class="sec-title">✅ Your character sheet is ready</div>', unsafe_allow_html=True)
        st.markdown('<div class="sec-sub">Looks right? Begin the quest. Everything can be changed later.</div>', unsafe_allow_html=True)
        r1, r2, r3, r4 = st.columns(4)
        with r1: st.markdown(stat_pill("Salary",         fmt_inr(s.salary)),       unsafe_allow_html=True)
        with r2: st.markdown(stat_pill("Fixed Needs",    fmt_inr(fixed_total),  color=C['teal']),     unsafe_allow_html=True)
        with r3: st.markdown(stat_pill("Invested",       fmt_inr(invest_total), color=C['gold_dk']),  unsafe_allow_html=True)
        with r4: st.markdown(stat_pill("Free to Spend",  fmt_inr(max(free,0)),  color=C['green'] if free >= 0 else C['red']), unsafe_allow_html=True)
        if free < 0:
            st.markdown(warn_banner("critical","🚨","Over-committed!",
                f"Your fixed needs + investments exceed salary by <b>{fmt_inr(abs(free))}</b>. Go back and adjust."), unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    nc1, nc2, nc3 = st.columns([1,1,1])
    with nc1:
        if step > 0 and st.button("← Back", use_container_width=True):
            st.session_state.wiz_step -= 1; st.rerun()
    with nc3:
        if step < 4:
            if st.button("Next →", type="primary", use_container_width=True):
                st.session_state.wiz_step += 1; st.rerun()
        else:
            if st.button("⚔️ Begin the Quest", type="primary", use_container_width=True):
                st.session_state.setup_done = True; st.rerun()

if not st.session_state.setup_done:
    render_wizard()
    st.stop()


# ═══════════════════════════════════════════════════════════════
# SIDEBAR
# ═══════════════════════════════════════════════════════════════
with st.sidebar:
    st.markdown(f"""
    <div class="sb-header">
      <div class="sb-title">⚔️ Salary Quest</div>
      <div class="sb-sub">Your financial adventure log</div>
    </div>""", unsafe_allow_html=True)

    st.markdown('<div class="sb-section">', unsafe_allow_html=True)
    if st.button("⚙️ Edit Character", use_container_width=True):
        st.session_state.setup_done = False
        st.session_state.wiz_step   = 0
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="sb-section"><div class="sb-section-title">📅 Today</div>', unsafe_allow_html=True)
    st.session_state.ref_date = st.date_input("Reference date", value=st.session_state.ref_date, label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)

    with st.expander("🏰 Homestead upkeep"):
        st.session_state.rent          = st.number_input("Rent / EMI ₹",       min_value=0, value=st.session_state.rent,          step=100)
        st.session_state.groceries_fix = st.number_input("Groceries ₹",        min_value=0, value=st.session_state.groceries_fix, step=100)
        st.session_state.transport_fix = st.number_input("Transport ₹",        min_value=0, value=st.session_state.transport_fix, step=50)
        st.session_state.utilities     = st.number_input("Utilities ₹",        min_value=0, value=st.session_state.utilities,     step=50)
        st.session_state.phone         = st.number_input("Phone/Internet ₹",   min_value=0, value=st.session_state.phone,         step=50)
        st.session_state.grooming      = st.number_input("Grooming ₹",         min_value=0, value=st.session_state.grooming,      step=50)
        st.session_state.other_fixed   = st.number_input("Other fixed ₹",      min_value=0, value=st.session_state.other_fixed,   step=100)

    with st.expander("💎 Vault & investments"):
        st.session_state.gold_inv        = st.number_input("Gold / SIP ₹",     min_value=0, value=st.session_state.gold_inv,        step=100)
        st.session_state.rd_inv          = st.number_input("RD / FD ₹",        min_value=0, value=st.session_state.rd_inv,          step=100)
        st.session_state.mutual_fund     = st.number_input("Mutual fund ₹",    min_value=0, value=st.session_state.mutual_fund,     step=100)
        st.session_state.emergency_add   = st.number_input("Emergency add ₹",  min_value=0, value=st.session_state.emergency_add,   step=100)
        st.session_state.current_ef_saved = st.number_input("Current EF ₹",   min_value=0, value=st.session_state.current_ef_saved, step=500)

    with st.expander("🎯 Quest goals"):
        st.session_state.salary            = st.number_input("Monthly salary ₹", min_value=0, value=st.session_state.salary, step=500)
        st.session_state.savings_goal_pct  = st.slider("Target savings %",   5, 50, st.session_state.savings_goal_pct, step=5)
        st.session_state.emergency_months  = st.slider("EF target (months)", 1, 12, st.session_state.emergency_months)

    st.markdown(f"""
    <div style="padding:16px 22px;font-size:11.5px;color:{C['text3']};line-height:1.7;font-weight:600">
      🗓 {st.session_state.ref_date.strftime('%B %Y')} ·
      {calendar.monthrange(st.session_state.ref_date.year, st.session_state.ref_date.month)[1]} days<br>
      📍 Day {st.session_state.ref_date.day} of the month
    </div>""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
# PULL STATE
# ═══════════════════════════════════════════════════════════════
today    = st.session_state.ref_date
salary   = st.session_state.salary
rent     = st.session_state.rent
groceries_fix  = st.session_state.groceries_fix
transport_fix  = st.session_state.transport_fix
utilities      = st.session_state.utilities
phone          = st.session_state.phone
grooming       = st.session_state.grooming
other_fixed    = st.session_state.other_fixed
gold_inv       = st.session_state.gold_inv
rd_inv         = st.session_state.rd_inv
mutual_fund    = st.session_state.mutual_fund
emergency_add  = st.session_state.emergency_add
savings_goal_pct  = st.session_state.savings_goal_pct
emergency_months  = st.session_state.emergency_months
current_ef_saved  = st.session_state.current_ef_saved


# ═══════════════════════════════════════════════════════════════
# CALCULATIONS
# ═══════════════════════════════════════════════════════════════
fixed_needs  = rent + groceries_fix + transport_fix + utilities + phone + grooming + other_fixed
total_invest = gold_inv + rd_inv + mutual_fund + emergency_add
total_fixed  = fixed_needs + total_invest
daily_total  = sum(i["Amount"] for i in st.session_state.expenses)
balance      = salary - total_fixed - daily_total
total_spent  = fixed_needs + daily_total

days_in_month  = calendar.monthrange(today.year, today.month)[1]
days_elapsed   = max(today.day, 1)
days_remaining = max(days_in_month - today.day + 1, 1)
month_progress = (today.day / days_in_month) * 100

safe_daily  = balance / days_remaining if days_remaining > 0 else 0
safe_weekly = safe_daily * 7

spent_today = sum(i["Amount"] for i in st.session_state.expenses if i["Date"] == today)
left_today  = max(safe_daily - spent_today, 0)

total_saved = total_invest + max(balance, 0)
saving_pct  = (total_saved / salary * 100) if salary > 0 else 0
invest_pct  = (total_invest / salary * 100) if salary > 0 else 0

need_consumed = fixed_needs + sum(i["Amount"] for i in st.session_state.expenses if i["Type"] == "Need")
want_consumed = sum(i["Amount"] for i in st.session_state.expenses if i["Type"] == "Want")
need_pct = (need_consumed / salary * 100) if salary > 0 else 0
want_pct = (want_consumed / salary * 100) if salary > 0 else 0

avg_daily_var  = daily_total / days_elapsed
proj_var_total = avg_daily_var * days_in_month
proj_balance   = salary - total_fixed - proj_var_total
proj_saved     = total_invest + max(proj_balance, 0)
proj_save_pct  = (proj_saved / salary * 100) if salary > 0 else 0

ef_target = fixed_needs * emergency_months
ef_gap    = max(ef_target - current_ef_saved, 0)
ef_pct    = min(100, (current_ef_saved / ef_target * 100)) if ef_target > 0 else 100

cat_totals, pay_totals = {}, {}
for exp in st.session_state.expenses:
    cat_totals[exp["Category"]] = cat_totals.get(exp["Category"], 0) + exp["Amount"]
    pay_totals[exp["Payment"]]  = pay_totals.get(exp["Payment"], 0)  + exp["Amount"]

sav_component  = min(100, (saving_pct / savings_goal_pct * 100)) if savings_goal_pct > 0 else 100
need_component = 100 if need_pct <= 50 else max(0, 100 - (need_pct - 50) * 2.5)
want_component = 100 if want_pct <= 30 else max(0, 100 - (want_pct - 30) * 3.0)
ef_component   = ef_pct
balance_penalty = 40 if balance < 0 else 0
score = round(sav_component*0.35 + need_component*0.2 + want_component*0.2 + ef_component*0.25) - balance_penalty
score = max(0, min(100, score))
health_color = C['green'] if score >= 75 else C['orange'] if score >= 50 else C['red']
health_label = "Excellent" if score >= 80 else "Good" if score >= 60 else "Fair" if score >= 40 else "Needs attention"
level_icon, level_title, level_sub = get_level(score)[1], get_level(score)[2], get_level(score)[3]


# ═══════════════════════════════════════════════════════════════
# MAIN PAGE
# ═══════════════════════════════════════════════════════════════
st.markdown(f"""
<div class="page-header">
  <div class="page-badge">⚔️ Quest Log · {today.strftime('%B %Y')}</div>
  <div class="page-title">Salary <span>Quest</span></div>
  <div class="page-sub">Track every coin · Know your safe spending limit · Level up your wealth, month by month</div>
</div>""", unsafe_allow_html=True)

if salary > 0:
    st.markdown(f"""
    <div class="level-badge" style="margin-bottom:22px">
      <div class="lvl-icon">{level_icon}</div>
      <div>
        <div class="lvl-title">{level_title} &nbsp;·&nbsp; Level Score {score}/100</div>
        <div class="lvl-sub">{level_sub}</div>
      </div>
    </div>""", unsafe_allow_html=True)

tab_dash, tab_add, tab_expenses, tab_insights, tab_tips = st.tabs([
    "📊 Quest Log", "➕ Log Encounter", "🎒 Inventory", "📈 Chronicle", "📜 Grimoire"
])


# ══════════════════════════════════════════════════════
# TAB 1 — DASHBOARD
# ══════════════════════════════════════════════════════
with tab_dash:
    if salary == 0:
        st.info("Open ⚙️ Edit Character in the sidebar to enter your salary.")
    else:
        k1, k2, k3, k4, k5 = st.columns(5)
        with k1: st.markdown(stat_pill("Monthly Salary",  fmt_inr(salary),      "your take-home"),                            unsafe_allow_html=True)
        with k2: st.markdown(stat_pill("Fixed Needs",     fmt_inr(fixed_needs), f"{fixed_needs/salary*100:.0f}% of salary",   C['teal']),    unsafe_allow_html=True)
        with k3: st.markdown(stat_pill("Invested",        fmt_inr(total_invest),f"{invest_pct:.0f}% of salary",              C['gold_dk']), unsafe_allow_html=True)
        with k4: st.markdown(stat_pill("Variable Spent",  fmt_inr(daily_total), f"{daily_total/salary*100:.0f}% of salary",  C['orange']),  unsafe_allow_html=True)
        with k5:
            bc = C['green'] if balance >= 0 else C['red']
            st.markdown(stat_pill("Free Balance", fmt_inr(balance), "uncommitted gold", bc), unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        left_col, mid_col, right_col = st.columns([1, 2, 1.3])

        with left_col:
            st.markdown('<div class="neo-card" style="text-align:center;padding:22px 14px">', unsafe_allow_html=True)
            st.markdown('<div class="sec-title" style="text-align:center">💎 Savings Rate</div>', unsafe_allow_html=True)
            st.markdown(savings_gauge_svg(saving_pct), unsafe_allow_html=True)
            tc = "tag-green" if saving_pct >= savings_goal_pct else "tag-yellow"
            st.markdown(f'<div style="text-align:center;margin-top:6px"><span class="tag {tc}">Goal: {savings_goal_pct}%</span></div>', unsafe_allow_html=True)
            st.markdown(f"""
            <div style="margin-top:14px;font-size:12.5px;color:{C['text3']};line-height:2;font-weight:600">
              Invested: <b style="color:{C['gold_dk']}">{fmt_inr(total_invest)}</b><br>
              Free: <b style="color:{C['green']}">{fmt_inr(max(balance,0))}</b>
            </div>""", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with mid_col:
            st.markdown('<div class="neo-card">', unsafe_allow_html=True)
            st.markdown('<div class="sec-title">📦 Salary Breakdown</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="sec-sub">How your ₹{salary:,} is allocated this month</div>', unsafe_allow_html=True)
            items = [
                ("🏠 Rent / EMI",          rent,               C['teal']),
                ("🛒 Groceries (fixed)",   groceries_fix,      C['teal']),
                ("🚌 Transport pass",      transport_fix,      C['teal']),
                ("📱 Bills & Utilities",   utilities+phone,    C['teal']),
                ("✂️ Grooming",            grooming,           C['teal']),
                ("📌 Other Fixed",         other_fixed,        C['teal']),
                ("💛 Gold / SIP",          gold_inv,           C['gold_dk']),
                ("📈 RD / FD",             rd_inv,             C['gold_dk']),
                ("📊 Mutual Fund",         mutual_fund,        C['gold_dk']),
                ("🛟 Emergency Fund",      emergency_add,      C['gold_dk']),
                ("🍛 Variable Expenses",   daily_total,        C['orange']),
                ("✅ Free Balance",        max(balance, 0),    C['green']),
            ]
            for label, amt, col in items:
                if amt <= 0: continue
                pct = amt / salary * 100
                st.markdown(f'<div class="bk-row"><span class="bk-label">{label}</span>'
                            f'<span style="display:flex;align-items:center;gap:10px">'
                            f'<span style="font-size:11px;color:{C["text3"]};font-weight:700">{pct:.1f}%</span>'
                            f'<span class="bk-val" style="color:{col}">{fmt_inr(amt)}</span>'
                            f'</span></div>', unsafe_allow_html=True)
            bar_cats   = {"Needs": fixed_needs, "Invest": total_invest, "Spent": daily_total, "Free": max(balance,0)}
            bar_colors = [C['teal'], C['gold'], C['orange'], C['green']]
            total_bar  = sum(bar_cats.values())
            segs = legend = ""
            for (cat, amt), col in zip(bar_cats.items(), bar_colors):
                if amt > 0 and total_bar > 0:
                    w = amt / total_bar * 100
                    segs   += f'<div title="{cat}: {fmt_inr(amt)}" style="width:{w:.1f}%;background:{col};height:100%"></div>'
                    legend += f'<span style="font-size:11px;color:{C["text3"]};font-weight:700">● <span style="color:{col}">{cat}</span></span>'
            st.markdown(f"""
            <div style="margin-top:18px">
              <div style="font-size:11px;color:{C['text3']};margin-bottom:7px;font-weight:800;text-transform:uppercase;letter-spacing:.06em">Visual split</div>
              <div style="display:flex;height:14px;border-radius:99px;overflow:hidden;box-shadow:inset 2px 2px 5px {C['neo_dark']},inset -2px -2px 5px {C['neo_light']}">{segs}</div>
              <div style="display:flex;gap:14px;margin-top:10px;flex-wrap:wrap">{legend}</div>
            </div>""", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with right_col:
            st.markdown('<div class="neo-card">', unsafe_allow_html=True)
            st.markdown('<div class="sec-title">📅 Today\'s Quest Budget</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="sec-sub">{today.strftime("%A, %d %B")}</div>', unsafe_allow_html=True)
            st.markdown(f"""
            <div class="hero-stat" style="margin:14px 0">
              <div class="hs-label">Safe to Spend Today</div>
              <div class="hs-value">{fmt_inr(safe_daily)}</div>
              <div class="hs-sub">per day · {days_remaining} days left</div>
            </div>""", unsafe_allow_html=True)
            today_pct = (spent_today / safe_daily * 100) if safe_daily > 0 else 0
            t_color   = C['red'] if today_pct >= 100 else C['orange'] if today_pct >= 80 else C['green']
            st.markdown(progress_html(f"Spent: {fmt_inr(spent_today)}", f"{today_pct:.0f}%", today_pct, t_color, f"Remaining: {fmt_inr(left_today)}"), unsafe_allow_html=True)
            st.markdown(progress_html(f"Month: Day {today.day}", f"{month_progress:.0f}%", month_progress, C['primary'], f"{days_remaining} days remaining"), unsafe_allow_html=True)
            st.markdown(f"""
            <div style="margin-top:14px">
              <div class="bk-row"><span class="bk-label">Safe Weekly</span><span class="bk-val">{fmt_inr(safe_weekly)}</span></div>
              <div class="bk-row"><span class="bk-label">Projected Balance</span><span class="bk-val" style="color:{C['red'] if proj_balance<0 else C['green']}">{fmt_inr(proj_balance)}</span></div>
              <div class="bk-row"><span class="bk-label">Projected Save %</span><span class="bk-val">{proj_save_pct:.1f}%</span></div>
              <div class="bk-row"><span class="bk-label">Level Score</span><span class="bk-val" style="color:{health_color}">{score}/100 · {health_label}</span></div>
            </div>""", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        # 50/30/20
        st.markdown('<div class="neo-card">', unsafe_allow_html=True)
        st.markdown('<div class="sec-title">🎯 50 / 30 / 20 Rule Benchmark</div>', unsafe_allow_html=True)
        st.markdown('<div class="sec-sub">Needs ≤50% · Wants ≤30% · Savings ≥20%</div>', unsafe_allow_html=True)
        b1, b2, b3 = st.columns(3)
        with b1:
            nc = C['red'] if need_pct > 50 else C['orange'] if need_pct > 40 else C['green']
            st.markdown(progress_html("Needs", f"{need_pct:.1f}% / 50%", need_pct/50*100, nc, f"{fmt_inr(need_consumed)} consumed"), unsafe_allow_html=True)
        with b2:
            wc = C['red'] if want_pct > 30 else C['orange'] if want_pct > 20 else C['green']
            st.markdown(progress_html("Wants", f"{want_pct:.1f}% / 30%", want_pct/30*100, wc, f"{fmt_inr(want_consumed)} on wants"), unsafe_allow_html=True)
        with b3:
            sc = C['green'] if saving_pct >= savings_goal_pct else C['orange'] if saving_pct >= 10 else C['red']
            st.markdown(progress_html("Savings", f"{saving_pct:.1f}% / {savings_goal_pct}%", saving_pct/savings_goal_pct*100, sc, f"{fmt_inr(total_saved)} secured"), unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # Emergency Vault
        st.markdown('<div class="neo-card">', unsafe_allow_html=True)
        st.markdown('<div class="sec-title">🛟 Emergency Vault</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="sec-sub">Target: {emergency_months} months of fixed needs = {fmt_inr(ef_target)}</div>', unsafe_allow_html=True)
        ef_col = C['green'] if ef_pct >= 100 else C['orange'] if ef_pct >= 50 else C['red']
        st.markdown(progress_html(f"Saved: {fmt_inr(current_ef_saved)}", f"{ef_pct:.0f}%", ef_pct, ef_col,
                                   "Fully funded 🎉" if ef_gap == 0 else f"{fmt_inr(ef_gap)} more needed"), unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # Quest Alerts
        alerts = []
        if balance < 0:
            alerts.append(("danger","🚨", f"You've overcommitted {fmt_inr(abs(balance))} beyond your salary! Cut all wants immediately."))
        if safe_daily < 150:
            alerts.append(("warning","⚠️", f"Tight budget — only {fmt_inr(safe_daily)}/day left. Prioritize needs only."))
        if want_pct > 30:
            alerts.append(("warning","🛑", f"Wants are at {want_pct:.0f}% of salary (guideline: ≤30%). Cut discretionary spending."))
        if saving_pct >= savings_goal_pct:
            alerts.append(("success","✅", f"Savings goal of {savings_goal_pct}% achieved — you're at {saving_pct:.1f}%."))
        elif saving_pct >= 20:
            alerts.append(("success","👍", f"Healthy savings at {saving_pct:.1f}%."))
        if proj_balance < balance * 0.7 and days_elapsed > 5:
            alerts.append(("warning","📉", f"At current pace, projected month-end balance is {fmt_inr(proj_balance)}."))
        if ef_gap > 0:
            alerts.append(("info","🛟", f"Emergency vault gap: {fmt_inr(ef_gap)} more needed for a {emergency_months}-month cushion."))
        if not alerts:
            alerts.append(("info","💡","Keep tracking daily — consistency is the key to leveling up."))
        st.markdown('<div class="neo-card">', unsafe_allow_html=True)
        st.markdown('<div class="sec-title">🔔 Quest Alerts</div>', unsafe_allow_html=True)
        for atype, icon, msg in alerts:
            st.markdown(f'<div class="alert-strip {atype}">{icon}&nbsp; {msg}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════
# TAB 2 — LOG ENCOUNTER  ← FULLY REBUILT WITH LIVE WARNINGS
# ══════════════════════════════════════════════════════
with tab_add:

    # ── TOP STATUS STRIP ────────────────────────────────────────
    if salary > 0:
        today_pct_top = (spent_today / safe_daily * 100) if safe_daily > 0 else 0

        # Choose banner level based on today's status
        if safe_daily <= 0 or balance <= 0:
            top_level, top_icon = "critical", "🚨"
            top_title = "Budget Exhausted — No Safe Spending Left!"
            top_body  = (f"Your free balance is <b>{fmt_inr(balance)}</b>. "
                         f"Every rupee spent now comes at the cost of your savings or pushes you into deficit. "
                         f"Only spend on absolute essentials.")
        elif today_pct_top >= 100:
            top_level, top_icon = "critical", "🔴"
            top_title = f"Today's Daily Limit Breached!"
            top_body  = (f"You've spent <b>{fmt_inr(spent_today)}</b> today against a safe limit of "
                         f"<b>{fmt_inr(safe_daily)}</b>. "
                         f"You are <b>{fmt_inr(spent_today - safe_daily)}</b> over — tomorrow's budget will shrink to compensate.")
        elif today_pct_top >= 80:
            top_level, top_icon = "caution", "🟡"
            top_title = "Caution — Approaching Today's Limit"
            top_body  = (f"You've used <b>{today_pct_top:.0f}%</b> of today's budget. "
                         f"Only <b>{fmt_inr(left_today)}</b> remains for the rest of today. "
                         f"Think before every purchase.")
        elif today_pct_top >= 50:
            top_level, top_icon = "caution", "🟠"
            top_title = "Halfway Through Today's Budget"
            top_body  = (f"Spent <b>{fmt_inr(spent_today)}</b> of <b>{fmt_inr(safe_daily)}</b> today. "
                         f"<b>{fmt_inr(left_today)}</b> left — you're on track if you slow down a bit.")
        else:
            top_level, top_icon = "safe", "🟢"
            top_title = "You're on Track Today!"
            top_body  = (f"Only <b>{fmt_inr(spent_today)}</b> spent so far out of <b>{fmt_inr(safe_daily)}</b> daily budget. "
                         f"<b>{fmt_inr(left_today)}</b> still available — keep it up!")

        st.markdown(warn_banner(top_level, top_icon, top_title, top_body), unsafe_allow_html=True)

        # Budget meter bar
        meter_color = C['red'] if today_pct_top >= 100 else C['orange'] if today_pct_top >= 80 else C['green']
        st.markdown(budget_meter_html(spent_today, safe_daily, meter_color, "Today's Budget Meter"), unsafe_allow_html=True)

        # Three KPI pills
        q1, q2, q3 = st.columns(3)
        with q1:
            st.markdown(f"""
            <div class="hero-stat">
              <div class="hs-label">Safe to Spend Today</div>
              <div class="hs-value" style="font-size:30px">{fmt_inr(safe_daily)}</div>
              <div class="hs-sub">{days_remaining} days remaining in month</div>
            </div>""", unsafe_allow_html=True)
        with q2:
            spent_color = C['red'] if spent_today > safe_daily else C['orange'] if spent_today > safe_daily*0.8 else C['text']
            st.markdown(stat_pill("Spent Today", fmt_inr(spent_today),
                                   f"{today_pct_top:.0f}% of daily limit",
                                   spent_color), unsafe_allow_html=True)
        with q3:
            bc = C['green'] if balance >= 0 else C['red']
            st.markdown(stat_pill("Month Free Balance", fmt_inr(balance),
                                   f"÷ {days_remaining} days = {fmt_inr(safe_daily)}/day",
                                   bc), unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # Monthly health strip
        mc1, mc2, mc3, mc4 = st.columns(4)
        with mc1: st.markdown(stat_pill("Monthly Spent",     fmt_inr(daily_total),       f"{daily_total/salary*100:.0f}% of salary",    C['orange']), unsafe_allow_html=True)
        with mc2: st.markdown(stat_pill("Projected Balance", fmt_inr(proj_balance),       "at month end",                                C['green'] if proj_balance>=0 else C['red']), unsafe_allow_html=True)
        with mc3: st.markdown(stat_pill("Projected Savings", f"{proj_save_pct:.1f}%",    f"goal: {savings_goal_pct}%",                  C['green'] if proj_save_pct>=savings_goal_pct else C['orange']), unsafe_allow_html=True)
        with mc4: st.markdown(stat_pill("Level Score",       f"{score}/100",              health_label,                                  health_color), unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

    # ── QUICK ADD ───────────────────────────────────────────────
    st.markdown('<div class="neo-card">', unsafe_allow_html=True)
    st.markdown('<div class="sec-title">⚡ Quick Encounter</div>', unsafe_allow_html=True)
    st.markdown('<div class="sec-sub">One tap for the small daily skirmishes</div>', unsafe_allow_html=True)
    qcols = st.columns(len(QUICK_ADD_PRESETS))
    for col, (label, cat, amt, typ) in zip(qcols, QUICK_ADD_PRESETS):
        with col:
            if st.button(f"{CATEGORY_ICONS.get(cat,'📌')} {label}\n{fmt_inr(amt)}", key=f"qa_{label}", use_container_width=True):
                st.session_state.expenses.append({
                    "Date": today, "Place": label, "Amount": float(amt),
                    "Payment": "UPI", "Category": cat, "Type": typ, "Note": "Quick add",
                })
                st.toast(f"✅ Logged {fmt_inr(amt)} for {label}")
                st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    # ── MAIN FORM ───────────────────────────────────────────────
    st.markdown('<div class="neo-card">', unsafe_allow_html=True)
    st.markdown('<div class="sec-title">➕ Log an Encounter</div>', unsafe_allow_html=True)
    st.markdown('<div class="sec-sub">Every entry sharpens your picture of where your gold flows</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        place    = st.text_input("📍 Where did you spend?", placeholder="e.g. Swiggy, Petrol bunk, Cafe Coffee Day")
        amount   = st.number_input("💸 Amount (₹)", min_value=0.0, value=0.0, step=10.0, format="%.2f")
        exp_date = st.date_input("📅 Date", value=today)
    with col2:
        category  = st.selectbox("🏷️ Category", list(CATEGORY_ICONS.keys()), format_func=lambda x: f"{CATEGORY_ICONS[x]} {x}")
        payment   = st.radio("💳 Payment Method", list(PAYMENT_ICONS.keys()), format_func=lambda x: f"{PAYMENT_ICONS[x]} {x}", horizontal=True)
        need_want = st.radio("🎯 Need or Want?", ["Need", "Want"], horizontal=True)

    note = st.text_input("📝 Note (optional)", placeholder="e.g. with friends, office lunch")

    # ── LIVE IMPACT PREVIEW (shows as soon as amount > 0) ───────
    if amount > 0 and salary > 0:
        new_spent_today   = spent_today + amount
        new_left_today    = safe_daily - new_spent_today
        new_balance       = balance - amount
        new_daily_total   = daily_total + amount
        new_safe_daily    = new_balance / days_remaining if days_remaining > 0 else 0
        new_today_pct     = (new_spent_today / safe_daily * 100) if safe_daily > 0 else 100
        new_saving_pct    = ((total_invest + max(new_balance, 0)) / salary * 100) if salary > 0 else 0
        new_proj_var      = (new_daily_total / days_elapsed) * days_in_month
        new_proj_balance  = salary - total_fixed - new_proj_var
        new_proj_save_pct = ((total_invest + max(new_proj_balance,0)) / salary * 100) if salary > 0 else 0

        # Choose warning level for the amount being entered
        if new_balance < 0:
            wlevel, wicon = "critical", "🚨"
            wtitle = f"DANGER: This {fmt_inr(amount)} will push you into deficit!"
            wbody  = (f"Your free balance will drop to <b style='color:{C['red']}'>{fmt_inr(new_balance)}</b>. "
                      f"You will be spending beyond your salary. "
                      f"This will reduce tomorrow's budget to <b>{fmt_inr(max(new_safe_daily,0))}/day</b>.")
        elif new_left_today < 0:
            wlevel, wicon = "critical", "🔴"
            wtitle = f"Over Daily Limit by {fmt_inr(abs(new_left_today))}!"
            wbody  = (f"Adding <b>{fmt_inr(amount)}</b> today means you've spent <b>{fmt_inr(new_spent_today)}</b> "
                      f"against a safe limit of <b>{fmt_inr(safe_daily)}</b>. "
                      f"Tomorrow's limit will shrink. New daily budget after this: <b>{fmt_inr(max(new_safe_daily,0))}/day</b>.")
        elif new_today_pct >= 80:
            wlevel, wicon = "caution", "⚠️"
            wtitle = f"Caution — This takes you to {new_today_pct:.0f}% of today's budget"
            wbody  = (f"After adding <b>{fmt_inr(amount)}</b>, only <b>{fmt_inr(max(new_left_today,0))}</b> "
                      f"will remain for today. Remaining month balance: <b>{fmt_inr(new_balance)}</b>.")
        elif new_saving_pct < savings_goal_pct and saving_pct >= savings_goal_pct:
            wlevel, wicon = "caution", "📉"
            wtitle = "This spend will drop you below your savings goal!"
            wbody  = (f"Your savings rate will slip from <b>{saving_pct:.1f}%</b> to <b>{new_saving_pct:.1f}%</b> "
                      f"(goal: {savings_goal_pct}%). Consider if this is really necessary.")
        else:
            wlevel, wicon = "safe", "✅"
            wtitle = f"Looks Good — {fmt_inr(amount)} is within your budget"
            wbody  = (f"After this, <b>{fmt_inr(max(new_left_today,0))}</b> remains for today. "
                      f"Month balance: <b>{fmt_inr(new_balance)}</b>. "
                      f"New daily budget: <b>{fmt_inr(new_safe_daily)}/day</b>.")

        st.markdown(warn_banner(wlevel, wicon, wtitle, wbody), unsafe_allow_html=True)

        # Live impact preview card
        pc = "has-amount"
        st.markdown(f'<div class="preview-card {pc}">', unsafe_allow_html=True)
        st.markdown(f'<div style="font-size:11px;font-weight:800;text-transform:uppercase;letter-spacing:.07em;color:{C["text3"]};margin-bottom:10px">📊 Live Impact Preview</div>', unsafe_allow_html=True)

        rows = [
            ("Spent Today (before)", fmt_inr(spent_today),   C['text2']),
            ("+ This Expense",       fmt_inr(amount),         C['orange']),
            ("Spent Today (after)",  fmt_inr(new_spent_today), C['red'] if new_today_pct >= 100 else C['orange'] if new_today_pct >= 80 else C['green']),
            ("Today's Budget Left",  fmt_inr(max(new_left_today,0)), C['red'] if new_left_today < 0 else C['orange'] if new_left_today < safe_daily*0.2 else C['green']),
            ("Month Balance (after)",fmt_inr(new_balance),    C['red'] if new_balance < 0 else C['green']),
            ("New Daily Budget",     fmt_inr(max(new_safe_daily,0)), C['red'] if new_safe_daily < 100 else C['orange'] if new_safe_daily < 200 else C['green']),
            ("Savings Rate (after)", f"{new_saving_pct:.1f}%",C['red'] if new_saving_pct < savings_goal_pct*0.5 else C['orange'] if new_saving_pct < savings_goal_pct else C['green']),
            ("Projected Save % EOM", f"{new_proj_save_pct:.1f}%", C['green'] if new_proj_save_pct >= savings_goal_pct else C['orange']),
        ]
        for lbl, val, col in rows:
            st.markdown(f'<div class="preview-row"><span class="preview-lbl">{lbl}</span>'
                        f'<span class="preview-val" style="color:{col}">{val}</span></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # Want-specific extra warning
        if need_want == "Want":
            want_after     = want_consumed + amount
            want_pct_after = (want_after / salary * 100) if salary > 0 else 0
            if want_pct_after > 30:
                st.markdown(warn_banner("caution","🛑",
                    f"Wants will reach {want_pct_after:.0f}% of salary (limit: 30%)",
                    f"The 50/30/20 rule recommends keeping wants under 30%. "
                    f"After this, wants total <b>{fmt_inr(want_after)}</b>. "
                    f"Consider skipping or deferring this."), unsafe_allow_html=True)
            elif want_pct_after > 25:
                st.markdown(warn_banner("info-blue","💡",
                    f"Wants approaching 30% limit ({want_pct_after:.0f}%)",
                    f"You'll have <b>{fmt_inr(want_after)}</b> in want spending this month. "
                    f"You have {fmt_inr(salary*0.30 - want_after)} left in your wants budget."), unsafe_allow_html=True)

    # ── ADD BUTTON ───────────────────────────────────────────────
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("➕ Add Expense", type="primary"):
        if not place.strip():
            st.error("Please enter where you spent.")
        elif amount <= 0:
            st.error("Amount must be greater than ₹0.")
        else:
            st.session_state.expenses.append({
                "Date": exp_date, "Place": place.strip(), "Amount": float(amount),
                "Payment": payment, "Category": category,
                "Type": need_want, "Note": note.strip(),
            })
            # Post-add warning toast
            new_bal = salary - total_fixed - (daily_total + amount)
            new_sd  = new_bal / days_remaining if days_remaining > 0 else 0
            if new_bal < 0:
                st.error(f"🚨 Logged! But your month balance is now {fmt_inr(new_bal)} — you're in deficit!")
            elif new_sd < 100:
                st.warning(f"⚠️ Logged! Only {fmt_inr(new_sd)}/day safe budget remains — spend very carefully.")
            else:
                st.success(f"✅ Logged {fmt_inr(amount)} at {place.strip()} — {fmt_inr(new_sd)}/day left in daily budget.")
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    # ── RECENT ENTRIES ───────────────────────────────────────────
    if st.session_state.expenses:
        recent = list(reversed(st.session_state.expenses[-6:]))
        st.markdown('<div class="neo-card">', unsafe_allow_html=True)
        st.markdown('<div class="sec-title">🕐 Recent Encounters</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="sec-sub">Last {len(recent)} logged expenses</div>', unsafe_allow_html=True)
        for exp in recent:
            icon  = CATEGORY_ICONS.get(exp["Category"], "📌")
            b_cls = "badge-need" if exp["Type"] == "Need" else "badge-want"
            note_str = f" · {exp['Note']}" if exp.get("Note") else ""
            is_today_exp = exp["Date"] == today
            highlight = f'border-left: 3px solid {C["primary"]}; padding-left: 10px;' if is_today_exp else ''
            st.markdown(f"""
            <div class="exp-row" style="{highlight}">
              <div class="exp-icon">{icon}</div>
              <div class="exp-info">
                <div class="exp-place">{exp['Place']}
                  {'<span style="font-size:10px;background:'+C['primary_bg']+';color:'+C['primary']+';border-radius:99px;padding:2px 8px;margin-left:6px;font-weight:800">TODAY</span>' if is_today_exp else ''}
                </div>
                <div class="exp-meta">{PAYMENT_ICONS.get(exp['Payment'],'💳')} {exp['Payment']} · {exp['Category']}{note_str} · {exp['Date']}</div>
              </div>
              <span class="exp-badge {b_cls}">{exp['Type']}</span>
              <span class="exp-amt">{fmt_inr(exp['Amount'])}</span>
            </div>""", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════
# TAB 3 — INVENTORY
# ══════════════════════════════════════════════════════
with tab_expenses:
    if not st.session_state.expenses:
        st.markdown(f"""
        <div class="neo-card" style="text-align:center;padding:60px 24px">
          <div style="font-size:48px;margin-bottom:14px">🎒</div>
          <div class="sec-title">Your inventory is empty</div>
          <div class="sec-sub">Head to "Log Encounter" to start tracking</div>
        </div>""", unsafe_allow_html=True)
    else:
        s1, s2, s3, s4 = st.columns(4)
        with s1: st.markdown(stat_pill("Total Entries", str(len(st.session_state.expenses))), unsafe_allow_html=True)
        with s2: st.markdown(stat_pill("Total Spent",   fmt_inr(daily_total),  color=C['orange']), unsafe_allow_html=True)
        with s3: st.markdown(stat_pill("Needs",  fmt_inr(sum(i["Amount"] for i in st.session_state.expenses if i["Type"]=="Need")), color=C['teal']), unsafe_allow_html=True)
        with s4: st.markdown(stat_pill("Wants",  fmt_inr(sum(i["Amount"] for i in st.session_state.expenses if i["Type"]=="Want")), color=C['orange']), unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown('<div class="neo-card">', unsafe_allow_html=True)
        st.markdown('<div class="sec-title">📋 All Encounters</div>', unsafe_allow_html=True)
        f1, f2, f3 = st.columns(3)
        with f1:
            cats     = ["All"] + sorted(set(i["Category"] for i in st.session_state.expenses))
            sel_cat  = st.selectbox("Filter by Category", cats, key="filter_cat")
        with f2:
            sel_type = st.selectbox("Filter by Type", ["All","Need","Want"], key="filter_type")
        with f3:
            pays     = ["All"] + sorted(set(i["Payment"] for i in st.session_state.expenses))
            sel_pay  = st.selectbox("Filter by Payment", pays, key="filter_pay")

        filtered = [e for e in st.session_state.expenses
                    if (sel_cat  == "All" or e["Category"] == sel_cat)
                    and (sel_type == "All" or e["Type"]     == sel_type)
                    and (sel_pay  == "All" or e["Payment"]  == sel_pay)]

        if not filtered:
            st.info("No expenses match the selected filters.")
        else:
            for exp in sorted(filtered, key=lambda x: x["Date"], reverse=True):
                icon    = CATEGORY_ICONS.get(exp["Category"], "📌")
                b_cls   = "badge-need" if exp["Type"] == "Need" else "badge-want"
                note_str = f" · {exp['Note']}" if exp.get("Note") else ""
                st.markdown(f"""
                <div class="exp-row">
                  <div class="exp-icon">{icon}</div>
                  <div class="exp-info">
                    <div class="exp-place">{exp['Place']}</div>
                    <div class="exp-meta">{PAYMENT_ICONS.get(exp['Payment'],'💳')} {exp['Payment']} · {exp['Category']}{note_str} · {exp['Date']}</div>
                  </div>
                  <span class="exp-badge {b_cls}">{exp['Type']}</span>
                  <span class="exp-amt">{fmt_inr(exp['Amount'])}</span>
                </div>""", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

            with st.expander("📊 View as Table"):
                df = pd.DataFrame(sorted(filtered, key=lambda x: x["Date"], reverse=True))[["Date","Place","Amount","Category","Payment","Type","Note"]]
                df["Amount"] = df["Amount"].apply(lambda x: f"₹{x:,.2f}")
                st.dataframe(df, use_container_width=True, hide_index=True)

            if cat_totals:
                st.markdown('<div class="neo-card" style="margin-top:16px">', unsafe_allow_html=True)
                st.markdown('<div class="sec-title">🍕 Category Totals</div>', unsafe_allow_html=True)
                for cat, amt in sorted(cat_totals.items(), key=lambda x: x[1], reverse=True):
                    pct  = amt / daily_total * 100 if daily_total > 0 else 0
                    icon = CATEGORY_ICONS.get(cat, "📌")
                    cb   = C['teal'] if pct < 30 else C['orange'] if pct < 50 else C['red']
                    st.markdown(progress_html(f"{icon} {cat} · {fmt_inr(amt)}", f"{pct:.1f}%", pct, cb), unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="neo-card">', unsafe_allow_html=True)
        st.markdown(f'<div class="sec-title" style="color:{C["red"]}">⚠️ Danger Zone</div>', unsafe_allow_html=True)
        if st.button("🗑 Clear All Expenses"):
            st.session_state.expenses = []
            st.success("All expenses cleared.")
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════
# TAB 4 — INSIGHTS
# ══════════════════════════════════════════════════════
with tab_insights:
    if not st.session_state.expenses or salary == 0:
        st.markdown(f"""
        <div class="neo-card" style="text-align:center;padding:60px 24px">
          <div style="font-size:48px;margin-bottom:14px">📜</div>
          <div class="sec-title">The chronicle is still blank</div>
          <div class="sec-sub">Add at least a few expenses to unlock insights</div>
        </div>""", unsafe_allow_html=True)
    else:
        li, ri = st.columns(2)
        with li:
            st.markdown('<div class="sec-title">📊 Spending by Category</div>', unsafe_allow_html=True)
            chart_df = pd.DataFrame(list(cat_totals.items()), columns=["Category","Amount"])
            st.bar_chart(chart_df.set_index("Category"), color=C['primary'])
        with ri:
            st.markdown('<div class="sec-title">💳 Spending by Payment</div>', unsafe_allow_html=True)
            pay_df = pd.DataFrame(list(pay_totals.items()), columns=["Method","Amount"])
            st.bar_chart(pay_df.set_index("Method"), color=C['teal'])

        st.markdown('<div class="sec-title" style="margin-top:8px">📅 Daily Spending Trend</div>', unsafe_allow_html=True)
        ddf = pd.DataFrame(st.session_state.expenses)
        ddf["Date"] = pd.to_datetime(ddf["Date"])
        dg = ddf.groupby("Date")["Amount"].sum().reset_index()
        dg["Safe Daily"] = safe_daily
        st.line_chart(dg.set_index("Date")[["Amount","Safe Daily"]])

        st.markdown('<div class="sec-title" style="margin-top:8px">🎯 Need vs Want Trend</div>', unsafe_allow_html=True)
        nw = ddf.groupby(["Date","Type"])["Amount"].sum().unstack(fill_value=0).reset_index()
        if "Need" not in nw.columns: nw["Need"] = 0
        if "Want" not in nw.columns: nw["Want"] = 0
        st.bar_chart(nw.set_index("Date")[["Need","Want"]])

        st.markdown('<div class="neo-card">', unsafe_allow_html=True)
        st.markdown('<div class="sec-title">🔍 Key Insights</div>', unsafe_allow_html=True)
        if cat_totals:
            top_cat     = max(cat_totals, key=cat_totals.get)
            avg_day     = daily_total / days_elapsed
            hday        = ddf.groupby("Date")["Amount"].sum().idxmax()
            hamt        = ddf.groupby("Date")["Amount"].sum().max()
            st.markdown(f"""
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px">
              <div class="neo-card-sm">
                <div style="font-size:11px;color:{C['text3']};text-transform:uppercase;font-weight:800;margin-bottom:6px">Biggest Leak</div>
                <div style="font-size:18px;font-weight:800;color:{C['orange']}">{CATEGORY_ICONS.get(top_cat,'📌')} {top_cat}</div>
                <div style="font-size:13px;color:{C['text2']};margin-top:3px;font-weight:600">{fmt_inr(cat_totals[top_cat])} · {cat_totals[top_cat]/daily_total*100:.0f}% of variable spend</div>
              </div>
              <div class="neo-card-sm">
                <div style="font-size:11px;color:{C['text3']};text-transform:uppercase;font-weight:800;margin-bottom:6px">Avg Daily Spend</div>
                <div style="font-size:18px;font-weight:800;color:{C['primary']}">{fmt_inr(avg_day)}</div>
                <div style="font-size:13px;color:{C['text2']};margin-top:3px;font-weight:600">vs safe budget of {fmt_inr(safe_daily)}</div>
              </div>
              <div class="neo-card-sm">
                <div style="font-size:11px;color:{C['text3']};text-transform:uppercase;font-weight:800;margin-bottom:6px">Highest Spending Day</div>
                <div style="font-size:18px;font-weight:800;color:{C['red']}">{fmt_inr(hamt)}</div>
                <div style="font-size:13px;color:{C['text2']};margin-top:3px;font-weight:600">{hday.strftime('%d %b %Y')}</div>
              </div>
              <div class="neo-card-sm">
                <div style="font-size:11px;color:{C['text3']};text-transform:uppercase;font-weight:800;margin-bottom:6px">Projected Savings</div>
                <div style="font-size:18px;font-weight:800;color:{C['green'] if proj_save_pct>=savings_goal_pct else C['orange']}">{proj_save_pct:.1f}%</div>
                <div style="font-size:13px;color:{C['text2']};margin-top:3px;font-weight:600">at current pace (goal: {savings_goal_pct}%)</div>
              </div>
            </div>""", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════
# TAB 5 — GRIMOIRE
# ══════════════════════════════════════════════════════
with tab_tips:
    st.markdown('<div class="neo-card">', unsafe_allow_html=True)
    st.markdown('<div class="sec-title">📖 How This Realm Works</div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:14px">
      <div class="neo-card-sm"><div style="font-size:22px;margin-bottom:8px">🏰</div>
        <div style="font-size:13.5px;font-weight:800;color:{C['text']}">Homestead Upkeep</div>
        <div style="font-size:12.5px;color:{C['text3']};margin-top:5px;line-height:1.55;font-weight:500">Recurring monthly costs — rent, bills, groceries. Deducted from salary first.</div></div>
      <div class="neo-card-sm"><div style="font-size:22px;margin-bottom:8px">💎</div>
        <div style="font-size:13.5px;font-weight:800;color:{C['text']}">Vault Investments</div>
        <div style="font-size:12.5px;color:{C['text3']};margin-top:5px;line-height:1.55;font-weight:500">Gold, SIP, RD, MF — savings, not expenses. Count toward savings %.</div></div>
      <div class="neo-card-sm"><div style="font-size:22px;margin-bottom:8px">📅</div>
        <div style="font-size:13.5px;font-weight:800;color:{C['text']}">Safe Daily Budget</div>
        <div style="font-size:12.5px;color:{C['text3']};margin-top:5px;line-height:1.55;font-weight:500">Free Balance ÷ Days Remaining. Spend below this every day to stay on track.</div></div>
    </div>""", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="neo-card">', unsafe_allow_html=True)
    st.markdown('<div class="sec-title">🎯 Personalised Tips</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="sec-sub">Based on your current numbers for {today.strftime("%B %Y")}</div>', unsafe_allow_html=True)
    if salary > 0:
        pers_tips = []
        if saving_pct < savings_goal_pct:
            gap_amt = (savings_goal_pct - saving_pct) / 100 * salary
            pers_tips.append(("Boost savings by " + fmt_inr(gap_amt),
                f"You need {fmt_inr(gap_amt)} more savings to hit your {savings_goal_pct}% goal. Increase your SIP or RD."))
        if want_pct > 25:
            pers_tips.append(("Reduce want spending",
                f"Wants are {want_pct:.0f}% of salary. Cutting them by 20% saves {fmt_inr(want_consumed*0.2)} this month."))
        if cat_totals and daily_total > 0:
            top_c = max(cat_totals, key=cat_totals.get)
            pers_tips.append((f"Watch your {top_c} spend",
                f"{top_c} is your biggest variable expense at {fmt_inr(cat_totals[top_c])} ({cat_totals[top_c]/daily_total*100:.0f}% of variable spend)."))
        if safe_daily < 300:
            pers_tips.append(("Budget is tight — plan ahead",
                f"Only {fmt_inr(safe_daily)}/day available. Avoid impulse purchases and plan meals/transport in advance."))
        if ef_gap > 0:
            pers_tips.append(("Emergency fund first",
                f"You're {fmt_inr(ef_gap)} short of a {emergency_months}-month emergency fund. Adding {fmt_inr(ef_gap/12)}/month gets you there in a year."))
        if not pers_tips:
            pers_tips.append(("You're doing great!","Your spending is well-balanced. Raise your SIP every time you get a raise."))
        for n, (title, body) in enumerate(pers_tips, 1):
            st.markdown(f'<div class="tip-row"><div class="tip-num">{n:02d}</div><div><div class="tip-title">{title}</div><div class="tip-body">{body}</div></div></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    tip_groups = [
        ("💰 On Salary Day", [
            ("Pay yourself first", f"Transfer your savings ({fmt_inr(total_invest)}/month here) before spending anything."),
            ("Automate investments", "Set up standing instructions for SIP, RD, and gold so saving doesn't depend on willpower."),
        ]),
        ("📅 Daily Habits", [
            ("Check your safe daily budget first", f"Your current limit is {fmt_inr(safe_daily)}. Check it before opening a food-delivery app."),
            ("Tag need vs want honestly", "Chai with colleagues is a Want, not a Need — even if it's routine."),
            ("Log immediately", "Enter expenses right after paying, or you'll forget and lose track."),
        ]),
        ("📆 Weekly Review", [
            ("Use the weekly budget as a checkpoint", f"Your safe weekly budget is {fmt_inr(safe_weekly)}. One expensive day is fine if the week balances out."),
            ("Watch the run-rate projection", "If Projected Balance is declining fast mid-month, course-correct now — not on day 28."),
        ]),
        ("📊 Monthly Reset", [
            ("50/30/20 as a compass, not a cage", "Aim for 50% needs, 30% wants, 20% savings. Use an off month as data for next month."),
            ("Build emergency fund first", f"Ensure you could cover {emergency_months} months of fixed needs ({fmt_inr(ef_target)}) if income stopped."),
            ("Review sidebar numbers monthly", "Update fixed costs and investments regularly — small adjustments compound over time."),
        ]),
        ("📈 Long-term Wealth", [
            ("Avoid lifestyle inflation", "When salary increases, raise your savings % first, then let spending catch up slowly."),
            ("Invest the difference", "When a fixed cost drops, redirect that exact amount to investments — you were living without it anyway."),
        ]),
    ]
    st.markdown('<div class="neo-card">', unsafe_allow_html=True)
    st.markdown('<div class="sec-title">📚 Complete Finance Grimoire</div>', unsafe_allow_html=True)
    counter = 1
    for group_title, tips in tip_groups:
        st.markdown(f'<div class="tip-group-title">{group_title}</div>', unsafe_allow_html=True)
        for title, body in tips:
            st.markdown(f'<div class="tip-row"><div class="tip-num">{counter:02d}</div><div><div class="tip-title">{title}</div><div class="tip-body">{body}</div></div></div>', unsafe_allow_html=True)
            counter += 1
    st.markdown('</div>', unsafe_allow_html=True)