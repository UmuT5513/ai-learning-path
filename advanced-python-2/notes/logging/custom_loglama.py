# import logging

# logger = logging.getLogger(__name__)
# logger.warning("Look at my logger")

# #add handlers
# console_handler = logging.StreamHandler()
# file_handler = logging.FileHandler("custom_app.log", mode='a', encoding='utf-8')

# logger.addHandler(console_handler)
# logger.addHandler(file_handler)
# print(logger.handlers)
# logger.warning("watch out! my custom logger")


# #adding formatter to my handlers
# formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s",
#                               style="%",
#                               datefmt="%Y-%m-%d %H:%M",
#                               )
# console_handler.setFormatter(formatter)
# logger.warning("stay calm!")




# setting log levels to custom loggers
# import logging

# logger = logging.getLogger(__name__)
# logger.setLevel("DEBUG")
# formatter = logging.Formatter("{levelname} - {message}", style="{")

# console_handler = logging.StreamHandler()
# console_handler.setLevel("DEBUG")
# console_handler.setFormatter(formatter)
# logger.addHandler(console_handler)


# file_handler = logging.FileHandler("custom_app.log", mode='a', encoding='utf-8')
# file_handler.setLevel("WARNING")
# file_handler.setFormatter(formatter)
# logger.addHandler(file_handler)


# logger.debug("debug message")
# logger.warning("warning message")
# logger.error("stay put")
# print(console_handler)
# print(file_handler)



# filtering logs: leveraging different log levels.
def tanım():
    '''there are three approaches to creating filters for logging. You can create a:

    -*Subclass* of logging.Filter() and overwrite the .filter() method

    -*Class* that contains a .filter() method

    -*Callable* that resembles a .filter() method
    '''

import logging

def show_only_debug(record):
    return record.levelname == "DEBUG"

logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")
formatter = logging.Formatter("{levelname} - {message}", style="{")

console_handler = logging.StreamHandler()
console_handler.setLevel("DEBUG")
console_handler.setFormatter(formatter)
console_handler.addFilter(show_only_debug)
logger.addHandler(console_handler)

file_handler = logging.FileHandler("custom_app.log", mode="w", encoding="utf-8")
file_handler.setLevel("WARNING")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

logger.debug("Just checking in!") #konsola yazılır


logger.warning("Stay curious!") # custom_app.log a yazılır
logger.error("Stay put!") # bu da