import os ##Utilizo la librería os para crear la función clear_screen y limpiar la pantalla en cada submenu.

def clear_screen(): ##Limpia la pantalla para una mejor lectura y fluidez del programa.
    if os.name == 'posix':
        os.system('clear')  ## Para Linux o mac
    else:
        os.system('cls')  ## Para Windows

## Preguntas y chequeo

def options(min, max): ##Función que chequea que la opción ingresada sea válida y este ente los valores especificados

    while True:
        try:
            option_1 = int(input("--> "))
            if option_1 >= min and option_1 <= max:
                return option_1
            else:
                print("\nOpción no válida.\n")
        except ValueError:
            print("\nDato ingresado no válido.\n")
    
def anew (question):##Realiza una pregunta que se responde por si o no, devolviendo un "s" o "n"  
    while True:
        answer = input(f"\n{question}? S/N: ").lower()
        if answer == "s":
            return answer
        elif answer == "n":
            return answer
        else:
            print("\nDato ingresado no válido.")

def entry_isbn(message): ##Función que solicita un ISBN y cheque que sea válido. Recibe un mensaje como, "ingrese el isbn del libro a eliminar", o a modificar.
    while True:
        try:
            isbn = int(input(f"\n{message}: "))
            if len(str(isbn)) != 13: ##El ISBN debe contener 13 dígitos, convierto momentáneamente a string para poder contarlos.
                print("\nEl ISBN debe contener 13 dígitos.")
                continue
            return isbn
        except ValueError:
            print("\nDato ingresado no válido.")

## Gestión
        
def new_book(database): ##  Función para ingresar un nuevo libro.

    option_new_book = "s" ##Variable para salir de los while

    while option_new_book != "n":
        ## Encabezado del menú.
        print("\nGestión de libros --> Ingreso de libro nuevo")
        print("-------------------------------------------")
    
        ## Solicitud de ingreso de datos y chequeo que sean datos válidos.    
        print("\nIngrese los datos del libro nuevo:\n")

        isbn = entry_isbn("Ingrese el ISBN") ##ISBN
        if isbn in database.keys():## Chequea si el libro ya esta ingresado.
            print("\nLibro ya ingresado.")
            option_new_book = anew("Desea agregar otro libro") ## Si esta en el catalogo, consulta si quiere ingresar otro libro.
            clear_screen()
            continue

        title = input("\nTítulo: ") ## Título
        author = input("\nAutor: ") ## Autor

        while option_new_book != "n": ## Página
            try:
                page = int(input("\nPáginas: "))
                if page <= 0:
                    print("\nEl número de páginas debe ser mayor a cero.")
                else:
                    option_new_book = "n"
            except:
                print("\nDato ingresado no válido.")

        option_new_book = "s"
        while option_new_book != "n": ## Precio
            try:
                price = float(input("\nPrecio: "))
                if price < 0:
                    print("\nEl precio debe ser mayor o igual a cero.")
                else:
                    option_new_book = "n"
            except:
                print("\nDato ingresado no válido.")
        
        option_new_book = "s"
        while option_new_book != "n": ## Stock
            stock = input("\nStock(Ingrese: S/N): ").lower()
            if stock == "s":
                stock = True
                option_new_book = "n"
            elif stock == "n":
                stock = False
                option_new_book = "n"
            else:
                print("\nDato ingresado no válido.")                
    
        ##Ingreso en el diccionario los datos ingresados anteriormente.    
        database[isbn] = {"titulo": title, "autor": author, "paginas": page, "precio": price, "stock": stock}

        print("\nLibro ingresado correctamente.")

        option_new_book = anew("Desea ingresar otro libro") #Consulta si quiere ingresar otro libro
        clear_screen()

def modify_book(database): ## Función para modificar un libro.

    option_modify_book = "s" ##Variable para salir de los while.

    while option_modify_book != "n":

        ## Encabezado del menú.
        print("\nGestión de libros --> Modificación de libro")
        print("-------------------------------------------")        
        
             
        isbn = entry_isbn("Ingrese el ISBN del libro a modificar") ##Función de chequeo de ISBN
        if isbn not in database.keys(): ##Chequeo si el libro esta en el catalogo
            print("\nEl libro no se encuentra ingresado.")
            option_modify_book = anew("Desea modificar otro libro") ## Si no esta consulta si quiere modificar otro libro
            clear_screen()
            continue  
        
        ##Consulta si es correcto si quiere modificar ese libro.
        option_modify_book = anew(f"Va a modificar el libro --> {database[isbn]['titulo'].upper()} del autor {database[isbn]['autor'].upper()}, es correcto") 
        if option_modify_book == "n": ##En caso que no quiera modificar ese libro consulto si quiere modificar otro libro
            option_modify_book = anew("Desea modificar otro libro")
            clear_screen()
            continue   
        
        clear_screen()

        while option_modify_book != "n": ##while de modificación de datos de un mismo libro
            ##Impresión de opciones para modificar un libro.
            print(f"""
Gestión de libros --> Modificación de libro
-------------------------------------------
                  
    Que dato desea modificar del libro {database[isbn]['titulo'].upper()}?:
    [1] --> ISBN
    [2] --> Título 
    [3] --> Autor
    [4] --> Página
    [5] --> Precio
    [6] --> Stock     
        """)
            
            modify = options(1,6) ## Devuelve una opción de 1 a 6

            ## Ingreso a opciones según lo ingresado en el while anterior.

            if modify == 1: ##ISBN
                while option_modify_book != "n":
                    isbn_new = entry_isbn("\nIngrese el ISBN nuevo") ##Ingreso ISBN nuevo

                    if isbn_new in database.keys(): ##Chequeo que el ISBN no este en el catalogo
                        print("\nISBN ya ingresado.")
                        option_modify_book = anew("Desea ingresar otro ISBN") ## Si el ISBN ya fue ingresado consulto si quiere ingresar otro o salir
                        if option_modify_book not in ["s", "n"]:
                            print("Dato ingresado no valido.")
                        elif option_modify_book == "n":
                            continue
                    else:
                        option_modify_book = "n"

                database[isbn_new] = database.pop(isbn) ##Borro el ISBN anterior con pop que devuelve el valor y lo almaceno en el nuevo ISBN
                isbn = isbn_new

            elif modify == 2: ## Título
                title_new = input("\nIngrese nuevo título: ")
                database[isbn]["titulo"] = title_new
            elif modify == 3: ## Autor
                author_new = input("\nIngrese el nuevo autor: ")
                database[isbn]["autor"] = author_new
            elif modify == 4: ## Páginas
                while option_modify_book != "n": ## Se chequea que se un valor numérico mayor a 0 y entero.
                    try:
                        page_new = int(input("\nIngrese en nuevo número de páginas: "))
                        if page_new <= 0:
                            print("\nEl número de páginas deber ser mayor a cero.")
                        else:
                            option_modify_book = "n"
                    except ValueError:
                        print("\nDato ingresado no válido.")

                database[isbn]["paginas"] = page_new

            elif modify == 5: ## Precio
                while option_modify_book != "n": ## Se cheque que el precio ingresado sea un número mayor a 0.
                    try:
                        price_new = float(input("\nIngrese el nuevo precio: "))
                        if price_new < 0:
                            print("\nEl precio debe ser mayor o igual a cero.")
                        else:
                            option_modify_book = "n"
                    except ValueError:
                        print("\nDato ingresado no válido.")

                database[isbn]["precio"] = price_new

            elif modify == 6: ##Stock
                while option_modify_book != "n": ## Se solicita que ingrese S/N para el stock
                        stock_new = input("\nStock(Ingrese: S/N): ").lower()
                        if stock_new == "s":
                            database[isbn]["stock"] = True
                            option_modify_book = "n"
                        elif stock_new == "n":
                            database[isbn]["stock"] = False
                            option_modify_book = "n"
                        else:
                            print("\nDato ingresado no válido.")

            print("\nDatos modificados correctamente.")

            option_modify_book = anew(f"Desea modificar otro dato del libro {database[isbn]['titulo'].upper()}") ## Consulta si quiere modificar otro dato del mismo libro
            if option_modify_book == "s":
                clear_screen()

        option_modify_book = anew("Desea modificar otro libro") ## Consulta si quiere modificar datos de otro libro
        clear_screen()

def delete_book(database):## Función para eliminar un libro

    option_delete_book = "s" ##Variable para salir de los while

    while option_delete_book != "n":

        ## Encabezado del menú.
        print("\nGestión de libros --> Eliminar libro")
        print("-------------------------------------------")

        ## Ingreso de ISBN para eliminar un libro            
        isbn = entry_isbn("Ingrese el ISBN del libro a eliminar")
        if isbn not in database.keys(): ## Si el libro no esta en el catalogo consulta si quiere eliminar otro libro.
            print("\nEl libro no se encuentra en el catalogo.")
            option_delete_book = anew("Desea eliminar otro libro")
            clear_screen()
            continue
        
        ##Consulta si quiere eliminar ese libro
        option_delete_book = anew(f"Va a eliminar el libro --> {database[isbn]['titulo'].upper()} del autor {database[isbn]['autor'].upper()}, es correcto") 
        if option_delete_book == "s":
            del database[isbn] ## Se elimina el libro
            print("\nEl libro se eliminó correctamente.")
        

        option_delete_book = anew("Desea eliminar otro libro") ##Consulta si quiere eliminar otro libro
        clear_screen()

## Reportes

def info_book (database): ## Función info por ISBN

    option_info_book = "s" ##Variable para salir del while

    while option_info_book != "n":

        ## Encabezado del menú. 
        print("\nReportes --> Información de libros por ISBN")
        print("-------------------------------------------")
        
        isbn = entry_isbn("Ingrese el ISBN del libro que quiere consultar")

        if isbn not in database.keys(): ##Control si el ISBN esta en el catalogo, si no esta, pregunta si quiere hacer otra consulta.
            print("\nEl libro no se encuentra en el catalogo.")
            option_info_book = anew("Desea consultar otro libro")
            clear_screen()
            continue
                
            
        print("\n---------------------\n")
        for clave, valor in database[isbn].items():##Recorre el diccionario del ISBN solicitado

            if valor == True: ##Transforma el true o false en sí o no para mayor prolijidad en el reporte
                valor = "Si"
            elif valor == False:
                valor = "No"

            if clave == "precio": ##Agrega el signo $ si la clave es precio
                valor = f"${valor}"
            
            print(f"{clave.capitalize()}: {valor}") ## Imprime los valores del ISBN solicitado
        print("\n---------------------\n")

        option_info_book = anew("Desea consultar otro libro") ## Pregunta si quiere consultar otro libro
        clear_screen()

def book_out_stock(database): ## Función de consulta de libros sin stock
    
    option_book_out_stock = "n" ##Variable para salir del while

    while option_book_out_stock != "s":
        
        ## Encabezado del menú.  
        print("\nReportes --> Libros sin stock")
        print("-------------------------------------------")
        
        print("\n-------------------------------------------")
        for isbn in database: ##Recorre el catalogo de libros e imprime los que tengan False en indice stock
            if database[isbn]["stock"] == False:
                print(f"\n\nISBN:{isbn}", end=" - ") 
                for clave, valor in database[isbn].items(): ##Recorre cada cada libro filtrado e imprime sus valores.

                    if valor == True: ##Transforma el true o false en sí o no para mayor prolijidad en el reporte
                        valor = "Si"
                    elif valor == False:
                        valor = "No"

                    if clave == "precio": ##Agrega el signo $ si la clave es precio
                        valor = f"${valor}"

                    print(f"{clave.capitalize()}: {valor}", end=" - ")

        print("\n\n-------------------------------------------\n")

        option_book_out_stock = anew("Desea salir de la consulta") ## Consulta si quiere salir de la consulta
        clear_screen()
        
def book_for_price(database): ## Función de consulta de libro por precio.

    option_book_for_price = "s" ##Variable para salir de los while

    while option_book_for_price != "n":
        ## Encabezado del menú.  
        print("\nReportes --> Búsqueda de libros por precio")
        print("-------------------------------------------")
        print("\nSe mostrarán los libros con el precio menor al que ingrese a continuación\n")

        while option_book_for_price != "n":## Pide un valor para filtrar por precio y chequea que sea positivo.
            try:
                price = float(input("Ingrese un precio para filtrar la búsqueda: "))
                if price < 0:
                    print("\nEl valor debe ser mayor a 0.\n")
                else:
                    option_book_for_price = "n"
            except ValueError:## Captura de error si no es un float
                print("\nDato ingresado no válido.\n")
        
        print("\n-------------------------------------------")
        for isbn in database: 
            if database[isbn]["precio"] <= price : ##Filtra todos los que tengan menor precio al indicado
                print(f"\n\nISBN:{isbn}", end=" - ") 
                for clave, valor in database[isbn].items(): ##Recorre cada cada libro filtrado e imprime sus valores.

                    if valor == True: ##Transforma el true o false en sí o no para mayor prolijidad en el reporte
                        valor = "Si"
                    elif valor == False:
                        valor = "No"

                    if clave == "precio": ##Agrega el signo $ si la clave es precio
                        valor = f"${valor}"

                    print(f"{clave.capitalize()}: {valor}", end=" - ")                

        print("\n\n-------------------------------------------\n")

        option_book_for_price = anew("Desea realizar otra consulta") ## Pregunta si quiere realizar otra consulta
        clear_screen()

def book_for_name(database):## Función de consulta de libro por título

    option_book_for_name = "s"

    while option_book_for_name != "n":

        ## Encabezado del menú.  
        print("\nReportes --> Búsqueda de libros por precio")
        print("-------------------------------------------")
        print("\nSe mostrarán los libros que contengan la palabra u oración que ingrese.\n")

        ## Pide una palabra u oración para filtrar por nombre
        title = (input("Ingrese una palabra o frase: ")).lower()
        
        print("\n-------------------------------------------")
        for isbn in database: 
            if title in database[isbn]["titulo"].lower() : ##Filtra todos los libros que contengan la palabra u oración dada
                print(f"\n\nISBN:{isbn}", end=" - ") 
                for clave, valor in database[isbn].items(): ##Recorre cada cada libro filtrado e imprime sus valores.

                    if valor == True: ##Transforma el true o false en sí o no para mayor prolijidad en el reporte
                        valor = "Si"
                    elif valor == False:
                        valor = "No"

                    if clave == "precio": ##Agrega el signo $ si la clave es precio
                        valor = f"${valor}"

                    print(f"{clave.capitalize()}: {valor}", end=" - ")                

        print("\n\n-------------------------------------------\n")

        option_book_for_name = anew("Desea realizar otra consulta") ## Pregunta si quiere hacer otra consulta
        clear_screen()

