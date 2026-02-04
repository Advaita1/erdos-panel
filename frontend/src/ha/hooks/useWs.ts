import { useCallback } from 'react';

import { useHass } from './useHass';

export function useWs() {
  const hass = useHass();
  return useCallback(<T>(message: Record<string, unknown>) => hass.callWS<T>(message), [hass]);
}
