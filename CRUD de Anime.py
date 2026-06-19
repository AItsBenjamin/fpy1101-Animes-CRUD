# ===============================
# CRUD DE ANIME - PYTHON
# ===============================

animes = []

# -------------------------
# Función para imprimir separadores
# -------------------------
def separador():
    print("=" * 40)

# -------------------------
# Función para pedir enteros con validación
# -------------------------
def pedir_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("❌ Error: debe ingresar un número entero.")

# -------------------------
# Verificar si el anime ya existe
# -------------------------
def anime_existe(nombre):
    for anime in animes:
        if anime["nombre"].lower() == nombre.lower():
            return True
    return False

# -------------------------
# CREATE - Agregar anime
# -------------------------
def agregar_anime():
    separador()
    print("🎬 AGREGAR NUEVO ANIME")
    separador()

    nombre = input("Nombre del anime: ").strip()
    if nombre == "":
        print("❌ El nombre no puede estar vacío.")
        return

    if anime_existe(nombre):
        print("❌ Este anime ya está registrado.")
        return

    genero = input("Género: ").strip()
    if genero == "":
        print("❌ El género no puede estar vacío.")
        return

    capitulos = pedir_entero("Cantidad de capítulos: ")
    temporadas = pedir_entero("Cantidad de temporadas: ")

    animes.append({
        "nombre": nombre,
        "genero": genero,
        "capitulos": capitulos,
        "temporadas": temporadas
    })

    print("✅ Anime agregado correctamente.")

# -------------------------
# READ - Mostrar animes
# -------------------------
def mostrar_animes():
    separador()
    print("📺 LISTA DE ANIMES")
    separador()

    if len(animes) == 0:
        print("No hay animes registrados.")
        return

    for i, anime in enumerate(animes, start=1):
        print(f"""
#{i}
Nombre     : {anime['nombre']}
Género     : {anime['genero']}
Capítulos  : {anime['capitulos']}
Temporadas : {anime['temporadas']}
""")

# -------------------------
# UPDATE - Editar anime
# -------------------------
def editar_anime():
    mostrar_animes()
    if len(animes) == 0:
        return

    try:
        indice = int(input("Seleccione el número del anime a editar: ")) - 1
        if indice < 0 or indice >= len(animes):
            print("❌ Opción inválida.")
            return
    except ValueError:
        print("❌ Debe ingresar un número válido.")
        return

    separador()
    print("✏️ EDITAR ANIME")
    separador()

    nombre = input("Nuevo nombre: ").strip()
    if nombre == "":
        print("❌ El nombre no puede estar vacío.")
        return

    genero = input("Nuevo género: ").strip()
    capitulos = pedir_entero("Nuevos capítulos: ")
    temporadas = pedir_entero("Nuevas temporadas: ")

    animes[indice] = {
        "nombre": nombre,
        "genero": genero,
        "capitulos": capitulos,
        "temporadas": temporadas
    }

    print("✅ Anime actualizado correctamente.")

# -------------------------
# DELETE - Eliminar anime
# -------------------------
def eliminar_anime():
    mostrar_animes()
    if len(animes) == 0:
        return

    try:
        indice = int(input("Seleccione el número del anime a eliminar: ")) - 1
        if indice < 0 or indice >= len(animes):
            print("❌ Opción inválida.")
            return
    except ValueError:
        print("❌ Debe ingresar un número válido.")
        return

    animes.pop(indice)
    print("🗑️ Anime eliminado correctamente.")

# -------------------------
# MENÚ PRINCIPAL
# -------------------------
def menu():
    while True:
        separador()
        print("🎌 SISTEMA CRUD DE ANIME 🎌")
        separador()
        print("""
1️⃣  Agregar anime
2️⃣  Mostrar animes
3️⃣  Editar anime
4️⃣  Eliminar anime
5️⃣  Salir
""")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_anime()
        elif opcion == "2":
            mostrar_animes()
        elif opcion == "3":
            editar_anime()
        elif opcion == "4":
            eliminar_anime()
        elif opcion == "5":
            separador()
            print("👋 Programa finalizado. ¡Hasta luego!")
            separador()
            break
        else:
            print("❌ Opción inválida. Intente nuevamente.")

menu()