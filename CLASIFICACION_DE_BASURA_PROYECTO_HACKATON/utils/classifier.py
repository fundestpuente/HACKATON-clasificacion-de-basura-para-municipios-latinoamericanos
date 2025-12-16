import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import (
    MobileNetV2,
    preprocess_input,
    decode_predictions
)
from tensorflow.keras.preprocessing import image
import numpy as np

# ==========================================
# 1. CARGA DEL MODELO (una sola vez)
# ==========================================
print("--- Cargando Cerebro de IA (MobileNetV2)... ---")
model = MobileNetV2(weights="imagenet", include_top=True)
print(" IA Cargada exitosamente.")

# ==========================================
# 2. PALABRAS CLAVE POR CATEGORÍA
# ==========================================
KEYWORDS = {
    "PLASTICO": [
        "plastic", "bottle", "container", "bag", "cup", "tub", "jug",
        "bucket", "toy", "keyboard", "mouse", "remote", "soap"
    ],
    "VIDRIO": [
        "glass", "goblet", "wine", "jar", "vase", "flask", "perfume",
        "beer", "bottle"
    ],
    "PAPEL_CARTON": [
        "paper", "cardboard", "carton", "box", "envelope", "book",
        "notebook", "menu", "packet", "tissue", "towel"
    ],
    "METAL": [
        "can", "tin", "steel", "aluminum", "screw", "nail", "bolt",
        "key", "lock", "hammer", "knife", "spoon"
    ],
    "ORGANICO": [
        "banana", "apple", "orange", "lemon", "fruit", "vegetable",
        "food", "bread", "burger", "pizza", "meat", "fish",
        "plant", "flower", "leaf"
    ]
}

# ==========================================
# 3. FUNCIÓN PRINCIPAL
# ==========================================
def clasificar_imagen(img_path):
    try:
        # ---- Preprocesamiento ----
        img = image.load_img(img_path, target_size=(224, 224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)

        # ---- Predicción ----
        preds = model.predict(x, verbose=0)

        # TOP-5 predicciones
        decoded = decode_predictions(preds, top=5)[0]

        # ---- Sistema de votación por categoría ----
        scores = {
            "PLASTICO": 0.0,
            "VIDRIO": 0.0,
            "PAPEL_CARTON": 0.0,
            "METAL": 0.0,
            "ORGANICO": 0.0
        }

        for _, nombre, prob in decoded:
            nombre = nombre.lower()

            for categoria, palabras in KEYWORDS.items():
                if any(p in nombre for p in palabras):
                    scores[categoria] += prob

        # ---- Decisión final ----
        categoria_final = max(scores, key=scores.get)
        confianza = round(scores[categoria_final] * 100, 2)

        # Nombre del objeto (solo informativo)
        nombre_objeto = decoded[0][1]

        # ---- Correcciones lógicas simples ----
        if "glass" in nombre_objeto or "jar" in nombre_objeto:
            categoria_final = "VIDRIO"

        if confianza < 5:
            categoria_final = "DESCONOCIDO"

        return nombre_objeto, categoria_final, confianza

    except Exception as e:
        print("Error procesando imagen:", e)
        return "Error", "DESCONOCIDO", 0.0


# ==========================================
# 4. PRUEBA LOCAL
# ==========================================
if __name__ == "__main__":
    print("Ejecuta desde Flask para ver resultados reales.")
