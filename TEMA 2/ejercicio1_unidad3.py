horas = input ('Introduzca las horas: ')
horas = int(horas)
precio = input ('Introduzca el precio/hora: ')
precio = int (precio)
if horas>40:
    h_extra = horas-40
    p_extra = precio*1.5
total = (horas-h_extra) * precio + h_extra * p_extra
print ('El total a pagar es:', total)
