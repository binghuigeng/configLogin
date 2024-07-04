import tkinter as tk

# 创建一个登陆界面
"""
@brief 创建了一个简单的登录界面，用户输入用户名和密码，然后点击登录按钮。程序会检查用户名和密码是否匹配，然后显示相应的登录结果。
"""


def login():
    username = entry_username.get()
    password = entry_password.get()

    if username == 'user123' and password == 'secret':
        lbl_result.config(text='Login Successful')
        root.quit()  # 退出界面
        print('Login Successful. Exiting the application.')
    else:
        lbl_result.config(text='Login Failed')


# 创建主窗口
root = tk.Tk()
root.title('Login Window')

# 设置窗口大小
root.geometry('400x300')

# 设置窗口置顶
root.wm_attributes('-topmost', 1)

# 用户名输入
lbl_username = tk.Label(root, text='Username:')
lbl_username.pack()
entry_username = tk.Entry(root)
entry_username.pack()

# 密码输入
lbl_password = tk.Label(root, text='Password:')
lbl_password.pack()
entry_password = tk.Entry(root, show='*')
entry_password.pack()

# 登录按钮
btn_login = tk.Button(root, text='Login', command=login)
btn_login.pack()

# 显示登录结果
lbl_result = tk.Label(root, text='')
lbl_result.pack()

# 运行主循环
root.mainloop()

# 打印退出信息
print('Application has exited.')
