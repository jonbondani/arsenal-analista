# Comparativa de herramientas

[Volver al índice](../README.md)

La elección de herramientas depende de la muestra, la arquitectura y el análisis. Aquí se compara su uso en el caso con las funciones descritas en la documentación oficial. No se han medido tiempos ni rendimiento.

## Herramientas utilizadas en el laboratorio

| Herramienta | Uso principal | Ventaja en el caso | Limitación |
| :--- | :--- | :--- | :--- |
| IDA Free | Estudiar funciones, cadenas y referencias | Relaciona el protocolo con ramas y operaciones del binario | La edición, licencia y decompilación condicionan el uso |
| Immunity Debugger | Examinar el estado de un proceso x86 | Permite leer registros, pila y memoria como en las capturas | El entorno histórico necesita versiones compatibles |
| mona clásico | Consultar patrones y comparar memoria | Reduce trabajo repetitivo y deja una salida concreta | Depende de la referencia y del host; su repositorio está archivado |
| Python | Comprobar representaciones y archivos | Facilita tareas pequeñas y revisables | El resultado depende de los datos y de la lógica del script |

IDA, Immunity y mona están documentados en el laboratorio original. La utilidad Python incluida tiene sus propias [comprobaciones locales](../ejemplos/VALIDACION.md).

## Alternativas para otros análisis

**Ghidra** permite una segunda lectura estática con desensamblado y decompilación. Puede ayudar a contrastar una función, aunque dos reconstrucciones distintas siguen necesitando una revisión del ensamblador. No se ha utilizado para repetir este caso.

**x32dbg y x64dbg** ofrecen otra opción de depuración de usuario en Windows. La arquitectura del proceso orienta la elección. Los plugins y los atajos del flujo de Immunity necesitan revisarse al cambiar de entorno.

**WinDbg con mona3** es una opción para evaluar en un laboratorio nuevo. El proyecto clásico de mona remite a mona3, cuya documentación contempla hosts como WinDbg y WinDbgX. La compatibilidad de instalación y comandos debe comprobarse antes de trasladar las instrucciones del caso.

Las capacidades se pueden consultar en las páginas oficiales de [IDA Free](https://hex-rays.com/ida-free), [Ghidra](https://github.com/NationalSecurityAgency/ghidra), [x64dbg](https://x64dbg.com/), [mona](https://github.com/corelan/mona) y [mona3](https://github.com/corelan/mona3).

## Elegir según el trabajo

Para seguir las capturas se mantienen las herramientas del laboratorio original. Un cambio de depurador o plugin necesita sus propias comprobaciones.

Para un análisis nuevo conviene elegir primero la arquitectura y el objetivo. Un proceso x64 necesita revisar las herramientas y los supuestos sobre registros y tamaños. Los valores de EIP y el offset del caso x86 no se trasladan directamente.

Si el binario es confidencial, hay que revisar el tratamiento de datos y las condiciones de licencia. La página de IDA Free describe un decompilador en la nube y restricciones de uso comercial, por lo que esas condiciones importan antes de cargar una muestra.

## Instalación y mantenimiento

Al preparar el entorno también hay que contar con cuentas, licencias, intérpretes, plugins y VM. Sus versiones y dependencias deben quedar anotadas para poder volver a montarlo.

Para mantener un caso histórico suele ser útil conservar las versiones con las que se generaron las evidencias. Si se prepara un entorno nuevo, una prueba pequeña de compatibilidad ayuda a decidir si conviene actualizarlo.

Esa prueba puede incluir la apertura de una muestra autorizada, la confirmación de su arquitectura, la lectura de registros y memoria y una comparación local con referencia conocida. Hasta completar esos pasos, la migración debe presentarse como una opción por evaluar.
