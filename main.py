import streamlit as st
import math

# App config
st.set_page_config(page_title="TrigoCalc", page_icon="📐", layout="centered")

# Custom styles
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to bottom right, rgba(96, 137, 148 , 0.6), rgba(28, 50, 56 , 0.6));
        font-family: 'Segoe UI', sans-serif;
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    .css-1d391kg {
        background-color: #ff4b4b !important;
        color: white !important;
        border-radius: 10px !important;
        padding: 0.5rem 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1 style='text-align:center; color:#ff4b4b;'>📐 Trigonometry Calculator</h1>", unsafe_allow_html=True)
st.markdown("### 🧠 Enter any 2 sides of a right triangle:")

# Input section
col1, col2 = st.columns(2)
with col1:
    p = st.number_input("📏 Perpendicular (P)", min_value=0.0, step=0.1)
with col2:
    b = st.number_input("📏 Base (B)", min_value=0.0, step=0.1)

h = st.number_input("📐 Hypotenuse (H)", min_value=0.0, step=0.1)

# Trig calculation
def solve_trigo(p, b, h):
    if p and b and not h:
        h = math.sqrt(p**2 + b**2)
    elif h and b and not p:
        p = math.sqrt(h**2 - b**2)
    elif h and p and not b:
        b = math.sqrt(h**2 - p**2)
    elif p and b and h:
        pass  # All sides entered
    else:
        st.warning("⚠️ Please enter any 2 sides.")
        return

    try:
        st.markdown("---")
        st.markdown("### 🧮 Calculated Side Lengths:")
        col1, col2, col3 = st.columns(3)
        col1.metric("📏 P", round(p, 2))
        col2.metric("📏 B", round(b, 2))
        col3.metric("📏 H", round(h, 2))

        st.write("")
        st.write("-"*10)
        st.markdown("### 📐 Trigonometric Ratios:")
        st.write(f"**sin(θ) [p / h]** = {round(p / h, 4)}")
        st.write(f"**cos(θ) [b / h]** = {round(b / h, 4)}")
        st.write(f"**tan(θ) [p / b]** = {round(p / b, 4)}")
        st.write(f"**cot(θ) []** = {round(b / p, 4)}")
        st.write(f"**cosec(θ) [h / p]** = {round(h / p, 4)}")
        st.write(f"**sec(θ) [h / b]** = {round(h / b, 4)}")
        st.write("")
        st.write("-"*10)

    except ZeroDivisionError:
        st.error("🚫 Can't divide by zero. Try different values.")
    except ValueError:
        st.error("⚠️ Invalid triangle. Hypotenuse must be longest.")


# Calculate button
if st.button("Calculate"):
    solve_trigo(p, b, h)

# # Footer
# st.markdown("<hr>", unsafe_allow_html=True)
# st.markdown("<p style='text-align:center;'> Built by <b>HEISENDEV</b> </p>", unsafe_allow_html=True)
