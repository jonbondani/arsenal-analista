# Referencias y procedencia

[Volver al índice](../README.md)

Consulta documental: **21 de octubre de 2026**. Se usan fuentes primarias para capacidades técnicas y un repositorio del usuario para el caso. Los enlaces a documentación viva pueden cambiar; el expediente del caso queda fijado por commit.

## Requisitos académicos

**R01.** *Modulo6_TareaColaborativa.pdf*, documento aportado por el usuario, páginas 4-6: actividad, objetivo, entrega y notas. No se redistribuye el PDF docente. La [matriz](../ENTREGA.md) resume su aplicación sin inventar una rúbrica adicional.

## Caso de laboratorio

**R02.** [Repositorio fuente, versión fijada](https://github.com/jonbondani/CVE-2025-5548/tree/6c302ee05599ce34dae0892f8678bed802879dab), `jonbondani`. Contexto y material histórico.

**R03.** [Entorno original](https://github.com/jonbondani/CVE-2025-5548/blob/6c302ee05599ce34dae0892f8678bed802879dab/01-Environment/README.md). Fuente de las descripciones de Windows, VirtualBox, IDA y snapshot; no acredita por sí sola la configuración efectiva de aislamiento.

**R04.** [Metodología original](https://github.com/jonbondani/CVE-2025-5548/blob/6c302ee05599ce34dae0892f8678bed802879dab/02-Exploitation/README.md). Fuente del relato y resultados históricos; se revisa críticamente en el [caso](03-caso-practico.md). Las rutas históricas de algunas imágenes son inconsistentes con sus archivos: el [manifiesto](../evidencias/manifiesto.json) identifica las rutas reales verificadas.

**R05.** [Commit de referencia](https://github.com/jonbondani/CVE-2025-5548/commit/6c302ee05599ce34dae0892f8678bed802879dab). Fecha documentada: 20-10-2026. Su cambio de estado editorial no sustituye resultados experimentales.

**R06.** [NVD: CVE-2025-5548](https://nvd.nist.gov/vuln/detail/CVE-2025-5548). Referencia externa para producto, versión y relación pública con `NOOP`. Las métricas de riesgo de terceros no se presentan como resultados propios.

## Herramientas y fundamentos

**R07.** [Hex-Rays: IDA Free](https://hex-rays.com/ida-free). Edición, arquitecturas, decompilación y condiciones de uso. Consultar antes de instalar o introducir datos en servicios remotos.

**R08.** [Hex-Rays: documentación](https://docs.hex-rays.com/). Punto de entrada oficial para confirmar operaciones y atajos según versión. Recurso de ampliación; no se utiliza para atribuir una ejecución a esta entrega.

**R09.** [Corelan: mona clásico](https://github.com/corelan/mona). Proyecto histórico y aviso de archivo. El caso fija su propio entorno; el repositorio remite a mona3.

**R10.** [Corelan: mona3](https://github.com/corelan/mona3). Referencia para evaluar una ruta de herramientas distinta en futuras sesiones. No se ha probado una migración del laboratorio.

**R11.** [Python: struct](https://docs.python.org/3/library/struct.html). Orden de bytes, tamaños y conversión entre enteros y bytes.

**R12.** [Python: hashlib](https://docs.python.org/3/library/hashlib.html). Ampliación oficial sobre funciones de hash usadas para integridad local.

**R13.** [Microsoft: Data Execution Prevention](https://learn.microsoft.com/en-us/windows/win32/memory/data-execution-prevention). Referencia para distinguir permisos de ejecución de memoria, política efectiva y atributos del ejecutable.

**R14.** [NSA: Ghidra](https://github.com/NationalSecurityAgency/ghidra). Proyecto oficial de la alternativa estática incluida en la comparación.

**R15.** [x64dbg](https://x64dbg.com/). Capacidades del depurador alternativo de usuario para Windows.

**R16.** [GitHub: diagramas Mermaid](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams). Ampliación para comprobar el renderizado del flujo tras la publicación.

## Cómo citar el recurso después de publicarlo

Usar propietario, título, fecha de la edición, URL real del repositorio y commit de la versión entregada. No se incluye una URL ficticia, DOI, licencia o versión publicada inexistente.

## Convención de atribución interna

- **Observado en captura:** dato visual revisado, con ID E01-E06.
- **Documentado por la fuente:** afirmación del relato original que no se ha reproducido aquí.
- **Interpretación:** razonamiento del recurso con alcance explícito.
- **Propuesta pendiente:** acción que requiere una sesión posterior o información adicional.
- **Sintético comprobado:** comportamiento local de los ejemplos de esta entrega, ajeno a la ejecución de FreeFloat.
