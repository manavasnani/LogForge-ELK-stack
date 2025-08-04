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
2. Filebeat (Optional)
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


