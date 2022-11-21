import hashlib
import json

def convertToSha1(string) -> str:
    encode_string = string.encode()
    sha_string = hashlib.sha1(encode_string)
    hexa_value = sha_string.hexdigest()
    return hexa_value


def convertToSha256(string) -> str:
    encode_string = string.encode()
    sha_string = hashlib.sha256(encode_string)
    hexa_value = sha_string.hexdigest()
    return hexa_value

string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!?"
dictionary = {}
for firstChar in range(len(string)):
    oneLetterPassword = string[firstChar]
    dictionary[convertToSha1(oneLetterPassword)] = oneLetterPassword
    dictionary[convertToSha256(oneLetterPassword)] = oneLetterPassword

    for secondChar in range(len(string)):
        twoLetterPassword = string[firstChar]+string[secondChar]
        dictionary[convertToSha1(twoLetterPassword)] = twoLetterPassword
        dictionary[convertToSha256(twoLetterPassword)] = twoLetterPassword

        for thirdChar in range(len(string)):
            threeLetterPassword = string[firstChar]+string[secondChar]+string[thirdChar]
            dictionary[convertToSha1(threeLetterPassword)] = threeLetterPassword
            dictionary[convertToSha256(threeLetterPassword)] = threeLetterPassword

print(len (dictionary))
json_object = json.dumps(dictionary, indent=4)
with open("data.json", "w") as outfile:
    outfile.write(json_object)
