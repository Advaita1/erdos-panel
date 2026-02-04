from __future__ import annotations

from homeassistant.core import HomeAssistant

from .panel import async_setup_panel
from .websocket import async_setup_websocket


async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Set up Erdos Panel from YAML (HACS-installed integration)."""
    await async_setup_panel(hass)
    async_setup_websocket(hass)
    return True


async def async_setup_entry(hass: HomeAssistant, entry) -> bool:
    """Set up Erdos Panel from a config entry."""
    await async_setup_panel(hass)
    async_setup_websocket(hass)
    return True
