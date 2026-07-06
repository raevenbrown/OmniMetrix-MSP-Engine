import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Main Page Canvas Configuration
st.set_page_config(page_title="OmniMetrix OS Suite", layout="wide")

# Persistent Session State 1: Active Helpdesk Queue (M365 & SharePoint Administrative Scopes)
if "ticket_db" not in st.session_state:
    st.session_state.ticket_db = pd.DataFrame({
        "ticket_id": [301, 302, 303, 304, 305, 306, 307],
        "client_name": ["Alpha Logistics", "Beta Healthcare Network", "Gamma Financial", "Alpha Logistics", "Delta E-Commerce", "Beta Healthcare Network", "Gamma Financial"],
        "task_category": ["M365 Admin Center", "SharePoint Online", "M365 Identity", "M365 Admin Center", "M365 Identity", "SharePoint Online", "Offboarding & Security"],
        "issue_description": [
            "Create corporate Distribution List and Mail-Enabled Security Group for Operations team.",
            "Provision secure Document Library structure for internal compliance file sync.",
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

# Persistent Session State 2: Live RMM Device Infrastructure & Patch Telemetry
if "rmm_db" not in st.session_state:
    st.session_state.rmm_db = pd.DataFrame({
        "asset_id": ["WS-01", "SRV-02", "WS-03", "WS-04", "SRV-05", "FW-06", "SW-07"],
        "client_name": ["Alpha Logistics", "Beta Healthcare Network", "Gamma Financial", "Delta E-Commerce", "Alpha Logistics", "Beta Healthcare Network", "Gamma Financial"],
        "device_type": ["Workstation", "Server", "Workstation", "Workstation", "Server", "WAN Edge Firewall", "Switch"],
        "os_platform": ["Windows 11 Pro", "Windows Server 2022", "Windows 11 Pro", "Windows 11 Pro", "Ubuntu Server", "Firmware OS", "Switch OS"],
        "patch_compliance": ["Needs Reboot", "Needs Review", "Installed", "Needs Review", "Installed", "Installed", "Needs Reboot"],
        "active_rmm_alert": ["None", "Cpu Monitoring: Alert usage over 90%", "App Crash Trigger: Event ID 1042", "Low Hd Space Trigger: Drive C under 10%", "None", "None", "None"]
    })

# Master B2B Client Business Profile Table Mapping
client_matrix_data = pd.DataFrame({
    "client_name": ["Alpha Logistics", "Beta Healthcare Network", "Gamma Financial", "Delta E-Commerce"],
    "service_tier": ["Silver Tier", "Platinum Tier", "Gold Tier", "Silver Tier"],
    "seat_count": [50, 40, 35, 25],
    "monthly_recurring_revenue": [4250.00, 7000.00, 4375.00, 2125.00],
    "relationship_length_months": [18, 24, 12, 6],
    "monthly_bill_status": ["Paid", "Paid", "Overdue", "Paid"],
    "out_of_scope_spend": [350.00, 1200.00, 0.00, 150.00]
})

# 2. Sidebar Layout Console
st.sidebar.title("💎 OmniMetrix Command Suite")
st.sidebar.markdown("**System Class:** `MSP Management Portal` ")
st.sidebar.markdown("**Network Sync:** `● SOC Live Mesh Active`")
st.sidebar.write("---")

# Corporate Tenant Switching Matrix
st.sidebar.subheader("🏢 Account Tenant Context")
client_selection = st.sidebar.selectbox(
    "Active Tenant Scope:",
    options=["All Managed Accounts"] + list(client_matrix_data["client_name"].unique())
)

# Apply Multi-Tenant Isolation Filter across tables
if client_selection == "All Managed Accounts":
    filtered_tickets = st.session_state.ticket_db
    filtered_rmm = st.session_state.rmm_db
    filtered_matrix = client_matrix_data
else:
    filtered_tickets = st.session_state.ticket_db[st.session_state.ticket_db["client_name"] == client_selection]
    filtered_rmm = st.session_state.rmm_db[st.session_state.rmm_db["client_name"] == client_selection]
    filtered_matrix = client_matrix_data[client_matrix_data["client_name"] == client_selection]

st.sidebar.write("---")

# Navigation Panel Option Matrix (Unified Under Operational Navigation)
st.sidebar.subheader("🏁 Operational Navigation")
app_panel = st.sidebar.radio(
    "Select Management Module Panel:",
    [
        "📋 Client Helpdesk Portal", 
        "⚙️ RMM Alerts & Patch Management",
        "💰 Tier Revenue & Service Accounts", 
        "📧 Email Marketing Analytics", 
        "📱 Social Media Tracking", 
        "🎯 Digital Ad Spend Performance"
    ]
)

# 3. Main Workspace Routing Layout
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
        st.warning("No tracking assets match the filtered criteria.")

# ==========================================
# MODULE 2: RMM ALERTS & PATCH MANAGEMENT
# ==========================================
elif app_panel == "⚙️ RMM Alerts & Patch Management":
    st.header("⚙️ Remote Monitoring & Automated Patch Infrastructure")
    
    # RMM Summary Cards
    rc1, rc2, rc3 = st.columns(3)
    with rc1:
        st.metric("Total Infrastructure Devices Tracked", value=len(filtered_rmm))
    with rc2:
        active_alerts = len(filtered_rmm[filtered_rmm["active_rmm_alert"] != "None"])
        st.metric("Critical Active Device Alerts", value=active_alerts)
    with rc3:
        needs_reboot = len(filtered_rmm[filtered_rmm["patch_compliance"] == "Needs Reboot"])
        st.metric("Assets Pending OS Reboot", value=needs_reboot)
        
    st.write("---")
    st.subheader("🖥️ Network Asset Inventory & Security Vulnerability Feed")
    
    # Custom colored table styling engine for patch compliance states
    def color_patch_rows(row):
        if row["patch_compliance"] == "Needs Reboot":
            return ['background-color: #3E2723; color: #FFCC80'] * len(row)
        elif row["patch_compliance"] == "Needs Review":
            return ['background-color: #4A3B00; color: #FFE082'] * len(row)
        return [''] * len(row)
        
    st.dataframe(filtered_rmm.style.apply(color_patch_rows, axis=1), use_container_width=True, hide_index=True)
    st.write("---")
    
    # Distribution Visual Charts
    p_col1, p_col2 = st.columns(2)
    with p_col1:
        fig_patch_pie = px.pie(filtered_rmm, names="patch_compliance", hole=0.4, title="Patch Management Asset Status Shares",
                               color_discrete_map={"Installed": "#00E676", "Needs Review": "#FFEA00", "Needs Reboot": "#D500F9"})
        st.plotly_chart(fig_patch_pie, use_container_width=True)
    with p_col2:
        fig_device_bar = px.bar(filtered_rmm, x="device_type", color="os_platform", title="Managed Operating System Assets by Architecture",
                                labels={"device_type": "Hardware Class", "count": "Device Total Volume"})
        st.plotly_chart(fig_device_bar, use_container_width=True)

# ==========================================
# MODULE 3: TIER REVENUE & SERVICE ACCOUNTS
# ==========================================
elif app_panel == "💰 Tier Revenue & Service Accounts":
    st.header("💰 Account Profitability Matrix & Tier Telemetry")
    
    rev_c1, rev_c2, rev_c3 = st.columns(3)
    with rev_c1:
        total_mrr = filtered_matrix["monthly_recurring_revenue"].sum()
        st.metric("Aggregated Contract MRR Pipeline", value=f"${total_mrr:,.2f}")
    with rev_c2:
        total_extra = filtered_matrix["out_of_scope_spend"].sum()
        st.metric("Out-of-Scope Project Billings (Ad-Hoc)", value=f"${total_extra:,.2f}")
    with rev_c3:
        overdue_invoices = len(filtered_matrix[filtered_matrix["monthly_bill_status"] == "Overdue"])
        st.metric("Delinquent Overdue Client Accounts", value=overdue_invoices, delta="Action Required", delta_color="inverse")
        
    st.write("---")
    st.subheader("🏢 Contract Relationship & Financial Audit Grid")
    st.dataframe(filtered_matrix, use_container_width=True, hide_index=True)
    st.write("---")
    
    g_col1, g_col2 = st.columns(2)
    with g_col1:
        fig_packages = px.bar(
            client_matrix_data, x="service_tier", y="monthly_recurring_revenue", color="client_name",
            title="Macro Pricing Tier Revenue Capture Map",
            labels={"service_tier": "Subscribed Tier Strategy", "monthly_recurring_revenue": "Total Contract MRR ($)"}
        )
        st.plotly_chart(fig_packages, use_container_width=True)
    with g_col2:
        fig_scope = px.pie(
            filtered_matrix, values="out_of_scope_spend", names="client_name", hole=0.4,
            title="Ad-Hoc Project Beyond Monthly Contract Base Split",
            color_discrete_sequence=px.colors.sequential.Purples_r
        )
        st.plotly_chart(fig_scope, use_container_width=True)

# ==========================================
# MODULE 4: EMAIL MARKETING ANALYTICS
# ==========================================
elif app_panel == "📧 Email Marketing Analytics":
    st.header("📧 Growth Performance & B2B Lead List Segments")
    
    st.subheader("👥 Active Subscriber Target Segments")
    list_col1, list_col2 = st.columns([1, 1])
    with list_col1:
        segment_df = pd.DataFrame({
            "B2B Industry Focus": ["Certified Public Accountants (CPAs)", "Law Firms & Attorneys", "Real Estate Agencies", "Medical Practices (HIPAA)"],
            "Active Leads": [4500, 3200, 4100, 2450],
            "Engagement Health": ["High (42% Open)", "Medium (29% Open)", "High (38% Open)", "Critical (18% Open)"]
        })
        st.dataframe(segment_df, use_container_width=True, hide_index=True)
    with list_col2:
        fig_seg = px.pie(segment_df, values="Active Leads", names="B2B Industry Focus", hole=0.4,
                         title="Lead Database Share by Target Niche Segment",
                         color_discrete_sequence=["#9C27B0", "#00B0FF", "#00E676", "#FFEA00"])
        st.plotly_chart(fig_seg, use_container_width=True)

    st.write("---")
    st.subheader("📬 Sent Outbound Email Campaigns Audit Log")
    campaign_df = pd.DataFrame({
        "Campaign Date": ["Jul 01, 2026", "Jun 24, 2026", "Jun 15, 2026"],
        "Target Segment": ["Law Firms & Attorneys", "Certified Public Accountants (CPAs)", "Medical Practices (HIPAA)"],
        "Subject Line": [
            "Is your firm's case file backup compliant with upcoming state data privacy laws?",
            "How top CPAs completely secure local QuickBooks environments against tax-season ransomware",
            "Urgent Security Alert: Preventing accidental document leaks on SharePoint networks"
        ],
        "Open Rate": ["31.2%", "44.5%", "19.1%"],
        "Clicks": [142, 312, 48],
        "Performance Status": ["🟢 Above Average Target", "🔥 High Performer", "⚠️ Needs Optimization"]
    })
    st.dataframe(campaign_df, use_container_width=True, hide_index=True)
    
    st.write("")
    st.markdown("#### 🔍 Outbound Email Blueprint Inspection Layout")
    inspect_target = st.selectbox("Select Sent Campaign to Inspect Copy Layout:", options=campaign_df["Target Segment"])
    with st.container(border=True):
        if inspect_target == "Law Firms & Attorneys":
            st.markdown("**Subject:** `Is your firm's case file backup compliant with upcoming state data privacy laws?`")
            st.markdown("**Body Framework Copy Preview:**")
            st.caption("Hello Team, Legal firms are increasingly targeted for client discovery information. If your on-prem server experiences hardware failures today, how fast can you recover a litigation archive? OmniMetrix provides server rollbacks to protect compliance...")
        elif inspect_target == "Certified Public Accountants (CPAs)":
            st.markdown("**Subject:** `How top CPAs completely secure local QuickBooks environments against tax-season ransomware`")
            st.markdown("**Body Framework Copy Preview:**")
            st.caption("Hi there, Tax season brings high volumes of financial document movement. One phishing link can lock up your data and halt tax filing timelines. Here is a step-by-step breakdown of how our strong authentication layers defend financial profiles...")
        else:
            st.markdown("**Subject:** `Urgent Security Alert: Preventing accidental document leaks on SharePoint networks`")
            st.markdown("**Body Framework Copy Preview:**")
            st.caption("Dear Administrator, Healthcare regulations require strict data security on patient tracking fields. Broken file inheritance rules within shared drives could expose internal documentation. Let our security teams trace your permission path maps...")

# ==========================================
# MODULE 5: SOCIAL MEDIA TRACKING
# ==========================================
elif app_panel == "📱 Social Media Tracking":
    st.header("📱 Multi-Platform Content Analysis & Growth Matrices")
    st.subheader("💡 Strategic Content Performance Breakdown")
    
    social_analysis = pd.DataFrame({
        "Social Platform": ["LinkedIn Corporate", "YouTube Explainer", "LinkedIn Corporate", "Twitter/X Flash Alerts", "Instagram Threads"],
        "Content Topic Strategy": ["M365 Account Deletion Step-by-Step Security Video", "How to Build a Custom SharePoint Library Walkthrough", "Text Post: Venting about messy client Excel billing logs", "Ransomware News Flash Link", "Daily motivational workplace quote graphics"],
        "Total Engagement Metric": ["High (2.4K Views, 18 Leads)", "High (4.1K Views, 22 Leads)", "Medium (800 Impressions, 2 Leads)", "Low (40 Views, 0 Clicks)", "Low (12 Likes, 0 Value)"],
        "Performance Classification": ["🔥 WHAT IS WORKING BEST", "🔥 WHAT IS WORKING BEST", "🟡 AVERAGE BASELINE", "❌ STOP CREATING / NOT WORKING", "❌ STOP CREATING / NOT WORKING"],
        "Actionable Next-Step Correction": ["Produce more technical video guides showing backend administrative workflows.", "Double down on long-form tech architectures to build brand authority.", "Keep as occasional filler, but prioritize valuable engineering videos.", "Stop posting text links without original visual context summaries.", "Immediately stop asset burn; B2B tech clients do not engage with quote cards."]
    })
    
    def color_social_rows(row):
        if "WORKING BEST" in row["Performance Classification"]:
            return ['background-color: #1B5E20; color: white'] * len(row)
        elif "NOT WORKING" in row["Performance Classification"]:
            return ['background-color: #B71C1C; color: white'] * len(row)
        return [''] * len(row)
        
    st.dataframe(social_analysis.style.apply(color_social_rows, axis=1), use_container_width=True)

# ==========================================
# MODULE 6: DIGITAL AD SPEND PERFORMANCE
# ==========================================
elif app_panel == "🎯 Digital Ad Spend Performance":
    st.header("🎯 Multi-Channel Paid Acquisition & Budget Tracking Matrix")
    st.subheader("📊 Active Advertising Campaign Performance Tiers")
    
    ad_df = pd.DataFrame({
        "Campaign Strategy Network": ["Google Intent Search (Keywords: Managed IT, M365 Deletions)", "LinkedIn Sponsored Message (Targeting: Law Firm Partners)", "Meta Lookalike Retargeting (Targeting: Local CPAs & Realtors)"],
        "Monthly Capital Deployed": [4500.00, 2500.00, 1500.00],
        "Average Cost Per Click (CPC)": [4.15, 8.50, 2.10],
        "Acquired Qualified Inbound Leads": [34, 12, 8],
        "Customer Acquisition Cost (CAC)": [132.35, 208.33, 187.50],
        "Return On Ad Spend (ROAS)": ["4.8x Return", "3.1x Return", "1.8x Return"],
        "Network Efficiency": ["🟢 Highly Profitable Scaling Tier", "🟡 Stable Pipeline - Keep Baseline", "⚠️ Unprofitable Friction Node"]
    })
    st.dataframe(ad_df, use_container_width=True, hide_index=True)
    
    st.write("---")
    col_ad1, col_ad2 = st.columns([1, 1])
    with col_ad1:
        fig_ad_pie = px.pie(ad_df, values="Monthly Capital Deployed", names="Campaign Strategy Network", hole=0.4,
                            title="Paid Marketing Capital Budget Distribution Splits",
                            color_discrete_sequence=["#00E676", "#00B0FF", "#D500F9"])
        st.plotly_chart(fig_ad_pie, use_container_width=True)
    with col_ad2:
        st.markdown("#### 🎯 Ad Spend Operational Directives:")
        st.info("**1. Scale Google Search Intent:** High efficiency tier generating high-intent keywords tracking local IT helpdesk setups. Target budget expansion to $6,000 next month.")
        st.warning("**2. Audit Meta CPA Ad Units:** Showing severe conversion friction. Low intent matches are wasting clicks. Optimize design creatives or pause CPA targeting entirely.")
