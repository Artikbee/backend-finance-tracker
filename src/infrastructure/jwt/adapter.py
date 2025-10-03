from datetime import datetime, timedelta, timezone
from typing import Tuple, Literal

import jwt

from application.__common__.ports.jwt_service.jwt_service import JWTService
from domains.user.models import UserID
from infrastructure.__common__.errors.jwt_error import JWTError


class JWTServiceAdapter(JWTService):
    def __init__(self):
        self._jwt_secret = "super_secret_key"
        self._jwt_algorithm = "HS256"
        self._access_token_expire_minutes = 30
        self._refresh_token_expire_minutes = 600

    async def generate(self, user_id: UserID) -> Tuple[str, str]:
        now = datetime.now(timezone.utc)

        access_payload = {
            "sub": str(user_id),
            "iat": now,
            "exp": now + timedelta(minutes=self._access_token_expire_minutes),
            "type": "access"
        }
        access_token = jwt.encode(
            access_payload,
            self._jwt_secret,
            algorithm=self._jwt_algorithm
        )

        refresh_payload = {
            "sub": str(user_id),
            "iat": now,
            "exp": now + timedelta(minutes=self._refresh_token_expire_minutes),
            "type": "refresh"
        }
        refresh_token = jwt.encode(
            refresh_payload,
            self._jwt_secret,
            algorithm=self._jwt_algorithm
        )
        return access_token, refresh_token

    async def get_expires_time(self) -> Tuple[int, int]:
        return self._access_token_expire_minutes, self._refresh_token_expire_minutes

    async def verify_and_get_user_id(
            self,
            token: str,
            expected_type: Literal["access", "refresh"] | None = None
    ) -> UserID:
        try:
            payload = jwt.decode(
                token,
                self._jwt_secret,
                algorithms=[self._jwt_algorithm],
            )

            if expected_type and payload.get("type") != expected_type:
                raise JWTError()  # Invalid token type

            user_id = payload.get("sub")
            if not user_id:
                raise JWTError()  # user_id not found in token

            return UserID(int(user_id))

        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
            raise JWTError()  # Token has expired and Invalid token
