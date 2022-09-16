def caesarCipher(s, k):
    # Write your code here
    print("s:", s, "k:",k)
    if k >= 26:
        k = k % 26
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    enc_str = ""
    for el in s:
        capital_letter = False
        if el.isupper():
            capital_letter = True
        el = el.lower()
        try:
            idx = alphabet.index(el)
        except ValueError:
            enc_str += el
            continue
        if idx+k > len(alphabet)-1:
            if capital_letter:
                enc_str += alphabet[idx+k-(len(alphabet))].upper()
            else:
                enc_str += alphabet[idx+k-(len(alphabet))]
        else:
            if capital_letter:
                enc_str += alphabet[idx+k].upper()
            else:
                enc_str += alphabet[idx+k]

    return enc_str
