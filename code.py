import json
import os

archivo = "movimientos.json"

def guardar_datos():
    datos = {
        "conta_id": conta_id,
        "gastos": gastos
    }

    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)


def cargar_datos():
    global gastos, conta_id

    if not os.path.isfile(archivo):
        return

    with open(archivo, "r", encoding="utf-8") as f:
        datos = json.load(f)

    gastos = datos.get("gastos", [])
    conta_id = datos.get("conta_id", 0)


gastos = [ {
  "id": 1,
    "tipo": "gasto",
  "categoria": "comida",
  "descripcion": "tacos",
  "monto": 80.0,
  "fecha": "2026-04-28"

} ]

conta_id = 1

def ver_movimientos():
    for gasto in gastos:
        print(gasto['id'])
        print(f"tipo: [{gasto['tipo']}]"),
        print(f"Descripcion: {gasto['descripcion']}") #categoria, monto, fecha
        print(f"Categoria: {gasto['categoria']}")
        print(f"Monto: {gasto['monto']}")
        print(f"Fecha: {gasto['fecha']}")

def agregar_gasto():
    global conta_id
    tipo = input("Dame el tipo de movimiento: ")
    if not tipo:
        print("respuesta invalida")
        return




    gasto_new = input("Ingrese la categoria del gasto: ")
    if not gasto_new:
        print("Respuesta invalida")
        return
    descripcion = input("Ingrese la descripcion del gasto: ")
    if not descripcion:
        print("Resuesta invalida")
        return
    monto = input("Ingrese el monto del gasto: ")
    if not monto:
        print("Respuesta invalida")
        return
    try:
        monto = float(monto)
    except ValueError:
        print("respuesta invalida")
        return
    fecha = input("Ingrese la fecha del gasto en formato xx-MM-yy: ")
    if not fecha:
        print("respuesta invalida")
        return

    conta_id += 1
    gastos.append({
        "id": conta_id,
        "tipo": tipo,
        "categoria": gasto_new,
        "descripcion": descripcion,
        "monto": monto,
        "fecha": fecha
    })


def agregar_ingreso():
    global conta_id
    ingreso_new = input("Imgresa el ingreso: ")
    if not ingreso_new:
        print("respuesta invalida")
        return
    try:
        ingreso_new = float(ingreso_new)
    except ValueError:
        print("respuesta invalida")
        return
    conta_id += 1
    gastos.append({
        "id": conta_id,
        "tipo": "ingreso",
        "monto": ingreso_new
    })

def editar_movimiento():
    global conta_id
    movimiento = input("dime el id del movimiento a editar: ")
    if not movimiento:
        print("Respuesta invalida")
        return
    try:
        movimiento = int(movimiento)
    except ValueError:
        print("respuesta invalida")
    for gasto in gastos:
        if gasto['id'] == movimiento:
            cambio = input("Que deseas cambiar?\n1. tipo\n2. Categoria\n3. Descripcion\n4. Monto\n5. Fecha\n")
            if not cambio:
                print("respuesta invalida")
            try:
                cambio = int(cambio)
            except ValueError:
                print("respuesta invalida")


            if cambio == 1:
                tipo_new = input("Ingrese el tipo de movimiento: ")
                if not tipo_new:
                    print("respuesya invalida")
                    return
                gasto['tipo'] = tipo_new

            elif cambio == 2:
                categoria_new = input("Ingrese la categoria del movimiento: ")
                if not categoria_new:
                    print("respuesta invalida")
                    return
                gasto['categoria'] = categoria_new
            elif cambio == 3:
                descripcion_new = input("Ingrese la descripcion del movimiento: ")
                if not descripcion_new:
                    print("respuesta invalida")
                    return
            elif cambio == 4:
                    monto_new = input("ingrese el monto del movimiento: ")
                    if not monto_new:
                        print("respuesta invalida")
                        return
                    try:
                        monto_new = float(monto_new)
                    except ValueError:
                        print("respuesta invalida")
                        return
                    if monto_new <0:
                        print("respuesta invalida")
                        return
                    gasto['monto'] = monto_new
            elif cambio == 5:
                fecha_new = input("Ingresa la fecha del movimiento: ")
                if not fecha_new:
                    print("respuesta invalida")
                    return
                gasto['fecha'] = fecha_new

            else:
                print("opcion invalida")
                return

            print("movimeinto actualizado")



def filtrar_categoria():
    cate = input("Ingrese la categoria que desea filtrar: ")
    if not cate:
        print("respuesta invalida")
        return
    for gasto in gastos:
        if gasto['categoria'] == cate:
            print(gasto['id'])
            print(f"tipo: [{gasto['tipo']}]"),
            print(f"Descripcion: {gasto['descripcion']}")  #
            print(f"Categoria: {gasto['categoria']}")
            print(f"Monto: {gasto['monto']}")
            print(f"Fecha: {gasto['fecha']}")


def ingresos_gastos():
    total_ingresos = 0
    total_gastos = 0
    for movimiento in gastos:
        if movimiento['tipo'] == "ingreso":
            total_ingresos += movimiento['monto']
        elif movimiento['tipo'] == "gasto":
            total_gastos += movimiento['monto']

    balance = total_ingresos - total_gastos

    print(f"Balance: {balance}")


def salir():
    print("gracias por usar el programa")


cargar_datos()
while True:
    print("\n1. Ver movimientos")
    print("2. Agregar gastos")
    print("3. Agregar ingresos")
    print("4. Editar movimiento")
    print("5. Filtrar por categoria")
    print("6. Balance")
    print("7. Salir")

    main_option = input("\nIngrese la opcion que desea: ")
    try:
        main_option = int(main_option)
    except ValueError:
        print("respuesta invalida")
        continue

    if main_option == 1:
        ver_movimientos()
        guardar_datos()
    elif main_option == 2:
        agregar_gasto()
        guardar_datos()
    elif main_option == 3:
        agregar_ingreso()
        guardar_datos()
    elif main_option == 4:
        editar_movimiento()
        guardar_datos()
    elif main_option == 5:
        filtrar_categoria()
        guardar_datos()
    elif main_option == 6:
        ingresos_gastos()
        guardar_datos()
    elif main_option == 7:
        salir()
        guardar_datos()
        break












