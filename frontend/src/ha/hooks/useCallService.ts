import { useCallback } from 'react';

import { useHass } from './useHass';

export function useCallService() {
  const hass = useHass();
  return useCallback(
    (domain: string, service: string, serviceData?: unknown) => {
      hass.callService(domain, service, serviceData);
    },
    [hass]
  );
}
