import { useSyncExternalStore } from 'react';

import { getHass, subscribe } from '../hassStore';

export function useEntity(entityId: string) {
  return useSyncExternalStore(
    subscribe,
    () => getHass()?.states?.[entityId],
    () => getHass()?.states?.[entityId]
  );
}
