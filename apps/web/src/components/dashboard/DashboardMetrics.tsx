import React from 'react';

export const DashboardMetrics: React.FC = () => {
  const cards = [
    { name: 'Total Scanned Hosts', value: '42', description: 'Active hosts in subnet', status: 'normal' },
    { name: 'Detected Vulnerabilities', value: '7', description: 'Requires immediate attention', status: 'warning' },
    { name: 'Active Sub-Agents', value: '3', description: 'Heartbeat online', status: 'success' },
  ];

  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
      {cards.map((card, i) => (
        <div key={i} className="p-6 bg-zinc-900 border border-zinc-800 rounded-xl shadow-lg hover:border-zinc-700 transition-all">
          <p className="text-sm font-medium text-zinc-400">{card.name}</p>
          <p className="text-3xl font-bold mt-2 text-white">{card.value}</p>
          <div className="mt-4 flex items-center gap-2 text-xs">
            <span className={`h-1.5 w-1.5 rounded-full ${
              card.status === 'warning' ? 'bg-rose-500' :
              card.status === 'success' ? 'bg-emerald-500' : 'bg-indigo-500'
            }`}></span>
            <span className="text-zinc-500">{card.description}</span>
          </div>
        </div>
      ))}
    </div>
  );
};
