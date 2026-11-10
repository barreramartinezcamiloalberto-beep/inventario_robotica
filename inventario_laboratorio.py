inventario = []


def buscar_componente(id_componente):
    """Devuelve el componente con ese ID o None si no existe."""
    for componente in inventario:
        if componente["id"] == id_componente:
            return componente
    return None


def registrar_componente():
    id_componente = input("ID del componente: ").strip()

    if not id_componente:
        print("El ID no puede estar vacío.")
        return

    if buscar_componente(id_componente) is not None:
        print("Ya existe un componente con ese ID.")
        return

    nombre = input("Nombre: ").strip()
    categoria = input("Categoría: ").strip()

    if not nombre or not categoria:
        print("El nombre y la categoría no pueden estar vacíos.")
        return

    try:
        stock = int(input("Stock inicial: "))
        precio_unitario = float(input("Precio unitario: "))
    except ValueError:
        print("El stock debe ser un entero y el precio debe ser un número.")
        return

    if stock < 0 or precio_unitario < 0:
        print("El stock y el precio no pueden ser negativos.")
        return

    componente = {
        "id": id_componente,
        "nombre": nombre,
        "categoria": categoria,
        "stock": stock,
        "precio_unitario": precio_unitario,
    }
    inventario.append(componente)
    print("Componente registrado correctamente.")


def mostrar_componente(componente):
    print(
        f"ID: {componente['id']} | Nombre: {componente['nombre']} | "
        f"Categoría: {componente['categoria']} | Stock: {componente['stock']} | "
        f"Precio: ${componente['precio_unitario']:.2f}"
    )


def consultar_inventario():
    if not inventario:
        print("El inventario está vacío.")
        return

    print("\n1. Mostrar todos los componentes")
    print("2. Filtrar por categoría")
    opcion = input("Elige una opción: ").strip()

    if opcion == "1":
        for componente in inventario:
            mostrar_componente(componente)
    elif opcion == "2":
        categoria_buscada = input("Categoría que deseas consultar: ").strip()
        encontrados = 0

        for componente in inventario:
            if componente["categoria"].lower() == categoria_buscada.lower():
                mostrar_componente(componente)
                encontrados += 1

        if encontrados == 0:
            print("No hay componentes en esa categoría.")
    else:
        print("Opción no válida.")


def actualizar_stock():
    id_componente = input("ID del componente: ").strip()
    componente = buscar_componente(id_componente)

    if componente is None:
        print("No se encontró un componente con ese ID.")
        return

    print(f"Stock actual de {componente['nombre']}: {componente['stock']}")
    print("1. Sumar unidades")
    print("2. Restar unidades")
    operacion = input("Elige una opción: ").strip()

    if operacion not in ("1", "2"):
        print("Opción no válida.")
        return

    try:
        unidades = int(input("Cantidad de unidades: "))
    except ValueError:
        print("La cantidad debe ser un número entero.")
        return

    if unidades <= 0:
        print("La cantidad debe ser mayor que cero.")
        return

    if operacion == "1":
        componente["stock"] += unidades
    elif unidades <= componente["stock"]:
        componente["stock"] -= unidades
    else:
        print("No se puede restar esa cantidad: el stock no puede ser negativo.")
        return

    print(f"Stock actualizado: {componente['stock']} unidades.")


while True:
    print("\n=== Inventario del Laboratorio de Robótica ===")
    print("1. Registrar componente")
    print("2. Consultar inventario")
    print("3. Actualizar stock")
    print("4. Salir")

    opcion = input("Elige una opción: ").strip()

    if opcion == "1":
        registrar_componente()
    elif opcion == "2":
        consultar_inventario()
    elif opcion == "3":
        actualizar_stock()
    elif opcion == "4":
        print("Programa finalizado.")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")