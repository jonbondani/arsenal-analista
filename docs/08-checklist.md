# Checklist de análisis

[Volver al índice](../README.md)

## Antes de empezar

- [ ] Definir la prueba y confirmar el alcance autorizado.
- [ ] Comprobar el aislamiento de red y guardar un snapshot.
- [ ] Registrar origen, hash y arquitectura del ejecutable.
- [ ] Anotar sistema, depurador, IDA, plugin e intérpretes con sus versiones.
- [ ] Guardar la entrada y la referencia que se van a utilizar.

## Durante la prueba

- [ ] Registrar la acción anterior a la detención.
- [ ] Guardar proceso, hilo, excepción, registros y memoria de la misma sesión.
- [ ] Indicar desde dónde se cuenta el offset y si el índice empieza en cero.
- [ ] Localizar el primer byte antes de comparar memoria.
- [ ] Comprobar longitud y hash de la referencia.
- [ ] Anotar exclusiones y el motivo de cada una.
- [ ] Identificar módulo, base y RVA de las direcciones relevantes.
- [ ] Distinguir atributos del ejecutable y mitigaciones efectivas.
- [ ] Conservar el estado antes de continuar o cambiar la configuración.

## Al terminar

- [ ] Relacionar cada conclusión con una captura o archivo.
- [ ] Separar observaciones, interpretaciones y comprobaciones que faltan.
- [ ] Registrar cambios de configuración entre pruebas.
- [ ] Guardar también los resultados que no coincidan con lo esperado.
- [ ] Revisar los datos que se van a compartir y conservar los originales.

La [ficha de sesión](../plantillas/sesion.md) y la [plantilla de informe](../plantillas/informe.md) sirven para guardar esta información.
