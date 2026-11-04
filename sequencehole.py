import argparse
import json
import sys
from pathlib import Path

def analyze(data):
    s = sorted(set(data))
    return [[a + 1, b - 1] for a, b in zip(s, s[1:]) if b > a + 1]

def main():
    parser = argparse.ArgumentParser(description='İlk ve son sıra numarası arasındaki kayıp aralıkları sıkıştırır.')
    parser.add_argument('file', nargs='?', help='UTF-8 JSON input file (default: stdin)')
    args = parser.parse_args()
    try:
        raw = Path(args.file).read_text(encoding='utf-8-sig') if args.file else sys.stdin.read()
        result = analyze(json.loads(raw))
        print(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False))
    except (SyntaxError, ValueError, KeyError, TypeError, OSError, IndexError, ArithmeticError) as error:
        parser.exit(2, f'Invalid input: {error}\n')
if __name__ == '__main__':
    main()
