'''
get bitcoin price
'''

import argparse
import requests

def _price_url(currency, action):
    """henerate coinbace url """
    return f'https://api.coinbase.com/v2/prices/BTC-{currency}/{action}'

def handle_args():
    """Process args"""
    parcer = argparse.ArgumentParser(description='get bit ptice')
    parcer.add_argument(
        '-c', '--currency',
        help='currency code.',
        choices=['GBP', 'USD', 'INR'],
        default='USD'
    )
    parcer.add_argument(
        '-a', '--action',
        help='action for perform',
        choices=['buy', 'sell'],
        default='buy'
    )

    return parcer.parse_args()


def main():
    '''entry point'''
    args = handle_args()
    url = _price_url(args.currency, args.action)
    res = requests.get(url)

    data = res.json()
    amnt = data['data']['amount']
    print(f'amount {amnt} ({args.currency})')


if __name__ == '__main__':
    main()
