import os

DATABASES = {
    "default": {
        "ENGINE": "backend.backoff_engine.postgres",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USERNAME"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
    },
}

WAIT_DB_TIMEOUT = int(os.getenv("WAIT_DB_TIMEOUT", 30))

