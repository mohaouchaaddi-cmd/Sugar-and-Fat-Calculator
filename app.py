import streamlit as st

st.set_page_config(
    page_title="Fitness App",
    page_icon="🏃",
)


# ---------------- TITRE ----------------
st.markdown(
    """
    <h2 style='color:#1E90FF; text-align:center;'>
        🏃 Fitness & calories calculator<br>
        اللياقة وحساب الطاقة
    </h2>
    """,
    unsafe_allow_html=True
)

# ---------------- CARD INTRO ----------------
st.markdown("""
<div style="
    padding:15px;
    border-radius:15px;
    background-color:#f5f7ff;
    box-shadow:0px 2px 8px rgba(0,0,0,0.1);
">
<h3>💡 Goal</h3>
Calculate: burned calories + glucose consumed + fat burned
</div>
""", unsafe_allow_html=True)

st.write("")

# ---------------- INPUTS ----------------
st.subheader("Inputs               المعطيات")

weight = st.number_input("Weight (kg) الوزن", 40, 200, 70)
duration = st.number_input("Duration (min)   مدة التمرين", 1, 300, 30)

activity_label = st.selectbox(
    "Activity          نوع التمرين",
    ["Rest الراحة", "Walking المشي", "Running الجري"]
)

# 🔥 IMPORTANT FIX: mapping correct
activity_map = {
    "Rest الراحة": "Rest",
    "Walking المشي": "Walking",
    "Running الجري": "Running"
}

activity = activity_map[activity_label]

# ---------------- CALCUL ----------------
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

# Calories
calories = met_values[activity] * weight * (duration / 60)

# Fuel breakdown
carb_ratio = fuel_split[activity]["carbs"]
fat_ratio = fuel_split[activity]["fat"]

carb_cal = calories * carb_ratio
fat_cal = calories * fat_ratio

# Conversion
carbs_g = carb_cal / 4
fat_g = fat_cal / 9

# ---------------- OUTPUT ----------------
st.subheader("Outputs               النتائج    ")
st.write("")

st.success(f"🔥 Burned calories : {calories:.2f} kcal")

col1, col2 = st.columns(2)

with col1:
    st.metric("🍬 Sugar  consumed    كمية السكر المستهلك", f"{carbs_g:.2f} g")

with col2:
    st.metric("🧈 Fat consumed        الدهون المستهلكة ", f"{fat_g:.2f} g")



st.subheader("Note 👉")
st.write(" Sugar cub = 4g")
