import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--first_name', nargs='?', required=True)
    parser.add_argument('--last_name', nargs='?', required=True)
    parser.add_argument('--age', nargs='?', required=True)
    parser.add_argument('--height', nargs='?', required=True)
    parser.add_argument('--weight', nargs='?', required=True)
    return dict(vars(parser.parse_args()))


if __name__ == "__main__":
    PARSED_ARGS = parse_arguments()
    print(PARSED_ARGS)
