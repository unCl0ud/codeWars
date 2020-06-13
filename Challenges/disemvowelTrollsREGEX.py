import re
def disemvowel(string):
    '''This function removes the vowels from troll comments'''

    string = re.sub("[aeiouAEIOU]","",string)
    return string

mean = ("This website is for losers LOL!")

print(disemvowel(mean))