import streamlit as st
from google import genai
from google.genai import types
import pypdf
import io
import webbrowser

# 1. Page Configuration
st.set_page_config(page_title="Chino Study Arena", page_icon="🍃", layout="wide")

# 2. Persistent State
if "xp" not in st.session_state: st.session_state.xp = 82
if "lvl" not in st.session_state: st.session_state.lvl = 4
if "theme" not in st.session_state: st.session_state.theme = "light"

# 3. Dynamic CSS: Complete Dark Mode Overhaul
bg_color = "#0F172A" if st.session_state.theme == "dark" else "#FFFFFF"
text_color = "#F8FAFC" if st.session_state.theme == "dark" else "#1E293B"
card_bg = "#1E293B" if st.session_state.theme == "dark" else "#F8FAFC"
border_color = "rgba(255,255,255,0.1)" if st.session_state.theme == "dark" else "rgba(0,0,0,0.05)"

st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;700&display=swap');
    
    /* Force background change on the whole app */
    .stApp {{
        background-color: {bg_color} !important;
        color: {text_color} !important;
        transition: all 0.5s ease-in-out;
    }}

    * {{ font-family: 'Outfit', sans-serif; }}

    /* Hero Section */
    .hero-container {{
        background: linear-gradient(135deg, #7C3AED 0%, #C1E1C1 100%);
        border-radius: 50px;
        padding: 80px 60px;
        color: white;
        margin-bottom: 40px;
        box-shadow: 0 25px 50px rgba(124, 58, 237, 0.3);
    }}

    .extraordinary-tag {{
        background: #FDE047; color: black; display: inline-block; 
        padding: 5px 25px; border-radius: 12px; transform: rotate(-2deg); 
        font-weight: 800; box-shadow: 4px 4px 0px #000;
    }}

    /* Bouncy Cards */
    .bouncy-card {{
        background: {card_bg};
        border-radius: 35px;
        padding: 30px;
        border: 1px solid {border_color};
        margin-bottom: 25px;
        transition: transform 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
    }}
    .bouncy-card:hover {{
        transform: translateY(-12px) scale(1.02);
        box-shadow: 0 20px 40px rgba(0,0,0,0.2);
    }}

    /* XP Progress Bar */
    .xp-hud {{
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        padding: 20px;
        border-radius: 25px;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }}
    .xp-bar-bg {{ width: 100%; background: rgba(255,255,255,0.2); border-radius: 50px; height: 12px; margin: 10px 0; }}
    .xp-bar-fill {{ height: 100%; background: #FDE047; border-radius: 50px; box-shadow: 0 0 15px #FDE047; }}

    /* Adjusting Streamlit specific elements for Dark Mode */
    .stMarkdown, p, h1, h2, h3 {{ color: {text_color} !important; }}
    .stButton>button {{
        background: #C1E1C1 !important;
        color: #0F172A !important;
        border-radius: 50px !important;
        border: none !important;
        font-weight: 700 !important;
    }}
</style>
""", unsafe_allow_html=True)

# 4. Sidebar: Social Connections & Mode Toggle
with st.sidebar:
    st.markdown("## 🍃 Chino Settings")
    if st.button("🌓 Toggle Dark/Light Mode"):
        st.session_state.theme = "dark" if st.session_state.theme == "light" else "light"
        st.rerun()
    
    st.divider()
    st.markdown("### 🔗 Connect Socials")
    
    # Social Buttons with Real Links
    if st.button("Connect Instagram 📸"):
        webbrowser.open_new_tab("https://www.instagram.com/accounts/login/")
    if st.button("Connect Snapchat 👻"):
        webbrowser.open_new_tab("https://accounts.snapchat.com/")
    if st.button("Connect TikTok 🎵"):
        webbrowser.open_new_tab("https://www.tiktok.com/login")
    if st.button("Connect X / Twitter 🐦"):
        webbrowser.open_new_tab("https://x.com/login")

# 5. Hero & XP HUD
st.markdown(f"""
<div class="hero-container">
    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 20px;">
        <div>
            <h1 style="font-size: 4rem; line-height: 1; margin:0; color:white !important;">Arena of the</h1>
            <div class="extraordinary-tag">EXTRAORDINARY</div>
            <h1 style="font-size: 4rem; line-height: 1; color:white !important;">Scholars</h1>
        </div>
        <div class="xp-hud" style="width: 350px;">
            <h3 style="margin:0; color:white !important;">🏆 Level {st.session_state.lvl}</h3>
            <div class="xp-bar-bg"><div class="xp-bar-fill" style="width: {st.session_state.xp}%;"></div></div>
            <div style="display: flex; justify-content: space-between; color:white !important;"><small>PROGRESS</small><small>{st.session_state.xp}/100 XP</small></div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# 6. Social Challenge Area
st.markdown("## ⚔️ Friend Battles")
c_v1, c_v2 = st.columns(2)

with c_v1:
    st.markdown(f"""
    <div class="bouncy-card">
        <h3>🔥 Head-to-Head Sprint</h3>
        <p>Challenge your Snapchat friends to a 60-second logic duel.</p>
        <p style="color:#7C3AED; font-weight:bold;">REWARD: +50 XP</p>
    </div>
    """, unsafe_allow_html=True)
    st.button("START CHALLENGE", key="v1")

with c_v2:
    st.markdown(f"""
    <div class="bouncy-card">
        <h3>📅 Daily Quest</h3>
        <p>Connect 2 socials to unlock the "Socialite" badge.</p>
        <p style="color:#7C3AED; font-weight:bold;">PROGRESS: 0/2</p>
    </div>
    """, unsafe_allow_html=True)
    st.button("CLAIM XP", disabled=True)

# 7. Main Dashboard (Functional Tools)
st.markdown("## 🕹️ Tools")
t1, t2, t3 = st.columns(3)
with t1:
    st.markdown(f'<div class="bouncy-card"><h3>📂 Study Forge</h3><p>Upload PDF to earn XP.</p></div>', unsafe_allow_html=True)
    st.file_uploader(" ", type=["pdf"], key="f1")
with t2:
    st.markdown(f'<div class="bouncy-card"><h3>💬 Zen Tutor</h3><p>Chat with Chino AI.</p></div>', unsafe_allow_html=True)
    st.chat_input("Message...")
with t3:
    st.markdown(f'<div class="bouncy-card"><h3>🎁 Prize Vault</h3><p>Real-world rewards.</p></div>', unsafe_allow_html=True)
    st.button("ENTER VAULT")

st.markdown("<p style='text-align: center; opacity: 0.5; margin-top: 100px;'>© 2026 Chino Study Arena</p>", unsafe_allow_html=True)