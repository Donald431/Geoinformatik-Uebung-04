import geopandas as gpd
import pandas as pd

data = gpd.read_file("data/ne_10m_admin_0_countries/ne_10m_admin_0_countries.shp")
 

def get_nachbarn(Land):
    
    # Index des eingebenen Landes (deutschsprachiger Name des Landes erfordert)
    index = data.index[data["NAME_DE"] == Land].tolist()
    
    # Ermittlung der Nachbarn des Landes mit touches Funtion
    nachbarn = data[data.geometry.touches(data.loc[int(index[0])]['geometry'])].NAME_DE.tolist()
    
    return nachbarn
        
    
def get_nachbar_nachbar(Start_Land):
    
    nachbarn = get_nachbarn(Start_Land)
    
    list_all = []
    
    for i in nachbarn:
        list_nachbarn = get_nachbarn(i)       
        for y in list_nachbarn:
            list_all.append(y)
    
    list_all = set(list_all)
    # Eingegebens Land entfernen
    #list_all.remove(Start_Land)
    # Anzahl der Nachbarländer
    print(len(list_all))
    # Namen der Nachbarländer
    print(list_all)
        
#print(type(data))
#print(data.head(5))
#test=print(data[data["SOVEREIGNT"] == "Germany"])
#print(type(test))
#print(data[data["SOVEREIGNT"] == "Germany"]["POP_EST"])
#print(data[data["SOVEREIGNT"] == "Germany"]["NAME"])


if __name__ == "__main__":
    get_nachbar_nachbar("Deutschland")