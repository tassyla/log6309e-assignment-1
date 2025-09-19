import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np

# --- 1. SETUP: File names and versions ---
file_names = {
    'base_version': '../data/base_version_perf.xlsx',
    'version_1':    '../data/version_1_perf.xlsx',
    'version_2':    '../data/version_2_perf.xlsx',
    'version_3':    '../data/version_3_perf.xlsx'
}

cpu_data = {}

# --- 2. DATA LOADING ---
print("--- Loading data for Q1 analysis---")
for version_name, file_path in file_names.items():
    try:
        # Load the Excel file and extract the 'TOTAL_CPU' column
        df = pd.read_excel(file_path)
        cpu_data[version_name] = df['TOTAL_CPU'].dropna() # Drop null values, if any
        print(f"Successfully loaded '{file_path}'. Found {len(cpu_data[version_name])} samples.")
    except FileNotFoundError:
        print(f"ERROR: File '{file_path}' not found. Please check the file name and location.")
        # Add sample data so the script doesn't break
        cpu_data[version_name] = pd.Series(np.random.randn(100))
    except KeyError:
        print(f"ERROR: Column 'TOTAL_CPU' not found in '{file_path}'. Please check the column name in your file.")
        cpu_data[version_name] = pd.Series(np.random.randn(100))
print("-" * 30 + "\n")


# --- 3. VISUAL ANALYSIS ---

# 3.1. Histograms for each version
plt.figure(figsize=(12, 8))
plt.suptitle('Histograms of TOTAL_CPU per Version', fontsize=16)
for i, (version_name, data) in enumerate(cpu_data.items()):
    plt.subplot(2, 2, i + 1)
    plt.hist(data, bins=30, edgecolor='k', alpha=0.7)
    plt.title(f'Version: {version_name}')
    plt.xlabel('TOTAL_CPU')
    plt.ylabel('Frequency')
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()

# 3.2. Q-Q (Quantile-Quantile) plots for each version
plt.figure(figsize=(12, 8))
plt.suptitle('Q-Q Plots of TOTAL_CPU per Version', fontsize=16)
for i, (version_name, data) in enumerate(cpu_data.items()):
    plt.subplot(2, 2, i + 1)
    stats.probplot(data, dist="norm", plot=plt)
    plt.title(f'Version: {version_name}')
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()


# --- 4. STATISTICAL TEST (SHAPIRO-WILK) ---
print("--- Normality Test Results (Shapiro-Wilk) ---")
alpha = 0.05 # Significance level

for version_name, data in cpu_data.items():
    if len(data) > 3: # Shapiro-Wilk requires at least 3 data points
        stat, p_value = stats.shapiro(data)
        print(f"\nVersion: {version_name}")
        print(f"  - Test Statistic: {stat:.4f}")
        print(f"  - p-value: {p_value:.4f}")
        
        # Interpreting the result
        if p_value > alpha:
            print("  - Conclusion: Data appears to be normally distributed (fail to reject H0).")
        else:
            print("  - Conclusion: Data is NOT normally distributed (reject H0).")
    else:
        print(f"\nVersion: {version_name} has too few data points to test for normality.")
print("-" * 55)