import type { HomeAssistantLike } from './types';

type Listener = () => void;

let hass: HomeAssistantLike | null = null;
const listeners = new Set<Listener>();

export function setHass(next: unknown) {
  hass = next as HomeAssistantLike;
  for (const listener of listeners) listener();
}

export function getHass() {
  return hass;
}

export function subscribe(listener: Listener) {
  listeners.add(listener);
  return () => {
    listeners.delete(listener);
  };
}
