class AbonadoController: 
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def get_fields(self):
        self.view.get_fields(self.model)

    def set_fields(self):
        self.view.set_fields(self.model)

class ZonaController: 
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def get_fields(self):
        self.view.get_fields(self.model)

    def set_fields(self):
        self.view.set_fields(self.model)

class SeñalTVController: 
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def get_fields(self):
        self.view.get_fields(self.model)

    def set_fields(self):
        self.view.set_fields(self.model)

class ServicioController: 
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def get_fields(self):
        self.view.get_fields(self.model)

    def set_fields(self):
        self.view.set_fields(self.model)

class ServicioBasicoController(ServicioController): 
    def __init__(self, model, view):
        self.model = model
        self.view = view


class ServicioVAController(ServicioController): 
    def __init__(self, model, view):
        self.model = model
        self.view = view



class TerminalDelClienteController: 
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def get_fields(self):
        self.view.get_fields(self.model)

    def set_fields(self):
        self.view.set_fields(self.model)


class LineasDeFOController: 
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def get_fields(self):
        self.view.get_fields(self.model)

    def set_fields(self):
        self.view.set_fields(self.model)

class InfraController: 
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def get_fields(self):
        self.view.get_fields(self.model)

    def set_fields(self):
        self.view.set_fields(self.model)

class FacturaController: 
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def get_fields(self):
        self.view.get_fields(self.model)

    def set_fields(self):
        self.view.set_fields(self.model)

class ConcentradorZonalController: 
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def get_fields(self):
        self.view.get_fields(self.model)

    def set_fields(self):
        self.view.set_fields(self.model)

class CajaDistribucionController: 
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def get_fields(self):
        self.view.get_fields(self.model)

    def set_fields(self):
        self.view.set_fields(self.model)
