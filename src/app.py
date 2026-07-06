import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Main Page Canvas Configuration
st.set_page_config(page_title="OmniMetrix OS Master Suite", layout="wide")

# ==========================================
# CENTRALIZED PERSISTENT DATA RECORD STREAMS
# ==========================================

# Initialize Helpdesk Queue reflecting custom M365 administrative tickets
if "ticket_db" not in st.session_state:
    st.session_state.ticket_db = pd.DataFrame({
        "ticket_id": [301, 302, 303, 304, 305, 306, 307],
        "client_name": ["Southeast Bookkeeping", "Expert Innovative Solutions", "My Velocity Group", "Southeast Bookkeeping", "Horizon Retail", "Expert Innovative Solutions", "My Velocity Group"],
        "task_category": ["M365 Admin Center", "SharePoint Online", "M365 Identity", "M365 Admin Center", "M365 Identity", "SharePoint Online", "Offboarding & Security"],
        "issue_description": [
            "Create corporate Distribution List and Mail-Enabled Security Group for Operations team.",
            "Provision secure Document Library structure for internal HIPAA auditing file sync.",
            "Enforce MFA and Strong Authentication validation across all finance team accounts.",
            "Provision a new user account with full Teams license configuration and custom email alias.",
            "Perform emergency account deletion and revoke active Microsoft 365 access tokens.",
            "Troubleshoot document permissions and broken inheritance rules on project folder.",
            "Perform full user removal: archive mailbox, strip security groups, remove from Teams."
        ],
        "priority": ["Medium", "High", "Critical", "Low", "Critical", "Medium", "High"],
        "status": ["Open", "In Progress", "Resolved", "Open", "Open", "In Progress", "Open"],
        "time_logged_minutes": [0, 15, 60, 0, 0, 45, 0],
        "technician_notes": ["", "Shared library configured; waiting on final user list.", "MFA enforced successfully via conditional access policies.", "", "", "Permissions re-inherited down to subfolders.", ""]
    })

# Initialize Real RMM Endpoint Alerts Data
rmm_alert_data = pd.DataFrame({
    "alert_id": [901, 902, 903, 904, 905, 906],
    "client_name": ["Bunch Consulting LLC", "Expert Innovative Solutions", "Southeast Bookkeeping", "My Velocity Group", "Southeast Bookkeeping", "My Velocity Group"],
    "asset_name": ["KEIONSPC", "BRIGI", "BIPANAB25", "MVG-291259", "KELLYLAPTOP", "MVG-AHB-OFFICE"],
    "check_type": ["App Crash Trigger", "App Crash Trigger", "App Crash Trigger", "App Crash Trigger", "Cpu Monitoring", "Low Hd Space Trigger"],
    "failure_description": [
        "Application crashes found: system core fault.",
        "Application crashes found: unhandled exception.",
        "Application crashes found: memory overflow leak.",
        "Application crashes found: trace thread exit.",
        "Alert when CPU usage is over 90% for 15 consecutive minutes.",
        "Some disks are low on space. Drive C: capacity dropping below 5%."
    ],
    "severity": ["High", "High", "Medium", "High", "Critical", "Critical"]
})

# Initialize Real Device Patch Management Data
patch_data = pd.DataFrame({
    "asset_name": ["BC-BAILEY", "BC-BAILEY", "MVG-OHH21S5", "BC-BAILEY", "BC-BAILEY", "MVG-OHH21S5"],
    "client_name": ["Bunch Consulting LLC", "Bunch Consulting LLC", "My Velocity Group", "Bunch Consulting LLC", "Bunch Consulting LLC", "My Velocity Group"],
    "patch_category": ["Security Updates", "Drivers", "Drivers", "Drivers", "Drivers", "Drivers"],
    "kb_id": ["KB5094126", "M-Driver", "Net-Driver", "Intel-Update", "Dell-Software", "Surface-Sys"],
    "patch_title": ["2026-06 Security Update", "Intel Extension Driver", "Realtek - Net - 1153.1", "Intel Driver Update (2.4)", "Dell Inc. SoftwareComponent", "Surface - System - 6.2"],
    "patch_status": ["Needs Reboot", "Needs Review", "Needs Review", "Needs Review", "Needs Review", "Needs Review"],
    "operating_system": ["Windows 11 Pro", "Windows 11 Pro", "Windows 11 Pro", "Windows 11 Pro", "Windows 11 Pro", "Windows 11 Pro"]
})

# Initialize Master Client Account Ledger Data
client_matrix_data = pd.DataFrame({
    "client_name": ["Southeast Bookkeeping", "Expert Innovative Solutions", "My Velocity Group", "Horizon Retail", "Bunch Consulting LLC"],
    "service_tier": ["Silver ($85/mo)", "Platinum ($175/mo)", "Gold ($125/mo)", "Silver ($85/mo)", "Platinum ($175/mo)"],
    "seat_count": [50, 40, 35, 25, 60],
    "monthly_recurring_revenue": [4250.00, 7000.00, 4375.00, 2125.00, 10500.00],
    "relationship_length_months": [18, 24, 12, 6, 36],
    "monthly_bill_status": ["Paid", "Paid", "Overdue", "Paid", "Paid"],
    "out_of_scope_spend": [350.00, 1200.00, 0.00, 150.00, 2500.00]
})

# 2. Sidebar Layout Console (Creative Metrix UI Pattern)
st.sidebar.title("💎 OmniMetrix Command Suite")
st.sidebar.markdown("**System Class:** `MSP Management Portal` ")
st.sidebar.markdown("**Network Sync:** `● SOC Live Mesh Active`")
st.sidebar.write("---")

# Corporate Tenant Switching Selector Matrix
st.sidebar.subheader("🏢 Account Tenant Context")
client_selection = st.sidebar.selectbox(
    "Active Tenant Scope:",
    options=["All Managed Accounts"] + list(client_matrix_data["client_name"].unique())
)

# Apply Multi-Tenant Isolation Filter across tables
if client_selection == "All Managed Accounts":
    filtered_tickets = st.session_state.ticket_db
    filtered_matrix = client_matrix_data
    filtered_alerts = rmm_alert_data
    filtered_patches = patch_data
else:
    filtered_tickets = st.session_state.ticket_db[st.session_state.ticket_db["client_name"] == client_selection]
    filtered_matrix = client_matrix_data[client_matrix_data["client_name"] == client_selection]
    filtered_alerts = rmm_alert_data[rmm_alert_data["client_name"] == client_selection]
    filtered_patches = patch_data[patch_data["client_name"] == client_selection]

st.sidebar.write("---")

# Navigation Panel Option Matrix (Unified Under Operational Navigation)
st.sidebar.subheader("🏁 Operational Navigation")
app_panel = st.sidebar.radio(
    "Select Management Module Panel:",
    [
        "📋 Client Helpdesk Portal", 
        "🤖 RMM Network Alerts & Patching",
        "💰 Tier Revenue & Service Accounts", 
        "📧 Email Marketing Analytics", 
        "📱 Social Media Tracking", 
        "🎯 Digital Ad Spend Performance"
    ]
)

# 3. Main Workspace Routing Layout Header
st.title("🛡️ OmniMetrix Central Business Control Center")
st.markdown(f"Active Context: **{client_selection}** | Operational Panel Focus: **{app_panel}**")
st.write("---")

# ==========================================
# MODULE 1: CLIENT HELPDESK PORTAL
# ==========================================
if app_panel == "📋 Client Helpdesk Portal":
    st.header("📋 Daily Inbound Operations & Ticket Workbench")
    open_load = len(filtered_tickets[filtered_tickets["status"] != "Resolved"])
    
    tc1, tc2, tc3 = st.columns(3)
    with tc1:
        st.metric("Total Inbound Ticket Volume", value=len(filtered_tickets))
    with tc2:
        st.metric("Active Unresolved Workload", value=open_load)
    with tc3:
        total_minutes = filtered_tickets["time_logged_minutes"].sum()
        st.metric("Total Engineering Duration Logged", value=f"{total_minutes} Mins")
        
    st.write("")
    st.subheader("📊 Master Operational Ticket Board (Daily Live Feed)")
    st.dataframe(filtered_tickets, use_container_width=True, hide_index=True)
    st.write("---")
    
    st.subheader("🛠️ Active Ticket Workbench Engine")
    if len(filtered_tickets) > 0:
        target_id = st.selectbox("Mount Ticket to Action Center ID:", options=filtered_tickets["ticket_id"].unique())
        idx = st.session_state.ticket_db[st.session_state.ticket_db["ticket_id"] == target_id].index[0]
        row = st.session_state.ticket_db.loc[idx]
        
        with st.container(border=True):
            w_col1, w_col2 = st.columns(2)
            with w_col1:
                st.markdown(f"**🏢 Client:** `{row['client_name']}` | **📁 Class:** `{row['task_category']}`")
                st.markdown(f"**📝 Scope Statement:** *{row['issue_description']}*")
            with w_col2:
                st.markdown(f"**⚙️ Current State:** `{row['status']}` | **⏳ Duration:** `{row['time_logged_minutes']} Mins`")
                
        w_in1, w_in2, w_in3 = st.columns([1, 2, 1])
        with w_in1:
            time_add = st.selectbox("Log Billable Time Slot:", options=[0, 15, 30, 45, 60, 120], format_func=lambda x: f"{x} Mins")
        with w_in2:
            note_add = st.text_input("Append Engineering Resolution Log notes:")
        with w_in3:
            state_update = st.selectbox("Flag Status Tier:", options=["Open", "In Progress", "Resolved"])
            
        if st.button("🚀 Push Update to Production Framework", use_container_width=True):
            st.session_state.ticket_db.at[idx, "time_logged_minutes"] += time_add
            st.session_state.ticket_db.at[idx, "status"] = state_update
            if note_add:
                st.session_state.ticket_db.at[idx, "technician_notes"] = f"{row['technician_notes']} | {note_add}".strip(" | ")
            st.success("Authorized entry submitted! Rerunning database tables.")
            st.rerun()
    else:
        st.warning("No tracking assets match the filtered filter.")

# ==========================================
# MODULE 2: RMM NETWORK ALERTS & PATCHING
# ==========================================
elif app_panel == "🤖 RMM Network Alerts & Patching":
    st.header("🤖 Remote Monitoring Management (RMM) & Patch Telemetry")
    
    ac1, ac2 = st.columns(2)
    with ac1:
        st.metric("Total Open Telemetry Alerts", value=len(filtered_alerts))
    with ac2:
        st.metric("Pending Vulnerability Patches Checked", value=len(filtered_patches))
        
    st.write("---")
    st.subheader("🚨 Live Automated Endpoint System Alert Matrix")
    st.dataframe(filtered_alerts, use_container_width=True, hide_index=True)
    
    st.write("---")
    st.subheader("🛠️ Asset OS Security Update & Patch Management Log")
    st.dataframe(filtered_patches, use_container_width=True, hide_index=True)
    
    st.write("---")
    st.subheader("📊 Network Alert Threat Severity Concentration")
    fig_alerts = px.bar(filtered_alerts, x="check_type", color="severity", title="RMM Monitoring Failure Triggers by Severity")
    st.plotly_chart(fig_alerts, use_container_width=True)

# ==========================================
# MODULE 3: TIER REVENUE & SERVICE ACCOUNTS
# ==========================================
elif app_panel == "💰 Tier Revenue & Service Accounts":
    st.header("💰 Account Profitability Matrix & Tier Telemetry")
    
    rc1, rc
