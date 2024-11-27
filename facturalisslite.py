import sqlite3
from sqlite3 import Error
import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_connection():
    try:
        connection = sqlite3.connect("facturaliss.db")
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def create_tables(connection):
    try:
        cursor = connection.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS vendedor (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                direccion TEXT NOT NULL,
                telefono TEXT NOT NULL,
                nit TEXT NOT NULL
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS cliente (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                direccion TEXT NOT NULL,
                telefono TEXT NOT NULL,
                nit TEXT NOT NULL
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS producto (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                categoria TEXT NOT NULL,
                precio REAL NOT NULL
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS factura (
                id INTEGER PRIMARY KEY,
                vendedor_id INTEGER NOT NULL,
                cliente_id INTEGER NOT NULL,
                fecha TEXT NOT NULL,
                fecha_entrega TEXT NOT NULL,
                FOREIGN KEY (vendedor_id) REFERENCES vendedor (id),
                FOREIGN KEY (cliente_id) REFERENCES cliente (id)
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS detalles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                factura_id INTEGER NOT NULL,
                codigo_producto INTEGER NOT NULL,
                cantidad INTEGER NOT NULL,
                extra TEXT,
                total REAL NOT NULL,
                FOREIGN KEY (factura_id) REFERENCES factura (id),
                FOREIGN KEY (codigo_producto) REFERENCES producto (id)
            )
        ''')

        connection.commit()
        print("Tablas creadas exitosamente.")
    except Error as e:
        print(f"Error: {e}")

def insertar_vendedor(connection):
    try:
        cls()
        nombre = input("Nombre del vendedor: ")
        direccion = input("Dirección del vendedor: ")
        telefono = input("Teléfono del vendedor: ")
        nit = input("NIT del vendedor: ")
        
        cursor = connection.cursor()
        cursor.execute('INSERT INTO vendedor (nombre, direccion, telefono, nit) VALUES (?, ?, ?, ?)', (nombre, direccion, telefono, nit))
        connection.commit()
        print("Vendedor ingresado exitosamente.")
    except Error as e:
        print(f"Error: {e}")

def insertar_cliente(connection):
    try:
        cls()
        nombre = input("Nombre del cliente: ")
        direccion = input("Dirección del cliente: ")
        telefono = input("Teléfono del cliente: ")
        nit = input("NIT del cliente: ")

        cursor = connection.cursor()
        cursor.execute('INSERT INTO cliente (nombre, direccion, telefono, nit) VALUES (?, ?, ?, ?)', (nombre, direccion, telefono, nit))
        connection.commit()
        print("Cliente ingresado exitosamente.")
    except Error as e:
        print(f"Error: {e}")

def insertar_producto(connection):
    try:
        cls()
        nombre = input("Nombre del producto: ")
        categoria = input("Categoría del producto: ")
        precio = float(input("Precio del producto: "))

        cursor = connection.cursor()
        cursor.execute('INSERT INTO producto (nombre, categoria, precio) VALUES (?, ?, ?)', (nombre, categoria, precio))
        connection.commit()
        print("Producto ingresado exitosamente.")
    except Error as e:
        print(f"Error: {e}")

def insertar_factura(connection):
    try:
        cls()
        id = int(input("ID de la factura: "))
        vendedor_id = int(input("ID del vendedor: "))
        cliente_id = int(input("ID del cliente: "))
        fecha = input("Fecha de la factura (YYYY-MM-DD): ")
        fecha_entrega = input("Fecha de entrega (YYYY-MM-DD): ")

        cursor = connection.cursor()
        cursor.execute('INSERT INTO factura (id, vendedor_id, cliente_id, fecha, fecha_entrega) VALUES (?, ?, ?, ?, ?)', (id, vendedor_id, cliente_id, fecha, fecha_entrega))
        connection.commit()
        print("Factura ingresada exitosamente.")
    except Error as e:
        print(f"Error: {e}")

def insertar_detalles(connection):
    try:
        cls()
        factura_id = int(input("ID de la factura: "))
        codigo_producto = int(input("Código del producto: "))
        cantidad = int(input("Cantidad: "))
        extra = input("Extra: ")
        total = float(input("Total: "))

        cursor = connection.cursor()
        cursor.execute('INSERT INTO detalles (factura_id, codigo_producto, cantidad, extra, total) VALUES (?, ?, ?, ?, ?)', (factura_id, codigo_producto, cantidad, extra, total))
        connection.commit()
        print("detalles ingresados exitosamente.")
    except Error as e:
        print(f"Error: {e}")

def mostrar_vendedores(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM vendedor")
        rows = cursor.fetchall()
        cls()
        for row in rows:
            print(row)
    except Error as e:
        print(f"Error: {e}")
    while True:
        opcion = input("Deseas salir: ").lower()
        if opcion == "si":
            break
        elif opcion == "no":
            print("OK, tomate tu tiempo")

def mostrar_clientes(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM cliente")
        rows = cursor.fetchall()
        cls()
        for row in rows:
            print(row)
    except Error as e:
        print(f"Error: {e}")
    while True:
        opcion = input("Deseas salir: ").lower()
        if opcion == "si":
            break
        elif opcion == "no":
            print("OK, tomate tu tiempo")

def mostrar_productos(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM producto")
        rows = cursor.fetchall()
        cls()
        for row in rows:
            print(row)
    except Error as e:
        print(f"Error: {e}")
    while True:
        opcion = input("deseas salir: ").lower()
        if opcion == "si":
            break
        elif opcion == "no":
            print("ok, cuando quieras")

def mostrar_productos_n(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM producto")
        rows = cursor.fetchall()
        cls()
        for row in rows:
            print(row)
    except Error as e:
        print(f"Error: {e}")

def mostrar_facturas(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM factura")
        rows = cursor.fetchall()
        for row in rows:
            cls()
            print(row)
    except Error as e:
        print(f"Error: {e}")
    while True:
        opcion = input("Deseas salir: ").lower()
        if opcion == "si":
            break
        elif opcion == "no":
            print("OK, tomate tu tiempo")

def mostrar_detalles(connection):


    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM detalles")
        rows = cursor.fetchall()
        cls()
        for row in rows:
            print(row)
    except Error as e:
        print(f"Error: {e}")
    while True:
        opcion = input("Deseas salir: ").lower()
        if opcion == "si":
            break
        elif opcion == "no":
            print("OK, tomate tu tiempo")

def mostrar_factura_completa(connection, factura_id):
    try:
        cursor = connection.cursor()

        # Obtener datos de la factura
        cursor.execute('''
            SELECT f.id, v.nombre, v.direccion, v.telefono, v.nit, 
                   c.nombre, c.direccion, c.telefono, c.nit, 
                   f.fecha, f.fecha_entrega
            FROM factura f
            JOIN vendedor v ON f.vendedor_id = v.id
            JOIN cliente c ON f.cliente_id = c.id
            WHERE f.id = ?
        ''', (factura_id,))
        factura = cursor.fetchone()

        if factura is None:
            print("Factura no encontrada.")
            while True:
                opcion = input("¿Deseas salir? ").lower()
                if opcion.lower() == "si":
                    break
                elif opcion.lower() == "no":
                    print("OK, tómate tu tiempo")
            return

        # Mostrar datos del vendedor
        print(f"{factura[1]}")
        print(f"Dirección: {factura[2]}")
        print(f"Teléfono: {factura[3]}")
        print(f"NIT: {factura[4]}")

        # Mostrar datos del cliente
        print("\nCliente:")
        print(f"Nombre: {factura[5]}")
        print(f"Dirección: {factura[6]}")
        print(f"Teléfono: {factura[7]}")
        print(f"NIT: {factura[8]}")

        # Mostrar datos de la factura
        print(f"Numero de Factura: {factura[0]}")
        print(f"Fecha: {factura[9]}")
        print(f"Fecha de Entrega: {factura[10]}")

        # Obtener detalles de la factura
        cursor.execute('''
            SELECT d.codigo_producto, p.nombre, p.precio, d.cantidad, d.extra, d.total
            FROM detalles d
            JOIN producto p ON d.codigo_producto = p.id
            WHERE d.factura_id = ?
        ''', (factura_id,))
        detalles = cursor.fetchall()

        # Mostrar detalles de la factura en una sola línea horizontal
        print("\nDetalles:")
        total = 0
        for detalle in detalles:
            print(f"Producto: {detalle[1]}, Precio: ${detalle[2]}, Cantidad: {detalle[3]}, Extra: ${detalle[4]}, Total: ${detalle[5]}")
            total += detalle[5]

        # Mostrar el total acumulado
        print(f"\nTotal: ${total}")
        while True:
            opcion = input("¿Deseas salir? ").lower()
            if opcion.lower() == "si":
                break
            elif opcion.lower() == "no":
                print("OK, tómate tu tiempo")
    
    except Error as e:
        print(f"Error: {e}")

def modificar_nit_vendedor(connection):
    try:
        cls()
        print("solo hay un vendedor usa el numero 1")
        vendedor_id = int(input("Ingrese el ID del vendedor: "))
        nuevo_nit = input("Ingrese el nuevo NIT del vendedor: ")
        cursor = connection.cursor()
        cursor.execute('UPDATE vendedor SET nit = ? WHERE id = ?', (nuevo_nit, vendedor_id))
        connection.commit()
        print("NIT del vendedor actualizado exitosamente.")
    except Error as e:
        print(f"Error: {e}")

def modificar_nit_cliente(connection):
    try:
        cls()
        mostrar_clientes(connection)
        cliente_id = int(input("Ingrese el ID del cliente: "))
        nuevo_nit = input("Ingrese el nuevo NIT del cliente: ")
        cursor = connection.cursor()
        cursor.execute('UPDATE cliente SET nit = ? WHERE id = ?', (nuevo_nit, cliente_id))
        connection.commit()
        print("NIT del cliente actualizado exitosamente.")
    except Error as e:
        print(f"Error: {e}")

def modificar_precio_producto(connection):
    try:
        cls()
        mostrar_productos_n(connection)
        producto_id = int(input("\nIngrese el ID del producto: "))
        nuevo_precio = float(input("Ingrese el nuevo precio del producto: "))
        cursor = connection.cursor()
        cursor.execute('UPDATE producto SET precio = ? WHERE id = ?', (nuevo_precio, producto_id))
        connection.commit()
        print("Precio del producto actualizado exitosamente.")
    except Error as e:
        print(f"Error: {e}")

def imprimir_factura_completa_txt(connection):
    try:
        factura_id = int(input("Ingrese el ID de la factura: "))
        cursor = connection.cursor()

        # Obtener datos de la factura
        cursor.execute('''
            SELECT f.id, v.nombre, v.direccion, v.telefono, v.nit, 
                   c.nombre, c.direccion, c.telefono, c.nit, 
                   f.fecha, f.fecha_entrega
            FROM factura f
            JOIN vendedor v ON f.vendedor_id = v.id
            JOIN cliente c ON f.cliente_id = c.id
            WHERE f.id = ?
        ''', (factura_id,))
        factura = cursor.fetchone()

        if factura is None:
            print("Factura no encontrada.")
            return

        detalles_str = []

        # Datos del vendedor
        detalles_str.append(f"{factura[1]}")
        detalles_str.append(f"Dirección: {factura[2]}")
        detalles_str.append(f"Teléfono: {factura[3]}")
        detalles_str.append(f"NIT: {factura[4]}")

        # Datos del cliente
        detalles_str.append("\nCliente:")
        detalles_str.append(f"Nombre: {factura[5]}")
        detalles_str.append(f"Dirección: {factura[6]}")
        detalles_str.append(f"Teléfono: {factura[7]}")
        detalles_str.append(f"NIT: {factura[8]}")

        # Datos de la factura
        detalles_str.append(f"Fecha: {factura[9]}")
        detalles_str.append(f"Fecha de Entrega: {factura[10]}")

        # Obtener detalles de la factura
        cursor.execute('''
            SELECT d.codigo_producto, p.nombre, p.precio, d.cantidad, d.extra, d.total
            FROM detalles d
            JOIN producto p ON d.codigo_producto = p.id
            WHERE d.factura_id = ?
        ''', (factura_id,))
        detalles = cursor.fetchall()

        # Mostrar detalles de la factura en una sola línea horizontal
        detalles_str.append("\nDetalles:")
        total = 0
        for detalle in detalles:
            detalles_str.append(f"Producto: {detalle[1]}, Precio: ${detalle[2]}, Cantidad: {detalle[3]}, Extra: {detalle[4]}, Total: ${detalle[5]}")
            total += detalle[5]

        # Mostrar el total acumulado
        detalles_str.append(f"\nTotal de la Factura: ${total}")

        # Escribir en el archivo txt
        with open(f"Factura_{factura_id}.txt", "w") as file:
            for line in detalles_str:
                file.write(line + "\n")

        print(f"Factura {factura_id} impresa en Factura_{factura_id}.txt")

    except Error as e:
        print(f"Error: {e}")

import json

def imprimir_factura_completa_json(connection):
    try:
        factura_id = int(input("Ingrese el ID de la factura: "))
        cursor = connection.cursor()

        # Obtener datos de la factura
        cursor.execute('''
            SELECT f.id, v.nombre AS vendedor_nombre, v.direccion AS vendedor_direccion, v.telefono AS vendedor_telefono, v.nit AS vendedor_nit, 
                   c.nombre AS cliente_nombre, c.direccion AS cliente_direccion, c.telefono AS cliente_telefono, c.nit AS cliente_nit, 
                   f.fecha, f.fecha_entrega
            FROM factura f
            JOIN vendedor v ON f.vendedor_id = v.id
            JOIN cliente c ON f.cliente_id = c.id
            WHERE f.id = ?
        ''', (factura_id,))
        factura = cursor.fetchone()

        if factura is None:
            print("Factura no encontrada.")
            return

        # Datos de la factura
        factura_dict = {
            "id de factura": factura[0],
            "vendedor": {
                "nombre": factura[1],
                "direccion": factura[2],
                "telefono": factura[3],
                "nit": factura[4]
            },
            "cliente": {
                "nombre": factura[5],
                "direccion": factura[6],
                "telefono": factura[7],
                "nit": factura[8]
            },
            "fecha": factura[9],
            "fecha_entrega": factura[10],
            "detalles": []
        }

        # Obtener detalles de la factura
        cursor.execute('''
            SELECT d.codigo_producto, p.nombre, p.precio, d.cantidad, d.extra, d.total
            FROM detalles d
            JOIN producto p ON d.codigo_producto = p.id
            WHERE d.factura_id = ?
        ''', (factura_id,))
        detalles = cursor.fetchall()

        total = 0
        for detalle in detalles:
            detalle_dict = {
                "producto": detalle[1],
                "precio": detalle[2],
                "cantidad": detalle[3],
                "extra": detalle[4],
                "total": detalle[5]
            }
            factura_dict["detalles"].append(detalle_dict)
            total += detalle[5]

        # Añadir el total acumulado
        factura_dict["total_factura"] = total

        # Escribir en el archivo JSON
        with open(f"Factura_{factura_id}.json", "w") as file:
            json.dump(factura_dict, file, indent=4)

        print(f"Factura {factura_id} impresa en Factura_{factura_id}.json")

    except Error as e:
        print(f"Error: {e}")




def main():
    connection = create_connection()
    if connection:
        create_tables(connection)
        
        while True:
            cls()
            print("===Facturas de LISS BAKERY===")
            print("\nOpciones:")
            print("1. INGRESAR DATOS")
            print("2. MOSTRAR DATOS")
            print("3. BUSCAR FACTURA")
            print("4. IMPRIMIR FACTURA")
            print('5. CERRAR')
            menu = input("\nElige una opción: ").lower()
            if menu == "1":
                cls()
                print("\nIngresar Datos:")
                print("1. Ingresar Vendedor")
                print("2. Ingresar Cliente")
                print("3. Ingresar Producto")
                print("4. Ingresar Factura")
                print("5. Ingresar Detalles")
                print('6. Cerrar')
                while True:
                    choice = input("Elige una opción: ").lower()
                    if choice == '1':
                        insertar_vendedor(connection)
                    elif choice == '2':
                        insertar_cliente(connection)
                    elif choice == '3':
                        insertar_producto(connection)
                    elif choice == '4':
                        insertar_factura(connection)
                    elif choice == '5':
                        insertar_detalles(connection)
                    elif choice == '6':
                        break
            elif menu == "2":
                cls()
                print("\nMostrar Datos:")
                print("1. Mostrar Vendedores")
                print("2. Mostrar Clientes")
                print("3. Mostrar Productos")
                print("4. Mostrar Facturas")
                print("5. Mostrar Detalles")
                print('6. Cerrar')
                while True:
                    choice = input("Elige una opción: ").lower()
                    if choice == '1':
                        mostrar_vendedores(connection)
                    elif choice == '2':
                        mostrar_clientes(connection)
                    elif choice == '3':
                        mostrar_productos(connection)
                    elif choice == '4':
                        mostrar_facturas(connection)
                    elif choice == '5':
                        mostrar_detalles(connection)
                    elif choice == '6':
                        break
            elif menu == '3':
                cls()
                factura_id = int(input("Ingrese el ID de la factura: "))
                mostrar_factura_completa(connection, factura_id) 
            elif menu == '4':
                imprimir_factura_completa_txt(connection)
            elif menu == '2323':
                while True:
                    cls()
                    print("===Menu secreto===")
                    print("1. Modificar NIT Liss Bakery")
                    print("2. Modificar NIT cliente")
                    print("3. Cambiar precio de productos")
                    print("4. Imprimir factura electronica")
                    print("Cerrar")
                    menu = input("Ingresa el item adecuado: ").lower()
                    if menu == "1":
                        modificar_nit_vendedor(connection)
                    elif menu == "2":
                        modificar_nit_cliente(connection)
                    elif menu == "3":
                        modificar_precio_producto(connection)
                    elif menu == "4":
                        imprimir_factura_completa_json(connection)
                    elif menu == "cerrar":
                        break
            elif menu == '5':
                break
            else:
                print('Ingresa una opción valida')


        connection.close()

if __name__ == '__main__':
    main()
