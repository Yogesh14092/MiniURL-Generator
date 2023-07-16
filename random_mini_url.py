import random
import string

NUM_CHARS_SHORT_LINK = 7
ALPHABET = string.ascii_uppercase + string.ascii_lowercase + string.digits

def generateRandomShortUrl():
    result = [None] * NUM_CHARS_SHORT_LINK
    while True:
        for i in range(NUM_CHARS_SHORT_LINK):
            randomIndex = random.randint(0, len(ALPHABET) - 1)
            result[i] = ALPHABET[randomIndex]
        shortLink = ''.join(result)
        # make sure the short link isn't already used
        if not DB.checkShortLinkExists(shortLink):
            return shortLink
