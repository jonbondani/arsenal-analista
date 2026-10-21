# Limitaciones, alcance y decisiones pendientes

[Volver al índice](../README.md)

## Límites del expediente

| Limitación | Consecuencia práctica | Tratamiento aplicado |
|---|---|---|
| No se recibió el binario original | No puede verificarse arquitectura, hash o flujo directamente | Se atribuyen esas descripciones al repositorio fuente |
| No se accedió a la VM | No hay reproducción nueva ni inventario completo | Se habla de revisión de evidencias |
| No se conserva aquí la entrada completa de cada sesión | El enlace entre bytes enviados y estado es parcial | Se marcan propuestas P02-P04 |
| Capturas parciales | Pueden faltar excepción, hilo y estado previo | Se evita afirmar una cadena completa |
| `USER` y `NOOP` son rutas distintas en el relato | La pista estática no acredita la causa dinámica | Se mantiene como hipótesis hasta trazar la ruta |
| Tres bytes se excluyen antes de comparar | La comparación no evalúa esos valores | Se distingue exclusión preventiva de fallo demostrado |
| Direcciones inconsistentes en el relato | No hay dirección canónica defendible | No se incluye receta de redirección |
| Sin repetición entre reinicios | No se acredita fiabilidad | Se exige registro entre sesiones para ampliarla |
| Indicadores de módulos incompletos | No describen toda la política del proceso | Se separan atributos PE de mitigaciones efectivas |
| Manual completo del módulo no aportado | No se verifica pertenencia de cada herramienta al temario | El propietario debe confirmarla al enviar |

## Límites de las herramientas

**IDA y decompilación.** Los nombres y tipos inferidos pueden ser incorrectos. Una expresión de puntero no informa por sí sola de la capacidad del destino. El análisis estático puede omitir decisiones indirectas o reconstruir mal una condición. Volver al ensamblador y conservar la incertidumbre es parte del método.

**Depuración.** Pausar, continuar y adjuntar un depurador puede cambiar tiempos y estados. Las direcciones dependen de la sesión. Una detención aislada no basta para atribuir una secuencia previa que no se capturó.

**mona.** Automatiza operaciones, pero depende de la referencia, dirección y entorno que se le entreguen. Su vocabulario de salida no determina por sí mismo el significado de la prueba. El proyecto clásico está archivado; una futura migración debe validarse por separado.

**Python.** La utilidad local verifica representaciones y datos. No identifica vulnerabilidades, no conoce la procedencia del dump y no decide si una exclusión es correcta. Sus resultados sintéticos no se incorporan como evidencia de FreeFloat.

## Mitigaciones: preguntas diferentes

ASLR trata la disposición de direcciones; DEP restringe ejecución desde páginas de datos; CFG controla determinadas transferencias indirectas; SafeSEH se relaciona con manejadores de excepciones en los entornos aplicables. No constituyen un indicador único de “explotable/no explotable”.

Según la [documentación de Microsoft sobre DEP](https://learn.microsoft.com/en-us/windows/win32/memory/data-execution-prevention), el sistema puede marcar páginas como no ejecutables y una ejecución desde ellas puede generar una violación de acceso. Por ello deben distinguirse la declaración del ejecutable, la política efectiva y los permisos de la página concreta. En esta revisión no se han medido esos estados.

## Límites de publicación

El paquete contiene una revisión educativa de un fallo ya público. No incluye shellcode, transmisores de fuzzing, direcciones listas para reutilizar, binarios vulnerables ni un exploit final. Los registros mostrados sirven para interpretar evidencia histórica. No se publica ningún hallazgo nuevo.

No se ha asignado una licencia en nombre del usuario. La autoría y los derechos del material fuente se conservan en [AVISO-DE-USO](../AVISO-DE-USO.md). GitHub público no convierte automáticamente una captura en dominio público ni autoriza a terceros a redistribuirla.

## Cuándo actualizar el recurso

Actualizar si se obtiene el inventario original, una traza causal de la ruta correcta, una referencia nueva o una migración comprobada. Cada ampliación necesita fecha, sesión, archivos y un estado explícito. No borrar las limitaciones históricas sin añadir la evidencia que las resuelve.
