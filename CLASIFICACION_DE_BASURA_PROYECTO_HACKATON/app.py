from flask import Flask, render_template, request, redirect, url_for, jsonify
import os
import models
from utils.classifier import clasificar_imagen

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Asegurar que existe la carpeta
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    # Obtener el último escaneo para mostrarlo en grande
    ultimo = models.obtener_ultimo_registro()
    return render_template('index.html', ultimo=ultimo)

@app.route('/upload', methods=['POST'])
def upload_file():
    """
    Este endpoint sirve tanto para el ESP32 como para subir archivos manuales
    """
    if 'imageFile' not in request.files:
        return "No file part", 400
    
    file = request.files['imageFile']
    if file.filename == '':
        return "No selected file", 400

    if file:
        # 1. Guardar imagen
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        # 2. Llamar a la IA
        obj_name, categoria, conf = clasificar_imagen(filepath)

        # 3. Guardar en Base de Datos
        models.guardar_registro(obj_name, categoria, conf, filepath)

        # Si viene del navegador, recargar página. Si viene del ESP32, devolver texto.
        return redirect(url_for('index'))

@app.route('/api/stats')
def stats():
    """Endpoint para alimentar las gráficas con JSON"""
    data = models.obtener_estadisticas() # [(Categoria, Cantidad), ...]
    labels = [row[0] for row in data]
    values = [row[1] for row in data]
    return jsonify({'labels': labels, 'values': values})

@app.route('/feedback', methods=['POST'])
def feedback():
    """Recibir corrección del humano"""
    id_registro = request.form.get('id')
    accion = request.form.get('accion') # 'correcto' o 'incorrecto'
    
    es_correcto = True if accion == 'correcto' else False
    categoria_real = request.form.get('real_category') if not es_correcto else None
    
    models.actualizar_feedback(id_registro, es_correcto, categoria_real)
    return redirect(url_for('index'))

if __name__ == '__main__':
    # host='0.0.0.0' permite que el ESP32 se conecte desde la red
    app.run(host='0.0.0.0', port=5000, debug=True)