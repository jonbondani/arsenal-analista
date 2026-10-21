# Cheatsheet de Immunity Debugger

[Índice](../README.md) · [Resolución de problemas](../docs/07-troubleshooting.md)

## Operaciones habituales

| Operación | Acceso orientativo | Uso |
| :--- | :--- | :--- |
| Abrir o adjuntar | `File > Open` o `File > Attach` | Seleccionar el proceso |
| Continuar | Habitualmente `F9` | Reanudar hasta otra detención |
| Paso dentro | Habitualmente `F7` | Entrar en una llamada |
| Paso sobre llamada | Habitualmente `F8` | Revisar su efecto sin entrar paso a paso |
| Breakpoint de software | Habitualmente `F2` | Detenerse en una instrucción |
| Seguir en dump | Menú contextual del registro o dirección | Leer los bytes de memoria |
| Examinar la pila | Vista de stack | Relacionar punteros y contenido del hilo |

Comprueba los atajos en la instalación utilizada. Antes de continuar, guarda los registros y la memoria que se estén revisando.

## Registrar una detención

- Sesión, hora y acción anterior.
- Proceso, hilo y arquitectura.
- Tipo y código de excepción.
- EIP, ESP y EBP en el proceso x86.
- Instrucción y bytes en EIP.
- Dirección y tipo de acceso, si aparecen.
- Módulos y permisos relevantes.
- Entrada y referencia utilizadas.

## Marcador en EIP

`42424242` corresponde a los bytes de `BBBB`. Para atribuirlo a una entrada, conserva los datos de esa prueba y el estado anterior a la transferencia cuando sea posible.

Algunos valores pueden truncarse o transformarse durante el parseo. Un marcador correcto no demuestra que todos los bytes lleguen de la misma forma.

## Datos cerca de ESP

ESP puede apuntar al interior de la secuencia. Localiza el principio en el dump antes de comparar.

En el laboratorio se describe una comparación ocho bytes antes de ESP. Ese desplazamiento pertenece a aquella prueba y debe comprobarse de nuevo si cambia el contexto.

## Detención en INT3

Registra si la interrupción estaba en el dato de prueba o si la insertó el depurador. La captura [E06](../evidencias/capturas/E06-int3.png) muestra la instrucción y EIP, pero no toda la ejecución anterior.

Si el proceso se detiene en otro punto, guarda el estado antes de modificar la configuración. Cualquier cambio de protecciones debe quedar anotado como una condición distinta de la prueba.
