import streamlit as st
import random
import matplotlib.pyplot as plt

st.set_page_config(page_title="Chris Pro Stars", layout="centered", page_icon="⭐")

st.markdown("<h1 style='text-align: center; color: white;'>Chris Pro</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #ccc;'>LeePee</p>", unsafe_allow_html=True)

fig, ax = plt.subplots(figsize=(6, 4))
ax.set_facecolor("black")
ax.axis("off")

for _ in range(80):
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)
    size = random.uniform(10, 60)
    color = random.choice(["white", "yellow", "cyan", "magenta", "orange"])
    ax.plot(x, y, marker="*", markersize=size/10, color=color)

st.pyplot(fig)
