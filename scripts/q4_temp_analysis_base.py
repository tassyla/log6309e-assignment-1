import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# --- 1. SETUP: File path ---
base_version_path = '../data/base_version_perf.xlsx'

# --- 2. DATA LOADING ---
print("--- Loading data for Q4 analysis ---")
try:
    df_base = pd.read_excel(base_version_path)
    cpu_base = df_base['TOTAL_CPU'].dropna()
    print(f"Successfully loaded {len(cpu_base)} samples for base_version.")

except FileNotFoundError as e:
    print(f"ERROR: Could not find a file. Make sure the path is correct.")
    print(e)
    exit()
except KeyError:
    print("ERROR: Column 'TOTAL_CPU' not found. Please check the column name.")
    exit()

# --- 3. VISUAL ANALYSIS (LINE PLOT) ---
print("\n--- Generating Line Plot ---")
# Create a time index (0, 1, 2, ...) to represent the sequence of measurements
time_index = range(len(cpu_base))

plt.figure(figsize=(12, 6))
plt.plot(time_index, cpu_base, label='TOTAL_CPU', linewidth=1)
plt.title('Performance (CPU Usage) of base_version Over Time')
plt.xlabel('Time Interval (in 30-second steps)')
plt.ylabel('TOTAL_CPU Usage')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.show()

# --- 4. STATISTICAL TEST (SPEARMAN'S CORRELATION) ---
print("\n--- Performing Spearman's Rank Correlation Test ---")
# The null hypothesis (H0) is that there is no monotonic correlation between
# CPU usage and time.
correlation_coeff, p_value = stats.spearmanr(cpu_base, time_index)

print(f"  - Spearman's Correlation Coefficient (rho): {correlation_coeff:.4f}")
print(f"  - p-value: {p_value:.4f}")

# --- 5. INTERPRETATION ---
print("\n--- Conclusion ---")
alpha = 0.05
if p_value < alpha:
    print("The p-value is significant (p < 0.05). We reject the null hypothesis.")
    if correlation_coeff > 0:
        print("Conclusion: There IS a statistically significant positive correlation (upward trend) over time.")
    else:
        print("Conclusion: There IS a statistically significant negative correlation (downward trend) over time.")
else:
    print("The p-value is not significant (p >= 0.05). We fail to reject the null hypothesis.")
    print("Conclusion: There is NO statistically significant monotonic trend in performance over time.")
