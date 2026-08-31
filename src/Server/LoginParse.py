#// Libs
import base64
import json
from pathlib import Path

DatabaseFile = Path(__file__).resolve().parent / 'Database' / 'Data.json'


#// Function to parse login data and find matched account in database
def ParseLoginData(NameInput: str, PasswordInput: str) -> bool:
    print(f'[LoginParser]: checking username={NameInput}')

    try:
        with open(DatabaseFile, 'r', encoding='utf-8') as rDataFile:
            ParsedDataFile = json.load(rDataFile)

        # Encode input using same format as stored database
        NameEncode = base64.b64encode(NameInput.encode('utf-8')).decode('utf-8')
        PassEncode = base64.b64encode(PasswordInput.encode('utf-8')).decode('utf-8')

        Accounts = ParsedDataFile.get('Accounts', {})
        StoredPassword = Accounts.get(NameEncode)

        if StoredPassword is None:
            print('[LoginParser]: username not found')
            return False

        if StoredPassword == PassEncode:
            print('[LoginParser]: login successful')
            return True

        print('[LoginParser]: password mismatch')
        return False

    except FileNotFoundError:
        print(f'[LoginParser]: database not found at {DatabaseFile}')
        return False


def ParseLoginPayload(RawData: str):
    if ':' in RawData:
        return RawData.split(':', 1)
    raise ValueError('Payload must be in username:password format')


if __name__ == '__main__':
    LoginTry: bool = ParseLoginData('John', '1234')
    if not LoginTry:
        print('no')
    else:
        print('yes')