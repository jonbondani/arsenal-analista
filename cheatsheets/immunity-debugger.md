# Cheatsheet comentada: Immunity Debugger

[Índice](../README.md) · [Troubleshooting](../docs/07-troubleshooting.md)

**Pregunta principal:** ¿qué estado tiene este proceso en este instante?  
**Uso en el caso:** registros x86, pila, dump y detenciones documentadas.  
**Estado:** revisión de capturas existentes; no se ejecutó el depurador durante esta preparación.

## Operaciones habituales

| Acción | Operación orientativa | Utilidad | Precaución |
|---|---|---|---|
| Abrir proceso autorizado | `File > Open` o `File > Attach` | Obtener contexto dinámico | Confirmar proceso y arquitectura |
| Continuar | `F9` en la configuración habitual | Reanudar hasta la siguiente detención | No continuar antes de guardar la evidencia relevante |
| Paso dentro | `F7` | Entrar en una llamada | Puede cambiar mucho el contexto y producir ruido |
| Paso sobre llamada | `F8` | Observar el efecto de una llamada | Una llamada puede no retornar o alterar estado |
| Breakpoint de software | `F2` sobre una instrucción, habitualmente | Detener antes de una operación conocida | Registrar si el breakpoint fue insertado por el analista |
| Seguir en dump | Menú contextual del registro o dirección | Ver los bytes reales | No confundir representación ASCII con bytes |
| Revisar pila | Vista de stack y registros | Relacionar punteros con memoria | La pila es específica del hilo y del instante |

Confirmar atajos en la instalación histórica. La comparación con otras herramientas no implica que compartan todos los menús o plugins.

## Datos mínimos al detenerse

| Campo | Razón |
|---|---|
| Sesión, hora y acción previa | Vincular la captura con una prueba |
| Proceso, hilo y arquitectura | Evitar mezclar contexto |
| Tipo/código de excepción | Distinguir acceso inválido, breakpoint y otras detenciones |
| EIP, ESP y EBP | Orientar la inspección x86 |
| Instrucción en EIP y bytes | Revisar si la decodificación es coherente |
| Dirección de acceso y operación, si constan | Separar lectura, escritura y ejecución |
| Módulos y permisos relevantes | Interpretar estabilidad y ejecutabilidad |
| Entrada o referencia con hash | Mantener trazabilidad sin copiar secretos al informe |

## Interpretaciones que deben acotarse

`EIP = 42424242` es compatible con el marcador `BBBB`. Para atribuirlo a una entrada concreta hay que relacionar sesión, datos y estado. Un valor repetido no acredita por sí solo acceso con privilegios ni una ejecución de órdenes.

ESP contiene una dirección de la pila, no una etiqueta del inicio de todos los datos de prueba. Los prólogos, epílogos, llamadas y convenciones de llamada pueden desplazar su relación con el contenido. En el caso, la fuente describe una comparación ocho bytes anterior a ESP; eso no es una regla del depurador.

`INT3` puede aparecer por un breakpoint del analista, por bytes ya presentes o por una prueba documentada. La imagen E06 permite ubicar la instrucción y EIP, pero no prueba toda la secuencia de ejecución. Debe registrarse si el breakpoint fue insertado por el depurador o estaba en el dato analizado.

## Cuándo detener el diagnóstico

Si no se puede relacionar la captura con la entrada o si el proceso es otro, marcar evidencia insuficiente y volver al inventario. Si se alcanza un estado distinto del previsto, guardar contexto antes de cambiar configuraciones. No resolver diferencias desactivando protecciones sin documentar que se ha creado un entorno diferente.

Para otro caso moderno, evaluar x32dbg/x64dbg o WinDbg según arquitectura y objetivo. La sustitución queda como propuesta; no se ha probado compatibilidad del flujo de Immunity en este paquete.
