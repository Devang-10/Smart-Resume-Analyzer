import matplotlib.pyplot as plt
import streamlit as st

def plot_skill_match_chart(score, width=4, height=2.5):
    if score is None:
        st.warning("No score to visualize.")
        return

    fig, ax = plt.subplots(figsize=(width, height))
    ax.barh(['Skill Match'], [score], color='#2ECC71')
    ax.set_xlim(0, 100)
    ax.set_xlabel('Matching Score (%)')
    ax.set_title('🔍 Skill Match Visualization')

    # Display score inside or outside bar based on value
    for i, v in enumerate([score]):
        if v < 90:
            ax.text(v + 2, i, f"{v}%", va='center', fontweight='bold')
        else:
            ax.text(v - 8, i, f"{v}%", va='center', fontweight='bold', color='white')

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)

    st.pyplot(fig)
