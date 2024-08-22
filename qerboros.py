import streamlit as st

st.set_page_config(page_title="Qerboros", page_icon=":shark:", layout="wide")

def analyze_logs(logs):
    # The code (model) to determine if the logs are malicious or benign goes here
    # Return the result (malicious or benign) based on the model output

    return "Benign"  # Replace this with your actual result

def dashboard():
    st.title("Dashboard")
    st.write("Hackers often install malicious services to maintain persistence on a compromised system.")
    st.write("A malicious service can be used to escalate privileges on the system. If the service is configured to run with higher privileges, the attacker could gain greater control over the system.")
    st.write("This tool helps you analyze Windows event logs to identify malicious services that may have been installed on the system.")
    st.write("Early detection helps in identifying sophisticated attacks that might evade other forms of detection.")
    st.write("Use the 'Log Analyzer' page to enter your Windows event logs and analyze them for malicious activity.")

def main():
    st.title("Windows Event Log Analyzer")
    st.write("Enter your Windows event logs below:")
    logs = st.text_area("Logs", "Enter your logs here")

    if st.button("Analyze"):
        result = analyze_logs(logs)
        st.write("Result:", result)

def references_page():
    st.title("References")
    st.link_button("Windows Event Log Reference", "https://docs.microsoft.com/en-us/windows/win32/eventlog/event-log-reference")
    st.link_button("Windows Logs in Incident Response", "https://www.sans.org/blog/windows-logs-in-incident-response/")
    st.link_button("Detecting Persistence Mechanisms in Windows", "https://www.fireeye.com/blog/threat-research/2018/07/detecting-persistence-mechanisms-on-windows.html")
    st.link_button("Windows Event Log Analysis", "https://www.varonis.com/blog/windows-event-log-analysis/")
    st.link_button("Rising Cyber Threats", "https://www.imf.org/en/Blogs/Articles/2024/04/09/rising-cyber-threats-pose-serious-concerns-for-financial-stability")

pages = {
    "Dashboard": dashboard,
    "Log Analyzer": main,
    "References": references_page
}

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(pages.keys()))

# Call the selected page function
pages[selection]()


