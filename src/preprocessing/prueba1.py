import numpy as np
import pandas as pd

np.random.seed(42)
data = {
    'edad': np.random.randint(18, 80, 1000),
    'nivel_educativo': np.random.randint(1, 6, 1000),
    'ingreso_mensual': np.random.randint(1000, 15000, 1000),
    'ubicacion': np.random.choice(['Urbano', 'Rural'], 1000)
}

df = pd.DataFrame(data)
print(df.head())
print(f"\nDataset: {df.shape[0]} votantes, {df.shape[1]} características")
print(f"\nTipos de datos:\n{df.dtypes}")