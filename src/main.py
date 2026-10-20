def preparar_texto(frase: str) -> str:
    """
    Elimina los espacios de los extremos y convierte el texto a minusculas.

    :param frase: frase original introducida 
    :return: Texto preparado (sin espacios extremos y en minsculas)
    """
    return frase.strip().lower()


def analizar_texto(frase: str) -> tuple[int, int, bool]:
    """
    Analiza el texto preparado y calcula caracteres, palabras y si contiene "python".

    :param frase: Texto ya preparado (minusculas y sin espacios extremos)
    :return: Tupla con (numero de caracteres, numero de palabras contiene "python")
    """
    num_caracteres: int = len(frase)
    palabras: list[str] = frase.split()
    num_palabras: int = len(palabras)
    contiene_python: bool = "python" in palabras

    return num_caracteres, num_palabras, contiene_python


def main():
    frase: str = input()

    texto_preparado: str = preparar_texto(frase)

    if not texto_preparado:
        print("Error: la frase esta vacia")
    else:
        caracteres, palabras, contiene = analizar_texto(texto_preparado)

        print(f"Texto: {texto_preparado}")
        print(f"Caracteres: {caracteres}")
        print(f"Palabras: {palabras}")
        print(f"Contiene la palabra python: {'sí' if contiene else 'no'}")


if __name__ == "__main__":
    main()