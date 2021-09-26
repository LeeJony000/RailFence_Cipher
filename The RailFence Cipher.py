import string
import math

function = input("Input e to encrypt or d to decrypt:")
function = function.upper()
if function == 'E':
    encrypt_message = ""
    message = input("Please input your message:")
    message_length = len(message)
    fence_number = int(input("Please input your fence number:"))

    # 创建全局空列表
    for i in range(fence_number):
        s = 'encrypt_message_list' + str(i)
        vars()[s] = []

    # 将字符串的字符加入列表
    for i in range(message_length):
        remainder = i % fence_number
        s = 'encrypt_message_list' + str(remainder)
        vars()[s].append(message[i])

    # 打印加密信息
    for i in range(fence_number):
        s = 'encrypt_message_list' + str(i)
        print((vars()[s]))
        encrypt_message = encrypt_message + "".join(vars()[s])
    print(encrypt_message)

elif function == 'D':
    decrypt_message = ""
    decrypt_message_list_size = 0
    encrypt_message = input("Please input your encrypt_message:")
    encrypt_message_length = len(encrypt_message)
    fence_number = int(input("Please input your fence number:"))
    j = 0
    h = 0
    m = 0

    # 创建全局空列表
    for i in range(fence_number):
        s = 'decrypt_message_list' + str(i)
        vars()[s] = []

    # 基本列表大小，即字符串大小除以栅栏数目取整
    basic_list_size = int(encrypt_message_length / fence_number)
    # 字符串大小除以栅栏数目取余，后面根据余数确定每个列表最终大小
    remainder1 = encrypt_message_length % fence_number
    remainder2 = encrypt_message_length % fence_number

    # 将字符串的字符加入列表
    for i in range(encrypt_message_length):
        s = 'decrypt_message_list' + str(j)

        if m == 0 and remainder1 == 0:
            if i == int(i / (basic_list_size-1)) * basic_list_size - 1:
                vars()[s].append(encrypt_message[i])
                j += 1
            else:
                vars()[s].append(encrypt_message[i])

        elif m != 0 and remainder1 == 0:
            if i == int(i / (basic_list_size - 1)) * basic_list_size - 1 + m:
                (vars()[s]).append(encrypt_message[i])
                j += 1
            else:
                vars()[s].append(encrypt_message[i])

        elif remainder1 != 0:
            if i == int(i / (basic_list_size - 1)) * basic_list_size + h and i != 0:
                vars()[s].append(encrypt_message[i])
                h += 1
                j += 1
                remainder1 -= 1
                m += 1
            else:
                vars()[s].append(encrypt_message[i])

    # 打印解密信息
    for i in range(fence_number):
        s = 'decrypt_message_list' + str(i)
        print((vars()[s]))

    if remainder2 == 0:
        for q in range(basic_list_size):
            for i in range(fence_number):
                s = 'decrypt_message_list' + str(i)
                decrypt_message = decrypt_message + (vars()[s])[0]
                del (vars()[s])[0]
        print(decrypt_message)
    else:
        for q in range(basic_list_size + 1):
            for i in range(fence_number):
                s = 'decrypt_message_list' + str(i)
                if len((vars()[s])) > 0:
                    decrypt_message = decrypt_message + (vars()[s])[0]
                    del (vars()[s])[0]
                else:
                    pass
    print(decrypt_message)

else:
    print("Input Error!")