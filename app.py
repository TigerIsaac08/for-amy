import streamlit as st
import streamlit.components.v1 as components
import random

# 1. Setup the page
st.set_page_config(page_title="For YAMY ❤️", page_icon="🌷")

# --- CUSTOM ANIMATION FUNCTION ---
def tulip_explosion():
    components.html(
        """
        <script>
        const container = window.parent.document.querySelector('.main');
        for (let i = 0; i < 50; i++) {
            const petal = window.parent.document.createElement('div');
            petal.innerHTML = i % 2 === 0 ? '🌷' : '🌸';
            petal.style.position = 'fixed';
            petal.style.left = Math.random() * 100 + 'vw';
            petal.style.top = '100vh';
            petal.style.fontSize = Math.random() * 20 + 20 + 'px';
            petal.style.zIndex = '9999';
            petal.style.transition = 'transform ' + (Math.random() * 3 + 2) + 's linear, opacity 2s';
            container.appendChild(petal);
            
            setTimeout(() => {
                petal.style.transform = 'translateY(-120vh) rotate(' + (Math.random() * 360) + 'deg)';
                petal.style.opacity = '0';
            }, 100);
            
            setTimeout(() => petal.remove(), 5000);
        }
        </script>
        """,
        height=0,
    )

# --- GLOBAL STYLING ---
st.markdown("""
<style>
.stApp {
    background-color: #a50000;
}

.main .block-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

h1, h2, h3, p {
    color: white !important;
    text-align: center;
    font-family: 'serif';
}

div.stButton > button, 
div.stButton > button p, 
div.stButton > button div {
    color: #000000 !important;
    background-color: #ffffff !important;
    font-weight: 900 !important;
}

div.stButton > button {
    border-radius: 15px;
    border: 3px solid #000000;
    width: 300px; 
    height: 70px;
    font-size: 22px !important;
    display: block;
    margin: 15px auto; 
    box-shadow: 0px 4px 15px rgba(0,0,0,0.5);
}

div.stButton > button:hover {
    background-color: #eeeeee !important;
    transform: scale(1.02);
}

[data-testid="stVerticalBlock"] {
    align-items: center;
}
</style>
""", unsafe_allow_html=True)

# --- SESSION STATE ---
if 'page' not in st.session_state:
    st.session_state.page = "home"
if 'tulip_count' not in st.session_state:
    st.session_state.tulip_count = 0
if 'date_result' not in st.session_state:
    st.session_state.date_result = None

def tulip_border():
    st.markdown('<div style="text-align:center; font-size:24px; padding: 10px;">✨ 🌷 ✨ 🌷 ✨ 🌷 ✨</div>', unsafe_allow_html=True)

# --- PAGE 1: HOME ---
if st.session_state.page == "home":
    tulip_border()
    st.markdown("<h1 style='font-size: 3rem;'>Happy valentines Amy! ❤️</h1>", unsafe_allow_html=True)
    st.write("Pick an option...")
    
    if st.button("Happy valentines Isaac"):
        st.session_state.page = "message"
        st.rerun()
        
    if st.button("Go away loser"):
        st.session_state.page = "rejection"
        st.rerun()
    tulip_border()

# --- PAGE 2: REJECTION ---
elif st.session_state.page == "rejection":
    st.markdown("<h1 style='font-size: 4rem;'>YOU HATE ME</h1>", unsafe_allow_html=True)
    
    if st.session_state.tulip_count == 0:
        st.subheader("Here, have a Tulip maybe you'll like me then")
        if st.button("🌷 Give Tulip 🌷"):
            st.session_state.tulip_count = 1
            st.rerun()
    else:
        st.subheader("Is that enough tulips yet?")

    if st.session_state.tulip_count > 0:
        st.markdown(f"<div style='font-size: 40px; text-align: center; padding: 10px;'>{'🌷' * st.session_state.tulip_count}</div>", unsafe_allow_html=True)
        if st.button("Need more Tulips"):
            st.session_state.tulip_count += 1
            st.rerun()
        if st.button("I like you now"):
            st.session_state.page = "yay"
            st.rerun()

# --- PAGE 3: YAY ---
elif st.session_state.page == "yay":
    tulip_explosion()
    st.markdown("<h1 style='font-size: 5rem;'>YAY!</h1>", unsafe_allow_html=True)
    st.write("The tulips worked!")
    if st.button("Proceed ❤️"):
        st.session_state.page = "message"
        st.rerun()

# --- PAGE 4: MESSAGE ---

elif st.session_state.page == "message":

    tulip_explosion()

    tulip_border()

    st.markdown("<h1 style='font-size: 2.5rem;'>For Amy 💌</h1>", unsafe_allow_html=True)

    

    st.markdown("""

    <div style="background: white; padding: 30px; border-radius: 20px; color: black; text-align: center; border: 5px solid #000000; max-width: 500px; margin: auto;">

        <h3 style="color: #a50000 !important;">My Dearest Amy,</h3>

        <p style="color: black !important; font-size: 18px; line-height: 1.6;">

        I know this probably wasnt what you were expecting, whilest I was trying to think of what to get you I wanted to do something different. Since im not going to be seeing you today, I wanted something to give TODAY. Ive never been good at arts and craft so I wanted to do something you know ive put effort into, not just a long message. Now, for the long message, I know its cringe but ill make a exception for this special day. Happy valentines day! I know things havent been easy for you, im so incredibly proud of how you. Youre doing so well with everything going on be able to manage it all at the same time, its really impressive Amy. You really are the most amazing girl, youre thoughtful, emotionally intelligent alongside intellectual intellegence, youre funny and not even to mention how beautiful you are. But above all of that, you make me happy. You put a smile on my face whenever I need it, you cant even come close to understanding how much youve helped me since we met. Although sometimes we may argue, we always make up. I love everything about you for you; I love the way you smile when you do something cheeky, the way you laugh so incredibly real, you really are a "Shot of espresso" in my life. 

        </p>

        <h4 style="color: #a50000;">Love, Isaac</h4>

    </div>

    """, unsafe_allow_html=True)



    st.markdown("<div style='height:40px;'></div>", unsafe_allow_html=True)



    if st.button("Theres more??!"):

        st.session_state.page = "more"

        st.rerun()



    st.markdown("<div style='height:20px;'></div>", unsafe_allow_html=True)



    if st.button("Back to start"):

        st.session_state.page = "home"

        st.session_state.tulip_count = 0

        st.rerun()

# --- PAGE 5: MORE (3 SECTIONS) ---
elif st.session_state.page == "more":

    st.markdown("""
    <style>
    .section {
        height: 30vh;
        display: flex;
        align-items: center;
        justify-content: center;
        border-top: 2px solid black;
        border-bottom: 2px solid black;
    }
    .top { background-color: #40E0D0; }
    .middle { background-color: #ff4b4b; }
    .bottom { background-color: #4b6cff; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section top">', unsafe_allow_html=True)
    if st.button("When you miss me"):
        st.session_state.page = "miss_me"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="section middle">', unsafe_allow_html=True)
    if st.button("Random Date generator!"):
        st.session_state.page = "date"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="section bottom">', unsafe_allow_html=True)
    if st.button("Memories!"):
        st.session_state.page = "memories"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- PAGE 6: WHEN YOU MISS ME ---
elif st.session_state.page == "miss_me":

    st.markdown("<h1>When you miss me 💙</h1>", unsafe_allow_html=True)

    st.markdown("""
    <div style="background:white; padding:30px; border-radius:20px; 
    border:3px solid black; color:black; max-width:700px; margin:auto; text-align:center;">
        <h3 style="color:#a50000;">My Sweet Amy,</h3>
        <p style="font-size:18px;">
        [WRITE YOUR HEARTFELT MESSAGE HERE]
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    cols = st.columns(3)
    for col in cols:
        with col:
            st.markdown("""
            <div style="height:150px; border:3px dashed black; 
            border-radius:15px; background:#f8f8f8;"></div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("Back"):
        st.session_state.page = "more"
        st.rerun()

# --- PAGE 7: DATE GENERATOR ---
elif st.session_state.page == "date":

    st.markdown("<h1>Random Date Generator 💕</h1>", unsafe_allow_html=True)

    st.write("I know you hate choosing, so i've came up with a few ideas you can look through and we can choose what to do")

    date_options = [
        "Movie night with homemade snacks 🍿",
        "Go out for dessert only 🍰",
        "Sunset walk + takeaway coffee ☕",
        "Cook a new recipe together 👩‍🍳",
        "Mini road trip somewhere random 🚗",
        "Bowling + loser buys drinks 🎳",
        "Picnic date 🌷",
        "Arcade night 🕹️"
    ]

    if st.button("Click for date! 🎲"):
        st.session_state.date_result = random.choice(date_options)

    if st.session_state.date_result:
        st.markdown(f"""
        <div style="margin-top:30px; background:white; padding:25px;
        border-radius:20px; border:3px solid black; color:black; 
        font-size:22px; text-align:center;">
        {st.session_state.date_result}
        </div>
        """, unsafe_allow_html=True)

    if st.button("Back"):
        st.session_state.page = "more"
        st.session_state.date_result = None
        st.rerun()

# --- PAGE 8: MEMORIES ---
elif st.session_state.page == "memories":

    st.markdown("<h1>Our Memories 💙</h1>", unsafe_allow_html=True)

    for i in range(3):
        st.markdown("""
        <div style="margin-bottom:40px;">
            <div style="height:200px; border:3px dashed black; 
            border-radius:15px; background:#f0f0f0;"></div>
            <div style="background:white; padding:15px; border-radius:10px;
            margin-top:10px; border:2px solid black; color:black;">
            Memory description goes here...
            </div>
        </div>
        """, unsafe_allow_html=True)

    if st.button("Back"):
        st.session_state.page = "more"
        st.rerun()




