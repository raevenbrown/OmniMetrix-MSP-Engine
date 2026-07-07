import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration Setup
st.set_page_config(page_title="OmniMetrix Enterprise OS v2", layout="wide")

# ==========================================
# CENTRALIZED DATA ARCHITECTURE (WHITELABELED)
# ==========================================

# 1. Advanced Helpdesk Ticketing Data
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

# 2. Live RMM Hardware Asset Inventory (Upgraded with Computer Model Specifics)
if "rmm_db" not in st.session_state:
    st.session_state.rmm_db = pd.DataFrame({
        "asset_id": ["WS-01", "LAP-02", "TAB-03", "LAP-04", "SRV-05", "LAP-06", "SW-07"],
        "client_name": ["Alpha Logistics", "Beta Healthcare Network", "Gamma Financial", "Delta E-Commerce", "Alpha Logistics", "Beta Healthcare Network", "Gamma Financial"],
        "device_name": ["ALPHA-DESK01", "BETA-MACBOOK", "GAMMA-IPAD-03", "DELTA-DELL-XPS", "ALPHA-PROXY-SRV", "BETA-APPLE-IMAC", "GAMMA-CORE-SW"],
        "hardware_type": ["Windows Desktop (Dell Inspiron)", "Apple Laptop (MacBook Pro)", "Apple Tablet (iPad Pro)", "Windows Laptop (Dell XPS 15)", "Linux Server (Ubuntu Node)", "Apple Desktop (iMac M3)", "Network Switch (Cisco Core)"],
        "serial_number": ["SN-78421-A", "SN-99210-B", "SN-11452-C", "SN-88421-D", "SN-55621-E", "SN-22104-F", "SN-33491-G"],
        "ram_gb": [16, 32, 8, 16, 128, 24, 4],
        "remote_screen_access": ["Available - View Live", "Available - View Live", "Offline", "Available - View Live", "Available - View Live", "Available - View Live", "Console Only"],
        "patch_status": ["Needs Reboot", "Needs Review", "Installed", "Needs Review", "Installed", "Installed", "Needs Reboot"],
        "patch_age_days": [25, 48, 0, 48, 0, 0, 50],
        "email_alert_threshold": ["Alert Sent (Age > 14d)", "Pending Engineer Notification", "Compliant", "Pending Engineer Notification", "Compliant", "Compliant", "Alert Sent (Age > 14d)"],
        "active_rmm_alert": ["None", "Cpu Monitoring: Usage over 90%", "App Crash Trigger: ID 1042", "Low Hd Space: Drive C under 10%", "None", "None", "None"]
    })

# 3. Master Client Business Profiles (Upgraded with Source Attribution & Exit Tracking)
client_matrix_data = pd.DataFrame({
    "client_name": ["Alpha Logistics", "Beta Healthcare Network", "Gamma Financial", "Delta E-Commerce"],
    "acquisition_source": ["B2B Local Event", "Executive Referral", "Digital Ads Campaign", "Social Media Content"],
    "service_tier": ["Silver Tier", "Platinum Tier", "Gold Tier", "Silver Tier"],
    "seat_count": [50, 40, 35, 25],
    "monthly_recurring_revenue": [4250.00, 7000.00, 4375.00, 2125.00],
    "contract_length_term": ["1-Year Commitment", "2-Year Commitment", "6-Month Short Term", "Month-to-Month Retainer"],
    "relationship_age_months": [18, 24, 12, 6],
    "monthly_bill_status": ["Paid", "Paid", "Overdue", "Paid"],
    "out_of_scope_spend": [350.00, 1200.00, 0.00, 150.00],
    "exit_risk_status": ["Safe", "Safe", "🔴 CRITICAL: Exiting Next Month", "Reviewing Renewal"]
})

# 4. Sales Pipeline Pipeline Deals (Upgraded with Bottleneck Stalls Explanations)
pipeline_data = pd.DataFrame({
    "Prospect Name": ["Zeta Manufacturing", "Sigma Consulting Group", "Omega Capital LLC", "Tau Wellness Inc"],
    "Deal Class Pipeline": ["Pipeline Target (To Win)", "Pipeline Target (To Win)", "Pending High Close", "Pending High Close"],
    "Lead Acquisition Source": ["Executive Referral", "B2B Local Event", "Social Media Content", "Digital Ads Campaign"],
    "Target Pricing Tier": ["Platinum Tier ($175/mo)", "Gold Tier ($125/mo)", "Platinum Tier ($175/mo)", "Silver Tier ($85/mo)"],
    "Projected Seats": [120, 45, 85, 30],
    "Estimated Value": [21000.00, 5625.00, 14875.00, 2550.00],
    "Confidence Score": ["35%", "50%", "85%", "90%"],
    "Deal Closing Bottleneck / Hold-up Reason": [
        "Awaiting target company signature from overseas parent holding company board.",
        "Prospect currently auditing internal budgeting variables; final check scheduled next week.",
        "🔴 HOLD-UP: Legal counsel processing customized data liability addendum parameters.",
        "🔴 HOLD-UP: Executive decision maker out of office on medical leave until Monday."
    ]
})

# ==========================================
# SIDEBAR NAVIGATION CONSOLE
# ==========================================
st.sidebar.title("💎 OmniMetrix Command Suite")
st.sidebar.markdown("**Active Engineer:** `Raeven Brown` ")
st.sidebar.markdown("**System Class:** `MSP Management Portal`")
st.sidebar.write("---")

client_selection = st.sidebar.selectbox(
    "Active Tenant Scope:",
    options=["All Managed Accounts"] + list(client_matrix_data["client_name"].unique())
)

if client_selection == "All Managed Accounts":
    filtered_tickets = st.session_state.ticket_db
    filtered_rmm = st.session_state.rmm_db
    filtered_matrix = client_matrix_data
else:
    filtered_tickets = st.session_state.ticket_db[st.session_state.ticket_db["client_name"] == client_selection]
    filtered_rmm = st.session_state.rmm_db[st.session_state.rmm_db["client_name"] == client_selection]
    filtered_matrix = client_matrix_data[client_matrix_data["client_name"] == client_selection]

st.sidebar.write("---")
st.sidebar.subheader("🏁 Operational Navigation")
app_panel = st.sidebar.radio(
    "Select Management Module Panel:",
    ["📋 Client Helpdesk Portal", "⚙️ RMM Alerts & Asset Telemetry", "💰 Tier Revenue & Financial Targets", "📧 Email Marketing Analytics", "📱 Social Media Performance", "🎯 Digital Ad Spend Performance"]
)

# ==========================================
# MODULE 1: CLIENT HELPDESK PORTAL
# ==========================================
if app_panel == "📋 Client Helpdesk Portal":
    st.header("📋 Daily Inbound Operations & Ticket Workbench")
    view_selection = st.radio("Filter Workbench Scope Matrix:", ["All Tickets", "All Unresolved", "Assigned to Me (Raeven Brown)", "My Queue (In Progress)", "Resolved Tickets", "Subscribed Accounts", "Unassigned Tickets"], horizontal=True)
    
    if view_selection == "All Unresolved": processed_tickets = filtered_tickets[filtered_tickets["status"] != "Resolved"]
    elif view_selection == "Assigned to Me (Raeven Brown)": processed_tickets = filtered_tickets[filtered_tickets["assigned_tech"] == "Raeven Brown"]
    elif view_selection == "My Queue (In Progress)": processed_tickets = filtered_tickets[(filtered_tickets["assigned_tech"] == "Raeven Brown") & (filtered_tickets["status"] == "In Progress")]
    elif view_selection == "Resolved Tickets": processed_tickets = filtered_tickets[filtered_tickets["status"] == "Resolved"]
    elif view_selection == "Subscribed Accounts": processed_tickets = filtered_tickets[filtered_tickets["priority"].isin(["High", "Critical"])]
    elif view_selection == "Unassigned Tickets": processed_tickets = filtered_tickets[filtered_tickets["status"] == "Unassigned"]
    else: processed_tickets = filtered_tickets

    tc1, tc2, tc3 = st.columns(3)
    with tc1: st.metric("Active Queue Ticket Volume", value=len(processed_tickets))
    with tc2: st.metric("Unassigned Tasks Pending Routing", value=len(filtered_tickets[filtered_tickets["status"] == "Unassigned"]))
    with tc3: st.metric("Total System Engineering Logs", value=f"{filtered_tickets['time_logged_minutes'].sum()} Mins")
        
    st.write("")
    st.dataframe(processed_tickets, use_container_width=True, hide_index=True)

# ==========================================
# MODULE 2: RMM ALERTS & ASSET TELEMETRY
# ==========================================
elif app_panel == "⚙️ RMM Alerts & Asset Telemetry":
    st.header("⚙️ Remote Monitoring & Automated Patch Infrastructure")
    
    st.subheader("🖥️ Hardware Endpoint Management (Apple, Windows & Network Hardware Inventory)")
    def color_patch_rows(row):
        if row["patch_status"] == "Needs Reboot": return ['background-color: #3E2723; color: #FFCC80'] * len(row)
        elif row["patch_status"] == "Needs Review": return ['background-color: #4A3B00; color: #FFE082'] * len(row)
        return [''] * len(row)
    st.dataframe(filtered_rmm.style.apply(color_patch_rows, axis=1), use_container_width=True, hide_index=True)
    st.write("---")
    
    st.subheader("📡 Live Remote Session & Patch Alert Desks")
    remote_target = st.selectbox("Choose Hardware Node to Mount Management Tunnel:", options=filtered_rmm["device_name"])
    r_row = filtered_rmm[filtered_rmm["device_name"] == remote_target].iloc[0]
    r_idx = st.session_state.rmm_db[st.session_state.rmm_db["device_name"] == remote_target].index[0]
    
    with st.container(border=True):
        m_c1, m_c2 = st.columns(2)
        with m_c1:
            st.markdown(f"### 🖥️ Asset Profile: `{r_row['device_name']}`")
            st.markdown(f"* **🖥️ Computer Model Classification:** `{r_row['hardware_type']}`")
            st.markdown(f"* **🔑 Serial Number String:** `{r_row['serial_number']}` | **💾 System Memory:** `{r_row['ram_gb']} GB RAM`")
            st.markdown(f"* **🛡️ Patch Status Age:** `{r_row['patch_status']} ({r_row['patch_age_days']} Days Stalled)`")
        with m_c2:
            st.markdown(f"#### 🔒 Active Alert Tracking State: `{r_row['email_alert_threshold']}`")
            
            # Interactive patch alert email mitigation workspace
            if r_row["patch_status"] == "Needs Review":
                st.warning("⚠️ This hardware node requires immediate policy optimization review.")
                if st.button(f"📧 Instantly Dispatch Critical Patch Warning Email to Client Management", use_container_width=True):
                    st.session_state.rmm_db.at[r_idx, "email_alert_threshold"] = "Alert Sent (Triggered by Engineer)"
                    st.success(f"Security Alert Email successfully fired! Dispatched copy sequence matching: {r_row['device_name']} configuration rules.")
                    st.rerun()
            elif "Alert Sent" in r_row["email_alert_threshold"]:
                st.info("🟢 Patch Alert Warning Email has already been locked and pushed out to the company administration.")
            else:
                st.success("🏆 Asset is currently compliant with centralized security blueprints.")

# ==========================================
# MODULE 3: TIER REVENUE & FINANCIAL TARGETS
# ==========================================
elif app_panel == "💰 Tier Revenue & Financial Targets":
    st.header("💰 Account Profitability Matrix & Contract Commitment Terminals")
    
    g1, g2, g3 = st.columns(3)
    with g1: st.metric("Monthly Revenue Goal ($15K Baseline)", value=f"${filtered_matrix['monthly_recurring_revenue'].sum():,.2f}", delta="+ $2,750 Above Track")
    with g2: st.metric("Quarterly Growth Metric ($50K)", value="$53,550.00")
    with g3: st.metric("Yearly Recurring Target ($200K)", value="$214,200.00 Run-Rate")
    
    st.write("---")
    st.subheader("🏢 Active Portfolio Audit & Lead Origin Tracking")
    st.dataframe(filtered_matrix, use_container_width=True, hide_index=True)
    st.write("---")
    
    st.subheader("📈 Forward Revenue Acquisition Pipelines")
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        st.markdown("#### 🎯 Pipeline Targets (To Win Across Fields)")
        st.dataframe(pipeline_data[pipeline_data["Deal Class Pipeline"] == "Pipeline Target (To Win)"], use_container_width=True, hide_index=True)
    with col_p2:
        st.markdown("#### 🔥 Pending High-Confidence Closes (Stall Diagnostics)")
        st.dataframe(pipeline_data[pipeline_data["Deal Class Pipeline"] == "Pending High Close"], use_container_width=True, hide_index=True)

# ==========================================
# MODULE 4: EMAIL MARKETING ANALYTICS
# ==========================================
elif app_panel == "📧 Email Marketing Analytics":
    st.header("📧 Advanced Specialized Funnel Drop-off & Conversion Matrix")
    
    # 1. Total Sent Volume Metrics per Segment
    st.subheader("📦 Dispatched Campaign Volumes & Close Conversions by Target Segment")
    
    email_master_df = pd.DataFrame({
        "Campaign Funnel Segment": ["1. Existing Retained Customers Base", "2. Patching Alert Overdue Notifications", "3. Sourced Inbound Prospects (Social Media)", "4. Cold/Warm Leads (Local B2B Events)"],
        "Total Dispatched Volume": [420, 850, 2400, 350],
        "Emails Successfully Delivered": [418, 842, 2380, 348],
        "Opened Actions Record": [310, 610, 1150, 190],
        "Link Clicks Logged": [184, 412, 680, 88],
        "Upgraded / Closed Conversions": [14, 56, 28, 12],
        "Contract Upgrades / Revenue Generation ($)": [2450.00, 7840.00, 4900.00, 2100.00]
    })
    st.dataframe(email_master_df, use_container_width=True, hide_index=True)
    
    st.write("---")
    
    # 2. Interactive Section: Subject Lines, Blueprint Layout Copy, and Funnel Leak Maps
    st.subheader("🔍 Granular Copy Inspection & Funnel Leak Mapping Tool")
    inspect_segment = st.selectbox("Select Target Segment to Inspect:", options=email_master_df["Campaign Funnel Segment"])
    
    with st.container(border=True):
        if "Existing" in inspect_segment:
            st.markdown("#### 📧 Email Structure Copy Profile: **Retained Base**")
            st.markdown("**Subject:** `Exclusive Add-On: Elevate your network protection to complete SOC 2 Framework Readiness`")
            st.caption("**Layout Preview:** Hello Team, as an active client, you are running stable infrastructure layers. However, modern corporate standards demand rigorous auditing trails. Here is a preview of our zero-trust access keys...")
            st.markdown("**📉 Forensic Drop-off Leak Map:** `Open-to-Click Transition` | **Drop-off Rate:** `40.6% Lost` | *Diagnostic:* High opens but weak click-through. *Correction:* Call-to-action button is buried too far down the message copy layer.")
        elif "Patching" in inspect_segment:
            st.markdown("#### 📧 Email Structure Copy Profile: **Patching Alerts**")
            st.markdown("**Subject:** `URGENT SECURITY WARNING: Unpatched server assets vulnerability expiration alert`")
            st.caption("**Layout Preview:** Alert, our automated remote RMM sensors have isolated unpatched endpoints matching security flaws inside your workspace. If unmitigated, these ports remain exposed to active malware injection strings...")
            st.markdown("**📉 Forensic Drop-off Leak Map:** `Delivered-to-Open Transition` | **Drop-off Rate:** `27.5% Lost` | *Diagnostic:* High conversion efficiency. *Correction:* Subject formatting is highly effective; copy model should be cloned.")
        elif "Social" in inspect_segment:
            st.markdown("#### 📧 Email Structure Copy Profile: **Social Prospects**")
            st.markdown("**Subject:** `Download Blueprint: The step-by-step Microsoft 365 identity protection manual`")
            st.caption("**Layout Preview:** Hi there, thanks for checking out our video on M365 user account terminations. As promised, here is your structural PDF guide detailing exactly how to clean up stale license pools and group allocations...")
            st.markdown("**📉 Forensic Drop-off Leak Map:** `Delivered-to-Open Transition` | **Drop-off Rate:** `51.6% CRITICAL LEAK` | *Diagnostic:* Severe interest loss at inbox arrival. *Correction:* Subject line text reads too robotic or generic. Rewrite to introduce immediate tactical pain-point hooks.")
        else:
            st.markdown("#### 📧 Email Structure Copy Profile: **B2B Local Events**")
            st.markdown("**Subject:** `Following up from the Regional Business Expo: Your complimentary infrastructure risk map`")
            st.caption("**Layout Preview:** It was great connecting at our local exhibition booth! We discussed how hidden system failures can slow down billing cycles. As a follow-up, our engineering crew has initialized a custom network health review...")
            st.markdown("**📉 Forensic Drop-off Leak Map:** `Click-to-Conversion Transition` | **Drop-off Rate:** `86.3% Lost` | *Diagnostic:* Clicks are high but final discovery signatures failed. *Correction:* The landing page appointment scheduling link contains too many entry form fields.")

# ==========================================
# MODULE 5: SOCIAL MEDIA PERFORMANCE
# ==========================================
elif app_panel == "📱 Social Media Performance":
    st.header("📱 Granular Five-Channel B2B Performance Tracker & Growth Curves")
    
    # 1. Historical Growth Comparison Line Chart
    growth_data = pd.DataFrame({
        "Quarter Frame": ["2025-Q1", "2025-Q2", "2025-Q3", "2025-Q4", "2026-Q1", "2026-Q2"],
        "LinkedIn Metrics": [1200, 2400, 3800, 5100, 6800, 8450],
        "YouTube Metrics": [1500, 3100, 5400, 7800, 9900, 12100],
        "TikTok Metrics": [500, 1200, 2900, 4300, 6100, 7900],
        "Instagram Metrics": [800, 1100, 1500, 1900, 2300, 2750],
        "Threads Metrics": [100, 300, 700, 1100, 1600, 2100]
    })
    fig_social_line = px.line(growth_data, x="Quarter Frame", y=["LinkedIn Metrics", "YouTube Metrics", "TikTok Metrics", "Instagram Metrics", "Threads Metrics"], markers=True, title="Chronological Audience Follower Growth Curves Across Platforms")
    st.plotly_chart(fig_social_line, use_container_width=True)
    
    st.write("---")
    st.subheader("📊 Native Performance Matrices Split by Isolated Platform Channel")
    
    # 2. Granular Tables per Channel
    tab_li, tab_yt, tab_tt, tab_ig, tab_th = st.tabs(["🔒 LinkedIn Logs", "📺 YouTube Logs", "🎵 TikTok Logs", "📸 Instagram Logs", "🧵 Threads Logs"])
    
    with tab_li:
        st.markdown("#### 🔒 LinkedIn Corporate Strategy Performance Feed")
        li_data = pd.DataFrame({
            "Post Topic Blueprint": ["M365 User Offboarding Video", "Ransomware Compliance Story", "Generic Image Graphics"],
            "Followers Sourced": [140, 45, 2], "Impressions": [12400, 3200, 210], "Likes": [412, 92, 14], "Shares": [89, 11, 1], "Clicks": [214, 45, 0],
            "Growth Catalyst Factor": ["🔥 Primary Scale Driver", "🟡 Average Brand Asset", "❌ Drag Node: Zero Value"]
        })
        st.dataframe(li_data, use_container_width=True, hide_index=True)
        st.caption("**LinkedIn Strategic Move:** Long-form carousel text breakdowns and walkthrough videos drive maximum corporate authority.")
        
    with tab_yt:
        st.markdown("#### 📺 YouTube Long-Form Technical Tutorial Log")
        yt_data = pd.DataFrame({
            "Video Topic Blueprint": ["SharePoint Permissions Guide", "M365 Admin Masterclass", "Shorts Channel Promos"],
            "Subscribers Gained": [865, 310, 2], "Video Views": [28500, 14100, 850], "Likes": [1840, 612, 12], "Comments Logged": [142, 56, 1], "Clicks": [945, 412, 8],
            "Growth Catalyst Factor": ["🔥 Primary Authority Engine", "🔥 High Intent Pipeline Asset", "❌ Drag Node: Unprofitable Reach"]
        })
        st.dataframe(yt_data, use_container_width=True, hide_index=True)
        st.caption("**YouTube Strategic Move:** High search-intent keywords drive evergreen inbound discovery leads effortlessly over multi-month lifecycles.")
        
    with tab_tt:
        st.markdown("#### 🎵 TikTok Creative Scripting & Short Hooks Monitor")
        tt_data = pd.DataFrame({
            "Short-Form Asset Subject": ["Day in the Life of a Cyber Engineer", "POV: Someone forgets their MFA token", "Trends Sound meme loop"],
            "Followers Gained": [280, 115, 42], "Views Count": [45000, 18200, 9500], "Likes": [3200, 940, 110], "Shares": [640, 88, 5], "Link Clicks": [112, 14, 0],
            "Growth Catalyst Factor": ["🔥 Viral Reach Engine", "🟡 Strong Engagement Asset", "❌ Drag Node: Zero Conversion Value"]
        })
        st.dataframe(tt_data, use_container_width=True, hide_index=True)
        
    with tab_ig:
        st.markdown("#### 📸 Instagram Visual Branding & Grid Asset Metrics")
        ig_data = pd.DataFrame({
            "Visual Asset Context": ["Client Server Room Cleanup (Before/After)", "Team Achievement Celebration Showcase", "Tech Quote Graphics Card"],
            "Followers Gained": [18, 22, 0], "Impressions": [1800, 2400, 140], "Likes": [114, 210, 8], "Comments": [12, 19, 0], "Link Clicks": [24, 8, 0],
            "Growth Catalyst Factor": ["🟡 Local Relationship Builder", "🟡 Strong Culture Showcase", "❌ Drag Node: Dead Reach Asset"]
        })
        st.dataframe(ig_data, use_container_width=True, hide_index=True)
        
    with tab_th:
        st.markdown("#### 🧵 Threads Conversational Networking Stream")
        th_data = pd.DataFrame({
            "Thread Narrative Conversation": ["Hot Take: Cloud migrations are overhyped for local SMBs", "Question: What is your biggest M365 migration failure?", "Link Share: Automated patch deployment logs"],
            "Followers Sourced": [34, 19, 1], "Impressions": [2900, 1400, 110], "Likes": [88, 41, 2], "Re-Threads": [14, 6, 0], "Link Clicks": [56, 12, 1],
            "Growth Catalyst Factor": ["🔥 High Conversational Engagement", "🟡 Strong Community Asset", "❌ Drag Node: Drop Link Fail Node"]
        })
        st.dataframe(th_data, use_container_width=True, hide_index=True)

    st.write("---")
    
    # 3. Competitor Intelligence
    st.subheader("🕵️ Competitor Benchmark Intelligence Grid")
    comp_df = pd.DataFrame({
        "Anonymized Competitor Profile": ["Competitor Alpha (Local Brand)", "Competitor Beta (Regional SaaS)", "Competitor Gamma (National Enterprise)"],
        "Observed Strategy Strengths": ["Heavy localized presence at chamber of commerce networks.", "Publishing weekly text blog materials on entry-level IT trends.", "Heavy capital investment in enterprise search engine keywords paid ads."],
        "Identified Content Weaknesses": ["Completely missing online technical video logs or video walkthrough assets.", "Low user-interaction metrics; boring updates that feel cold.", "Generic, highly disconnected copy style that doesn't target pain points."],
        "OmniMetrix Strategic Exploitation Blueprint": [
            "Produce clear technical walkthrough video assets on LinkedIn and YouTube to capture local authority.",
            "Deploy highly actionable short-form interactive guides to pull away their search volume base.",
            "Leverage personalized B2B workflows and high-density script tools to dominate conversion cycles."
        ]
    })
    st.dataframe(comp_df, use_container_width=True, hide_index=True)

# ==========================================
# MODULE 6: DIGITAL AD SPEND PERFORMANCE
# ==========================================
elif app_panel == "🎯 Digital Ad Spend Performance":
    st.header("🎯 Multi-Channel Paid Acquisition & Historical Forensic Dashboard")
    
    st.subheader("📊 Q1 vs Q2 Campaign Strategy Forensic Audit (Side-by-Side Evaluation)")
    st.markdown("##### *Forensic mapping isolating asset performance, expenditure efficiency metrics, and root-cause analytical breakdowns.*")
    
    ad_forensic_df = pd.DataFrame({
        "Quarter Timeline": ["Q1 2026", "Q1 2026", "Q2 2026", "Q2 2026"],
        "Campaign Strategy Network": ["Google Intent Search (Keywords: IT Helpdesk, M365 Setup)", "Meta Lookalikes (Quote Cards Assets)", "LinkedIn Message Ads (Targeting: Corporate Law Partners)", "Google Intent Search (Keywords: M365 Account Deletion)"],
        "Deployed Budget": [4500.00, 1500.00, 2500.00, 6000.00],
        "Acquired Leads": [34, 2, 12, 58],
        "ROAS Ratios": ["3.8x Return", "0.4x Loss", "3.1x Return", "5.2x Return"],
        "Operational Outcome State": ["=== SUCCESSFUL SCALING VECTOR ===", "=== CRITICAL FAIL NODE ===", "=== SUCCESSFUL SCALING VECTOR ===", "=== MAXIMUM MARGIN CATALYST ==="],
        "Analytical Root-Cause Rationale (Why)": [
            "Inbound search intent perfectly maps transactional client requirements; buyers have budget locked.",
            "B2B managers and executive decision makers do not engage with social media quote visual cards when sourcing a security engine.",
            "Direct personalization tokens hitting corporate leadership inboxes bypass traditional gatekeepers cleanly.",
            "Targeting ultra-granular client bottleneck friction points (e.g., 'M365 offboarding legal risk') converts instantly."
        ]
    })
    
    def color_ad_rows(row):
        if "SUCCESSFUL" in row["Operational Outcome State"] or "MAXIMUM" in row["Operational Outcome State"]:
            return ['background-color: #1B5E20; color: white'] * len(row)
        elif "FAIL" in row["Operational Outcome State"]:
            return ['background-color: #B71C1C; color: white'] * len(row)
        return [''] * len(row)
        
    st.dataframe(ad_forensic_df.style.apply(color_ad_rows, axis=1), use_container_width=True, hide_index=True)
