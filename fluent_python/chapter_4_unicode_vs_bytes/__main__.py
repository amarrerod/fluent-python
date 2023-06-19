def byte_essentials():
    # Bytes are immutable
    # Bytearray are mutable
    cafe = bytes("café", encoding="utf_8")
    print(f"Café as bytes in UTF-8: {cafe}")

    print(
        f"First byte of the object: {cafe[0]}. Slice of the first two bytes are also bytes: {cafe[:1]}"
    )

    cafe_arr = bytearray(cafe)
    print(f"Byte array of cafe: {cafe_arr}")
    print(f"Slice of bytearray: {cafe_arr[-1:]}")


def encode_decode(string: str = ""):
    for codec in ["latin_1", "utf_8", "utf_16"]:
        print(f"{string} encoded with {codec}: {string.encode(codec)}", sep="\t")


def encode_problems():
    city = "Säo Paulo"
    print(f'{city} in UTF-8: {city.encode("utf_8")}')
    print(f'{city} in UTF-16: {city.encode("utf_16")}')
    print(f'{city} in ISO 8859_1: {city.encode("iso8859_1")}')
    # Encoding with error handling
    print(f'{city} in CP437 ignoring errors: {city.encode("cp437", errors="ignore")}')
    print(f'{city} in CP437 replacing errors: {city.encode("cp437", errors="replace")}')
    print(
        f'{city} in CP437 XML char reference replace errors: {city.encode("cp437", errors="xmlcharrefreplace")}'
    )


def decode_problems():
    octets = b"Montr\xe9al"
    print(f'CP1252 Decoded: {octets.decode("cp1252")}')
    print(f'ISO8859_7 Decoded: {octets.decode("iso8859_7")}')
    print(f'KOI_8_r Decoded: {octets.decode("koi8_r")}')
    # Codecs is not a valid UTF-8 --> raises UnicodeDecodeError
    print(f'Utf-8 with error replace: {octets.decode("utf_8", errors="replace")}')


def main():
    byte_essentials()
    encode_decode("El Niño")
    encode_problems()
    decode_problems()


if __name__ == "__main__":
    main()
