import pandas as pd
import numpy as np

def cohen_d(x, y):
    """
    Calculates Cohen's d for independent samples.
    
    Parameters:
    x, y: Array-like sequences of data.
    
    Returns:
    d: Cohen's d statistic.
    """
    nx = len(x)
    ny = len(y)
    dof = nx + ny - 2
    
    mean_x, mean_y = np.mean(x), np.mean(y)
    std_x, std_y = np.std(x, ddof=1), np.std(y, ddof=1)
    
    # Calculate the pooled standard deviation
    pooled_std = np.sqrt(((nx - 1) * std_x ** 2 + (ny - 1) * std_y ** 2) / dof)
    
    # Calculate Cohen's d
    d = (mean_x - mean_y) / pooled_std
    
    return d

# --- 1. SETUP: File paths ---
base_version_path = '../data/base_version_perf.xlsx'
version_1_path = '../data/version_1_perf.xlsx'

# --- 2. DATA LOADING ---
print("--- Loading data for Q3 analysis ---")
try:
    df_base = pd.read_excel(base_version_path)
    df_v1 = pd.read_excel(version_1_path)

    cpu_base = df_base['TOTAL_CPU'].dropna()
    cpu_v1 = df_v1['TOTAL_CPU'].dropna()

    print("Data loaded successfully.")

except FileNotFoundError as e:
    print(f"ERROR: Could not find a file. Make sure the path is correct.")
    print(e)
    exit()
except KeyError:
    print("ERROR: Column 'TOTAL_CPU' not found. Please check the column names.")
    exit()

# --- 3. CALCULATE EFFECT SIZE (COHEN'S D) ---
print("\n--- Calculating Effect Size (Cohen's d) ---")

d_value = cohen_d(cpu_v1, cpu_base) # Comparing version_1 to base_version

print(f"  - Mean CPU (base_version): {np.mean(cpu_base):.4f}")
print(f"  - Mean CPU (version_1):    {np.mean(cpu_v1):.4f}")
print(f"  - Cohen's d: {d_value:.4f}")

# --- 4. INTERPRETATION ---
print("\n--- Interpretation ---")
abs_d = abs(d_value)

if abs_d >= 0.8:
    interpretation = "LARGE"
elif abs_d >= 0.5:
    interpretation = "MEDIUM"
else:
    interpretation = "SMALL"

print(f"The magnitude of the effect is considered {interpretation}.")
if d_value > 0:
    print("This indicates that, on average, version_1 has a higher CPU usage than base_version.")
else:
    print("This indicates that, on average, version_1 has a lower CPU usage than base_version.")
