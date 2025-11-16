# Electocluster — Pre-experimento

Breve README para el pre-experimento de clustering electoral. Contiene instrucciones mínimas para preparar el entorno, descargar los datos de LAPOP necesarios para algunas pruebas y ejecutar los notebooks.

## Descripción

Este repositorio contiene experimentos y scripts para pruebas preliminares de clustering sobre datos de encuestas (ej. LAPOP). El objetivo es preparar un pipeline ligero para:

- cargar y verificar datasets (ej. LAPOP Bolivia 2023),
- normalizar variables, probar distintos algoritmos de clustering (K-Medoids, DBSCAN, jerárquico),
- generar visualizaciones de prueba (scatter, boxplot, dendrograma, heatmap),
- calcular métricas de validación de clustering.

Los notebooks en `notebooks/` contienen pruebas y ejemplos (generación de datos de muestra y uso del dataset LAPOP cuando está disponible).

## Estructura relevante

- `data/raw/` — aquí debes colocar los archivos de datos (NO se suben al repo por `.gitignore`).
- `data/processed/` — salidas procesadas (ignoradas por defecto).
- `notebooks/` — notebooks de exploración y pruebas (ej. `02_pruebas_preprocesamiento.ipynb`).
- `src/` — código fuente y utilidades.
- `requirements.txt` — lista de dependencias Python.

## Datos (LAPOP)

Para algunas pruebas se usa el dataset de LAPOP (por ejemplo `lapop_bolivia_2023.dta`).

Pasos recomendados:

1. Descarga el(s) archivo(s) desde el sitio oficial de LAPOP (o la fuente autorizada que uses).
2. Coloca el archivo en `data/raw/` con el mismo nombre que esperan los notebooks: `data/raw/lapop_bolivia_2023.dta`.

Nota: los notebooks del directorio suponen la ruta relativa `../data/raw/lapop_bolivia_2023.dta` desde `notebooks/` — ajusta la ruta si colocas el archivo en otra carpeta.

## Dependencias e instalación (PowerShell)

Se recomienda crear un entorno virtual limpio. En PowerShell (Windows):

```powershell
cd C:\electocluster
# Crear entorno virtual (usar nombre que prefieras)
python -m venv .venv

# Activar el entorno
.\.venv\Scripts\Activate.ps1

# Instalar dependencias
pip install --upgrade pip
pip install -r requirements.txt

# (Opcional) Si ya usas otro virtualenv como 'venv_clustering', actívalo en lugar de crear uno nuevo.
```

Si tienes problemas con permisos en PowerShell al activar el entorno (ExecutionPolicy), puedes ejecutar `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` antes de activar — hazlo sólo si comprendes las implicaciones.

## Ejecutar notebooks

Con el entorno activado:

```powershell
pip install jupyterlab notebook  # si no están instalados
jupyter lab
# o
jupyter notebook
```

Abre `notebooks/02_pruebas_preprocesamiento.ipynb` y ejecuta las celdas. Asegúrate de que `data/raw/lapop_bolivia_2023.dta` esté en `data/raw/` si vas a correr la sección que carga LAPOP.
