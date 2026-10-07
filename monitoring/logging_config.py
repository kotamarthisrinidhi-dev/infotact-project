import logging
from pathlib import Path


# Create logs directory
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "atmosync_pipeline.log"


# Configure logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


logger = logging.getLogger("AtmoSync")


def get_logger():
    """
    Return the AtmoSync pipeline logger.
    """
    return logger


if __name__ == "__main__":

    logger.info("AtmoSync monitoring logger initialized.")

    print("=" * 50)
    print("AtmoSync Logging Setup")
    print("=" * 50)

    print(f"Log directory: {LOG_DIR}")
    print(f"Log file: {LOG_FILE}")
    print("Logging system initialized successfully.")