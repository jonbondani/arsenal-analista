# Cheatsheet de Python

[Índice](../README.md) · [Ejemplos locales](../docs/04-tutorial-local.md)

## Enteros y orden de bytes

```python
import struct

valor = 0x12345678
datos = struct.pack("<I", valor)
print(datos.hex())  # 78563412
print(struct.unpack("<I", datos)[0] == valor)  # True
```

`<` fija little-endian e `I` representa un entero sin signo de cuatro bytes en ese formato. Indica el orden de forma explícita cuando el dato pertenece a otra arquitectura.

`0x12345678` es un valor de ejemplo, no una dirección del laboratorio. Los formatos están en la [documentación de struct](https://docs.python.org/3/library/struct.html).

## Texto hexadecimal y bytes

```python
texto = "41 42 43"
datos = bytes.fromhex(texto)
print(len(texto), len(datos))  # 8 caracteres, 3 bytes
```

`bytes.fromhex()` interpreta los pares hexadecimales. `.encode()` sobre ese texto produciría los caracteres de la representación, no los tres bytes indicados.

## Truncamientos

```python
referencia = bytes.fromhex("01 02 03 04")
observado = bytes.fromhex("01 02 03")
print(referencia == observado)  # False
```

Al comparar pares con `zip()`, revisa también las longitudes. La iteración termina cuando se agota el más corto y puede ocultar un truncamiento.

La utilidad incluida comprueba el prefijo común y después el tamaño. El índice de diferencia empieza en cero; si falta un byte al final, coincide con la longitud del prefijo común.

## SHA-256 de un archivo

```console
python3 herramientas/auditoria_local.py hash evidencias/capturas/E02-offset-246.png
```

El archivo se lee por bloques. El resultado identifica su contenido, mientras que el origen y el contexto se guardan en el registro de la prueba.

## Códigos de salida

| Orden | Resultado |
| :--- | :--- |
| `demo` | 0 si termina correctamente |
| `hash ARCHIVO` | 0 si lee y calcula el hash |
| `compare REFERENCIA OBSERVADO` | 0 si coinciden; 1 si hay diferencia o truncamiento |
| Error de uso, lectura, formato o tamaño | 2 |

`compare` acepta pares hexadecimales separados por espacios o saltos de línea, hasta 1 MiB de texto por archivo. No admite direcciones, prefijos `0x`, comentarios ni columnas ASCII. Si se parte de un dump, limpia una copia de trabajo y conserva el original.
