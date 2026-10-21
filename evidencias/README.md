# Capturas del laboratorio

[Volver al índice](../README.md)

Las capturas proceden de [jonbondani/CVE-2025-5548](https://github.com/jonbondani/CVE-2025-5548), en el commit [`6c302ee05599ce34dae0892f8678bed802879dab`](https://github.com/jonbondani/CVE-2025-5548/commit/6c302ee05599ce34dae0892f8678bed802879dab), del 20 de octubre de 2026.

Se han renombrado para identificarlas como E01 a E06, sin editar su contenido. La identidad de cada blob Git coincide con la del archivo original. Las rutas, tamaños y hashes están en el [manifiesto](manifiesto.json).

## E01. Copia en IDA

[Captura](capturas/E01-ida-copia.png) · [Original](https://github.com/jonbondani/CVE-2025-5548/blob/6c302ee05599ce34dae0892f8678bed802879dab/02-Exploitation/images/paso-0/12-pseudocodigo-strcpy.png)

Se ve una llamada de copia en la rama descrita como `USER`. La imagen permite revisar esa operación, pero no determina por sí sola la capacidad del destino ni la causa del fallo asociado a `NOOP`.

## E02. Offset del patrón

[Captura](capturas/E02-offset-246.png) · [Original](https://github.com/jonbondani/CVE-2025-5548/blob/6c302ee05599ce34dae0892f8678bed802879dab/02-Exploitation/images/paso-2/06-mona-pattern-offset-246.png)

`pattern_offset` devuelve la posición 246. El origen es el patrón consultado. La reproducción necesita el patrón transmitido y la entrada de la misma prueba.

## E03. Marcador en EIP

[Captura](capturas/E03-eip-marcador.png) · [Original](https://github.com/jonbondani/CVE-2025-5548/blob/6c302ee05599ce34dae0892f8678bed802879dab/02-Exploitation/images/paso-3/02-eip-42424242.png)

EIP contiene `42424242`, correspondiente a `BBBB`. La entrada exacta y el contexto de la sesión son necesarios para reconstruir cómo llegó ese valor al registro.

## E04. Alineación del dump

[Captura](capturas/E04-dump-alineacion.png) · [Original](https://github.com/jonbondani/CVE-2025-5548/blob/6c302ee05599ce34dae0892f8678bed802879dab/02-Exploitation/images/paso-4/04-hexdump-offset-esp8.png)

Se muestra parte de la secuencia en memoria. La explicación del laboratorio sitúa su inicio ocho bytes antes de ESP. Ese desplazamiento debe comprobarse de nuevo en otra detención.

## E05. Comparación de memoria

[Captura](capturas/E05-comparacion.png) · [Original](https://github.com/jonbondani/CVE-2025-5548/blob/6c302ee05599ce34dae0892f8678bed802879dab/02-Exploitation/images/paso-4/05-mona-compare-unmodified.png)

Se comparan 253 bytes y aparece `Unmodified`. `00`, `0a` y `0d` se excluyeron antes de la comparación. El resultado no evalúa esos valores omitidos.

## E06. INT3

[Captura](capturas/E06-int3.png) · [Original](https://github.com/jonbondani/CVE-2025-5548/blob/6c302ee05599ce34dae0892f8678bed802879dab/02-Exploitation/images/paso-5/10-eip-sobreescrito-final.png)

EIP coincide con una posición que se decodifica como `INT3`. La captura no muestra toda la ejecución previa ni su repetibilidad tras reiniciar.

El [caso práctico](../docs/03-caso-practico.md) desarrolla la interpretación de estas imágenes. Al ser capturas parciales, no se pueden tratar como una traza completa del mismo instante.
