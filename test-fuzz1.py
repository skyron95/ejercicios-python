#instalamos la libreria thefuzz
from thefuzz import fuzz
from thefuzz import process

#Lista de nombres registrados
nombres_resgistrados = [
    "Marti Benza",
    "Giani Lopez",
    "Juan Perez",
    "Martin Borgez",
    "Mari Gonzalez",
    "Martu Bensa",     #Variante similar de "Marti Benza"
    "Angie Gonzales",
]

#Nombre a buscar
nombre_ingresado = "Mrti Bnza"

#Buscar los 3 nombre más similares
coincidencias = process.extract(nombre_ingresado, nombres_resgistrados, limit=3)

#Mostrar los resultados (con porcentaje de similitud)
for nombre, puntaje in coincidencias:
    print(f"Coincidencias: {nombre}-- Similitud: {puntaje}%")


from thefuzz import fuzz
fuzz.ratio("Hola mundo", "Hola mundo")

#Comparar palabras con errores ortográficos
fuzz.ratio("Manzana", "Mnzana")