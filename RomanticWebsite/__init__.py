"""
The flask application package.
"""

from flask import Flask # type: ignore
app = Flask(__name__)

import RomanticWebsite.views
