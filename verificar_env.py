import sys
import numpy as np
import pandas as pd
import sklearn
import sklearn_extra
import hdbscan
import scipy
import matplotlib
import seaborn as sns
import jupyter

print("=== VERIFICACIÓN DEL ENTORNO ===")
print(f"Python: {sys.version}")
print(f"jupyter: {jupyter.__version__}")
print(f"NumPy: {np.__version__}")
print(f"pandas: {pd.__version__}")
print(f"scikit-learn: {sklearn.__version__}")
print(f"scikit-learn-extra: {sklearn_extra.__version__}")
print(f"SciPy: {scipy.__version__}")
print(f"matplotlib: {matplotlib.__version__}")
print(f"seaborn: {sns.__version__}")
