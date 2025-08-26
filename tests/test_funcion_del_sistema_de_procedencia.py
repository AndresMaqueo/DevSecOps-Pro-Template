from pathlib import Path
import sys

# Aseguramos que el directorio raíz del proyecto esté en sys.path para poder
# importar los módulos del paquete ``scripts`` durante la ejecución de los
# tests.
sys.path.append(str(Path(__file__).resolve().parents[1]))

from scripts.Python import funcion_del_sistema_de_procedencia  # noqa: E402


def test_funcion_del_sistema_de_procedencia():
    assert (
        funcion_del_sistema_de_procedencia() ==
        "Función de procedencia ejecutada correctamente"
    )
