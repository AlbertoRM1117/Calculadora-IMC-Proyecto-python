#le damos la bienvenida al usuario
print('¡Bienvenido a la calculadora de su índice de masa corporal, a continuacion ingrese sus datos!\n')


#Creamos un ciclo while para  que el usuario ingrese cada uno de los datos
while True:
    
    nombre = input('Introduce tu nombre: ')
    
    #utilizamos una sentencia if para que en caso que el usuario no ingrese ningun dato 
    # entre en el if y el ciclo se repita
    if nombre == "":
        print("No ingreso ningun dato, debe ingresar su nombre")
    elif nombre.isdigit():
        print("No debe de ingresar números")
    elif nombre.isalpha() == False:
        print("Error, no esta permitido ingresar caracteres que no sean letras del alfabeto")
               
    else:
        break

while True:
    apellido_pat = input('Ingrese su apellido paterno: ')
    if apellido_pat == "":
        print("No a ingresado nungun dato, debe ingresar su apellido")
    elif nombre.isdigit():
        print("No debe de ingresar números") 

    else:
        break
            
while True:
    apellido_mat = input('Ingrese su apellido materno: ')
    if apellido_mat == "":
        print('No ingreso ningun dato, debe ingresar su apellido materno')
    elif nombre.isdigit():
        print("No debe de ingresar números")    
    else:
        break    
        
while True:
    try:
        edad = int(input('Ingrese su edad: '))
        if edad < 0:
            print("No puede ingresar numeros negativos")
        else:
            break
    except ValueError:
        print('Error, debe ingresar un número')
      

while True:
    try:
        peso = float(input('Ingrese su peso: '))
        if edad < 0:
            print("No puede ingresar numeros negativos")
        else:
            break
    except ValueError:
        print('Error, debe ingresar un número')
        
                    


while True:
    try:
        estatura = float(input("Ingrese su estatura: "))
        if edad < 0:
            print("No puede ingresar numeros negativos")
        else:
            break
    except ValueError:
        print('Error,Debe ingresar un número')    
        

                   
imc = peso / estatura**2 
                       
#Creamos condicionales if y elif para que si el rango de imc se ecnuentra entre alguno de ellos 
# imprima los datos del usuario junto con su IMC 
if  imc < 18.5 :
    print (nombre+ " "+ apellido_pat + " " + apellido_mat + 
            " de " + str(edad) + " años de edad, con un  peso de " + str(peso) +  
            " Kg y una estatura de " + str(estatura) + ", tiene un IMC de: " + str(f' {imc:.2f}')+ 
            " y se encuentra en un rango de peso bajo")
    
elif imc >= 18.50 and imc <= 24.99 :
    print (nombre+ " "+ apellido_pat + " " + apellido_mat + 
            " de " + str(edad) + " años de edad, con un  peso de " + str(peso) +  
            " Kg y una estatura de " + str(estatura) + ", tiene un IMC de: " + str(f' {imc:.2f}')+ 
            " y se encuentra en un rango de peso normal") 
                   
elif imc >= 25.00 and imc <= 29.99:
    print (nombre+ " "+ apellido_pat + " " + apellido_mat + 
            " de " + str(edad) + " años de edad, con un  peso de " + str(peso) +  
            " Kg y una estatura de " + str(estatura) + ", tiene un IMC de: " + str(f' {imc:.2f}')+ 
             " y se encuentra en un rango de sobre peso")
                   
elif imc >= 30.0 and imc <= 34.99 :
    print (nombre+ " "+ apellido_pat + " " + apellido_mat + 
            " de " + str(edad) + " años de edad, con un  peso de " + str(peso) +  
            " Kg y una estatura de " + str(estatura) + ", tiene un IMC de: " + str(f' {imc:.2f}')+ 
            " y se encuentra en un rango de obesidad leve")        

elif imc >= 35.00 and imc <= 39.99:
    print (nombre+ " "+ apellido_pat + " " + apellido_mat + 
            " de " + str(edad) + " años de edad, con un  peso de " + str(peso) +  
            " Kg y una estatura de " + str(estatura) + ", tiene un IMC de: " + str(f' {imc:.2f}')+ 
            " y se encuentra en un rango de obesidad media")        
                        
elif imc >= 40.00:
    print (nombre+ " "+ apellido_pat + " " + apellido_mat + 
            " de " + str(edad) + " años de edad, con un  peso de " + str(peso) +  
            " Kg y una estatura de " + str(estatura) + ", tiene un IMC de: " + str(f' {imc:.2f}')+ 
            " y se encuentra en un rango de obesidad mórbida")
                        


    


          
       
        

    
        

      
        

