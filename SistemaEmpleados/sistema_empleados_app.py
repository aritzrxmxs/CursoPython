from SistemaEmpleados.empleado import Empleado
from SistemaEmpleados.empresa import Empresa

print('*** Sistema de empleados ***')

# Creamos una instancia de una empresa
empresa1 = Empresa('Global Mentoring')

# Contratamos algunos empleados
empresa1.contratar_empleado('Aritz', 'Ventas')
empresa1.contratar_empleado('Victoria', 'Acosta')
empresa1.contratar_empleado('Pedro', 'Ventas')
empresa1.contratar_empleado('Roberto', 'Recursos Humanos')

# Obtener el total de empleados
print(f'Total de empleados: {Empleado.obtener_total_empleados()}')

# Obtener el numero de empleados en el departamento de ventas
print(f'Empleados en el departamento de Ventas: '
      f'{empresa1.obetener_numero_empleados_departamento('Ventas')}')

# Mostrar todos los empleados de empresa
empresa1.obtener_total_empleados()