# Memoria de la actividad

## Tema y objetivo

**Actividad:** El Arsenal de un Analista. Módulo 6, Vulnerabilidades.

El trabajo reúne una guía práctica de IDA Free, Immunity Debugger, mona y Python a partir del [laboratorio de CVE-2025-5548](https://github.com/jonbondani/CVE-2025-5548). El objetivo es explicar cómo se combinan estas herramientas al analizar un fallo de memoria, cómo se interpretan sus resultados y qué información conviene conservar para documentar el trabajo.

La documentación está en castellano y utiliza Markdown, diagramas Mermaid, capturas del laboratorio y ejemplos locales. La publicación se realiza manualmente en GitHub y la URL se comunica al presentar la actividad.

## Relación con el enunciado

Las páginas 4 a 6 de *Modulo6_TareaColaborativa.pdf* plantean la creación de un recurso técnico útil para otros analistas. Se pide aplicar una o varias herramientas, integrarlas en una metodología y explicar sus posibilidades y limitaciones. Entre los formatos sugeridos aparecen las cheatsheets, los flujos visuales y las guías de operación.

El recurso combina esos tres formatos. La organización permite leer el caso completo o acudir directamente a una ficha para consultar una operación concreta.

La página 5 orienta el trabajo al portfolio profesional y establece su publicación en un proyecto público de GitHub. La página 6 recomienda Markdown, admite castellano o inglés y permite trabajo individual o grupal. También indica que las variaciones del enunciado deben validarse previamente y que esta actividad representa un 20 % de la nota final del módulo.

## Contenido que cubre cada requisito

| Requisito | Apartado |
| :--- | :--- |
| Aplicación práctica de las herramientas | [Guía de operación](docs/01-guia-operacion.md) y [caso FreeFloat](docs/03-caso-practico.md) |
| Cheatsheets con operaciones comentadas | [IDA](cheatsheets/ida-free.md), [Immunity](cheatsheets/immunity-debugger.md), [mona](cheatsheets/mona.md) y [Python](cheatsheets/python.md) |
| Flujo visual de análisis | [Metodología con Mermaid](docs/02-metodologia.md) |
| Capturas y explicación de resultados | [Registro de evidencias](evidencias/README.md) |
| Comparación y limitaciones | [Comparativa](docs/05-comparativa.md) y [alcance](docs/06-limitaciones.md) |
| Utilidad para otros analistas | [Tutorial](docs/04-tutorial-local.md), [resolución de problemas](docs/07-troubleshooting.md) y [checklist](docs/08-checklist.md) |
| Documentación reutilizable | [Ficha de sesión](plantillas/sesion.md) y [plantilla de informe](plantillas/informe.md) |
| Publicación y envío de la URL | [Guía de publicación](docs/10-publicacion.md) |

Esta relación sirve para localizar el contenido. El enunciado no reparte puntos por apartado, por lo que la tabla no representa una rúbrica de calificación.

## Desarrollo del trabajo

El punto de partida es el análisis de FreeFloat ya recogido en el repositorio. A partir de sus capturas se explican tareas habituales: seguir referencias en IDA, interpretar EIP y ESP, localizar una secuencia con mona y comparar bytes desde una dirección bien identificada.

El caso también permite revisar errores de interpretación. La copia observada en la rama de `USER` no basta para explicar el fallo asociado a `NOOP`; el offset 246 necesita un origen; y el resultado `Unmodified` solo se aplica a la referencia comparada. Estas precisiones forman parte de la explicación técnica.

Los ejercicios de Python se centran en orden de bytes, comparación e integridad. Utilizan datos sintéticos y pueden ejecutarse sin el servidor vulnerable. Sus resultados están registrados aparte para no mezclarlos con las pruebas del laboratorio original.

## Alcance de las pruebas

Se revisaron la documentación y las capturas del repositorio. También se ejecutaron los ejemplos locales y se comprobaron enlaces, hashes y contenido del ZIP.

La ejecución de FreeFloat no se repitió durante la elaboración de esta guía. El recurso conserva esa diferencia y no presenta como terminadas las comprobaciones que faltan en el caso original.

## Revisión antes del envío

1. Confirmar los datos de autoría y, si corresponde, los participantes del grupo.
2. Comprobar que las herramientas elegidas encajan con el manual del módulo.
3. Revisar la [lista de entrega](docs/08-checklist.md).
4. Publicar los archivos en GitHub y comprobar su acceso público.
5. Revisar imágenes, enlaces y diagramas desde el repositorio.
6. Enviar la URL y conservar una copia de la versión presentada.

El PDF docente se utiliza como referencia del enunciado y no forma parte de los archivos que se publican.
