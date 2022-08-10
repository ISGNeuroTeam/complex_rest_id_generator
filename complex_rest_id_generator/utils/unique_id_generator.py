from typing import Dict
from .exceptions import *
import psycopg2
from super_id_generator import IDGenerator, generators
from super_id_generator.backends.postgres import PGBackend
from plugins.id_generator.settings import DB_INFO


class UniqueIdGenerator:
    """Wrapper over IDGenerator from super_id_generator lib"""

    SUPPORTED_TYPES = {  # get supported types from super_id_generator lib
        k for k in generators.__dict__ if isinstance(generators.__dict__[k], type) and type(generators.__dict__[k])
    }
    BACKEND_REQUIRED_TYPES = {  # if generator has db attribute it means that backend db is required
        k for k in SUPPORTED_TYPES if generators.__dict__[k]().db_connection_required
    }
    try:
        backend = PGBackend(
            connection=psycopg2.connect(database=DB_INFO['database'],
                                        host=DB_INFO['host'],
                                        port=DB_INFO['port'],
                                        user=DB_INFO['user'],
                                        password=DB_INFO['password'])
        )
    except Exception as e:
        backend = None

    @classmethod
    def create_unique_id_generator(cls, qs_args: Dict[str, any]) -> 'UniqueIdGenerator':
        """To evade raising exceptions from init - Factory method to create id generator from query string parameters"""
        amount = qs_args.get('amount', ['1'])
        id_type = qs_args.get('type')
        realm = qs_args.get('realm')
        entity = qs_args.get('entity')

        if not id_type:
            raise NoIdType
        id_type = id_type[0]
        if id_type not in cls.SUPPORTED_TYPES:
            raise UnknownIdType(id_type)
        if id_type in cls.BACKEND_REQUIRED_TYPES and not cls.backend:
            raise DatabaseConnectionRequired(id_type)
        if not realm:
            raise NoRealm
        realm = realm[0]

        if not entity:
            raise NoEntity
        entity = entity[0]

        amount = amount[0]
        if not amount.isdigit():
            raise AmountNotNumber(amount)
        amount = int(amount)
        if amount > 100 or amount < 1:
            raise AmountOutOfRange(amount)

        return UniqueIdGenerator(id_type, realm, entity, amount)

    def __init__(self, id_type: str, realm: str, entity: str, amount: int):
        self.id_type = id_type
        self.amount = amount
        self.realm = realm
        self.entity = entity
        self.gen = IDGenerator(backend=self.backend)

    def generate_ids(self):
        """
        Every supported type is a method in IDGenerator
        We can find self.id_type in IDGenerator methods and call it
        """
        return [
            self.gen.__getattribute__(self.id_type)(realm=self.realm, entity=self.entity) for _ in range(self.amount)
        ]
