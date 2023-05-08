import os

# rb - read binary
with open('alphabetFile.txt', 'rb') as af:
    # print(af.read(1))
    # print(type(af.read(1)))
    # print(af.read(1).decode())

    print('Every other letters:')
    while True:
        letter = af.read(1)
        if letter:
            print(letter.decode())
            # af.seek(1,1)
            af.seek(1,  os.SEEK_CUR) # os.SEEK_CUR - seek from a cursor
        else:
            break

    print("Last letter:")
    af.seek(-1, os.SEEK_END) # os.SEEK_END - seek from end of file (and move to the -1 index)
    print(af.read(1).decode())