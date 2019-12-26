# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

#------------------------------------------------------------------------
#Programa para determinar el valor de un pasaje de avion
valor=0

distancia = float(input("Ingrese la distancia recorrer: "))#ingresar valor en metros

num_dias = int(input("Ingrese el número de dias de estancia: "))

if distancia > (1000*(10**3)) and num_dias > 7:
    valor=(35*distancia*30)/100
    print(valor)
else:
    valor=35*distancia
    print(valor)
    
#------------------------------------------------------------------------   
    
#Programa para determinar la recepción de equipajes en un avión BOING 747


from tabulate import tabulate
    
peso_max=18000000 #Peso maximo permitido
peso_max_bulto=500000 #Peso maximo por bulto permitido
peso_carga=0 #Peso total de la carga
num_bultos=0 #Número de bultos ingresados
peso_bulto=0
lista_bulto=[] #Lista de los bultos ingresados
bulto_mas_pesado=0
bulto_mas_liviano=500000
valor_equipaje=0
valor_equipaje_total=0
lista_valor_equipaje_total=[]
valor_equipaje_total_US=0
lista_valor_equipaje_total_US=[]
peso_prom=0 #Peso promedio
Resultados = {}

while peso_carga < peso_max:
    
    peso_bulto = float(input("Ingrese peso del bulto: "))
    lista_bulto.append(peso_bulto)
    peso_carga = peso_carga + peso_bulto
    
    if peso_bulto > peso_max_bulto:
        print("¡¡¡Peso máximo excedido!!!")
    else:
        num_bultos=num_bultos + 1
        peso_prom=(peso_carga/num_bultos)
        
        if bulto_mas_pesado > peso_bulto:
            bulto_mas_pesado = bulto_mas_pesado
        else:
            bulto_mas_pesado = peso_bulto
            
        if bulto_mas_liviano > peso_bulto: 
            bulto_mas_liviano = peso_bulto
        else:
            bulto_mas_liviano = bulto_mas_liviano
            
        if peso_bulto > 0 and peso_bulto <= 25000:
            valor_equipaje = 0
            print("El valor del equipaje es: ", valor_equipaje)
        elif peso_bulto > 26000 and peso_bulto <= 300000:
            valor_equipaje = (peso_bulto*1500)/1000
            print("El valor del equipaje es: ", valor_equipaje)
        else:
            valor_equipaje = (peso_bulto*2500)/1000
            print("El valor del equipaje es: ", valor_equipaje)
        
        valor_equipaje_total=valor_equipaje_total + valor_equipaje
        lista_valor_equipaje_total.append(valor_equipaje_total)
        valor_equipaje_total_US=(valor_equipaje_total/3350)
        lista_valor_equipaje_total_US.append(valor_equipaje_total_US)
        
print("El número total de bultos es: ", num_bultos)
print("El peso total de la carga es: ", peso_carga)
print("El peso promedio de la carga es: ", peso_prom)
print("El peso del bulto mas pesado es: ", bulto_mas_pesado)
print("El peso del bulto mas liviano es: ", bulto_mas_liviano)
print("El valor total del equipaje es: ", valor_equipaje_total)
print("El valor total del equipaje en dolares es: ", valor_equipaje_total_US)
    
Resultados = {lista_bulto,
                  lista_valor_equipaje_total,
                  lista_valor_equipaje_total_US}
    
print(tabulate(Resultados, headers = ['Peso (gramos)', 'Valor total', 'Valor total US']))
        
        



































#---------------------------------------------------------------