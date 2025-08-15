# Analizador de CV con IA

Una herramienta de línea de comandos que utiliza un Modelo de Lenguaje Grande (LLM) para realizar un análisis cualitativo de currículums (CVs) en formato PDF. La herramienta evalúa la estructura, claridad y lenguaje del documento, y genera un análisis estructurado en formato JSON con sugerencias concretas para su mejora.

---

## Características

- Extrae texto directamente de archivos PDF.
- Analiza el contenido del CV en busca de claridad, impacto, uso de verbos de acción y cuantificación de logros.
- Genera una salida JSON estructurada con puntuaciones y sugerencias accionables.
- Soporta la exportación del análisis a un archivo `.txt`.

## Stack 

- **Python 3.9+**
- **LangChain:** Framework para LLMs.
- **Google Gemini:** Modelo de lenguaje.
- **PyMuPDF:** Extracción de texto de PDF.
- **Python-Dotenv:** Gestión de variables de entorno.

---

## Uso

Crear un archivo `.env` en la raíz del proyecto y añadir la clave de API de Google:

GOOGLE_API_KEY="tu_clave_de_api_aqui"

El script se ejecuta desde el directorio raíz del proyecto.

**Para imprimir el análisis en la consola:**
```bash
python -m src --cv_path ruta/a/tu/cv.pdf
```

**Para guardar el análisis en un archivo de texto:**
```bash
python -m src --cv_path ruta/a/tu/cv.pdf --output reporte.txt
```
