# Cheatsheet de Python

[Índice](../README.md) · [Tutorial](../docs/04-tutorial-local.md)

Python resulta útil para revisar representaciones, comparar datos y conservar la identidad de los archivos. Los ejemplos de esta ficha trabajan en local y utilizan valores sintéticos.

## Convertir un entero a bytes

```python
import struct

valor = 0x12345678
datos = struct.pack("<I", valor)
print(datos.hex())  # 78563412
print(struct.unpack("<I", datos)[0] == valor)  # True
```

El prefijo `<` fija little-endian y `I` representa un entero sin signo de cuatro bytes en ese formato. Es preferible indicar el orden de forma explícita cuando se trabaja con datos de una arquitectura concreta.

El entero del ejemplo es arbitrario y no corresponde a una dirección del laboratorio. La [documentación de struct](https://docs.python.org/3/library/struct.html) explica los formatos y tamaños.

## Separar texto hexadecimal y bytes

```python
texto = "41 42 43"
datos = bytes.fromhex(texto)
print(len(texto), len(datos))  # 8 caracteres, 3 bytes
```

La longitud del texto y la del dato representado son distintas. `bytes.fromhex()` interpreta los pares hexadecimales; aplicar `.encode()` al texto produciría los caracteres de esa representación.

## Detectar un truncamiento

```python
referencia = bytes.fromhex("01 02 03 04")
observado = bytes.fromhex("01 02 03")
print(referencia == observado)  # False
```

Si se comparan pares con `zip()`, hay que revisar también las longitudes: la iteración termina cuando se acaba el archivo más corto. La utilidad incluida comprueba el prefijo común y después el tamaño.

El primer índice de diferencia se cuenta desde cero. Cuando falta el último byte, coincide con la longitud del prefijo común.

## Calcular un hash

```console
python3 herramientas/auditoria_local.py hash evidencias/capturas/E02-offset-246.png
```

La lectura por bloques permite calcular SHA-256 sin cargar el archivo completo en memoria. El resultado sirve para comprobar integridad e identificar una copia. La procedencia y el contexto de la evidencia deben registrarse aparte.

## Códigos de salida

| Orden | Resultado |
| :--- | :--- |
| `demo` | 0 si termina correctamente |
| `hash ARCHIVO` | 0 si puede leer y calcular el hash |
| `compare REFERENCIA OBSERVADO` | 0 si coinciden; 1 si hay diferencia o truncamiento |
| Error de uso, lectura, formato o tamaño | 2 |

`compare` acepta archivos con pares hexadecimales y espacios o saltos de línea. El límite es 1 MiB de texto por archivo. Los prefijos `0x`, las direcciones, los comentarios y las columnas ASCII de un dump deben limpiarse antes, conservando el original para revisar la conversión.

## Uso dentro del análisis

Automatizar hashes, longitudes y comparaciones evita errores mecánicos. La utilidad no sabe si dos archivos pertenecen a la misma sesión ni si se eligió bien la dirección de memoria. Esos datos forman parte del registro del analista.
