"""Módulo que expone la función del sistema de procedencia."""


def funcion_del_sistema_de_procedencia() -> str:
    """Retorna el mensaje de confirmación del sistema.

    Returns:
        str: Mensaje indicando que la función se ejecutó.
    """

    return "Función de procedencia ejecutada correctamente"


if __name__ == "__main__":  # pragma: no cover - comportamiento CLI
    print(funcion_del_sistema_de_procedencia())
