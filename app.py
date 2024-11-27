from flask import Flask, request, jsonify, render_template
import sqlite3

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def connect_db():
    return sqlite3.connect('pedidos.db')

@app.route('/add_pedido', methods=['POST'])
def add_pedido():
    data = request.get_json()
    print(data)  # Ver los datos recibidos
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO pedidos (cliente, producto, detalle, fecha_pedido, fecha_entrega, total) VALUES (?, ?, ?, ?, ?, ?)", 
                       (data['cliente'], data['producto'], data['detalle'], data['fecha_pedido'], data['fecha_entrega'], data['total']))
        conn.commit()
        conn.close()
        return jsonify({'status': 'Pedido agregado exitosamente'})
    except Exception as e:
        print(f"Error al agregar pedido: {e}")
        return jsonify({'status': 'Error al agregar pedido'}), 500


@app.route('/pedidos', methods=['GET'])
def get_pedidos():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pedidos")
    pedidos = cursor.fetchall()
    conn.close()
    return jsonify([{'cliente': row[0], 'producto': row[1], 'detalle': row[2], 'fecha_pedido': row[3], 'fecha_entrega': row[4], 'total': row[5]} for row in pedidos])

if __name__ == '__main__':
    app.run(debug=True, port=5500)
