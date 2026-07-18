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


st.markdown("""
<style>
/* ====================================================== */
/* RANDOM MEME THING */
/* ====================================================== */

iframe{
width:100%;
border:none;
border-radius:18px;
box-shadow:
0 15px 40px rgba(0,0,0,.08);

}

@media (max-width:900px){
.title{
font-size:3.4rem;

}

.logo{
font-size:3rem;

}

}

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Bebas+Neue&display=swap');

html,
body,
[data-testid="stAppViewContainer"]{

background:#F6F4EF;
color:#111;
font-family:'Inter',sans-serif;

}

/* Remove Streamlit header */

[data-testid="stHeader"]{
background:transparent;
box-shadow:none;

}

/* Main container */
.block-container{
max-width:1180px;
padding-top:2rem;
padding-bottom:5rem;
}

/* Better spacing */

div[data-testid="stVerticalBlock"]{
gap:1.6rem;
}

/* Typography */

.logo{
font-family:'Bebas Neue';
font-size:4rem;
letter-spacing:.12em;
line-height:1;

}

.section{
font-size:.8rem;
letter-spacing:.25em;
text-transform:uppercase;
color:#666;
margin-bottom:12px;
}

.title{
font-size:4.8rem;
font-weight:800;
line-height:.92;
margin-bottom:20px;

}

.body{
font-size:1.05rem;
line-height:1.8;
color:#555;
max-width:720px;

}

/* Cards */

.card{
background:white;
border:1px solid rgba(0,0,0,.08);
border-radius:22px;
padding:28px;
box-shadow:
0 14px 35px rgba(0,0,0,.04);
transition:.25s;

}

.card:hover{
transform:translateY(-4px);
box-shadow:
0 20px 45px rgba(0,0,0,.08);

}

/* Images */
.stImage img{
border-radius:18px;

}

/* Buttons */

.stButton>button{
border-radius:999px;
background:#111;
color:white;
border:none;
padding:.7rem 1.5rem;

}
/* ====================================================== */
/* PROJECTS */
/* ====================================================== */

.card{

margin-bottom:18px;

}

.stCaption{
letter-spacing:.12em;
text-transform:uppercase;
font-size:.75rem;
color:#888;
}

/* ========================================== */
/* SONG LIST */
/* ========================================== */

button[kind="secondary"]{
text-align:left;
padding:14px;
font-weight:600;
border-radius:14px;
margin-bottom:8px;
}
iframe{
border-radius:18px;
}

/* ========================================= */
/* SONG PANEL */
/* ========================================= */

.song-panel{
animation:fadeIn .35s ease;

}

@keyframes fadeIn{

from{
opacity:0;
transform:translateY(12px);

}

to{
opacity:1;
transform:none;

}

}

.stDivider{
margin-top:6px;
margin-bottom:6px;
} 
            
/* Hide Streamlit radio circles */

div[role="radiogroup"] label{

padding:14px 18px;
margin-bottom:10px;
border-radius:16px;
background:white;
border:1px solid rgba(0,0,0,.08);
transition:.25s;
cursor:pointer;
display:block;

}

div[role="radiogroup"] label:hover{
transform:translateY(-2px);
box-shadow:0 10px 20px rgba(0,0,0,.08);

}
div[role="radiogroup"] input{
display:none;
}
</style>

""", unsafe_allow_html=True)

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

    st.markdown("### YOUR PICKS")

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
        "media":"assets/covers/pcs.mp4",
        "category":"ROM Hack",
        "status":"Demo • TBA",
        "description":
        "A ROM Hack Project I started back in 2025. Planning on moving it to pokeemerald expansion."
    },

    {
        "title":"FOR YOU v1",

        "category":"Music",

        "status":"Released - Originally on Instagram",

        "video":"assets/covers/for-you-v1-snippet.mp4",

        "description":
        "A small snippet for one of my singles. (Temporarily archived on Instagram)"
    },

    {
        "title":"GARDEN OF THORNS",

        "category":"EP",

        "status":"In Progress",

        "image":"assets/projects/garden_of_thorns.png",

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