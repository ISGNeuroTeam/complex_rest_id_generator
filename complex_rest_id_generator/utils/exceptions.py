class NoIdType(Exception):

    def __init__(self):
        super().__init__('Id type not provided')


class NoRealm(Exception):

    def __init__(self):
        super().__init__('Realm not provided')


class NoEntity(Exception):

    def __init__(self):
        super().__init__('Entity not provided')


class UnknownIdType(Exception):

    def __init__(self, id_type):
        super().__init__(f'Unknown id type: {id_type}')


class DatabaseConnectionRequired(Exception):

    def __init__(self, id_type):
        super().__init__(f'Database connection required for id type: {id_type}')


class AmountNotNumber(Exception):

    def __init__(self, amount):
        super().__init__(f'amount: {amount} is not a number')


class AmountOutOfRange(Exception):

    def __init__(self, amount):
        super().__init__(f'Can generate from 1 to 100 ids per request. {amount} was requested')
