#no ordenado
import csv
with open("Catalogo.csv","r" enconding="utf-8)as archivo:
Lector = csv.dictpleader (archivo)
Catalogo = list (lector) 
Print (catalogo)
#ordenado
Import csv
def cargar_catalogo():
  with open ("catalogo.csv", "r", encording="utf_8") as archivo:
    Lector = csv.dictpleader (archivo)
Catalogo = list (lector)
return catalogo

def listar catalogo(catalogo):
Print ("/n==== CATALOGO====")
for i, cancióbn in enumerate (cataogo, start=1):
  print(
    i,
    "-",
    canción ["nombbre"],
    "-",
    canción ["artistas"]
    9

def mostrar_menu():
    print("\n===== PLAYLIST =====")
    print("1. Listar catálogo")
    print("2. Buscar canción")
    print("3. Reproducir canción")
    print("4. Pausar canción")
    print("5. Siguiente canción")
    print("6. Canción anterior")
    print("7. Salir")


def main():
    catalogo = cargar_catalogo()

    while True:
        mostrar_menu()

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            listar_catalogo(catalogo)

        elif opcion == "7":
            print("Programa finalizado.")
            break

        else:
            print("Opción todavía no implementada.")


main()
