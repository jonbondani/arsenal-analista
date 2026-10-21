# Cheatsheet de Immunity Debugger

[Índice](../README.md) · [Resolución de problemas](../docs/07-troubleshooting.md)

Immunity se utiliza en el laboratorio para examinar un proceso x86 detenido. Las vistas de registros, pila y memoria permiten interpretar el estado que queda después de una prueba.

## Operaciones habituales

| Operación | Acceso orientativo | Uso |
| :--- | :--- | :--- |
| Abrir o adjuntar | `File > Open` o `File > Attach` | Seleccionar el proceso autorizado |
| Continuar | Habitualmente `F9` | Reanudar hasta la siguiente detención |
| Paso dentro | Habitualmente `F7` | Entrar en una llamada |
| Paso sobre llamada | Habitualmente `F8` | Observar el efecto sin entrar paso a paso |
| Breakpoint de software | Habitualmente `F2` sobre la instrucción | Detenerse en una ubicación concreta |
| Seguir en dump | Menú contextual del registro o dirección | Revisar los bytes de memoria |
| Examinar la pila | Vista de stack y registros | Relacionar punteros y contenido del hilo |

Comprueba los atajos en la instalación utilizada. Guarda el contexto antes de continuar, porque reanudar puede cambiar el estado que se está analizando.

## Datos que conviene conservar

- Identificador de sesión, hora y acción previa.
- Proceso, hilo y arquitectura.
- Tipo y código de excepción.
- EIP, ESP y EBP en el análisis x86.
- Instrucción y bytes en la posición de EIP.
- Dirección y tipo de acceso, si aparecen en la excepción.
- Módulos y permisos relevantes.
- Entrada y referencia de la prueba, identificadas por hash.

## Interpretar un marcador en EIP

El valor `42424242` es compatible con los bytes de `BBBB`. Para relacionarlo con una entrada concreta hay que conservar el contexto de esa prueba. La captura muestra un estado, mientras que la entrada y la secuencia de acciones explican cómo se llegó a él.

También hay que tener en cuenta los valores que el protocolo puede truncar o transformar. Ver un marcador no demuestra que todos los bytes se puedan utilizar de la misma manera.

## Localizar datos desde ESP

ESP puede apuntar al interior de la secuencia que interesa comparar. Las llamadas y los cambios de pila afectan a esa relación. Localiza el inicio real en el dump antes de utilizar una dirección como referencia.

El laboratorio describe una comparación ocho bytes antes de ESP. Es un dato de aquella prueba y necesita verificarse de nuevo si cambia el contexto.

## Registrar una detención en INT3

Anota si la interrupción estaba en los datos de prueba o si se insertó como breakpoint desde el depurador. Conserva también el estado anterior cuando sea posible. La captura [E06](../evidencias/capturas/E06-int3.png) permite leer la instrucción y EIP, aunque no contiene toda la ejecución previa.

Si una prueba llega a un estado diferente del esperado, guarda los datos antes de cambiar configuraciones. Un cambio de protecciones crea otras condiciones de análisis y debe quedar registrado.

Para otros procesos o arquitecturas se pueden valorar x32dbg, x64dbg o WinDbg. La [comparativa](../docs/05-comparativa.md) explica esas opciones; el flujo de este caso no se ha repetido con ellas.
