Inventario_libros = []
genero = ['Ficcion' , 'no ficcion', 'ciencia']
registro_ventas = []
ventas_realizadas = []

def registrar_libro():
    print("Registar libros")
    titulo= input("Ingrese nombre del libro")
    autor= input("Ingrese autor del libro")
    genero= input("ingrese genero del libro")
    while genero not in generos:
        print("genero no disponible, por favor ingrese un genero valido")
        precio=float(input("Ingrese el precio del libro"))
        if titulo.strip() == ' ' or autor.strip() == ' ' or genero.strip() == ' ' or precio <=0:
            print(" Error todos los campos tienen que estar completos /precio no valido ")
            return
        

Inventario_libros.append({
    'titulo':titulo,
    'autor':autor,
    'genero':genero,
    'precio':precio,
    'stock':0,
    })
print("Libro registrado")
else:
print("Error el registar libro")


def listar_libros():
    print("Este es los libors en inventario")
    if not Inventario_libros:
        print("No hay libros en inventario")
        return
    
def registrar_venta():
    if not Inventario_libros:
        print("no hay libros registrados")
        return
    
print("registro de venta:")
listar_libros()
titulo_libro = input("Ingrese el titulo")

libro_encontrado = None
for libro in Inventario_libros:
    if libro['titulo'].lower() == titulo_libro.lower():
        libro_encontrado=libro
        break
if not libro_encontrado:
    print("el libro no esta registrado")
    return

cantidad_vendida = int (input("ingrese la cantidad vendida "))
precio_unitario= libro_encontrado['precio']
precio_final = cantidad_vendida * precio_unitario

if cantidad_vendida > libro_encontrado['no hay suficiente stock']:
    print("no hay suficiente stock")
    return

ventas_realizadas.append({
    'titulo': titulo_libro,
    'cantidad': cantidad_vendida,
    'precio_unitario': precio_unitario,
    'precio_final': precio_final,
})

libro_encontrado['stock']-= cantidad_vendida
print("venta registrada exitosamente")

def imprimir_reporte_ventas():
    print("seleccione una opcion para imprimir el reporte")
    print("1 imprimit todas las ventas")
    print("2 imprimir ventas por genero")
    opcion = int(input("ingrese el numero de la opcion que desea realiazr"))
    
    if opcion == 1:
        imprimit_reporte_todas_ventas()
    elif opcion == 2:
        imprimir_reporte_por_genero()
    else:
        print("seleccione una opcion valida")
        return
    
def imprimir_reporte_todas_ventas():
    if not ventas_realizadas:
        print("no se a realizado ninguna venta")
        return
    
print("reporte de todas las ventas:")
for idx, venta in enumerate(ventas_realizadas, start=1):
    print(f"venta {idx}")
    print(f"titulo: {venta[titulo_libro]}")
    print(f"cantidad {venta[cantidad_vendida]}")
    print(f"precio unitario: {venta[precio_unitario]}")
    print(f"precio fional {venta[precio_final]}")
    

gererar_archivo_txt("reporte de las ventas", ventas_realizadas)
print("se genero el reporte")

def imprimir_reporte_genero():
    print("seleccione el genero")
    for idx, genero in enumerate(genero, start=1):
        print(f"{idx}, {genero}")
        
seleccion = int(input("ingrese el numero de genero para generar el reporte"))
if seleccion < 1 or seleccion > 3:
    print("seleccion no valida")
    return

genero_selecionado = genero[seleccion-1]
ventas_por_genero = [venta for venta in ventas_realizadas if venta['titulo']] in [libro['titulo']for libro in Inventario_libros if libro['genero'] == genero_selecionado]

if not ventas_por_genero:
    print("no se an realizado ventas para ese genero")
    return

print("reporte de ventas para el genero seleccionado")
for idx, venta in enumerate(ventas_por_genero, start=1):
    print(f"venta {idx}")
    print(f"titulo: {venta[titulo_libro]}")
    print(f"cantidad {venta[cantidad_vendida]}")
    print(f"precio unitario: {venta[precio_unitario]}")
    print(f"precio fional {venta[precio_final]}")
    
generar_archivo_txt(f"reporte ventas")
print("se a generado el archivo de reporte ventas")


def generar_archivo_txt(nombre_archivo, ventas)
with open(nombre_archivo,"w") as archivo:
    archivo.write("reporte de ventas")
    for venta in ventas:
        archivo.write("titulo")
        archivo.write("cantidad")
        archivo.write("precio_unitario")
        archivo.write("precio final")
        
def main():
    while True:
        print("1. registar libro")
        print("2. listar todos los libros")
        print("3 registrar ventas")
        print("4 imprimir reporte de ventas")
        print("5, generar archivo txt")
        print("6. salir programa")
        
if opcion ==1:
    registrar_libro()
elif opcion ==2:
    listar_libros()
elif opcion ==3:
    registrar_ventas
elif opcion ==4:
    imprimir_reporte_ventas
elif opcion ==5:
    if ventas_realizadas:
        generar_archivo_txt("ventas txt", ventas_realizadas)
        print("se genero el reporte")
    else:
        print("no hay ventas registradas")
elif opcion ==6:
    print("a salido del programa")
    break
else:
    print("opcion invalida")
    
if __name__=="__main__":
    main()    
    


