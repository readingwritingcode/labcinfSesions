from time import sleep
from progress.bar import Bar

# Planteo: Seleccionar entre un número x de postulantes, el que cumpla los requisitos para aspirar al cargo de programador
#-------------------------------------------------------------------------------------------------------------------------
# Definición de los requisitos y sus valores de referencia bajo la estructura de un diccionario   
datos_cargo = {"nombre_cargo":"programador",
               "experticia":"intermedio",
               "nota_mínima": 3.9
                  }
# Definción de la lista compuesta (listas entre listas) con los datos de cada uno de los aspirantes
postulantes = [
    
    {"nombre":"Carlos", 
    "profesion":"analista",
    "experticia": "alto",
    "nota": 4.2},

    {"nombre":"Jenny",
     "profesion":"programador", 
     "experticia":"intermedio",
      "nota":4.0},

    {"nombre":"David",
     "profesion":"practicante", 
     "experticia":"bajo",
      "nota": 3.0},

      {"nombre":"Jaider",
     "profesion":"desarrollador", 
     "experticia":"intermedio",
      "nota": 3.5},

       {"nombre":"Carolina",
     "profesion":"investigadora", 
     "experticia": "alto",
      "nota": 4.5},

      {"nombre":"Tatiana",
     "profesion":"programador", 
     "experticia":"intermedio",
      "nota": 3.3},

       {"nombre":"Lorena",
     "profesion":"programador", 
     "experticia":"alto",
      "nota": 4.6}
]
            
# Definición de tres listas vacías. Se actualizarán con los datos de los postulantes que cumplan cada nivel de requisitos
preselecc = [] # Almacena los postulantes que cumplan con el requisito del cargo
preselecc1 = [] # Almacena los postulantes que cumplan con los requisitos "cargo" y "experticia"
finalistas = [] # Almacena los postulantes que cumplan con los requisitos "cargo", "experticia" y "nota_mínima"
print("PROCESO DE SELECCIÓN DE UN POSTULANTE A CARGO DE PROGRAMADOR")
print("EN CASO DE PRESENTARSE MÚLTIPLE SELECCIÓN, LO DEFINIRÁ EL COMITÉ ADMINISTRATIVO")
# A partir de la lista de postulantes, este ciclo evalúa, selecciona y almacena en nueva lista, 
# los postulantes que cumplan con el requisito del cargo

for i in postulantes:

    # preseleccionados a partir de nombre de cargo
    if i.get("profesion") == datos_cargo.get("nombre_cargo"):
        preselecc.append(i)

    # preseleccionados1 a partir de nivel de experticia
        if i.get("experticia") == datos_cargo.get("experticia"):
            preselecc1.append(i)

    # finalistas cumplen todo y buena calificacion
            if i.get("nota") >= datos_cargo.get("nota_minima"):
                finalistas.append(i)

if len(finalistas) >1:
    print("CASO MÚLTIPLE SELECCIÓN, LO DEFINIRÁ EL COMITÉ ADMINISTRATIVO")
    # proceso de seleccion de candidato con mejor calificacion
    
    with Bar('Processing...') as bar:
        for i in range(100):
            sleep(0.02)
            bar.next()

    m=finalistas[0].get('nota')
    for i in finalistas:
        if i.get('nota')>m:
            m = i.get('nota')
            g=i
    print("enviar correo a: %s, asunto:bienvendo!" % g['nombre'])

else:

    print("enviar correo a: %s, asunto:bienvendo!" % finalistas[0]['nombre'])