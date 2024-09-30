class NameTooShortError(Exception):
    """When the name in the email is less than or equal to 4."""
    pass


class MustContainAtSymbolError(Exception):
    """When there is no "@" in the email."""
    pass


class InvalidDomainError(Exception):
    """When the domain of the email is invalid(not in VALID_DOMAINS)."""
    pass


VALID_DOMAINS = (".com", ".bg", ".org", ".net")
NAME_MIN_SYMBOLS = 4

email = input()

while email != "End":

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")
    elif len(email.split("@")[0]) <= NAME_MIN_SYMBOLS:
        raise NameTooShortError("Name must be more than 4 characters")
    elif f".{email.split('.')[-1]}" not in VALID_DOMAINS:
        raise InvalidDomainError(f"Domain must be one of the following: {', '.join(VALID_DOMAINS)}")
        # using the constant in the error message ensures changing it in just one place if it is needed later

    print("Email is valid")

    email = input()
