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