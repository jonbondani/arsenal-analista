# Validación de la entrega

Fecha: 21-10-2026. Estos controles pertenecen al paquete documental y a sus ejemplos. **No son reproducciones del laboratorio FreeFloat.**

## Ejemplos ejecutados

Entorno de comprobación: Python **3.12.14**, biblioteca estándar. La utilidad declara como mínimo Python 3.10; no se ha ejecutado aquí en todas las versiones o sistemas operativos compatibles.

| Comprobación | Resultado real |
|---|---|
| Demostración de endianness | `78563412`, conversión de ida y vuelta correcta |
| Comparación sintética sin alinear | Diferencia detectada |
| Comparación sintética alineada | Coincidencia detectada |
| Diferencia introducida en los ejemplos | Índice 3 desde cero, código de salida 1 |
| Comparación del mismo archivo | Coincidencia, código de salida 0 |
| Hash de E02 | Coincide con SHA-256 calculado independientemente |
| Archivo truncado | Diferencia de longitud detectada en el índice 3 |
| Formato hexadecimal inválido | Rechazado, código de salida 2 |
| Archivo hexadecimal superior al límite | Rechazado, código de salida 2 |

Las cuatro órdenes del tutorial y su salida real se conservan en [salida-comprobada.json](salida-comprobada.json). Los controles de truncamiento, formato y tamaño usaron archivos temporales y no añadieron datos del laboratorio al paquete.

## Integridad y revisión documental

- Las seis capturas coinciden byte a byte, mediante su identidad de blob Git, con los archivos de las rutas y el commit registrados en el [manifiesto](../evidencias/manifiesto.json).
- Se revisaron visualmente las seis capturas seleccionadas.
- Se comprobaron destinos de enlaces locales e imágenes y equilibrio de bloques de código Markdown.
- El paquete incluye tres diagramas Mermaid. Se revisó su estructura textual; el renderizado efectivo en la versión de Mermaid de GitHub queda para la revisión de publicación. No se instaló un renderizador adicional.
- Se generó [SHA256SUMS](../SHA256SUMS.txt) para todos los demás archivos de la carpeta. El manifiesto de hashes no se incluye a sí mismo.
- Se comprobó la integridad del ZIP y la correspondencia de sus archivos con la carpeta entregada.

Las comprobaciones no certifican ausencia universal de secretos: el propietario debe revisar el contexto de publicación y los derechos del material. No se ejecutó un escáner de vulnerabilidades, un exploit ni una sesión de depuración.

## Pendiente externo

Publicar tras autorización, comprobar accesibilidad pública, renderizar en GitHub y comunicar la URL docente. La preparación local no completa esos pasos.
