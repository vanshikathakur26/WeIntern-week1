import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv(r"C:\Users\Lenovo\OneDrive\Documents\WeIntern\Outputs\cleaned_students_performance.csv")

print("Dataset Loaded Successfully!")

print(data.shape)
print(data.head())

# --------------------------------
# GRAPH 1: HISTOGRAM
# --------------------------------

plt.figure(figsize=(8, 5))

sns.histplot(data["math score"], bins=10)

plt.title("Distribution of Math Scores")
plt.xlabel("Math Score")
plt.ylabel("Number of Students")

plt.savefig(
    r"C:\Users\Lenovo\OneDrive\Documents\WeIntern\Outputs\histogram_math_scores.png"
)

plt.show()

# --------------------------------
# GRAPH 2: BOX PLOT
# --------------------------------

plt.figure(figsize=(8, 5))

sns.boxplot(
    x="gender",
    y="math score",
    data=data
)

plt.title("Math Score by Gender")
plt.xlabel("Gender")
plt.ylabel("Math Score")

plt.savefig(
    r"C:\Users\Lenovo\OneDrive\Documents\WeIntern\Outputs\boxplot_math_gender.png"
)

plt.show()

# --------------------------------
# GRAPH 3: SCATTER PLOT
# --------------------------------

plt.figure(figsize=(8, 5))

sns.scatterplot(
    x="math score",
    y="reading score",
    data=data
)

plt.title("Math Score vs Reading Score")
plt.xlabel("Math Score")
plt.ylabel("Reading Score")

plt.savefig(
    r"C:\Users\Lenovo\OneDrive\Documents\WeIntern\Outputs\scatter_math_reading.png"
)

plt.show()

# --------------------------------
# GRAPH 4: HEATMAP
# --------------------------------

plt.figure(figsize=(8, 6))

corr = data.select_dtypes(include="number").corr()

sns.heatmap(
    corr,
    annot=True,
    cmap="Blues"
)

plt.title("Correlation Heatmap")

plt.savefig(
    r"C:\Users\Lenovo\OneDrive\Documents\WeIntern\Outputs\correlation_heatmap.png"
)

plt.show()