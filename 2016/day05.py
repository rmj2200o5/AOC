import hashlib
ipt = "ojvtpuvg"
search = "00000"


def part1():
    hashes = []
    x=0
    for i in range(8):
        while str(hashlib.md5(f"{ipt}{str(x)}".encode()).hexdigest())[:5]!=search:
            x+=1
        hashes.append(str(hashlib.md5(f"{ipt}{str(x)}".encode()).hexdigest()))
        print(str(hashlib.md5(f"{ipt}{str(x)}".encode()).hexdigest()))
        x+=1
    code = ""
    for hash in hashes:
        code+=hash[5]
    print(code)

def part2():
    hashes = {}
    x=0
    count = 0
    while count<8:
        while str(hashlib.md5(f"{ipt}{str(x)}".encode()).hexdigest())[:5]!=search:
            x+=1
        c = str(hashlib.md5(f"{ipt}{str(x)}".encode()).hexdigest())[5]
        if c.isalpha() or ord(c)<48 or ord(c)>55:
            x+=1
            continue
        if c in hashes:
            x+=1
            continue
        hashes[c]=str(hashlib.md5(f"{ipt}{str(x)}".encode()).hexdigest())
        count = len(hashes)
        x+=1
    code = [0,1,2,3,4,5,6,7]
    for hash in hashes:
        code[int(hash)] = hashes.get(hash)[6]
    out = "".join(code)
    print(out)

part1()
part2()