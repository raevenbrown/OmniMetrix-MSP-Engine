-- Insert primary corporate account tenants
INSERT INTO clients VALUES (1, 'Apex Logistics', 'Supply Chain', '2025-01-15', 'Premium');
INSERT INTO clients VALUES (2, 'Summit Health Network', 'Healthcare', '2024-11-01', 'Elite');
INSERT INTO clients VALUES (3, 'Vanguard Finance', 'Banking', '2025-03-10', 'Elite');
INSERT INTO clients VALUES (4, 'Horizon Retail', 'E-Commerce', '2026-02-22', 'Standard');

-- Insert historical system operational logs
INSERT INTO incidents VALUES (201, 1, 'Cybersecurity', 'Critical', 1, 'Successful', 42, 4500.00, 'In Bounds');
INSERT INTO incidents VALUES (202, 2, 'Backup & Recovery', 'High', 3, 'Failed Retry', 0, 7200.00, 'Breached SLA');
INSERT INTO incidents VALUES (203, 1, 'Helpdesk Tier 2', 'Medium', 5, 'Successful', 15, 4500.00, 'In Bounds');
INSERT INTO incidents VALUES (204, 3, 'Compliance Auditing', 'High', 12, 'Successful', 8, 5800.00, 'Breached SLA');
INSERT INTO incidents VALUES (205, 2, 'Cybersecurity', 'Critical', 0, 'Successful', 89, 7200.00, 'In Bounds');
INSERT INTO incidents VALUES (206, 3, 'Helpdesk Tier 1', 'Low', 2, 'Successful', 4, 5800.00, 'In Bounds');
INSERT INTO incidents VALUES (207, 1, 'Backup & Recovery', 'Low', 0, 'Failed Retry', 0, 4500.00, 'In Bounds');
INSERT INTO incidents VALUES (208, 3, 'Cybersecurity', 'Medium', 4, 'Successful', 22, 5800.00, 'In Bounds');
INSERT INTO incidents VALUES (209, 2, 'Cloud Ops', 'Low', 1, 'Successful', 112, 7200.00, 'In Bounds');
INSERT INTO incidents VALUES (210, 4, 'Compliance Auditing', 'High', 9, 'Failed Retry', 0, 3900.00, 'Breached SLA');
