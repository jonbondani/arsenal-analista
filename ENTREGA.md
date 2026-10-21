# Memoria de entrega y cobertura del enunciado

## Identificación

**Actividad:** El Arsenal de un Analista. Módulo 6, Vulnerabilidades.  
**Tema:** integración de IDA Free, Immunity Debugger, mona y Python para analizar evidencias de un buffer overflow FTP conocido.  
**Referencia de autoría del caso:** perfil público `jonbondani`; no se asignan nombres de participantes ni se inventa reparto de trabajo.  
**Formato:** repositorio documental en español, Markdown con Mermaid, capturas existentes, plantillas y ejercicios locales.  
**Estado:** preparado para revisión y publicación; sin URL nueva de entrega porque no se ha autorizado publicar.

## Interpretación de las páginas 4-6

La página 4 pide un recurso técnico profesional sobre una o varias herramientas del arsenal del módulo, aplicado a casos reales e integrado en una metodología, con posibilidades y limitaciones. Cheatsheet, flujo visual y guía operativa aparecen como propuestas: este recurso combina las tres.

La página 5 orienta el resultado al trabajo cotidiano y al portfolio, con criterio propio, uso práctico y profundidad. Exige crear un proyecto público en GitHub, subir el recurso estructurado y comunicar posteriormente su URL. No exige producir un PDF adicional ni completar una cadena de explotación.

La página 6 permite trabajo individual o grupal, recomienda Markdown, admite castellano o inglés y exige validación previa si se introducen variaciones del enunciado. Indica una ponderación del 20 % para esta actividad. No contiene una rúbrica numérica por apartado: la matriz siguiente es una comprobación de cobertura, no una promesa de calificación.

## Matriz de trazabilidad

| Página | Requisito o criterio | Evidencia en la entrega | Estado |
|---|---|---|---|
| 4 | Aplicación profesional de una o varias herramientas | [Guía operativa](docs/01-guia-operacion.md) y [cuatro cheatsheets](cheatsheets/mona.md) | Cubierto documentalmente |
| 4 | Caso práctico | [Caso FreeFloat](docs/03-caso-practico.md), capturas E01-E06 | Evidencias históricas revisadas; sin nueva reproducción |
| 4 | Integración en metodología | [Flujos Mermaid y puntos de control](docs/02-metodologia.md) | Incluido |
| 4 | Posibilidades y limitaciones frente a otras | [Comparativa](docs/05-comparativa.md) y [límites](docs/06-limitaciones.md) | Incluido; alternativas no probadas |
| 4 | Comandos, explicación propia y capturas | [mona](cheatsheets/mona.md), [IDA](cheatsheets/ida-free.md) y [registro](evidencias/README.md) | Incluido con contexto y reservas |
| 4 | Ayudar a nuevos analistas | [Operación](docs/01-guia-operacion.md), [troubleshooting](docs/07-troubleshooting.md), [checklist](docs/08-checklist.md) | Incluido |
| 5 | Criterio técnico y profundidad | Revisión de causalidad, alineación, endianness y mitigaciones en el [caso](docs/03-caso-practico.md) | Incluido |
| 5 | Utilidad y portfolio | [Tutorial sin red](docs/04-tutorial-local.md) y [plantilla de informe](plantillas/informe.md) | Incluido |
| 5 | Proyecto público y URL | [Plan de publicación](docs/10-publicacion.md) | **Pendiente de autorización y ejecución** |
| 6 | Markdown e idioma admitido | Archivos Markdown en castellano | Cubierto |
| 6 | Participantes | No se atribuyen contribuciones inexistentes | El propietario declarará participantes al enviar |
| 6 | Validar previamente cambios del enunciado | Se mantiene la actividad como recurso sobre herramientas | No se propone una variación; si el docente discrepa, consultar antes del envío |

El manual completo del módulo no fue aportado: se parte de las herramientas indicadas por el usuario y del caso del repositorio. Antes del envío, el propietario debe confirmar que encajan en el arsenal tratado en clase.

## Aportación técnica

El recurso aporta una disciplina de análisis: cada conclusión necesita una observación, una procedencia y un límite. Se enseña a usar la sincronización entre vistas de IDA, a interpretar coincidencias de mona y a comprobar manualmente la dirección inicial de una comparación. El tutorial demuestra con datos sintéticos por qué una alineación equivocada genera diagnósticos falsos y por qué una representación de cuatro bytes requiere orden explícito.

No se atribuye al autor una nueva ejecución del laboratorio. Se reutiliza su documentación pública y se amplía con interpretación, metodología y utilidades de revisión. El material nuevo está etiquetado como propuesta, práctica sintética o verificación documental.

## Texto preparado para la plataforma docente

> Presento «El Arsenal de un Analista: de una captura de crash a una conclusión defendible», un recurso técnico sobre IDA Free, Immunity Debugger, mona y Python. A partir de mi repositorio público de laboratorio CVE-2025-5548, reúne metodología visual, cheatsheets comentadas, análisis crítico de evidencias, comparativa, troubleshooting y ejercicios locales sin red. Se diferencian los resultados documentados de las comprobaciones pendientes; no se afirma una reproducción nueva ni un exploit final validado. La URL del proyecto público se añadirá tras su publicación autorizada.

Este texto es un borrador listo para adaptar al envío. Sustituir la última frase por la URL real solo cuando exista y se haya verificado su acceso público.

## Cierre antes de enviar

1. Revisar identidad y participantes reales.
2. Confirmar adecuación de herramientas al manual del módulo.
3. Completar la revisión de derechos y privacidad del [checklist](docs/08-checklist.md).
4. Autorizar y realizar la publicación siguiendo el [plan](docs/10-publicacion.md).
5. Verificar enlaces y Mermaid en el repositorio público.
6. Comunicar la URL definitiva y conservar el ZIP de la versión entregada.

No se incluye el PDF docente en el repositorio público. Se utilizó únicamente como fuente de requisitos, páginas 4-6.
