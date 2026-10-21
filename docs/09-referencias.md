# Referencias

[Volver al índice](../README.md)

Consulta documental: 21 de octubre de 2026. Los enlaces del caso apuntan a un commit concreto para conservar la versión utilizada. La documentación de las herramientas puede actualizarse con el tiempo.

## Enunciado

*Modulo6_TareaColaborativa.pdf*, páginas 4 a 6. Documento de la actividad aportado como referencia. La [memoria](../ENTREGA.md) explica la relación entre sus requisitos y el contenido del repositorio. El PDF no se redistribuye.

## Laboratorio FreeFloat

- [Repositorio del caso](https://github.com/jonbondani/CVE-2025-5548/tree/6c302ee05599ce34dae0892f8678bed802879dab): documentación y capturas de `jonbondani`.
- [Entorno original](https://github.com/jonbondani/CVE-2025-5548/blob/6c302ee05599ce34dae0892f8678bed802879dab/01-Environment/README.md): instalación, VM y snapshot descritos en el laboratorio.
- [Metodología original](https://github.com/jonbondani/CVE-2025-5548/blob/6c302ee05599ce34dae0892f8678bed802879dab/02-Exploitation/README.md): relato de las pruebas y sus resultados.
- [Commit de referencia](https://github.com/jonbondani/CVE-2025-5548/commit/6c302ee05599ce34dae0892f8678bed802879dab): versión del 20 de octubre de 2026.
- [NVD: CVE-2025-5548](https://nvd.nist.gov/vuln/detail/CVE-2025-5548): información pública del producto, versión y relación con `NOOP`.

El [manifiesto de capturas](../evidencias/manifiesto.json) conserva las rutas reales de las imágenes. Algunas referencias del relato original utilizan rutas distintas de las que tienen los archivos en el commit.

## Herramientas

- [IDA Free](https://hex-rays.com/ida-free): capacidades de la edición, requisitos y condiciones de uso.
- [Documentación de Hex-Rays](https://docs.hex-rays.com/): operaciones, vistas y ayuda del producto.
- [mona clásico](https://github.com/corelan/mona): proyecto utilizado en el flujo histórico y aviso de archivo.
- [mona3](https://github.com/corelan/mona3): referencia para evaluar un entorno distinto en futuras sesiones.
- [Ghidra](https://github.com/NationalSecurityAgency/ghidra): proyecto oficial de la alternativa de análisis estático.
- [x64dbg](https://x64dbg.com/): funciones del depurador alternativo para Windows.

Las alternativas se incluyen como orientación. Su presencia en las referencias no significa que se haya repetido el laboratorio con ellas.

## Fundamentos y formatos

- [Python: struct](https://docs.python.org/3/library/struct.html): conversión entre enteros y bytes, tamaños y orden de representación.
- [Python: hashlib](https://docs.python.org/3/library/hashlib.html): cálculo de hashes de archivos y datos.
- [Microsoft: Data Execution Prevention](https://learn.microsoft.com/en-us/windows/win32/memory/data-execution-prevention): permisos de ejecución y política de memoria.
- [GitHub: diagramas Mermaid](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams): soporte de diagramas dentro de Markdown.

## Identificación de los resultados

En el recurso se distingue entre los datos visibles en una captura, las descripciones del laboratorio original y las interpretaciones que se explican a partir de ellos. Las comprobaciones por completar se señalan en el caso práctico. Los ejercicios sintéticos tienen sus propios archivos y resultados en la carpeta `ejemplos`.

Para citar una versión publicada, utiliza autoría, título, fecha, URL del repositorio y commit. Así la referencia permite recuperar los mismos archivos.
