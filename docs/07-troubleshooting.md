# Resolución de problemas

[Volver al índice](../README.md)

## El servicio no responde

Comprueba primero si el proceso está pausado en el depurador o detenido por una excepción. Revisa la conectividad por separado. Un timeout no basta para identificar un crash.

## EIP no coincide con el patrón

Revisa que entrada, patrón y captura pertenezcan a la misma sesión. Un espacio, un prefijo o un comando distinto puede desplazar la medida. Comprueba también el formato del valor consultado y el modo de generación del patrón.

Si falta la entrada exacta, anota esa carencia antes de atribuir el cambio a otra causa.

## mona no encuentra la secuencia

Comprueba el valor transcrito y la referencia. La longitud o el modo pueden ser diferentes. Conserva la salida completa, aunque no encuentre coincidencia, para contrastarla con el patrón utilizado.

## La tabla parece alterada desde el principio

Localiza el primer byte en el dump y comprueba el hash y la longitud de la referencia. Una dirección desplazada o un archivo antiguo pueden explicar diferencias en casi toda la tabla.

Si en ESP aparece `09`, puede que apunte al interior de la secuencia. El ajuste de ocho bytes del caso no se aplica automáticamente a otras detenciones.

## Aparece Unmodified con valores excluidos

La coincidencia solo cubre los bytes presentes en la tabla. Guarda las exclusiones junto a la salida. Para estudiar un valor omitido hace falta una prueba que lo incluya.

## El plugin no carga

Revisa host, versión, intérprete y ruta de instalación. mona clásico y mona3 pueden necesitar entornos distintos. Comprueba una orden de diagnóstico antes de empezar a interpretar resultados.

## IDA no genera pseudocódigo

Revisa edición, licencia, servicio y estado del análisis. Se puede continuar con el grafo y el ensamblador. Si una reconstrucción es dudosa, las instrucciones permiten comprobar el cálculo o la condición que interesa.

## Una dirección cambia

Compara muestra, módulo, versión, base y RVA. La diferencia puede deberse a ASLR, a otra copia o a otra sesión. La dirección virtual por sí sola no distingue esas causas.

## INT3 aparece en un contexto diferente

Comprueba si el breakpoint lo insertó el depurador, si estaba en los datos o si se llegó por otra ruta. Guarda la instrucción, los registros y el estado anterior cuando esté disponible.

## El hash de una captura no coincide

Revisa tamaño y origen. Puede ser otra copia, una edición o una conversión. Conserva el archivo distinto por separado y registra el cambio antes de actualizar la referencia.

## La utilidad local devuelve 1 o 2

`compare` devuelve 1 cuando hay diferencia o truncamiento. Es lo esperado al comparar los dos archivos distintos del tutorial.

El código 2 indica un problema de lectura, formato o tamaño. Solo se aceptan pares hexadecimales con espacios o saltos de línea, hasta 1 MiB de texto por archivo. Retira direcciones, comentarios y columnas ASCII de una copia de trabajo, conservando el original.

## Revisar una comparación

1. Guarda la primera salida.
2. Comprueba referencia, hash y longitud.
3. Localiza el inicio de la secuencia.
4. Repite cambiando solo la variable que se está revisando.
5. Compara ambas salidas y anota el cambio.

Si solo quedan imágenes y falta el estado original, la causa puede quedar sin resolver. Registra la explicación posible y los datos que permitirían comprobarla.

Para compartir el problema, incluye arquitectura, versiones, comando y salida relevante. La [ficha de sesión](../plantillas/sesion.md) recoge esos datos.
