# Cheatsheet comentada: IDA Free

[Índice](../README.md) · [Caso](../docs/03-caso-practico.md)

**Pregunta principal:** ¿cómo llega un dato a una operación relevante?  
**Uso en el caso:** cadenas FTP, referencias, dispatcher y copia.  
**Estado:** acciones descritas por la documentación histórica; no se abrió el binario en esta preparación.

## Ruta de trabajo

| Acción | Operación orientativa | Para qué sirve | Qué conservar |
|---|---|---|---|
| Confirmar carga | Revisar loader PE y arquitectura antes del autoanálisis | Evitar un modo de desensamblado equivocado | Arquitectura, base de imagen y hash externo |
| Abrir cadenas | `View > Open subviews > Strings` | Localizar vocabulario del protocolo | Cadena, ubicación y contexto |
| Seguir una referencia | Seleccionar elemento y abrir referencias cruzadas; habitualmente `X` | Encontrar usos reales | Lista de xrefs y función de destino |
| Saltar a una ubicación | `G`, si está asignado en la instalación | Volver a una posición documentada | Dirección y nombre de función |
| Alternar grafo y texto | `Space`, en la vista de desensamblado | Comparar estructura y detalle | Bloque y salto condicional |
| Decompilar | `F5` si la edición y el servicio lo permiten | Leer una representación de alto nivel | Pseudocódigo junto al ensamblador |
| Nombrar una función | `N` en el contexto adecuado | Sustituir un nombre automático por uno útil | Nombre y justificación |
| Comentar | `;` en el contexto adecuado | Separar dato observado de interpretación | Comentario con etiqueta de confianza |

Los atajos dependen de versión, foco, plataforma y configuración; comprobarlos en el menú de la instalación. La guía fuente cita `Ctrl+X` para referencias. Para una instrucción de equipo, documentar el menú y confirmar el atajo efectivo en lugar de asumir que todas las instalaciones coinciden.

## Cómo leer una copia sin sobreinterpretarla

1. Identificar de dónde procede el puntero origen y si hubo validación previa.
2. Reconstruir el destino: tipo, capacidad, asignación y vida del objeto.
3. Seguir la rama exacta que se pretende explicar.
4. Volver al ensamblador si una inferencia de tipos cambia el significado.
5. Anotar un límite cuando falte información.

Una llamada sin parámetro de tamaño es una pista. No demuestra por sí sola que un destino esté en la pila o que una entrada concreta alcance ese código. El pseudocódigo es una reconstrucción, no el código fuente original.

## Funcionalidad avanzada útil: vistas correlacionadas

El caso muestra desensamblado, pseudocódigo y hexadecimal sincronizados. La combinación permite revisar si una operación inferida en pseudocódigo concuerda con las instrucciones y bytes del bloque. Guardar ubicación y contexto en la nota, porque una captura recortada puede perder los llamadores o la condición que hace accesible la copia.

En E01 la rama observada se relaciona con `USER`. La futura comprobación de `NOOP` requiere una ruta independiente. No renombrar una función como “vulnerable_NOOP_confirmada” a partir de esa sola imagen; un nombre como “dispatcher_ftp_candidato” conserva la incertidumbre.

## Límites y errores frecuentes

- Una cadena sin xrefs no significa que no se use: puede resolverse indirectamente o existir un análisis incompleto.
- Un tipo incorrecto puede dar una falsa impresión de capacidad o de región de memoria.
- La VA del análisis depende de la base elegida. Para cruzar con memoria cargada, registrar módulo y RVA.
- La [página oficial de IDA Free](https://hex-rays.com/ida-free) describe un decompilador en la nube y restricciones de uso comercial. Revisar condiciones antes de cargar material confidencial o trasladar la herramienta a un encargo profesional.
- Si F5 no está disponible, el análisis puede continuar con grafo y ensamblador. No es necesario atribuir pseudocódigo a una edición distinta de la utilizada.

**Salida de calidad:** función candidata, ruta de datos, evidencia visual, hipótesis y validación necesaria. Véase [E01](../evidencias/README.md).
