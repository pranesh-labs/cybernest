import { BrowserRouter, Route, Routes } from 'react-router-dom';
import { MainLayout } from './components/layout/MainLayout';
import { DashboardMetrics } from './components/dashboard/DashboardMetrics';
import { DeviceTable } from './components/devices/DeviceTable';
import { VulnerabilityReportList } from './components/reports/VulnerabilityReportList';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<MainLayout />}>
          <Route
            index
            element={
              <div className="space-y-8">
                <section>
                  <h2 className="text-xl font-bold text-white mb-2">Dashboard Overview</h2>
                  <p className="text-sm text-zinc-400 mb-6">Real-time platform telemetry and connection state.</p>
                  <DashboardMetrics />
                </section>

                <section>
                  <h2 className="text-xl font-bold text-white mb-4">Critical Vulnerabilities</h2>
                  <VulnerabilityReportList />
                </section>
              </div>
            }
          />
          <Route
            path="devices"
            element={
              <div className="space-y-6">
                <div>
                  <h2 className="text-xl font-bold text-white mb-2">Scanned Subnet Devices</h2>
                  <p className="text-sm text-zinc-400">Inventory of detected host systems and port maps.</p>
                </div>
                <DeviceTable />
              </div>
            }
          />
          <Route
            path="reports"
            element={
              <div className="space-y-6">
                <div>
                  <h2 className="text-xl font-bold text-white mb-2">Vulnerability Diagnostics</h2>
                  <p className="text-sm text-zinc-400">Identified software weaknesses mapped against NVD and CVE databases.</p>
                </div>
                <VulnerabilityReportList />
              </div>
            }
          />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
