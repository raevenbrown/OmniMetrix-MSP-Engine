import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration Setup
st.set_page_config(page_title="OmniMetrix Enterprise OS", layout="wide")

# ==========================================
# CENTRAL STATE DATABASE (WHITELABELED & RE-ENGINEERED)
# ==========================================

# Persistent Session State: Advanced Helpdesk Ticketing Log Matrix
if "ticket_db" not in st.session_state:
    st.session_state.ticket_db = pd.DataFrame({
        "ticket_id": [301, 302, 303, 304, 305, 306, 307, 308],
        "client_name": ["Alpha Logistics", "Beta Healthcare Network", "Gamma Financial", "Alpha Logistics", "Delta E-Commerce", "Beta Healthcare Network", "Gamma Financial", "Epsilon Legal"],
        "assigned_tech": ["Raeven Brown", "Alex Mercer", "Raeven Brown", "Unassigned", "Sarah Jenkins", "Alex Mercer", "Unassigned", "Sarah Jenkins"],
        "task_category": ["M365 Admin Center", "SharePoint Online", "M365 Identity", "M365 Admin Center", "M365 Identity", "SharePoint Online", "Offboarding & Security", "M365 Identity"],
        "issue_description": [
            "Create corporate Distribution List and Mail-Enabled Security Group for Operations team.",
            "Provision secure Document Library structure for internal compliance file sync.",
            "Enforce MFA and Strong Authentication validation across all finance team accounts.",
            "Provision a new user account with full Teams license configuration and custom email alias.",
            "Perform emergency account deletion and revoke active Microsoft 365 access tokens.",
            "Troubleshoot document permissions and broken inheritance rules on project folder.",
            "Perform full user removal: archive mailbox, strip security groups, remove from Teams.",
            "Configure self-service password reset (SSPR) authentication policies."
        ],
        "priority": ["Medium", "High", "Critical", "Low", "Critical", "Medium", "High", "Medium"],
        "status": ["Open", "In Progress", "Open", "Unassigned", "Open", "In Progress", "Unassigned", "Resolved"],
        "time_logged_minutes": [0, 15, 0, 0, 0, 45, 0, 90],
        "technician_notes": ["", "Shared library configured.", "", "", "", "Permissions re-inherited down to subfolders.", "", "SSPR verified successfully."]
    })

# Persistent Session State: Live RMM Hardware Asset Inventory & Telemetry
if "rmm_db" not in st.session_state:
    st.session_state.rmm_db = pd.DataFrame({
        "asset_id": ["WS-01", "SRV-02", "WS-03", "WS-04", "SRV-05", "FW-06", "SW-07"],
        "client_name": ["Alpha Logistics", "Beta Healthcare Network", "Gamma Financial", "Delta E-Commerce", "Alpha Logistics", "Beta Healthcare Network", "Gamma Financial"],
        "device_name": ["ALPHA-DESK01", "BETA-HIPAA-SRV", "GAMMA-FIN-WS03", "DELTA-WEB-STORE", "ALPHA-PROXY-SRV", "BETA-EDGE-GATE", "GAMMA-CORE-SW"],
        "device_type": ["Workstation", "Server", "Workstation", "Workstation", "Server", "WAN Edge Firewall", "Switch"],
        "serial_number": ["SN-78421-A", "SN-99210-B", "SN-11452-C", "SN-88421-D", "SN-55621-E", "SN-22104-F", "SN-33491-G"],
        "ram_gb": [16, 64, 32, 16, 128, 8, 4],
        "remote_screen_access": ["Available - View Live", "Available - View Live", "Offline", "Available - View Live", "Available - View Live", "Console Only", "Console Only"],
        "patch_status": ["Needs Reboot", "Needs Review", "Installed", "Needs Review", "Installed", "Installed", "Needs Reboot"],
        "patch_age_days": [25, 48, 0, 48, 0, 0, 50],
        "email_alert_threshold": ["Alert Sent (Age > 14d)", "Alert Sent (Age > 14d)", "Compliant", "Alert Sent (Age > 14d)", "Compliant", "Compliant", "Alert Sent (Age > 14d)"],
        "active_rmm_alert": ["None", "Cpu Monitoring: Usage over 90%", "App Crash Trigger: ID 1042", "Low Hd Space: Drive C under 10%", "None", "None", "None"]
    })

# Client Contract Financial Matrix (With Target Pipelines, Renewal Status, and Goals)
client_matrix_data = pd.DataFrame({
    "client_name": ["Alpha Logistics", "Beta Healthcare Network", "Gamma Financial", "Delta E-Commerce"],
    "service_tier": ["Silver Tier", "Platinum Tier", "Gold Tier", "Silver Tier"],
    "seat_count": [50, 40, 35, 25],
    "monthly_recurring_revenue": [4250.00, 7000.00, 4375.00, 2125.00],
    "contract_length_term": ["1-Year Commitment", "2-Year Commitment", "6-Month Short Term", "Month-to-Month Retainer"],
    "relationship_age_months": [18, 24, 12, 6],
    "monthly_bill_status": ["Paid", "Paid", "Overdue", "Paid"],
    "out_of_scope_spend": [350.00, 1200.00, 0.00, 150.00],
    "exit_risk_status": ["Safe", "Safe", "🔴 CRITICAL: Exiting Next Month", "Reviewing Renewal"]
})

pipeline_data = pd.DataFrame({
    "Prospect Name": ["Zeta Manufacturing", "Sigma Consulting Group", "Omega Capital LLC", "Tau Wellness Inc"],
    "Deal Class Pipeline": ["Pipeline Target (To Win)", "Pipeline Target (To Win)", "Pending High Close", "Pending High Close"],
    "Target Pricing Tier": ["Platinum Tier ($175/mo)", "Gold Tier ($125/mo)", "Platinum Tier ($175/mo)", "Silver Tier ($85/mo)"],
    "Projected Seats": [120, 45, 85, 30],
    "Estimated Value": [21000.00, 5625.00, 14875.00, 2550.00],
    "Confidence Score": ["35%", "50%", "85%", "90%"]
})

# 2. Sidebar Layout Console
st.sidebar.title("💎 OmniMetrix Command Suite")
st.sidebar.markdown("**Active Engineer Identity:** `Raeven Brown` ")
st.sidebar.markdown("**Network Sync:** `● NOC Connected`")
st.sidebar.write("---")

# Corporate Tenant Switching Matrix
st.sidebar.subheader("🏢 Account Tenant Context")
client_selection = st.sidebar.selectbox(
    "Active Tenant Scope:",
    options=["All Managed Accounts"] + list(client_matrix_data["client_name"].unique())
)

# Apply Isolation Filters across objects
if client_selection == "All Managed Accounts":
    filtered_tickets = st.session_state.ticket_db
    filtered_rmm = st.session_state.rmm_db
    filtered_matrix = client_matrix_data
else:
    filtered_tickets = st.session_state.ticket_db[st.session_state.ticket_db["client_name"] == client_selection]
    filtered_rmm = st.session_state.rmm_db[st.session_state.rmm_db["client_name"] == client_selection]
    filtered_matrix = client_matrix_data[client_matrix_data["client_name"] == client_selection]

st.sidebar.write("---")

# Navigation Panel Matrix
st.sidebar.subheader("🏁 Operational Navigation")
app_panel = st.sidebar.radio(
    "Select Management Module Panel:",
    [
        "📋 Client Helpdesk Portal", 
        "⚙️ RMM Alerts & Asset Telemetry",
        "💰 Tier Revenue & Financial Targets", 
        "📧 Email Marketing Analytics", 
        "📱 Social Media Performance", 
        "🎯 Digital Ad Spend Performance"
    ]
)

st.write("---")

# ==========================================
# MODULE 1: CLIENT HELPDESK PORTAL
# ==========================================
if app_panel == "📋 Client Helpdesk Portal":
    st.header("📋 Daily Inbound Operations & Ticket Workbench")
    
    # Advanced Engineer Ticket Filter Queue Routing
    st.markdown("### 🗂️ Helpdesk Operational View Switcher")
    view_selection = st.radio(
        "Filter Workbench Scope Matrix:",
        ["All Tickets", "All Unresolved", "Assigned to Me (Raeven Brown)", "My Queue (In Progress)", "Resolved Tickets", "Subscribed Accounts", "Unassigned Tickets"],
        horizontal=True
    )
    
    # Process Selection Parameters
    if view_selection == "All Unresolved":
        processed_tickets = filtered_tickets[filtered_tickets["status"] != "Resolved"]
    elif view_selection == "Assigned to Me (Raeven Brown)":
        processed_tickets = filtered_tickets[filtered_tickets["assigned_tech"] == "Raeven Brown"]
    elif view_selection == "My Queue (In Progress)":
        processed_tickets = filtered_tickets[(filtered_tickets["assigned_tech"] == "Raeven Brown") & (filtered_tickets["status"] == "In Progress")]
    elif view_selection == "Resolved Tickets":
        processed_tickets = filtered_tickets[filtered_tickets["status"] == "Resolved"]
    elif view_selection == "Subscribed Accounts":
        processed_tickets = filtered_tickets[filtered_tickets["priority"].isin(["High", "Critical"])]
    elif view_selection == "Unassigned Tickets":
        processed_tickets = filtered_tickets[filtered_tickets["status"] == "Unassigned"]
    else:
        processed_tickets = filtered_tickets

    # Live Counters
    tc1, tc2, tc3 = st.columns(3)
    with tc1: st.metric("Active Queue Ticket Volume", value=len(processed_tickets))
    with tc2: st.metric("Unassigned Tasks Pending Routing", value=len(filtered_tickets[filtered_tickets["status"] == "Unassigned"]))
    with tc3: st.metric("Total System Engineering Logs", value=f"{filtered_tickets['time_logged_minutes'].sum()} Mins")
        
    st.write("")
    st.dataframe(processed_tickets, use_container_width=True, hide_index=True)
    st.write("---")
    
    # Interactive Workstation Hook
    st.subheader("🛠️ Active Ticket Workbench Engine")
    if len(processed_tickets) > 0:
        target_id = st.selectbox("Mount Ticket to Action Center ID:", options=processed_tickets["ticket_id"].unique())
        idx = st.session_state.ticket_db[st.session_state.ticket_db["ticket_id"] == target_id].index[0]
        row = st.session_state.ticket_db.loc[idx]
        
        with st.container(border=True):
            w_col1, w_col2 = st.columns(2)
            with w_col1:
                st.markdown(f"**🏢 Client Tenant Context:** `{row['client_name']}` | **📁 Category:** `{row['task_category']}`")
                st.markdown(f"**👤 Assigned Personnel Engineer:** `{row['assigned_tech']}`")
                st.markdown(f"**📝 Scope Statement:** *{row['issue_description']}*")
            with w_col2:
                st.markdown(f"**⚙️ Ticket Workflow Status:** `{row['status']}`")
                st.markdown(f"**⏳ Billable Tech Time Counter:** `{row['time_logged_minutes']} Mins`")
                
        w_in1, w_in2, w_in3, w_in4 = st.columns([1, 1, 2, 1])
        with w_in1:
            time_add = st.selectbox("Log Billable Time Slot:", options=[0, 15, 30, 45, 60, 120], format_func=lambda x: f"{x} Mins")
        with w_in2:
            assign_update = st.selectbox("Reassign Personnel Role:", options=["Raeven Brown", "Alex Mercer", "Sarah Jenkins", "Unassigned"])
        with w_in3:
            note_add = st.text_input("Append Engineering Case File Log Notes:")
        with w_in4:
            state_update = st.selectbox("Flag Status Tier:", options=["Open", "In Progress", "Resolved", "Unassigned"])
            
        if st.button("🚀 Push Update to Production Framework", use_container_width=True):
            st.session_state.ticket_db.at[idx, "time_logged_minutes"] += time_add
            st.session_state.ticket_db.at[idx, "status"] = state_update
            st.session_state.ticket_db.at[idx, "assigned_tech"] = assign_update
            if note_add:
                st.session_state.ticket_db.at[idx, "technician_notes"] = f"{row['technician_notes']} | {note_add}".strip(" | ")
            st.success("Authorized entry submitted! Rerunning tables.")
            st.rerun()

# ==========================================
# MODULE 2: RMM ALERTS & ASSET TELEMETRY
# ==========================================
elif app_panel == "⚙️ RMM Alerts & Asset Telemetry":
    st.header("⚙️ Remote Monitoring & Automated Patch Infrastructure")
    
    st.subheader("🖥️ Hardware Endpoint Management & Screen Access Monitor")
    st.markdown("##### *Select an asset row to initiate secure remote access tunneling directly into client hardware nodes.*")
    
    # Custom conditional coloring engine for patch compliance states
    def color_patch_rows(row):
        if row["patch_status"] == "Needs Reboot": return ['background-color: #3E2723; color: #FFCC80'] * len(row)
        elif row["patch_status"] == "Needs Review": return ['background-color: #4A3B00; color: #FFE082'] * len(row)
        return [''] * len(row)
        
    st.dataframe(filtered_rmm.style.apply(color_patch_rows, axis=1), use_container_width=True, hide_index=True)
    st.write("---")
    
    st.subheader("📡 Live Remote Session Portal")
    remote_target = st.selectbox("Choose Hardware Node to Mount Screen Tunnel:", options=filtered_rmm["device_name"])
    r_row = filtered_rmm[filtered_rmm["device_name"] == remote_target].iloc[0]
    
    with st.container(border=True):
        m_c1, m_c2 = st.columns(2)
        with m_c1:
            st.markdown(f"### 🖥️ Virtual Workspace: `{r_row['device_name']}`")
            st.markdown(f"* **Hardware Serial Hash:** `{r_row['serial_number']}`")
            st.markdown(f"* **Total Provisioned System Memory:** `{r_row['ram_gb']} GB RAM`")
            st.markdown(f"* **Patching Status Cycle:** `{r_row['patch_status']} ({r_row['patch_age_days']} Days Unresolved)`")
        with m_c2:
            st.markdown(f"#### 🔒 Screen Tunnel: `{r_row['remote_screen_access']}`")
            if "Available" in r_row['remote_screen_access']:
                st.button(f"🔌 Establish Live Remote Desktop Stream to {r_row['device_name']}", use_container_width=True)
                st.success("Security token clear. Secure Shell (SSH) and VNC frame listener buffer mapping is ready.")
            else:
                st.error("Connection Dropped. Remote agent reporting terminal is currently offline.")

# ==========================================
# MODULE 3: TIER REVENUE & FINANCIAL TARGETS
# ==========================================
elif app_panel == "💰 Tier Revenue & Financial Targets":
    st.header("💰 Account Profitability Matrix & Contract Commitment Terminals")
    
    # Financial Corporate Macro Goals Verification
    st.subheader("🎯 Executive Run-Rate Corporate Goal Trackers (2026 Fiscal Cycle)")
    g1, g2, g3 = st.columns(3)
    with g1: st.metric("Monthly Revenue Goal ($15K Baseline)", value=f"${filtered_matrix['monthly_recurring_revenue'].sum():,.2f}", delta="+ $2,750 Above Track")
    with g2: st.metric("Quarterly Growth Metric ($50K)", value="$53,550.00", delta="+6.2% Pace")
    with g3: st.metric("Yearly Recurring Target ($200K)", value="$214,200.00 Run-Rate", delta="🟢 Goal Target Attained")
    
    st.write("---")
    
    # Contract Lifecycles and Exiting Flags
    st.subheader("🏢 Active Portfolio Audit & Agreement Expiry Lifecycle Alerts")
    st.dataframe(filtered_matrix, use_container_width=True, hide_index=True)
    st.write("---")
    
    # Forward Sales Pipelines: Targets to Win vs Pending High Closes
    st.subheader("📈 Forward Revenue Pipeline Acquisitions Matrix")
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        st.markdown("#### 🎯 Pipeline Targets (To Win Across Fields)")
        st.dataframe(pipeline_data[pipeline_data["Deal Class Pipeline"] == "Pipeline Target (To Win)"], use_container_width=True, hide_index=True)
    with col_p2:
        st.markdown("#### 🔥 Pending High-Confidence Closes")
        st.dataframe(pipeline_data[pipeline_data["Deal Class Pipeline"] == "Pending High Close"], use_container_width=True, hide_index=True)

# ==========================================
# MODULE 4: EMAIL MARKETING ANALYTICS
# ==========================================
elif app_panel == "📧 Email Marketing Analytics":
    st.header("📧 Growth Performance & Specialized Outreach Funnel Segments")
    
    # Segment Dropdown Workspace Selector
    st.markdown("### 🗂️ Specialized Customer Segment Filters")
    email_segment = st.selectbox("Select Target Campaign Category Loop:", ["1. Existing Retained Customers Base", "2. Patching Alert Overdue Notifications", "3. Inbound Prospects (Sourced via Social Media)", "4. Cold/Warm Leads Sourced from Local B2B Events"])
    
    if "Existing" in email_segment:
        st.info("📊 **Segment Target:** Active client organizations mapped to current monthly billing profiles. Goal: Drive system retention and announce new security tiers.")
    elif "Patching" in email_segment:
        st.warning("⚠️ **Segment Target:** System managers running unpatched hardware networks older than 14 days. Purpose: Send automated critical system warnings.")
    elif "Social" in email_segment:
        st.success("📱 **Segment Target:** Inbound leads acquired from high-ROI video guides. Strategy: Nurture interest into scheduled discovery calls.")
    else:
        st.info("🤝 **Segment Target:** Warm business profiles captured from regional B2B exhibitions. Strategy: Offer zero-obligation security risk maps.")
        
    st.write("---")
    
    # Performance metrics including conversions and conversions metrics
    st.subheader("📊 Performance Telemetry & Funnel Drop-off Auditing")
    
    funnel_df = pd.DataFrame({
        "Campaign Metric Parameter": ["Total Dispatched Volumes", "Delivered Base Emails", "Opened Event Actions", "Link Click Tracker", "Upgraded / Closed Conversions"],
        "Existing Retained Base": [420, 418, 310, 184, 14],
        "Patching Overdue Notices": [850, 842, 610, 412, 56],
        "Social Inbound Prospects": [2400, 2380, 1150, 680, 28],
        "B2B Local Event Lists": [350, 348, 190, 88, 12]
    })
    
    fig_funnel = px.bar(funnel_df, x="Campaign Metric Parameter", y=["Existing Retained Base", "Patching Overdue Notices", "Social Inbound Prospects", "B2B Local Event Lists"], barmode="group", title="Granular Funnel Velocity & Pipeline Leak Drops")
    st.plotly_chart(fig_funnel, use_container_width=True)
    
    st.markdown("#### 🔍 Funnel Leak Identification Notes:")
    st.error("**Drop-off Discovery:** The 'Social Inbound Prospects' campaign suffers a steep 52% drop-off from Delivered down to Opened actions. *Diagnostic:* Subject lines are too broad. Re-engineer titles to focus directly on specific administrative problem points.")

# ==========================================
# MODULE 5: SOCIAL MEDIA PERFORMANCE
# ==========================================
elif app_panel == "📱 Social Media Performance":
    st.header("📱 Multi-Platform Content Analysis & Competitive Market Tracking")
    
    # Time series line graph tracking audience growth curves chronologically
    st.subheader("📈 Chronological Network Follower Growth Velocity Tracker")
    growth_history = pd.DataFrame({
        "Quarter Timeline": ["2025-Q1", "2025-Q2", "2025-Q3", "2025-Q4", "2026-Q1", "2026-Q2"],
        "LinkedIn Growth": [1200, 2400, 3800, 5100, 6800, 8450],
        "YouTube Growth": [1500, 3100, 5400, 7800, 9900, 12100],
        "Twitter/X Growth": [22000, 21950, 21900, 21850, 21820, 21800]
    })
    fig_growth = px.line(growth_history, x="Quarter Timeline", y=["LinkedIn Growth", "YouTube Growth", "Twitter/X Growth"], markers=True, title="Audience Scaling Performance Timeline Charts")
    st.plotly_chart(fig_growth, use_container_width=True)
    
    st.write("---")
    
    # Granular Platform Channels tables split
    st.subheader("📊 Native Performance Matrices Sliced by Isolated Channel")
    ch_tab1, ch_tab2 = st.tabs(["🔒 LinkedIn Performance Records", "📺 YouTube Platform Matrix"])
    
    with ch_tab1:
        li_df = pd.DataFrame({
            "LinkedIn Core Asset Post": ["M365 User Offboarding Action Guide Video", "Ransomware Defense Text Story", "Quote Cards Graphics Pack"],
            "Impressions Shared": [12400, 3200, 210],
            "Likes": [412, 92, 14],
            "Shares": [89, 11, 1],
            "Clicks Generated": [214, 45, 0],
            "Growth Factor Contribution": ["🔥 Primary Growth Engine: High Clicks", "🟡 Baseline Brand Asset", "❌ Drag Asset: Lowering Metrics"]
        })
        st.dataframe(li_df, use_container_width=True, hide_index=True)
        
    with ch_tab2:
        yt_df = pd.DataFrame({
            "YouTube Video Asset Target": ["SharePoint Permissions Architecture Guide", "M365 Admin Walkthrough Masterclass", "Shorts Channel Promos"],
            "Video Views Count": [28500, 14100, 850],
            "Likes": [1840, 612, 12],
            "Comments": [142, 56, 1],
            "Subscribers Acquired": [865, 310, 2],
            "Growth Factor Contribution": ["🔥 Primary Scale Catalyst: Heavy Subs", "🔥 Strong Lead Gen Pipeline", "❌ Drag Asset: Weak User Conversions"]
        })
        st.dataframe(yt_df, use_container_width=True, hide_index=True)

    st.write("---")
    
    # Competitor Tracking Frame Matrix Layout
    st.subheader("🕵️ Competitor Benchmark Intelligence Grid")
    comp_df = pd.DataFrame({
        "Anonymized Competitor Profile": ["Competitor Alpha (Local)", "Competitor Beta (Regional SaaS)", "Competitor Gamma (National Enterprise)"],
        "Observed Strategy Strengths": ["Heavy localized presence at chamber of commerce network meetings.", "Publishing weekly blog articles covering basic industry topics.", "Heavy investment in paid corporate ad assets across search indices."],
        "Identified Content Weaknesses": ["Completely missing online technical tutorials or video assets.", "Weak user engagement metrics; low-energy content updates.", "Cold, generic brand identity that feels detached from customers."],
        "OmniMetrix Strategic Exploitation Blueprint": [
            "Exploit their lack of video content by pushing high-value M365 guide videos to capture local authority.",
            "Produce higher-quality interactive tutorial materials to draw their organic search audiences away.",
            "Lean hard on our personalized B2B client context and responsive helpdesk script support models to win deals."
        ]
    })
    st.dataframe(comp_df, use_container_width=True, hide_index=True)

# ==========================================
# MODULE 6: DIGITAL AD SPEND PERFORMANCE
# ==========================================
elif app_panel == "🎯 Digital Ad Spend Performance":
    st.header("🎯 Multi-Channel Paid Acquisition & Budget Tracking Matrix")
    
    st.subheader("📊 Q1 vs Q2 Historical Campaign Performance Audit (2026)")
    st.markdown("##### *Comprehensive forensic analysis mapping exactly what strategies succeeded, which initiatives failed, and the direct business rationale.*")
    
    ad_forensic_df = pd.DataFrame({
        "Quarter Window": ["Q1 2026", "Q1 2026", "Q2 2026", "Q2 2026"],
        "Campaign Asset Network": ["Google Intent Search (Keywords: IT Helpdesk, M365 Setup)", "Meta Lookalikes (Quote Cards Assets)", "LinkedIn Message Ads (Targeting: Corporate Partners)", "Google Intent Search (Keywords: M365 Account Deletion)"],
        "Deployed Capital": [4500.00, 1500.00, 2500.00, 6000.00],
        "Acquired Leads": [34, 2, 12, 58],
        "ROAS Ratios": ["3.8x Return", "0.4x Loss", "3.1x Return", "5.2x Return"],
        "Operational Outcome State": ["🟢 SUCCESSFUL PIPELINE", "❌ UNPROFITABLE FAIL NODE", "🟢 SUCCESSFUL PIPELINE", "🔥 HIGHEST RUN-RATE MARGIN"],
        "Analytical Root-Cause Rationale (Why)": [
            "High inbound search intent matches clear solution requirements; buyers have budget ready.",
            "B2B managers and decision makers do not click social quote assets when sourcing security engines.",
            "Direct personalization hooks landing directly in executive inboxes hit targets cleanly.",
            "Targeting exact corporate problem sets (like 'M365 offboarding friction') secures buyers instantly."
        ]
    })
    
    # Apply row coloring engine to isolate ad spend success vectors
    def color_ad_rows(row):
        if "SUCCESSFUL" in row["Operational Outcome State"] or "HIGHEST" in row["Operational Outcome State"]:
            return ['background-color: #1B5E20; color: white'] * len(row)
        elif "FAIL" in row["Operational Outcome State"]:
            return ['background-color: #B71C1C; color: white'] * len(row)
        return [''] * len(row)
        
    st.dataframe(ad_forensic_df.style.apply(color_ad_rows, axis=1), use_container_width=True, hide_index=True)
