import streamlit as st
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
SONG = {
    "title": "SONG OF THE WEEK.",

    "artist": "Kanye West - Homecoming",

    "cover": "assets/covers/mari-kart.jpg",

    "youtube":
    "https://www.youtube.com/embed/EzU0ofo3jOs",
    "description":
    """
    idk lol.
    """
}

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
# NOW PLAYING
# ==========================================================

st.write("")
st.write("")

st.markdown(
    """
<div class="section">

RANDOM MEME THING

</div>
""",
    unsafe_allow_html=True,
)

cover_col, player_col = st.columns([1, 2], gap="large")

# ----------------------------------------------------------
# LEFT
# ----------------------------------------------------------

from pathlib import Path

with cover_col:
    cover = Path(SONG["cover"])

    if cover.exists():
        st.image(
            cover,
            use_container_width=True,
        )
    else:
        st.markdown(
            """
<div class="card" style="
height:320px;
display:flex;
justify-content:center;
align-items:center;
color:#777;
">
Album cover missing
</div>
""",
            unsafe_allow_html=True,
        )

# ----------------------------------------------------------
# RIGHT
# ----------------------------------------------------------

with player_col:

    st.markdown(
        f"""
<div class="card">

<h2 style="margin-top:0;margin-bottom:6px;">

{SONG["title"]}

</h2>

<p style="margin-top:0;color:#666;font-size:1rem;">

{SONG["artist"]}

</p>

<p style="margin-top:24px;line-height:1.8;color:#555;">

{SONG["description"]}

</p>

</div>
""",
        unsafe_allow_html=True,
    )

    st.write("")

    st.components.v1.iframe(
        SONG["youtube"],
        height=315,
        scrolling=False,
    )

    # ==========================================================
# FEATURED PROJECTS
# ==========================================================

PROJECTS = [

    {
        "title":"Pokémon Cerulean Seas",

        "category":"ROM Hack",

        "status":"Demo • TBA",

        "video":"assets/covers/pcs.mp4",

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

    left,right = st.columns([1,2], gap="large")

    with left:

        image = Path(project["image"])

        if image.exists():

            st.image(
                image,
                use_container_width=True
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
                unsafe_allow_html=True
            )

    with right:

        st.caption(project["category"])

        st.subheader(project["title"])

        st.write(project["description"])

        st.caption(project["status"])

    st.markdown("</div>", unsafe_allow_html=True)

    st.write("")