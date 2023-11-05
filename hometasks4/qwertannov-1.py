class VigenereCipher(object):

    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet

    def encode(self, text):

        result = ''
        i = 0

        for char in text:

            if char not in self.alphabet:
                result += char
                i += 1

            else:
                message_index = self.alphabet.index(char)
                key_index = self.alphabet.index(self.key[i % len(self.key)])
                shift = (message_index + key_index) % len(self.alphabet)
                result += self.alphabet[shift]
                i += 1

        return result

    def decode(self, text):

        result = ''
        i = 0

        for char in text:

            if char not in self.alphabet:
                result += char
                i += 1
            else:
                message_index = self.alphabet.index(char)
                key_index = self.alphabet.index(self.key[i % len(self.key)])
                shift = (message_index - key_index) % len(self.alphabet)
                result += self.alphabet[shift]
                i += 1

        return result
