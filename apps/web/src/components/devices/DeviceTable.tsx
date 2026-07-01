import React from 'react';
import { HostInfo } from '@cybernest/shared-types';

interface DeviceTableProps {
  devices?: HostInfo[];
}

export const DeviceTable: React.FC<DeviceTableProps> = ({ devices = [] }) => {
  const dummyDevices: HostInfo[] = devices.length > 0 ? devices : [
    { ip: '192.168.1.1', mac: '00:11:22:33:44:55', hostname: 'Gateway-Router', osName: 'Linux', osVersion: '5.10', openPorts: [80, 443] },
    { ip: '192.168.1.10', mac: 'AA:BB:CC:DD:EE:FF', hostname: 'Production-DB', osName: 'Ubuntu', osVersion: '22.04', openPorts: [5432, 22] },
    { ip: '192.168.1.15', mac: '12:34:56:78:90:AB', hostname: 'Dev-Sandbox', osName: 'Windows', osVersion: 'Server 2022', openPorts: [3389] }
  ];

  return (
    <div className="overflow-x-auto border border-zinc-800 rounded-xl bg-zinc-900 shadow-xl">
      <table className="min-w-full divide-y divide-zinc-800">
        <thead className="bg-zinc-900/50">
          <tr>
            <th className="px-6 py-4 text-left text-xs font-semibold text-zinc-400 uppercase tracking-wider">IP Address</th>
            <th className="px-6 py-4 text-left text-xs font-semibold text-zinc-400 uppercase tracking-wider">Hostname</th>
            <th className="px-6 py-4 text-left text-xs font-semibold text-zinc-400 uppercase tracking-wider">MAC Address</th>
            <th className="px-6 py-4 text-left text-xs font-semibold text-zinc-400 uppercase tracking-wider">OS Details</th>
            <th className="px-6 py-4 text-left text-xs font-semibold text-zinc-400 uppercase tracking-wider">Open Ports</th>
          </tr>
        </thead>
        <tbody className="divide-y divide-zinc-800 bg-zinc-900/30">
          {dummyDevices.map((device, idx) => (
            <tr key={idx} className="hover:bg-zinc-800/30 transition-colors">
              <td className="px-6 py-4 whitespace-nowrap text-sm font-semibold text-white">{device.ip}</td>
              <td className="px-6 py-4 whitespace-nowrap text-sm text-zinc-300">{device.hostname || 'Unknown'}</td>
              <td className="px-6 py-4 whitespace-nowrap text-sm text-zinc-400 font-mono">{device.mac || '-'}</td>
              <td className="px-6 py-4 whitespace-nowrap text-sm text-zinc-300">
                {device.osName ? `${device.osName} ${device.osVersion || ''}` : 'Detecting...'}
              </td>
              <td className="px-6 py-4 whitespace-nowrap text-sm text-zinc-400">
                <div className="flex gap-1.5 flex-wrap">
                  {device.openPorts.map((port) => (
                    <span key={port} className="text-xs px-2 py-0.5 rounded bg-zinc-800 text-indigo-400 border border-zinc-700">
                      {port}
                    </span>
                  ))}
                </div>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};
