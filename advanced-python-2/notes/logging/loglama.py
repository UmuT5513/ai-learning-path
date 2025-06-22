# BUILT-IN LOGGERS

# import logging


# logging.basicConfig(level=logging.DEBUG)


# logging.warning("Remain calm!")

# logging.debug("This is a debug message")

# logging.info("This is an info message")

# logging.warning("This is a warning message")

# logging.error("This is an error message")


# logging.critical("This is a critical message")




# import logging
# logging.basicConfig(
#     format="{asctime} - {levelname} - {message}",
#     style="{",
#     datefmt="%Y-%m-%d %H:%M",
# )
# logging.error("This is a error message")



# import logging 
# logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', 
#                     datefmt='%Y-%m-%d %H:%M:%S', 
#                     level=logging.DEBUG,
#                     style="{",
#                     filename="app.log",
#                     filemode='a',
#                     encoding='utf-8'
#                     )
# logging.warning("save me!")



# import logging
# name="Umut"
# logging.basicConfig(level=logging.DEBUG)
# logging.debug(f"{name=}")




# import logging
logging.basicConfig(
    filename="app.log",
    encoding="utf-8",
    filemode="a",
    format="{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M",
)

# donuts = 5
# guests = 0
# try:
#     donuts_per_guest = donuts / guests
# except ZeroDivisionError:
#     logging.error("DonutCalculationError", exc_info=True)
#     #logging.exception("DonutCalculationError")


# So far, you’ve seen the default logger named root, which is used by the logging module whenever functions like logging.debug(), logging.warning(), and so on are called.
#CUSTOM LOGGER

