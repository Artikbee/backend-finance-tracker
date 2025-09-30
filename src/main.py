import logging

from fastapi import FastAPI

from setup.apps import make_fastapi_app

logger = logging.getLogger(__name__)


def create_app() -> FastAPI:
    fastapi_app = make_fastapi_app()
    logger.info(msg="App created", extra={"app_version": fastapi_app.version})
    return fastapi_app
