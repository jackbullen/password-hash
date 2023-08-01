# Sources:
# 1. Pseudo-code: 
    #https://resources.saylor.org/wwwresources/archived/site/wp-content/uploads/2012/07/SHA-1-1.pdf
# 2. Stackexchange question with implementation of the above pseudo-code:
    #https://codereview.stackexchange.com/questions/37648/python-implementation-of-sha1

# Note:    
# Not meant to be an optimized or well written implementation.
# Meant to be instructive and easy to read to understand SHA1.
    
def chunkify(l, n):
    # Taken from stackexchange source
    return [l[i:i+n] for i in range(0, len(l), n)]

def left_rotate(n, b):
    # Taken from stackexchange source
    return ((n << b) | (n >> (32 - b))) & 0xffffffff

def sha1(msg):
    # Majority of this function was self-written following the
    # pseudocode, however, many ideas and python implementations 
    #were taken from stackexchange source
    
    # Initialize the output bitstring variable
    out = ""
    
    # Initialize the landscape
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0
    
    # Pre-processing:
    #  1. Add the input string in bits in chunks of bytes to out
    for i,char in enumerate(msg):
        out += "{0:08b}".format(ord(char))
    # 2. Collect the length of bit string of the message
    pp_msg_length = len(out)
    # 3. Append the bit 1 to out, the output bitstring, so it is input_msg_bitstring1
    out += "1"
    # 4. Append the 0 bit to out until the length of out is equal congruent to 448 mod(512).
    while len(out)%512 != 448:
        out += "0"
    # 5. Append the original length of input in bitstring   
    out += "{0:064b}".format(pp_msg_length)
    
    # Processing:
    # 1. Split the message in 512 bit chunks

    for chunk in chunkify(out,512):
        
        w = [0]*80

        words = chunkify(chunk, 32)

        for i in range(0,16):
            w[i] = int(words[i], 2)
        for i in range(16,80):
            w[i] = left_rotate(w[i-3] ^ w[i-8] ^ w[i-14] ^ w[i-16], 1)
        
        a = h0
        b = h1
        c = h2
        d = h3
        e = h4
        
        for i in range(80):
            if 0<=i<=19:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif 20<=i<=39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif 40<=i<=59:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            elif 60<=i<=79:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = (left_rotate(a, 5)) + f + e + k + w[i] & 0xffffffff
            e = d
            d = c
            c = left_rotate(b, 30)
            b = a
            a = temp

        h0 = h0 + a & 0xffffffff
        h1 = h1 + b & 0xffffffff
        h2 = h2 + c & 0xffffffff
        h3 = h3 + d & 0xffffffff
        h4 = h4 + e & 0xffffffff
       
    return '%08x%08x%08x%08x%08x' % (h0, h1, h2, h3, h4)
import hashlib
print(sha1("Hello") == hashlib.sha1(b'Hello').hexdigest())
