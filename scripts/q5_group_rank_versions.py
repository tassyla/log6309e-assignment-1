import pandas as pd
from scipy import stats
import scikit_posthocs as sp
import matplotlib.pyplot as plt
import seaborn as sns

# --- 1. SETUP: File names and versions ---
file_names = {
    'base_version': '../data/base_version_perf.xlsx',
    'version_1':    '../data/version_1_perf.xlsx',
    'version_2':    '../data/version_2_perf.xlsx',
    'version_3':    '../data/version_3_perf.xlsx'
}

# --- 2. DATA LOADING ---
print("--- Loading data for Q5 analysis ---")
all_data = []
try:
    for version_name, file_path in file_names.items():
        df = pd.read_excel(file_path)
        # Add a column for the version name to combine data later
        df['version'] = version_name
        all_data.append(df[['TOTAL_CPU', 'version']].dropna())
    
    # Combine all data into a single DataFrame
    combined_df = pd.concat(all_data)
    print("All data loaded and combined successfully.")

except FileNotFoundError as e:
    print(f"ERROR: Could not find a file. Make sure paths are correct.")
    print(e)
    exit()
except KeyError:
    print("ERROR: Column 'TOTAL_CPU' not found. Please check column names.")
    exit()

# Prepare data for Kruskal-Wallis test (list of series)
data_groups = [group["TOTAL_CPU"] for name, group in combined_df.groupby("version")]

# --- 3. VISUAL ANALYSIS (BOXPLOT) ---
print("\n--- Generating Boxplot ---")
plt.figure(figsize=(10, 7))
sns.boxplot(x='version', y='TOTAL_CPU', data=combined_df, 
            order=['base_version', 'version_1', 'version_2', 'version_3'])
plt.title('Comparison of CPU Usage Across Software Versions')
plt.ylabel('TOTAL_CPU Usage')
plt.xlabel('Software Version')
plt.show()

# --- 4. STATISTICAL ANALYSIS ---

# Step 4.1: Kruskal-Wallis Test (Omnibus Test)
print("\n--- Performing Kruskal-Wallis H-test ---")
h_statistic, p_value_kruskal = stats.kruskal(*data_groups)
print(f"  - H-statistic: {h_statistic:.4f}")
print(f"  - p-value: {p_value_kruskal:.4f}")

alpha = 0.05
if p_value_kruskal >= alpha:
    print("\nThe test is not significant. No further post-hoc testing needed.")
    print("Conclusion: There is no statistically significant difference among the versions.")
else:
    print("\nThe test is significant. Proceeding with post-hoc analysis.")
    
    # Step 4.2: Dunn's Post-Hoc Test
    print("\n--- Performing Dunn's Post-Hoc Test ---")
    # This returns a DataFrame of p-values for each pairwise comparison
    p_values_dunn = sp.posthoc_dunn(combined_df, val_col='TOTAL_CPU', group_col='version', p_adjust='bonferroni')
    
    print("Dunn's Test Results (p-values):")
    print(p_values_dunn)

# --- 5. FINAL RANKING ---
print("\n--- Median CPU Usage for Ranking ---")
median_values = combined_df.groupby('version')['TOTAL_CPU'].median().sort_values(ascending=False)
print(median_values)
