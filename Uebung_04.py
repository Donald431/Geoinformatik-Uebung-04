import geopandas as gpd
import functions

def get_nachbar_nachbar(file, Start_Land):
    
    data = gpd.read_file(file)
    
    nachbarn = functions.get_nachbarn(data, Start_Land)
    
    list_all = []
    
    for i in nachbarn:
        list_nachbarn = functions.get_nachbarn(data, i)       
        for y in list_nachbarn:
            list_all.append(y)
    
    list_all = set(list_all)
    list_without_start_land = list_all
    list_without_start_land.remove(Start_Land)
    
    einwohner_gesamt = 0
    
    for i in list_without_start_land:
        
        einwohner = functions.get_population(data, i)
        
        einwohner_gesamt = einwohner_gesamt + einwohner
        print(einwohner_gesamt)
        
    # Eingegebens Land entfernen
    #list_all.remove(Start_Land)
    # Anzahl der Nachbarländer
    #print(len(list_all))
    # Namen der Nachbarländer
    #print(list_all)

if __name__ == "__main__":
    get_nachbar_nachbar("data/ne_10m_admin_0_countries/ne_10m_admin_0_countries.shp", "Deutschland")
    #get_population("Deutschland")