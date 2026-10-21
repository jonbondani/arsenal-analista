# Resultados de los ejemplos locales

Pruebas realizadas el 21 de octubre de 2026 con Python 3.12.14 y la biblioteca estándar. Los datos son sintéticos; estos resultados no corresponden a una ejecución de FreeFloat.

| Comprobación | Resultado |
| :--- | :--- |
| Entero a little-endian | `78563412` |
| Conversión inversa | Recupera el entero original |
| Referencia con prefijo sin ajustar | Detecta diferencia |
| Referencia con el inicio ajustado | Detecta coincidencia |
| Archivos distintos | Diferencia en el índice 3; código 1 |
| Archivo comparado consigo mismo | Coincidencia; código 0 |
| SHA-256 de E02 | Coincide con un cálculo independiente |
| Archivo truncado | Diferencia en el índice 3 |
| Hexadecimal inválido | Rechazado con código 2 |
| Archivo superior a 1 MiB de texto | Rechazado con código 2 |

Las cuatro órdenes del [tutorial](../docs/04-tutorial-local.md) y sus salidas están en [salida-comprobada.json](salida-comprobada.json). Las pruebas de truncamiento, formato y tamaño utilizaron archivos temporales.

La utilidad necesita Python 3.10 o posterior. La versión comprobada es la indicada arriba; no se ha probado en todos los sistemas operativos.
