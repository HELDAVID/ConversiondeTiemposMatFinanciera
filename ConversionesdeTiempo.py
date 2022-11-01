""" 
Unidades y dias:
Semana: 7
Mes: 30
Bimestre: 60
Trimestre: 90
Cuatrimestre: 120
Semestre: 180
Año: 360

Bimestre = 2 meses
Trimestre = 3 meses
Cuatrimestre: 4 meses
Semestre : 6 meses 
Año : 12 meses
"""

# Ejercicio: Convertir 8 cuatrimestres en trimestres:

from cgi import print_form


Cuatrimestres = 8
MesesXCuatrimestre = 4
Trimestres = 3

Conversion1= Cuatrimestres * (MesesXCuatrimestre / Trimestres)
print(f"la cantidad de trimestres es {Conversion1}")


# Ejercicio: Desea convertir 13.3037 años en expresiones enteras en años, meses y dias:

años = 13
años1 = 0.3037
Taño =  12
DiasdelMes = 30

CalculoAño1 = (años1 * Taño)
print(f"el valor de los 3037 es {CalculoAño1}")
CalculoResiduo = CalculoAño1 - 3 #años 
calculoaño2 = CalculoAño1 - 0.6444
residuoCalculoAño1 = CalculoResiduo * 30
print(CalculoResiduo )
print(round(residuoCalculoAño1))
print(f"la solucion es {años} {calculoaño2} { round(residuoCalculoAño1)}")
