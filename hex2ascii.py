hex_data = """  
01 10 19 62 F1 95 4A 61
01 21 6E 20 20 37 20 32
01 22 30 32 35 2E 43 32
01 23 38 31 2E 56 31 30
01 24 31 42 FF FF FF FF
"""  

# 清理数据并拆分为十六进制列表  
hex_values = hex_data.split()  
ascii_output = ""  

for hex_value in hex_values:  
    # 将十六进制转换为整数  
    decimal_value = int(hex_value, 16)  

    # 将可打印的ASCII字符转换为字符  
    if 32 <= decimal_value < 127:  
        ascii_output += chr(decimal_value)  
    else:  
        ascii_output += ' '  # 非打印字符用 表示

print(ascii_output)