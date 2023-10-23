class AbonadoView:
    def get_fields(self, abonado):
        fields={
            'id': abonado.get_id(),
            'nombre': abonado.get_nombre(),
            'zona': abonado.get_zona(),
            'direccion': abonado.get_direccion(),
            'servicio_basico': abonado.get_servicio_basico(),
            'servicio_va': abonado.get_servicio_va()
        }

        return fields
    
    def set_fields(self,abonado):                               #Por cuestiones de tiempo no se implemento el caso de los atributos que son objetos, ya que se complicaria la logica 
        new_nombre = input("Ingrese el nuevo nombre: ")
        new_direccion = input("Ingrese la nueva direccion: ")
        abonado.nombre = new_nombre
        abonado.direccion = new_direccion
    

class ZonaView:
    def get_fields(self, zona):
        fields={
            'id': zona.get_id(),
            'nombre': zona.get_nombre(),
            'servicios_dispo': zona.get_servicios_dispo(),
            'max_abonados': zona.get_max_abonados(),
            'abonados': zona.get_abonados(),
            'infra': zona.get_infra()
        }

        return fields
    
    def set_fields(self,zona):                               #Por cuestiones de tiempo no se implemento el caso de los atributos que son objetos, ya que se complicaria la logica 
        new_nombre = input("Ingrese el nuevo nombre: ")
        new_max_abonados = input("Ingrese la nueva direccion: ")
        zona.nombre = new_nombre
        zona.direccion = new_max_abonados
    


class SeñalTVView:
    def get_fields(self, señal_TV):
        fields={
            'id': señal_TV.get_id(),
            'nombre': señal_TV.get_nombre(),           
        }
        return fields
    
    def set_fields(self,señal_TV):                               #Por cuestiones de tiempo no se implemento el caso de los atributos que son objetos, ya que se complicaria la logica 
        new_nombre = input("Ingrese el nuevo nombre: ")
        
        señal_TV.nombre = new_nombre
        


class ServicioView:
    def get_fields(self, servicio):
        fields={
            'id': servicio.get_id(),
            'nombre': servicio.get_nombre(),
        }

        return fields
    
    def set_fields(self,servicio):                               #Por cuestiones de tiempo no se implemento el caso de los atributos que son objetos, ya que se complicaria la logica 
        new_nombre = input("Ingrese el nuevo nombre: ")
        new_direccion = input("Ingrese la nueva direccion: ")
        servicio.nombre = new_nombre
        servicio.direccion = new_direccion
    

class ServicioBasicoView(ServicioView):
    def get_fields(self, servicio_basico):
        fields = super().get_fields() 
        fields['señales_tv'] = servicio_basico.get_señales_TV()  

        return fields
    
    def set_fields(self,servicio_basico):                               #Por cuestiones de tiempo no se implemento el caso de los atributos que son objetos, ya que se complicaria la logica 
        new_nombre = input("Ingrese el nuevo nombre: ")
        servicio_basico.nombre = new_nombre
        


class ServicioVAView(ServicioView):
    def get_fields(self, servicio_va):
        fields = super().get_fields() 
        return fields
    
    def set_fields(self,servicio_basico):                               #Por cuestiones de tiempo no se implemento el caso de los atributos que son objetos, ya que se complicaria la logica 
        new_nombre = input("Ingrese el nuevo nombre: ")
        servicio_basico.nombre = new_nombre


class TerminalDelClienteView:

    def get_fields(self, terminal_del_cliente):
        fields={
            'id': terminal_del_cliente.get_id(),
            'abonado': terminal_del_cliente.get_abonado(),
        }

        return fields
    

class LineasDeFOView:
     def get_fields(self, lineas_FO):
        fields={
            'id': lineas_FO.get_id(),
        }

        return fields


class InfraView:
    def get_fields(self, infra):
        fields={
            'id': infra.get_id(),
            'nombre': infra.get_nombre(),
            'lineas_de_fo': infra.get_lineas_de_fo(),
            'concentrador_zonal': infra.get_concentrador_zonal(),
            'caja_distribucion': infra.get_caja_distribucion(),
        }

        return fields
    

class FacturaView:
    def get_fields(self, zona):
        fields={
            'id': zona.get_id(),
            'fecha': zona.get_fecha(),
            'abonado': zona.get_abonado(),
            'total': zona.get_total()
        }

        return fields
    
    def set_fields(self,zona):                               #Por cuestiones de tiempo no se implemento el caso de los atributos que son objetos, ya que se complicaria la logica 
        new_total = input("Ingrese el nuevo nombre: ")
        new_fecha = input("Ingrese la fecha: ")
        zona.nombre = new_total
        zona.fecha = new_fecha

class ConcentradorZonalView:
    def get_fields(self, concentrador_zonal):
        fields={
            'id': concentrador_zonal.get_id(),
            
        }

        return fields
    


class CajaDistribucionView:
    def get_fields(self, caja_distribucion):
        fields={
            'id': caja_distribucion.get_id(),
            'caja_distribucion': caja_distribucion.get_terminal_del_cliente()
        }

        return fields
    