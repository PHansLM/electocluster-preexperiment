from sklearn.preprocessing import MinMaxScaler

numeric_features = ['edad', 'nivel_educativo', 'ingreso_mensual']
scaler = MinMaxScaler()

df_normalized = df.copy()
df_normalized[numeric_features] = scaler.fit_transform(df[numeric_features])

print("Datos originales (primeras 3 filas):")
print(df[numeric_features].head(3))
print("\nDatos normalizados (primeras 3 filas):")
print(df_normalized[numeric_features].head(3))
print(f"\nEstadísticas de normalización:")
print(df_normalized[numeric_features].describe())