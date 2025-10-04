from dishka import Provider, Scope
from sqlalchemy.ext.asyncio import AsyncSession

from application.__common__.ports.jwt_service.jwt_service import JWTService
from application.__common__.ports.password_hasher_service.password_hasher_service import PasswordHasherService
from application.__common__.ports.persistence.account.gateway import AccountGateway
from application.__common__.ports.persistence.account.reader import AccountReader
from application.__common__.ports.persistence.category.gateway import CategoryGateway
from application.__common__.ports.persistence.category.reader import CategoryReader
from application.__common__.ports.persistence.entity_saver import EntitySaver
from application.__common__.ports.persistence.transaction_db import TransactionDB
from application.__common__.ports.persistence.user.gateway import UserGateway
from application.__common__.ports.persistence.user.reader import UserReader
from application.commands.account.create_account.handler import CreateAccountCommandHandler
from application.commands.account.delete_account.handler import DeleteAccountCommandHandler
from application.commands.account.update_account.handler import UpdateAccountCommandHandler
from application.commands.category.create_category.handler import CreateCategoryCommandHandler
from application.commands.user.delete_user import DeleteUserCommandHandler
from application.commands.user.login_user import LoginUserCommandHandler
from application.commands.user.logout_user import LogoutUserCommandHandler
from application.commands.user.register_user import RegisterUserCommandHandler
from application.commands.user.update_user import UpdateUserCommandHandler
from application.queries.account.get_account_by_id.handler import GetAccountByIDQueryHandler
from application.queries.account.get_accounts.handler import GetAccountsQueryHandler
from application.queries.category.get_categories.handler import GetCategoriesQueryHandler
from application.queries.user.get_user.handler import GetUserQueryHandler
from infrastructure.configs import APIConfig, PostgresConfig
from infrastructure.jwt.adapter import JWTServiceAdapter
from infrastructure.password_hasher.adapter import PasswordHasherServiceAdapter
from infrastructure.persistence.adapters.account import AccountGatewayAlchemy, AccountReaderAlchemy
from infrastructure.persistence.adapters.category import CategoryReaderAlchemy, CategoryGatewayAlchemy
from infrastructure.persistence.adapters.entity_saver import EntitySaverAlchemy
from infrastructure.persistence.adapters.transaction_db import TransactionDBAlchemy
from infrastructure.persistence.adapters.user import UserReaderAlchemy, UserGatewayAlchemy
from infrastructure.persistence.db_provider import get_engine, get_sessionmaker, get_session


def infrastructure_provider() -> Provider:
    provider = Provider(scope=Scope.REQUEST)
    _ = provider.provide(JWTServiceAdapter, provides=JWTService)
    _ = provider.provide(PasswordHasherServiceAdapter, provides=PasswordHasherService)
    return provider


def db_provider() -> Provider:
    provider = Provider(scope=Scope.REQUEST)
    _ = provider.provide(get_engine, scope=Scope.APP)
    _ = provider.provide(get_sessionmaker, scope=Scope.APP)
    _ = provider.provide(get_session, provides=AsyncSession)
    return provider


def configs_provider() -> Provider:
    provider = Provider()
    _ = provider.from_context(provides=APIConfig, scope=Scope.APP)
    _ = provider.from_context(provides=PostgresConfig, scope=Scope.APP)
    return provider


def gateways_provider() -> Provider:
    provider = Provider(scope=Scope.REQUEST)
    _ = provider.provide(TransactionDBAlchemy, provides=TransactionDB)
    _ = provider.provide(EntitySaverAlchemy, provides=EntitySaver)
    _ = provider.provide(UserReaderAlchemy, provides=UserReader)
    _ = provider.provide(UserGatewayAlchemy, provides=UserGateway)
    _ = provider.provide(AccountGatewayAlchemy, provides=AccountGateway)
    _ = provider.provide(AccountReaderAlchemy, provides=AccountReader)
    _ = provider.provide(CategoryReaderAlchemy, provides=CategoryReader)
    _ = provider.provide(CategoryGatewayAlchemy, provides=CategoryGateway)
    return provider


def interactors_provider() -> Provider:
    provider = Provider(scope=Scope.REQUEST)
    _ = provider.provide_all(
        DeleteUserCommandHandler,
        LoginUserCommandHandler,
        LogoutUserCommandHandler,
        RegisterUserCommandHandler,
        UpdateUserCommandHandler,
        GetUserQueryHandler,
        GetAccountsQueryHandler,
        GetAccountByIDQueryHandler,
        CreateAccountCommandHandler,
        UpdateAccountCommandHandler,
        DeleteAccountCommandHandler,
        CreateCategoryCommandHandler,
        GetCategoriesQueryHandler,
    )
    return provider


def setup_providers() -> tuple[Provider, ...]:
    return (
        configs_provider(),
        interactors_provider(),
        gateways_provider(),
        db_provider(),
        infrastructure_provider(),
    )
