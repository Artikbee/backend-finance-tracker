from os import environ as env

from dotenv import load_dotenv

from infrastructure.configs import Configs, PostgresConfig, APIConfig


def load_configs(env_path: str = ".env") -> Configs:
    load_dotenv(dotenv_path=env_path)

    return Configs(
        db=PostgresConfig(
            user=env["POSTGRES_USER"],
            password=env["POSTGRES_PASSWORD"],
            host=env["POSTGRES_HOST"],
            port=env["POSTGRES_PORT"],
            db_name=env["POSTGRES_DB"],
            debug=env["POSTGRES_DEBUG"] == "true",
        ),
        api=APIConfig(
            host=env["UVICORN_HOST"],
            port=env["UVICORN_PORT"],
        ),
    )
