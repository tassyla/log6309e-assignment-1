# Performance Analysis of OpenMRS Software Versions

## Course Information
- **Course:** LOG 6309E - Intelligent DevOps
- **Assignment:** Individual Assignment: Analyzing Performance Data

## Project Description

This repository contains the data, analysis script, and final report for an assignment focused on performance analysis. The project investigates the CPU usage ("TOTAL_CPU") of four different versions of the OpenMRS software system: `base_version`, `version_1`, `version_2`, and `version_3`.

The analysis determined that the performance data is not normally distributed, leading to the use of non-parametric statistical methods. Key questions regarding statistical differences, the magnitude of these differences, performance trends over time, and a final ranking of the versions are addressed using techniques like the Mann-Whitney U test, Kruskal-Wallis test, Dunn's post-hoc test, and Cohen's d for effect size.

## Repository Structure

- **/data**: Contains the raw performance data for each software version in `.xlsx` format.
- **/scripts**: Contains all Python scripts that were used for each question.
- **/output**: Contains the final deliverables.
  - **/output/figures**: Generated plots (histograms, Q-Q plots, line plot, boxplots) from the analysis.
  - **/output/instructions.pdf**: The given instructions for the assignment.
  - **/output/report.pdf**: The final report in PDF format.
- `requirements.txt`: A list of all Python dependencies required to run the analysis script.
- `.gitignore`: Specifies files for Git to ignore.
- `README.md`: This explanatory file.

## How to Reproduce the Analysis

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/tassyla/log6309e-assignment-1.git
    cd log6309e-assignment-1
    ```

2.  **Install dependencies:**
    Ensure you have Python 3 installed. Then, install the required libraries using pip:
    ```sh
    pip install -r requirements.txt
    ```

3.  **Run the analysis script:**
    The `scripts/` folder provides each analyses from Q1 to Q5.
    ```sh
    python scripts/test.py
    ```
    The script will print all statistical results to the console.

## Summary of Results

The analysis provided several key insights into the performance evolution across the software versions:

* **Non-Normal Data:** The CPU usage data for all four versions was found to be **not normally distributed**, which dictated the use of non-parametric tests for all subsequent comparisons.

* **Stable Baseline:** The `base_version` demonstrated a stable performance profile over time. Although a statistically significant downward trend was detected, its magnitude was **practically negligible** (Spearman's ρ = -0.09), confirming its reliability as a baseline for comparisons.

* **All Versions are Statistically Distinct:** A Kruskal-Wallis test followed by Dunn's post-hoc test revealed that **every version is statistically different from every other version**.

* **Performance Ranking & Evolution:** Based on median CPU usage, the versions were ranked from highest to lowest consumption:
    1.  **`version_2`** (Median CPU: 50.53) - A minor performance regression from the baseline.
    2.  **`base_version`** (Median CPU: 49.66) - The reference point.
    3.  **`version_1`** (Median CPU: 48.72) - A small but significant performance improvement.
    4.  **`version_3`** (Median CPU: 4.22) - A massive and radical performance optimization.

In conclusion, the software's performance did not evolve linearly. A small gain in `version_1` was followed by a small loss in `version_2`. Most notably, `version_3` introduced a fundamental change that drastically reduced CPU consumption, marking a major success in optimization.