from connexion import FlaskApp


app = FlaskApp(__name__, specification_dir='./swagger')
app.add_api('swagger.yaml')

__all__ = (
    'app',
)

# Imports que serão usados em outras partes do projeto que não será invocados
# fora desse módulo deverão ser importados no final do arquivo para evitar
# dependência ciclica.
from . import api
from . import services
from . import factory