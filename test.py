
def is_equval(ar1, ar2):
    if len(ar1) != len(ar2):
        return False
    for i in range(len(ar1)):
        if ar1[i] != ar2[i]:
            return False
    return True

def rle_encode(data):
    MIN_COUNT = 2
    SAMPLE = [255, 255, 255]

    encode = []
    count = 0
    prev_i = None

    for i in data:
        if prev_i == None:
            prev_i = i
            continue
        if i == prev_i:
            count += 1
            if count >= 5:
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

    return encode

def rle_decode(data):
    SAMPLE = [255, 255, 255]

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
    return decode




test_ar = [66, 66, 55, 55, 55, 55, 55, 55, 66, 66, 66, 66, 66, 66, 66,2, 3, 4, 1, 31, 123, 34, 35, 66, 66, 66, 66, 66, 66, 66, 66, 66, 55, 55, 55,123, 55, 55, 55, 55, 55, 55, 55, 66, 66, 66, 66, 66, 66, 66, 66, 66]

ddd = rle_encode(test_ar)
print(ddd)
ddd = rle_decode(ddd)
print(test_ar)
print(ddd)
if is_equval(test_ar, ddd):
    print("GOOD")
else:
    print("BAD")

with open("mydatabase.db", "rb") as file:
    nol = []
    sample = [255, 255, 255]
    tmp = []
    data = file.read()
    size = len(data)
    counn = 0
    last = None
    for i in data:
        counn+=1
        proc = round((counn/size)*100)
        if proc % 5 == 0 and last != proc:
            last = proc
            print(f"{proc}%")
        tmp.append(i)
        if len(tmp) > 3:
            del tmp[0]

        if is_equval(sample, tmp):
            print(tmp)
            nol.append(0)



    print(nol)
    print(len(nol))
