# Cheatsheet comentada: mona clásico

[Índice](../README.md) · [Registro de evidencias](../evidencias/README.md)

**Pregunta principal:** ¿coincide esta referencia con el estado observado?  
**Alcance:** órdenes de revisión y preparación local presentes en la metodología histórica. No incluye búsqueda de gadgets ni construcción de payloads.

El repositorio [corelan/mona](https://github.com/corelan/mona) está archivado y remite a [mona3](https://github.com/corelan/mona3). Esta ficha conserva la sintaxis histórica para comprender el caso. No afirma compatibilidad directa con mona3, WinDbg o una instalación actual; verificar ayuda y versión antes de emplearla.

## Comandos y criterios

### Aislar la salida de una sesión

```text
!mona config -set workingfolder C:\Mona\sesion_revision
```

**Para qué:** separar tablas, patrones e informes de distintas sesiones.  
**Guardar:** ruta efectiva, versión del plugin y archivos producidos.  
**Evitar:** reutilizar una referencia antigua por haber mantenido la misma carpeta. La configuración cambia el directorio de salida y debe hacerse solo dentro del entorno autorizado.

### Crear una referencia de patrón local

```text
!mona pattern_create 400
```

**Para qué:** generar un patrón identificable de la longitud documentada por la fuente.  
**Guardar:** archivo exacto, longitud, hash y convención del offset.  
**Límite:** generar el patrón no demuestra que se enviara, que alcanzara la función ni que produjera un crash. Esta entrega no incluye un transmisor de entradas.

### Consultar un valor histórico

```text
!mona pattern_offset 41326941
```

**Para qué:** ubicar la secuencia correspondiente al valor leído en EIP, según el patrón y modo utilizados.  
**Evidencia:** E02 devuelve posición 246.  
**Evitar:** escribir el valor como texto decimal o invertir bytes manualmente sin entender cómo los interpreta la orden. Conservar la salida completa y contrastarla con la referencia real.

### Generar una tabla con exclusiones declaradas

```text
!mona bytearray -b "\x00\x0a\x0d"
```

**Para qué:** crear la referencia de 253 bytes descrita en el caso.  
**Flag:** `-b` declara bytes excluidos.  
**Límite:** excluir un byte es una decisión de la prueba; no demuestra que ese byte haya fallado. Registrar si la exclusión se basa en protocolo, hipótesis o una observación anterior.

### Comparar desde una dirección comprobada

```text
!mona compare -f C:\Mona\sesion_revision\bytearray.bin -a DIRECCION_VERIFICADA
```

`DIRECCION_VERIFICADA` es un marcador documental, no un argumento literal válido. Sustituirlo por la dirección del primer byte de la tabla, observada en la sesión actual.

**Flags:** `-f` identifica la referencia y `-a` la dirección inicial.  
**Guardar:** hash y longitud de la referencia, dirección, registros del mismo instante y salida.  
**Interpretar:** `Unmodified` solo corresponde a esa referencia y ubicación. En la fuente se usó una dirección descrita como ESP menos ocho; no copiar ese ajuste automáticamente.

### Revisar módulos

```text
!mona modules
```

**Para qué:** inventariar módulos y atributos que la herramienta presenta.  
**Guardar:** módulo, versión o hash cuando se disponga, base y sesión.  
**Límite:** los indicadores del módulo no son una evaluación completa de la política efectiva del proceso. No convertir `NXCompat = False` en “DEP desactivado” ni un resultado aislado en fiabilidad entre reinicios.

## Árbol de diagnóstico de una comparación

1. ¿La referencia es la de esta sesión? Si no, identificar la correcta antes de comparar.
2. ¿Comienza el dump con la secuencia inicial esperada? Si no, localizar el principio sin asumir ESP.
3. ¿La longitud está completa? Si no, distinguir truncamiento de modificación.
4. ¿Hay divergencia en un punto concreto? Registrar el primer índice y revisar parser, representación y delimitadores.
5. ¿No hay divergencias? Concluir solo sobre los bytes incluidos en esa comparación.

**Regla operativa:** primero dirección y referencia; después interpretación. Una comparación automatizada sobre una hipótesis equivocada produce una salida precisa para la pregunta equivocada.
