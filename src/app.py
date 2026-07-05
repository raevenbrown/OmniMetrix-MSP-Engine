import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Main Page Canvas Configuration
st.set_page_config(page_title="OmniMetrix OS Suite", layout="wide")

# Initialize persistent session state for helpdesk ticket work simulation
if "ticket_db" not in st.session_state:
    st.session_state.ticket_db = pd.DataFrame({
        "ticket_id": [301, 302, 303, 304, 305, 306, 307],
        "client_name": ["Apex Logistics", "Summit Health Network", "Vanguard Finance", "Apex Logistics", "Horizon Retail", "Summit Health Network", "Vanguard Finance"],
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

# Master client account matrix data frame mapping financials, tiers, and payment status loops
client_matrix_data = pd.DataFrame({
    "client_name": ["Apex Logistics", "Summit Health Network", "Vanguard Finance", "Horizon Retail"],
    "service_tier": ["Silver ($85/mo)", "Platinum ($175/mo)", "Gold ($125/mo)", "Silver ($85/mo)"],
    "seat_count": [50, 40, 35, 25],
    "monthly_recurring_revenue": [4250.00, 7000.00, 4375.00, 2125.00],
    "relationship_length_months": [18, 24, 12, 6],
    "monthly_bill_status": ["Paid", "Paid", "Overdue", "Paid"],
    "out_of_scope_spend": [350.00, 1200.00, 0.00, 150.00]  -- Projects like AI Enablement/Cabling
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
    options=["All Managed Accounts"] + list(st.session_state.ticket_db["client_name"].unique())
)

# Apply Multi-Tenant Isolation Filter across tables
if client_selection == "All Managed Accounts":
    filtered_tickets = st.session_state.ticket_db
    filtered_matrix = client_matrix_data
else:
    filtered_tickets = st.session_state.ticket_db[st.session_state.ticket_db["client_name"] == client_selection]
    filtered_matrix = client_matrix_data[client_matrix_data["client_name"] == client_selection]

st.sidebar.write("---")

# Navigation Panel Option Matrix (Unified Under Operational Navigation)
st.sidebar.subheader("🏁 Operational Navigation")
app_panel = st.sidebar.radio(
    "Select Management Module Panel:",
    [
        "📋 Client Helpdesk Portal", 
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
    
    # Calculate unresolved workload cleanly outside the widget arguments
    open_load = len(filtered_tickets[filtered_tickets["status"] != "Resolved"])
    
    # Live Ticket Counters
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
    
    # Interactive Workstation Hook
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
# MODULE 2: TIER REVENUE & SERVICE ACCOUNTS
# ==========================================
elif app_panel == "💰 Tier Revenue & Service Accounts":
    st.header("💰 Account Profitability Matrix & Tier Telemetry")
    
    # Revenue KPI Layout Blocks
    rc1, rc2, rc3 = st.columns(3)
    with rc1:
        total_mrr = filtered_matrix["monthly_recurring_revenue"].sum()
        st.metric("Aggregated Contract MRR Pipeline", value=f"${total_mrr:,.2f}")
    with rc2:
        total_extra = filtered_matrix["out_of_scope_spend"].sum()
        st.metric("Out-of-Scope Project Billings (Ad-Hoc)", value=f"${total_extra:,.2f}")
    with rc3:
        overdue_invoices = len(filtered_matrix[filtered_matrix["monthly_bill_status"] == "Overdue"])
        st.metric("Delinquent Overdue Client Accounts", value=overdue_invoices, delta="Action Required", delta_color="inverse")
        
    st.write("---")
    st.subheader("🏢 Contract Relationship & Financial Audit Grid")
    st.dataframe(filtered_matrix, use_container_width=True, hide_index=True)
    st.write("---")
    
    # Chart Visualization of package performance metrics
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
# MODULE 3: EMAIL MARKETING ANALYTICS
# ==========================================
elif app_panel == "📧 Email Marketing Analytics":
    st.header("📧 Growth Performance — Corporate Email Journeys")
    
    ec1, ec2, ec3 = st.columns(3)
    with ec1:
        st.metric("Total List Subscribers", value="14,250 Profiles", delta="+380 This Week")
    with ec2:
        st.metric("Average Campaign Open Rate", value="28.4%", delta="+1.2% versus Baseline")
    with ec3:
        st.metric("CTR (Click-Through Conversion Rate)", value="4.1%")
        
    st.write("---")
    st.subheader("📈 Chronological Subscriber List Velocity")
    mock_email_time = pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "Campaign_Opens": [2100, 2400, 2900, 3100, 3800, 4200],
        "Unsubscribes": [45, 30, 55, 22, 12, 19]
    })
    fig_email = px.line(mock_email_time, x="Month", y="Campaign_Opens", title="Executive Newsletter Engagement Inflow Trajectory", markers=True)
    st.plotly_chart(fig_email, use_container_width=True)

# ==========================================
# MODULE 4: SOCIAL MEDIA TRACKING
# ==========================================
elif app_panel == "📱 Social Media Tracking":
    st.header("📱 B2B Audience Optimization & Engagement Matrices")
    
    sc1, sc2, sc3 = st.columns(3)
    with sc1:
        st.metric("Cross-Platform Follower Base", value="45.1K Reach")
    with sc2:
        st.metric("Net Social Engagement Velocity", value="8.7%")
    with sc3:
        st.metric("Total Social Lead Conversions", value="114 Accounts")
        
    st.write("---")
    st.subheader("📊 Network Distribution & Social Impression Shares")
    mock_social_platforms = pd.DataFrame({
        "Channel": ["LinkedIn", "YouTube", "Twitter/X", "Instagram Threads"],
        "Inbound_Leads": [65, 29, 15, 5]
    })
    fig_social = px.bar(mock_social_platforms, x="Channel", y="Inbound_Leads", color="Channel", title="Inbound Qualified B2B Contract Leads per Platform")
    st.plotly_chart(fig_social, use_container_width=True)

# ==========================================
# MODULE 5: DIGITAL AD SPEND PERFORMANCE
# ==========================================
elif app_panel == "🎯 Digital Ad Spend Performance":
    st.header("🎯 Multi-Channel Paid Acquisition & ROAS Dashboard")
    
    ac1, ac2, ac3 = st.columns(3)
    with ac1:
        st.metric("Total Monthly Ad Budget Capital Deployed", value="$8,500.00")
    with ac2:
        st.metric("Average CPC (Cost Per Acquisition Click)", value="$3.42")
    with ac3:
        st.metric("ROAS (Return on Advertising Capital Invested)", value="4.2x")
        
    st.write("---")
    st.subheader("🍩 Paid Visual Asset Performance Breakdown")
    mock_ad_spend = pd.DataFrame({
        "Ad_Network": ["Google Intent Search", "LinkedIn Dynamic Ads", "Meta B2B Lookalikes"],
        "Budget_Allocation": [4500, 2500, 1500]
    })
    fig_ads = px.pie(mock_ad_spend, values="Budget_Allocation", names="Ad_Network", hole=0.5, color_discrete_sequence=["#00E676", "#00B0FF", "#D500F9"])
    st.plotly_chart(fig_ads, use_container_width=True)
