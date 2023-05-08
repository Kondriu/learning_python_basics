import argparse
import os


def handle_args():
    '''arguments for script'''
    parser = argparse.ArgumentParser(
        description='Write number range for script.'
    )

    parser.add_argument(
        'path',
        help='Path to store files.'
    )

    parser.add_argument(
        '-s', '--start',
        help='start of range to print to file.',
        type=int,
        default=1
    )

    parser.add_argument(
        '-f', '--finish',
        help='Finish of range  to print',
        type = int,
        default=100
    )

    return parser.parse_args()


def main():
    '''entrypoint of script'''
    cur_dir = os.getcwd()
    out = os.path.join(cur_dir, 'output')
    os.makedirs(out, exist_ok=True)

    args = handle_args()
    out_file_path = os.path.join(out, args.path) 
    with open(out_file_path, 'w') as f:
        for x in range(args.start, args.finish):
            f.write(f'{str(x)}\n')

if __name__ == '__main__':
    main()