import geopandas as gpd

def get_index(data, Land):
    
    # Index des eingebenen Landes (deutschsprachiger Name des Landes erfordert)
    index = data.index[data["NAME_DE"] == Land].tolist()
    
    # Umwandlung Index in Integer
    index = int(index[0])
    
    return index

def get_nachbarn(data, Land):
    
    # Index des Landes
    index = get_index(data, Land)
    
    # Ermittlung der Nachbarn des Landes mit touches Funtion
    nachbarn = data[data.geometry.touches(data.loc[index]['geometry'])].NAME_DE.tolist()
    
    return nachbarn

def get_nachbarn_nachbarn(data, nachbarn):
    
    list_all = []
    
    # Liste mit den Nchbarländern der Nachbarländer
    for i in nachbarn:
        list_nachbarn = get_nachbarn(data, i)       
        for y in list_nachbarn:
            list_all.append(y)
            
    return list_all

def get_population(data, Land):
    
    # Index des Landes
    index = get_index(data, Land)
    
    # Auslesen der Einwohnerzahl aus der Spalte POP_EST
    einwohner = data.loc[index].POP_EST.tolist()  
    
    return einwohner

def get_population_gesamt(data, list_without_start_land):
    
    einwohner_gesamt = 0 
    
    # Berechnung der gesamt Einwohner für die Länder außer dem Startland
    for i in list_without_start_land:
        
        einwohner = get_population(data, i)
        
        einwohner_gesamt = einwohner_gesamt + einwohner
        
    return einwohner_gesamt

def get_area(data, Land):
    
    # Index des Landes
    index = get_index(data, Land)
    
    # Umprojezierung
    # Funktion Area kann nicht mit Lat/Long rechnen
    data = data.to_crs({'proj':'cea'})
    
    # Ermittlung der Fläche des Landes
    area = data.loc[index]['geometry'].area / 10**6
    
    return area

def get_area_gesamt(data, list_without_start_land):
    
    area_gesamt = 0
    
    # Berechnung der gesamt Fläche für die Länder außer dem Startland
    for i in list_without_start_land:
        
        area = get_area(data, i)
        
        area_gesamt = area_gesamt + area
        
    return area_gesamt

def export_geopackage():
    
    pass