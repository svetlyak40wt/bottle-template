import os

activate_this = os.path.join(
    os.path.dirname(__file__),
    'env', 'bin', 'activate_this.py')

execfile(activate_this, dict(__file__=activate_this))

from app import application