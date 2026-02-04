from __future__ import annotations

from typing import Any

import voluptuous as vol

from homeassistant.components import websocket_api
from homeassistant.core import HomeAssistant

from .const import DOMAIN
from .storage import ErdosPanelStorage


def async_setup_websocket(hass: HomeAssistant) -> None:
    hass.data.setdefault(DOMAIN, {})
    if hass.data[DOMAIN].get("websocket_registered"):
        return

    websocket_api.async_register_command(hass, ws_config_get)
    websocket_api.async_register_command(hass, ws_config_save)
    websocket_api.async_register_command(hass, ws_config_patch)
    websocket_api.async_register_command(hass, ws_config_reset)

    hass.data[DOMAIN]["websocket_registered"] = True


def _storage(hass: HomeAssistant) -> ErdosPanelStorage:
    return ErdosPanelStorage(hass)


@websocket_api.websocket_command(
    {
        vol.Required("type"): f"{DOMAIN}/config/get",
    }
)
@websocket_api.async_response
async def ws_config_get(
    hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]
) -> None:
    data = await _storage(hass).async_load()
    connection.send_result(msg["id"], data)


@websocket_api.websocket_command(
    {
        vol.Required("type"): f"{DOMAIN}/config/save",
        vol.Required("config"): dict,
    }
)
@websocket_api.async_response
async def ws_config_save(
    hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]
) -> None:
    config = msg["config"]
    if not isinstance(config, dict):
        raise vol.Invalid("config must be an object")
    await _storage(hass).async_save(config)
    connection.send_result(msg["id"], {})


@websocket_api.websocket_command(
    {
        vol.Required("type"): f"{DOMAIN}/config/patch",
        vol.Required("patch"): dict,
    }
)
@websocket_api.async_response
async def ws_config_patch(
    hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]
) -> None:
    patch = msg["patch"]
    if not isinstance(patch, dict):
        raise vol.Invalid("patch must be an object")

    current = await _storage(hass).async_load()
    current.update(patch)
    await _storage(hass).async_save(current)
    connection.send_result(msg["id"], current)


@websocket_api.websocket_command(
    {
        vol.Required("type"): f"{DOMAIN}/config/reset",
    }
)
@websocket_api.async_response
async def ws_config_reset(
    hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]
) -> None:
    data = await _storage(hass).async_reset()
    connection.send_result(msg["id"], data)
