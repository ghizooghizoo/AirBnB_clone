#!/usr/bin/python3
<<<<<<< HEAD
"""__init__magic method for models directory"""
from models.engine.file_storage import FileStorage

=======
'''create a unique FileStorage instance for the application'''
from models.engine.file_storage import FileStorage


'''A variable storage, an instance of FileStorage'''
>>>>>>> 8ab641b669c9dad7650615848ce92d5febba9c98
storage = FileStorage()
storage.reload()
