import random

def generar_cadenas_markov(texto, longitud_orden):
    cadenas_markov = {}
    palabras = texto.split()

    for i in range(len(palabras)-longitud_orden):
        fragmento = tuple(palabras[i:i+longitud_orden])
        siguiente_palabra = palabras[i+longitud_orden]
        
        if fragmento in cadenas_markov:
            cadenas_markov[fragmento].append(siguiente_palabra)
        else:
            cadenas_markov[fragmento] = [siguiente_palabra]
    
    return cadenas_markov

def generar_texto(cadenas_markov, longitud_texto):
    fragmento_inicial = random.choice(list(cadenas_markov.keys()))
    texto_generado = ' '.join(fragmento_inicial)
    
    for _ in range(longitud_texto):
        if fragmento_inicial in cadenas_markov:
            siguiente_palabra = random.choice(cadenas_markov[fragmento_inicial])
            texto_generado += ' ' + siguiente_palabra
            fragmento_inicial = fragmento_inicial[1:] + (siguiente_palabra,)
        else:
            break
    
    return texto_generado


texto_entrenamiento = "El gato está en el jardín. El perro está en la casa. El gato está en la casa."
longitud_orden = 2
longitud_texto_generado = 20

cadenas_markov = generar_cadenas_markov(texto_entrenamiento, longitud_orden)
texto_generado = generar_texto(cadenas_markov, longitud_texto_generado)

print("Texto generado:", texto_generado)
