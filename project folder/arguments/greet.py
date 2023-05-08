import argparse

greetengs = {
    'english': 'Hello',
    'french': 'Bonjour',
    'german': 'Hallo',
    'italian': 'Ciao'
}

def handle_args():
    '''parse and return arguments'''

    parser = argparse.ArgumentParser(description='generate greething.')
    parser.add_argument('first_name', help='first name of person to greet')
    parser.add_argument('last_name', help='last name of person to greet')
    parser.add_argument(
        '-l', '--language',
        help='Language of greeteng.',
        choices=greetengs.keys(),
        default='english',
    )

    return parser.parse_args()
 
def main():
    '''entry point'''
    args = handle_args()
    greeteng = greetengs[args.language]
    print(f"{greeteng}, {args.first_name} {args.last_name}!")


if __name__ == '__main__':
    main()


