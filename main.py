import datetime
import random
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog

window = Tk()
window.title("password加解密")
window.geometry("700x800")
window.resizable(True, True)


# 加密过程
def encrypted(加密内容, encrypted_text='', 后缀=''):  # encrypted_text不要管
    encrypted_content = []  # 加密码内宽数据列表
    random_number = random.randint(1, 101)  # 生成随机数
    random_password = ''
    lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                         't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                         'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for i in range(random.randint(5, 37)):
        temp = random.choice(lowercase_letters)
        random_password += temp
    lower_num = 0
    for i in list(random_password):
        lower_num += ord(i)
    symbols = ["+", "-", "*"]  # 符号列表
    random_symbol = random.choice(symbols)  # 随机选择符号
    if type(加密内容) == Entry:
        content = list(加密内容.get())  # 将解密码内宽数据解添加到列表中
    else:
        content = list(加密内容)  # 将解密码内宽数据解添加到列表中
    if 后缀 != "":
        for i in range(len(后缀)):
            content.append(list(后缀)[i])
    encrypted_content.append("104 ")  # 加密内容标识
    for char in content:
        if random_symbol == "*":
            encrypted_char = str(ord(char) * random_number + lower_num)  # 字符乘以随机数
            encrypted_content.append(encrypted_char + " ")  # 加入加密内容列表
        elif random_symbol == "+":
            encrypted_char = str(ord(char) + random_number + lower_num)  # 字符加上随机数
            encrypted_content.append(encrypted_char + " ")  # 加入加密内容列表
        else:
            encrypted_char = str(ord(char) - random_number + lower_num)  # 字符减去随机数
            encrypted_content.append(encrypted_char + " ")  # 加入加密内容列表
    if 后缀 == '':
        encrypted_content.append("0 ")  # 无后缀标识符
    else:
        encrypted_content.append(str(len(后缀)) + " ")  # 后缀长度标识符
    encrypted_content.append(str(random_number) + " ")  # 加入随机数
    encrypted_content.append(str(symbols.index(random_symbol)))  # 加入符号索引
    for item in encrypted_content:
        encrypted_text += item

    return encrypted_text, random_password


def encrypt_word():

    a = messagebox.askyesno('password加解密','可能会覆盖前之前的加密文件，是否继续？')
    if a:
        temp = encrypted(加密内容=txt_encryptWord)
        with open("加密内容.txt", "w") as r:
            r.write(f'加密内容：{temp[0]}\n密钥：{temp[1]}')
        messagebox.showinfo("password加解密", "已将加密内容保存到当前程序所在目录！")


def choose_file():
    file_path = filedialog.askopenfilename()
    return file_path


def encrypt_file():
    file_path = choose_file()
    file_后缀 = file_path.split("/")[-1].split('.')[-1]
    file_name = file_path.split("/")[-1].split('.')[0]

    with open(file_path, "r", encoding='utf-8') as f:
        # 读取文件内容并进行处理
        file_text = f.read()

    temp = encrypted(加密内容=file_text, 后缀=file_后缀)
    a = messagebox.askyesno('password加解密', '可能会覆盖前之前的加密文件，是否继续？')
    if a:
        with open(f"{file_name}.happy", 'w') as r:
            r.write(temp[0])
        with open("key_file.txt", 'w') as r:
            r.write(temp[1])
        messagebox.showinfo("password加解密", "已将加密密钥保存到当前程序所在目录！")
        messagebox.showinfo("password加解密", "已将文件加密并保存到程序目录！")


# 解密码过程
def decrypted(解密内容, 密钥, decrypted_text=''):  # decrypted_text不要管
    # 解密过程
    temp = False
    decrypted_content = 解密内容.split(" ")  # 将解密码内宽数据解添加到列表中

    lower_num = 0

    for i in list(密钥):
        lower_num += ord(i)
    if decrypted_content[0] == "104":
        temp = True
        decrypted_content.pop(0)
        index = 0  # 索引
        for item in decrypted_content[0:-3]:
            if decrypted_content[-1] == "0":
                try:
                    decrypted_content[index] = chr(int(item) - int(decrypted_content[-2]) - lower_num)  # 将数字减去倒数第二个数字
                    index += 1
                except:
                    messagebox.showerror('password加解密', '密钥好像不太对哦！')
                    break
            elif decrypted_content[-1] == "1":
                try:
                    decrypted_content[index] = chr(int(item) + int(decrypted_content[-2]) - lower_num)  # 将数字加上倒数第二个数字
                    index += 1
                except:
                    messagebox.showerror('password加解密', '密钥好像不太对哦！')
                    break
            elif decrypted_content[-1] == "2":
                try:
                    decrypted_content[index] = chr(int(item) // int(decrypted_content[-2]) - lower_num)  # 将数字除以倒数第二个数字
                    index += 1
                except:
                    messagebox.showerror('password加解密', '密钥好像不太对哦！')
                    break
        if decrypted_content[-3] == '0':
            for char in decrypted_content[0:-3]:
                decrypted_text += char
        else:
            后缀 = ''
            for char in decrypted_content[0:-3 - int(decrypted_content[-3])]:
                decrypted_text += char
            for i in decrypted_content[-3 - int(decrypted_content[-3]):-3]:
                后缀 += i
    else:
        temp = False
        messagebox.showerror("password加解密码", "你给予的不是符合要求的加密码！")
    templist = [decrypted_text, temp, 后缀]
    return templist


def decrypt_word():
    temp = decrypted(解密内容=txt_decryptWord.get(), 密钥=txt_decryptKey.get())
    if temp[1]:
        time = datetime.datetime.now()
        time = list(str(time))
        count = 0
        for i in time:
            if i == ".":
                time[count] = "-"
            elif i == ":":
                time[count] = "-"
            count += 1
        times = ""
        for i in time:
            times += i
        with open(f"{times}.txt", "w") as f:
            f.write(temp[0])
        messagebox.showinfo("password加解密", "已经保存在同一目录下名为当前时间的文本文件，请打开文件查看")
    elif not temp[1]:
        pass


def decrypt_file():
    file_path = choose_file()
    后缀 = file_path.split("\\")[-1].split('.')[-1]
    if 后缀 != 'happy':
        messagebox.showerror('password加解密', '看起来文件后缀不太对哦！')
    else:
        def askname():
            result = simpledialog.askstring(title='信息', prompt='请输入密钥：', initialvalue='')
            return result

        密钥 = askname()
        if 密钥 != '':
            解密内容 = ''
            with open(file_path, 'r') as f:
                解密内容 = f.read()
            temp = decrypted(解密内容=解密内容, 密钥=密钥)
            time = datetime.datetime.now()
            time = list(str(time))
            count = 0
            for i in time:
                if i == ".":
                    time[count] = "-"
                elif i == ":":
                    time[count] = "-"
                count += 1
            times = ""
            for i in time:
                times += i

            with open(f"{times}.{temp[2]}", "w") as f:
                f.write(temp[0])

            messagebox.showinfo("password加解密", "已经保存在同一目录下名为当前时间的文本文件，请打开文件查看")


lbl_encryptWord = Label(window, text="加密文字:", font=("Arial", 20))
lbl_encryptWord.grid(column=0, row=0)

txt_encryptWord = Entry(window, width=50)
txt_encryptWord.grid(column=1, row=0)

btn_encryptWord = Button(window, text="加密码", command=encrypt_word)
btn_encryptWord.grid(column=2, row=0)

lbl_decryptWord = Label(window, text="解密文字:", font=("Arial", 20))
lbl_decryptWord.grid(column=0, row=1)
txt_decryptWord = Entry(window, width=50)
txt_decryptWord.grid(column=1, row=1)

lbl_decryptKey = Label(window, text="解密文字密钥:", font=("Arial", 20))
lbl_decryptKey.grid(column=0, row=2)
txt_decryptKey = Entry(window, width=50)
txt_decryptKey.grid(column=1, row=2)

btn_decryptWord = Button(window, text="解密码", command=decrypt_word)
btn_decryptWord.grid(column=2, row=2)

btn_encryptFile = Button(window, text="加密文件", command=encrypt_file)
btn_encryptFile.grid(column=0, row=3)
btn_decryptFile = Button(window, text='解密文件', command=decrypt_file)
btn_decryptFile.grid(column=1, row=3)
window.mainloop()
