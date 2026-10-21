# Registro de evidencias y capturas

[Volver al índice](../README.md)

## Procedencia y alcance

Repositorio fuente: [jonbondani/CVE-2025-5548](https://github.com/jonbondani/CVE-2025-5548).  
Commit: [`6c302ee05599ce34dae0892f8678bed802879dab`](https://github.com/jonbondani/CVE-2025-5548/commit/6c302ee05599ce34dae0892f8678bed802879dab).  
Fecha del commit: 20-10-2026. Revisión: 21-10-2026.

Las seis imágenes son copias sin edición de capturas ya presentes en el repositorio del usuario; se renombraron para evitar ambigüedad. Sus identidades de blob Git se consultaron por archivo en el commit citado y se contrastaron con los bytes locales. El [manifiesto](manifiesto.json) contiene ruta original, URL permanente, tamaño, SHA-256 e identidad de blob. El contraste de identidad confirma procedencia de esa versión; no valida cómo se produjo la sesión original.

No se ha repetido el laboratorio. Tampoco se atribuye una fecha experimental a partir de la fecha del commit o de una fecha visible en la interfaz de una herramienta. Los recortes pueden proceder de instantes distintos: no se fusionan como si fueran una traza única.

## Registro de observaciones

| ID | Archivo local | Dato visible o documentado | Qué permite concluir | Qué no demuestra |
|---|---|---|---|---|
| E01 | [IDA: copia](capturas/E01-ida-copia.png) | Pseudocódigo con llamada de copia en la rama descrita como `USER` | Pista estática que merece revisión de capacidad y origen | Causa de la ruta `NOOP`, región real del objeto o ausencia de validación anterior |
| E02 | [Offset 246](capturas/E02-offset-246.png) | Orden `pattern_offset`, valor consultado y posición 246 | Coincidencia en el patrón consultado | Capacidad del buffer o posición universal en todo mensaje FTP |
| E03 | [EIP con marcador](capturas/E03-eip-marcador.png) | EIP `42424242` | Estado compatible con el marcador documentado | Cualquier dirección elegible, privilegios o ejecución de órdenes |
| E04 | [Dump y alineación](capturas/E04-dump-alineacion.png) | Secuencia de bytes visible desde una dirección concreta | Revisar alineación junto al relato fuente | Inicio completo de la tabla en la misma imagen o una regla fija de ESP |
| E05 | [Comparación](capturas/E05-comparacion.png) | Referencia de 253 bytes, tres exclusiones y `Unmodified` | Coincidencia del conjunto comparado en esa prueba | Comportamiento individual de bytes omitidos o de otras rutas |
| E06 | [INT3](capturas/E06-int3.png) | EIP coincide con posición que se decodifica como `INT3` | Estado compatible con la detención descrita | Cadena completa de ejecución, estabilidad entre reinicios o exploit final |

## Enlaces a los originales

- E01: [paso-0/12-pseudocodigo-strcpy.png](https://github.com/jonbondani/CVE-2025-5548/blob/6c302ee05599ce34dae0892f8678bed802879dab/02-Exploitation/images/paso-0/12-pseudocodigo-strcpy.png).
- E02: [paso-2/06-mona-pattern-offset-246.png](https://github.com/jonbondani/CVE-2025-5548/blob/6c302ee05599ce34dae0892f8678bed802879dab/02-Exploitation/images/paso-2/06-mona-pattern-offset-246.png).
- E03: [paso-3/02-eip-42424242.png](https://github.com/jonbondani/CVE-2025-5548/blob/6c302ee05599ce34dae0892f8678bed802879dab/02-Exploitation/images/paso-3/02-eip-42424242.png).
- E04: [paso-4/04-hexdump-offset-esp8.png](https://github.com/jonbondani/CVE-2025-5548/blob/6c302ee05599ce34dae0892f8678bed802879dab/02-Exploitation/images/paso-4/04-hexdump-offset-esp8.png).
- E05: [paso-4/05-mona-compare-unmodified.png](https://github.com/jonbondani/CVE-2025-5548/blob/6c302ee05599ce34dae0892f8678bed802879dab/02-Exploitation/images/paso-4/05-mona-compare-unmodified.png).
- E06: [paso-5/10-eip-sobreescrito-final.png](https://github.com/jonbondani/CVE-2025-5548/blob/6c302ee05599ce34dae0892f8678bed802879dab/02-Exploitation/images/paso-5/10-eip-sobreescrito-final.png).

## Selección y privacidad

Se seleccionan únicamente imágenes necesarias para los objetivos didácticos. No se copia la captura con el código de redirección ni el conjunto completo de instalación, cuenta y configuración. No se han detectado credenciales o tokens en las seis imágenes seleccionadas; contienen direcciones de memoria y contexto de la aplicación del laboratorio. El propietario conserva la revisión contextual final antes de hacer público este nuevo paquete.

No se reconstruyen capturas inexistentes. Las tablas y diagramas del recurso son material explicativo, no salidas originales de herramientas. Los ejemplos de Python son sintéticos y tienen un registro separado en [VALIDACION](../ejemplos/VALIDACION.md).
