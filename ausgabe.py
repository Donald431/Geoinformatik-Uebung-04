import geopandas as gpd
import functions

def get_nachbar_nachbar(file, Start_Land):
    
    data = gpd.read_file(file)
    
    nachbarn = functions.get_nachbarn(data, Start_Land)
    
    list_all = set(functions.get_nachbarn_nachbarn(data, nachbarn))
    list_without_start_land = list_all.copy()
    list_without_start_land.remove(Start_Land)
        
    area_gesamt = functions.get_area_gesamt(data, list_without_start_land)
    einwohner_gesamt = functions.get_population_gesamt(data, list_without_start_land) 
    
    # Wenn Nachbarland des NAchbarland nur das eingebene Land ist, kann keine Bevölkerungsdichte berechnet wer
    # Dann würde durch 0 geteilt werden womit ein Fehler auftritt
    if area_gesamt == 0 and einwohner_gesamt == 0:
        bevoelkerungsichte = 0
    else:
        bevoelkerungsichte = einwohner_gesamt / area_gesamt
    
    print("-" * 70)
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
    
    # Export der Daten in eine .shp Datei
    functions.export_geopackage(data, Start_Land, list_without_start_land)
    print("-" * 70)
    print(f'Export als .shp erfolgreich im Ordner Export erstellt!')
    
    # Plotten der Länder
    functions.plot_countries(data, Start_Land, list_without_start_land)
    print(f'Weltkarte als .png erfolgreich im Ordner Export erstellt!')