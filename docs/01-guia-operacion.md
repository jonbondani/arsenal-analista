# Guía de operación para incorporarse al análisis

[Volver al índice](../README.md)

## 1. Definir una pregunta que pueda responderse

Una sesión útil comienza con una pregunta concreta: «¿Qué parte del estado del proceso relaciona esta entrada con el crash?». Evita comenzar con «conseguir ejecución de código», porque mezcla objetivos distintos y favorece afirmar más de lo que muestran las capturas. En esta entrega el objetivo es revisar evidencias existentes de un caso público y aprender a documentar resultados.

El responsable del análisis delimita artefactos permitidos, sistema autorizado, ventana de trabajo, condiciones de parada y destino de los resultados. Si solo se revisa este paquete, no hace falta ejecutar el servicio. Para una futura sesión dinámica, usar exclusivamente una VM autorizada, desechable, con snapshot y red interna o host-only sin exposición a Internet. Registrar la topología real; tener una VM no garantiza aislamiento.

## 2. Crear el expediente antes de abrir herramientas

Duplica la [ficha de sesión](../plantillas/sesion.md) y asigna un identificador. Anota zona horaria, origen, SHA-256 de cada binario o dump, arquitectura del proceso, versión de Windows, snapshot, versiones de las herramientas y del plugin. Una dirección sin módulo y una captura sin sesión pierden valor rápidamente.

Ejemplo de inventario pendiente para el caso original:

| Dato | Lo que existe | Lo que debe registrarse en otra sesión |
|---|---|---|
| Software | FreeFloat FTP Server 1.0 según el repositorio | Hash del ejecutable concreto |
| Arquitectura | PE 80386 descrito por el caso | Confirmación de cabecera PE y modo del depurador |
| Sistema | Windows 11 y VirtualBox documentados | Build, configuración de VM y mitigaciones efectivas |
| IDA | La guía fuente menciona IDA Free 9.4 para Windows x64 | Versión de instalación, licencia y modo de decompilación |
| Immunity y mona | Visibles o citados en el laboratorio | Versiones y hashes; intérprete embebido y configuración |
| Python externo | Scripts descritos como Python 3 | Versión, hash de cada script y entradas exactas |

Windows x64 y una aplicación x86 pueden coexistir. El tamaño de palabra que interesa para interpretar EIP es el del proceso objetivo. El Python usado para utilidades externas tampoco equivale al intérprete que carga un plugin dentro del depurador.

## 3. Elegir herramientas por pregunta

| Pregunta | Herramienta principal | Artefacto de salida |
|---|---|---|
| ¿Qué bloques procesan una cadena? | IDA Free | Función, xrefs, grafo y nota de hipótesis |
| ¿Qué estado existe al detenerse el proceso? | Immunity Debugger | Tipo de excepción, hilo, registros, pila y memoria |
| ¿Coinciden estos bytes con una referencia? | mona | Comando exacto, archivo de referencia y resultado |
| ¿Se copió bien una dirección o un archivo? | Python | Comparación explícita, hash y salida local |
| ¿Qué demuestra todo ello? | Revisión del analista | Informe con hechos, hipótesis y límites |

IDA reduce el espacio de búsqueda; Immunity muestra un estado concreto; mona automatiza comprobaciones repetitivas; Python ayuda a evitar errores de representación y a conservar integridad. Ninguna herramienta sustituye el enlace causal entre entrada y efecto.

## 4. Trabajar con puntos de control

Antes de interpretar un crash, registra qué proceso está detenido y si la excepción es de lectura, escritura, ejecución u otro tipo. No infieras un crash a partir de un timeout de red. Antes de comparar memoria, localiza la secuencia inicial y confirma cuántos bytes se van a leer. Antes de usar una dirección, separa VA, RVA y offset de archivo.

Si se cambia de binario, de ruta del protocolo, de prefijo, de versión del sistema o de snapshot, abre una nueva sesión. No mezcles resultados de configuraciones distintas para completar una explicación que ninguna de ellas demuestra por separado.

## 5. Preservar y transferir conocimiento

Guarda las capturas originales y su hash local. Si hay que redactar datos, conserva el original fuera del repositorio, crea una copia pública identificada como editada y registra la transformación. La copia pública debe conservar el contexto técnico necesario sin incluir secretos. Esta entrega selecciona capturas ya públicas y no contiene dumps completos.

Cada hallazgo debe poder expresarse así: «En E05, la referencia de 253 bytes produjo `Unmodified` en una dirección concreta. Esto apoya que los bytes comparados llegaron sin cambios en esa prueba. No demuestra el comportamiento de los bytes omitidos». Esa frase es más útil para el compañero que una casilla genérica de “badchars completado”.

## 6. Cerrar la sesión

Completa el [checklist](08-checklist.md), actualiza el [informe](../plantillas/informe.md) y deja una tarea pendiente con condición de aceptación para cada incógnita. Una tarea como «comprobar ASLR» es demasiado ambigua; «registrar módulo, base y RVA en sesiones independientes con reinicio y comparar resultados» permite saber cuándo se ha completado.

No hace falta alcanzar ejecución arbitraria para cerrar un análisis documental valioso. El cierre requiere una conclusión proporcional, trazabilidad y una explicación de lo que falta.
