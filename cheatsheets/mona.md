# Cheatsheet de mona

[Índice](../README.md) · [Evidencias](../evidencias/README.md)

Estos son los comandos de mona clásico utilizados para revisar los patrones y la memoria del caso. El proyecto [corelan/mona](https://github.com/corelan/mona) está archivado y remite a [mona3](https://github.com/corelan/mona3). Antes de usar otro entorno, revisa sus requisitos y ayuda: la compatibilidad de hosts y comandos puede cambiar.

## Separar los archivos de una sesión

```text
!mona config -set workingfolder C:\Mona\sesion_revision
```

La carpeta de trabajo reúne patrones, referencias e informes. Utilizar una carpeta distinta por sesión evita confundir una tabla antigua con la que se acaba de generar. Guarda también la versión del plugin y la ruta efectiva.

## Generar un patrón local

```text
!mona pattern_create 400
```

La orden crea un patrón con la longitud descrita en el laboratorio. Conserva el archivo exacto y su hash para poder contrastarlo más adelante.

Generar el patrón es una operación local. Para relacionarlo con un crash harían falta la entrada utilizada y el contexto de la ejecución. El repositorio no incluye un script que lo transmita al servidor.

## Consultar el valor de la captura

```text
!mona pattern_offset 41326941
```

En E02, la consulta devuelve la posición 246. La medida se refiere al patrón consultado y necesita un origen bien definido. Revisa la representación del valor antes de invertir bytes a mano o cambiar su formato.

La salida completa y el archivo del patrón permiten comprobar que la coincidencia corresponde a la referencia de esa prueba.

## Crear una tabla con exclusiones

```text
!mona bytearray -b "\x00\x0a\x0d"
```

El parámetro `-b` indica los bytes que quedan fuera de la referencia. Con esas tres exclusiones, la tabla contiene 253 valores.

Anota el motivo de cada exclusión. Puede proceder del protocolo, de una hipótesis o de una observación previa. El hecho de excluir un valor no demuestra que haya fallado en la comparación.

## Comparar desde el inicio de la tabla

```text
!mona compare -f C:\Mona\sesion_revision\bytearray.bin -a DIRECCION_VERIFICADA
```

Sustituye `DIRECCION_VERIFICADA` por la dirección del primer byte observada en la sesión. Es un marcador de la explicación y no un argumento literal válido.

`-f` identifica el archivo de referencia y `-a` la posición inicial de memoria. Conserva el hash y la longitud de la tabla, la dirección utilizada, los registros de ese instante y la salida de mona.

`Unmodified` indica que esa referencia coincide en esa ubicación. En el caso se describe un inicio ocho bytes antes de ESP, pero el ajuste necesita comprobarse de nuevo en otra detención.

## Revisar módulos

```text
!mona modules
```

La salida ayuda a inventariar módulos y sus atributos. Registra módulo, versión o hash cuando estén disponibles, base y sesión.

Los indicadores deben interpretarse por separado. `NXCompat = False` no permite concluir por sí solo que DEP esté desactivado. La estabilidad de una dirección tampoco se determina con una única lista de módulos.

## Comprobar una comparación dudosa

1. Confirma que la referencia pertenece a la sesión actual.
2. Localiza en el dump el comienzo de la secuencia.
3. Comprueba que la longitud permite leerla completa.
4. Si hay diferencias, anota el primer índice y revisa representación, delimitadores y parseo.
5. Si coincide, limita la conclusión a los bytes y al contexto comparados.

La dirección y la referencia deben estar resueltas antes de interpretar la salida. La [resolución de problemas](../docs/07-troubleshooting.md) amplía los síntomas más habituales.
