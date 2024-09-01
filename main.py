
print("-------- WinPiska --------")

def rle_decode(data):
    encoding = bytes()
    is_byte = False
    prev_char = None
    for char in data:
        if char == b'\0':
            is_byte = True
        elif is_byte:
            if prev_char == None:
                prev_char = char
            else:
                count = int(char)
                for _ in range(count):
                    encoding += bytes([char])
                prev_char = None
                is_byte = False
        else:
            encoding += bytes([char])
    return encoding
def rle_encode(data):
    encoding = bytes()
    prev_char = data[0]
    count = 1
    for char in data[1:]:
        if char == prev_char:
            count += 1
            if count == 255:
                encoding += b'\0'
                encoding += bytes(prev_char)
                encoding += bytes(count)
                count = 0
        else:
            if count > 10:
                encoding += b'\0'
                encoding += bytes(prev_char)
                encoding += bytes(count)
            else:
                for _ in range(count):
                    encoding += bytes(prev_char)
            prev_char = char
            count = 0
    if count > 0:
        if count > 10:
            encoding += b'\0'
            encoding += bytes(prev_char)
            encoding += bytes(count)
        else:
            for _ in range(count):
                encoding += bytes(prev_char)
    else:
        encoding += bytes(prev_char)
    return encoding



data = None
size1, size2 = 0, 0

with open("1.jpg", "rb") as file:
    data = file.read()
    size1 = len(data)
    print("SIZE", file.name, len(data))


data = rle_encode(data)



with open("output.pipiska", "wb") as file:
    file.write(data)
    size2 = len(data)
    print("SIZE", file.name, len(data))

persent_compress = round((size2/size1)*100, 2)
print(f"COMPRESS = {100 - persent_compress} %")