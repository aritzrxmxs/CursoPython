class Empleado:

    contador_empleados = 0

    def __init__(self, nombre, departamento):
        Empleado.contador_empleados += 1
        self._nombre = nombre
        self._departamento = departamento
        self._id = Empleado.contador_empleados

    @classmethod
    def obtener_total_empleados(cls):
        return cls.contador_empleados