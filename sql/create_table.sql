CREATE TABLE issues (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    body TEXT,
    created_at TIMESTAMP,
    closed_at TIMESTAMP,
    resolution_time_days NUMERIC(10, 2),
    milestone TEXT,
    author_username TEXT,
    assignee_username TEXT,
    tema_relacionado TEXT[],
    url_issue TEXT
);
