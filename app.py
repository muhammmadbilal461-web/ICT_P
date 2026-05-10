import streamlit as st

# Page Configuration
st.set_page_config(page_title="Mechanical Unit Hub", layout="centered")

# --- CUSTOM CSS FOR MECHANICAL THEME ---
# This adds a subtle mechanical background and styles the headers
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://www.transparenttextures.com/patterns/carbon-fibre.png");
        background-color: #1a1a1a;
    }
    h1, h2, h3 {
        color: #ff9100 !important;
        font-family: 'Courier New', Courier, monospace;
        text-shadow: 2px 2px #000000;
    }
    .stNumberInput, .stSelectbox {
        border: 2px solid #ff9100;
        border-radius: 5px;
    }
    .main-header {
        border-bottom: 3px solid #ff9100;
        padding-bottom: 10px;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_status=True)

# --- HEADER SECTION ---
st.markdown('<div class="main-header">', unsafe_allow_html=True)
st.title("⚙️ Mechanical Unit & Density Hub")
st.subheader("Muhammad Bilal | Roll: 25-ME-124")
st.markdown('</div>', unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
st.sidebar.header("Navigation")
option = st.sidebar.radio(
    "Select Tool",
    ("Unit Converter", "Material Density Checker")
)

# --- UNIT CONVERTER LOGIC ---
if option == "Unit Converter":
    st.header("🔄 Precision Converter")
    
    col1, col2 = st.columns(2)
    with col1:
        category = st.selectbox("Quantity", ["Pressure", "Power", "Force"])
    with col2:
        value = st.number_input("Input Magnitude", value=1.0)

    st.write("---")

    if category == "Pressure":
        # Bar to Pascal
        result = value * 100000
        st.success(f"⚙️ {value} Bar = {result:,} Pa (N/m²)")
        
    elif category == "Power":
        # HP to Watts
        result = value * 745.7
        st.success(f"⚙️ {value} HP = {result:.2f} Watts")
        
    elif category == "Force":
        # Newtons to Pounds-force
        result = value * 0.224809
        st.success(f"⚙️ {value} Newtons = {result:.4f} lbf")

# --- DENSITY CHECKER LOGIC ---
elif option == "Material Density Checker":
    st.header("⚖️ Density Database")
    
    densities = {
        "Mild Steel": 7850,
        "Aluminum 6061": 2700,
        "Cast Iron": 7200,
        "Copper": 8960,
        "Titanium": 4506,
        "Stainless Steel": 8000
    }
    
    mat_choice = st.selectbox("Select Engineering Material", list(densities.keys()))
    d_val = densities[mat_choice]
    
    st.metric(label="Density (kg/m³)", value=f"{d_val}")
    
    st.info(f"The density of {mat_choice} is approximately {d_val} kg/m³.")

# --- FOOTER ---
st.sidebar.markdown("---")
st.sidebar.write("🔩 **Status:** System Operational")
st.sidebar.write("🛠️ **Engineer:** M. Bilal")
