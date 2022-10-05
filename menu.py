#-*- coding:utf8 -*-

from operator import length_hint
from colorama import Fore
from clientes import Clientes
from configuracion import Configuracion
from empresa import Empresa
import xml.etree.ElementTree as ET
from escriActivos import EscriActivos
from listaDobleC import ListaDobleC
from listaDobleConfi import ListaDobleConfi
from listaDobleEscriA import ListaDobleEscriA
from listaDobleT import ListaDobleT
from listaDobleTransa import ListaDobleTransa
from puntosAtencion import PuntoAtencion
from transaNueva import TransaNueva
from transacciones import Transacciones
from listaDoble import ListaDoble
from pilaEscritorio import PilaEscritorio


def menu():
    opcionosa = ''
    listaEmpresas = ListaDoble()
    pilaE=PilaEscritorio()
    listaEmpresasConfi=ListaDobleConfi()
    listaClientes= ListaDobleC()
    listaTransaNueva=ListaDobleTransa()
    listaEscriActivo=ListaDobleEscriA()
   
    while opcionosa != '3':
        print(Fore.MAGENTA + "----------------------MENU PRINCIPAL--------------------")
        print(Fore.MAGENTA + "1 --- CONFIGURACIÓN DE EMPRESAS")
        print(Fore.MAGENTA + "2 --- SELECCIÓN DE EMPRESAS Y PUNTOS DE ATENCIÓN")
        print(Fore.MAGENTA + "3 --- SALIR")

        opcionosa = input(Fore.YELLOW + "Seleccione una opcion del menu \n")
         
        if opcionosa == '1':

            print(Fore.YELLOW + "**************MENU EMPRESAS************")
            print(Fore.YELLOW + "1 --- LIMPIAR SISTEMA")
            print(Fore.YELLOW + "2 --- CARGAR ARCHIVO DE CONFIGURACIÓN")
            print(Fore.YELLOW + "3 --- MOSTRAR EMPRESAS")
            print(Fore.YELLOW + "4 --- MOSTRAR PUNTOS DE ATENCION POR EMPRESA")
            print(Fore.YELLOW + "5 --- MOSTRAR TRANSACCIONES POR EMPRESA")
            print(Fore.YELLOW + "6 --- MOSTRAR ESCRITORIOS POR PUNTO DE ATENCION")
            print(Fore.YELLOW + "7 --- CREAR 'NUEVA EMPRESA' ")
            print(Fore.YELLOW + "8 --- CARGAR ARCHIVO DE INICIO ")

            opcion = input(Fore.YELLOW + "Seleccione una opción porfavor \n")

            if opcion=="1":
                print("estás en 'limpiar sistema' ")
            elif opcion =="2":
                
                nombreArchivo = input(Fore.BLUE + "Ingrese el nombre del archivo de configuración XML\n")
                ruta = './' + nombreArchivo
                listaEmpresas = cargaArchivo1(ruta)
                print(Fore.GREEN + "Se cargo el archivo con exito!!\n")
            elif opcion =="3":
                print("las empresas actuales de Soluciones Guatemaltecas S.A son:  \n")
                listaEmpresas.print()
            elif opcion=="4":
                codEmpresa = input(Fore.BLUE + "Ingresar codigo de la empresa: \n")
                empresa = listaEmpresas.buscarByCodigo(codEmpresa)
              
                if empresa is None:
                    print(Fore.RED + "Esa empresa no se encuentra registrado en la lista")
                else:
                    print("Los puntos de atencion de "+empresa.nombre+" son: \n")
                    empresa.puntoAtencion.print()
            elif opcion =="5":
                codEmpresa = input(Fore.BLUE + "Ingresar codigo de la empresa: \n")
                empresa = listaEmpresas.buscarByCodigo(codEmpresa)
              
                if empresa is None:
                    print(Fore.RED + "Esa empresa no se encuentra registrado en la lista")
                else:
                    print("Las transacciones de "+empresa.nombre+" son: \n")
                    empresa.transaccion.print() 
            elif opcion =="6":
                codEmpresa = input(Fore.BLUE + "Ingresar codigo de la empresa: \n")
                empresa = listaEmpresas.buscarByCodigo(codEmpresa)
                if empresa is None:
                    print(Fore.RED + "Esa empresa no se encuentra registrado en la lista")
                else:
                    codPA=input(Fore.BLUE + "Ingresar codigo del punto de atención correspondiente: \n")
                    puntito=empresa.puntoAtencion.buscarByCodigo(codPA)
       
                    if puntito is None:
                        print(Fore.RED + "Ese escritorio no se encuentra registrado en la lista de empresas")
                    else:
                        print("Los escritorios de "+puntito.nombre+" de la empresa "+empresa.nombre+" son: \n")
                        puntito.escritorio.printPila()

            elif opcion =="7":
                print(Fore.CYAN + "----------CREACIÓN DE EMPRESAS--------")
                print(Fore.CYAN + "1 --- CREAR EMPRESA")
                print(Fore.CYAN + "2 --- CREAR PUNTOS DE ATENCIÓN")
                print(Fore.CYAN + "3 --- CREAR ESCRITORIOS DE SERVICIO")
                print(Fore.CYAN + "4 --- CREAR TRANSACCIÓN")

                opcion = input(Fore.YELLOW + "Querido empresario, ingrese una opción porfavor \n")
                if opcion=="1":
                    nombreEmpresosa=input("¿Cuál es el nombre de la nueva empresa?\n ")
                    abreviaturaEmpresosa=input("¿Cuál es la abreviación de la nueva empresa?\n ")
                    idEmpresosa=input("¿Cuál es el ID de la nueva empresa?\n ")

                    nuevaEmpre=Empresa(idEmpresosa,nombreEmpresosa,abreviaturaEmpresosa)
                    listaEmpresas.append(nuevaEmpre)

                    print(Fore.GREEN + "Se agregado la empresa con exito!!\n")

                elif opcion=="2":
                    codEmpresosa = input(Fore.BLUE + "Ingresar codigo de la empresa: \n")
                    empresita = listaEmpresas.buscarByCodigo(codEmpresosa)
              
                    if empresita is None:
                        print(Fore.RED + "Esa empresa no se encuentra registrado en la lista")
                    else:
                    
                        nombrePuntoso=input("¿Cuál es el nombre del nuevo punto de atención?\n ")
                        direccionPuntoso=input("¿Cuál es la dirección del nuevo punto de atención?\n ")
                        idPuntoso=input("¿Cuál es el ID del nuevo punto de atención?\n ")

                        nuevoPuntoso=PuntoAtencion(idPuntoso,nombrePuntoso,direccionPuntoso)
                        empresita.puntoAtencion.append(nuevoPuntoso)

                        print(Fore.GREEN + "Se agregado el punto de atención a su empresa con exito!!\n")
                elif opcion=="3":
                    codEmpresa = input(Fore.BLUE + "Ingresar codigo de la empresa: \n")
                    empresa = listaEmpresas.buscarByCodigo(codEmpresa)
                    if empresa is None:
                        print(Fore.RED + "Esa empresa no se encuentra registrado en la lista")
                    else:
                        codPA=input(Fore.BLUE + "Ingresar codigo del punto de atención correspondiente: \n")
                        puntito=empresa.puntoAtencion.buscarByCodigo(codPA)
       
                        if puntito is None:
                            print(Fore.RED + "Ese escritorio no se encuentra registrado en la lista de empresas")
                        else:
                            nombreEscri=input("¿Cuál es el nombre del empleado del nuevo escritorio?\n ")
                            identiEscri=input("¿Cuál es la identificación del nuevo escritorio?\n ")
                            idEscri=input("¿Cuál es el ID del nuevo escritorio?\n ") 
                            
                            puntito.escritorio.append(idEscri,identiEscri,nombreEscri,"inactivo")

                            print(Fore.GREEN + "Se agregado el punto de atención a su empresa con exito!!\n")
                elif opcion=="4":
                    codEmpresosa = input(Fore.BLUE + "Ingresar codigo de la empresa: \n")
                    empresita = listaEmpresas.buscarByCodigo(codEmpresosa)
              
                    if empresita is None:
                        print(Fore.RED + "Esa empresa no se encuentra registrado en la lista")
                    else:
                        nombreTransa=input("¿Cuál es el nombre de la nueva transacción?\n ")
                        minutosTransa=input("¿Cuál es la duración en minutos de la nueva transacción?\n ")
                        idTransa=input("¿Cuál es el ID de la nueva transacción?\n ")
                        

                        nuevaTransa=Transacciones(idTransa,nombreTransa,minutosTransa)
                        empresita.transaccion.append(nuevaTransa)

                        print(Fore.GREEN + "Se agregado la nueva transacción a su empresa con exito!!\n")
            elif opcion =="8":
                
                nombreArchivo = input(Fore.BLUE + "Ingrese el nombre del archivo de configuración XML\n")
                ruta = './' + nombreArchivo
                listaEmpresasConfi = cargaArchivo2(ruta)[0]
                print(Fore.GREEN + "Se han cargado los datos con éxito!!\n")
                    

        elif opcionosa == '2':
            print(Fore.BLUE + "Querido empresario, ¿Qué desea hacer? \n")
            print(Fore.BLUE + "1 --- ingresar manualmente los datos")
            print(Fore.BLUE + "2 --- usar datos cargados del archivo \n")

            respuesturbia=input("¿Qué opción prefiere?  \n")

            if respuesturbia=="1":
                print(Fore.BLUE + "----------MENÚ DE SELECCION--------")
                codEmpresa = input(Fore.BLUE + "Ingresar codigo de la empresa a manipular: \n")
                empresaActual = listaEmpresas.buscarByCodigo(codEmpresa)
                if empresaActual is None:
                    print(Fore.RED + "Esa empresa no se encuentra registrado en la lista")
                else:
                    codPA=input(Fore.BLUE +"está en "+empresaActual.nombre+ ", ingrese el codigo del punto de atención a manipular : \n")
                    puntoActual=empresaActual.puntoAtencion.buscarByCodigo(codPA)
        
                    if puntoActual is None:
                        print(Fore.RED + "Ese escritorio no se encuentra registrado en la lista de empresas")
                    else:

                        print("Usted está en "+puntoActual.nombre+", indique a continuación qué desea hacer: ")
                        print(Fore.BLUE + "1-- Ver estado de punto de atención")
                        print(Fore.BLUE + "2-- Activar escritorio de servicio")
                        print(Fore.BLUE + "3-- Desactivar escritorio de servicio")
                        print(Fore.BLUE + "4-- Atender cliente")
                        print(Fore.BLUE + "5-- Solicitud de atención")
                        print(Fore.BLUE + "6-- Simular actividad")
                    
                        opcion = input(Fore.BLUE + "Favor seleccionar una opcion porfavor \n")

                        if opcion=="1":
                            print("Información de Puntos de Atención:\n")
                            
                            
                               
                        elif opcion=="2":
                            puntoActual.escritorio.raiz.estado="activo"
                            print(Fore.GREEN +"el escritorio de: "+puntoActual.escritorio.raiz.nombreE+" ha sido activado exitosamente!")
                        elif opcion=="3":
                            puntoActual.escritorio.raiz.estado="inactivo"
                            print(Fore.GREEN +"el escritorio de "+puntoActual.escritorio.raiz.nombreE+" ha sido desactivado exitosamente!")
                        elif opcion=="4":
                            print("estas en 'Atender cliente' ")
                        elif opcion=="5":
                            nombreCliente=input("¿Cuál es el nombre del nuevo cliente?\n ")
                            dpiCliente=input("¿Cuál es el dpi del nuevo cliente?\n ")
                            

                            nuevoClien=Clientes(dpiCliente,nombreCliente)
                            listaClientes.append(nuevoClien)
                        

                            print(Fore.GREEN + "Se agregado al cliente con exito!!\n")
                            
                            codigoTransa=input(Fore.BLUE +"Ingrese el código de la transacción que realizará\n ")
                            cantitransa=input("Ingrese la cantidad de transacciones de ese tipo que hará\n ")
                            
                            nuevaTrans=TransaNueva(codigoTransa,cantitransa)
                            nuevoClien.transaNueva.append(nuevaTrans)

                            print("el id de la nueva transaccion es: "+codigoTransa)
                            
                            if nuevoClien.transaNueva.search(codigoTransa)==True:
                                transaccionita=empresaActual.transaccion.buscarByCodigo(codigoTransa)


                                operacionosa=int(transaccionita.minutos)*int(cantitransa)

                                print("el tiempo promedio que tardará "+ nuevoClien.nombre+" es: ",operacionosa," minutos")
                            else:
                                print("esa transacción no existe")
                        elif opcion=="6":
                            print("estás en 'Simular actividad' ")
            elif respuesturbia=="2":
                print(Fore.BLUE + "----------MENÚ DE SELECCION--------")
                codiConfi = input(Fore.BLUE + "Ingresar codigo de la configuración a utilizar: \n")
                confiActual = listaEmpresasConfi.buscarByCodigo(codiConfi)
                empresaCurrent=listaEmpresas.buscarByCodigo(confiActual.idE)
                if confiActual is None:
                    print(Fore.RED + "Esa configuración no se encuentra registrado en la lista")
                else:
                    
                    puntoCurrent=empresaCurrent.puntoAtencion.buscarByCodigo(confiActual.idP)
        
                    if puntoCurrent is None:
                        print(Fore.RED + "Ese escritorio no se encuentra registrado en la lista de empresas")
                    else:
                        
                        print("la empresa a manipular es "+empresaCurrent.nombre+", y ")
                        print("el punto de atención es "+puntoCurrent.nombre+", indique a continuación qué desea hacer: \n")
                        print(Fore.BLUE + "1-- Ver estado de punto de atención")
                        print(Fore.BLUE + "2-- Activar escritorio de servicio")
                        print(Fore.BLUE + "3-- Desactivar escritorio de servicio")
                        print(Fore.BLUE + "4-- Atender cliente")
                        print(Fore.BLUE + "5-- Solicitud de atención")
                        print(Fore.BLUE + "6-- Simular actividad")
                    
                        opcion = input(Fore.BLUE + "Favor seleccionar una opcion porfavor \n")

                        if opcion=="1":
                            print("Información de Puntos de Atención:\n")

                            print("los escritorios activos son: ")

                            listaEscriActivo = cargaArchivo2(ruta)[2]
                            listaEscriActivo.print()

                    

                            puntoCurrent.escritorio.delete()
                            puntoCurrent.escritorio.delete()
                            
                            
                            print("los escritorios inactivos son: ")
                            puntoCurrent.escritorio.printPila()
                            
                            
                            
                               
                        elif opcion=="2":
                            puntoCurrent.escritorio.raiz.estado="activo"
                            print(Fore.GREEN +"el escritorio de: "+puntoCurrent.escritorio.raiz.nombreE+" ha sido activado exitosamente!")
                        elif opcion=="3":
                            puntoCurrent.escritorio.raiz.estado="inactivo"
                            print(Fore.GREEN +"el escritorio de "+puntoCurrent.escritorio.raiz.nombreE+" ha sido desactivado exitosamente!")
                        elif opcion=="4":
                            
                            print("estas en 'Atender cliente' ")
                        elif opcion=="5":
                            nombreClientoso=input("¿Cuál es el nombre del nuevo cliente?\n ")
                            dpiClientoso=input("¿Cuál es el dpi del nuevo cliente?\n ")
                            

                            nuevoClientoso=Clientes(dpiClientoso,nombreClientoso)
                            listaClientes.append(nuevoClientoso)
                        

                            print(Fore.GREEN + "Se agregado al cliente con exito!!\n")
                            
                            newCode=input(Fore.BLUE +"Ingrese el código de la transacción que realizará\n ")
                            amount=input("Ingrese la cantidad de transacciones de ese tipo que hará\n ")
                            
                            newTransa=TransaNueva(newCode,amount)
                            nuevoClientoso.transaNueva.append(newTransa)

                            print("el id de la nueva transaccion es: "+newCode)
                            
                            if nuevoClientoso.transaNueva.search(newCode)==True:
                                transaccionosa=empresaCurrent.transaccion.buscarByCodigo(newCode)


                                operacionsita=int(transaccionosa.minutos)*int(amount)

                                print("el tiempo promedio que tardará "+ nuevoClientoso.nombre+" es: ",operacionsita," minutos")
                            else:
                                print("esa transacción no existe")


                        elif opcion=="6":
                            print("estás en 'Simular actividad' ")
                            
    

def cargaArchivo1(ruta):
    tree = ET.parse(ruta)
    listaEmpresas = tree.getroot()
    listaEmpresasDesdeXml = ListaDoble()
    
    for element in listaEmpresas:
        for datotes in element.iter("empresa"):
            for nombreE in datotes.iter("nombre"):
                #print(nombreE.text)
                break
            for abreviatura in datotes.iter("abreviatura"):
               #print(abreviatura.text)
               pass
            nuevaEmpresa = Empresa(datotes.attrib["id"],nombreE.text,abreviatura.text)

        for datosos in element.iter("puntoAtencion"):
            for nombrePA in datosos.iter("nombre"):
                #print(nombrePA.text)
                pass
            for direccion in datosos.iter("direccion"):
                #print(direccion.text)
                pass

            nuevoPuntoAtencion = PuntoAtencion(datosos.attrib["id"],nombrePA.text,direccion.text)
            nuevaEmpresa.puntoAtencion.append(nuevoPuntoAtencion)
            
            for datita in datosos.iter("escritorio"):     
                for identificacion in datita.iter("identificacion"):
                        #print(identificacion.text)
                    pass
                for encargado in datita.iter("encargado"):
                        #print(encargado.text)
                    pass
                    
                nuevoPuntoAtencion.escritorio.append(datita.attrib["id"],identificacion.text,encargado.text,"inactivo")
                

        for datitos in element.iter("transaccion"):
            for nombreR in datitos.iter("nombre"):
                #print(nombreR.text)
                pass
            for tiempo in datitos.iter("tiempoAtencion"):
                #print(tiempo.text)
                pass

            nuevaTransaccion = Transacciones(datitos.attrib["id"],nombreR.text,tiempo.text)
            nuevaEmpresa.transaccion.append(nuevaTransaccion)

        listaEmpresasDesdeXml.append(nuevaEmpresa)
        #listaEmpresasDesdeXml.print()
        #nuevaEmpresa.puntoAtencion.print()
        #nuevoPuntoAtencion.escritorio.printPila()
        #nuevaEmpresa.transaccion.print()



    return listaEmpresasDesdeXml

def cargaArchivo2(ruta):
    tree = ET.parse(ruta)
    listadoInicial = tree.getroot()
    listaConfiDesdeXml = ListaDobleConfi()
    listaEscriADesdeXml = ListaDobleEscriA()
    listaClientesDesdeXml = ListaDobleC()
    
    for element in listadoInicial:
        for datotes in element.iter("configInicial"):
            nuevaConfi = Configuracion(datotes.attrib["id"],datotes.attrib["idEmpresa"],datotes.attrib["idPunto"])
            listaConfiDesdeXml.append(nuevaConfi)
        #listaConfiDesdeXml.print()
        for datosos in element.iter("escritorio"):
            nuevoEscriA=EscriActivos(datosos.attrib["idEscritorio"])
            listaEscriADesdeXml.append(nuevoEscriA)
        #listaEscriADesdeXml.print()
        for datita in element.iter("cliente"):
            for nombreC in datita.iter("nombre"):
                nuevoCliente=Clientes(datita.attrib["dpi"],nombreC.text)  
            listaClientesDesdeXml.append(nuevoCliente)
            #listaClientesDesdeXml.print() 
            for datosa in datita.iter("transaccion"):                    
                nuevaTransa=TransaNueva(datosa.attrib["idTransaccion"],datosa.attrib["cantidad"])
                nuevoCliente.transaNueva.append(nuevaTransa)
            #nuevoCliente.transaNueva.print()
           
    
    return listaConfiDesdeXml, listaClientesDesdeXml, listaEscriADesdeXml

    
             
menu()
