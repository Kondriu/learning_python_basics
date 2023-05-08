file_path = 'output.txt'

strings = [
    "String bla bla!\n"
    "Onother line...\n"
    "hello \n"
]

with open(file_path, 'a') as out_file:      
    # 'w' - opening file in write mode. owerwriting all existed content
    # 'a' - open in write mode + appending new content to existed 
    out_file.write("\n")
    out_file.writelines(strings)