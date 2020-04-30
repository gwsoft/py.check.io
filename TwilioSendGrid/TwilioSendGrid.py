import re

def is_stressful(subj):
    """
    recognize stressful subject
    """
    result = False

    # 1st case: all letters are in uppercase
    if subj == subj.upper():
        #print("Found! All uppercase")
        return True

    # 2nd case: ends by at least 3 exclamation marks
    if subj[-3:] == '!!!':
        #print("Found! Three exlamation marks")
        return True

    # 3rd case: contains at least one "red" word
    red_words_patterns = ('^h+e+l+p+$',
                          '^a+s+a+p+$',
                          '^u+r+g+e+n+t+$')
    subj_words = subj.split()
    for x in subj_words:
        x = x.lower()
        # remove unwanted chars from the word
        xrem = x.replace('-','').replace('!','').replace('.','')
        #print('checking the word: ' + xrem)
        # check if the word matches red words patterns
        for pattern in red_words_patterns:
            check = re.match(pattern, xrem)
            if check:
                #print('-> that word matches pattern '  + pattern)
                result = True
                break
    return result
