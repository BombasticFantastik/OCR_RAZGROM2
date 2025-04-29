def get_normal_word(word):
    normal_word=''
    for i in range(len(word)-1):
        if word[i]!=word[i+1]:
            normal_word+=word[i]
    return normal_word

