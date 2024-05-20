import ausgabe

# Eingabeaufforderung
print(f'Bitte ein Land eingeben (Deutschsprachig):')

# Eingabe des Landes (Deutschsprachig)
eingabe = input()
print(f'Die folgenden Berechnungen werden für das Land {eingabe} durchgeführt!')

ausgabe.get_nachbar_nachbar("data/ne_10m_admin_0_countries/ne_10m_admin_0_countries.shp", eingabe)