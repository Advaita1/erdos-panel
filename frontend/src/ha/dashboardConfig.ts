import { getHass } from './hassStore';

export interface DashboardConfig {
  version: number;
  dashboards: Record<string, unknown>;
}

function requireHass() {
  const hass = getHass();
  if (!hass) throw new Error('Home Assistant hass not available yet');
  return hass;
}

export async function getDashboardConfig(): Promise<DashboardConfig> {
  return requireHass().callWS<DashboardConfig>({
    type: 'erdos_panel/config/get',
  });
}

export async function saveDashboardConfig(next: DashboardConfig): Promise<void> {
  await requireHass().callWS({
    type: 'erdos_panel/config/save',
    config: next,
  });
}

export async function patchDashboardConfig(
  patch: Partial<DashboardConfig>
): Promise<DashboardConfig> {
  return requireHass().callWS<DashboardConfig>({
    type: 'erdos_panel/config/patch',
    patch,
  });
}

export async function resetDashboardConfig(): Promise<DashboardConfig> {
  return requireHass().callWS<DashboardConfig>({
    type: 'erdos_panel/config/reset',
  });
}
