# Comparativa de herramientas

[Volver al índice](../README.md)

## Herramientas del caso

| Herramienta | Uso | Ventaja | Limitación |
| :--- | :--- | :--- | :--- |
| IDA Free | Seguir funciones, cadenas y referencias | Relaciona las entradas FTP con el código | Edición, licencia y decompilación condicionan el uso |
| Immunity Debugger | Revisar el proceso x86 detenido | Muestra registros, pila y memoria | Necesita un entorno compatible con el depurador y sus plugins |
| mona clásico | Consultar patrones y comparar bytes | Automatiza búsquedas y comparaciones | Depende de la referencia y del host; su repo está archivado |
| Python | Convertir, comparar y calcular hashes | Comprobaciones pequeñas que se pueden repetir | No conoce el contexto de los archivos que recibe |

IDA, Immunity y mona aparecen en las pruebas documentadas del laboratorio. Los ejemplos locales de Python tienen sus [resultados](../ejemplos/VALIDACION.md) aparte.

## Alternativas

**Ghidra** sirve para contrastar el análisis estático con otro desensamblador y decompilador. Si las reconstrucciones difieren, hay que volver a las instrucciones y revisar los tipos; no basta con elegir la salida más legible.

**x32dbg y x64dbg** son opciones de depuración de usuario en Windows. Se eligen según la arquitectura del proceso. Los plugins, atajos y comandos del flujo de Immunity necesitan revisarse al cambiar de entorno.

**WinDbg con mona3** es otra opción para un laboratorio nuevo. El repo clásico remite a mona3, que contempla hosts como WinDbg y WinDbgX. La instalación y los comandos se deben comprobar antes de trasladar los pasos del caso.

Estas alternativas se comparan a partir de su documentación. No se ha repetido el laboratorio con ellas ni se han medido tiempos o rendimiento.

## Arquitectura y condiciones de uso

Para estudiar un proceso x64 hay que revisar herramientas, registros y tamaños. EIP y el offset del caso x86 no se trasladan directamente.

Con un binario confidencial también importan las condiciones del decompilador. La página de IDA Free describe decompilación en la nube y restricciones de uso comercial. Hay que revisar esas condiciones antes de cargar una muestra.

## Cambiar de entorno

Guarda versiones, intérpretes y dependencias para poder volver a montar el laboratorio. Mantener un caso antiguo puede requerir conservar su entorno original; actualizarlo necesita una prueba de compatibilidad.

Esa prueba debería confirmar la apertura de una muestra autorizada, su arquitectura, la lectura de registros y memoria y una comparación con referencia conocida. Hasta hacerlo, el cambio de herramienta queda como una opción por evaluar.

Fuentes: [IDA Free](https://hex-rays.com/ida-free), [Ghidra](https://github.com/NationalSecurityAgency/ghidra), [x64dbg](https://x64dbg.com/), [mona](https://github.com/corelan/mona) y [mona3](https://github.com/corelan/mona3).
