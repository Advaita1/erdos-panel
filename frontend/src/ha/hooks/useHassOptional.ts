import { useSyncExternalStore } from 'react';

import { getHass, subscribe } from '../hassStore';

export function useHassOptional() {
  return useSyncExternalStore(subscribe, getHass, getHass);
}
