import sys

def threshCheck(pw):
    upperList = "QAZWSXEDCRFVTGBYHNUJMIKOLP"
    lowerList = "qazwsxedcrfvtgbyhnujmikolp"
    return len([x for x in pw if x in upperList]) > 0 and \
        len([x for x in pw if x in lowerList]) > 0 and \
        len([x for x in pw if x.isdigit()]) > 0

def strRating(pw):
    symbols = ".?!&#,;:-_*"
    upperList = "QAZWSXEDCRFVTGBYHNUJMIKOLP"
    lowerList = "qazwsxedcrfvtgbyhnujmikolp"
    if not threshCheck(pw):
        return 0
    score = len(pw) + len([x for x in pw if x in symbols])
    processed = [0 if x in symbols else (1 if x in upperList else 2 if x in lowerList else 3) for x in pw]
    lastStatus = processed[0]
    chain = 0
    for index,x in enumerate(processed):
        if index != 0 and processed[index] == lastStatus:
            chain += 1
        else:
            score += 1
            if chain >= 2:
                score -= chain / 10
            chain = 1
        lastStatus = processed[index]
    final = score/1000 * 3
    if 0 in processed:
        final += 3
    if 3 in processed:
        final += 2
    if 1 in processed:
        final += 1
    if 2 in processed:
        final += 2
    return final

print "Enter password"
line = raw_input('> ')
print "Strength of " + line + ": " + str(strRating(line))
