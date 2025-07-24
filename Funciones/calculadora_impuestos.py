print('*** Calculadora de impuestos ***')

def calcular_impuesto(pago, impuesto):
    return pago + pago * (impuesto/100)


pago_bruto = float(input('Dime el pago sin impuesto: '))
porcentaje = float(input('Dime el porcentaje de impuesto: '))
print(f'El pago con impuesto es: {calcular_impuesto(pago_bruto, porcentaje)}')