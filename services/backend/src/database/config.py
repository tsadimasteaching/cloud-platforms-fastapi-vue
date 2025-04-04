import os
from dotenv import load_dotenv

load_dotenv()

print(os.environ.get("DATABASE_URL"))
TORTOISE_ORM = {
    "connections": {"default": os.environ.get("DATABASE_URL")},
    "apps": {
        "models": {
            "models": [
                "src.database.models", "aerich.models"
            ],
            "default_connection": "default"
        }
    }
}
