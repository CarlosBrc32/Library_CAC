import Library_Functions ## Importa las funciones del archivo que las contiene.

##Catologo inicial
book_catalog = {
    1234567891234:{"titulo": "Introducción a la programación",
                   "autor": "Codo a codo inicial", 
                   "paginas": 450, 
                   "precio": 2500, 
                   "stock": True},

    9788498726138:{"titulo": "El Imperio Final",
                   "autor": "Brandon Sanderson", 
                   "paginas": 688, 
                   "precio": 5300, 
                   "stock": False},

    9788498388893:{"titulo": "Harry Potter y la piedra filosofal",
                   "autor": "J. K. Rowling", 
                   "paginas": 320, 
                   "precio": 7500, 
                   "stock": True},

    9781539638261:{"titulo": "La Guerra de los Mundos",
                   "autor": "H.G. Wells", 
                   "paginas": 174, 
                   "precio": 3200, 
                   "stock": True},

    9788492915033:{"titulo": "El arca",
                   "autor": "Boyd Morrison", 
                   "paginas": 512, 
                   "precio": 3750, 
                   "stock": False}                 

  } 

Library_Functions.clear_screen()##Limpia la pantalla para un inicio mas prolijo.


def main():
    option = 1 ## Variable para salir del while

    while option != 0: 
        ##Encabezado del programa.
        print("\nBIENVENIDO AL SISTEMA DE ADMINISTRACIÓN DE LIBRERÍAS")
        print("-------------------------------------------------")

        ##Impresión del menú principal
        print("""
    Ingrese una opción para comenzar:

    [1] Gestión de libros
    [2] Reportes
    [0] Salir
        """) 

        option = Library_Functions.options(0,2) #Devuelve un valor entre 0 y 2

        ##If que ejecutas las funciones según las opciones.

        if option == 1: ## Gestión de libros

            option_1 = 1 ## Variable para salir del while

            while option_1 != 4:
                Library_Functions.clear_screen()##Limpia la pantalla para una mejor lectura y fluidez del programa.
                ##Impresión de opciones si ingresó 1.
                print("""
    GESTIÓN DE LIBROS   
    -----------------
            """)
                print("""Ingrese una opción para continuar

    [1] Ingresar nuevo libro
    [2] Modificar dato de un libro
    [3] Eliminar un libro
    [4] Volver al menú principal
                    
            """)
                option_1= Library_Functions.options(1,4) ##Retorna opciones entre 1 y 4.
                Library_Functions.clear_screen()
                if option_1 == 1:
                    Library_Functions.new_book(book_catalog) ##Función para agregar un nuevo libro.
                elif option_1 == 2:
                    Library_Functions.modify_book(book_catalog) ##Función para modificar un libro.
                elif option_1 == 3:
                    Library_Functions.delete_book(book_catalog) ## Función para borrar un libro.
                elif option_1 == 4:
                    pass
        elif option == 2: ## Reportes

            option_2 = 1 ## Variable para salir del while

            while option_2 != 5:
                Library_Functions.clear_screen()
                ##Impresión de opciones si ingresó 2.
                print("""
    REPORTES
    -----------------
            """)
                print("""Ingrese una opción para continuar

    [1] Información por ISBN
    [2] Libros sin stock
    [3] Libros filtrados por precio menor a $X 
    [4] Buscar libro por nombre
    [5] Volver al menú principal  
            """)
                option_2 = Library_Functions.options(1,5) ##Retorna opciones entre 1 y 5.
                Library_Functions.clear_screen()
                if option_2 == 1:
                    Library_Functions.info_book(book_catalog) ## Función info por ISBN
                elif option_2 == 2:
                    Library_Functions.book_out_stock(book_catalog)## Función de consulta de libros sin stock
                elif option_2 == 3:
                    Library_Functions.book_for_price(book_catalog)## Función de consulta de libro por precio
                elif option_2 == 4:
                    Library_Functions.book_for_name(book_catalog)## Función de consulta de libro por título
                elif option_2 == 5:
                    pass
        elif option == 0: ## Salir del sistema
            Library_Functions.clear_screen()
            print("""
                

                    ------------------------------------------------------------
                    | Gracias por usar el sistema de administración de librerías.|
                    ------------------------------------------------------------        
                

                    """)
        
if __name__ == "__main__":
    main()