"""
Nombre: calculadora
Entradas: operacion, op1, op2
Salidas: el resultado del calculo correspondiente de cada operación
Restricciones:
    Las operaciones soportadas son suma=1, resta=2, multiplicación=3 y divición_entera=4
    No es posible la divición entre 0
    Los parámetros deben ser de tipo entero
    Los operadores deben ser de tipo entero
"""
def calculadora(operacion, op1, op2):
    if operacion < 1:
        return "Error: el parámetro operacion debe ser un valor mayor que CERO"
    if operacion > 4:
        return "Error: el parámetro operacion debe ser unn valor menor a 5"

    return calculadora_aux(operacion, op1, op2)

def calculadora_aux(operacion, op1, op2):

    while (op1, int) and (op2, int):
        if operacion == 1:
            suma = op1 + op2
            resultado = suma
            return resultado
        elif operacion == 2:
            resta = op1 - op2
            resultado = resta
            return resultado
        elif operacion == 3:
            multiplicación = op1 * op2
            resultado = multiplicación
            return resultado
        if (operacion == 4) and op2 != 0:
            divición_entera = op1 // op2
            resultado = divición_entera
            return resultado
        else:
            return "Error: no es posible la divición entre 0"

"""
Nombre: contadorDigitos
Entradas: num, digito
Salidas: el retorno del número de veces que el dígito aparece en el número
Restricciones:
    Ambos parámetros deben ser de tipo entero
    El párametro llamado digito debe ser menor a 10 y mayor igual a 0
"""
def contadorDigitos(num, digito):
    if not isinstance(num, int):
        return "Error: el parámetro num debe ser de tipo entero"
    if not isinstance(digito, int):
        return "Error: el parámetro digito debe ser entero"
    if(digito > 10):
        return "Error: El párametro llamado digito debe ser menor a 10"
    if(digito < 0):
        return "Error: El párametro llamado digito debe ser mayor o igual a 0"

    return contadorDigitos_aux(num, digito)

def contadorDigitos_aux(num, digito):
    resultado = 0
    
    if num == 0 and digito == 0:
        resultado = resultado + 1

    while num != 0:
        num % 10
        if digito == num % 10:
            resultado = resultado + 1
            num = num // 10
        else:
            num = num // 10

    return resultado

"""
Nombre: sumatoria_V2
Entradas: inicio, fin, distancia, excepcion
Salidas: la suma total de los números desde el parámetro inicio hasta el final
Restricciones:
    Todos parámetros deben ser de tipo entero
    Los párametros distancia y excepcion debe ser menor a 10 y mayor a 0
    Los valores de inicio y fin deben ser positivos
    Si la distancia es un número negativo, el valor de fin debe ser menor a inicio
    Si la distancia es un número positivo, el valor de fin debe ser mayor a inicio
    Si excepcion es igual a cero, se debe ignorar este valor
"""
def sumatoria_V2(inicio, fin, distancia, excepcion):
    if not isinstance(inicio, int):
        return "Error: el parámetro num debe ser de tipo entero"
    if not isinstance(fin, int):
        return "Error: el parámetro fin debe ser de tipo entero"
    if not isinstance(distancia, int):
        return "Error: el parámetro distancia debe ser de tipo entero"
    if not isinstance(excepcion, int):
        return "Error: el parámetro excepcion debe ser de tipo entero"
    if (inicio < 0):
        return "Error: el valor de inicio debe ser positivo"
    if (fin < 0):
        return "Error: el valor de fin debe ser positivo"
    if (-2 < distancia > 10):
        return "Error: el párametro distancia debe ser menor a 10"
    if (excepcion > 10):
        return "Error: el párametro excepcion debe ser menor a 10"
    if (excepcion < 0):
        return "Error: el párametro excepcion debe ser mayor a 0"


    return sumatoria_V2_aux(inicio, fin, distancia, excepcion)

def sumatoria_V2_aux(inicio, fin, distancia, excepcion):
    if distancia <= 0:
        if inicio > fin:
            resultado = 0
            while inicio >= fin:
                if excepcion != 0:
                    if inicio % excepcion == 0:
                        inicio -= distancia
                    else:
                        resultado += inicio
                        inicio -= distancia
                else:
                    resultado += inicio
                    inicio -= distancia

            return resultado
        else:
            return "Error: el rámetro inicio debe ser mayor a fin"

    else:
        resultado = 0
        while inicio <= fin:
            if excepcion != 0:
                if inicio % excepcion == 0:
                    inicio += distancia
                else:
                    resultado += inicio
                    inicio += distancia
            else:
                resultado += inicio
                inicio += distancia
        return resultado
                



        
            
        
            

        
        
            
        

         
    
        
        
    

            
    
        
        
        
    
