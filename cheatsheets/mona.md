# Cheatsheet de mona

[Índice](../README.md) · [Evidencias](../evidencias/README.md)

Los comandos corresponden a mona clásico. Su [repo](https://github.com/corelan/mona) está archivado y remite a [mona3](https://github.com/corelan/mona3). Si cambia el host o la versión, comprueba los requisitos y la ayuda antes de trasladar estas órdenes.

## Carpeta de trabajo

```text
!mona config -set workingfolder C:\Mona\sesion_revision
```

Utiliza una carpeta por sesión para separar patrones, tablas y resultados. Anota la versión del plugin y la ruta efectiva.

## Patrón local

```text
!mona pattern_create 400
```

Genera el patrón de 400 bytes descrito en el caso. Guarda el archivo y su hash. La relación con una detención necesita también la entrada completa y el contexto de la ejecución.

## Buscar el valor de EIP

```text
!mona pattern_offset 41326941
```

En E02 devuelve la posición 246. El origen es el inicio del patrón consultado. Conserva la salida y comprueba la representación del valor antes de cambiar su orden de bytes.

## Tabla de bytes

```text
!mona bytearray -b "\x00\x0a\x0d"
```

`-b` indica las exclusiones. Con esos tres valores omitidos quedan 253 bytes.

Guarda el motivo de cada exclusión. Puede basarse en el protocolo o en una observación previa, pero excluir un byte no demuestra que haya fallado en esta comparación.

## Comparación de memoria

```text
!mona compare -f C:\Mona\sesion_revision\bytearray.bin -a DIRECCION_VERIFICADA
```

Sustituye `DIRECCION_VERIFICADA` por la dirección del primer byte de la tabla en la sesión actual.

- `-f`: archivo de referencia.
- `-a`: dirección inicial de memoria.

Guarda longitud y hash de la referencia, dirección, registros del mismo instante y salida. `Unmodified` cubre los bytes comparados en esa ubicación.

El inicio ocho bytes antes de ESP descrito en el laboratorio no es un ajuste fijo de mona. Hay que localizar la secuencia en cada detención.

## Módulos

```text
!mona modules
```

Registra nombre, base y versión o hash del módulo cuando estén disponibles. Sus indicadores no describen todas las mitigaciones efectivas del proceso. `NXCompat = False` no demuestra por sí solo que DEP esté desactivado.

## Si aparecen diferencias

1. Confirma la referencia de la sesión.
2. Localiza el comienzo real en el dump.
3. Revisa que la longitud esté completa.
4. Anota el primer índice distinto.
5. Comprueba representación, delimitadores y parseo antes de clasificar el byte.
