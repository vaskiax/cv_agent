# src/utils.py
import fitz
import json 
from typing import Dict


def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extrae el texto del archivo PDF.

    Args:
        pdf_path: La ruta al archivo.

    Returns:
        El contenido de texto completo del archivo.
    """
    
    try:
        doc = fitz.open(pdf_path)
        full_text = ""
        for page in doc:
            full_text += page.get_text()
        doc.close()
        return full_text
    
    except Exception as e:
        print(f"Un error inesperado ocurrió al leer el PDF: {e}")
        return ""
    
def save_analysis_to_txt(analysis_data: Dict, output_path: str) -> bool:
    """
    Guarda el diccionario del análisis en un archivo de texto con formato JSON.

    Args:
        analysis_data: El diccionario que contiene el análisis de la IA.
        output_path: La ruta al archivo .txt donde se guardará el resultado.

    Returns:
        True si se guardó correctamente, False si hubo un error.
    """
    
    try:
        report_content = json.dumps(analysis_data, indent=2, ensure_ascii=False)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(report_content)
        return True
    
    except Exception as e:
        print(f"Error al guardar el análisis en {output_path}: {e}")
        return False