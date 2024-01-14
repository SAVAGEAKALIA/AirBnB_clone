#!/usr/bin/env python3
""" Update init.py"""

from engine.file_storage.py import FileStorage

storage = FileStorage()
storage.reload()
