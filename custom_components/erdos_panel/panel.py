from __future__ import annotations

from pathlib import Path

from homeassistant.components import panel_custom
from homeassistant.components.http import StaticPathConfig
from homeassistant.core import HomeAssistant

from .const import (
    DOMAIN,
    PANEL_FRONTEND_URL_PATH,
    PANEL_SIDEBAR_ICON,
    PANEL_SIDEBAR_TITLE,
    PANEL_WEBCOMPONENT_NAME,
    STATIC_URL_PATH,
)


async def async_setup_panel(hass: HomeAssistant) -> None:
    """Register static assets and the Home Assistant custom panel."""
    hass.data.setdefault(DOMAIN, {})
    if hass.data[DOMAIN].get("panel_registered"):
        return

    frontend_dir = Path(__file__).parent / "frontend"

    hass.http.async_register_static_paths(
        [StaticPathConfig(STATIC_URL_PATH, str(frontend_dir), cache_headers=False)]
    )

    panel_custom.async_register_panel(
        hass,
        webcomponent_name=PANEL_WEBCOMPONENT_NAME,
        frontend_url_path=PANEL_FRONTEND_URL_PATH,
        module_url=f"{STATIC_URL_PATH}/panel.js",
        sidebar_title=PANEL_SIDEBAR_TITLE,
        sidebar_icon=PANEL_SIDEBAR_ICON,
        require_admin=False,
        config={},
    )

    hass.data[DOMAIN]["panel_registered"] = True
