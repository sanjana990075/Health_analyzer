import streamlit as st

st.set_page_config(page_title="Social Media Health Analyzer", layout="centered")

# ----------------------------- #
#          APP HEADER           #
# ----------------------------- #
st.title("🧠 Social Media Health Analyzer")
st.markdown("### Understand how your social media usage might be affecting your mental and physical health.\n")
st.info("Answer the following questions honestly to receive personalized suggestions.")

# ----------------------------- #
#         QUESTIONS SET         #
# ----------------------------- #
questions = [
    {
        "q": "1. How many hours a day do you spend on social media?",
        "options": {
            "<1 hour": 0,
            "1-3 hours": 1,
            "3-5 hours": 2,
            ">5 hours": 3
        }
    },
    {
        "q": "2. Do you feel anxious when you can’t access your social apps?",
        "options": {
            "Never": 0,
            "Occasionally": 1,
            "Often": 2,
            "Always": 3
        }
    },
    {
        "q": "3. Do you scroll social media while eating meals?",
        "options": {
            "Never": 0,
            "Rarely": 1,
            "Sometimes": 2,
            "Always": 3
        }
    },
    {
        "q": "4. Does social media interfere with your sleep routine?",
        "options": {
            "Never": 0,
            "Rarely": 1,
            "Often": 2,
            "Always": 3
        }
    },
    {
        "q": "5. Do you compare your life to others online?",
        "options": {
            "Never": 0,
            "Occasionally": 1,
            "Often": 2,
            "Always": 3
        }
    },
    {
        "q": "6. Have you tried to reduce screen time but failed?",
        "options": {
            "Never needed": 0,
            "Tried once": 1,
            "Tried multiple times": 2,
            "Always fail": 3
        }
    },
    {
        "q": "7. Does social media make you feel left out (FOMO)?",
        "options": {
            "Not at all": 0,
            "Sometimes": 1,
            "Often": 2,
            "Always": 3
        }
    },
    {
        "q": "8. Do you skip physical activity because of screen time?",
        "options": {
            "Never": 0,
            "Rarely": 1,
            "Sometimes": 2,
            "Often": 3
        }
    },
    {
        "q": "9. Do you feel tired after long social media sessions?",
        "options": {
            "Never": 0,
            "Rarely": 1,
            "Often": 2,
            "Always": 3
        }
    },
    {
        "q": "10. Have you ever lost track of time while scrolling?",
        "options": {
            "Never": 0,
            "Sometimes": 1,
            "Often": 2,
            "Always": 3
        }
    },
]

# ----------------------------- #
#     USER RESPONSES & SCORE    #
# ----------------------------- #
total_score = 0
user_responses = []

st.markdown("---")
with st.form("quiz_form"):
    for q in questions:
        response = st.radio(q["q"], list(q["options"].keys()), key=q["q"])
        total_score += q["options"][response]
        user_responses.append(response)

    submitted = st.form_submit_button("🧾 Submit Quiz")

# ----------------------------- #
#         FEEDBACK LOGIC        #
# ----------------------------- #
if submitted:
    st.markdown("---")
    st.header("📊 Your Result")
    st.success(f"Your Total Score: {total_score} / 30")

    if total_score <= 5:
        st.balloons()
        st.markdown("### ✅ You're doing great!")
        st.write("You have a **healthy relationship** with social media. Keep maintaining balance.")
    elif total_score <= 10:
        st.markdown("### ⚠️ Mild Impact")
        st.write("You’re slightly affected. Try to **set screen-time limits** and enjoy offline activities.")
    elif total_score <= 17:
        st.markdown("### 🚧 Moderate Impact")
        st.write("Social media is affecting your **sleep, time, or mood**. Try digital detox, and use time-tracker apps.")
    elif total_score <= 24:
        st.markdown("### 🚨 High Impact")
        st.write("You may be experiencing **stress or anxiety** due to overuse. Start journaling, reduce usage before sleep.")
    else:
        st.markdown("### ❌ Critical Zone!")
        st.error("Your usage is heavily impacting your health.")
        st.warning("Seek support, use app blockers, and try staying off social media for a few hours each day.")

    

# ----------------------------- #
#        END OF APP UI          #
# ----------------------------- #
st.markdown("---")
st.caption("Made with ❤️ using Streamlit")
