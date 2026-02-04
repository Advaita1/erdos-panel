export type HassEntityState = Record<string, unknown>;

export interface HomeAssistantLike {
  states: Record<string, HassEntityState | undefined>;
  callService: (domain: string, service: string, serviceData?: unknown) => void;
  callWS: <T = unknown>(message: Record<string, unknown>) => Promise<T>;
}
