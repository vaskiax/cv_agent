# src/analyzer.py

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from typing import Dict

def analyze_cv(cv_text: str, api_key: str) -> Dict:
    """
    Analiza la calidad de un CV usando un LLM.

    Args:
        cv_text: El texto extraído del CV.
        api_key: La clave de API para el servicio LLM.

    Returns:
        Un diccionario con el análisis estructurado.
    """
    prompt_template = """
    Eres un experto en reclutamiento técnico y un coach de carrera de élite. Tu tarea es analizar la calidad intrínseca del siguiente CV.
    No lo estás comparando con una oferta de trabajo, estás evaluando qué tan bien está escrito y estructurado para el mercado laboral tecnológico en general. El análisis completo, incluyendo el formato JSON, debe estar en español.

    **Contenido del CV:**
    {cv_text}

    Basado exclusivamente en el contenido del CV, por favor proporciona un análisis en formato JSON con las siguientes claves en español:
    - "puntaje_claridad": Un puntaje de 0 a 10 evaluando la claridad, concisión y facilidad de lectura del CV, como un número entero.
    - "puntaje_impacto": Un puntaje de 0 a 10 evaluando si el CV utiliza lenguaje de impacto y métricas cuantificables para demostrar logros, como un número entero.
    - "habilidades_clave_identificadas": Una lista de las 5-7 habilidades técnicas o competencias más importantes que se pueden extraer del CV.
    - "analisis_verbos_accion": Un análisis breve sobre el uso de verbos de acción fuertes (ej. "Lideré", "Implementé", "Optimicé") al describir la experiencia.
    - "analisis_cuantificacion": Un análisis sobre si el candidato cuantifica sus logros con números y métricas (ej. "reduje el tiempo de respuesta en un 20%").
    - "sugerencias_concretas_mejora": Una lista de 3 a 5 sugerencias muy específicas y accionables para mejorar el impacto general de este CV. Por ejemplo, "Reemplazar 'Responsable de...' por un verbo de acción como 'Gestioné...' o 'Desarrollé...'", "Añadir métricas específicas a los logros en el puesto de 'Desarrollador de Software', como el porcentaje de mejora o el número de usuarios impactados."
    """
    
    model = ChatGoogleGenerativeAI(model="gemini-2.5-pro", google_api_key=api_key)
    parser = JsonOutputParser()
    
    prompt = ChatPromptTemplate.from_template(
        template=prompt_template,
        partial_variables={"format_instructions": parser.get_format_instructions()}
    )
    
    chain = prompt | model | parser
    
    print("Analizando la calidad del CV... Esto puede tardar un momento.")
    response = chain.invoke({"cv_text": cv_text})
    
    return response