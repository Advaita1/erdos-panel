import React from "react";
import { createRoot, type Root } from "react-dom/client";

import "./index.css";
import { setHass } from "./ha/hassStore";
import { App } from "./routes/app";

declare global {
  interface HTMLElementTagNameMap {
    "erdos-panel": ErdosPanelElement;
  }
}

export class ErdosPanelElement extends HTMLElement {
  private root: Root | null = null;
  private mounted = false;

  set hass(hass: unknown) {
    setHass(hass);
  }

  connectedCallback() {
    if (this.mounted) return;
    this.mounted = true;

    const mount = document.createElement("div");
    this.appendChild(mount);

    this.root = createRoot(mount);
    this.root.render(
      <React.StrictMode>
        <App />
      </React.StrictMode>,
    );
  }

  disconnectedCallback() {
    this.root?.unmount();
    this.root = null;
    this.mounted = false;
  }
}

customElements.define("erdos-panel", ErdosPanelElement);
