import os



current_dir = os.getcwd() #path of directory

# os.path.join() #create walid path for current os
sub_dir = 'files'
file_name = 'data.txt'

# if directory does'nt exist we shuld create it:
dir_path = os.path.join(current_dir, sub_dir)
os.makedirs(dir_path, exist_ok=True)


full_path = os.path.join(current_dir, sub_dir, file_name)


print('\n' + full_path)

# homedir:
home_dir=os.path.expanduser('~')

