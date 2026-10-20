def preparar_texto(frase: str) -> str:
    """
    Elimina los espacios de los extremos y convierte el texto a minúsculas.

    :param frase: Frase original introducida por el usuario
    :return: Texto preparado (sin espacios extremos y en minúsculas)
    """
    return frase.strip().lower()


def analizar_texto(frase: str) -> tuple[int, int, bool]:
    """
    Analiza el texto preparado y calcula caracteres, palabras y si contiene "python".

    :param frase: Texto ya preparado (minúsculas y sin espacios extremos)
    :return: Tupla con (número de caracteres, número de palabras, contiene "python")
    """
    num_caracteres: int = len(frase)
    palabras: list[str] = frase.split()
    num_palabras: int = len(palabras)
    contiene_python: bool = "python" in palabras

    return num_caracteres, num_palabras, contiene_python


def main() -> None:
    frase: str = input()

    texto_preparado: str = preparar_texto(frase)

    if not texto_preparado:
        print("Error: la frase está vacía")
    else:
        caracteres, palabras, contiene = analizar_texto(texto_preparado)

        print(f"Texto: {texto_preparado}")
        print(f"Caracteres: {caracteres}")
        print(f"Palabras: {palabras}")
        print(f"Contiene la palabra python: {'sí' if contiene else 'no'}")


if __name__ == "__main__":
    main()