class PasswordTooShortError(Exception):
    """Each password should be at least 8 characters long."""
    pass


class PasswordTooCommonError(Exception):
    """If the password consists of only digits, only letters, or only special characters."""
    pass


class PasswordNoSpecialCharactersError(Exception):
    """Each password should have at least 1 special character(from SPECIAL_CHARACTERS)."""
    pass


class PasswordContainsSpacesError(Exception):
    """If the password contains empty spaces."""
    pass


PASSWORD_MIN_LENGTH = 8
SPECIAL_CHARACTERS = ("@", "*", "&", "%")

password = input()

while password != "Done":

    if len(password) < PASSWORD_MIN_LENGTH:
        raise PasswordTooShortError("Password must contain at least 8 characters")

    elif password.isalpha() or password.isdigit() or all(char in SPECIAL_CHARACTERS for char in password):
        raise PasswordTooCommonError("Password must be a combination of digits, letters, and special characters")

    elif not any(char in SPECIAL_CHARACTERS for char in password):
        raise PasswordNoSpecialCharactersError("Password must contain at least 1 special character")

    elif " " in password:
        raise PasswordContainsSpacesError("Password must not contain empty spaces")

    print("Password is valid")

    password = input()
