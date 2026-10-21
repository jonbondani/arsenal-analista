# Resolución de problemas

[Volver al índice](../README.md)

## El servicio no responde

Un timeout puede deberse a una pausa del depurador, a un proceso detenido o a la comunicación de red. En una sesión autorizada, revisa primero el estado del proceso y comprueba la conectividad por separado. El timeout no permite identificar por sí solo un crash.

## El valor de EIP no coincide con el patrón

Comprueba que el patrón, la entrada y la captura pertenecen a la misma sesión. Un espacio, un prefijo o un comando diferente puede cambiar el origen de la medida. Revisa también la representación hexadecimal del valor y el modo con el que se consulta el patrón.

Si no se conserva la entrada exacta, deja anotada esa falta de contexto antes de atribuir la diferencia a otra causa.

## mona no encuentra la secuencia

Revisa el valor transcrito y el patrón utilizado. La longitud o el modo de generación pueden ser distintos. Conserva la salida completa, incluso cuando no haya coincidencia, para poder contrastarla con la referencia.

## La tabla parece modificada casi desde el principio

La causa puede estar en la dirección inicial o en un archivo de referencia antiguo. Localiza el principio de la secuencia en el dump y comprueba el hash y la longitud de la referencia antes de interpretar bytes alterados.

Si ESP apunta a una posición cuyo primer byte es `09`, puede estar dentro de la tabla. El ajuste de ocho bytes descrito en el caso no se debe aplicar automáticamente a otras sesiones.

## Aparece Unmodified con bytes excluidos

El resultado se limita a los valores presentes en la referencia. Revisa cómo se generó la tabla y conserva las exclusiones junto a la salida. Para conocer el comportamiento de un byte omitido haría falta una prueba específica que lo incluyera y quedara documentada.

## El plugin no carga

Comprueba host, versión, ruta de instalación e intérprete. El entorno de mona clásico y el de mona3 pueden tener requisitos distintos. Antes de empezar el análisis, verifica que una orden de diagnóstico funciona en la instalación elegida.

## IDA no genera pseudocódigo

La disponibilidad depende de la edición, la licencia, el servicio y el estado del análisis. Revisa las condiciones de la instalación y continúa con el grafo y el ensamblador cuando sea necesario. El pseudocódigo facilita el trabajo, pero las instrucciones siguen siendo la referencia para comprobar una reconstrucción dudosa.

## Una dirección cambia entre sesiones

Compara módulo, versión, base y RVA. La diferencia puede deberse a ASLR, a otra muestra o a otro contexto. Una dirección virtual aislada no permite distinguir esas causas.

## La detención en INT3 no tiene el contexto esperado

Revisa si el breakpoint fue insertado por el depurador, si formaba parte de los datos o si el proceso llegó por otra ruta. Guarda el estado anterior cuando esté disponible y registra la sesión. La instrucción visible no explica por sí sola toda la ejecución previa.

## El hash de una captura es distinto

Comprueba tamaño y origen. Puede tratarse de otra copia, una edición, una conversión o un archivo dañado. Conserva la diferencia en el registro; el manifiesto debe reflejar los archivos que realmente corresponden a la versión compartida.

## La utilidad local termina con código 1 o 2

`compare` devuelve 1 cuando encuentra una diferencia o un truncamiento. Los dos archivos del tutorial difieren a propósito, así que ese resultado es el esperado.

El código 2 indica un problema de lectura, formato o tamaño. Los archivos aceptan pares hexadecimales con espacios o saltos de línea, sin direcciones, comentarios ni columnas ASCII. El límite es 1 MiB de texto por archivo.

## El visor no muestra Mermaid

Abre el documento en GitHub y revisa el bloque de código. La explicación de cada fase se conserva también en texto para poder seguir la metodología desde un visor sin soporte de diagramas.

## Revisar una comparación paso a paso

1. Guarda el resultado inicial antes de cambiar nada.
2. Comprueba referencia, hash y longitud.
3. Localiza el primer byte de la secuencia.
4. Repite la comparación cambiando solo la variable que se está revisando.
5. Anota la diferencia entre ambas salidas.

Si solo quedan imágenes y falta el estado original, la causa puede quedar sin resolver. En ese caso conviene describir la explicación posible y la información necesaria para comprobarla.

Al compartir un problema, incluye arquitectura, versiones, orden utilizada y resultado resumido. La [ficha de sesión](../plantillas/sesion.md) ayuda a reunir esos datos sin enviar dumps o información privada innecesaria.
