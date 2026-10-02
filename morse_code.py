#!/usr/bin/env python3
"""Encode text as International Morse code or decode Morse tokens."""

import argparse
import sys


MORSE = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
    "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
    "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
    "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
    "Z": "--..", "0": "-----", "1": ".----", "2": "..---",
    "3": "...--", "4": "....-", "5": ".....", "6": "-....",
    "7": "--...", "8": "---..", "9": "----.",
    ".": ".-.-.-", ",": "--..--", "?": "..--..", "'": ".----.",
    "!": "-.-.--", "/": "-..-.", "(": "-.--.", ")": "-.--.-",
    "&": ".-...", ":": "---...", ";": "-.-.-.", "=": "-...-",
    "+": ".-.-.", "-": "-....-", "_": "..--.-", '"': ".-..-.",
    "$": "...-..-", "@": ".--.-.",
}
PLAIN = {code: char for char, code in MORSE.items()}


def encode(text):
    words = []
    for word in text.split():
        codes = []
        for char in word.upper():
            if char not in MORSE:
                raise ValueError(f"unsupported character: U+{ord(char):04X}")
            codes.append(MORSE[char])
        words.append(" ".join(codes))
    if not words:
        raise ValueError("text is empty")
    return " / ".join(words)


def decode(code):
    tokens = code.split()
    if not tokens or tokens[0] == "/" or tokens[-1] == "/":
        raise ValueError("Morse code must contain dot-dash tokens")
    words = []
    letters = []
    for token in tokens:
        if token == "/":
            if not letters:
                raise ValueError("word separators cannot be repeated")
            words.append("".join(letters))
            letters = []
        elif token in PLAIN:
            letters.append(PLAIN[token])
        else:
            raise ValueError(f"unknown Morse token: {token}")
    words.append("".join(letters))
    return " ".join(words)


def main():
    parser = argparse.ArgumentParser(description="Encode or decode International Morse code.")
    subparsers = parser.add_subparsers(dest="action", required=True)
    encoder = subparsers.add_parser("encode", help="convert text to dot-dash tokens")
    encoder.add_argument("text", help="text to encode; quote it to preserve spaces")
    decoder = subparsers.add_parser("decode", help="convert dot-dash tokens to text")
    decoder.add_argument("code", help="tokens separated by spaces, with / between words")
    args = parser.parse_args()
    try:
        result = encode(args.text) if args.action == "encode" else decode(args.code)
    except ValueError as error:
        print(f"morse-code: {error}", file=sys.stderr)
        return 2
    print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
