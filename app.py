import streamlit as st

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="Fitness & calories calculator اللياقة وحساب الطاقة",
    page_icon="🏃‍♂️",
    layout="centered"
)

# ---------------- SESSION STATE ----------------
if "started" not in st.session_state:
    st.session_state.started = False

# ---------------- STYLE GLOBAL ----------------
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background-color: #f5f7fa;
}

.hero {
    text-align: center;
    padding: 40px 20px;
    background: linear-gradient(90deg, #1E90FF, #00C6FF);
    border-radius: 20px;
    color: white;
    box-shadow: 0px 6px 20px rgba(0,0,0,0.2);
}

div.stButton > button {
    background: linear-gradient(90deg, #00C6FF, #0072FF);
    color: white;
    border-radius: 12px;
    padding: 0.6em 1.2em;
    font-size: 18px;
    font-weight: bold;
    border: none;
    box-shadow: 0px 6px 15px rgba(0,0,0,0.15);
    transition: 0.3s;
}

div.stButton > button:hover {
    transform: scale(1.05);
    cursor: pointer;
}
</style>
""", unsafe_allow_html=True)

# ======================================================
# 🟦 PAGE D'ACCUEIL
# ======================================================
if not st.session_state.started:

    st.markdown("""
    <div class="hero">
        <h2>🏃 Fitness & calories monitoring</h2>
        <h2>اللياقة وتتبع طاقة الجسم</h2>
    </div>
    """, unsafe_allow_html=True)

    st.write("Welcome! This app helps you estimate calories burned based on activity")
    st.write("مرحبا، تطبيق يساعدك على تتبع السكر واستهلاك الطاقة")

    if st.button("Start"):
        st.session_state.started = True
        st.rerun()

# ======================================================
# 🏋️ APPLICATION
# ======================================================
else:

    st.markdown("## 🏃‍♂️ Fitness Calculator")
    st.markdown("---")

    # ---------------- INPUTS ----------------
    col1, col2 = st.columns(2)

    with col1:
        weight = st.number_input("Weight (kg) الوزن", 40, 200, 70)

    with col2:
        duration = st.number_input("Duration (min) مدة التمرين", 1, 300, 30)

    # 👇 IMPORTANT : mapping affichage → valeur interne
    activity_display = st.selectbox(
        "Activity نوع التمرين",
        ["Rest الراحة", "Walking المشي", "Running الجري"]
    )

    activity_map = {
        "Rest الراحة": "Rest",
        "Walking المشي": "Walking",
        "Running الجري": "Running"
    }

    activity = activity_map[activity_display]

    # ---------------- DATA ----------------
    met_values = {
        "Rest": 1.3,
        "Walking": 3.5,
        "Running": 8.0
    }

    fuel_split = {
        "Rest": {"carbs": 0.2, "fat": 0.8},
        "Walking": {"carbs": 0.5, "fat": 0.5},
        "Running": {"carbs": 0.75, "fat": 0.25}
    }

    # ---------------- BUTTON ----------------
    if st.button("🔥Calories          السعرات الحرارية"):

        calories = met_values[activity] * weight * (duration / 60)

        carbs_g = (calories * fuel_split[activity]["carbs"]) / 4
        fat_g = (calories * fuel_split[activity]["fat"]) / 9

        # ✅ conversion en cubes de sucre
        sugar_cubes = carbs_g / 4

        # ---------------- RESULT ----------------
        st.markdown(f"""
        <div style="
            padding:20px;
            border-radius:15px;
            background-color:#e8f5e9;
            text-align:center;
            font-size:22px;
            font-weight:bold;
            color:#2e7d32;">
            🔥 {calories:.2f} kcal burned
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            st.metric("🍬 Sugar (g) سكر", f"{carbs_g:.2f}")
            st.caption(f"≈ {sugar_cubes:.1f} cubes de sucre 🧊مكعب صغير من السكر")

        with col2:
            st.metric("🧈 Fat (g) دهون", f"{fat_g:.2f}")

        # ---------------- FEEDBACK ----------------
        if calories < 100:
            st.info("Light activity نشاط خفيف 💡")
        elif calories < 300:
            st.success("Good workout تمرين جيد 💪")
        else:
            st.warning("intensive training      نشاط مكثف 🔥")

    # ---------------- BACK BUTTON ----------------
    st.markdown("---")
    if st.button("⬅ Back to Home"):
        st.session_state.started = False
        st.rerun()
