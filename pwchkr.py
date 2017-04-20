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
    score = 0
    processed = [0 if x in symbols else (1 if x in upperList else 2 if x in lowerList else 3) for x in pw]
    lastStatus = processed[0]
    for index,x in enumerate(processed):
        if index != 0 and processed[index] == lastStatus:
            score -= 1
        else:
            score += 1
        lastStatus = processed[index]

    
