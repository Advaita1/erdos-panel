import { useSyncExternalStore } from 'react';

import { getHass, subscribe } from '../hassStore';

export function useHass() {
  const hass = useSyncExternalStore(subscribe, getHass, getHass);
  if (!hass) {
    throw new Error('Home Assistant hass not available yet');
  }
  return hass;
}
