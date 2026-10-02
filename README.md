# morse-code

Convert text to International Morse code or decode dot-dash tokens. It works offline and uses only the Python standard library.

## Use

Requires Python 3.10+.

```sh
python morse_code.py encode "Hello, world!"
python morse_code.py decode ".... . .-.. .-.. --- --..-- / .-- --- .-. .-.. -.. -.-.--"
```

Spaces separate letters and `/` separates words. The supported characters are A–Z, 0–9, and common International Morse punctuation. Text is case-insensitive. Unsupported characters and malformed tokens return an error without a traceback.

## License

MIT
