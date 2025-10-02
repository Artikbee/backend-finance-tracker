In this project, I try to cover everything with tests. However, in a real project, you will most likely not have enough time to test absolutely everything. Therefore, it’s better to focus on writing tests for authentication and authorization, as well as for key business processes (for example, the shopping cart or product creation).

You can add `Keycloack` for auth.
https://www.keycloak.org/

You can add `ouuid` in `src/domains/__common__/base_entity.py`.
The UUID will be provided by a third-party service or API. The ID is used internally by the service.

```python
from dataclasses import dataclass
from typing import Generic, TypeVar

OIDType = TypeVar("OIDType")
OUUIDType = TypeVar("OUUIDType")


@dataclass
class BaseEntity(Generic[OIDType, OUUIDType]):
    oid: OIDType
    ouuid: OUUIDType
```