"""Se deben ingresar 10 valores numéricos de a uno por vez.
Determinar:
El rango de variación de estos valores (valor máximo - valor mínimo).
El orden de ubicación de estos valores dentro de los 10 ingresados.
Se deben ingresar 10 valores numéricos de a uno por vez. """



for x in range(0,10):
     
     nro = int(input("Ingrese un numero:"))
     
     if x == 0:
         v_max = nro
         v_min = nro
     else:
         if nro > v_max:
             v_max = nro
         else:
             if(nro < v_min):
                 v_min = nro
                 
     variacion = v_max - v_min
       
print("La varacion es de: ",variacion)
