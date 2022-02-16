"""Defines constants and settings for the package."""

# Logging configuration for both, Uvicorn server
# and gunicorn server in docker container.
LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "simple": {
            "format": ("%(asctime)s %(levelname)-9s %(threadName)-25s"
                       " %(name)-25s %(message)s")
        },
        "extended": {
            "format": ("%(asctime)s %(levelname)-9s %(threadName)-25s "
                       "%(name)-25s %(message)s "
                       "[%(pathname)s:%(funcName)s:%(lineno)d]")
        }
    },
    "handlers": {
        "console": {
            "formatter": "simple",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
            "level": "DEBUG"
        },
        "error": {
            "formatter": "extended",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
            "level": "ERROR"
        }
    },
    "loggers": {
        "app": {
            "handlers": ["console", "error"],
            "propagate": False,
            "level": "DEBUG"
        },
        "fastapi": {
            "propagate": False,
            "handlers": ["console"]
        },
        "gunicorn.access": {
            "handlers": ["console"],
            "propagate": False
        },
        "gunicorn.error": {
            "propagate": False,
            "handlers": ["console"]
        },
        "uvicorn": {
            "propagate": False,
            "handlers": ["console"]
        },
        "uvicorn.access": {
            "propagate": False,
            "handlers": ["console"]
        },
        "uvicorn.asgi": {
            "propagate": False,
            "handlers": ["console"]
        },
        "uvicorn.error": {
            "propagate": False,
            "handlers": ["console"]
        },
    },

    "root": {
        "handlers": ["console"],
        "level": "INFO"
    }
}
