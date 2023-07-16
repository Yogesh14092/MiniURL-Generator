import hashlib

SHORT_URL_CHAR_SIZE = 7

def convert(longURL):
    try:
        # Create MD5 Hash
        digest = hashlib.md5()
        digest.update(longURL.encode())
        messageDigest = digest.digest()
        # Create Hex String
        hexString = ''.join(format(byte, '02x') for byte in messageDigest)
        return hexString
    except Exception as e:
        raise RuntimeError(e)

def generateRandomShortUrl(longURL):
    hash = convert(longURL)
    numberOfCharsInHash = len(hash)
    counter = 0
    while counter < numberOfCharsInHash - SHORT_URL_CHAR_SIZE:
        if not DB.exists(hash[counter:counter+SHORT_URL_CHAR_SIZE]):
            return hash[counter:counter+SHORT_URL_CHAR_SIZE]
        counter += 1

