import streamlit as st
from pathlib import Path
# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="THORNED GARDEN",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================================
# SITE DATA
# ==========================================================

SITE = {

    "name": "THORNED GARDEN",
    "owner": "BY EVOTHORNE - Tim Gabriel",
    "tagline": "Independent Upcoming Producer • Web/Game Developer • Strategy Game Analyst",
    
}
SONGS = [

    {
        "title": "Homecoming",
        "artist": "Kanye West",
        "cover": "assets/covers/homecoming.jpg",
        "youtube": "https://www.youtube.com/embed/LQ488QrqGE4"
    },

    {
        "title": "Saint Pablo",
        "artist": "Kanye West",
        "cover": "assets/covers/saint_pablo.jpg",
        "youtube": "https://www.youtube.com/embed/w9rzz4pDFwA"
    },

    {
        "title": "White Ferrari",
        "artist": "Frank Ocean",
        "cover": "assets/covers/white_ferrari.jpg",
        "youtube": "https://www.youtube.com/embed/Dlz_XHeUUis"
    },
]

PROJECTS = []

# ==========================================================
# GLOBAL CSS
# ==========================================================

#ayoha sa ni boss
# ==========================================================
# LOAD CSS
# ==========================================================

def load_css():

    with open("assets/assets/styles/main.css") as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True

        )
load_css()


# ==========================================================
# HERO
# ==========================================================

st.markdown(
f"""

<div class="logo">
{SITE["name"]}
</div>

<div class="section">
{SITE["owner"]}
</div>


""",

unsafe_allow_html=True
)

# ==========================================================
# SONGS OF THE WEEK
# ==========================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    """
<div class="section">
SONGS OF THE WEEK
</div>
""",
    unsafe_allow_html=True,
)

if "selected_song" not in st.session_state:
    st.session_state.selected_song = 0

left, right = st.columns([2.2, 1], gap="large")

current = SONGS[st.session_state.selected_song]

# ==========================================================
# LEFT PANEL
# ==========================================================

with left:

    st.markdown('<div class="song-panel">', unsafe_allow_html=True)

    cover = Path(current["cover"])

    if cover.exists():
        st.image(cover, use_container_width=True)

    st.markdown(
        f"""
### {current["title"]}

<span style="color:#777;font-size:18px;">
{current["artist"]}
</span>
""",
        unsafe_allow_html=True,
    )

    st.components.v1.iframe(
        current["youtube"],
        height=340,
        scrolling=False,
    )

    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================================
# PLAYLIST
# ==========================================================

with right:

    st.markdown("### HEHEHEHA")

    song_names = [f"{s['title']} — {s['artist']}" for s in SONGS]

selection = st.radio(
    "",
    options=range(len(song_names)),
    format_func=lambda i: song_names[i],
    index=st.session_state.selected_song,
    label_visibility="collapsed",
)

if selection != st.session_state.selected_song:
    st.session_state.selected_song = selection
    st.rerun()

    # ==========================================================
# FEATURED PROJECTS
# ==========================================================

PROJECTS = [

    {
        "title":"Pokémon Cerulean Seas",
        "media_type": "video",
        "media":"assets/assets/pcs.mp4",
        "category":"Coding: Game - Demo",
        "status":"TBA",
        "description":
        "A ROM Hack Project I started back in 2025. Planning on moving it to pokeemerald expansion."
    },

    {
        "title":"FOR YOU v1",

        "category":"Music - Single",

        "status":"Released - Originally on Instagram",

        "video":"assets/assets/for-you-v1-snippet.mp4",

        "description":
        "A small snippet for one of my singles. (Temporarily archived on Instagram)"
    },

    {
        "title":"GARDEN OF THORNS",

        "category":"Music - EP",

        "status":"In Progress",

        "image":"assets/assets/images (1).jpg",

        "description":
        "A conceptual, WIP EP. More info on the Autobiography page."
    }

]

st.write("")
st.write("")

st.markdown(
"""
<div class="section">

FEATURED PROJECTS

</div>
""",
unsafe_allow_html=True
)

for project in PROJECTS:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    left, right = st.columns([1, 2], gap="large")
    from pathlib import Path
    with left:
        # support keys: media, video, image
        media_path = project.get("media") or project.get("video") or project.get("image")
        if media_path:
            media = Path(media_path)
            if media.exists():
                # determine type
                mtype = project.get("media_type")
                if not mtype:
                    suffix = media.suffix.lower()
                    if suffix in [".mp4", ".mov", ".webm"]:
                        mtype = "video"
                    else:
                        mtype = "image"
                if mtype == "image":
                    st.image(media, use_container_width=True)
                elif mtype == "video":
                    st.video(str(media))
                else:
                    st.write("")
            else:
                st.markdown(
                    """
<div style="
height:220px;
display:flex;
justify-content:center;
align-items:center;
background:#ECE8E2;
border-radius:18px;
color:#666;
font-weight:600;
">
Preview unavailable
</div>
""",
                    unsafe_allow_html=True,
                )
        else:
            st.markdown(
                """
<div style="
height:220px;
background:#ECE8E2;
border-radius:18px;
display:flex;
justify-content:center;
align-items:center;
color:#666;
">
Preview
</div>
""",
                unsafe_allow_html=True,
            )

    with right:
        st.caption(project.get("category", ""))
        st.subheader(project.get("title", ""))
        st.write(project.get("description", ""))
        st.caption(project.get("status", ""))

    st.markdown("</div>", unsafe_allow_html=True)

    st.write("")