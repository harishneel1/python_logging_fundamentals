import logging

file_handler = logging.FileHandler('app.log')
console_handler = logging.StreamHandler()


logging.basicConfig(
    level=logging.INFO, 
    format="%(asctime)s - %(levelname)s - %(message)s", 
    handlers=[file_handler, console_handler]
)

logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")

