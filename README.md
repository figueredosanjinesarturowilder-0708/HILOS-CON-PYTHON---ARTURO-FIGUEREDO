Práctica de Hilos en Python

Interpretación de los resultados por trabajador

En este programa trabajamos con cuatro trabajadores llamados LEON, TONY, RODNEY y EMILIANO. Cada uno se encarga de procesar 6 documentos, haciendo un total de 24 documentos.

Utilizamos random para que los documentos se repartan de diferente manera cada vez que ejecutamos el programa. También usamos Lock para evitar problemas cuando los trabajadores guardan sus resultados.
Al terminar, el programa muestra los documentos que hizo cada trabajador y comprueba que los 24 documentos se procesaron sin repetir ninguno.

Preguntas :

1. ¿Por qué queue.Queue es apropiada para compartir trabajos?

Porque permite guardar todos los documentos en una misma cola y que cada trabajador vaya sacando uno a la vez. Así evitamos que dos trabajadores hagan el mismo documento y logramos que cada uno complete sus 6 documentos.

2. ¿Qué protege Lock y qué pasaría si se actualizara el resumen sin él?

Lock sirve para que los trabajadores no cambien los resultados al mismo tiempo. En nuestro programa lo utilizamos cuando guardamos los documentos que terminó cada trabajador. Si no lo utilizáramos, podrían existir problemas cuando varios trabajadores intenten actualizar los resultados al mismo tiempo.

3. ¿Qué cambiarías si cada documento tuviera que guardarse en un archivo real?

Cambiaría la parte donde el programa simula el trabajo para que realmente guarde los documentos en archivos.
También pondría un nombre diferente a cada archivo para que no se mezclen ni se reemplacen. Además, agregaría una forma de avisar si ocurre algún error al guardar.
