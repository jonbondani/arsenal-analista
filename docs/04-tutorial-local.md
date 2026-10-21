# Tutorial local con Python

[Volver al índice](../README.md)

Estos ejercicios trabajan el orden de bytes, la comparación de archivos y la posición desde la que se empieza a leer una secuencia. Usan datos sintéticos y se ejecutan en local, sin instalar FreeFloat.

Necesitas Python 3.10 o posterior. Ejecuta los comandos desde la raíz del repositorio. En Windows puedes sustituir `python3` por `py -3`. Las salidas comprobadas están en [validación local](../ejemplos/VALIDACION.md).

## Leer la captura del patrón

Abre [E02](../evidencias/capturas/E02-offset-246.png). La imagen contiene la orden `pattern_offset`, el valor `41326941` y la posición `246`.

Para repetir la prueba hacen falta también el archivo del patrón transmitido, el origen desde el que se cuenta el offset y su relación con la sesión. Anota ambos grupos por separado: datos disponibles e información necesaria para reproducirlos.

## Comprobar el orden de bytes

```console
python3 herramientas/auditoria_local.py demo
```

La demostración usa el entero arbitrario `0x12345678`. Al representarlo como cuatro bytes little-endian aparece `78563412`. La conversión inversa recupera el mismo entero y el campo `ida_vuelta_correcta` devuelve `true`.

El número es un ejemplo y no corresponde a una dirección del laboratorio. La conversión se hace con `struct` para evitar invertir los bytes a mano.

La misma demostración añade dos bytes al principio de una referencia. Por eso `coincide_inicio_cero` devuelve `false` y `coincide_inicio_dos` devuelve `true`: la secuencia está intacta, pero empieza dos posiciones después.

## Comparar dos referencias

Los archivos de ejemplo contienen ocho bytes cada uno. El cuarto byte se cambió a propósito, así que la primera diferencia aparece en el índice 3, contando desde cero.

```console
python3 herramientas/auditoria_local.py compare ejemplos/referencia.hex ejemplos/observado.hex
```

La salida devuelve `coinciden: false`, longitudes de 8 bytes y `primera_diferencia: 3`. El programa termina con código 1 para indicar que ha encontrado una diferencia.

A continuación compara un archivo consigo mismo:

```console
python3 herramientas/auditoria_local.py compare ejemplos/referencia.hex ejemplos/referencia.hex
```

En este caso la coincidencia es completa y el código de salida es 0. Los errores de lectura, formato o tamaño devuelven 2.

La diferencia de estos ejemplos es artificial. No aporta información sobre los bad characters de FreeFloat; sirve para aprender a interpretar una comparación y distinguir una diferencia de un error del programa.

## Revisar la integridad de una captura

```console
python3 herramientas/auditoria_local.py hash evidencias/capturas/E02-offset-246.png
```

Compara el SHA-256 obtenido con el [manifiesto](../evidencias/manifiesto.json) o con [SHA256SUMS](../SHA256SUMS.txt). La utilidad muestra nombre, tamaño y hash del archivo.

Si los hashes coinciden, la copia corresponde a los mismos bytes registrados. La fecha y el contexto de la captura se guardan aparte; el hash solo identifica el archivo.

## Interpretar la comparación de mona

En [E05](../evidencias/capturas/E05-comparacion.png) se observa una referencia de 253 bytes, una dirección de comparación, tres exclusiones y el resultado `Unmodified`.

El resultado respalda que los bytes de esa referencia coinciden en la ubicación utilizada. Los valores excluidos no se han evaluado mediante esa comparación. Para otra sesión hay que localizar de nuevo el inicio de la tabla antes de comparar.

Es lo que ocurre en el ejemplo del prefijo: la referencia está bien, pero la comparación falla si se empieza a leer desde otra posición.

## Guardar los resultados

En la [plantilla de informe](../plantillas/informe.md) se pueden guardar los comandos y sus resultados. Para estos ejercicios basta con identificar la revisión de E02 y E05 y las pruebas sintéticas locales.

En una futura sesión con la VM original, convendría empezar por guardar el inventario, la entrada exacta y los registros del mismo instante. Esa información permitiría relacionar el resultado de mona con la ruta de código y con el estado del proceso.
