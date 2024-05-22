import ausgabe
import geopandas as gpd
import functions
import sys


# Einlesen der Daten
try:
    print(f'Daten werden geladen ...')
    data = gpd.read_file("data/ne_10m_admin_0_countries/ne_10m_admin_0_countries.shp")
except Exception as error:
    print(f'Daten konnten nicht eingelesen werden.')
    print(error)
    # Beenden des Programms wenn Daten nicht geladen werden können
    sys.exit()

# Eingabeaufforderung
print(f'Bitte ein Land eingeben (Deutschsprachig):')

while True:
    
    # Eingabe des Landes (Deutschsprachig)
    eingabe = input()
    
    # Prüfung ob Eingabe nur alphabetische Zeichen enthält
    # Wenn nicht erneute Eingabe notwendig
    if eingabe.isalpha() == False:
        print(f'Die Eingabe enthält nicht alphabetische Zeichen. \nErneute Eingabe des Landes erforderlich:')
        continue 
    # Prüfung ob eingegebens Land wirklich vorhaden ist
    # Wenn nicht wirft Funktion Fehler aus
    try:
        functions.get_index(data, eingabe)
        break
    except:
        print(f'Das eingegebene Land ist nicht vorhanden. \nErneute Eingabe des Landes erforderlich:')

print(f'\nDie folgenden Berechnungen werden für das Land {eingabe} durchgeführt!')
 
# Aufrufen der Hauptfunktion für die Berechnungen und Ausgabe der Daten
ausgabe.get_nachbar_nachbar(data, eingabe)    