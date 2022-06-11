# repository: https://github.com/s22442/pjatk-asd2

from helpers import ascii, file, huffman


if __name__ == "__main__":
    print("Enter the path to the file to be encoded:")
    path = input()

    text = file.read_from(path)

    char_codes = huffman.create_codes(text)
    encoded_text = huffman.encode(text, char_codes)

    # assign the codes to ascii representation of the characters for better handling of specials (e.g. new lines)
    ascii_char_codes = ascii.asciify_dict_keys(char_codes)

    path_without_extension = file.create_path_without_extension(path)
    file.write_to(f"{path_without_extension}_encoded.txt", encoded_text)
    file.write_dict_as_yaml_to(f"{path_without_extension}_char-codes.yaml", char_codes)
    file.write_dict_as_yaml_to(
        f"{path_without_extension}_ascii-char-codes.yaml", ascii_char_codes
    )
