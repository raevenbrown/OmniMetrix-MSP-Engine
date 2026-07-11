import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import date

# 1. Main Page Canvas Configuration
st.set_page_config(page_title="Bunch Consulting MSP Control Suite", layout="wide")

# ==========================================
# CENTRALIZED HIGH-DENSITY LIFE CYCLE DATA STATES (40 SYNCRO TICKET/CLIENT RECORDS)
# ==========================================
if "enrollment_funnel_db" not in st.session_state:
    st.session_state.enrollment_funnel_db = pd.DataFrame({
        "ticket_id": [f"TIC-{4200+i}" for i in range(1, 41)],
        "incident_subject": [
            "M365 Authentication Failure", "Entra ID Sync Malfunction", "BitLocker Encryption Lockout", 
            "Firewall Policy Exception", "Server Backup Corrupted", "Workstation Patching Failure", 
            "VPN Gateway Disconnect", "SQL Database Timeout", "Spam Filter Lease Expiry", "Network Switch Loop",
            "OneDrive Document Sync Error", "SharePoint Permission Wipe", "Azure AD Connect Loop", 
            "Local Print Spooler Crash", "NAS Storage Capacity Breach", "DKIM/SPF Record Misconfiguration", 
            "Malware Containment Alert", "Phishing Trap Event Check", "DHCP Scope Exhaustion", "RADIUS Server Timeout",
            "Hyper-V Cluster Fault", "SSO Token Validation Error", "VOIP Phone SIP Dropout", "Web Filter Bypass Alert",
            "UPS Battery Disconnect", "DNS Record Propagation Lag", "Ransomware Sandbox Hit", "MDM Compliance Breach",
            "Exchange Online Mail Flow Delay", "VLAN Routing Table Collision", "Public IP Blacklist Alert", "SaaS Provisioning Freeze",
            "SSL Certificate Expiry", "Docker Container Fault", "SAN Fiber Channel Drop", "IIS Worker Process Crash",
            "WAP Signal Drop Loop", "Remote Desktop Gateway Drop", "API Webhook Fail Event", "SIEM Alert Flood Threat"
        ],
        "customer_organization": [
            "Bunch Consulting LLC", "5 Boroughs Delicatessen, LLC", "Cordance Medical", "Inspire Nurse Leaders", "Medtechnik",
            "Bunch Consulting Academy", "Bunch Legal Group P.C.", "Expert Innovative Solutions", "Grant Solutions Partners LLC", "JPCC Associates",
            "Karma Advisory", "LAO Group LLC", "My Velocity Group", "New Paradigm CFO", "Professional Environmental Consultants",
            "Reveille Executive Coaching & Consulting", "RoBailey Consulting", "Southeast Bookkeeping", "Sudler Property Management", "SYLWOS",
            "TechniPROS Inc.", "Bunch Consulting LLC", "5 Boroughs Delicatessen, LLC", "Cordance Medical", "Inspire Nurse Leaders",
            "Medtechnik", "Bunch Consulting Academy", "Bunch Legal Group P.C.", "Expert Innovative Solutions", "Grant Solutions Partners LLC",
            "JPCC Associates", "Karma Advisory", "LAO Group LLC", "My Velocity Group", "New Paradigm CFO",
            "Professional Environmental Consultants", "Reveille Executive Coaching & Consulting", "RoBailey Consulting", "Southeast Bookkeeping", "Sudler Property Management"
        ],
        "service_tier_plan": [
            "Silver Plan", "Gold Plan", "Platinum Plan", "Silver Plan", "Platinum Plan", 
            "Silver Plan", "Platinum Plan", "Gold Plan", "Gold Plan", "Gold Plan",
            "Silver Plan", "Gold Plan", "Platinum Plan", "Silver Plan", "Platinum Plan", 
            "Silver Plan", "Platinum Plan", "Gold Plan", "Gold Plan", "Gold Plan",
            "Silver Plan", "Gold Plan", "Platinum Plan", "Silver Plan", "Platinum Plan", 
            "Silver Plan", "Platinum Plan", "Gold Plan", "Gold Plan", "Gold Plan",
            "Silver Plan", "Gold Plan", "Platinum Plan", "Silver Plan", "Platinum Plan", 
            "Silver Plan", "Platinum Plan", "Gold Plan", "Gold Plan", "Gold Plan"
        ],
        "infrastructure_category": [
            "Cloud Infrastructure", "Local Workspace", "Cybersecurity Audit", "Network Hardware", "Business Continuity",
            "Cloud Infrastructure", "Local Workspace", "Cybersecurity Audit", "Network Hardware", "Business Continuity",
            "Cloud Infrastructure", "Local Workspace", "Cybersecurity Audit", "Network Hardware", "Business Continuity",
            "Cloud Infrastructure", "Local Workspace", "Cybersecurity Audit", "Network Hardware", "Business Continuity",
            "Cloud Infrastructure", "Local Workspace", "Cybersecurity Audit", "Network Hardware", "Business Continuity",
            "Cloud Infrastructure", "Local Workspace", "Cybersecurity Audit", "Network Hardware", "Business Continuity",
            "Cloud Infrastructure", "Local Workspace", "Cybersecurity Audit", "Network Hardware", "Business Continuity",
            "Cloud Infrastructure", "Local Workspace", "Cybersecurity Audit", "Network Hardware", "Business Continuity"
        ],
        "system_stability_index": [
            3.85, 3.31, 2.45, 3.82, 1.95, 2.88, 3.12, 2.15, 3.64, 3.22,
            3.40, 2.90, 3.75, 1.80, 2.65, 3.10, 2.25, 3.55, 3.90, 2.40,
            3.15, 2.70, 3.60, 2.10, 3.45, 2.80, 3.85, 1.90, 2.95, 3.35,
            3.20, 2.60, 3.65, 2.30, 3.50, 2.75, 3.95, 1.75, 2.50, 3.05
        ],
        "rmm_agent_status": [
            "Good Standing - Regular Sync", "Good Standing - Regular Sync", "Patching Alert - Pending Reboot", 
            "Good Standing - Regular Sync", "Good Standing - Regular Sync", "Good Standing - Regular Sync", 
            "Good Standing - Regular Sync", "Firewall Hold - Security Exception", "Good Standing - Regular Sync", 
            "Critical Alert - Agent Offline", "Good Standing - Regular Sync", "Patching Alert - Pending Reboot",
            "Good Standing - Regular Sync", "Critical Alert - Agent Offline", "Good Standing - Regular Sync",
            "Good Standing - Regular Sync", "Firewall Hold - Security Exception", "Good Standing - Regular Sync",
            "Patching Alert - Pending Reboot", "Good Standing - Regular Sync", "Good Standing - Regular Sync",
            "Critical Alert - Agent Offline", "Good Standing - Regular Sync", "Firewall Hold - Security Exception",
            "Good Standing - Regular Sync", "Good Standing - Regular Sync", "Good Standing - Regular Sync",
            "Patching Alert - Pending Reboot", "Good Standing - Regular Sync", "Good Standing - Regular Sync",
            "Critical Alert - Agent Offline", "Good Standing - Regular Sync", "Firewall Hold - Security Exception",
            "Good Standing - Regular Sync", "Good Standing - Regular Sync", "Patching Alert - Pending Reboot",
            "Good Standing - Regular Sync", "Critical Alert - Agent Offline", "Good Standing - Regular Sync", "Firewall Hold - Security Exception"
        ],
        "helpdesk_status": [
            "Resolved", "Resolved", "Resolved", "Resolved", "Resolved", "Resolved", "Resolved", "Assigned to me", "In Progress", "Unassigned",
            "Resolved", "Resolved", "Resolved", "Assigned to me", "Resolved", "Resolved", "Resolved", "Resolved", "Assigned to me", "Resolved",
            "Resolved", "Resolved", "Resolved", "Assigned to me", "Resolved", "Resolved", "Resolved", "Resolved", "Assigned to me", "Resolved",
            "Resolved", "Resolved", "Resolved", "Assigned to me", "Resolved", "Resolved", "Resolved", "Resolved", "Assigned to me", "Unassigned"
        ],
        "automation_policy_group": [
            "M365 Baselines Push", "M365 Baselines Push", "M365 Baselines Push", "M365 Baselines Push", "M365 Baselines Push", 
            "M365 Baselines Push", "M365 Baselines Push", "Entra ID Sync Automation", "BitLocker Policy Enforce", "VLAN Reconfiguration",
            "M365 Baselines Push", "M365 Baselines Push", "M365 Baselines Push", "Entra ID Sync Automation", "M365 Baselines Push",
            "M365 Baselines Push", "M365 Baselines Push", "M365 Baselines Push", "Entra ID Sync Automation", "M365 Baselines Push",
            "M365 Baselines Push", "M365 Baselines Push", "M365 Baselines Push", "Entra ID Sync Automation", "M365 Baselines Push",
            "M365 Baselines Push", "M365 Baselines Push", "M365 Baselines Push", "Entra ID Sync Automation", "M365 Baselines Push",
            "M365 Baselines Push", "M365 Baselines Push", "M365 Baselines Push", "Entra ID Sync Automation", "M365 Baselines Push",
            "M365 Baselines Push", "M365 Baselines Push", "M365 Baselines Push", "Entra ID Sync Automation", "VLAN Reconfiguration"
        ],
        "sla_breach_risk": [
            "Resolved", "Resolved", "Resolved", "Resolved", "Resolved", "Resolved", "Resolved", "High SLA Breach Risk", "Medium SLA Breach Risk", "Low SLA Breach Risk",
            "Resolved", "Resolved", "Resolved", "High SLA Breach Risk", "Resolved", "Resolved", "Resolved", "Resolved", "High SLA Breach Risk", "Resolved",
            "Resolved", "Resolved", "Resolved", "High SLA Breach Risk", "Resolved", "Resolved", "Resolved", "Resolved", "High SLA Breach Risk", "Resolved",
            "Resolved", "Resolved", "Resolved", "High SLA Breach Risk", "Resolved", "Resolved", "Resolved", "Resolved", "High SLA Breach Risk", "Low SLA Breach Risk"
        ],
        "last_scan_date": ["2026-07-10" for _ in range(40)],
        "open_warning_flags": [i % 4 for i in range(40)],
        "channel_preference": ["Email Link" if i % 2 == 0 else "Syncro Chat UI" for i in range(40)],
        "compliance_scope": ["SOC 2 Compliance Scope" if i % 3 == 0 else "Regular SLA Retention Plan" for i in range(40)],
        "rmm_telemetry_logs": [f"SyncroMSP telemetry audit track frame line instance flag {i}." for i in range(1, 41)]
    })

if "faculty_retention_db" not in st.session_state:
    st.session_state.faculty_retention_db = pd.DataFrame({
        "engineer_id": [f"TECH-{400+i}" for i in range(1, 21)],
        "engineer_name": [
            "Stacey Nebriaga", "Michael Gabriele", "Tyler Pede", "Thomas Anderson", 
            "Emily Holzgrefe", "Sarah Jenkins", "David Vance", "Elena Rostova",
            "Robert Langdon", "Minerva McGonagall", "Alan Grant", "Ellie Sattler",
            "Charles Xavier", "Henry Wu", "Ian Malcolm", "Albus Dumbledore",
            "Severus Snape", "Gilderoy Lockhart", "Remus Lupin", "Pomona Sprout"
        ],
        "assigned_focus_area": [
            "Cloud Ops", "Database Admin", "Cybersecurity", "Network Routing", "SaaS Management", 
            "Identity Access", "Storage Infrastructure", "VOIP Systems", "Cloud Ops", "Database Admin", 
            "Cybersecurity", "Network Routing", "SaaS Management", "Identity Access", "Storage Infrastructure", 
            "VOIP Systems", "Cloud Ops", "Database Admin", "Cybersecurity", "Network Routing"
        ],
        "escalation_tier_rank": [
            "Tier 3 Cybersecurity Lead", "Tier 2 Systems Admin", "Tier 1 Helpdesk Specialist", "Tier 3 Cybersecurity Lead", 
            "Tier 2 Network Engineer", "Tier 1 Helpdesk Specialist", "Tier 3 Cybersecurity Lead", "Tier 2 Systems Admin",
            "Tier 3 Cybersecurity Lead", "Tier 3 Cybersecurity Lead", "Tier 1 Helpdesk Specialist", "Tier 3 Cybersecurity Lead",
            "Tier 3 Cybersecurity Lead", "Tier 2 Systems Admin", "Tier 2 Network Engineer", "Tier 3 Cybersecurity Lead",
            "Tier 3 Cybersecurity Lead", "Tier 2 Systems Admin", "Tier 1 Helpdesk Specialist", "Tier 3 Cybersecurity Lead"
        ],
        "operational_status": [
            "Active - Full Operations Load", "Active - Full Operations Load", "Pending Certification Update", 
            "Standby - Available Onsite", "Active - Full Operations Load", "Pending Certification Update", 
            "Active - Full Operations Load", "On Temporary Leave", "Active - Full Operations Load",
            "Active - Full Operations Load", "Pending Certification Update", "Active - Full Operations Load",
            "Standby - Available Onsite", "Active - Full Operations Load", "Active - Full Operations Load",
            "Active - Full Operations Load", "Active - Full Operations Load", "On Temporary Leave",
            "Pending Certification Update", "Active - Full Operations Load"
        ],
        "years_with_bunch": [
            12.5, 3.0, 4.5, 16.0, 2.5, 5.0, 14.0, 1.5,
            8.0, 22.0, 3.5, 11.0, 19.5, 4.0, 1.0, 35.0,
            15.0, 2.0, 5.5, 13.0
        ],
        "assigned_monthly_tickets": [
            42, 58, 39, 31, 62, 41, 33, 60,
            45, 30, 51, 40, 28, 59, 61, 20,
            35, 55, 43, 38
        ],
        "burnout_hazard_flag": [
            "Low Risk", "Medium Risk", "Low Risk", "Low Risk", "High Risk", "Low Risk", "Low Risk", "Medium Risk",
            "Low Risk", "Low Risk", "Medium Risk", "Low Risk", "Low Risk", "High Risk", "High Risk", "Low Risk",
            "Low Risk", "High Risk", "Low Risk", "Low Risk"
        ],
        "estimated_departure_timeline": [
            "Stable (>5 Years)", "Review in 1-2 Years", "Stable (>5 Years)", "Stable (>5 Years)", "Immediate Risk (<1 Year)", "Stable (>5 Years)", "Stable (>5 Years)", "Review in 1-2 Years",
            "Stable (>5 Years)", "Stable (>5 Years)", "Review in 1-2 Years", "Stable (>5 Years)", "Stable (>5 Years)", "Immediate Risk (<1 Year)", "Immediate Risk (<1 Year)", "Stable (>5 Years)",
            "Stable (>5 Years)", "Immediate Risk (<1 Year)", "Stable (>5 Years)", "Stable (>5 Years)"
        ],
        "throughput_notes": [
            "SyncroMSP throughput validation checks complete.", "Seeking path escalation parameters.",
            "Progressing on timeline baseline track.", "Senior infrastructure asset established.",
            "Workload indicators signal intervention parameters required.", "Security clearing passed successfully.",
            "Approaching standard retirement matrix horizon.", "Reviewing market compensation structuring indices.",
            "SyncroMSP throughput validation checks complete.", "Seeking path escalation parameters.",
            "Progressing on timeline baseline track.", "Senior infrastructure asset established.",
            "Workload indicators signal intervention parameters required.", "Security clearing passed successfully.",
            "Approaching standard retirement matrix horizon.", "Reviewing market compensation structuring indices.",
            "SyncroMSP throughput validation checks complete.", "Seeking path escalation parameters.",
            "Progressing on timeline baseline track.", "Senior infrastructure asset established."
        ]
    })

if "bunch_capacity_db" not in st.session_state:
    st.session_state.bunch_capacity_db = pd.DataFrame({
        "infrastructure_node": ["Cloud Ops", "Database Admin", "Cybersecurity", "Network Routing", "SaaS Management", "Identity Access", "Storage Infrastructure", "VOIP Systems", "Helpdesk Desk", "Compliance Auditing"],
        "total_monitored_endpoints": [850, 1250, 680, 410, 350, 980, 240, 890, 1650, 1420],
        "monthly_hours_allocated": [12400, 18400, 9100, 5200, 4800, 24500, 3100, 9400, 19800, 14200],
        "target_sla_pct": [84.0, 85.0, 88.0, 80.0, 82.0, 82.0, 80.0, 88.0, 80.0, 85.0],
        "actual_sla_pct": [81.2, 82.4, 86.7, 79.1, 81.5, 76.8, 80.2, 89.5, 74.2, 81.1],
        "deployed_hardware_inventory": [45, 120, 85, 30, 25, 110, 15, 60, 140, 130]
    })

# High contrast primary colors (No mud tones)
msp_color_palette = ["#FFC400", "#00E676", "#FF5722", "#00B0FF", "#AA00FF", "#FF3D00"]

# ==========================================
# SIDEBAR SELECTION SYSTEM
# ==========================================
st.sidebar.title("🛡️ Bunch Control Console")
st.sidebar.markdown("**Enterprise MSP Engine:** `Bunch Consulting LLC`")
st.sidebar.write("---")

st.sidebar.subheader("👁️ Layer Visibility Options")
show_clients = st.sidebar.checkbox("Show Client Telemetry & Tickets", value=True)
show_engineers = st.sidebar.checkbox("Show MSP Helpdesk Technical Roster", value=True)
st.sidebar.write("---")

st.sidebar.subheader("🗂️ Global RMM Filters")

dept_filter = st.sidebar.selectbox("Filter by Customer Organization:", options=["All Organizations"] + list(st.session_state.enrollment_funnel_db["customer_organization"].unique()))
term_filter = st.sidebar.selectbox("Filter by Contract Service Tier Plan:", options=["All Contract Tiers", "Silver Plan", "Gold Plan", "Platinum Plan"])
studentvue_filter = st.sidebar.selectbox("Filter by Syncro RMM Agent State:", options=["All Agent Sync States", "Good Standing - Regular Sync", "Patching Alert - Pending Reboot", "Firewall Hold - Security Exception", "Critical Alert - Agent Offline"])
faculty_status_filter = st.sidebar.selectbox("Filter by Technical Team Dispatch Status:", options=["All Tech Work States", "Active - Full Operations Load", "Pending Certification Update", "Standby - Available Onsite"])

processed_funnel = st.session_state.enrollment_funnel_db.copy()
processed_faculty = st.session_state.faculty_retention_db.copy()

if dept_filter != "All Organizations":
    processed_funnel = processed_funnel[processed_funnel["customer_organization"] == dept_filter]

if term_filter != "All Contract Tiers":
    processed_funnel = processed_funnel[processed_funnel["service_tier_plan"] == term_filter]

if studentvue_filter != "All Agent Sync States":
    processed_funnel = processed_funnel[processed_funnel["rmm_agent_status"] == studentvue_filter]

if faculty_status_filter != "All Tech Work States":
    processed_faculty = processed_faculty[processed_faculty["operational_status"] == faculty_status_filter]

st.sidebar.write("---")
st.sidebar.subheader("🏁 Navigation Terminal")

nav_options = []
if show_clients: nav_options.append("👤 Syncro Service Desk Portal")
if show_engineers: nav_options.append("🏛️ MSP Engineering Workload Console")
if show_clients: nav_options.append("📢 Automation Action Script Matrix")
nav_options.append("📈 Reports & Analytics Compliance Portfolio")

app_panel = st.sidebar.radio("Select Operational Workspace Desk:", options=nav_options)

# ==========================================
# MODULE 1: CLIENT LIFE PORTAL
# ==========================================
if app_panel == "👤 Syncro Service Desk Portal":
    main_workspace, ai_assistant_col = st.columns([3, 1])
    
    with main_workspace:
        st.markdown("## 📋 Syncro Service Desk: Ticket Progress & Endpoint Infrastructure Management")
        st.write("---")
        
        fc1, fc2, fc3, fc4 = st.columns(4)
        with fc1: st.metric("Active Monitored Infrastructure Alerts", value=len(processed_funnel))
        with fc2: st.metric("Tickets Assigned to Me", value=len(processed_funnel[processed_funnel["helpdesk_status"] == "Assigned to me"]))
        with fc3: st.metric("Resolved Tickets Count", value=len(processed_funnel[processed_funnel["helpdesk_status"] == "Resolved"]))
        with fc4: 
            if "open_warning_flags" in processed_funnel.columns and len(processed_funnel) > 0:
                st.metric("Open Automated Warning Flags", value=int(processed_funnel["open_warning_flags"].sum()))
            else: st.metric("Open Automated Warning Flags", value=0)
        
        st.write("")
        if len(processed_funnel) > 0:
            selected_prospect = st.selectbox("🔍 Select Active Incident Event Ticket to Audit:", options=list(processed_funnel["incident_subject"].unique()))
            master_match = st.session_state.enrollment_funnel_db[st.session_state.enrollment_funnel_db["incident_subject"] == selected_prospect]
            idx = master_match.index[0]
            p_row = master_match.loc[idx]
            
            with st.container(border=True):
                st.markdown(f"### Ticket Subject: **{p_row['incident_subject']}** | Asset Ref: `{p_row['ticket_id']}`")
                st.write("")
                det_col1, det_col2 = st.columns(2)
                with det_col1:
                    st.markdown(f"**🏢 Customer Organization Tenant:** `{p_row['customer_organization']}`")
                    st.markdown(f"**🗓️ Contract Service Tier Plan:** `{p_row['service_tier_plan']}`")
                    st.markdown(f"**🎯 Syncro Helpdesk Workflow State:** `{p_row['helpdesk_status']}`")
                with det_col2:
                    st.markdown(f"**🔮 SLA Breach Probability Curve:** `{p_row['sla_breach_risk']}`")
                    st.markdown(f"**🔒 Syncro RMM Agent Core Update:** `{p_row['rmm_agent_status']}`")
                    st.markdown(f"**🏷️ Audit Scope Class Mapping:** `{p_row['compliance_scope']}`")
            
            st.write("")
            st.subheader("🤖 AI Assistant: Automated Event Log Prep Insights")
            with st.container(border=True):
                st.markdown(f"*🧠 RMM Ingestion Diagnostics Material:* **\"{p_row['rmm_telemetry_logs']}\"**")
                
            st.write("---")
            st.subheader("🛠️ Streamline Helpdesk Ticket Resolution Tasks")
            w1, w2, w3 = st.columns([1, 1, 2])
            with w1: stage_update = st.selectbox("Advance Ticket Status:", options=["Unassigned", "Assigned to me", "In Progress", "Resolved"])
            with w2: camp_update = st.selectbox("Reassign RMM Baseline Script Group:", options=["M365 Baselines Push", "Entra ID Sync Automation", "BitLocker Policy Enforce", "VLAN Reconfiguration"])
            with w3: append_note = st.text_input("Append Syncro Desk Communication Log Entry:")
                
            if st.button("🚀 Commit Adjustments to Centralized Syncro Ledger", use_container_width=True):
                st.session_state.enrollment_funnel_db.at[idx, "helpdesk_status"] = stage_update
                st.session_state.enrollment_funnel_db.at[idx, "automation_policy_group"] = camp_update
                if append_note: st.session_state.enrollment_funnel_db.at[idx, "rmm_telemetry_logs"] = f"{p_row['rmm_telemetry_logs']} | CDO Edit: {append_note}"
                st.success("Syncro ticket fields updated successfully.")
                st.rerun()
        else: st.warning("No incident telemetry matching current filter scope constraints.")
            
        st.write("---")
        st.subheader("📋 Centralized View: Filtered Active Helpdesk Syncro Ticket Ledger")
        st.dataframe(processed_funnel[["ticket_id", "incident_subject", "customer_organization", "service_tier_plan", "helpdesk_status", "rmm_agent_status"]], use_container_width=True, hide_index=True)

    with ai_assistant_col:
        st.markdown("### 🤖 MSP AI Agent")
        st.write("---")
        if len(processed_funnel) > 0 and 'p_row' in locals():
            with st.container(border=True):
                st.markdown(f"**Node Scope:** `{p_row['ticket_id']}`")
                st.write(f"* **Tier Group:** {p_row['service_tier_plan']}")
                st.write(f"* **Agent State:** {p_row['rmm_agent_status']}")
        st.write("")
        st.button("✉️ Deploy Automated RMM Warning Nudge Alert", use_container_width=True)
        st.button("📅 Dispatch On-Site Support Technician Event", use_container_width=True)

# ==========================================
# MODULE 2: FIXED MSP ENGINEERING WORKLOAD CONSOLE
# ==========================================
elif app_panel == "🏛️ MSP Engineering Workload Console":
    st.header("🏛️ MSP Engineering Roster: Performance & Capacity Analytics")
    st.markdown("##### *Auditing technician service years, live ticket workload balancing metrics, and retention threat hazard parameters.*")
    st.write("---")
    
    if len(processed_faculty) > 0:
        faculty_picker = st.selectbox("👤 Select Tech Staff Member Profile File to Open:", options=list(processed_faculty["engineer_name"].unique()))
        f_row = processed_faculty[processed_faculty["engineer_name"] == faculty_picker].iloc[0]
        
        with st.container(border=True):
            st.markdown(f"### Engineer Resource File: **{f_row['engineer_name']}** | Staff Ref: `{f_row['engineer_id']}`")
            st.write("")
            f_c1, f_c2, f_c3 = st.columns(3)
            with f_c1:
                st.markdown(f"**🏢 Tech Escalation Assignment Tier:** `{f_row['escalation_tier_rank']}`")
                st.markdown(f"**⚙️ Administrative Operational Status:** `{f_row['operational_status']}`")
            with f_c2:
                st.markdown(f"**⏳ Stated Years with Bunch Consulting:** `{f_row['years_with_bunch']} Years Longevity`")
                st.markdown(f"**📚 Live Syncro Active Monthly Ticket Volume:** `{f_row['assigned_monthly_tickets']} Tickets Assigned`")
            with f_c3:
                st.markdown(f"**🔮 Workload Attrition Risk Flag Tier:** `{f_row['burnout_hazard_flag']}`")
                st.markdown(f"**📅 Retention Horizon Estimate Line:** `{f_row['estimated_departure_timeline']}`")
            st.write("---")
            st.markdown(f"**📥 HR Manager Operational Notes:** *\"{f_row['throughput_notes']}\"*")
            
        st.write("---")
        f_g1, f_g2 = st.columns(2)
        with f_g1:
            # FIXED: Corrected column map inputs inside the bar execution logic to remove the NameError crash loop
            fig_tenure = px.bar(processed_faculty, x="engineer_name", y="years_with_bunch", title="Staff Longevity Analysis (Years with Bunch Consulting LLC)", color="escalation_tier_rank", color_discrete_sequence=msp_color_palette)
            st.plotly_chart(fig_tenure, use_container_width=True)
        with f_g2:
            fig_hazard = px.pie(processed_faculty, values="assigned_monthly_tickets", names="burnout_hazard_flag", title="Helpdesk Resource Load Distribution Shares Sorted by Hazard Threat", hole=0.4, color_discrete_sequence=["#00E676", "#FFC400", "#FF5722"])
            st.plotly_chart(fig_hazard, use_container_width=True)
    else: st.warning("No engineering metrics log segments found matching current filters.")

# ==========================================
# MODULE 3: FIXED AUTOMATION SCRIPT MATRIX
# ==========================================
elif app_panel == "📢 Automation Action Script Matrix":
    st.header("📢 Syncro Automation Profile Task Group Dispatcher")
    st.write("---")
    with st.form("campaign_creation_desk"):
        c_name = st.text_input("RMM Baseline Automation Script Label:", value="M365 Entra ID Mandatory MFA Push Script")
        c_channel = st.selectbox("Primary deployment Execution Strategy Channel:", options=["Targeted PowerShell Sequences via Agent", "Automated E-Mail Ticket Prompts", "RMM Bulk Scripting Push"])
        c_cohort = st.selectbox("Target Customer System Scope Ring:", options=["Inquiry Population Pool", "Patching Exception Groups", "Critical Agent Warning Alerts Tiers"])
        if st.form_submit_button("🚀 Deploy Nuanced Automation Script Strategy"):
            st.success(f"RMM Script Engine Strategy task group '{c_name}' deployed successfully!")

    st.write("---")
    # FIXED: Re-mapped chart metrics properties targeting helpdesk_status fields explicitly to eliminate deployment crashes
    fig_funnel = px.bar(processed_funnel, x="helpdesk_status", title="Continuous Progress Helpdesk Resolution Funnel Analytics Curve", color="helpdesk_status", color_discrete_sequence=msp_color_palette)
    st.plotly_chart(fig_funnel, use_container_width=True)

# ==========================================
# MODULE 4: LEDGER GATEWAY (KEYS 6, 8, 9, 10 STRIPPED OUT NATIVELY)
# ==========================================
elif app_panel == "📈 Reports & Analytics Compliance Portfolio":
    st.header("📈 Enterprise Reports & Analytics Compliance Gateway")
    st.markdown("##### *Mapping interactive query views to verify core analytical milestones against your technical infrastructure directives.*")
    st.write("---")
    
    # Pruned rows down to exactly 6 enterprise metrics
    ledger_df = pd.DataFrame({
        "Key ID": ["Key 1", "Key 2", "Key 3", "Key 4", "Key 5", "Key 7"],
        "Job Description Requirement Statement": [
            "1. Compiles standard and ad hoc reports per established guidelines and frequency",
            "2. Provides reports, analysis and data interpretation for all assigned corporate accounts",
            "3. Identifies areas of opportunity and presents findings and recommendations to leadership and stakeholders",
            "4. Provides productivity analysis reports",
            "5. Develops and maintains reports to measure operational and/or utilization activity",
            "7. Compiles recurring operational review that includes trend analysis"
        ],
        "Dashboard Validation Status": ["🟢 Engine Integrated & Deployable"] * 6
    })
    st.dataframe(ledger_df, use_container_width=True, hide_index=True)
    st.write("---")
    
    selected_key_tab = st.selectbox("Select Active Compliance Report to Query Natively:", options=list(ledger_df["Job Description Requirement Statement"]))
    st.write("---")
    
    if "1. Compiles standard and ad hoc" in selected_key_tab:
        st.markdown("### 📊 Key 1: Standardized Scheduled vs. Ad Hoc Event Extractions Engine")
        st.caption("🔗 *SyncroMSP Mapping Source:* Sourced directly from **Syncro -> Tickets -> Ticket Views -> Scheduled Reports** data matrices.")
        rep_type = st.radio("Select Guidelines Frequency Distribution Format:", ["Standard Recurring (Weekly Intake)", "Ad Hoc Live Extract"])
        if rep_type == "Standard Recurring (Weekly Intake)":
            st.info("📦 **Standard Guideline Run:** Extracting scheduled multi-tenant operational endpoint data logs, asset references, and SLA metrics.")
            st.dataframe(processed_funnel[["ticket_id", "incident_subject", "customer_organization", "service_tier_plan", "helpdesk_status"]], use_container_width=True, hide_index=True)
        else:
            st.warning("⚡ **Ad Hoc Command Executed:** Running dynamic cross-sectional splice targeting high risk critical SLA alert breaches.")
            ad_hoc_subset = processed_funnel[processed_funnel["sla_breach_risk"].str.contains("High")]
            st.dataframe(ad_hoc_subset, use_container_width=True, hide_index=True)

    elif "2. Provides reports, analysis and data interpretation" in selected_key_tab:
        st.markdown("### 🏛️ Key 2: Corporate Tenant Technical Interpretation Summary Ledger")
        st.caption("🔗 *SyncroMSP Mapping Source:* Sourced from **Syncro -> Admin -> Employees** metrics combined with **Syncro Ticket Timesheets** tracking.")
        c_act, c_graph = st.columns(2)
        with c_act:
            st.info("📊 **Assigned Service Hub Engineering Matrix**")
            st.dataframe(processed_faculty[["engineer_name", "escalation_tier_rank", "operational_status", "years_with_bunch"]], use_container_width=True, hide_index=True)
        with c_graph:
            fig_key2 = px.bar(processed_faculty, x="engineer_name", y="assigned_monthly_tickets", title="Total Active Syncro Tickets Handled per Specialist", color_discrete_sequence=["#FFC400"])
            st.plotly_chart(fig_key2, use_container_width=True)

    elif "3. Identifies areas of opportunity" in selected_key_tab:
        st.markdown("### 💡 Key 3: Enterprise Opportunity Discovery & Technical Strategic Analysis")
        st.caption("🔗 *SyncroMSP Mapping Source:* Filtered using **Syncro -> Assets & RMM -> Policy Alerts** threshold trigger indices.")
        low_perf_leads = processed_funnel[processed_funnel["system_stability_index"] < 2.5] if len(processed_funnel) > 0 else pd.DataFrame()
        with st.container(border=True):
            st.markdown("🏆 **Executive Data Insights Memorandum — Bunch Consulting Corporate Board**")
            st.write(f"1. **Identified Area of Opportunity:** Found **{len(low_perf_leads)}** endpoint agent entities demonstrating device stability indices beneath the target line.")
            st.write("2. **Analytical Interpretation:** Root cause logging verifies a high correlation with obsolete patch bundles and missing credential validation updates.")
            st.write("3. **Actionable Strategic Recommendation:** Execute automated mass PowerShell alignment scripting over identified target vectors to eliminate processing friction.")
        if len(low_perf_leads) > 0:
            st.error("🚨 Critical Vulnerability Opportunity Track Watchlist:")
            st.dataframe(low_perf_leads[["ticket_id", "incident_subject", "customer_organization", "service_tier_plan", "rmm_agent_status"]], use_container_width=True, hide_index=True)

    elif "4. Provides productivity analysis reports" in selected_key_tab:
        st.markdown("### ⏳ Key 4: Helpdesk Optimization & Automation Script Efficiency Audit")
        st.caption("🔗 *SyncroMSP Mapping Source:* Tracked inside **Syncro -> Scripts -> Script Run Logs** profiling performance yield variables.")
        if len(processed_funnel) > 0:
            prod_df = processed_funnel.groupby("automation_policy_group").agg(total_endpoints_managed=("ticket_id", "count"), remaining_open_alerts=("open_warning_flags", "sum"), mean_stability_rating=("system_stability_index", "mean")).reset_index()
            c_p1, c_p2 = st.columns(2)
            with c_p1: st.dataframe(prod_df, use_container_width=True, hide_index=True)
            with c_p2:
                fig_prod = px.bar(prod_df, x="automation_policy_group", y="total_endpoints_managed", title="Total Infrastructure Volume Processed per RMM Policy Group", color_discrete_sequence=["#161B22"])
                st.plotly_chart(fig_prod, use_container_width=True)

    elif "5. Develops and maintains reports to measure operational" in selected_key_tab:
        st.markdown("### ⚙️ Key 5: Helpdesk Channel Allocation & Ticket Ingestion Benchmarks")
        st.caption("🔗 *SyncroMSP Mapping Source:* Sourced from **Syncro -> Tickets -> Inbound Email/Chat Integration** log registers.")
        if len(processed_funnel) > 0:
            util_df = processed_funnel.groupby("channel_preference").size().reset_index(name="active_allocated_leads")
            c_u1, c_u2 = st.columns(2)
            with c_u1: st.dataframe(util_df, use_container_width=True, hide_index=True)
            with c_u2:
                fig_util = px.pie(util_df, values="active_allocated_leads", names="channel_preference", title="Ingested Helpdesk Interaction Channel Utilization Share", color_discrete_sequence=msp_color_palette, hole=0.4)
                st.plotly_chart(fig_util, use_container_width=True)

    elif "7. Compiles recurring operational review that includes trend analysis" in selected_key_tab:
        st.markdown("### 📈 Key 7: Multi-Quarter Infrastructure System Performance Trend Review")
        st.caption("🔗 *SyncroMSP Mapping Source:* Sourced from **Syncro -> Reports -> Customer SLA Breach Gaps** longitudinal matrices.")
        
        # FIXED: Bound explicitly to bunch_capacity_db arrays using targeted columns to eliminate KeyErrors completely
        trend_df = st.session_state.bunch_capacity_db.copy()
        trend_df["retention_shortfall"] = trend_df["target_sla_pct"] - trend_df["actual_sla_pct"]
        c_t1, c_t2 = st.columns([2, 3])
        with c_t1: st.dataframe(trend_df[["infrastructure_node", "target_sla_pct", "actual_sla_pct", "retention_shortfall"]], use_container_width=True, hide_index=True)
        with c_t2:
            fig_trend = px.line(trend_df, x="infrastructure_node", y="retention_shortfall", title="Longitudinal Core SLA Performance Gaps Profile Trends", markers=True, color_discrete_sequence=["#FF5722"])
            st.plotly_chart(fig_trend, use_container_width=True)
