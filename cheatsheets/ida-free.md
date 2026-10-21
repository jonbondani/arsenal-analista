# Cheatsheet de IDA Free

[Índice](../README.md) · [Caso práctico](../docs/03-caso-practico.md)

IDA permite estudiar las funciones y seguir el recorrido de un dato por el binario. En el caso de FreeFloat se utiliza para localizar cadenas FTP, seguir sus referencias y revisar las operaciones de copia.

## Operaciones habituales

| Operación | Acceso orientativo | Uso |
| :--- | :--- | :--- |
| Revisar la carga | Loader PE y arquitectura | Confirmar el modo de análisis antes de continuar |
| Abrir cadenas | `View > Open subviews > Strings` | Localizar nombres de comandos y mensajes |
| Seguir referencias | Menú de referencias cruzadas, habitualmente `X` | Encontrar el código que utiliza un elemento |
| Ir a una ubicación | `G` | Volver a una dirección anotada |
| Cambiar entre grafo y texto | `Space` en la vista de desensamblado | Leer la estructura y el detalle de un bloque |
| Abrir pseudocódigo | `F5`, si está disponible | Seguir la lógica con una representación de alto nivel |
| Renombrar | `N` en el contexto adecuado | Sustituir nombres automáticos por otros descriptivos |
| Comentar | `;` en el contexto adecuado | Guardar observaciones junto al código |

Los atajos pueden cambiar según versión, plataforma, foco y configuración. La guía original cita `Ctrl+X` para referencias. Si la combinación no coincide con tu instalación, utiliza el menú y comprueba el atajo asignado.

## Seguir una entrada

1. Localiza una cadena del protocolo o un mensaje relacionado con la operación.
2. Abre sus referencias y sitúa la función que la utiliza.
3. Revisa la condición de la rama y la procedencia del dato.
4. Sigue las llamadas y los destinos de las copias.
5. Anota la ubicación y el contexto que necesitarás contrastar en ejecución.

Una llamada de copia sin parámetro de tamaño merece atención. Para valorar el riesgo también hay que conocer la capacidad del destino y las validaciones previas.

## Trabajar con varias vistas

El caso muestra desensamblado, pseudocódigo y hexadecimal sincronizados. Esta combinación ayuda a comprobar si la operación reconstruida corresponde a las instrucciones del bloque.

El pseudocódigo puede sugerir tipos y nombres que necesitan corregirse. Si una conclusión depende de un cálculo de punteros, vuelve al ensamblador y sigue la asignación del objeto. Una expresión como `this + 28` no determina por sí sola la región de memoria donde vive el destino.

En [E01](../evidencias/capturas/E01-ida-copia.png) se estudia la rama asociada a `USER`. La explicación de `NOOP` necesita seguir su propia ruta. Un nombre como `dispatcher_ftp_candidato` ayuda a describir el papel de la función sin dar por confirmada una relación que aún se está revisando.

## Notas prácticas

- Guarda función, dirección y contexto junto a cada observación.
- Una cadena sin referencias visibles puede usarse indirectamente o requerir más análisis.
- Al pasar al depurador, relaciona la ubicación con módulo, base y RVA.
- Si F5 no está disponible, continúa con el grafo y el ensamblador.
- Revisa las [condiciones de IDA Free](https://hex-rays.com/ida-free) antes de trabajar con material confidencial o comercial. La página oficial describe decompilación en la nube.
