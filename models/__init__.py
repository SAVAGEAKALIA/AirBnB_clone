#!/usr/bin/env python3
""" Update init.py"""

# from models.engine.file_storage import FileStorage
from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
