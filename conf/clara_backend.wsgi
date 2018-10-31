activate_this = '/var/www/clara_backend/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import sys
path = '/var/www/clara_backend/src'
if path not in sys.path:
    sys.path.insert(0, path)

from clara_backend import app as application
