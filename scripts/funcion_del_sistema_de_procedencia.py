"""Puente para compatibilidad retro con el script original."""

from Python.funcion_del_sistema_de_procedencia import (
    funcion_del_sistema_de_procedencia,
)


if __name__ == "__main__":  # pragma: no cover - punto de entrada CLI
    print(funcion_del_sistema_de_procedencia())
