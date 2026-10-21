# Tutorial: revisar memoria y representaciones sin tocar un servicio

[Volver al índice](../README.md)

## Objetivo y condiciones

Este tutorial practica cuatro tareas de un analista: verificar integridad, interpretar endianness, comparar una referencia y detectar una alineación incorrecta. Usa datos sintéticos incluidos y una utilidad de la biblioteca estándar de Python. No abre sockets, no ejecuta binarios analizados y no genera una entrada de explotación.

Requisito: Python 3.10 o posterior. Ejecutar desde la raíz del recurso. En Windows puede sustituirse `python3` por `py -3`. Los resultados comprobados durante la preparación están en [validación local](../ejemplos/VALIDACION.md); no deben confundirse con el laboratorio FreeFloat.

## Paso 1. Revisar la evidencia con una pregunta

Abre [E02](../evidencias/capturas/E02-offset-246.png) y anota tres datos: orden utilizada, valor buscado y posición devuelta. La captura permite leer `pattern_offset`, `41326941` y `246`. A continuación escribe lo que falta: archivo exacto del patrón transmitido, origen del offset y relación completa con una sesión.

Esta separación evita que un dato visible termine convertido en un supuesto no declarado. No hace falta conocer una dirección de salto para extraer una conclusión útil del resultado.

## Paso 2. Ejecutar la demostración sintética

```console
python3 herramientas/auditoria_local.py demo
```

La salida JSON incluye estos resultados:

| Campo | Resultado esperado | Interpretación |
|---|---|---|
| `clase` | `SINTETICO` | No es una prueba sobre el servidor |
| `entero_hex` | `0x12345678` | Número elegido exclusivamente para el ejercicio |
| `little_endian` | `78563412` | Orden en memoria de un entero de 32 bits |
| `ida_vuelta_correcta` | `true` | Desempaquetar recupera el mismo entero |
| `coincide_inicio_cero` | `false` | El prefijo del dump sintético desplaza el dato |
| `coincide_inicio_dos` | `true` | La referencia empieza dos bytes después |
| `primera_diferencia` | `3` | Índice desde cero del byte alterado en otro ejemplo |

El entero elegido no corresponde a una dirección validada del laboratorio. El prefijo artificial ilustra el mismo tipo de error de alineación que puede aparecer al asumir que una tabla comienza en ESP.

## Paso 3. Comparar dos archivos hexadecimales

Los archivos de ejemplo contienen ocho bytes cada uno. Se diferencian en el cuarto byte: índice 3 desde cero.

```console
python3 herramientas/auditoria_local.py compare ejemplos/referencia.hex ejemplos/observado.hex
```

La salida indica `coinciden: false`, longitudes 8 y 8 y `primera_diferencia: 3`. El código de salida es **1**, porque se encontró una diferencia intencional. Esto no significa que la utilidad haya fallado. Un resultado idéntico devuelve 0; errores de lectura o formato devuelven 2.

Para el control positivo:

```console
python3 herramientas/auditoria_local.py compare ejemplos/referencia.hex ejemplos/referencia.hex
```

La diferencia de estos archivos se ha introducido artificialmente. No se puede trasladar a una lista de bad characters de FreeFloat. Precisamente ese salto entre datos sintéticos y resultado real es lo que este tutorial enseña a evitar.

## Paso 4. Calcular el hash de una captura

```console
python3 herramientas/auditoria_local.py hash evidencias/capturas/E02-offset-246.png
```

Compara el SHA-256 con el [manifiesto](../evidencias/manifiesto.json) o con [SHA256SUMS](../SHA256SUMS.txt). El hash acredita que ambos archivos contienen los mismos bytes a efectos prácticos de integridad. No acredita fecha de captura, autoría, corrección de un razonamiento o ausencia de edición anterior.

La utilidad muestra solo nombre de archivo, tamaño y hash. Para evitar filtraciones, tampoco imprime contenido de los archivos comparados ni vuelca memoria. No pases rutas confidenciales a herramientas ajenas sin revisar antes cómo registran sus argumentos.

## Paso 5. Revisar el resultado histórico de mona

Abre [E05](../evidencias/capturas/E05-comparacion.png). Identifica longitud de referencia, dirección de comparación y exclusiones. Redacta una conclusión con cuatro componentes:

> En E05, mona compara una referencia de 253 bytes en una dirección concreta y devuelve `Unmodified`. Esto respalda que la referencia comparada coincide en esa prueba. Los bytes excluidos no se han contrastado mediante ese resultado. La alineación debe verificarse de nuevo en otra sesión.

El objetivo no es copiar la frase, sino comprobar que cada parte se apoya en un dato y no en una costumbre del laboratorio.

## Paso 6. Crear un miniinforme

Usa la [plantilla de informe](../plantillas/informe.md) con este alcance: «Revisión documental de E02 y E05, más ejercicios sintéticos locales». Registra comandos realmente ejecutados, resultados y limitaciones. No marques como realizada una prueba simplemente porque esta entrega incluye una salida de ejemplo.

## Ampliación propuesta para un laboratorio autorizado

Si más adelante se dispone de la VM y los artefactos originales, la primera ampliación útil es inventariar y conservar la entrada exacta, no construir un payload final. El siguiente paso consiste en relacionar la rama de protocolo con la operación de memoria y guardar registros, dump y salida de mona de la misma sesión. Estas ampliaciones permanecen pendientes en esta entrega.

## Preguntas de autoevaluación

1. ¿Por qué una tabla intacta puede parecer corrupta? Porque se compara desde una dirección equivocada o con otra referencia.
2. ¿Qué demuestra `Unmodified`? Coincidencia del conjunto y la ubicación comparados, dentro del contexto de esa prueba.
3. ¿Qué falta para reproducir el offset? Patrón y entrada exactos, origen de la medida y mismo contexto de ejecución.
4. ¿Un hash demuestra que un crash ocurrió? No; solo ayuda a identificar el archivo que se está revisando.
5. ¿EIP con un marcador equivale a una shell? No; son afirmaciones de alcance distinto.
