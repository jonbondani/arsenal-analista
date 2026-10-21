# Evidencias del laboratorio

[Volver al índice](../README.md)

## Procedencia

Las seis capturas proceden de [jonbondani/CVE-2025-5548](https://github.com/jonbondani/CVE-2025-5548), en el commit [`6c302ee05599ce34dae0892f8678bed802879dab`](https://github.com/jonbondani/CVE-2025-5548/commit/6c302ee05599ce34dae0892f8678bed802879dab), del 20 de octubre de 2026. La revisión se realizó el 21 de octubre.

Los archivos se renombraron para identificarlos dentro de la guía y se mantuvieron sin editar. Su identidad de blob Git se contrastó con las rutas del commit. El [manifiesto](manifiesto.json) recoge ruta original, URL, tamaño, SHA-256 e identidad del blob.

Esta comprobación vincula las copias con esa versión del repositorio. La ejecución del laboratorio no se ha repetido para preparar la guía. Las imágenes parciales tampoco se unen como si fueran una traza completa del mismo instante.

## E01. Copia en IDA

[Ver captura](capturas/E01-ida-copia.png) · [Archivo original](https://github.com/jonbondani/CVE-2025-5548/blob/6c302ee05599ce34dae0892f8678bed802879dab/02-Exploitation/images/paso-0/12-pseudocodigo-strcpy.png)

El pseudocódigo muestra una llamada de copia en la rama descrita como `USER`. Sirve para estudiar el origen del dato, el destino y sus validaciones. La imagen no determina por sí sola la región del objeto ni la causa de la ruta `NOOP`.

## E02. Posición del patrón

[Ver captura](capturas/E02-offset-246.png) · [Archivo original](https://github.com/jonbondani/CVE-2025-5548/blob/6c302ee05599ce34dae0892f8678bed802879dab/02-Exploitation/images/paso-2/06-mona-pattern-offset-246.png)

La consulta `pattern_offset` devuelve una coincidencia en la posición 246. El resultado se refiere al patrón consultado. Para reproducirlo hay que conservar el patrón transmitido y el origen de esa medida.

## E03. Marcador en EIP

[Ver captura](capturas/E03-eip-marcador.png) · [Archivo original](https://github.com/jonbondani/CVE-2025-5548/blob/6c302ee05599ce34dae0892f8678bed802879dab/02-Exploitation/images/paso-3/02-eip-42424242.png)

EIP contiene `42424242`, compatible con `BBBB`. La relación completa con la entrada necesita el contexto de la prueba. La captura no acredita por sí sola ejecución de órdenes, privilegios ni la posibilidad de utilizar cualquier valor.

## E04. Alineación del dump

[Ver captura](capturas/E04-dump-alineacion.png) · [Archivo original](https://github.com/jonbondani/CVE-2025-5548/blob/6c302ee05599ce34dae0892f8678bed802879dab/02-Exploitation/images/paso-4/04-hexdump-offset-esp8.png)

El dump permite revisar una secuencia de bytes desde una dirección concreta. La explicación original sitúa el inicio de la tabla ocho bytes antes de ESP. La imagen es parcial y ese ajuste debe comprobarse de nuevo en otra sesión.

## E05. Comparación de memoria

[Ver captura](capturas/E05-comparacion.png) · [Archivo original](https://github.com/jonbondani/CVE-2025-5548/blob/6c302ee05599ce34dae0892f8678bed802879dab/02-Exploitation/images/paso-4/05-mona-compare-unmodified.png)

La salida compara una referencia de 253 bytes y muestra `Unmodified`. Los valores `00`, `0a` y `0d` se excluyeron previamente. La coincidencia se aplica al conjunto comparado en esa dirección y en esa prueba.

## E06. Detención en INT3

[Ver captura](capturas/E06-int3.png) · [Archivo original](https://github.com/jonbondani/CVE-2025-5548/blob/6c302ee05599ce34dae0892f8678bed802879dab/02-Exploitation/images/paso-5/10-eip-sobreescrito-final.png)

EIP coincide con una posición que se decodifica como `INT3`. El estado es compatible con la detención descrita. Para reconstruir la ejecución previa y su estabilidad hacen falta más datos de la sesión.

## Selección de imágenes

Las capturas cubren los conceptos que se explican en la guía. Se han dejado fuera las pantallas de cuenta e instalación y la imagen con el código de redirección.

En las imágenes seleccionadas no se detectaron credenciales ni tokens durante la revisión visual. Antes de una nueva publicación conviene revisar también su contexto y los derechos de uso. Las direcciones visibles son direcciones de memoria del laboratorio.

Los diagramas y tablas son material explicativo. Los ejercicios locales tienen su registro independiente en [validación](../ejemplos/VALIDACION.md).
