import { useSyncExternalStore } from 'react';

import { getHass, subscribe } from '../hassStore';
import type { HassEntityState } from '../types';

export function useEntities(filter?: (entityId: string, state: HassEntityState) => boolean) {
  return useSyncExternalStore(
    subscribe,
    () => {
      const states = getHass()?.states ?? {};
      if (!filter) return states;
      const out: Record<string, HassEntityState> = {};
      for (const [entityId, state] of Object.entries(states)) {
        if (state && filter(entityId, state)) out[entityId] = state;
      }
      return out;
    },
    () => ({})
  );
}
