from __future__ import annotations

import logging
from pathlib import Path

from homeassistant.components import panel_custom
from homeassistant.components.http import StaticPathConfig
from homeassistant.const import EVENT_HOMEASSISTANT_STARTED
from homeassistant.core import HomeAssistant
from homeassistant.helpers.event import async_listen_once

from .const import (
    DOMAIN,
    PANEL_FRONTEND_URL_PATH,
    PANEL_SIDEBAR_ICON,
    PANEL_SIDEBAR_TITLE,
    PANEL_WEBCOMPONENT_NAME,
    STATIC_URL_PATH,
)


_LOGGER = logging.getLogger(__name__)


async def async_setup_panel(hass: HomeAssistant) -> None:
    """Register static assets and the Home Assistant custom panel."""
    hass.data.setdefault(DOMAIN, {})
    if hass.data[DOMAIN].get("panel_registered"):
        return

    # In some startup orders (especially during early bootstrap), the HTTP
    # component may not be ready yet. Defer panel registration until HA is
    # started.
    if getattr(hass, "http", None) is None:
        if not hass.data[DOMAIN].get("panel_registration_scheduled"):
            hass.data[DOMAIN]["panel_registration_scheduled"] = True
            _LOGGER.debug("HTTP not ready yet; deferring panel registration")

            async_listen_once(
                hass,
                EVENT_HOMEASSISTANT_STARTED,
                lambda _event: hass.async_create_task(async_setup_panel(hass)),
            )
        return

    frontend_dir = Path(__file__).parent / "frontend"

    if not (frontend_dir / "panel.js").exists():
        _LOGGER.warning(
            "panel.js not found at %s; the sidebar entry will exist but the panel may not load",
            frontend_dir,
        )

    hass.http.async_register_static_paths(
        [StaticPathConfig(STATIC_URL_PATH, str(frontend_dir), cache_headers=False)]
    )

    module_url = f"{STATIC_URL_PATH}/panel.js"
    try:
        panel_custom.async_register_panel(
            hass,
            webcomponent_name=PANEL_WEBCOMPONENT_NAME,
            frontend_url_path=PANEL_FRONTEND_URL_PATH,
            module_url=module_url,
            sidebar_title=PANEL_SIDEBAR_TITLE,
            sidebar_icon=PANEL_SIDEBAR_ICON,
            require_admin=False,
            config={},
        )
    except TypeError:
        # Backwards/forwards compat: HA has historically changed kwarg names.
        panel_custom.async_register_panel(
            hass,
            webcomponent_name=PANEL_WEBCOMPONENT_NAME,
            frontend_url_path=PANEL_FRONTEND_URL_PATH,
            js_url=module_url,
            sidebar_title=PANEL_SIDEBAR_TITLE,
            sidebar_icon=PANEL_SIDEBAR_ICON,
            require_admin=False,
            config={},
        )

    hass.data[DOMAIN]["panel_registered"] = True
    _LOGGER.info("Registered Erdos Panel sidebar entry at /%s", PANEL_FRONTEND_URL_PATH)
