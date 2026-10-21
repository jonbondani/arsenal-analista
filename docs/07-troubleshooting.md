# Troubleshooting: diagnosticar sin añadir supuestos

[Volver al índice](../README.md)

| Síntoma | Explicaciones posibles | Comprobación útil | Cuándo darlo por resuelto |
|---|---|---|---|
| No hay respuesta FTP | Proceso pausado, servicio detenido, red o timeout | En laboratorio autorizado, revisar estado del proceso y conectividad básica por separado | Se identifica la causa con evidencia, sin deducir un crash solo por red |
| EIP no coincide con el patrón esperado | Otra entrada, prefijo distinto, otra ruta o sesión mezclada | Comparar patrón exacto, entrada y contexto de la captura | Todos pertenecen a una misma sesión identificada |
| mona no devuelve coincidencia | Valor mal transcrito, modo/longitud diferentes o patrón ajeno | Confirmar representación hexadecimal y archivo de referencia | La coincidencia se valida contra el patrón utilizado, o se marca no encontrada |
| Casi toda la tabla parece modificada | Dirección inicial errónea o referencia antigua | Buscar secuencia inicial y revisar hashes | Se demuestra alineación correcta antes de interpretar diferencias |
| La referencia comienza con `09` en ESP | ESP puede apuntar dentro de la secuencia | Localizar el primer byte y conservar registros del mismo instante | Se documenta el inicio real; no se aplica un ajuste fijo por costumbre |
| `Unmodified`, pero hay dudas sobre bytes excluidos | Esos valores no formaban parte de la referencia | Revisar cómo se generó la tabla | La conclusión limita el conjunto observado |
| El plugin no carga | Versión, host, ruta o intérprete incompatibles | Revisar instalación y ayuda de la versión concreta | Una orden de diagnóstico funciona en el host elegido |
| F5 no genera pseudocódigo | Edición, licencia, servicio o función no disponibles | Revisar condiciones y continuar en ensamblador cuando proceda | Se identifica la limitación sin atribuir capacidades no presentes |
| Una VA cambia | ASLR, otra versión, otra base o sesión | Comparar módulo, base y RVA | Se explica el cambio con inventario, no con direcciones sueltas |
| Aparece `INT3` sin el resultado esperado | Breakpoint del depurador, dato ya presente o ruta distinta | Revisar origen del breakpoint y contexto previo | Se sabe quién insertó la interrupción y en qué sesión |
| Hash distinto en una captura | Copia distinta, edición, corrupción o conversión | Volver al origen y comparar tamaño y bytes | Se registra la diferencia; no se cambia el manifiesto para ocultarla |
| `compare` devuelve 1 | Los ejemplos difieren deliberadamente o existe una diferencia real | Leer longitudes y primer índice | Se clasifica como resultado, no como fallo de instalación |
| `compare` devuelve 2 | Formato no hexadecimal, archivo ilegible o demasiado grande | Usar solo pares hexadecimales y espacios | Entrada válida y resultado interpretable |
| Mermaid no se ve | Visor sin soporte o sintaxis no admitida | Abrir Markdown en GitHub; consultar la tabla de fases | Se conserva una explicación textual legible |

## Procedimiento para una comparación sospechosa

1. Detener cambios y guardar el resultado inicial.
2. Confirmar referencia, hash y longitud.
3. Localizar manualmente el inicio real de la secuencia.
4. Repetir solo la comparación en el estado autorizado, sin cambiar varias variables.
5. Comparar las dos salidas y anotar qué cambió.
6. Si falta el estado original, marcar la explicación como hipótesis y diseñar una sesión nueva.

No “reparar” una captura existente ni editar una salida para hacerla coincidir. Si solo se dispone de imágenes, puede identificarse la duda, pero quizá no resolverse.

## Cómo pedir ayuda de forma útil

Compartir versión de herramientas, arquitectura, orden exacta, resultado resumido y un recorte público revisado. Evitar dumps, tokens, rutas personales o direcciones ajenas innecesarias. Indicar qué ya se comprobó y qué variable se está intentando aislar. Usar la [ficha de sesión](../plantillas/sesion.md) como base reduce intercambios ambiguos.
