# Cheatsheet comentada: Python para revisar datos

[Índice](../README.md) · [Tutorial](../docs/04-tutorial-local.md)

**Uso en esta entrega:** comprobaciones locales de representación, integridad y diferencias. No hay funciones de red, ejecución del binario ni construcción de un exploit.

## Separar enteros, texto y bytes

```python
import struct

valor_sintetico = 0x12345678
representacion = struct.pack("<I", valor_sintetico)
print(representacion.hex())  # 78563412
print(struct.unpack("<I", representacion)[0] == valor_sintetico)  # True
```

`<` fija little-endian; `I` fija un entero sin signo de cuatro bytes en este formato. Evitar el orden nativo implícito si los datos pertenecen a una arquitectura concreta. El número es sintético y no representa una dirección del caso. Fuente: [documentación oficial de struct](https://docs.python.org/3/library/struct.html).

```python
texto = "41 42 43"
datos = bytes.fromhex(texto)
print(len(texto), len(datos))  # 8 caracteres, 3 bytes
```

La longitud de un texto hexadecimal no es la longitud de los bytes representados. Registrar ambas cuando se transforme material de una captura. No aplicar `.encode()` al texto hexadecimal esperando obtener los valores que representa.

## Comparación con longitudes explícitas

```python
referencia = bytes.fromhex("01 02 03 04")
observado = bytes.fromhex("01 02 03")
print(referencia == observado)  # False
```

Comparar solo los pares producidos por `zip()` puede ocultar un truncamiento: `zip` se detiene al terminar el más corto. La utilidad incluida compara el prefijo común y después revisa la longitud. La primera diferencia se expresa con índice desde cero; si falta el último byte, el índice es el tamaño del prefijo común.

## Integridad de un archivo

```console
python3 herramientas/auditoria_local.py hash evidencias/capturas/E02-offset-246.png
```

Leer el archivo por bloques permite calcular un hash sin cargarlo entero. Un resultado de integridad no autentica la historia del archivo. Conservar procedencia y contexto por separado.

## Ejecución y códigos de salida

| Orden | Código 0 | Código 1 | Código 2 |
|---|---|---|---|
| `demo` | Demostración ejecutada | No utilizado | Error de uso o ejecución |
| `hash ARCHIVO` | Hash calculado | No utilizado | Lectura o argumentos inválidos |
| `compare REFERENCIA OBSERVADO` | Bytes idénticos | Diferencia o truncamiento detectado | Formato, tamaño o lectura inválidos |

Los archivos de `compare` deben contener únicamente pares hexadecimales y espacios o saltos de línea. No aceptan prefijos `0x`, direcciones, columnas ASCII ni comentarios. El límite es 1 MiB de texto por archivo: una captura pegada como tabla debe limpiarse de manera controlada antes de entrar.

## Qué automatizar y qué conservar manualmente

Automatizar hashes, longitudes y comparación reduce errores mecánicos. Elegir la dirección inicial, la sesión y el significado del resultado requiere criterio. Una salida JSON válida puede documentar perfectamente una referencia equivocada; el programa no decide si dos artefactos pertenecen al mismo experimento.
