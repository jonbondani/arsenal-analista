# Comparativa y selección de herramientas

[Volver al índice](../README.md)

## Criterio de comparación

La comparación se basa en funciones documentadas y en el papel de cada herramienta dentro del caso. No se midieron rendimiento, facilidad de uso o precisión en un benchmark. «Usada en el caso» significa citada o visible en el repositorio fuente; no equivale a una instalación o ejecución nueva durante esta preparación.

| Herramienta | Pregunta que resuelve mejor aquí | Ventaja práctica | Limitación decisiva | Estado en esta entrega |
|---|---|---|---|---|
| IDA Free | ¿Qué rutas y operaciones sugiere el binario? | Grafo, xrefs y vistas correlacionadas | Edición, licencia, arquitectura admitida y decompilación condicionan el uso | Evidencia histórica E01 |
| Immunity Debugger | ¿Qué registros y memoria hay en la detención x86? | Continuidad con las capturas y el plugin del caso | Entorno histórico; no asumir equivalencia con depuración x64 | Evidencias históricas E03-E06 |
| mona clásico | ¿Qué patrón coincide y qué referencia llega intacta? | Automatiza contraste de datos de la sesión | Depende del host y versión; repositorio archivado | Salidas históricas E02 y E05 |
| Python | ¿Se transcribieron y conservaron bien los datos? | Comprobaciones portables y auditables | La calidad depende de la entrada y de la lógica del programa | Utilidad local comprobada |
| Ghidra | ¿Conviene una segunda lectura estática? | Proyecto abierto con desensamblado y decompilación | Importación, tipos y análisis pueden dar otra reconstrucción | Alternativa propuesta, no probada |
| x32dbg/x64dbg | ¿Necesitamos otro depurador de usuario Windows? | Vistas de memoria, hilos y soporte de arquitecturas documentado | Migrar plugins y hábitos requiere validación | Alternativa propuesta, no probada |
| WinDbg con mona3 | ¿Se plantea una plataforma distinta para futuras sesiones? | El proyecto mona3 se orienta a WinDbg/WinDbgX y otros hosts documentados | No asumir instalación, sintaxis ni compatibilidad directa del flujo clásico | Alternativa propuesta, no probada |

Fuentes de capacidades: [IDA Free](https://hex-rays.com/ida-free), [Ghidra](https://github.com/NationalSecurityAgency/ghidra), [x64dbg](https://x64dbg.com/), [mona clásico](https://github.com/corelan/mona), [mona3](https://github.com/corelan/mona3). Fecha de consulta: 21-10-2026.

## Decisiones por escenario

| Escenario | Decisión razonada | Primer control |
|---|---|---|
| Explicar las imágenes existentes | Mantener nomenclatura de IDA, Immunity y mona clásico | Identificar qué imagen respalda cada afirmación |
| Auditar sin ejecutar una muestra | Usar capturas, registro de procedencia y utilidades locales | Comprobar que no se presentan inferencias como reproducciones |
| Abrir un análisis nuevo x86 | Elegir depurador compatible y fijar versiones | Arquitectura y prueba básica del plugin antes de analizar |
| Analizar un proceso x64 | Replantear herramientas y supuestos de memoria | No trasladar EIP, offset o palabras de cuatro bytes |
| Trabajar con un binario confidencial | Revisar licencias y tratamiento de datos | No enviar material a un servicio remoto sin autorización |
| Contrastar una decompilación dudosa | Revisar ensamblador y considerar una segunda herramienta | Comparar la misma función y base, sin votar entre decompiladores |
| Mantener el recurso a medio plazo | Conservar el caso histórico y evaluar una ruta actual aparte | No sustituir instrucciones sin probar y etiquetar la migración |

## Coste total de integración

Una herramienta gratuita puede exigir cuenta, licencia, componentes externos, una VM o mantenimiento de un intérprete histórico. El coste operativo incluye instalar, fijar versiones, validar plugins, preservar artefactos y formar al compañero que leerá la salida.

Para este expediente, cambiar de herramienta antes de interpretar las evidencias existentes aporta poco. Para un laboratorio nuevo, conservar dependencias antiguas sin revisar compatibilidad puede costar más que migrar. La decisión debe registrar qué problema resuelve y qué pruebas de aceptación exige.

## Propuesta de prueba de migración

Antes de declarar un sustituto equivalente: abrir una muestra autorizada con hash conocido, confirmar arquitectura, registrar registros y dump, hacer una comparación local de referencia y comprobar exportación de resultados. Ese pequeño ensayo mide compatibilidad del flujo. Sigue pendiente; aquí no se publica una tabla de tiempos ni de tasas de acierto inventadas.
