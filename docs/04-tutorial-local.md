# Ejemplos locales con Python

[Volver al índice](../README.md)

Los ejemplos usan datos sintéticos para comprobar el orden de bytes, la comparación de archivos y la posición inicial de una secuencia. Se ejecutan en local con Python 3.10 o posterior, desde la raíz del repo. En Windows se puede usar `py -3` en lugar de `python3`.

## Orden de bytes

```console
python3 herramientas/auditoria_local.py demo
```

La demostración convierte `0x12345678` a cuatro bytes little-endian. La salida es `78563412`. Al hacer la conversión inversa se recupera el mismo entero y `ida_vuelta_correcta` devuelve `true`.

El número es un ejemplo, no una dirección del caso. La conversión se hace con `struct`, como se explica en la [cheatsheet de Python](../cheatsheets/python.md).

## Inicio de una secuencia

La misma demostración añade dos bytes al principio de una referencia:

- `coincide_inicio_cero` devuelve `false` al comparar desde el principio.
- `coincide_inicio_dos` devuelve `true` al saltar el prefijo.

Los bytes de la referencia no han cambiado. La diferencia viene de la posición desde la que se leen. Es el mismo tipo de error que puede aparecer si se asume que una tabla comienza justo en ESP.

## Comparar dos archivos

Los archivos de ejemplo tienen ocho bytes. Se ha cambiado a propósito el cuarto, que ocupa el índice 3 contando desde cero.

```console
python3 herramientas/auditoria_local.py compare ejemplos/referencia.hex ejemplos/observado.hex
```

La salida indica `coinciden: false`, longitudes de 8 y `primera_diferencia: 3`. El código de salida es 1 porque se ha encontrado una diferencia.

Para comprobar una coincidencia completa:

```console
python3 herramientas/auditoria_local.py compare ejemplos/referencia.hex ejemplos/referencia.hex
```

Al comparar el archivo consigo mismo, `coinciden` devuelve `true` y el código de salida es 0. Los errores de lectura, formato o tamaño devuelven 2.

Esta diferencia es artificial y no forma parte de la lista de bad characters de FreeFloat.

## Calcular el hash de una captura

```console
python3 herramientas/auditoria_local.py hash evidencias/capturas/E02-offset-246.png
```

El programa muestra nombre, tamaño y SHA-256. Se puede comparar con el [manifiesto de capturas](../evidencias/manifiesto.json) o con [SHA256SUMS](../SHA256SUMS.txt).

El hash identifica los bytes del archivo. La fecha y el contexto de la captura se registran aparte.

## Revisar la salida de mona

En [E02](../evidencias/capturas/E02-offset-246.png) aparecen `pattern_offset`, el valor `41326941` y la posición `246`. Para repetir la consulta vinculada a una ejecución hacen falta el patrón transmitido y el origen del offset.

En [E05](../evidencias/capturas/E05-comparacion.png) se compara una referencia de 253 bytes y el resultado es `Unmodified`. Los valores excluidos no están evaluados por esa comparación. El inicio debe localizarse de nuevo en otra sesión, igual que se ajusta el prefijo en el ejemplo local.

Las [salidas comprobadas](../ejemplos/VALIDACION.md) recogen los resultados de estos comandos. La [plantilla de informe](../plantillas/informe.md) sirve para guardar una ejecución propia, separada de las pruebas del servidor.
