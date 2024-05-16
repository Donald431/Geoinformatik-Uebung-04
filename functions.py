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

def get_population(data, Land):
    
    # Index des Landes
    index = get_index(data, Land)
    
    # Auslesen der Einwohnerzahl aus der Spalte POP_EST
    einwohner = data.loc[index].POP_EST.tolist()  
    
    return einwohner

def get_area(data, Land):
    
    pass

def export_geopackage():
    
    pass