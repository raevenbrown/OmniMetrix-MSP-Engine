-- Insert primary corporate account tenants with explicit seat counts and pricing tracking
INSERT INTO clients VALUES (1, 'Apex Logistics', 'Supply Chain', '2025-01-15', 'Silver');  -- 50 users * $85 = $4,250.00
INSERT INTO clients VALUES (2, 'Summit Health Network', 'Healthcare', '2024-11-01', 'Platinum'); -- 40 users * $175 = $7,000.00
INSERT INTO clients VALUES (3, 'Vanguard Finance', 'Banking', '2025-03-10', 'Gold');    -- 35 users * $125 = $4,375.00
INSERT INTO clients VALUES (4, 'Horizon Retail', 'E-Commerce', '2026-02-22', 'Silver'); -- 25 users * $85 = $2,125.00

-- Insert operational tracking logs perfectly reflecting the screenshot's service options
INSERT INTO incidents VALUES (201, 1, 'Patching & Security', 'Medium', 1, 'Successful', 42, 4250.00, 'In Bounds');
INSERT INTO incidents VALUES (202, 2, 'Dark Web & Compliance', 'Critical', 3, 'Failed Retry', 0, 7000.00, 'Breached SLA');
INSERT INTO incidents VALUES (203, 1, 'Help Desk Support', 'Low', 5, 'Successful', 15, 4250.00, 'In Bounds');
INSERT INTO incidents VALUES (204, 3, 'Threat Detection', 'High', 12, 'Successful', 8, 4375.00, 'Breached SLA');
INSERT INTO incidents VALUES (205, 2, 'Cybersecurity Team', 'Critical', 0, 'Successful', 89, 7000.00, 'In Bounds');
INSERT INTO incidents VALUES (206, 3, 'Help Desk Support', 'Low', 2, 'Successful', 4, 4375.00, 'In Bounds');
INSERT INTO incidents VALUES (207, 1, 'Workstation Backup', 'Low', 0, 'Failed Retry', 0, 4250.00, 'In Bounds');
INSERT INTO incidents VALUES (208, 3, 'Security Training', 'Medium', 4, 'Successful', 22, 4375.00, 'In Bounds');
INSERT INTO incidents VALUES (209, 2, 'Server Backup', 'Low', 1, 'Successful', 112, 7000.00, 'In Bounds');
INSERT INTO incidents VALUES (210, 4, 'Compliance Auditing', 'High', 9, 'Failed Retry', 0, 2125.00, 'Breached SLA');
