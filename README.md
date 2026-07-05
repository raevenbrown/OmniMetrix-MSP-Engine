# 💎 OmniMetrix-MSP-Engine
An enterprise-grade, multi-tenant B2B Managed Service Provider (MSP) and Infrastructure Analytics platform engineered to transform raw operational logs into clean, department-specific business intelligence.

## 🏢 Project Architecture & Scope
OmniMetrix OS serves as a professional software dashboard built for IT and Cybersecurity companies. Instead of tracking loose data across separate spreadsheets, this system establishes a multi-tenant isolation layout. A central manager or account executive can securely monitor an entire multi-company business portfolio at a glance, or isolate just a single corporate client's network on demand.

* **👉 View the Live Interactive Portal Here:** [YOUR_STREAMLIT_LIVE_URL_HERE]

---

### 🗄️ Phase 1: Relational Database Architecture (SQL)
Designed a centralized B2B relational framework modeling multi-client corporate accounts. The structure isolates tracking metrics into two core tables connected via strict foreign key constraints to maximize search efficiency and protect data integrity.
* **clients table:** Serves as the master corporate index (storing Client Names, Industry Sectors, and Contract Start dates).
* **incidents table:** Captures transactional workflow records (tracking incident severity levels, vulnerability patches, system uptimes, and contractual billing metrics).
* **Code Links:** `database/tenants_schema.sql` | `database/seed_payload.sql`

---

### ⚙️ Phase 2: Python Data Transformation & Payload Logic
Engineered a programmatic data engineering layer utilizing Python and the `pandas` library to replace manual, fragile input pipelines with a clean data pipeline.
* **Data Ingestion Routing:** Pulls raw multi-tenant data matrices and formats them directly into queryable, clean data tables.
* **Boolean Risk Masking:** Applies automated boolean logic arrays to evaluate live row data, instantly flagging critical security risk clusters, firewall vulnerabilities, and backup failures without manual intervention.
* **Code Link:** `src/app.py`

---

### 🖥️ Phase 3: High-Density Business Intelligence Workspace (Streamlit)
Developed a clean, modern user-facing dark mode web application configured with custom brand colors matching premium visual layout systems.
* **Unified Left-Hand Command Console:** Moves system-wide filters and navigation parameters directly into a clean vertical sidebar, maximizing main-screen space and organizing data paths into clean operational views.
* **Multi-Tenant Context Switches:** Integrates responsive selection fields that dynamically filter data frames instantly to protect client cross-tenant data.
* **Granular Financial Telemetry:** Formats raw numerical floats natively into clean, legible currency values (`$#,##0.00`) alongside relative allocation percentages simultaneously on plot interfaces.
