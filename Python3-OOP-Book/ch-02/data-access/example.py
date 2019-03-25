class SecretString:
    def __init__(self, secretstring, passcode):
        self.__secretstring = secretstring
        self.__passcode = passcode

    def decode(self, passcode):
        if self.__passcode == passcode:
            return self.__secretstring
        else:
            return "Wrong Passcode !"

if __name__ == "__main__":
    s = SecretString("Hot Chocolate !", "snow")
    print(s.decode("sand"))
    print(s.decode("snow"))
    print(s.__secretstring) # This will result in error.
    print(s._SecretString__secretstring) # This is the hack to bypass above error.
    