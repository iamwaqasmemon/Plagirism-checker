from difflib import SequenceMatcher

a = input("Input First file Name")
b = input("Input 2nd file Name")

with open(a) as ff, open(b) as sf:
    f1 = ff.read()
    f2 = sf.read()

    ab = SequenceMatcher(None, f1, f2).ratio()

    ffin = int(ab * 100)
    print(f"{ffin}% Plagiarized Content")
