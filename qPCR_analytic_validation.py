import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
import os

# ---------------- USER PARAMETERS ----------------
input_file = "cq_input_replicates.csv"   # your CSV file
outdir = "results"
plot_standard_curve = True

# ---------------- CREATE OUTPUT DIRECTORY ----------------
if not os.path.exists(outdir):
    os.makedirs(outdir)

# ---------------- LOAD DATA ----------------
df = pd.read_csv(input_file)  # CSV must be comma-separated (UTF-8)

# Check columns
expected_cols = {'ReplicateID','logCopyNumber','Cq'}
if not expected_cols.issubset(df.columns):
    raise ValueError(f"CSV must contain columns: {expected_cols}")

# ---------------- SUMMARY STATS ----------------
summary = df.groupby('logCopyNumber')['Cq'].agg(['mean','std']).reset_index()
summary.rename(columns={'mean':'Cq_mean','std':'Cq_std'}, inplace=True)

# ---------------- STANDARD CURVE ----------------
x = summary['logCopyNumber']
y = summary['Cq_mean']

slope, intercept, r_value, _, _ = linregress(x,y)
efficiency = (10**(-1/slope) - 1) * 100

# ---------------- LOD & LOQ ----------------
blank_cqs = df[df['logCopyNumber'] == 0]['Cq']
if len(blank_cqs) >= 2:
    noise_std = blank_cqs.std()
    LOD = 3 * noise_std
    LOQ = 10 * noise_std
else:
    LOD, LOQ = np.nan, np.nan

# ---------------- PLOT STANDARD CURVE ----------------
if plot_standard_curve:
    plt.figure(figsize=(6,6))
    plt.errorbar(summary['logCopyNumber'], summary['Cq_mean'],
                 yerr=summary['Cq_std'], fmt='o', capsize=5)
    plt.plot(x, slope*x + intercept, 'r')
    plt.xlabel("log10(Copy Number)")
    plt.ylabel("Cq (mean ± SD)")
    plt.title(f"Standard Curve\nSlope={slope:.3f}, R²={r_value**2:.3f}, Eff={efficiency:.1f}%")
    plt.tight_layout()
    plt.savefig(f"{outdir}/standard_curve.png")
    plt.close()

# ---------------- SAVE RESULTS ----------------
with open(f"{outdir}/results_summary.csv","w") as f:
    f.write("Slope,Intercept,R²,Efficiency(%),LOD,LOQ\n")
    f.write(f"{slope:.3f},{intercept:.3f},{r_value**2:.3f},{efficiency:.1f},{LOD:.2f},{LOQ:.2f}\n")

summary.to_csv(f"{outdir}/replicate_summary.csv", index=False)

print("✅ qPCR analytic validation complete!")
print(f"Results saved in folder: {outdir}/")