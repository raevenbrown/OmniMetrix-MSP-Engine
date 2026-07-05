-- Create the master B2B corporate clients table
CREATE TABLE clients (
    client_id INT PRIMARY KEY,
    client_name VARCHAR(100) NOT NULL,
    industry_sector VARCHAR(50),
    contract_start_date DATE,
    sla_tier VARCHAR(20) DEFAULT 'Standard'
);

-- Create the transactional operational incidents table
CREATE TABLE incidents (
    ticket_id INT PRIMARY KEY,
    client_id INT,
    service_sector VARCHAR(50),
    incident_severity VARCHAR(20),
    days_open INT DEFAULT 0,
    backup_status VARCHAR(20),
    vulnerabilities_patched INT DEFAULT 0,
    monthly_recurring_revenue DECIMAL(10, 2),
    sla_status VARCHAR(20),
    FOREIGN KEY (client_id) REFERENCES clients(client_id)
);
