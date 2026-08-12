# Check the similarity score
from thefuzz import fuzz
from os import name

#Definimos 2 variables para comparar la similitud entre dos cadenas
full_name = "Dr. Jane Elizabeth Smith"
full_name_reordered = "Smith, Jane Elizabeth Dr."

# la función fuzz.token_sort_ratio() ayuda a comparar la similitud entre los dos nombres 
# El orden no importa para token sort ratio
print(f"Token sort ratio similarity score: {fuzz.token_sort_ratio(full_name_reordered, full_name)}")

# la función fuzz.partial_ratio() para comparar la similitud entre los dos nombres. Esta función compara las dos cadenas basándose en la subcadena coincidente contigua más larga.
# El orden importa para la proporción parcial
print(f"Partial ratio similarity score: {fuzz.partial_ratio(full_name, full_name_reordered)}")

# la función fuzz.ratio() para comparar la similitud entre los dos nombres. Esta función compara las dos cadenas basándose en el número de caracteres coincidentes.
# El orden no afectará la proporción simple si las cadenas no coinciden.
print(f"Simple ratio similarity score: {fuzz.ratio(name, full_name)}")

