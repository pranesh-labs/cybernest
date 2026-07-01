-- Optional setup script to create tables, extensions or run initial seeding
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Initialize database tables, indices, or roles if needed
CREATE TABLE IF NOT EXISTS initial_checkpoint (
    id SERIAL PRIMARY KEY,
    initialized_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
