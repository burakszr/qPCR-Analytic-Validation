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

## Usage

1. **Prepare your CSV file**  
   - Create a CSV named `cq_input_replicates.csv` with the following columns:
ReplicateID,logCopyNumber,Cq
S1_1,6,12.46
S1_2,6,12.46
S1_3,6,12.43
S2_1,5,15.86
S2_2,5,15.80
S2_3,5,15.87
…

   - Each dilution should have at least **3 technical replicates**.  

2. **Run the script**

```bash
python3 qPCR_analytic_validation.py

3.	View outputs
•	All results are saved in the results/ folder:
•	replicate_summary.csv → Mean and standard deviation of Cq per dilution
•	results_summary.csv → Slope, intercept, R², PCR efficiency, LOD, LOQ
•	standard_curve.png → Standard curve plot with error bars

4.	Interpret results
•	Check slope and efficiency to ensure PCR performance
•	Verify R² for standard curve linearity
•	Use LOD and LOQ for analytic validation of your qPCR assay



Example Output

Slope: -3.32
Intercept: 36.8
R²: 0.998
Efficiency: 99.8%
LOD: 0.72 Cq
LOQ: 2.40 Cq
