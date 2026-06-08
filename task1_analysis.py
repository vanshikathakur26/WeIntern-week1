import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\Lenovo\OneDrive\Documents\WeIntern\Data\Students Performance.csv")

print("Dataset Loaded Successfully!")

print("\nDATASET SHAPE")
print(data.shape)

print("\nDATA TYPES")
print(data.dtypes)

print("\nMISSING VALUES")
print(data.isnull().sum())

print("\nDUPLICATE ROWS")
print(data.duplicated().sum())

print("\nSUMMARY STATISTICS")
print(data.describe())

print("\nGENDER COUNT")
print(data["gender"].value_counts())


print("\nTEST PREPARATION COURSE")
print(data["test preparation course"].value_counts())

print("\nAVERAGE MATH SCORE BY TEST PREPARATION")
print(data.groupby("test preparation course")["math score"].mean())

print("\nAVERAGE SCORES BY TEST PREPARATION")
print(
    data.groupby("test preparation course")[
        ["math score", "reading score", "writing score"]
    ].mean()
)

print("\nAVERAGE SCORES BY LUNCH TYPE")
print(
    data.groupby("lunch")[
        ["math score", "reading score", "writing score"]
    ].mean()
)
#-----------------------------
# GRAPH 1: Gender Distribution
# ----------------------------

gender_count = data["gender"].value_counts()

gender_count.plot(kind="bar")

plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Number of Students")

plt.tight_layout()

plt.savefig(r"C:\Users\Lenovo\OneDrive\Documents\WeIntern\Outputs/gender_distribution.png")
plt.show()

#--------------------------------------
# GRAPH 2:Test Preparation Distribution
# -------------------------------------
prep_count = data["test preparation course"].value_counts()

prep_count.plot(kind="bar")

plt.title("Test Preparation Course Distribution")
plt.xlabel("Course Status")
plt.ylabel("Number of Students")
plt.xticks(rotation=30)

plt.tight_layout()

plt.savefig(r"C:\Users\Lenovo\OneDrive\Documents\WeIntern\Outputs/test_preparation_distribution.png")
plt.show()

# ------------------------------------------
# GRAPH 3:Average Scores by Test Preparation
# -------------------------------------------


prep_scores = data.groupby("test preparation course")[
    ["math score", "reading score", "writing score"]
].mean()

prep_scores.plot(kind="bar")

plt.title("Average Scores by Test Preparation Course")
plt.xlabel("Course Status")
plt.ylabel("Average Score")
plt.xticks(rotation=30)

plt.tight_layout()

plt.savefig(r"C:\Users\Lenovo\OneDrive\Documents\WeIntern\Outputs/scores_by_test_preparation.png")
plt.show()

#---------------------------------------
# GRAPH 4 : Average Scores by Lunch Type
# --------------------------------------

lunch_scores = data.groupby("lunch")[
    ["math score", "reading score", "writing score"]
].mean()

lunch_scores.plot(kind="bar")

plt.title("Average Scores by Lunch Type")
plt.xlabel("Lunch Type")
plt.ylabel("Average Score")
plt.xticks(rotation=30)

plt.tight_layout()

plt.savefig(r"C:\Users\Lenovo\OneDrive\Documents\WeIntern\Outputs/scores_by_lunch.png")
plt.show()

# ----------------------------
# OVERALL SCORE
# ----------------------------

data["overall_score"] = (
    data["math score"]
    + data["reading score"]
    + data["writing score"]
) / 3

print("\nOVERALL SCORE STATISTICS")
print(data["overall_score"].describe())

print("\nTOP 5 STUDENTS BY OVERALL SCORE")

print(
    data.sort_values(
        by="overall_score",
        ascending=False
    ).head(5)
)

# ----------------------------
# SAVE CLEANED DATASET
# ----------------------------

data.to_csv(
    r"C:\Users\Lenovo\OneDrive\Documents\WeIntern\Outputs\cleaned_students_performance.csv",
    index=False
)

print("\nCleaned dataset saved successfully!")