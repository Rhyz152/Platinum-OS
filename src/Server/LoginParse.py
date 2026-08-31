#// Libs
import base64
import json

DatabaseFile = 'src/Server/Database/Data.json'

#// Function to parse login data and find matched account in database
def ParseLoginData(NameInput: str, PasswordInput: str) -> bool:
    print('parsing data')
    try:
        with open(file=DatabaseFile, encoding='utf-8') as rDataFile:
            ParsedDataFile = json.load(rDataFile)

            # Encode input
            bNameEncode: bytes = base64.b64encode(NameInput.encode('utf-8'))
            NameEncode: str = bNameEncode.decode('utf-8')
            bPassEncode: bytes = base64.b64encode(PasswordInput.encode('utf-8'))
            PassEncode: str = bPassEncode.decode('utf-8')

            #// Check if the encoded data matches anything in data base
            for Account in ParsedDataFile["Account"]:
                if NameEncode == Account:
                    pass

    except FileNotFoundError:
        return False

    return True

if __name__ == '__main__':
    LoginTry: bool = ParseLoginData('John', '1234')
    if not LoginTry:
        print('no')
    else:
        print('yes')