# src/__main__.py

import argparse
import os
import json
from dotenv import load_dotenv
from .utils import extract_text_from_pdf, save_analysis_to_txt
from .analyzer import analyze_cv

def main():
    
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("Error: La variable de entorno GOOGLE_API_KEY no está configurada.")
        return

    parser = argparse.ArgumentParser(description="Analizador de Calidad de CVs con IA.")
    parser.add_argument("--cv_path", required=True, help="Ruta al CV en formato PDF.")
    parser.add_argument("--output", help="Ruta opcional al archivo de salida .txt donde se guardará el análisis.") # <--- NUEVO ARGUMENTO
    
    args = parser.parse_args()

    print(f"Leyendo y extrayendo texto del CV en: {args.cv_path}...")
    cv_text = extract_text_from_pdf(args.cv_path)

    if not cv_text:
        print("No se pudo procesar el archivo PDF. Saliendo.")
        return

    try:
        analysis = analyze_cv(cv_text, api_key)
        
        if args.output:
            if save_analysis_to_txt(analysis, args.output):
                print(f"\n✅ Análisis guardado exitosamente en: {args.output}")
        else:
            print("\n--- Análisis de Calidad del CV Completado ---")
            print(json.dumps(analysis, indent=2, ensure_ascii=False))
            print("--- Fin del Análisis ---")

    except Exception as e:
        print(f"\nOcurrió un error durante el análisis de la IA: {e}")

if __name__ == "__main__":
    main()