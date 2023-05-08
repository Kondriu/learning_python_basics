cart = [
    {'name': 'Pencil'},
    {'name': 'Pen'},
    {'name': 'Rubber'}
]

try:
    item = cart[1]
    # prod = item['product']
    prod = item['name']
# except (IndexError, KeyError):
# except (LookupError):
    # print('Index or key not found   ')

except IndexError:
    print('Not in the cart')
except KeyError:
    print('prodict key NF')
else:
    print(f"Product: {prod}")