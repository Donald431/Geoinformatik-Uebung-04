import ausgabe
import sys

# Eingabeaufforderung
print(f'Bitte ein Land eingeben (Deutschsprachig):')

# Eingabe wird so lange wiederholt nur alphabetische Zeichen eingegeben werden
while True:
    
    # Eingabe des Landes (Deutschsprachig)
    eingabe = input()

    # Prüfung ob Eingabe nur alphabetische Zeichen enthält
    # Wenn nicht erneute Eingabe notwendig
    if eingabe.isalpha() == False:
        print(f'Die Eingabe enthält nicht alphabetische Zeichen. \nErneute Eingabe des Landes erforderlich:')
    else:
        break
    
print(f'\nDie folgenden Berechnungen werden für das Land {eingabe} durchgeführt!')


ausgabe.get_nachbar_nachbar("data/ne_10m_admin_0_countries/ne_10m_admin_0_countries.shp", eingabe)