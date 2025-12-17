# ♻️ CLASIFICACIÓN DE BASURA PARA MUNICIPIOS LATINOAMERICANOS

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Flask](https://img.shields.io/badge/Backend-Flask-green)
![AI](https://img.shields.io/badge/AI-MobileNetV2-orange)

## 📖 Descripción
Plataforma de software inteligente para la **clasificación automática de residuos reciclables**, orientada a apoyar a municipios y comunidades latinoamericanas en la correcta separación de desechos.

El sistema utiliza **Visión Artificial con MobileNetV2** para identificar residuos a partir de imágenes y un enfoque de **Active Learning (Human-in-the-Loop)** que permite validar las predicciones, mejorar progresivamente la precisión del modelo y generar **estadísticas reales de impacto ambiental**.

La solución es accesible desde cualquier dispositivo con navegador web, lo que permite su uso inmediato sin necesidad de aplicaciones móviles o infraestructura compleja.

---

## 🚀 Funcionalidades

* **Clasificación Automática:**  
  Identificación de residuos reciclables como **Plástico, Vidrio, Papel/Cartón y Metal** mediante inteligencia artificial.

* **Dashboard Web:**  
  Visualización clara de métricas y estadísticas en tiempo real para análisis y toma de decisiones.

* **Simulador Manual:**  
  Carga de imágenes desde cualquier dispositivo para pruebas, auditoría y validación sin sensores físicos.

* **Validación Humana:**  
  Sistema de retroalimentación (Correcto / Incorrecto) que permite mejorar el modelo y generar datos confiables.

* **Base de Datos Histórica:**  
  Registro persistente de todas las detecciones utilizando **SQLite** para análisis posterior.

---

## 🛠️ Arquitectura del Software
El proyecto sigue el patrón **MVC (Modelo–Vista–Controlador)**:

1. **Controlador (`app.py`):**  
   Servidor Flask encargado de la lógica del sistema, API y flujo de datos.

2. **Modelo (`models.py` & `classifier.py`):**  
   * **IA:** MobileNetV2 preentrenado con pesos de ImageNet.  
   * **DB:** Base de datos SQLite para almacenamiento de registros.

3. **Vista (`templates/index.html`):**  
   Dashboard web interactivo desarrollado con **Bootstrap** y **Chart.js**.

---

## 📂 Estructura del Proyecto
```text
CLASIFICACION_DE_BASURA_PROYECTO_HACKATON/
├── app.py                 # Servidor principal (Flask)
├── models.py              # Gestión de base de datos
├── requirements.txt       # Dependencias del proyecto
├── utils/
│   └── classifier.py      # Motor de clasificación con IA
├── static/                # Archivos estáticos e imágenes
└── templates/             # Interfaz web (HTML)
