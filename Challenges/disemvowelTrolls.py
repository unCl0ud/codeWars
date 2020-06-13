def disemvowel(string):
    '''This function removes the vowels from troll comments'''

    vowels = ['a','e','i','o','u','A','E','I','O','U']
    
    for x in string.lower():
        if x in vowels:
            string = string.replace(x, "")

    return string

mean = ("This website is for losers LOL!")

print(disemvowel(mean))