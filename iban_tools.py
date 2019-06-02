import string


IBAN_CHARS = set(string.ascii_letters + string.digits + ' ')
NUMBER_CODES = {char: number + 10 for (number, char) in enumerate(string.ascii_uppercase)}


def clean_string(str_input: str) -> str:
    if not set(str_input).issubset(IBAN_CHARS):
        raise ValueError("Not a valid IBAN")
    return str_input.replace(' ', '').upper()


def is_valid_iban(iban: str) -> bool:
    iban = clean_string(iban)
    iban_num = int(f"{iban[4:]}{NUMBER_CODES[iban[0]]}{NUMBER_CODES[iban[1]]}{iban[2:4]}")
    if iban_num % 97 == 1:
        return True
    return False


if __name__ == '__main__':
    assert is_valid_iban('FI42 5000 1510 0000 23') is True
    assert is_valid_iban('FI4250001510000023') is True
    assert is_valid_iban('FI22 5000 1510 0000 23') is False
    assert is_valid_iban('  F I 42 5 00  015  1  000 002  3 ') is True
    assert is_valid_iban('  FI42 5010 1510 0000 23 ') is False
