/**
 * Shared DTO Type Definitions for CyberNest
 */

export interface AgentHeartbeat {
  agentId: string;
  timestamp: string; // ISO 8601 string
  status: 'online' | 'scanning' | 'idle' | 'offline';
  version: string;
  systemInfo: Record<string, any>;
}

export interface HostInfo {
  ip: string;
  mac?: string;
  hostname?: string;
  osName?: string;
  osVersion?: string;
  openPorts: number[];
}

export interface VulnerabilityReport {
  cveId: string;
  severity: 'low' | 'medium' | 'high' | 'critical';
  description: string;
  targetHost: string;
  port?: number;
}

export interface ScanResultPayload {
  agentId: string;
  scanId: string;
  startedAt: string; // ISO 8601 string
  finishedAt: string; // ISO 8601 string
  hosts: HostInfo[];
  vulnerabilities: VulnerabilityReport[];
}

export interface UserDTO {
  id: string;
  email: string;
  fullName?: string;
  isActive: boolean;
  role: 'admin' | 'analyst' | 'read_only';
  createdAt: string;
}
