"""
License: Apache
Organization: UNIR
"""

import os
import sys

DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False


def sort_list(items, ascending=True):
    if not isinstance(items, list):
        raise RuntimeError(f"Cannot sort {type(items)}")

    return sorted(items, reverse=(not ascending))


def remove_duplicates_from_list(items):
    return list(set(items))

def rename_file(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        print(f"Archivo renombrado exitosamente a: {new_name}")
    except FileNotFoundError:
        print(f"Error: El archivo {old_name} no existe para ser renombrado.")
    except Exception as e:
        print(f"Ocurrió un error al renombrar: {e}")

if __name__ == "__main__":
    filename = DEFAULT_FILENAME
    remove_duplicates = DEFAULT_DUPLICATES
    if len(sys.argv) == 3:
        filename = sys.argv[1]
        remove_duplicates = sys.argv[2].lower() == "yes"
    else:
        print("You must specify the file as the first argument")
        print("The second argument indicates if duplicates should be removed")
        sys.exit(1)

    print(f"Reading words from file {filename}")
    file_path = os.path.join(".", filename)
    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, "r") as file:
            for line in file:
                word_list.append(line.strip())
    else:
        print(f"The file {filename} does not exist")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    if remove_duplicates:
        word_list = remove_duplicates_from_list(word_list)

    print(sort_list(word_list))
	confirm = input("¿Deseas renombrar el archivo original? (s/n): ").lower()
    if confirm == "s":
        nuevo_nombre = input("Introduce el nuevo nombre (ejemplo: 'procesado.txt'): ")
        rename_file(filename, nuevo_nombre)
