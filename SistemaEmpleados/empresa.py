from SistemaEmpleados.empleado import Empleado


class Empresa:

    def __init__(self, nombre):
        self._nombre = nombre
        self._empleados = []

    def contratar_empleado(self, nombre, departamento):
        empleado = Empleado(nombre, departamento)
        self._empleados.append(empleado)

    def obetener_numero_empleados_departamento(self, departamento):
        contador_empleados_por_departamento = 0
        for empleado in self._empleados:
            if empleado._departamento == departamento:
                contador_empleados_por_departamento += 1
        return contador_empleados_por_departamento

    def obtener_total_empleados(self):
        print(f'\nTotal de empleaos para la empresa: {self._nombre}')
        for empleado in self._empleados:
            print(f'''Empleado {empleado._id}
            Nombre: {empleado._nombre}
            Departamento: {empleado._departamento}''')