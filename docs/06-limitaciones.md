# Limitaciones del análisis

[Volver al índice](../README.md)

## Datos del laboratorio

El caso se revisa a partir de su documentación y capturas. Faltan el binario original identificado por hash, el inventario completo del entorno y las entradas exactas de todas las pruebas. Tampoco está conservado todo el contexto de las detenciones.

Esto afecta a la reproducción y a la relación entre cada entrada y el estado observado. Los ejemplos de Python son pruebas locales con datos sintéticos y no cubren esas carencias del servidor.

## Resultados que necesitan más contexto

| Resultado | Límite |
| :--- | :--- |
| Copia en la rama `USER` | Falta seguir la ruta `NOOP` hasta la operación que corrompe memoria |
| Offset 246 | Se refiere al patrón y al origen de aquella prueba |
| Tabla de 253 bytes sin cambios | Los tres valores excluidos no se compararon |
| EIP sobre `INT3` | No se ve toda la ejecución anterior ni la repetibilidad |
| Dirección de salto | Hay diferencias entre su representación escrita, los bytes y la captura |
| Indicadores de módulos | No describen por sí solos la política efectiva del proceso |

Las comprobaciones concretas están al final del [caso práctico](03-caso-practico.md).

## Pseudocódigo y memoria

IDA reconstruye tipos y expresiones. Una suma a un puntero no determina por sí sola la capacidad del objeto ni si se encuentra en pila o heap. Para confirmarlo hay que seguir la asignación y revisar los llamadores y las instrucciones.

El depurador muestra un instante. La pausa, la continuación y el cambio de hilo pueden afectar al estado observado. La captura debe quedar vinculada con la entrada y la sesión.

## Referencias y comparaciones

mona compara los bytes desde la dirección indicada. Una referencia antigua o un comienzo desplazado puede producir una salida correcta para datos que no corresponden a la prueba.

La utilidad Python tampoco comprueba la procedencia de sus archivos. Detecta diferencias y calcula hashes; la relación con el experimento se guarda en el registro.

## Mitigaciones

La [documentación de Microsoft sobre DEP](https://learn.microsoft.com/en-us/windows/win32/memory/data-execution-prevention) explica el marcado de páginas como no ejecutables. Para interpretar una dirección hay que distinguir atributos del ejecutable, política del proceso y permisos de la página.

No se han comprobado de nuevo esos estados en FreeFloat. ASLR, DEP, CFG y SafeSEH tampoco deben resumirse como una única condición de “explotable” o “no explotable”.

## Repetibilidad

Una dirección observada una vez no queda validada entre reinicios. Hacen falta sesiones independientes con la muestra identificada y un registro de módulo, base y RVA. El resultado de cada repetición debe conservarse, también si cambia respecto a la anterior.
