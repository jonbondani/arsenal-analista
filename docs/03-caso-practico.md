# Caso práctico: FreeFloat FTP Server

[Volver al índice](../README.md)

## Punto de partida

El caso utiliza la documentación de [jonbondani/CVE-2025-5548](https://github.com/jonbondani/CVE-2025-5548), en el commit [`6c302ee05599ce34dae0892f8678bed802879dab`](https://github.com/jonbondani/CVE-2025-5548/tree/6c302ee05599ce34dae0892f8678bed802879dab), del 20 de octubre de 2026. La [ficha de NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-5548) relaciona FreeFloat FTP Server 1.0 con un buffer overflow asociado a `NOOP`.

La guía revisa las capturas y el relato de ese laboratorio. No se ha repetido la ejecución del servidor al elaborar esta documentación. Las comprobaciones locales de Python se explican en otro apartado y utilizan datos sintéticos.

El [registro de evidencias](../evidencias/README.md) recoge la procedencia de cada imagen. Los archivos se conservaron sin editar y se comprobaron contra el commit citado.

## Entorno

La [documentación del entorno](https://github.com/jonbondani/CVE-2025-5548/blob/6c302ee05599ce34dae0892f8678bed802879dab/01-Environment/README.md) describe Windows 11 en VirtualBox y un snapshot después de instalar las herramientas. La metodología carga el binario como PE 80386 y las imágenes muestran EIP y ESP, coherentes con un proceso x86.

Para repetir exactamente el laboratorio harían falta algunos datos más: el hash del ejecutable, la build de Windows, las versiones completas de Immunity y mona y la configuración efectiva de memoria y red. El nombre del programa y su versión comercial no identifican por sí solos una muestra concreta.

## La copia localizada en IDA

El análisis original sigue cadenas del protocolo y sus referencias hasta `sub_402190`. En E01 aparece pseudocódigo con una llamada `strcpy` en la rama descrita como `USER`.

![E01: copia localizada en el pseudocódigo de IDA](../evidencias/capturas/E01-ida-copia.png)

La llamada merece revisarse porque no recibe la capacidad del destino. Para determinar si esa copia puede escribir fuera de sus límites hay que reconstruir el origen del dato, la capacidad real del destino y las validaciones anteriores.

La expresión `this + 28` tampoco permite afirmar por sí sola que el destino sea una variable local en la pila. Hay que seguir la asignación del objeto y sus llamadores, y contrastar los tipos del pseudocódigo con las instrucciones.

Más adelante, el laboratorio trabaja con `NOOP` o comandos no reconocidos y menciona la construcción de una respuesta de error. Esa ruta debe estudiarse por separado. La copia observada en `USER` es una pista estática, pero no basta para identificar la operación responsable del crash asociado a `NOOP`.

La comprobación que falta consiste en seguir esa entrada desde el parseo hasta la escritura que corrompe memoria, conservando la capacidad del destino, el origen de los bytes y la pila de llamadas de una misma sesión.

## Del timeout al estado de EIP

El relato describe un aumento de longitud en las entradas, seguido de un timeout. Ese síntoma puede aparecer si el proceso está pausado, si se produce una excepción o si hay un problema de comunicación. El contexto del depurador permite distinguir esas situaciones.

E03 muestra EIP con el valor `42424242`, compatible con el marcador `BBBB` descrito en la prueba.

![E03: EIP con el valor 42424242](../evidencias/capturas/E03-eip-marcador.png)

La imagen encaja con una influencia de la entrada sobre EIP en esa sesión. Para reconstruir la relación completa también harían falta la entrada exacta, la excepción, el hilo y el estado anterior a la transferencia.

Además, un marcador reconocible no demuestra que cualquier valor de cuatro bytes llegue igual. El protocolo o las funciones de cadena pueden tratar algunos valores de forma distinta. La ejecución de órdenes, los privilegios y la repetibilidad requieren evidencias adicionales.

## El offset 246

E02 recoge la consulta `!mona pattern_offset 41326941` y una coincidencia en la posición 246.

![E02: coincidencia de patrón en la posición 246](../evidencias/capturas/E02-offset-246.png)

En x86 little-endian, el valor `0x41326941` corresponde a los bytes `41 69 32 41`, que se leen como `Ai2A`. Esa diferencia entre el entero y el orden de sus bytes explica la salida de mona.

El offset se cuenta desde cero respecto al patrón consultado. Los cuatro bytes que empiezan en el índice 246 ocupan los índices 246 a 249. Si se numeran las posiciones desde uno, corresponden a las posiciones 247 a 250.

Este dato no indica que el buffer tenga una capacidad de 246 bytes. Puede haber otros campos, prefijos o transformaciones entre el comienzo del dato y la posición sobrescrita. Para reutilizar la medida hay que conservar el patrón y la entrada completos, incluidos el comando, los espacios y el final de línea.

La metodología menciona un patrón de 400 bytes. La longitud de búsqueda interna que aparece en la salida de mona no significa que se transmitiera esa misma cantidad de datos por red.

## Alineación y comparación de bytes

La referencia descrita en el caso excluye `00`, `0a` y `0d`. Al partir de 256 valores posibles quedan 253 bytes para comparar.

E04 muestra parte del dump y E05 recoge una comparación con el resultado `Unmodified`.

![E04: secuencia de bytes en memoria](../evidencias/capturas/E04-dump-alineacion.png)

![E05: comparación de una referencia de 253 bytes](../evidencias/capturas/E05-comparacion.png)

El relato sitúa el inicio de la tabla ocho bytes antes de ESP. Ese ajuste corresponde a la prueba descrita. En otra detención hay que localizar de nuevo el primer byte de la secuencia, porque ESP puede apuntar al interior del dato.

La captura de comparación contiene una dirección concreta, pero no reconstruye por sí sola toda la sesión. Las dos imágenes se interpretan junto a la documentación, sin unirlas como si fueran un dump completo del mismo instante.

El resultado permite afirmar que la referencia comparada coincide en esa ubicación y en esa prueba. Los tres bytes excluidos no formaban parte de la comparación, de modo que su comportamiento individual sigue sin quedar demostrado por esa salida.

El mensaje de mona utiliza la palabra “shellcode”. En este contexto describe una comparación de bytes; no acredita que se haya ejecutado shellcode funcional.

Una dirección inicial equivocada puede hacer que una tabla intacta parezca modificada. El [tutorial local](04-tutorial-local.md) reproduce ese problema con un prefijo sintético, sin provocar un crash ni conectarse a un servidor.

## Direcciones y detención en INT3

La sección original de salto a pila contiene diferencias entre la dirección escrita en la prosa, la secuencia de bytes y la captura del script. Con ese material no se puede fijar una única representación validada. La guía conserva la observación y evita convertir esas direcciones en instrucciones reutilizables.

E06 muestra EIP sobre una posición que se decodifica como `INT3`.

![E06: EIP sobre una instrucción INT3](../evidencias/capturas/E06-int3.png)

La captura es compatible con la detención descrita en el laboratorio. Aun así, no muestra todos los pasos anteriores ni permite medir la estabilidad entre reinicios. También conviene registrar si la interrupción estaba en el dato de prueba o si la insertó el depurador.

Una secuencia de opcodes encontrada en memoria necesita más contexto: módulo, base, RVA, versión, modo de ejecución y permisos de la página. Encontrarla una vez no garantiza que la misma dirección sirva en otra sesión.

## Mitigaciones y estabilidad

Los indicadores del módulo responden a cuestiones diferentes. ASLR afecta a la disposición de direcciones; DEP limita la ejecución desde determinadas páginas; CFG controla ciertas transferencias indirectas; SafeSEH se relaciona con manejadores de excepciones en los entornos aplicables.

Por eso, `NXCompat = False` no basta para afirmar que DEP está desactivado. Hay que comprobar la política efectiva y los permisos de la memoria concreta. Del mismo modo, la ausencia de una declaración de ASLR no demuestra estabilidad universal en cualquier sistema.

Para ampliar esa parte del laboratorio se necesitarían sesiones identificadas, un inventario de módulos y una comparación de bases y RVA tras reiniciar. Esas comprobaciones no están documentadas aquí como realizadas.

## Resultado de la revisión

Las capturas permiten estudiar una copia candidata en IDA, una coincidencia de patrón, EIP con un marcador, una comparación de memoria y una detención compatible con `INT3`.

La explicación completa de la ruta `NOOP`, la reproducción exacta y la estabilidad de las direcciones necesitan más información. El README original utiliza la etiqueta “Finalizado”, aunque los apartados de shellcode y exploit final siguen pendientes en la versión consultada. Esa etiqueta describe el estado editorial del repositorio y no añade resultados técnicos.

## Continuación del análisis

Las siguientes comprobaciones permitirían completar el registro del laboratorio:

- **Identificar la muestra:** guardar hash, origen y arquitectura confirmada.
- **Seguir la ruta `NOOP`:** conservar parseo, operación de copia, capacidad del destino y pila de llamadas de la misma sesión.
- **Preservar las entradas:** guardar el patrón y el mensaje completos, junto al origen del offset.
- **Documentar la comparación:** registrar inicio, longitud, referencia y registros del mismo instante.
- **Precisar las exclusiones:** separar decisiones preventivas de comportamientos observados.
- **Resolver las direcciones:** relacionar una representación coherente con módulo, base y RVA.
- **Comprobar repetibilidad:** repetir en sesiones independientes y registrar los cambios tras reiniciar.

Son ampliaciones del caso original. El tutorial de Python puede seguirse con los archivos incluidos, sin completar estas pruebas.
