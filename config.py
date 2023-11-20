import os

app_dir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    FORMSD= [
        {
            'name': 'bla',
            'f_name1': 'email',
            'f_name2': 'phone'
         }
    ]


class DevConfig(BaseConfig):
    DEBUG = True


class TestConfig(BaseConfig):
    DEBUG = True


class ProdConfig(BaseConfig):
    DEBUG = False
