# main.py
import streamlit as st
from auth import login, signup
from analysis import *
from visualizations import show_all_visualizations
from elt import load_data_to_mysql

st.set_page_config(page_title=" Disaster Tracker Dashboard", layout="wide")

# Custom CSS Styling
st.markdown("""
    <style>
    .main {
        background-color: #f9f9f9;
    }
    .block-container {
        padding-top: 2rem;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 0.5rem;
        margin-top: 1rem;
    }
    .stTitle {
        font-size: 2rem !important;
        font-weight: 700;
    }
    </style>
""", unsafe_allow_html=True)

# Session Initialization
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = ""

# Sidebar Header
st.sidebar.title("Disaster Analysis Tracker")

# ----------- LOGIN/SIGNUP PAGE -----------
if not st.session_state.logged_in:
    menu = ["Login", "Signup"]
    choice = st.sidebar.selectbox("Choose Option", menu)

    if choice == "Login":
        st.markdown("## 🔐 Login")
        user = st.text_input("Username")
        pwd = st.text_input("Password", type='password')
        if st.button("Login"):
            if login(user, pwd):
                st.success("✅ Login successful!")
                st.session_state.logged_in = True
                st.session_state.username = user
              
            else:
                st.error("❌ Invalid credentials.")

    elif choice == "Signup":
        st.markdown("## 📝 Signup")
        user = st.text_input("Create Username")
        pwd = st.text_input("Create Password", type='password')
        if st.button("Signup"):
            if signup(user, pwd):
                st.success("✅ Signup successful! Please login.")
            else:
                st.error("⚠️ Username already exists.")

# ----------- LOGGED IN DASHBOARD -----------
else:
    st.sidebar.markdown(f"👋 Welcome, **{st.session_state.username}**")

    actions = ["📊 Data Tables", "📈 Visualizations", "🚪 Logout"]
    selection = st.sidebar.radio("Navigation", actions)

    if selection == "📊 Data Tables":
        st.title("📊 Disaster Management Dashboard")

        # Upload Button
        if st.button("📥 Upload CSV to MySQL"):
            with st.spinner("Processing data..."):
                load_data_to_mysql()
                st.success("✅ Data uploaded to MySQL successfully!")

        st.markdown("### 📁 Explore Analysis Tables")
        with st.expander("Click to Show All Tables"):
            tabs = [
                ("Most Affected Areas", most_affected_area),
                ("Year-wise Disaster Count", year_wise_disaster_count),
                ("Disaster Types Frequency", disaster_types_frequency),
                ("Top Countries by Economic Loss", top_countries_by_economic_loss),
                ("Population Affected per Disaster", population_affected_per_disaster),
                ("Total Disasters per Country", total_disasters_per_country),
                ("Avg Duration by Disaster Type", avg_duration_by_disaster_type),
                ("Recent 10 Disasters", recent_10_disasters),
                ("Cities with Highest Relief Measures", cities_with_highest_relief),
                ("Monthly Disaster Count", monthly_disaster_count),
                ("Relief Aid Distribution Summary", relief_aid_distribution_summary),
                ("Avg Economic Loss by Region", avg_economic_loss_by_region),
                ("Countries with Most Floods", countries_with_most_floods),
                ("Disaster Count by Severity", disaster_count_by_severity)
            ]

            for title, func in tabs:
                st.subheader(f"📌 {title}")
                try:
                    data = func()
                    st.dataframe(data)
                except Exception as e:
                    st.error(f"Error loading data: {e}")


    elif selection == "📈 Visualizations":
        st.title("📈 Visual Insights on Disasters")
        show_all_visualizations()

    elif selection == "🚪 Logout":
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.success("👋 Logged out successfully!")
        
