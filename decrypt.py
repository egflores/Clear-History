from sys import argv

script, answer, shifts = argv

shift = int(shifts)

shift2 = lambda txt,sft=1:''.join([[ch,chr((ord(ch) - ord(['A','a'][ch.islower()]) + sft)%26+ord(['A','a'][ch.islower()]))][ch.isalpha()] for ch in txt])

#test
print shift2(answer, shift)