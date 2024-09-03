IN_FILENAME = "mydatabase.db"
OUT_FILENAME = "out.db"

MIN_LEN = 50
DEFOULT_SAMPLE = [255, 255, 255]


print("-------- WinPiska --------")
def is_equval(ar1, ar2):
    if len(ar1) != len(ar2):
        return False
    for i in range(len(ar1)):
        if ar1[i] != ar2[i]:
            return False
    return True

def rle_encode(data):
    MIN_COUNT = MIN_LEN
    SAMPLE = DEFOULT_SAMPLE

    encode = []
    count = 0
    prev_i = None

    for i in data:
        if prev_i == None:
            prev_i = i
            continue
        if i == prev_i:
            count += 1
            if count >= 254:
                for t in SAMPLE:
                    encode.append(t)
                encode.append(prev_i)
                encode.append(count)
                count = 0
                prev_i = None
        else:
            if count > MIN_COUNT:
                for t in SAMPLE:
                    encode.append(t)
                encode.append(prev_i)
                encode.append(count)
            else:
                encode.append(prev_i)
                for _ in range(count):
                    encode.append(prev_i)
            count = 0
            prev_i = i
    if prev_i != None:
        if count > MIN_COUNT:
            for t in SAMPLE:
                encode.append(t)
            encode.append(prev_i)
            encode.append(count)
        else:
            encode.append(prev_i)
            for _ in range(count):
                encode.append(prev_i)
    return bytes(encode)

def rle_decode(data):
    SAMPLE = DEFOULT_SAMPLE

    decode = []
    tmp_sample = []
    prev_i = None
    is_char = False
    char = None
    is_count = False

    for i in data:
        if len(tmp_sample) < len(SAMPLE)-1:
            tmp_sample.append(i)
            continue
        if is_char == False:
            tmp_sample.append(i)
            if len(tmp_sample) > len(SAMPLE):
                decode.append(tmp_sample[0])
                del tmp_sample[0]
        if is_equval(SAMPLE, tmp_sample):
            if is_char == False:
                is_char = True
                continue
            if is_char and is_count == False:
                char = i
                is_count = True
                continue
            if is_count:
                decode.append(char)
                for _ in range(i):
                    decode.append(char)
                is_char = False
                is_count = False
                tmp_sample = []
    for i in tmp_sample:
        decode.append(i)
    return bytes(decode)


data = None
size1, size2 = 0, 0

with open(IN_FILENAME, "rb") as file:
    data = file.read()
    size1 = len(data)
    print("SIZE", file.name, len(data))


data = rle_encode(data)



with open("output.pipiska", "wb") as file:
    file.write(data)
    size2 = len(data)
    print("SIZE", file.name, len(data))

persent_compress = round((size2/size1)*100, 2)
print(f"COMPRESS = {round(100 - persent_compress, 2)} %")


with open("output.pipiska", "rb") as file:
    data = file.read()
    print("SIZE", file.name, len(data))

data = rle_decode(data)


with open(OUT_FILENAME, "wb") as file:
    file.write(data)
    size2 = len(data)
    print("SIZE", file.name, len(data))

persent_compress = round((size2/size1)*100, 2)
print(f"LESS = {round(100 - persent_compress, 2)} %")
