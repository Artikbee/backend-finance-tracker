from typing import TYPE_CHECKING

from starlette.middleware.cors import CORSMiddleware

from presentation.http.v1.middlewares.tracing import LoggingMiddleware

if TYPE_CHECKING:
    from fastapi import FastAPI

    from infrastructure.configs import APIConfig


def setup_middlewares(
        app: "FastAPI", /,
        api_config: "APIConfig",  # noqa: ARG001
) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        # f"http://localhost:{api_config.port}",
        # f"http://{api_config.host}:{api_config.port}",
        allow_credentials=False,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.add_middleware(LoggingMiddleware)
