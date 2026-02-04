from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from homeassistant.core import HomeAssistant
from homeassistant.helpers.storage import Store

from .const import DOMAIN

STORAGE_VERSION = 1
STORAGE_KEY = f"{DOMAIN}.json"


def _default_config() -> dict[str, Any]:
    return {"version": 1, "dashboards": {}}


@dataclass
class ErdosPanelStorage:
    hass: HomeAssistant

    def __post_init__(self) -> None:
        self._store = Store(self.hass, STORAGE_VERSION, STORAGE_KEY)

    async def async_load(self) -> dict[str, Any]:
        data = await self._store.async_load()
        if isinstance(data, dict):
            return data
        return _default_config()

    async def async_save(self, data: dict[str, Any]) -> None:
        await self._store.async_save(data)

    async def async_reset(self) -> dict[str, Any]:
        data = _default_config()
        await self.async_save(data)
        return data

