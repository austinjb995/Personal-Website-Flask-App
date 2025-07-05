import sys
import os
import logging

logging.basicConfig(stream=sys.stderr)

sys.path.insert(0, '/home/flaskapp')
sys.path.insert(0, '/home/flaskapp/app')

from app.app import app
