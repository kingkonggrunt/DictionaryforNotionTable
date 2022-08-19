import logging

 
def error_handler(filename: str=".logs/errors.log"):
    handler = logging.FileHandler(filename)
    handler.setLevel(logging.ERROR)
    format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(format)
    return handler

def definition_found(filename: str=".logs/words_found.log"):
    handler = logging.FileHandler(filename)
    handler.setLevel(logging.INFO)
    format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(format)
    return handler

def definition_not_found(filename: str=".logs/words_notfound.log"):
    handler = logging.FileHandler(filename)
    handler.setLevel(logging.WARNING)
    format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(format)
    return handler
    
def streaming():
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(format)
    return handler
