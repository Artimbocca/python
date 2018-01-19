import random

greekChars = ['Α', 'Β', 'Γ', 'Δ', 'Ε', 'Ζ', 'Η', 'Θ',
              'Ι', 'Κ', 'Λ', 'Μ', 'Ν', 'Ξ', 'Ο', 'Π',
              'Ρ', 'Σ', 'Τ', 'Υ', 'Φ', 'Χ', 'Ψ', 'Ω'];
nlChars = ['Α', 'Β', 'C', 'D', 'E', 'F', 'G', 'H',
           'Ι', 'J', 'K', 'L', 'Μ', 'Ν', 'O', 'P',
           'Q', 'R', 'S', 'Τ', 'U', 'V', 'W', 'Χ', 'Y', 'Z'];


def makeWord(chars, n):
    l = len(chars)
    c = ""
    for i in range(n):
        c += random.choice(chars)
    print(c, " bytes: ", len(bytearray(c,"utf-8")))
    print(c.encode('ascii', 'xmlcharrefreplace'))
    print(c.encode('ascii', 'backslashreplace'))
    print(c.encode('ascii', 'namereplace'))
    return c


makeWord(greekChars, 12)
makeWord(nlChars, 12)

