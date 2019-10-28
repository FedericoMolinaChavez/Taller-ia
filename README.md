"# Taller-ia" 
En este repositorio se puede encontrar el codigo utilizado para el taller dictado el 31 de Octubre en la Pontificia Universidad Javeriana.

Como utilizar el repositorio, en la carpeta de ejemplos pueden encontrar ejemplos completos pero para una guía básica.

    Reglas del lenguaje:
    
    declaración de capaz neuronales:
        - tipo ( especificaciones ) cantidad . => especificaciones = ( numCell 3 activation softmax drop 0.1)
        - tipo (especificaciones) -> defecto 1
        - tipo () cantidad -> inferir especificaciones.
        - 
    declaración de conjunto de datos:
        - conjunto(dirArchivo)
    Para poder procesar los datos es necesario tener una función en python que se encargue de pre procesar los datos para ser entregados a la red y que retorne como resultado los conjuntos de test, validación y prueba separados en x y y.
    
    declaración algoritmo de optim:
        - optim nombre ( lr )
    declaración algoritmo de loss:
        - loss nombre
    agregar variables globales de entrenamiento:
        - global (var1, var2, ...)
            types: batch size, epochs, drop, r_drop

En la carpeta de compiler se puede encontrar un archivo de ejemplo.
