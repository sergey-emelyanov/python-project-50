from gendiff.cli import parse_args
from gendiff import generate_diff


def main():
    first_file, second_file, format_style = parse_args()
    print(generate_diff(first_file, second_file, format_style))


if __name__ == "__main__":
    main()
