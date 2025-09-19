import pandas as pd
from scipy import stats

# --- 1. SETUP: File paths ---
base_version_path = '../data/base_version_perf.xlsx'
version_1_path = '../data/version_1_perf.xlsx'

# --- 2. DATA LOADING ---
print("--- Loading data for Q2 analysis ---")
try:
    df_base = pd.read_excel(base_version_path)
    df_v1 = pd.read_excel(version_1_path)

    # Extract the 'TOTAL_CPU' column for each version
    cpu_base = df_base['TOTAL_CPU'].dropna()
    cpu_v1 = df_v1['TOTAL_CPU'].dropna()

    print(f"Successfully loaded {len(cpu_base)} samples for base_version.")
    print(f"Successfully loaded {len(cpu_v1)} samples for version_1.")

except FileNotFoundError as e:
    print(f"ERROR: Could not find a file. Make sure the path is correct.")
    print(e)
    exit() # Exit the script if data can't be loaded
except KeyError:
    print("ERROR: Column 'TOTAL_CPU' not found in one of the files. Please check the column names.")
    exit()

# --- 3. STATISTICAL TEST (MANN-WHITNEY U) ---
print("\n--- Performing Mann-Whitney U Test ---")

# The null hypothesis (H0) is that the distributions of the two samples are equal.
# The alternative hypothesis (H1) is that the distributions are not equal.
statistic, p_value = stats.mannwhitneyu(cpu_base, cpu_v1, alternative='two-sided')

print(f"  - U-statistic: {statistic:.4f}")
print(f"  - p-value: {p_value}") # Print the full p-value, it might be very small

# --- 4. INTERPRETATION ---
alpha = 0.05 # Significance level

print("\n--- Conclusion ---")
if p_value < alpha:
    print(f"The p-value ({p_value:.4f}) is less than {alpha}.")
    print("We reject the null hypothesis.")
    print("Conclusion: There IS a statistically significant difference in CPU performance between base_version and version_1.")
else:
    print(f"The p-value ({p_value:.4f}) is greater than or equal to {alpha}.")
    print("We fail to reject the null hypothesis.")
    print("Conclusion: There is NO statistically significant difference in CPU performance between base_version and version_1.")