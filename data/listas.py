#TODA LISTA SE DEBE DE ESCRIBIR EN PLURAL
arboles=['ceiba','yarumo', 'manzano', 'guayacan']
municipios=['medellin', 'titiribi', 'carolina del principe']
hectareasSembradas=[2500,500,1200]
LluviasMayoresA500=[False, True, True]

#Recorriendo un arreglo...
#Accerder de FORMA DINAMICA el contenido de un arreglo
#Para RECORRERLO DEBO UTILIZAR UN CICLO O UN BUCLE O LOOP

#ciclo while (mientras)
'''contador=0
while contador<10 :
    contador=contador+1
    print("Estoy triunfando...")'''
    
#Ciclo for (para)

'''for i in range(1,301,2):
    print (i)'''
 
#RECORRER DINAMICAMENTE UN ARREGLO USANDO FOREACH (PARA CADA UNO)
for arbol in arboles:
    print(arbol)   

for municipio in municipios:
    print(municipio)    
        