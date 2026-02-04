import { HashRouter, Route, Routes } from 'react-router-dom';

import { DashboardRoute } from './dashboard';
import { SettingsRoute } from './settings';

export function App() {
  return (
    <HashRouter>
      <Routes>
        <Route path="/" element={<DashboardRoute />} />
        <Route path="/settings" element={<SettingsRoute />} />
      </Routes>
    </HashRouter>
  );
}
