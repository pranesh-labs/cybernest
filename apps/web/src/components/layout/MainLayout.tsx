import React from 'react';
import { Link, Outlet } from 'react-router-dom';

export const MainLayout: React.FC = () => {
  return (
    <div className="flex h-screen bg-zinc-950 text-zinc-100 font-sans antialiased overflow-hidden">
      {/* Sidebar */}
      <aside className="w-64 bg-zinc-900 border-r border-zinc-800 flex flex-col">
        <div className="p-6 border-b border-zinc-800 flex items-center gap-3">
          <div className="h-8 w-8 rounded-lg bg-indigo-600 flex items-center justify-center font-bold text-lg text-white">
            CN
          </div>
          <span className="font-semibold text-lg tracking-wider bg-gradient-to-r from-white to-zinc-400 bg-clip-text text-transparent">
            CyberNest
          </span>
        </div>

        <nav className="flex-1 p-4 space-y-1">
          <Link
            to="/"
            className="flex items-center gap-3 px-4 py-3 rounded-lg text-zinc-300 hover:bg-zinc-800 hover:text-white transition-all"
          >
            <span className="text-sm font-medium">Dashboard Overview</span>
          </Link>
          <Link
            to="/devices"
            className="flex items-center gap-3 px-4 py-3 rounded-lg text-zinc-300 hover:bg-zinc-800 hover:text-white transition-all"
          >
            <span className="text-sm font-medium">Scanned Devices</span>
          </Link>
          <Link
            to="/reports"
            className="flex items-center gap-3 px-4 py-3 rounded-lg text-zinc-300 hover:bg-zinc-800 hover:text-white transition-all"
          >
            <span className="text-sm font-medium">Vulnerabilities</span>
          </Link>
        </nav>

        <div className="p-4 border-t border-zinc-800 flex items-center gap-3 text-zinc-400 text-xs">
          <div className="h-2 w-2 rounded-full bg-emerald-500 animate-pulse"></div>
          <span>System active</span>
        </div>
      </aside>

      {/* Main Content Area */}
      <div className="flex-1 flex flex-col overflow-hidden">
        {/* Header */}
        <header className="h-16 border-b border-zinc-800 bg-zinc-900/50 backdrop-blur-md px-6 flex items-center justify-between">
          <h1 className="text-sm font-medium text-zinc-400">Security Control Platform</h1>
          <div className="flex items-center gap-4">
            <span className="text-xs px-2 py-1 bg-indigo-500/10 text-indigo-400 border border-indigo-500/20 rounded">
              v1.0.0-alpha
            </span>
          </div>
        </header>

        {/* Dynamic Route Content */}
        <main className="flex-1 overflow-y-auto p-8">
          <Outlet />
        </main>
      </div>
    </div>
  );
};
