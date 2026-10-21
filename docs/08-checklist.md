# Checklist de análisis y entrega

[Volver al índice](../README.md)

## A. Preparación del recurso: comprobación de esta edición

- [x] Páginas 4-6 del PDF original consultadas y matriz de cobertura redactada.
- [x] Repositorio fuente leído sin modificación remota.
- [x] Versión de referencia identificada mediante commit.
- [x] Capturas seleccionadas revisadas visualmente y atribuidas.
- [x] Hechos históricos separados de hipótesis y comprobaciones pendientes.
- [x] Cheatsheets, flujo Mermaid, caso, tutorial y comparativa incluidos.
- [x] Limitaciones y troubleshooting incluidos.
- [x] Ejemplos locales sintéticos incluidos y comprobados; ver [validación](../ejemplos/VALIDACION.md).
- [x] Sin binarios vulnerables ni scripts de explotación en el paquete.
- [x] Sin publicación ni modificación del repositorio remoto.

La validación mecánica de enlaces y hashes se registra en [VALIDACION](../ejemplos/VALIDACION.md). Esta lista no certifica el laboratorio original.

## B. Checklist reutilizable para una nueva sesión

Estas casillas están vacías porque son una plantilla para quien realice la sesión.

- [ ] Alcance y autorización registrados.
- [ ] Topología de aislamiento y snapshot comprobados.
- [ ] Hash, procedencia y arquitectura de la muestra anotados.
- [ ] Versiones de SO, depurador, IDA, plugin e intérpretes anotadas.
- [ ] Pregunta de análisis y criterio de aceptación definidos.
- [ ] Entrada o referencia exacta conservada con hash.
- [ ] Excepción, hilo, registros y memoria corresponden a la misma sesión.
- [ ] Offset definido respecto a un origen y una convención de índices.
- [ ] Dirección inicial de comparación verificada en el dump.
- [ ] Exclusiones distinguidas de fallos demostrados.
- [ ] Módulos, bases y RVA usados donde corresponde.
- [ ] Atributos PE separados de mitigaciones efectivas.
- [ ] Conclusiones redactadas con evidencias y límites.
- [ ] Propuestas pendientes tienen condición de aceptación.

## C. Revisión del propietario antes de publicar y enviar

- [ ] Confirmar participantes reales y herramientas del temario.
- [ ] Revisar que la selección de capturas propias puede publicarse con su atribución.
- [ ] Revisar privacidad contextual: nombres, rutas, direcciones y contenido visible.
- [ ] Decidir derechos/licencia del material propio sin relicenciar material ajeno.
- [ ] Confirmar destino: repositorio nuevo o integración en uno existente.
- [ ] Autorizar expresamente la publicación o modificación remota.
- [ ] Publicar y abrir la URL en una ventana sin autenticación.
- [ ] Verificar renderizado de Markdown, imágenes y Mermaid en GitHub.
- [ ] Verificar que el ZIP corresponde a la versión publicada.
- [ ] Sustituir la frase pendiente del texto docente por la URL real y enviar.

La sección C no se marca como completada por haber preparado este paquete. El usuario pidió reservar la publicación para una confirmación posterior.
