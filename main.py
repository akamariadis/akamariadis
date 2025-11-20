import matplotlib.pyplot as plt

languages = ["C++", "MATLAB", "C", "Python", "Assembly", "TeX", "CMake"]
percentages = [69.8, 27.3, 0.0, 1.1, 0.9, 0.5, 0.5]

fig, ax = plt.subplots(figsize=(8, 8))

def autopct_func(pct):
    """Show % only for reasonably large slices (>= 5%)."""
    return f"{pct:.1f}%" if pct >= 5 else ""

wedges, texts, autotexts = ax.pie(
    percentages,
    startangle=90,
    labels=None,
    autopct=autopct_func,
    pctdistance=0.7,
)

ax.set_title("Languages I Use", fontsize=18, pad=20)
ax.axis("equal")  # keep it circular

legend_labels = [f"{lang}: {pct}%" for lang, pct in zip(languages, percentages)]
ax.legend(
    wedges,
    legend_labels,
    title="Languages",
    loc="center left",
    bbox_to_anchor=(1.05, 0.5),
    borderaxespad=0.,
)

plt.tight_layout()
plt.savefig("languages_pie_fixed.png", dpi=300)
plt.show()