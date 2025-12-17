# ♻️ CLASIFICACIÓN DE BASURA PARA MUNICIPIOS LATINOAMERICANOS

![Python](https://img.shields.io/badge/Python-3.9%2B-blue) ![Flask](https://img.shields.io/badge/Backend-Flask-green) ![AI](https://img.shields.io/badge/AI-MobileNetV2-orange)

## 📖 Descripción
Plataforma de software inteligente para la gestión y clasificación de residuos. Utiliza **Visión Artificial (MobileNetV2)** para identificar objetos reciclables desde imágenes y emplea un sistema de **Active Learning** (Human-in-the-loop) que permite validar las predicciones para mejorar la precisión del sistema y generar estadísticas de impacto ambiental.

## 🚀 Funcionalidades
* **Clasificación Automática:** Detecta Plástico, Vidrio, Papel y Metal usando IA.
* **Dashboard Web:** Interfaz gráfica para visualización de métricas en tiempo real.
* **Simulador Manual:** Permite cargar imágenes para auditoría sin necesidad de sensores físicos.
* **Validación Humana:** Sistema de botones (Correcto/Incorrecto) para auditar a la IA y guardar datos reales.
* **Base de Datos Histórica:** Registro persistente de todas las detecciones en SQLite.

## 🛠️ Arquitectura del Software
El proyecto sigue el patrón **MVC (Modelo-Vista-Controlador)**:

1.  **Controlador (`app.py`):** Servidor Flask que gestiona la API y el flujo de datos.
2.  **Modelo (`models.py` & `classifier.py`):**
    * **IA:** Modelo pre-entrenado MobileNetV2 con pesos de ImageNet.
    * **DB:** SQLite para almacenamiento de transacciones.
3.  **Vista (`templates/index.html`):** Dashboard interactivo con Chart.js y Bootstrap.

## 📂 Estructura del Proyecto
```text
SMART_WASTE_APP/
├── app.py                 # Servidor Principal
├── models.py              # Gestión de Base de Datos
├── requirements.txt       # Dependencias
├── utils/
│   └── classifier.py      # Motor de IA
├── static/                # Archivos estáticos (CSS, Imágenes subidas)
└── templates/             # Interfaz de usuario (HTML)
