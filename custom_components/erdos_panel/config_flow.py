from __future__ import annotations

from typing import Callable, cast

from homeassistant import config_entries

from .const import DOMAIN, PANEL_SIDEBAR_TITLE


def _already_configured(flow: config_entries.ConfigFlow) -> bool:
    return bool(flow._async_current_entries())


def _build_config_flow() -> type[config_entries.ConfigFlow]:
    try:

        class _ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):  # type: ignore[call-arg]
            VERSION = 1

            async def async_step_user(self, user_input=None):
                if _already_configured(self):
                    return self.async_abort(reason="single_instance_allowed")
                return self.async_create_entry(title=PANEL_SIDEBAR_TITLE, data={})

        return _ConfigFlow

    except TypeError:
        # Compatibility shim for HA versions where ConfigFlow doesn't accept
        # `domain=...` in the class definition.
        register = getattr(getattr(config_entries, "HANDLERS", None), "register", None)
        register = cast(Callable[[str], Callable[[type], type]] | None, register)

        if callable(register):

            @register(DOMAIN)
            class _ConfigFlowRegistered(config_entries.ConfigFlow):
                VERSION = 1

                async def async_step_user(self, user_input=None):
                    if _already_configured(self):
                        return self.async_abort(reason="single_instance_allowed")
                    return self.async_create_entry(title=PANEL_SIDEBAR_TITLE, data={})

            return _ConfigFlowRegistered

        class _ConfigFlowFallback(config_entries.ConfigFlow):
            VERSION = 1
            domain = DOMAIN

            async def async_step_user(self, user_input=None):
                if _already_configured(self):
                    return self.async_abort(reason="single_instance_allowed")
                return self.async_create_entry(title=PANEL_SIDEBAR_TITLE, data={})

        return _ConfigFlowFallback


ConfigFlow = _build_config_flow()
