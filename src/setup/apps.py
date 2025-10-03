from contextlib import asynccontextmanager
from typing import AsyncIterator

from dishka import make_async_container, AsyncContainer
from dishka.integrations import fastapi as fastapi_integration
from fastapi import FastAPI, APIRouter
from fastapi.responses import ORJSONResponse

from infrastructure.configs import APIConfig, PostgresConfig
from presentation.http.v1.routers import user, account
from setup.configs import load_configs
from setup.db_tables import map_tables
from setup.exc_handlers import setup_exc_handlers
from setup.ioc import setup_providers


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    yield
    container: AsyncContainer = app.state.dishka_container
    await container.close()


def setup_http_routes(app: FastAPI) -> None:
    router_v1 = APIRouter(prefix="/v1")
    router_v1.include_router(user.router)
    router_v1.include_router(account.router)
    app.include_router(router_v1)


def make_fastapi_app() -> FastAPI:
    configs = load_configs()
    fastapi_app = FastAPI(
        lifespan=lifespan,
        default_response_class=ORJSONResponse,
        title="Finance Tracker API",
    )
    context = {APIConfig: configs.api, PostgresConfig: configs.db}
    container = make_async_container(*setup_providers(), context=context)
    map_tables()
    setup_http_routes(fastapi_app)
    setup_exc_handlers(fastapi_app)
    # setup_middlewares(fastapi_app, api_config=configs.api)
    fastapi_integration.setup_dishka(container, fastapi_app)
    return fastapi_app
