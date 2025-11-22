# The code behind the pie chart featured in this repository!

import matplotlib.pyplot as plt

languages = ["C++", "MATLAB", "C", "Assembly", "Scilab", "HTML"]
percentages = [69.76, 27.34, 0.03, 0.47, 0.84, 1.57]

fig, ax = plt.subplots(figsize=(8, 8))

def autopct_func(pct):
    return f"{pct:.1f}%" if pct >= 5 else ""

wedges, texts, autotexts = ax.pie(
    percentages,
    startangle=90,
    labels=None,
    autopct=autopct_func,
    pctdistance=0.7,
)

ax.set_title("LANGUAGES", fontsize=18, pad=20)
ax.axis("equal")

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
