class Tire:
    """
    Represente el tipo de rueda
    """
    def __init__(self, tipo_rueda='estandar', ancho='estandar', ratio='estandar', diametro='estandar', marca='', construccion='') -> None:
        self.tipo_rueda=tipo_rueda
        self.ancho=ancho
        self.ratio=ratio
        self.diametro=diametro
        self.marca=marca
        self.construccion=construccion

    def __repr__(self):
        # corredera="ruedas manolo"
        # return corredera
        return "ruedas manolo"