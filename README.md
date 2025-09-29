# qPCR Analytic Validation

Python script for **analytic validation of qPCR assays** using replicate Cq data.  
This tool calculates standard curve statistics, PCR efficiency, LOD, LOQ, and generates plots automatically.

---

## Features

- Calculate **mean and standard deviation** of Cq values per dilution  
- Generate **standard curve** and linear regression (slope, intercept, R²)  
- Compute **PCR efficiency (%)**  
- Determine **Limit of Detection (LOD)** and **Limit of Quantification (LOQ)**  
- Save results and plots to a dedicated `results/` folder  

---

## Requirements

- Python 3.8+  
- Packages: `pandas`, `numpy`, `matplotlib`, `scipy`  

Install dependencies:

```bash
pip install pandas numpy matplotlib scipy
