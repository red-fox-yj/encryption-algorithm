'''
简单要求：
    自己写一个加密程序，能够加密的内容是英文和汉字。同时加密并且解密
    就是说，一段话中既有中文又有英文，标点符号不用处理。
    加密规则，获取ascii码数字，中间用|分割 
    
    # 思路提示：
    print(ord("我"))
    print(chr(25105))
    
    扩展内容：自定义规则玩起来
    
规则：
    加密：先将字符转化为ASCII码对应的十进制数，再针对不同的字符按照各个不同的公式的转化为不同的数据，加上类型进行存储
    
    解密：根据不同类型及公式，进行反向转化
    
不足：
1、转化公式比较随机，没什么逻辑，其他人看可能不太好理解，但这就不是优势嘛
2、注释写得有点乱


'''


# 加密过程
def encrypt_string(message):
    encode_result = ""
    for char in message:
        char_int = ord(char)
        if char.isalpha():  # 判断是否为字母
            if 64 < char_int < 78 or 96 < char_int < 110:  # 针对其中的部分字母进行加密
                encode_result += "00" + str((char_int + 13) * 2) + "|"
            else:  # 对剩下字母进行加密
                encode_result += "01" + str(char_int - 23) + "|"

        elif '\u4e00' <= char <= '\u9fff':  # 单个汉字可以这么判断
            encode_result += "02" + str(char_int + 24) + "|"
        else:  # 对数字、特殊字符进行加密
            encode_result += "03" + str(char_int) + "|"

    print("Encode result: {}".format(encode_result))

    return encode_result


# 解密过程
def decrypt_string(message):
    decode_result = ""

    # 将message转换为list
    message_list = message.split("|")
    message_list.remove("")  # 移除list中的空元素

    for i in message_list:
        type_ = i[:2]
        char_number = int(i[2:])
        if type_ == "00":
            char_number = int(char_number / 2 - 13)
        elif type_ == "01":
            char_number = char_number + 23
        elif type_ == "02":
            char_number = char_number - 24
        else:
            char_number = char_number

        decode_result += chr(char_number)

    print("Decode result: {}".format(decode_result))


if __name__ == '__main__':
    # 输入要加密的字符
    message = input("Please input your message>>>>")
    print("Input message: {}".format(message))

    # 加密
    mes = encrypt_string(message)

    # 解密
    decrypt_string(mes)