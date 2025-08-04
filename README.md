# Project Overview
## Project Name: LogForge: Threat Monitoring with ELK Stack
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
Docker:	Containerization of the entire ELK stack
Docker Compose:	Orchestration of multi-container deployment
Elasticsearch 8.6.0:	Backend search and indexing engine
Logstash 8.6.0:	Ingests and transforms logs with Grok filters
Kibana 8.6.0:	UI for search, visualization, dashboards, alerts
Filebeat (optional):	Lightweight log forwarder for log files
YAML:	Used for mapping logs to MITRE ATT&CK techniques
