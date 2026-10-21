# Cheatsheet de IDA Free

[Índice](../README.md) · [Caso práctico](../docs/03-caso-practico.md)

## Operaciones habituales

| Operación | Acceso orientativo | Uso |
| :--- | :--- | :--- |
| Revisar la carga | Loader PE y arquitectura | Confirmar el modo de análisis |
| Abrir cadenas | `View > Open subviews > Strings` | Buscar comandos y mensajes |
| Seguir referencias | Referencias cruzadas, habitualmente `X` | Localizar el código que utiliza un elemento |
| Ir a una ubicación | `G` | Volver a una dirección |
| Cambiar grafo y texto | `Space` en el desensamblado | Revisar bloques e instrucciones |
| Abrir pseudocódigo | `F5`, si está disponible | Leer la función decompilada |
| Renombrar | `N` en el contexto adecuado | Sustituir nombres automáticos |
| Comentar | `;` en el contexto adecuado | Anotar una observación junto al código |

Los atajos dependen de la configuración y del foco. La guía original cita `Ctrl+X` para referencias. Comprueba el menú si la combinación no coincide con tu instalación.

## Seguir una entrada FTP

1. Localiza una cadena del protocolo.
2. Abre sus referencias y sigue la función que la utiliza.
3. Revisa la condición de la rama.
4. Sigue el origen y el destino de las copias.
5. Anota las ubicaciones que se van a contrastar en el depurador.

Una copia sin parámetro de tamaño necesita revisar la capacidad del destino y las validaciones anteriores. El nombre de la función de copia no demuestra por sí solo qué entrada llega hasta ella.

## Cruzar las vistas

Mantén desensamblado, pseudocódigo y hexadecimal en la misma ubicación. Comprueba que los cálculos y condiciones reconstruidos corresponden a las instrucciones.

El decompilador puede inferir tipos incorrectos. Si una explicación depende de un puntero, sigue la asignación del objeto y sus llamadores. `this + 28` no determina por sí solo si el destino está en la pila.

En [E01](../evidencias/capturas/E01-ida-copia.png) aparece la rama de `USER`. La ruta `NOOP` necesita revisarse aparte. Al renombrar, utiliza un nombre descriptivo como `dispatcher_ftp_candidato` mientras esa relación siga sin comprobarse.

## Detalles a tener en cuenta

- Una cadena sin referencias visibles puede utilizarse de forma indirecta.
- Guarda función y ubicación, no solo el recorte de una línea.
- Al pasar al depurador, relaciona la dirección con módulo, base y RVA.
- Si F5 no está disponible, continúa con grafo y ensamblador.
- Revisa las [condiciones de IDA Free](https://hex-rays.com/ida-free) antes de cargar muestras confidenciales: su página describe decompilación en la nube.
