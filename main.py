
print("-------- WinPiska --------")
def rle_encode(data):
    encoding = bytearray()
    prev_char = data[0]
    count = 1

    for char in data[1:]:
        if char == prev_char:
            count += 1
            if count == 255:  # максимальное значение для байта
                encoding.extend([count, prev_char])
                count = 0
        else:
            if count > 10:
                print("SSSSS", count)
            if count > 0:
                encoding.extend([count, prev_char])
            prev_char = char
            count = 1

    # Обработка последней серии символов
    if count > 0:
        encoding.extend([count, prev_char])

    return encoding



data = None
size1, size2 = 0, 0

with open("1.jpg", "rb") as file:
    data = file.read()
    size1 = len(data)
    print("SIZE", file.name, len(data))


rle_encode(data)



with open("output.pipiska", "wb") as file:
    file.write(data)
    size2 = len(data)
    print("SIZE", file.name, len(data))

persent_compress = round((size2/size1)*100, 2)
print(f"COMPRESS = {100 - persent_compress} %")