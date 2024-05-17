import geopandas as gpd
import functions

def get_nachbar_nachbar(file, Start_Land):
    
    data = gpd.read_file(file)
    
    nachbarn = functions.get_nachbarn(data, Start_Land)
    
    functions.get_area(data, Start_Land)
    
    list_all = []
    
    for i in nachbarn:
        list_nachbarn = functions.get_nachbarn(data, i)       
        for y in list_nachbarn:
            list_all.append(y)
    
    list_all = set(list_all)
    list_without_start_land = list_all
    list_without_start_land.remove(Start_Land)
        
     
    area_gesamt = functions.get_area_gesamt(data, list_without_start_land)
    einwohner_gesamt = functions.get_population_gesamt(data, list_without_start_land) 
    bevoelkerungsichte = einwohner_gesamt / area_gesamt
    
    print(f'Anzahl der Nachbarländer der Nachbarländer: {len(list_all)}')
    print("-" * 70)
    print(f'Namen der Nachbarländer der Nachbarländer:')
    for i in list_all:
        print(f'-   {i}')
    print("-" * 70)
    print(f'Die nachfolgenden Angaben sind alle exklusive des eingegebenen Landes')
    print(f'Gesamtfläche der Nachbarländer der Nachbarländer: {area_gesamt:,.3f} km\u00b2')
    print("-" * 70)
    print(f'Gesamtbevölkerung der Nachbarländer der Nachbarländer: {einwohner_gesamt:,}')
    print("-" * 70)
    print(f'Bevölkerungsdichte der Nachbarländer der Nachbarländer: {bevoelkerungsichte:,.3f} P / km\u00b2')

if __name__ == "__main__":
    get_nachbar_nachbar("data/ne_10m_admin_0_countries/ne_10m_admin_0_countries.shp", "Deutschland")
    #get_population("Deutschland")