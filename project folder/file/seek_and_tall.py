with open('alphabetFile.txt') as af:
    print(f'Location when opened is {af.tell()}') # return index of file, where pointer looked
    print(f'First letter: {af.read(1)}')    #  prints first letter
    print(f'Second letter: {af.read(1)}')   #  same funtion, but another result - it is becouce file pointer moves by previous use, and now returns 2 letter
    af.seek(4)  #   Also set pointer to this position (counting as in Java starts form 0)
    print(f'Print 5 letter: {af.read(1)}')
    