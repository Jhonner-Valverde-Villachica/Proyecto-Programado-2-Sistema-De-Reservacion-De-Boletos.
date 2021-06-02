# Sistema de reservación de boletos.

# Entradas: Este programa como base recibirá un menú de opciones(Opciones administrativas, Opciones de usuario normal y Salir).
# Salidas: Retornar un Menú Principal donde se encuentren las Opciones administrativas, Opciones de usuario normal y Salir.
# Restricciones: Tener una contraseña generada y guardada para ingresar al menú principal.

from tkinter import *
ventana = Tk()

ventana.title("Sistema de reservación de boletos")

def menuPrincipal():
    print("Opciones administrativas.")
    print("Opciones de usuario normal.")
    print("Salir.")
    opciones = input("")

# Detalles de Opciones administrativas.

#    Entradas: Para acceder a este apartado, recibirá una clave de acceso para habilitar la función(Menú administrativo) y este mismo
#              mostrará un menú llamado "Menú Administrativo" (Gestión de empresas, Gestión de transporte por empresa, Gestión de viaje,
#              Consultar historial de reservaciones, Estadísticas de viaje).
#    Salidas: Retornar un Menú Administrativo donde se encuentren todas las funcionalidades que tiene este apartado
#             (Gestión de empresas, Gestión de transporte por empresa, Gestión de viaje, Consultar historial de reservaciones,
#              Estadísticas de viaje).
#    Restricciones: Ingresar únicamente por medio del menú principal.


    if (opciones == 'Opciones administrativas.'):
        print("Gestión de empresas.")
        print("Gestión de transporte por empresa.")
        print("Gestión de viaje.")
        print("Consultar el historial de reservaciones.")
        print("Estadísticas de viaje.")
        opciones == input('')

        # Detalles de Gestión de empresas.
        
#        Entradas: Recibirá una Cédula jurídica, Nombre y Ubicación(Dirección de la empresa) con el fin de dar un mantenimiento a las empresas.
#        Salidas: Dar mantenimiento a las empresas (Cédula jurídica, Nombre, Ubicación(Dirección del negocio).
#        Restricciones: Debe permitir incluir, eliminar, o modificar empresas, además de mostrarlas. La información que debe
#                       almacenar por empresa debe ser; Cédula jurídica, Nombre y Ubicación(Dirección del negocio).
#                       No pueden existir empresas con la misma cédula y no pueden eliminarse empresas que hayan sido asociadas
#                       con algún transporte. La cédula no se modifica.
        
        if (opciones == 'Gestión de empresas.'):
            print("Gestión de empresas.")
            cedulaJuridica = int(input("Cédula jurídica: "))
            nombre = str(input("Nombre: "))
            ubicacion = str(input("Ubicación del negocio: "))

        # Detalles de Gestión de transporte por empresa
 
#        Entradas: Recibirá una Placa, Tipo(Buseta y/o limosina), Marca, Modelo, Año, Empresa,
#                  Cantidad de asientos clase VIP, clase normal y clase económica
#                  con el fin de dar mantenimiento al transporte.
#        Salidas: Dar mantenimiento a los transportes que poseen las empresas(Placa, Marca, Modelo, Año,
#                 Empresa, Cantidad de asientos clase VIP, clase normal y clase económica).
#        Restricciones: Debe permitir incluir, eliminar o modificar transporte, además de mostrarlos.
#                       La información que se debe almacenar por transporte será: Placa, Marca, Modelo, Año,
#                       Empresa(Esta seleccionarla de la lista existente del punto 3.1),
#                       Cantidad asientos clase vip, clase normal y clase económica.
#                       Se debe indicar la cantidad de asientos por fila por tipo(Esto se considera en el punto 4.2).
#                       No pueden existir dos transportes con la misma placa y no pueden eliminarse tranportes que estén registrados en un viaje.
#                       La placa no se modifica.

        elif (opciones == 'Gestión de transporte por empresa.'):
            print("Gestión de transporte por empresa.")
            placa = str(input("Placa: "))
            tipoVehiculo = str(input("Buseta o limosina: "))
            marca = str(input("Marca: "))
            modelo = str(input("Modelo: "))
            año = str(input("Año: "))
            empresa = str(input("Empresa: "))
            cantidadDeAsientosVIP = int(input("Cantidad de asientos clase VIP: "))
            cantidadDeAsientosNormal = int(input("Cantidad de asientos clase normal: "))
            cantidadeAsientosEconómica = int(input("Cantidad de clase económica: "))

        # Detalles de Gestión de viaje.
        
#        Entradas: Recibirá un Número de viaje(Este es generado automáticamente), Ciudad de salida, Fecha y hora de salida,
#                  Ciudad de llegada, Fecha y hora de llegada, Empresa y transporte,
#                  Monto del asiento clase VIP, Monto del asiento clase normal, Monto del asiento clase económica, esto
#                  con el fin de registrar viajes.
#        Salidas: Pemitir registrar viajes(Número de viaje(generado automáticamente), Ciudad de salida, Fecha y hora de salida,
#                 Ciudad de llegada, Fecha y hora de llegada, Empresa y transporte(Seleccionar de la lista existente pertenecientes
#                 a la empresa), Monto clase VIP, monto clase normal y monto clase económica).
#        Restricciones: Debe permitir registrar viajes, se debe permitir incluir, eliminar o modificar viajes, además de mostrarlos.
#                       La información que se debe almacenar por viaje será:
#                       Número de viaje(Generado automáticamente), Ciudad de salida,
#                       Fecha y hora de salida, Ciudad de llegada, Fecha y hora de llegada, Empresa y transporte(Seleccionar de la lista
#                       existente pertenecientes a la empresa seleccionada), Monto asiento clase VIP, monto clase normal y monto clase económica.
    
        elif (opciones == 'Gestión de viaje.'):
            print("Gestión de viaje.")
            numeroDeViaje = print("")
            provinciaYciudadDeSalida = str(input("Provincia y ciudad de salida: "))
            fechaYhoraDeSalida = str(input("Fecha y hora de salida: "))
            provinciaYciudadDellegada = str(input("Provincia y ciudad de llegada: "))
            fechaYhoraDellegada = str(input("Fecha y hora de llegada: "))
            empresaYtransporte = print("")
            precioDeAsientosVIP = str(input("Monto de asientos clase VIP: "))
            precioDeAsientosNormal = str(input("Monto de asientos clase normal: "))
            precioDeAsientosEconomica = str(input("Monto de asientos clase económica: "))

        # Detalles de Consultar el historial de reservaciones.
    
#        Entradas: Mostrar una lista de las reservaciones generadas por el sistema.
#        Salidas: Mostrar una lista de reservaciones generadas en el sistema. Por cada reservación mostrar
#                 (Identificador, Nombre de la persona que reserva, Número de viaje, Fecha y hora de la reservación,
#                 Empresa, transporte, Lugar fecha y hora de salida, Lugar fecha y hora de llegada,
#                 Cantidad de asientos reservados VIP, clase normal, clase económica, Monto de reservación).
#        Restricciones: Se debe selecionar un viaje(Mostrar al usuario los existentes).
#                       Por cada reservación debe generar un reporte.
        
        elif (opciones == 'Consultar el historial de reservaciones.'):
            print("Consultar el historial de reservaciones.")
            identificador = print("Identificador: ")
            nombreReservador = print("Nombre de la persona que reserva: ")
            numeroDeViaje = print("Número de viaje: ")
            fechaYhoraDeLaReservacion = print("Fecha y hora de la reservación: ")
            empresa,transporte = print("Empresa, transporte: ")
            lugar,fechaYhorasalida = print("Lugar, fecha y hora de salida: ")
            lugar,fechaYhorallegada = print("Lugar, fecha y hora de llegada: ")
            cantidadDeAsientosReservadosVIP = print("Cantidad de asientos reservados en clase VIP: ")
            cantidadDeAsientosReservadosNormal = print("Cantidad de asientos reservados en clase normal: ")
            cantidadDeAsientosReservadosEconomica = print("Cantidad de asientos reservados en clase económica: ")
            montoDeReservación = print("Monto de resevación: ")
            
        # Detalles de Estadísticas de viaje.
    
#        Entradas: Seleccionar un viaje y mostrar los siguientes detalles: (Número de viaje: ,Empresa transporte:, Lugar, fecha y hora de salida: ,
#                  Lugar, fecha y hora de llegada: ,Cantidad de asientos clase VIP reservados y asientos clase VIP disponibles:,
#                  Cantidad de asientos normal reservados y asientos normal disponibles: ,Cantidad de asientos económico reservados y asientos económico disponibles: ,
#                  Costo por boleto vip, normal y económico: ,Monto recaudado por el viaje: )
#        Salidas: Seleccionar un viaje y mostrar el siguiente detalle(Número de viaje, Empresa, transporte,
#                 Lugar fecha y hora de salida, Lugar, fecha y hora de llegada, Cantidad de asientos clase VIP reservados y asientos
#                 clase VIP disponibles, Cantidad de asientos normal reservados y asientos normal disponibles,
#                 Cantidad de asientos económico reservados y asientos económico disponibles,
#                 Costo por boleto vip, normal y económico, Monto recaudado por el viaje).
#        Restricciones: Se debe selecionar un viaje(Mostrar al usuario los existentes). Por ende, mostrar los siguientes detalles: (Número de viaje: ,
#                       Empresa, transporte: ,Lugar, fecha y hora de salida: ,Lugar, fecha y hora de llegada: ,
#                       Cantidad de asientos clase vip reservados y asientos clase vip disponibles:
#                       Cantidad de asientos normal reservados y asientos normal disponibles:
#                       Cantidad de asientos económico reservados y asientos económico disponibles:
#                       Costo por boleto vip, normal y económico:
#                       Monto recaudado por el viaje:
#                       Se debe generar un reporte en txt.
        
        elif (opciones == 'Estadísticas de viaje.'):
            print("Estadísticas de viajes.")
            numeroDeViaje = print("Número de viaje: ")
            empresa,transporte = print("Empresa y transporte: ")
            lugar,fechaYhorasalida = print("Lugar, fecha y hora salida: ")
            lugar,fechaYhorallegada = print("Lugar, fecha y hora llegada: ")
            cantidadDeAsientosVIP = print("Cantidad de asientos clase VIP reservados y asientos clase VIP disponibles: \n")
            cantidadDeAsientosNormal = print("Cantidad de asientos clase normal reservados y asientos clase normal disponibles: \n")
            cantidadDeAsientosEconomico = print("Cantidad de asientos clase económico reservados y asientos clase económico disponibles: \n")
            costoBoletoVIP = print("Costo por boleto clase VIP: ")
            costoBoletoNormal = print("Costo por boleto clase normal: ")
            costoBoletoEconomico = print("Costo por boleto clase económico: ")
            recaudacion = print("Monto recaudado por el viaje: ")
            
        else:
            return print("Error: Este dígito no es reconocido por el sistema.")

    # Detalles de Opciones de usuario normal.
   
#    Entradas: Ingresar por medio del menú principal y por ende, habilitar demás funciones(Menú General) "Consulta de viajes,
#              Reservación de viaje, Cancelación de reservación".
#    Salidas: Retornar el Menú General.
#    Restricciones: Ingresar únicamente por medio del Menú Principal.
    
    elif (opciones == 'Opciones de usuario normal.'):
        print("Consulta de viajes.")
        print("Reservación de viaje.")
        print("Cancelación de reservación.")
        print("Salir")
        opciones = input("")

    # Detalles de Consulta de viajes.
    
#    Entradas: Mostrar una lista de viajes de cada viaje.
#    Salidas: Mostrar una lista de los viajes.
#    Restricciones: Mostrar una lista de los viajes.
    
        if (opciones == 'Consulta de viajes.'):
            print("Consulta de viajes")
            print("Número de viaje: ")
            print("Ciudad de salida: ")
            print("Fecha y hora de salida: ")
            print("Ciudad de llegada: ")
            print("Fecha y hora de llegada: ")
            print("Empresa y transporte: ")
            print("Monto clase VIP: ")
            print("Monto clase normal: ")
            print("Monto clase económica: ")

        # Detalles de Reservación de Viaje.
        
#        Entradas: Mostrar y escoger el diferente tipo de viaje(Son distintas opciones, por lo cual mostrará el Número de Viaje,
#                  Empresa, Lugar de salida y llegada y las fechas). Luego indicar el nombre, La cantidad de espacios a reservar en clase vip, normal y
#                  económica(Se deberá reservar al menos un asiento en total. Se le entregará un comprobante (Se mostrará en pantalla,
#                  no debe exportarse ni imprimir) al cliente con la siguiente información: Identificador de la reserva(Generado automáticamente),
#                  Nombre de la persona que reserva, Fecha y hora de de la reservación(capturado del sistema), Empresa, Transporte,
#                  Lugar, fecha y hora salida, lugar, fecha y hora llegada, Cantidad de asientos reservados en clase vip, clase normal y clase económica y
#                  Monto de reservación (calcular según cantidad, tipos y montos de asientos).
#        Salidas: Seleccionar el viaje que desea y luego indicar; El nombre, La cantidad espacios a reservar en clase VIP,
#                 normal y económica, Identificador de la reserva(generado automáticamente), Nombre de la persona que reserva,
#                 Fecha y hora de la reservación(capturadas del sistema), Empresa, Transporte,
#                 Lugar, fecha y hora salida, lugar, fecha y hora llegada,
#                 Cantidad de asientos reservados en clase vip, clase normal y clase económica y
#                 Monto de reservación (calcular según cantidad, tipos y montos de asientos).
#        Restricciones: Se debe seleccionar el viaje una vez que se haya realizado la reservación(Mostrar al usuario información de número
#                       de viaje, empresa, lugar de salida y llegada, y fechas). El usuario selecciona uno y luego indicar lo solicitado.
#                       Mostrar una gráfica de la distribución del transporte donde el usuario selecciona los asientos a reservar.
#                       Considerando la cantidad de asientos por fila por tipo de asiento del transporte(indicado en punto 3.2)
#                       Se debe diferenciar los asientos que han sido reservados previamente y los que están disponibles.
#                       Además diferenciar los que está reservando el usuario.
        

        if (opciones == 'Reservación de viaje.'):
            print("Reservación de viaje.")
            nombre = str(input("Nombre: "))
            espaciosPorReservar = str(input("Cantidad de espacios a reservar: \nClase VIP: \nClase normal: \nClase económica: "))
            identificador = print("")
            nombreDeLaPersonaReservadora = str(input("Nombre de la persona que reserva: "))
            fechaYhoraDeLaReservación = print("")
            empresa = str(input("Empresa: "))
            transporte = str(input("Transporte: "))
            fechasYhoras = str(input("Lugar, fecha y hora de salida: \nLugar, fecha y hora de llegada"))
            asientosReservadosVIP = str(input("Cantidad de asientos reservados clase VIP: "))
            asientosReservadosNormal = str(input("Cantidad de asientos clase normal: "))
            asientosReservadosEconomica = str(input("Cantidad de asienstos clase económica: "))
            identificadorDeAsientosPorTipo = str(input("Identificador de asientos por tipo: "))
            montoDeReservación = print("")

        # Detalles de Cancelación de reservación.
        
#        Entradas: Ingresar el identificador de la reserva.
#        Salidas: Cancelar la reserva del viaje.
#        Restricciones: Se debe indicar el identificador de la reserva y se debe eliminar el sistema de la reservación con todos los
#                       respectivos datos, también debe liberar los asientos reservados.
        
        if (opciones == 'Cancelación de reservación.'):
            print("Cancelación de reservación")
            identificador = str(input("Identificador: "))

        # Detalles de Salir.
        
#        Entradas: Salir del programa.
#        Salidas: Salir del programa.
#        Restricciones: Salir del programa, debe almacenar toda la información para que sean datos persistentes.
#                       Se debe mantener para los siguientes usos del programa.
        
        if (opciones == 'Salir'):
            return print("Hasta pronto.")

Button(text = "Menú Principal",bg = "dark salmon",command = menuPrincipal).place(x = 10,y = 70)
ventana.mainloop()
