from __future__ import annotations

import logging

from homeassistant.core import HomeAssistant

from .panel import async_setup_panel
from .websocket import async_setup_websocket


_LOGGER = logging.getLogger(__name__)


async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Set up Erdos Panel from YAML (HACS-installed integration)."""
    _LOGGER.warning("Setting up Erdos Panel (async_setup)")
    await async_setup_panel(hass)
    async_setup_websocket(hass)
    return True


async def async_setup_entry(hass: HomeAssistant, entry) -> bool:
    """Set up Erdos Panel from a config entry."""
    _LOGGER.warning("Setting up Erdos Panel (async_setup_entry)")
    await async_setup_panel(hass)
    async_setup_websocket(hass)
    return True
