
from thefuzz import fuzz
from thefuzz import process
import pandas as pd

# creadomos un dataframe
#Los nombres representan los mismos países, pero están escritos de manera diferente.
dict_1 = {
    "country": ["England", "Scotland", "Wales", "United Kingdom", "Northern Ireland"],
    "population_in_millions": [55.98, 5.45, 3.14, 67.33, 1.89]
}

dict_2 = {
    "country": ["Northern Iland", "Wles", "Scotlnd", "Englnd", "United K."],
    "GDP_per_capita": [24900, 23882, 37460, 45101, 46510.28]
}

#Esto convierte el diccionario en una tabla.
existing_data = pd.DataFrame(dict_1)
exported_data = pd.DataFrame(dict_2)

print(existing_data, exported_data, sep="\n\n")

# Cambia el nombre de las columnas mal escritas
exported_data["country"] = exported_data["country"].apply(
    lambda x: process.extractOne(x, existing_data["country"], 
    scorer=fuzz.partial_ratio)[0]
)


# Intenta unir los dos dataframes en función de la columna "country" y muestra el resultado.
data = pd.merge(existing_data, exported_data, on="country", how="left")
print("\n", data.head())

