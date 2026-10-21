# Comprobaciones locales

Las siguientes comprobaciones corresponden a los archivos y ejercicios del recurso. No son una reproducción del laboratorio FreeFloat.

## Ejemplos de Python

Los ejemplos se ejecutaron el 21 de octubre de 2026 con Python 3.12.14 y la biblioteca estándar. La utilidad utiliza sintaxis compatible con Python 3.10 o posterior, aunque no se ha ejecutado en todas las versiones y sistemas operativos.

| Comprobación | Resultado |
| :--- | :--- |
| Entero sintético a little-endian | `78563412` |
| Conversión inversa | Recupera el entero original |
| Referencia con prefijo sin ajustar | Detecta diferencia |
| Referencia después de ajustar el inicio | Detecta coincidencia |
| Archivos de ejemplo distintos | Primera diferencia en el índice 3; código 1 |
| Archivo comparado consigo mismo | Coincidencia; código 0 |
| SHA-256 de E02 | Coincide con un cálculo independiente |
| Archivo truncado | Diferencia detectada en el índice 3 |
| Hexadecimal inválido | Rechazado con código 2 |
| Archivo superior al límite | Rechazado con código 2 |

Las cuatro órdenes del tutorial y sus salidas están en [salida-comprobada.json](salida-comprobada.json). Las pruebas de truncamiento, formato y tamaño utilizaron archivos temporales.

## Documentación y capturas

Las seis imágenes se revisaron visualmente y su identidad de blob Git coincide con las rutas del commit del [manifiesto](../evidencias/manifiesto.json). Los nombres locales cambian, pero sus bytes se conservaron.

La revisión de estilo abarca los 23 documentos Markdown. Se comprobaron enlaces locales, imágenes y cierre de bloques de código. Los tres diagramas Mermaid conservan su estructura; su renderizado en GitHub forma parte de la revisión posterior a la publicación.

## Integridad del paquete

[SHA256SUMS](../SHA256SUMS.txt) contiene los hashes de los demás archivos de la carpeta. No se incluye a sí mismo. Después de actualizar la documentación se regeneraron los hashes y el ZIP, y se comprobó que sus archivos corresponden al contenido de la carpeta.

## Publicación

El acceso público, el aspecto de los diagramas en GitHub y el envío de la URL se comprueban al publicar manualmente el repositorio. Estas comprobaciones locales no indican que esos pasos ya se hayan realizado.
