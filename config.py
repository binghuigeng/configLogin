import configparser

# 读写配置文件
"""
@brief 在Python中，可以使用内置的configparser模块来读写配置文件。configparser模块能够解析INI文件格式，使得读取和修改配置文件变得非常方便。

1. 创建配置文件config.ini:

[settings]
username = user123
password = secret

2. 读取配置文件内容:

import configparser

# 创建ConfigParser对象
config = configparser.ConfigParser()

# 读取配置文件
config.read('config.ini')

# 获取配置信息
username = config.get('settings', 'username')
password = config.get('settings', 'password')

print(f'Username: {username}')
print(f'Password: {password}')

3. 修改配置文件内容:

import configparser

# 创建ConfigParser对象
config = configparser.ConfigParser()

# 读取配置文件
config.read('config.ini')

# 修改配置信息
config.set('settings', 'username', 'new_user')
config.set('settings', 'password', 'new_password')

# 写入修改后的配置到文件
with open('config.ini', 'w') as configfile:
    config.write(configfile)

print('Configuration updated.')

在这个示例中，我们首先创建了一个名为config.ini的配置文件，然后使用configparser模块读取了该文件中的配置信息。
接着，我们修改了配置信息并将修改后的内容写回到配置文件中。通过这种方法，你可以方便地读取和修改配置文件中的参数。
"""

# 创建配置解析器对象
config = configparser.ConfigParser()
# 读取配置文件
config.read('config.ini')

# 获取配置值
username = config.get('Login', 'username')
password = config.get('Login', 'password')

print(f'Username: {username}')
print(f'Password: {password}')

# 修改配置信息
config.set('Login', 'username', 'new_user')
config.set('Login', 'password', 'new_password')

# 写入修改后的配置到文件
with open('config.ini', 'w') as configfile:
    config.write(configfile)

print('Configuration updated.')

# 获取配置值
username = config.get('Login', 'username')
password = config.get('Login', 'password')

print(f'Username: {username}')
print(f'Password: {password}')
