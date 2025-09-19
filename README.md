# Performance Analysis of OpenMRS Software Versions

## Course Information
- **Course:** LOG 6309E - Intelligent DevOps
- **Assignment:** Individual Assignment: Analyzing Performance Data

## Project Description

This repository contains the data, analysis script, and final report for the individual assignment. The project aims to analyze and compare the CPU performance ("TOTAL_CPU") of four different versions of the OpenMRS software system: `base_version`, `version_1`, `version_2`, and `version_3`.

The analysis involves statistical techniques such as normality testing (Shapiro-Wilk), hypothesis testing (Mann-Whitney U, Kruskal-Wallis), and effect size calculation to draw evidence-based conclusions about performance differences.

## Repository Structure

- **/data**: Contains the raw performance data for each software version in `.xlsx` format.
- **/scripts**: Contains the main Python script `normality_analysis.py` used for all data loading, analysis, and visualization.
- **/output**: Contains the final deliverables.
  - **/output/figures**: Generated plots (histograms and Q-Q plots) from the analysis.
  - **/output/report.pdf**: The final report in PDF format.
- `requirements.txt`: A list of all Python dependencies required to run the analysis script.
- `README.md`: This file, explaining the project.

## How to Reproduce the Analysis

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/tassyla/log6309e-assignment-1.git](https://github.com/tassyla/log6309e-assignment-1.git)
    cd log6309e-assignment-1
    ```

2.  **Install dependencies:**
    Make sure you have Python 3 installed. Then, install the required libraries using pip:
    ```sh
    pip install -r requirements.txt
    ```

3.  **Run the analysis script:**
    Navigate to the `scripts` directory and run the Python script. The script will load data from the `../data` directory and generate plots.
    ```sh
    cd scripts
    python performance_analysis.py
    ```

## Summary of Results

The analysis concluded that the CPU usage data for all four versions are not normally distributed. Statistical tests revealed significant differences in performance between certain versions, with `version_3` showing the highest CPU consumption. For a detailed discussion of the results, please see the full `report.pdf` in the `/output` folder.