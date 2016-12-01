# file SecretSantaConstraintSolver/settings.py
"""
Settings for secret santa
"""
from __future__ import division

import logging

__modname__ = "settings.py"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__modname__)

EMAIL_TEMPLATE = """Greetings {}!
You have been selected to be the Secret Santa for {}
"""

EMAIL_SUBJECT = "Your Secret Santa!"
GMAIL_SMTP_URL = "smtp.gmail.com"
GMAIL_SMTP_PORT = 587

try:
    from local_settings import SANTA_EMAIL, SANTA_PASSWORD
except ImportError:
    logger.error("Cannot import Santa's email and password from local_settings.py!, please add!")
    raise SystemExit