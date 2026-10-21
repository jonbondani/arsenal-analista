# Caso práctico: revisión técnica del laboratorio FreeFloat

[Volver al índice](../README.md)

## Alcance y fuentes

El caso procede de [jonbondani/CVE-2025-5548](https://github.com/jonbondani/CVE-2025-5548), fijado para esta revisión en el commit [`6c302ee05599ce34dae0892f8678bed802879dab`](https://github.com/jonbondani/CVE-2025-5548/tree/6c302ee05599ce34dae0892f8678bed802879dab), fechado el 20 de octubre de 2026. Se consultaron su README, la documentación del entorno y la metodología de explotación. Las capturas seleccionadas se describen en el [registro](../evidencias/README.md).

La ficha [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-5548) identifica FreeFloat FTP Server 1.0 y un buffer overflow asociado al componente `NOOP Command Handler`. Se usa como contexto de una vulnerabilidad ya pública. No se deduce un CVE nuevo, una ruta adicional confirmada ni un impacto propio superior al demostrado.

**Método de esta entrega:** revisión documental, visual y comprobaciones locales con datos sintéticos. No se recibió el binario original ni se accedió a la VM. No se ejecutaron scripts del repositorio contra el servicio. Las pruebas históricas siguen siendo pruebas documentadas por su autor, no reproducciones de esta revisión.

## 1. Entorno y arquitectura

La [guía fuente del entorno](https://github.com/jonbondani/CVE-2025-5548/blob/6c302ee05599ce34dae0892f8678bed802879dab/01-Environment/README.md) describe Windows 11 en VirtualBox, una instalación asistida por un script docente y un snapshot. La metodología carga el programa como PE 80386 y muestra registros EIP/ESP, coherentes con un proceso x86.

La conclusión útil es que el análisis de esos registros debe hacerse con palabras de cuatro bytes. No puede deducirse el inventario exacto del entorno: faltan hash del ejecutable, build del sistema, versiones completas de Immunity/mona y política efectiva de memoria. Tampoco se ha verificado la topología de red de aquella VM.

## 2. IDA: encontrar una copia y acotar la hipótesis

La documentación sigue cadenas del protocolo, referencias cruzadas y la función `sub_402190`. E01 contiene pseudocódigo con una llamada `strcpy` en una rama asociada al tratamiento de `USER`.

![E01: pseudocódigo de IDA con una copia y vistas sincronizadas](../evidencias/capturas/E01-ida-copia.png)

**Observación:** se ve una operación de copia cuyo prototipo no recibe capacidad de destino. **Interpretación:** merece revisar la procedencia de la entrada, validaciones previas y capacidad real del destino. **Límite:** el pseudocódigo no demuestra por sí solo el tamaño ni la región de memoria del objeto apuntado por `this`, ni la relación causal con una ejecución posterior en otra rama.

La expresión `this + 28` no debe traducirse automáticamente como «buffer local en la pila». Para decidirlo hay que reconstruir asignación y vida del objeto, tipos, llamadores y acceso real en ensamblador. La ausencia de comprobación en una línea aislada tampoco prueba que no exista una validación previa.

El caso fuente pasa después a entradas `NOOP` o comandos no reconocidos y a la construcción de una respuesta de error. Esa diferencia es relevante: localizar una copia en `USER` no identifica de forma concluyente la operación responsable del fallo que se atribuye a `NOOP`.

**Comprobación propuesta, no realizada:** en una sesión autorizada, seguir la rama exacta desde el parseo hasta la construcción de la respuesta y registrar la instrucción que escribe fuera del destino, su origen, capacidad y pila de llamadas. El resultado debería explicar el mismo crash sin combinar rutas diferentes.

## 3. Timeout, excepción y marcador

El relato fuente describe aumentos de longitud, un timeout y registros con un valor repetido. Un timeout por sí mismo puede significar que el proceso está pausado bajo el depurador, que el servicio dejó de responder o que existe un problema de red. La evidencia de memoria aporta más información que el síntoma de red.

E03 muestra EIP = `42424242`, compatible con los bytes ASCII del marcador `BBBB` descrito en la documentación.

![E03: registro EIP con el marcador 42424242](../evidencias/capturas/E03-eip-marcador.png)

**Conclusión acotada:** la imagen es coherente con influencia de una entrada sobre el valor de EIP en esa sesión. No demuestra control de cualquier valor posible: algunos bytes pueden truncarse o transformarse. Tampoco demuestra privilegios, persistencia, ejecución de órdenes o repetibilidad.

Para defender una conclusión más fuerte harían falta entrada exacta y su hash, identidad del proceso, excepción, hilo, contexto previo a la transferencia y repetición controlada. La captura es útil, pero no contiene todo ese expediente.

## 4. Offset: qué significa realmente 246

E02 contiene la orden `!mona pattern_offset 41326941` y una coincidencia en la posición 246.

![E02: mona encuentra una coincidencia en la posición 246](../evidencias/capturas/E02-offset-246.png)

En x86 little-endian, el entero `0x41326941` corresponde en memoria a los bytes `41 69 32 41`, legibles como `Ai2A`. Eso explica la coincidencia de mona; no es un cambio de patrón.

La posición debe expresarse con su convención: offset **246 contado desde cero** respecto al patrón consultado. Cuatro bytes a partir de ese offset ocupan los índices 246 a 249. En numeración humana de posiciones desde uno, son 247 a 250. No son 246 bytes de capacidad del buffer: entre el inicio del dato y el estado sobrescrito puede haber otros campos, prefijos o transformaciones.

La búsqueda interna que aparece en la salida no implica que esa longitud interna se enviara por red. La metodología fuente menciona un patrón de 400 bytes y mona consulta su espacio de búsqueda. Para reproducir la relación habría que conservar el patrón realmente empleado y la entrada completa, incluidos comando, espacios y terminación de línea.

**Lección transferible:** un offset siempre necesita un origen. Escribir «246 desde el inicio del patrón de esa prueba» evita que otro analista lo aplique a todo el mensaje FTP o a una rama distinta.

## 5. Comparación de bytes: la dirección importa

La fuente describe una tabla que excluye previamente `00`, `0a` y `0d`. E04 muestra un dump que comienza visualmente con `09` en la dirección de referencia del relato. E05 compara una tabla de 253 bytes en otra dirección y devuelve `Unmodified`.

![E04: dump de memoria para revisar la alineación](../evidencias/capturas/E04-dump-alineacion.png)

![E05: mona compara 253 bytes y devuelve Unmodified](../evidencias/capturas/E05-comparacion.png)

El relato establece que se usó una dirección ocho bytes anterior a ESP. La captura de comparación muestra una dirección concreta, pero no basta para generalizar «usar siempre ESP - 8». Hay que localizar el principio de la tabla en cada detención. E04 y E05 se entienden junto al relato; no deben tratarse como un dump íntegro o una traza completa de la misma ejecución.

La tabla se obtiene de 256 valores posibles menos tres exclusiones: 253 bytes. Si esos bytes coinciden, la interpretación defendible es que **no se detectaron modificaciones adicionales en la referencia comparada, en esa ubicación y en esa prueba**. Los tres bytes excluidos nunca se contrastaron en esa comparación: no se ha demostrado individualmente su comportamiento.

El mensaje de mona contiene la palabra “shellcode”, pero aquí se describe el resultado de comparar bytes. Esa etiqueta de la herramienta no acredita que hubiera shellcode funcional o que se ejecutara.

Una mala alineación genera diferencias aparentes en casi toda una tabla intacta. El [ejercicio local](04-tutorial-local.md) reproduce ese error con ocho bytes sintéticos para aprender a diagnosticarlo sin provocar un crash.

## 6. Direcciones, módulos y fiabilidad

La sección histórica de salto a pila presenta tres representaciones incompatibles: una dirección en la prosa, otra secuencia literal de bytes y otra en la captura del script. Esto impide documentar una única dirección validada a partir del relato. Esta entrega no las convierte en una receta ni copia el script.

E06 sí muestra una instrucción `INT3` en la posición indicada por EIP. Eso es compatible con una prueba de interrupción en la sesión documentada; no muestra toda la cadena que llevó hasta ella.

![E06: EIP coincide visualmente con una instrucción INT3](../evidencias/capturas/E06-int3.png)

Encontrar una secuencia de opcodes en memoria no garantiza que pertenezca a una página ejecutable, a una instrucción válida en el modo correcto o a un módulo estable. Una dirección virtual aislada carece de contexto sin módulo, base, RVA, versión y configuración del proceso.

La fuente interpreta determinados indicadores de mona como ausencia de protecciones modernas. Esa conclusión es excesiva: `NXCompat = False` no decide por sí solo la política DEP efectiva, SafeSEH se relaciona con manejadores de excepciones y no todas las mitigaciones responden a la misma pregunta. Que un módulo no declare ASLR tampoco prueba estabilidad universal en cualquier sistema.

**Comprobación propuesta, no realizada:** registrar módulos y permisos de memoria en sesiones identificadas, conservar base y RVA y verificar el comportamiento tras reinicios. En esta entrega no se diseña una evasión de mitigaciones ni se valida una dirección reutilizable.

## 7. Informe de conclusiones

| Conclusión | Soporte | Reserva |
|---|---|---|
| El caso es un laboratorio de una vulnerabilidad FTP ya pública | Repositorio y NVD | La atribución externa no demuestra el estado de una copia local |
| Hay una copia que merece revisión en la rama `USER` | E01 | No equivale a la causa demostrada del fallo `NOOP` |
| mona identifica una posición 246 en el patrón consultado | E02 | Origen y configuración importan |
| EIP presenta el marcador descrito por el autor | E03 | No prueba un conjunto ilimitado de valores ni ejecución arbitraria |
| La referencia de 253 bytes resulta sin cambios | E05 | No cubre bytes omitidos ni todas las rutas |
| Se documenta una detención compatible con `INT3` | E06 | Cadena causal y estabilidad entre sesiones incompletas |
| Existe un exploit final validado en esta revisión | Ninguno | No se afirma |

El README histórico usa una etiqueta de “Finalizado”, pero sus apartados 6 y 7 siguen pendientes en la versión consultada. Ese estado editorial no aporta evidencia adicional. La entrega de este recurso puede estar preparada aunque el laboratorio fuente no documente una cadena de explotación completa.

## 8. Backlog verificable

| ID | Propuesta pendiente | Criterio de aceptación |
|---|---|---|
| P01 | Inventariar la muestra original | Hash, origen autorizado y arquitectura verificada |
| P02 | Trazar la ruta asociada a `NOOP` | Parseo, copia efectiva, capacidad y pila de llamadas de la misma sesión |
| P03 | Conservar entrada y patrón | Archivos exactos, hash y convención del offset |
| P04 | Documentar el punto inicial de comparación | Dump con inicio y longitud de la tabla, registros del mismo instante |
| P05 | Precisar las exclusiones | Diferenciar exclusión preventiva de resultado observado; no declarar pruebas inexistentes |
| P06 | Resolver incoherencia de direcciones | Una representación canónica, módulo, base, RVA y correspondencia de bytes |
| P07 | Evaluar repetibilidad | Sesiones independientes con reinicio y resultados registrados |
| P08 | Publicar el recurso documental | Revisión y autorización del propietario, URL accesible sin autenticación |

P01-P07 aumentan la fuerza del expediente histórico; no son requisitos para ejecutar los ejercicios locales ni se presentan como tareas ya realizadas.
