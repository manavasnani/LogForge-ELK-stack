# Overview
## LogForge: Threat Monitoring with ELK Stack
LogForge is a lightweight, Docker-based environment for simulating and analyzing cyber threats using the ELK stack (Elasticsearch, Logstash, and Kibana). The project is designed to help with understanding, monitoring, and visualizing log-based threats using MITRE ATT&CK mappings and provides a visual SIEM-like experience.

## Purpose
The goal of this project is to:
- Simulate threat activity and ingest logs (e.g., from Filebeat or simulated sources).
- Parse and enrich logs using Logstash with custom filters.
- Index and store data efficiently in Elasticsearch for querying and correlation.
- Visualize logs and alerts in Kibana dashboards, including MITRE-mapped threat tags.
- Explore security event analysis, dashboarding, and alerting from a blue team perspective.
- This project offers a beginner-to-intermediate level introduction to using the ELK stack for threat detection and log analytics.

## Core Technologies Used
- Docker:	Containerization of the entire ELK stack
- Docker Compose:	Orchestration of multi-container deployment
- Elasticsearch 8.6.0:	Backend search and indexing engine
- Logstash 8.6.0:	Ingests and transforms logs with Grok filters
- Kibana 8.6.0:	UI for search, visualization, dashboards, alerts
- Filebeat (optional):	Lightweight log forwarder for log files
- YAML:	Used for mapping logs to MITRE ATT&CK techniques

# System Architecture
## Data Flow Overview
This project follows a modular pipeline architecture to simulate log ingestion, enrichment, indexing, and visualization using the ELK Stack. The flow is designed to mimic real-world SIEM data processing pipelines.
1. Log Generation
Custom scripts or security event simulators generate sample log data (e.g., SSH access logs, failed logins, command execution, malware artifacts). These logs can be written to a file continuously or dumped in batch.
2. Filebeat
Filebeat acts as the lightweight log shipper agent. It monitors specific log files and forwards them to Logstash in real time. It’s configured using a filebeat.yml file which specifies input paths and output settings.
3. Logstash
Logstash ingests the incoming logs and processes them using defined grok patterns and filters (configured in logstash.conf).
It performs:
   - Field extraction (timestamp, IP, command)
   - Enrichment (e.g., adding MITRE technique tags)
   - Normalization (parsing raw log formats into structured JSON)
4. Elasticsearch
Logstash then forwards the structured data to Elasticsearch, which stores and indexes it for fast querying and correlation. The logs are stored in indices like logstash-*.
5. Kibana
Finally, Kibana connects to Elasticsearch and offers a GUI to search logs, build dashboards, and set up alerts or visualizations. Security dashboards and MITRE-tagged events can be explored here.

## Directory Structure
.<br>
├── config/<br>
      └── mitre_mapping.yaml<br>
├── Logs/<br>
      └── Cloud<br>
      └── Linux<br>
      └── Windows<br>
├── attacks/<br>
      └── cloud_iam_misuse.py<br>
      └── linux_brute_force.py<br>
      └── powershell_exec.py<br>
      └── port_scan.py<br>
      └── ssh_failures.py<br>
├── elk/<br>
      └── docker-compose.yml<br>
      └── logstash.conf<br>
├── utils/<br>
      └── formatter.py<br>
      └── writer.py<br>
└── main.py<br>
└── README.md<br>

# Setup 
## Prerequisites
- Docker
- Docker Compose
- Python 3.x
- Open Ports
   - 5044 (Logstash input)
   - 9200 (Elasticsearch)
   - 5601 (Kibana UI)
 
## Docker-Compose Setup
Clone this repository and run "docker-compose up -d --build" in the repo directory. Once the containers are up and running, access kibana at http://localhost:5601 and verify if everything is running properly. 

# Logstash & Filebeat Configuration
After the initial installation, I focused on setting up the Logstash & Filebeat pipeline to correctly ingest & forward simulated log data generated from various attack scenarios. My goal was to ensure that each type of attack log could be parsed accurately, tagged appropriately, and enriched with MITRE ATT&CK mappings before being forwarded to Elasticsearch.

## Filtering & Tagging Each Attack Type
To handle different types of attack logs, I created conditional filters in the logstash.conf file. Each filter block parses logs specific to one type of attack and adds a unique attack_type tag for identification.
Here’s how I approached each:
- PowerShell Execution
   - I parsed Windows Event logs for command-line activities using grok filters.
   - Fields like CommandLine, User, and ProcessName were extracted.

- SSH Brute Force
   - For SSH logs, I extracted fields such as the source IP and username from the auth logs.
   - Failed login attempts were detected and tagged with attack_type => ssh_bruteforce.

- Linux Brute Force
   - Similar to SSH, I created filters for Linux logs from /var/log/auth.log.
   - The filters identified repeated login attempts and added the attack_type => linux_bruteforce.

- Port Scanning
   - I simulated logs from Nmap and created filters to extract scanned port numbers and IPs.
   - These were tagged with attack_type => port_scanning.

- Cloud IAM Misuse
   - I simulated cloud IAM misuse events (e.g., unauthorized actions in AWS) and extracted fields like user, service, and action.
   - I tagged these events with attack_type => cloud_iam_misuse.

Each type of log had its own conditional block in the logstash.conf file to ensure accurate parsing and tagging.

## Adding Tags & MITRE Fields
To enhance the logs with contextual threat intelligence, I made sure each log entry had MITRE ATT&CK data. I used the Python script (main.py) to read a YAML file (mitre_mapping.yaml) and inject the following fields:
- fields.attack_type
- fields.mitre_technique
These values were dynamically added before logs reached Logstash. I confirmed that new logs reflected these fields in Kibana, even though old logs showed them as empty (as expected).

## Filebeat Setup
I installed Filebeat on the same host where my attack simulations were being logged.
In the Filebeat configuration file (filebeat.yml), I defined multiple input paths to collect logs such as:

- Auth logs (/var/log/auth.log)
- Syslogs
- Simulated cloud activity logs

I configured the output to forward all logs to Logstash rather than directly to Elasticsearch to allow for additional enrichment and parsing.

Once logstash and filebeat were configured, and all of the docker containers were up and running, my Kibana looked like this. 

<img width="313" height="292" alt="Screenshot 2025-08-04 180954" src="https://github.com/user-attachments/assets/14cfcdf5-eec6-4611-b85d-6bfae9d2fc5b" />

<img width="1552" height="629" alt="Screenshot 2025-08-04 180841" src="https://github.com/user-attachments/assets/9ef9d4ed-7eb5-4a81-9396-18cbfeed223a" />

# Kibana Configuration & Visualizations
Once log ingestion was functional via Filebeat → Logstash → Elasticsearch, I moved on to setting up Kibana to analyze and visualize the attack patterns in real-time.

1. MITRE Technique by Count (Bar Chart)
This horizontal bar chart represents the top 5 most frequently triggered MITRE ATT&CK techniques in the dataset.
   - Data Source: fields.mitre_technique.keyword
   - Visualization Type: Bar chart (count aggregation)
   - Purpose: Helps identify the most common adversary behaviors (e.g., lateral movement, command execution, credential dumping).

2. Attack Frequency by Type (Donut Chart)
This donut chart visualizes the distribution of attack types detected in the logs.
   - Data Source: attack_type.keyword
   - Visualization Type: Donut chart (terms aggregation)
   - Purpose: Highlights the proportion of different attack behaviors across the dataset.

<img width="1917" height="776" alt="Screenshot 2025-08-04 180910" src="https://github.com/user-attachments/assets/f551546f-a309-41e2-99ef-1111b8f66881" />

# Future Enhancements
## Alerts & Monitoring 
One of the key goals for this project was to set up real-time alerting mechanisms within Kibana using Elastic Stack’s native capabilities (e.g., rule-based detection, action connectors, email/webhook integrations). However, this functionality has been postponed due to unresolved issues related to security configuration and encryption keys within Kibana.

## Planned Next Steps:
- Define the required encryption keys manually in kibana.yml
- Implement proper user authentication and RBAC (Role-Based Access Control) to access the Security section and configure alert rules
- Set up alert conditions based on:
   - Thresholds for specific MITRE techniques
   - Detection of repeated port scans or brute-force attempts
   - Unusual spikes in specific log types
- Use connectors like:
   - Email notifications (via SMTP)
   - Webhooks to external systems like Slack, Discord, or SIEMs
Once the Kibana security issues are resolved, this will significantly enhance the automation and response capabilities of the LogForge stack.
