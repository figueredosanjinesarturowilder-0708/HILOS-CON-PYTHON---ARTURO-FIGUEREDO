
import threading
import queue
import time
import random

trabajos = queue.Queue()
resultados = {}
lock = threading.Lock()

documentos = list(range(1, 25))
random.shuffle(documentos)

for doc_id in documentos:
    trabajos.put((doc_id, random.randint(1, 5)))

def trabajador(nombre):
    for i in range(6):
        doc_id, tamano = trabajos.get()

        print(nombre, "procesando documento", doc_id)

        time.sleep(tamano * 0.1)

        with lock:
            resultados[nombre].append(doc_id)
            print(nombre, "termino documento", doc_id)

        trabajos.task_done()

nombres = ["LEON", "TONY", "RODNEY", "EMILIANO"]
hilos = []

for nombre in nombres:
    resultados[nombre] = []

    hilo = threading.Thread(
        target=trabajador,
        args=(nombre,)
    )

    hilos.append(hilo)

for hilo in hilos:
    hilo.start()

for hilo in hilos:
    hilo.join()

print("\n= RESULTADOS FINALES =")

total = 0
todos_documentos = []

for nombre in nombres:
    print("\nTrabajador:", nombre)

    for documento in resultados[nombre]:
        print("Documento procesado:", documento)
        todos_documentos.append(documento)

    cantidad = len(resultados[nombre])
    print("Total de", nombre, ":", cantidad)

    total += cantidad

print("TOTAL DE DOCUMENTOS:", total)
print("DOCUMENTOS UNICOS:", len(set(todos_documentos)))

if total == 24 and len(set(todos_documentos)) == 24:
    print("CORRECTO: 24 documentos sin repetir")
else:
    print("ERROR: Documentos repetidos o faltantes")

print("Los cuatro trabajadores finalizaron")

