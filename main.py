import logging
import database
import auth


logging.basicConfig( 
    level=logging.INFO, 
    format="%(asctime)s - %(levelname)s - %(message)s", 
)

logger = logging.getLogger(__name__)

logger.info("Application started")
database.connect()
database.query_users()
auth.login("alice")
auth.logout("alice")
logger.info("Application finished")
