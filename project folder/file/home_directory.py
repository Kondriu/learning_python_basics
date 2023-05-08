import os

home_dir = os.path.expanduser('~') #returms home dir for current user
conf_dir = '.python-code-home-dir-conf'
conf_dir_path = os.path.join(home_dir, conf_dir)
os.makedirs(conf_dir_path, exist_ok=True)

conf_file_name = 'message.conf'
conf_file_path = os.path.join(conf_dir_path, conf_file_name)

DEFAULT_MESSGE = 'Change me!'

if os.path.exists(conf_file_path):
    with open(conf_file_path) as msg_file:
        message = msg_file.read()
        print(f">Configured message: {message}")
else: 
    with open(conf_file_path, 'w') as msg_file:
        msg_file.write(DEFAULT_MESSGE)
        print('Message set')
