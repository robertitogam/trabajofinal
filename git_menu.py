import os

def run_cmd(cmd):
    result = os.system(cmd)
    return result == 0

def menu():
    print("\n¿Qué quieres hacer con Git?")
    print("1. Agregar todos los archivos (git add .)")
    print("2. Hacer commit con mensaje")
    print("3. Hacer push al repositorio")
    print("4. Agregar + Commit + Push")
    print("5. Salir")

while True:
    menu()
    opcion = input("Elige una opción (1-5): ")

    if opcion == "1":
        print("Agregando archivos...")
        if run_cmd("git add ."):
            print("Archivos agregados correctamente.")
        else:
            print("Error al agregar archivos.")
    elif opcion == "2":
        msg = input("Escribe el mensaje del commit: ")
        if run_cmd(f'git commit -m "{msg}"'):
            print("Commit realizado.")
        else:
            print("Error al hacer commit. ¿Seguro que hay cambios para commitear?")
    elif opcion == "3":
        print("Haciendo push...")
        if run_cmd("git push"):
            print("Push exitoso.")
        else:
            print("Error al hacer push.")
    elif opcion == "4":
        msg = input("Escribe el mensaje del commit: ")
        print("Agregando archivos...")
        if not run_cmd("git add ."):
            print("Error al agregar archivos.")
            continue
        print("Haciendo commit...")
        if not run_cmd(f'git commit -m "{msg}"'):
            print("Error al hacer commit.")
            continue
        print("Haciendo push...")
        if run_cmd("git push"):
            print("Todo listo, cambios subidos.")
        else:
            print("Error al hacer push.")
    elif opcion == "5":
        print("Saliendo...")
        break
    else:
        print("Opción no válida, intenta de nuevo.")
