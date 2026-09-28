"""Визуализация данных: 4 типа графиков."""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

np.random.seed(42)
df = pd.DataFrame({
    "category": np.random.choice(["A", "B", "C", "D"], 200),
    "value": np.random.normal(100, 20, 200),
    "group": np.random.choice(["X", "Y"], 200),
})

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 1. Гистограмма
axes[0, 0].hist(df["value"], bins=20, color="skyblue", edgecolor="black")
axes[0, 0].set_title("Распределение значений")

# 2. Boxplot
sns.boxplot(data=df, x="category", y="value", ax=axes[0, 1])
axes[0, 1].set_title("Boxplot по категориям")

# 3. Bar plot
df.groupby("category")["value"].mean().plot(kind="bar", ax=axes[1, 0], color="coral")
axes[1, 0].set_title("Среднее по категориям")

# 4. Scatter
for grp in df["group"].unique():
    subset = df[df["group"] == grp]
    axes[1, 1].scatter(subset.index, subset["value"], label=grp, alpha=0.6)
axes[1, 1].set_title("Scatter по группам")
axes[1, 1].legend()

plt.tight_layout()
plt.savefig("visualization.png", dpi=100)
plt.show()
