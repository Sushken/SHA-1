def division_into_blocks(messageLength, blockSize):
    blocks = []
    for i in range(0, len(messageLength), blockSize):
        blocks.append(messageLength[i:i + blockSize])
    return blocks


def left_rotate(block, count):
    return ((block << count) | (block >> (32 - count))) & 0xffffffff


def sha1_Function(message):
    # Инициализация 5 32-битных значений
    A = 0x67452301
    B = 0xEFCDAB89
    C = 0x98BADCFE
    D = 0x10325476
    E = 0xC3D2E1F0

    messageLength = ""
    for char in range(len(message)):
        messageLength += '{0:08b}'.format(ord(message[char]))

    tmpLength = messageLength

    messageLength += '1'
    count = 0
    while len(messageLength) % 512 != 448:
        messageLength += '0'
        count += 1

    messageLength += '{0:064b}'.format(len(tmpLength))

    blocks = division_into_blocks(messageLength, 512)

    f = 0
    k = 0
    for block in blocks:
        words = division_into_blocks(block, 32)
        # print(words)
        w = []
        for n in range(0, 16):
            w.append(int(words[n], 2))

        for i in range(16, 80):
            w.append(left_rotate((w[i - 3] ^ w[i - 8] ^ w[i - 14] ^ w[i - 16]), 1))

        a = A
        b = B
        c = C
        d = D
        e = E

        for i in range(0, 80):
            if 0 <= i <= 19:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999

            elif 20 <= i <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1

            elif 40 <= i <= 59:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC

            elif 60 <= i <= 79:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = (left_rotate(a, 5) + f + e + k + w[i]) & 0xffffffff
            e = d
            d = c
            c = left_rotate(b, 30) & 0xffffffff
            b = a
            a = temp

        A = (A + a) & 0xffffffff
        B = (B + b) & 0xffffffff
        C = (C + c) & 0xffffffff
        D = (D + d) & 0xffffffff
        E = (E + e) & 0xffffffff

    return '%08x%08x%08x%08x%08x' % (A, B, C, D, E)


if __name__ == '__main__':
    # файл 1МБ 10МБ 100МБ
    input_text = "sha"
    sha1hash = sha1_Function(input_text)
    print(len(sha1hash))
    print(sha1hash)
