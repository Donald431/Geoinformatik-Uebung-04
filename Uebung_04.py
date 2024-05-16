import geopandas as gpd
import pandas as pd

data = gpd.read_file("data/ne_10m_admin_0_countries/ne_10m_admin_0_countries.shp")

def get_nachbar_nachbar(Start_Land):
    
    nachbarn = get_nachbarn(Start_Land)
    
    list_all = []
    
    for i in nachbarn:
        list_nachbarn = get_nachbarn(i)       
        for y in list_nachbarn:
            list_all.append(y)
    
    list_all = set(list_all)
    list_without_start_land = list_all
    list_without_start_land.remove(Start_Land)
    
    einwohner_gesamt = 0
    
    for i in list_without_start_land:
        
        einwohner = get_population(i)
        
        einwohner_gesamt = einwohner_gesamt + einwohner
        print(einwohner_gesamt)
        
    # Eingegebens Land entfernen
    #list_all.remove(Start_Land)
    # Anzahl der Nachbarländer
    #print(len(list_all))
    # Namen der Nachbarländer
    #print(list_all)

def get_population(Land):
    
    index = get_index(Land)
    
    einwohner = data.loc[index].POP_EST.tolist()  
    
    return einwohner

def get_area(Land):
    
    pass
 
def get_nachbarn(Land):
    
    # Index des eingebenen Landes (deutschsprachiger Name des Landes erfordert)
    index = get_index(Land)
    
    # Ermittlung der Nachbarn des Landes mit touches Funtion
    nachbarn = data[data.geometry.touches(data.loc[index]['geometry'])].NAME_DE.tolist()
    
    return nachbarn

def get_index(Land):
    
    # Index des eingebenen Landes (deutschsprachiger Name des Landes erfordert)
    index = data.index[data["NAME_DE"] == Land].tolist()
    
    index = int(index[0])
    
    return index


if __name__ == "__main__":
    get_nachbar_nachbar("Deutschland")
    #get_population("Deutschland")