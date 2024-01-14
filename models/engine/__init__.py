#!/usr/bin/env python3
""" Update init.py"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
