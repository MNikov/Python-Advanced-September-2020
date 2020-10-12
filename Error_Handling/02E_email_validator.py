class NameTooShortError(Exception):
    """Raised when the name len is less or equal to 4"""


class MustContainAtSymbolError(Exception):
    """Raised when there is no @ in the email"""


class InvalidDomainError(Exception):
    """Raised when the domain is not .com, .bg, .net or .org"""


def validate_name(email):
    name = email.split('@')[0]
    if len(name) <= 4:
        raise NameTooShortError('Name must be more than 4 characters')


def validate_at_symbol(email):
    if '@' not in email:
        raise MustContainAtSymbolError('Email must contain @')


def validate_domain(email, valid_domains):
    domain = email.split('.')[-1]
    if domain not in valid_domains:
        raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')


valid_domains = ('com', 'bg', 'net', 'org')

while True:
    email = input()
    if email == 'End':
        break
    validate_name(email)
    validate_at_symbol(email)
    validate_domain(email, valid_domains)
    print('Email is valid')
