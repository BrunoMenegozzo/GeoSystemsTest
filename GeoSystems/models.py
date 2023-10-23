import datetime
from typing import Any

"""@package Empresa de television por cable GeoSystems: Models
    Modelado de las clases para el sistema de la empresa de television.

""" 


class AbonadoModel:
    """
        Esta clase modela el abonado.
        Parametros: id: id unico del abonado. type: Int
                    nombre: Nombre del abonado. type: String
                    direccion: Direccion del abonado. type: String
                    zona: zona del abonado. type: Zona
                    servicion_va: servicios de valor agregado contratados por el ususario. type: Servicio_VA
    """

    #Atributos
    id_counter = 0
    

    #Constructor
    def __init__(self, nombre, direccion, zona, servicio_va):
        """The constructor."""
        self.zona = zona
        if zona.cantidad_abonados >= zona.max_abonados :                        #Si la zona ya alcanzo el maximo de abonados no crea el objeto
            raise Exception("No se pueden añadir más abonados en esta zona")
            
        self.nombre = nombre
        self.direccion = direccion
        self.id = self.id_counter
        self.id_counter += 1
        self.servicio_va = servicio_va                                          #lista de servicios de valor agregado

    #Metodos
        #Getter y setter
    def get_id(self):
        
        return self.id

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_direccion(self):
        return self.direccion

    def set_direccion(self, direccion):
        self.direccion = direccion

    def get_zona(self):
        return self.zona

    def set_zona(self, zona):
        self.zona = zona

    def get_servicio_basico(self):
        return self.servicio_basico

    def set_servicio_basico(self, servicio_basico):
        self.servicio_basico = servicio_basico

    def get_servicio_va(self):
        return self.servicio_va

    def set_servicio_va(self, servicio_va):
        self.servicio_va = servicio_va

        
    def generar_factura(self):                                      #Metodo para facturar
        """ 
            Metodo que calcula el monto a pagar por el abonado y retorna la factura
            Return type: Factura
    
        """
        total = 0
        descuento_va = 1

        if 2 < len(self.servicio_va) :                              #Calcula el descuento por cantidad de serv.VA 
            descuento_va = len(self.servicio_va) * 0.05
            if descuento_va > 0.70:
                descuento_va = 0.7

        for servicio, precio in self.zona.servicios_dispo:          #Calculo del total a facturar teniendo en cuenta zona y cant. serv.VA
            if isinstance(servicio, ServicioVAModel):
                if servicio in self.servicio_va:
                    total += precio * descuento_va
            elif isinstance(servicio, ServicioBasicoModel):      
                if servicio == self.servicio_basico:            
                    total += precio
        
        return FacturaModel(abonado=self, fecha=datetime.datetime.now.month , total=total)
    
    
class ZonaModel:
    """
        Clase que modela las zonas.
        Atributos:  id: id de zona. type: Int
                    nombre: Nombre de la zona. type: String
                    servicio_dispo: Lista de servicios disponibles en la zona. type: List<(Servicio, float)>
                    max_abonado: Cantidad maxima de abonado esperados en esa zona. type: Int
                    abonados: Lista de abonados que se encuentran actualmente en esa zona. type: List<Abonados>
                    infra: Infraestructura intalada en la zona. type: Infra
    """
    #Atributos
    id_counter = 0

    #Constructor
    def __init__(self, nombre, servicios_dispo, max_abonados, abonados, infra):
        self.nombre = nombre
        self.id = self.id_counter
        self.id_counter += 1
        self.servicios_dispo = servicios_dispo              #Lista de tuplas de servicios y precios disponibles en la zona
        self.max_clientes = max_abonados                    #Cantidad maxima de clientes en la zona
        self.abonados = abonados                            #Lista de abonados en zona
        self.infra = infra                                  #La infraestructura de la zona 
        
    #Metodos
     #Getter y setter
    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_max_abonados(self):
        return self.max_abonados
    
    def set_max_abonados(self, max_abonados):
        self.max_clientes = max_abonados

    def get_servicios_dispo(self):
        return self.servicios_dispo
    
    def set_servicios_dispo(self, servicios_dispo):
        self.servicios_dispo = servicios_dispo

    def get_abonados(self):
        return self.abonados
    
    def set_abonados(self, abonados):
        self.abonados = abonados

    def get_infra(self):
        return self.infra
    
    def set_infra(self, infra):
        self.infra = infra


        
    def servicio_is_disponibles(self, consulta_servicio):           #Con este metodos se puede consultar si un servicio esta en la zona entrando con el nombre
        """ 
            Metodo para saber si algun servicio en particular esta disponible en esa zona
            Return type: Bool
    
        """
        if consulta_servicio in self.servicios_dispo.nombre:
            return True
        else:
            return False



    def get_servicio_basico(self):
        """ 
            Metodo que retorna el servicio basico disponible en esa zona.
            Return type: ServicioBasico
    
        """
        for servicio, precio in self.zona.servicios_dispo:                  #Retorna el servicio basico de esa zona
            if isinstance(servicio, ServicioBasicoModel):      
                return servicio



    def cantidad_abonados(self):                                            #Retorna la cantidad actual de abonado en la zona
        """ 
            Metodo que retorna la cantidad actual de abonado en la zona
            Return type: Int
    
        """
        return len(self.abonados) 


class SeñalTVModel:
    """
        Clase que modela la señal de televisión.
        Atributos:  id: id de la señal de TV. type: Int
                    nombre: Nombre de la señal de TV. type: String
                    
    """
    #Atributos
    id_counter = 0

    #Constructor
    def __init__(self, nombre):
        self.nombre = nombre
        self.id = self.id_counter
        self.id_counter += 1

    #Metodos
    def get_id(self):
        return self.id


    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre


class ServicioModel:
    """
        Clase que modela los servicios.
        Atributos:  id: id del servicio. type: Int
                    nombre: Nombre del servicio. type: String
                    
    """

    #Atributos
    id_counter = 0

    #Constructor
    def __init__(self, nombre):
        self.id = self.id_counter
        self.id_counter += 1
        self.nombre=nombre

    #Metodos
    def get_id(self):
        return self.id


    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre
    

class ServicioBasicoModel(ServicioModel):
    """
        Clase que modela los servicios basico. Hereda de Servicio
        Atributos:  id: id del servicio. type: Int
                    nombre: Nombre del servicio. type: String
                    señales_TV: lista de señales de television que tiene el servicio basico. type: list<SeñalTV>
                    
    """
    #Atributos
    señales_TV = []                                             # Lista de las señales que tiene este servicio basico en particular

    #Constructor
    def __init__(self, señales_TV):
        self.señales_TV = señales_TV
        
    
    #Metodos

    def add_señal_TV(self, señal_TV):                           # Añade una nueva señal de TV a las señales del servicio basico  
        """ 
            Metodo que añade una señal de TV a la lista señales_TV
    
        """
        if isinstance(señal_TV, SeñalTVModel):
            self.señales_TV.append(señal_TV)
        else:
            raise Exception("No es una señal de TV") 
         
    def remove_señal_TV(self, señal_TV):                        # Elimina una señal de TV de las señales del servicio basico  
        """ 
            Metodo que elimina una señal de TV de la lista de señales de TV
    
        """
        for index, señal in enumerate(self.señales_TV):
            if señal.id == señal_TV.id:
                self.señales_TV.pop(index)



    def get_señales_TV(self):
        return self.señales_TV
    
    def set_señales_TV(self,señales_TV):
        self.señales_TV = señales_TV


class ServicioVAModel(ServicioModel):
    """
        Clase que modela los servicios de valor agregado. Hereda de Servicio
        Atributos:  id: id del servicio. type: Int
                    nombre: Nombre del servicio. type: String
                    
    """
    #Atributos
    id_counter = 0

    #Constructor
    def __init__(self, nombre):
        self.nombre = nombre
        self.id = self.id_counter
        self.id_counter += 1
        
    #Metodos
    

class TerminalDelClienteModel:
    """
        Clase que modela la terminal del cliente.
        Atributos:  id: id de terminal. type: Int
                    abonado: Abonado conectado a dicha terminal. type: Abonado
                    
    """
    #Atributos
    id_counter = 0

    #Constructor
    def __init__(self, abonado):
        self.id = self.id_counter
        self.id_counter += 1 
        self.abonado = abonado

    #Metodos
        #Get y Set
    def get_id(self):
        return self.id

    def get_abonado(self):
        return self.abonado

class LineasDeFOModel:
    """
        Clase que modela las lineas de fibre optica. 
                    Atributos:  id: id de linea de fibre optica. type: Int
                    
                    
    """
    #Atributos
    id_counter = 0

    #Constructor
    def __init__(self):
        self.id = self.id_counter
        self.id_counter += 1 


    #Metodos
        #Get y Set
    def get_id(self):
        return self.id  

class InfraModel:
    """
        Clase que modela la infraestructura.
        Atributos:  id: id de infraestructura. type: Int
                    nombre: Nombre del sistma de infraestructura. type: String
                    lineas_de_fo: Las lineas de fibra optica en esa infraestructura. type: list<LineasDeFO>
                    concentrador_zonal: El concentrador zonal de la infraestructura. type: ConcentradorZonal
                    caja_distribucion: Las cajas de distribucion en la infraestructura. type: list<CajaDistribucion>
                    
    """
    #Atributos
    id_counter = 0

    #Constructor
    def __init__(self, nombre, lineas_de_fo, concentrador_zonal, caja_distribucion):
        self.id = self.id_counter
        self.id_counter += 1 
        self.nombre = nombre
        self.lineas_de_fo = lineas_de_fo
        self.concentrador_zonal = concentrador_zonal
        self.caja_distribucion = caja_distribucion

    #Metodos
        #Get y Set
    def get_id(self):
        return self.id


    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre
    
    
    def get_lineas_de_fo(self):
        return self.lineas_de_fo

    def set_lineas_de_fo(self, lineas_de_fo):
        self.lineas_de_fo = lineas_de_fo

    def get_concentrador_zonal(self):
        return self.concentrador_zonal

    def set_concentrador_zonal(self, concentrador_zonal):
        self.concentrador_zonal = concentrador_zonal
    
    def get_caja_distribucion(self):
        return self.caja_distribucion

    def set_caja_distribucion(self, caja_distribucion):
        self.caja_distribucion = caja_distribucion

class FacturaModel:
    """
        Clase que modela la factura.
        Atributos:  id: id de factura. type: Int
                    abonado: Abonado que debe pagar la factura. type: Abonado
                    fecha: Fecha de la factura. type: Fecha
                    total: Total a facturar. type: Float
                    
    """
    #Atributos
    id_counter = 0

    #Constructor
    def __init__(self, abonado, fecha, total):
        self.id = self.id_counter
        self.id_counter += 1
        self.abonado = abonado
        self.fecha = fecha
        self.total = total
    #Metodos
        #Get y Set
    def get_id(self):
        return self.id


    def get_abonado(self):
        return self.abonado

    def set_abonado(self, abonado):
        self.abonado = abonado

    def get_fecha(self):
        return self.fecha

    def set_fecha(self, fecha):
        self.fecha = fecha

    def get_total(self):
        return self.total

    def set_total(self, total):
        self.total = total

class ConcentradorZonalModel:
    """
        Clase que modela el concetrador zonal.
        Atributos:  id: id unico del concentrador zonal. type: Int
                                    
    """
    #Atributos
    id_counter = 0

    #Constructor
    def __init__(self):
        self.id = self.id_counter
        self.id_counter += 1 


    #Metodos
    def get_id(self):
        return self.id

class CajaDistribucionModel:
    """
        Clase que modela el concetrador zonal.
        Atributos:  id: id unico del concentrador zonal. type: Int
                    terminal_del_cleiente: lista de terminales conectadas a la caja de disribucion. type: list<TerminalDelCliente>
                                    
    """
    #Atributos
    id_counter = 0

    #Constructor
    def __init__(self, terminales_de_clientes):
        self.id = self.id_counter
        self.id_counter += 1 
        self.terminales_de_clientes = terminales_de_clientes

    #Metodos
    def get_id(self):
        return self.id

    
    def get_terminales_de_clientes(self):
        return self.terminales_de_clientes

    def set_terminal_del_cliente(self, terminales_de_clientes):
        self.terminales_de_clientes = terminales_de_clientes