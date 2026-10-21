# Alcance y limitaciones

[Volver al índice](../README.md)

## Información disponible

El recurso parte de la documentación y las capturas del laboratorio. La revisión permite explicar resultados y señalar los datos necesarios para repetirlos, pero no sustituye una sesión con el binario original.

En el material consultado faltan el hash del ejecutable, el inventario completo de herramientas y parte del contexto de las detenciones. Tampoco se conservan aquí las entradas exactas de todas las pruebas. Por eso la relación entre el dato enviado y el estado del proceso se apoya en el relato y las imágenes disponibles.

Las pruebas nuevas registradas en el repositorio corresponden a la utilidad local de Python. Utilizan datos sintéticos y están separadas de las evidencias de FreeFloat.

## Límites del caso

| Aspecto | Alcance de la evidencia |
| :--- | :--- |
| Copia observada en `USER` | Permite estudiar una operación candidata, pero la ruta `NOOP` necesita su propio seguimiento |
| Coincidencia en el offset 246 | Se refiere al patrón y al contexto documentados |
| Tabla de 253 bytes sin cambios | Valida la referencia comparada; no evalúa los tres valores excluidos |
| Captura con `INT3` | Muestra una detención compatible con el relato, sin reconstruir toda la ejecución previa |
| Direcciones del ejemplo | Presentan diferencias de representación que deben resolverse antes de reutilizarlas |
| Estabilidad entre sesiones | No queda acreditada sin comprobaciones tras reiniciar |
| Indicadores de módulos | No describen por sí solos todas las mitigaciones efectivas del proceso |

El [caso práctico](03-caso-practico.md) desarrolla cada punto y enumera las comprobaciones que permitirían completar el análisis.

## Interpretación de las herramientas

El pseudocódigo de IDA es una reconstrucción. Los tipos, nombres y expresiones pueden necesitar correcciones. Cuando una conclusión depende de la capacidad de un objeto o de su ubicación en memoria, hay que seguir también sus llamadores y revisar el ensamblador.

El depurador muestra un instante concreto. Pausar o continuar puede cambiar el estado y los tiempos del proceso. Una captura necesita su sesión, entrada y contexto para poder interpretarse con precisión.

mona automatiza comparaciones, pero trabaja sobre la dirección y la referencia que recibe. Un resultado correcto puede corresponder a una referencia equivocada o a otra sesión. El repositorio clásico está archivado; la migración a mona3 requiere una revisión independiente.

Python ayuda a comparar e identificar archivos. La utilidad incluida no conoce su procedencia ni decide si una referencia representa bien la prueba. Esa parte debe quedar explicada en el registro del análisis.

## Mitigaciones

ASLR, DEP, CFG y SafeSEH tienen funciones distintas. La presencia o ausencia de un indicador no resume la seguridad completa del proceso.

La [documentación de Microsoft sobre DEP](https://learn.microsoft.com/en-us/windows/win32/memory/data-execution-prevention) explica que el sistema puede marcar páginas como no ejecutables. Por eso conviene distinguir la declaración del ejecutable, la política efectiva y los permisos de la página que se está estudiando. Esos estados no se han medido de nuevo para esta guía.

## Uso y publicación

El contenido se limita a un fallo ya público, sus evidencias y ejercicios locales. Los binarios, dumps privados, credenciales y payloads finales quedan fuera del repositorio.

Las capturas mantienen su atribución. Los derechos y condiciones de reutilización se describen en el [aviso de uso](../AVISO-DE-USO.md).

Si se añade una prueba, conviene registrar fecha, sesión, archivos y resultado. Una limitación se puede dar por resuelta cuando se incorpora la evidencia correspondiente. Así se conserva la continuidad entre la documentación original y las ampliaciones posteriores.
