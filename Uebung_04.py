import geopandas as gpd
import pandas as pd

#pd.set_option('display.max_rows', None, 'display.max_columns', None)

file_path = "data/ne_10m_admin_0_countries/ne_10m_admin_0_countries.shp"

data = gpd.read_file(file_path)
#print(type(data))
#print(data.head(5))
#test=print(data[data["SOVEREIGNT"] == "Germany"])
#print(type(test))
#print(data[data["SOVEREIGNT"] == "Germany"]["POP_EST"])
#print(data[data["SOVEREIGNT"] == "Germany"]["NAME"])


index = data.index[data["NAME"] == "Germany"].tolist()

neighbors = data[data.geometry.touches(data.loc[int(index[0])]['geometry'])].NAME.tolist() 

for i in neighbors:
    print(i)
    index_nachbar_nachbar = data.index[data["NAME"] == i].tolist()
    nachbar_nachbar = data[data.geometry.touches(data.loc[int(index_nachbar_nachbar[0])]['geometry'])].NAME.tolist() 
    print(index_nachbar_nachbar)
    print(nachbar_nachbar)
    #nachbar_nachbar=data[data["SOVEREIGNT"] == i]
    #print(nachbar_nachbar)
    
print(neighbors)
#neighbors = data[data["SOVEREIGNT"] == "Germany"]["NEIGHBORS"]
#print(neighbors)