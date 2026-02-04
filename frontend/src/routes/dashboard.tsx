import { useHassOptional } from '@/ha/hooks/useHassOptional';

export function DashboardRoute() {
  const hass = useHassOptional();

  return (
    <div style={{ padding: 16 }}>
      <h1>Erdos Panel</h1>
      <p>Dashboard placeholder.</p>
      <pre style={{ opacity: 0.7 }}>connected: {String(Boolean(hass))}</pre>
    </div>
  );
}
