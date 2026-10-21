#!/usr/bin/env python3
"""Revisión local de datos; sin red, ejecución de muestras ni escritura de archivos."""
import argparse
import hashlib
import json
from pathlib import Path
import struct
import sys

MAX_HEX_TEXT = 1024 * 1024


def first_difference(reference: bytes, observed: bytes):
    """Índice desde cero, incluido un truncamiento; None significa igualdad."""
    for index, (left, right) in enumerate(zip(reference, observed)):
        if left != right:
            return index
    if len(reference) != len(observed):
        return min(len(reference), len(observed))
    return None


def load_hex(path: Path) -> bytes:
    # Lectura acotada incluso si el archivo crece después de consultarlo.
    with path.open("rb") as stream:
        raw = stream.read(MAX_HEX_TEXT + 1)
    if len(raw) > MAX_HEX_TEXT:
        raise ValueError("el archivo hexadecimal supera 1 MiB de texto")
    return bytes.fromhex(raw.decode("ascii"))


def hash_file(path: Path):
    digest = hashlib.sha256()
    total = 0
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(65536), b""):
            digest.update(block)
            total += len(block)
    return {"archivo": path.name, "bytes": total, "sha256": digest.hexdigest()}


def demo():
    number = 0x12345678  # Entero arbitrario, ajeno a direcciones del laboratorio.
    packed = struct.pack("<I", number)
    reference = bytes.fromhex("01 02 03 04 05 06 07 08")
    memory = bytes.fromhex("aa bb") + reference
    changed = bytes.fromhex("01 02 03 99 05 06 07 08")
    return {
        "clase": "SINTETICO",
        "entero_hex": hex(number),
        "little_endian": packed.hex(),
        "ida_vuelta_correcta": struct.unpack("<I", packed)[0] == number,
        "coincide_inicio_cero": memory[:len(reference)] == reference,
        "coincide_inicio_dos": memory[2:2 + len(reference)] == reference,
        "primera_diferencia": first_difference(reference, changed),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("demo", help="demostración sintética sin archivos")
    hashing = commands.add_parser("hash", help="SHA-256 de un archivo local")
    hashing.add_argument("file", type=Path)
    comparison = commands.add_parser("compare", help="comparar dos archivos hexadecimales")
    comparison.add_argument("reference", type=Path)
    comparison.add_argument("observed", type=Path)
    args = parser.parse_args()
    code = 0
    try:
        if args.command == "demo":
            result = demo()
        elif args.command == "hash":
            result = hash_file(args.file)
        else:
            reference = load_hex(args.reference)
            observed = load_hex(args.observed)
            difference = first_difference(reference, observed)
            result = {
                "coinciden": difference is None,
                "longitud_referencia": len(reference),
                "longitud_observado": len(observed),
                "primera_diferencia": difference,
                "convencion": "indice desde cero",
            }
            code = 0 if difference is None else 1
    except (OSError, ValueError) as error:
        # Evita imprimir rutas o contenido de entradas en mensajes de error.
        print(json.dumps({"error": type(error).__name__,
                          "ayuda": "revise lectura, pares hexadecimales ASCII y limite de 1 MiB"},
                         ensure_ascii=False), file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return code


if __name__ == "__main__":
    raise SystemExit(main())
