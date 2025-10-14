import logging
import time
from enum import IntEnum

from starlette.middleware.base import (
    BaseHTTPMiddleware,
    RequestResponseEndpoint,
)
from starlette.requests import Request
from starlette.responses import Response
from typing_extensions import override

logger = logging.getLogger(__name__)


class BoundCode(IntEnum):
    INFORMATION = 199
    SUCCESSFUL = 299
    REDIRECT = 399
    CLIENT_ERROR = 499


class LoggingMiddleware(BaseHTTPMiddleware):
    @override
    async def dispatch(
            self,
            request: Request,
            call_next: RequestResponseEndpoint,
    ) -> Response:
        start_time = time.time()
        response = await call_next(request)
        duration = time.perf_counter() - start_time
        status_code = response.status_code
        client = request.client
        extra = {
            "method": request.method,
            "path": request.url.path,
            "url": str(request.url),
            "client": f"{client.host}:{client.port}" if client else None,
            "status": status_code,
            "duration_s": round(duration, 3),
            "req_size": int(request.headers.get("content-length", 0)),
            "res_size": int(response.headers.get("content-length", 0)),
        }

        if status_code <= BoundCode.INFORMATION:
            logger.info("Information response", extra=extra)
        elif status_code <= BoundCode.SUCCESSFUL:
            logger.info("Success response", extra=extra)
        elif status_code <= BoundCode.REDIRECT:
            logger.info("Redirect response", extra=extra)
        elif status_code <= BoundCode.CLIENT_ERROR:
            logger.warning("Client request error", extra=extra)
        else:
            logger.error("Server response error", extra=extra)

        return response
