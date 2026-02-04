# Erdos Panel

Home Assistant custom integration (HACS) that registers a React-based Custom Panel (sidebar page) and serves its static assets from the integration (no external backend).

## Install (HACS)

1. HACS → menu → **Custom repositories** → add this repo as **Integration**.
2. HACS → install **Erdos Panel**.
3. Home Assistant → **Settings → Devices & services → Add integration → Erdos Panel**.
4. Restart Home Assistant.
5. Open **Erdos Panel** from the sidebar.

Notes:
- The built frontend assets are committed to `custom_components/erdos_panel/frontend/` so Home Assistant can serve them directly.
- If you update the repo, restart Home Assistant and hard refresh your browser to clear cached JS.

## Development

This repo uses `pnpm` workspaces.

### Frontend (local)

```bash
pnpm install
pnpm dev
```

### Build assets for Home Assistant

```bash
pnpm run build
```

This produces deterministic `panel.js` (and `panel.css`) and copies them into `custom_components/erdos_panel/frontend/`.

## WebSocket API

- `erdos_panel/config/get`
- `erdos_panel/config/save`
- `erdos_panel/config/patch`
- `erdos_panel/config/reset`

Initial permission model is permissive: one global config that any authenticated user can read/write. Tighten later if needed.
