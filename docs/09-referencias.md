# Referencias

[Volver al índice](../README.md)

## Laboratorio FreeFloat

- [Repo del caso](https://github.com/jonbondani/CVE-2025-5548/tree/6c302ee05599ce34dae0892f8678bed802879dab): documentación y capturas de `jonbondani`.
- [Entorno](https://github.com/jonbondani/CVE-2025-5548/blob/6c302ee05599ce34dae0892f8678bed802879dab/01-Environment/README.md): VM, instalación y snapshot.
- [Metodología original](https://github.com/jonbondani/CVE-2025-5548/blob/6c302ee05599ce34dae0892f8678bed802879dab/02-Exploitation/README.md): pasos y resultados del laboratorio.
- [Commit de referencia](https://github.com/jonbondani/CVE-2025-5548/commit/6c302ee05599ce34dae0892f8678bed802879dab): versión del 20 de octubre de 2026.
- [NVD: CVE-2025-5548](https://nvd.nist.gov/vuln/detail/CVE-2025-5548): producto, versión y relación pública con `NOOP`.

Las rutas de las seis capturas están en el [registro de evidencias](../evidencias/README.md) y en el [manifiesto](../evidencias/manifiesto.json).

## Herramientas

- [IDA Free](https://hex-rays.com/ida-free): edición, requisitos y condiciones de uso.
- [Documentación de Hex-Rays](https://docs.hex-rays.com/): operaciones y vistas de IDA.
- [mona clásico](https://github.com/corelan/mona): proyecto del flujo histórico y aviso de archivo.
- [mona3](https://github.com/corelan/mona3): requisitos y hosts del proyecto actual.
- [Ghidra](https://github.com/NationalSecurityAgency/ghidra): alternativa para análisis estático.
- [x64dbg](https://x64dbg.com/): depuración de usuario en Windows.

## Memoria y representación de datos

- [Python: struct](https://docs.python.org/3/library/struct.html): conversión entre enteros y bytes, orden y tamaños.
- [Python: hashlib](https://docs.python.org/3/library/hashlib.html): cálculo de hashes.
- [Microsoft: DEP](https://learn.microsoft.com/en-us/windows/win32/memory/data-execution-prevention): ejecución desde páginas de memoria.
- [GitHub: Mermaid](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams): diagramas dentro de Markdown.

Documentación consultada el 21 de octubre de 2026. Los enlaces del laboratorio apuntan al commit utilizado; la documentación de las herramientas puede actualizarse.
