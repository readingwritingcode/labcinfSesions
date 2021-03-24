# Planteo: Seleccionar entre un número x de postulantes, el que cumpla los requisitos para aspirar al cargo de programador
#-------------------------------------------------------------------------------------------------------------------------
# Definición de los requisitos y sus valores de referencia bajo la estructura de un diccionario   
datos_cargo = {"nombre_cargo":"programador",
               "experticia":"intermedio",
               "nota_mínima": 3.9
                  }
# Definción de la lista compuesta (listas entre listas) con los datos de cada uno de los aspirantes
postulantes = [["Carlos", "analista", "alto", 4.2],
               ["Jenny", "programador", "intermedio", 4.0],
               ["David", "practicante", "bajo", 3.0],
               ["Jaider", "desarrollador", "intermedio", 3.5],
               ["Carolina", "investigadora", "alto", 4.5],
               ["Tatiana", "programador", "intermedio", 3.3],
               ["Lorena", "programador", "alto", 4.6],
               ["Santiago", "programador", "intermedio", 3.9],
               ["Esteven", "digitador", "bajo", 3.0],
               ["Fernando", "analista", "alto", 4.5]
              ]
# Definición de tres listas vacías. Se actualizarán con los datos de los postulantes que cumplan cada nivel de requisitos
preselecc = [] # Almacena los postulantes que cumplan con el requisito del cargo
preselecc1 = [] # Almacena los postulantes que cumplan con los requisitos "cargo" y "experticia"
ganador = [] # Almacena los postulantes que cumplan con los requisitos "cargo", "experticia" y "nota_mínima"
print("PROCESO DE SELECCIÓN DE UN POSTULANTE A CARGO DE PROGRAMADOR")
print("EN CASO DE PRESENTARSE MÚLTIPLE SELECCIÓN, LO DEFINIRÁ EL COMITÉ ADMINISTRATIVO")
# A partir de la lista de postulantes, este ciclo evalúa, selecciona y almacena en nueva lista, 
# los postulantes que cumplan con el requisito del cargo

for i in range(10):
    if postulantes[i][1] == datos_cargo.get("nombre_cargo"):
        preselecc.append(postulantes[i])
x = len(preselecc)
y = 0
print("------------------------------------------------")
print(x, "Preseleccionados por Nombre de Cargo")
print("------------------------------------------------")
# A partir de la primera lista creada(preselecc) con los que cumplen requisito de cargo, este ciclo evalúa, selecciona y almacena 
# en nueva lista, los postulantes que cumplan con el requisito del cargo, más el de experticia

while y < x:
#    print (y)
    print(preselecc[y])
    if preselecc[y][2] == datos_cargo.get("experticia"):
        preselecc1.append(preselecc[y])
    y = y + 1    
x = len(preselecc1)
print("----------------------------------------------------")
print(x, "Preseleccionados por Nombre de Cargo y Experticia")
print("----------------------------------------------------")
# A partir de la segunda lista creada(preselecc1) con los que cumplen requisito de cargo y experticia, este ciclo evalúa, selecciona
# y almacena en nueva lista, los postulantes que cumplan con los requisitos de cargo, experticia y nota mínima.

for i in range(x):
    print(preselecc1[i])
    if preselecc1[i][3] >= datos_cargo.get("nota_mínima"):
        ganador.append(preselecc1[i])
x = len(ganador)

print("********************************************************")
print("Persona(s) que cumple(n) todos los requisitos...........")
print("********************************************************")
z = 0
# A partir de la tercera lista creada(ganador) con los que cumplen todos los requisitos, este ciclo muestra en detalle
# los datos de cada uno de los seleccionados

for i in range(x):
    while z < 4:
        if z == 0:
            print("Nombre:     ", ganador[i][z])
        if z == 1:
            print("Cargo:      ", ganador[i][z])
        if z == 2:
            print("Experticia: ", ganador[i][z])
        if z == 3:
            print("Nota:       ", ganador[i][z])
        z = z + 1
       
    print("===============================")
    z = 0

            
