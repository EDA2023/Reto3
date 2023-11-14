﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
import datetime
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.ADT import minpq as mpq
from DISClib.ADT import indexminpq as impq
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf
import datetime as dt
from time import strftime
from tabulate import tabulate

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #TODO: Inicializar las estructuras de datos
    earthquakes = {"temblores": None,
                    "time": None,
                    "mag": None,
                    "depth": None, 
                    "nst" : None
                    }
    
    earthquakes["temblores"] = lt.newList("ARRAY_LIST")
    earthquakes["time"] = om.newMap(omaptype="RBT", cmpfunction=cmpDates)
    earthquakes["mag"] = om.newMap(omaptype="RBT", cmpfunction=cmpMag)
    earthquakes["depth"] = om.newMap(omaptype="RBT", cmpfunction=cmpDepth)
    earthquakes["nst"] = om.newMap(omaptype="RBT", cmpfunction=cmpNst)

    return earthquakes


# Funciones para agregar informacion al modelo

def add_temblores_fechas(earthquakes, temblores):
    """
    Función para agregar fechas al arbol.
    """
    fechas = earthquakes["time"]
    if not om.contains(fechas,temblores["time"]):
        lista = lt.newList("ARRAY_LIST")
        lt.addLast(lista, temblores)
        om.put(fechas, temblores["time"], lista)
    else:
        pair = om.get(fechas, temblores["time"])
        lista = me.getValue(pair)
        lt.addLast(lista, temblores)   
        mp.put(fechas, temblores["time"], lista)
   
    return fechas
        
def add_mag(earthquakes, temblores):
    """
    Función para agregar magnitudes al arbol.
    """
    magnitudes = earthquakes["mag"]
    if not om.contains(magnitudes,temblores["mag"]):
        lista = lt.newList("ARRAY_LIST")
        lt.addLast(lista, temblores)
        om.put(magnitudes, temblores["mag"], lista)
    else:
        pair = om.get(magnitudes, temblores["mag"])
        lista = me.getValue(pair)
        lt.addLast(lista, temblores)   
        mp.put(magnitudes, temblores["mag"], lista)
   
    return magnitudes

def add_depth(earthquakes, temblores):
    """
    Función para agregar magnitudes al arbol.
    """
    magnitudes = earthquakes["depth"]
    if not om.contains(magnitudes,temblores["depth"]):
        lista = lt.newList("ARRAY_LIST")
        lt.addLast(lista, temblores)
        om.put(magnitudes, temblores["depth"], lista)
    else:
        pair = om.get(magnitudes, temblores["depth"])
        lista = me.getValue(pair)
        lt.addLast(lista, temblores)   
        mp.put(magnitudes, temblores["depth"], lista)
   
    return magnitudes

def add_nst(earthquakes, temblores):
    """
    Función para agregar magnitudes al arbol.
    """
    magnitudes = earthquakes["nst"]
    if not om.contains(magnitudes,temblores["nst"]):
        lista = lt.newList("ARRAY_LIST")
        lt.addLast(lista, temblores)
        om.put(magnitudes, temblores["nst"], lista)
    else:
        pair = om.get(magnitudes, temblores["nst"])
        lista = me.getValue(pair)
        lt.addLast(lista, temblores)   
        mp.put(magnitudes, temblores["nst"], lista)
   
    return magnitudes

def add_earthquakes(earthquakes, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    data_filtrada = filtrar(data["code"], data["time"], data["lat"], data["long"], data["mag"], data["nst"], data["title"], data["depth"], data["felt"], data["cdi"], data["mmi"], data["tsunami"])
    lt.addLast(earthquakes["temblores"], data_filtrada)
    add_mag(earthquakes, data_filtrada)
    add_temblores_fechas(earthquakes, data_filtrada)
    add_depth(earthquakes, data_filtrada)
    add_nst(earthquakes, data_filtrada)

def filtrar(code, time, lat, long, mag, nst, title,depth,felt, cdi, mmi, tsunami):
    resp = {
        "code": code,
        "time": time,
        "lat": lat,
        "long": long,
        "mag": float(mag),
        "nst": float(nst) if not nst in[None,"", " "] else "Unknown",
        "title": title,
        "depth": float(depth),
        "felt": felt if not felt in [None, "", " "] else "Unknown",
        "cdi": cdi if not cdi in [None, "", " "] else "Unknown",
        "mmi": mmi if not mmi in [None, "", " "] else "Unknown",
        "tsunami": False if tsunami == "0" else True
    }
    
    return resp

# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass

def timeSize(earthquakes):
    """
    Retorna el tamaño de la lista de datos
    """
    return lt.size(earthquakes["time"])

def temblores_size(earthquake):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    return lt.size(earthquake["temblores"])


def req_1(earthquakes, initial, final):
    """
    Función que soluciona el requerimiento 1
    """
    
    treeDates = earthquakes["time"]
    valores = om.values(treeDates, initial, final)
    llaves = om.keys(treeDates, initial, final)
    lt.iterator(valores)
    resp = lt.newList("ARRAY_LIST")

    i=1
    while i<= lt.size(llaves):
        key = lt.getElement(llaves, i)
        value = lt.getElement(valores, i)
        dic = {"time": key,       
                "events": lt.size(value),    
                "details": tabulate(lt.iterator(value),headers="keys",tablefmt="grid", maxcolwidths=[None, None, None, None, None, None, 20, None, None, None, None, None])
                }
        lt.addLast(resp, dic)
        i+=1
              
    return resp, lt.size(llaves)


def req_2(earthquakes, inferior, superior):
    """
    Función que soluciona el requerimiento 2
    """
    
    mag_map = earthquakes["mag"]
    values = om.values(mag_map, inferior, superior)
    keys = om.keys(mag_map, inferior, superior)
    lt.iterator(values)
    answer = lt.newList("ARRAY_LIST")
    
    i=1
    
    while i<= lt.size(keys):
        key = lt.getElement(keys,i)
        value = lt.getElement(values,i)
        dic = {"mag":key,
               "events": lt.size(value),
               "details": tabulate(lt.iterator(value), headers="keys", tablefmt="grid",maxcolwidths=[None, None, None, None, None, None, 20, None, None, None, None, None])
               }
        lt.addLast(answer, dic)
        i+=1
        
    return answer, lt.size(keys)



def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


"""def req_5(earthquakes, depth, nst):

    
    arbol = earthquakes["depth"]
    values_depth = om.values(arbol, depth, om.maxKey(arbol))
    fechas = om.newMap(cmpfunction=cmpDates)

    contador = 0    
    for value in lt.iterator(values_depth):
        element = value["elements"]
        lt.iterator(element)
        values_nst  =om.values(element["nst"], nst, om.maxKey(value["nst"]))
        for evento in lt.iterator(values_nst):
            for evento in lt.iterator(evento):
                time = evento["time"]
                if om.contains(fechas, time):
                    value = me.getValue(om.get(fechas, time))
                else:
                    value = lt.newList("ARRAY_LIST")
                    om.put(fechas, time, value)
                contador+=1
                lt.addLast(value, evento)
                
    lista_fechas = om.keySet(fechas)
    lista_listas_eventos = om.valueSet(fechas)
    lista_retorno = lt.newList("ARRAY_LIST")
    
    for i in range(1, lt.size(lista_fechas)+1):
        titulos = ["mag","lat","long", "depth", "sig", "gap", "nst", "title", "cdi", "mmi", "magType", "type", "code"]
        dic = {"time": lt.getElement(lista_fechas, i),
               "events": lt.size(lt.getElement(lista_listas_eventos,i)),
               "details": tabulate(lt.iterator(get3(lt.getElement(lista_listas_eventos))), headers=titulos, tablefmt="grid")}
        lt.addFirst(lista_retorno, dic)
    return lista_retorno, contador"""

def req_5(earthquakes, min_depth, min_nst):
    depth_arbol = earthquakes["depth"]
    max_depth = om.maxKey(depth_arbol)
    keys = om.keys(depth_arbol, min_depth, max_depth)  
    answer = lt.newList("ARRAY_LIST")

    for depth_key in lt.iterator(keys):        
        element_depth = om.get(depth_arbol, depth_key)
        value_element = element_depth["value"]
        elements = value_element["elements"]
        for element in elements:
            nst = element["nst"]
            if nst == "Unknown":
                nst = 0
            if nst >= min_nst:
                lt.addLast(answer, element)
    final = lt.newList("ARRAY_LIST")
    for data in lt.iterator(answer):
        keys = data.keys()
        table = tabulate([data.values()], headers=keys, tablefmt="grid")

        dic = {"time": data["time"],
               "events" :1,
               "details" : table}
        lt.addLast(final, dic)
    return final 


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass

# Funciones de ordenamiento


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    pass


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass

    
def cmpDates(date1, date2):
    """
    Compara dos fechas
    """
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1
    
def cmpMag(mag1, mag2):
    """
    Compara dos fechas
    """
    if (mag1 == mag2):
        return 0
    elif (mag1 > mag2):
        return 1
    else:
        return -1
    
def cmpDepth(depth1, depth2):
    """
    Compara dos fechas
    """
    if (depth1 == depth2):
        return 0
    elif (depth1 > depth2):
        return 1
    else:
        return -1
    
def cmpNst(nst1, nst2):
    
    if nst1 == "Unknown":
        nst1 = 0
    if nst2 == "Unknown":
        nst2 = 0
        
    if (nst1 == nst2):
        return 0
    elif (nst1 > nst2):
        return 1
    else:
        return -1
    
def get5(lista):
    sublist = lt.newList("ARRAY_LIST")
    for x in range(0,5):
        element = lt.getElement(lista, x)
        lt.addLast(sublist, element)
    for x in range((lt.size(lista)-5),(lt.size(lista))):
        element = lt.getElement(lista, x)
        lt.addLast(sublist, element)
    return sublist 

def get3(lista):
    if lt.size(lista) > 6:
        sublist = lt.newList("ARRAY_LIST")
        for x in range(0,3):
            element = lt.getElement(lista, x)
            lt.addLast(sublist, element)
        for x in range((lt.size(lista)-3),(lt.size(lista))):
            element = lt.getElement(lista, x)
            lt.addLast(sublist, element)
    else:
        sublist = lista
    return sublist 

def get3_normal(lista):
    if len(lista) > 6:
        sublist = lt.newList("ARRAY_LIST")
        primeros3 = lista[:3]
        lt.addLast(sublist, primeros3)
        ultimos3 = lista[-3:]
        lt.addLast(sublist, ultimos3)
    else:
        sublist = lista
    return sublist 


def mag(earthquakes):
    return earthquakes["mag"]