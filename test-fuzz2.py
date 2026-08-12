#ejercicio para comprar dos cadenas con fuzz.ratio
#Compara dos textos exactamente iguales.
#La función ratio() calcula un porcentaje de similitud entre ambas cadenas.
#100 = completamente iguales y 0 = totalmente diferentes.

from thefuzz import fuzz
print (fuzz.ratio("Hola mundo", "Hola mundo"))


#Comparar palabras con errores ortográficos
print (fuzz.ratio("Manzana", "Mnzana"))