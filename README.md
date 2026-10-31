 APT Campaign & Multi-Stage RAT Analysis

 Project Overview

This project is an educational cybersecurity study of a multi-stage
threat campaign using **Remcos Remote Access Trojan (RAT)** as the
case-study malware. It explains the attack lifecycle, maps possible
attacker behaviours to the MITRE ATT&CK framework, and demonstrates how
command-and-control (C2) beaconing patterns may be identified from
sample network logs.

**Important:** This project uses simulated network traffic and
illustrative examples. It does not execute Remcos, connect to a real C2
server, or analyse a live infected system.

Project Objectives

-   Understand the stages of a multi-stage RAT attack.
-   Study Remcos RAT capabilities and associated security risks.
-   Map relevant behaviours to MITRE ATT&CK techniques.
-   Explain C2 architecture and periodic beaconing.
-   Demonstrate basic beaconing detection using Python.
-   Analyse sample network logs and identify repeated connections.

 Project Contents

  -----------------------------------------------------------------------
  File                                Description
  ----------------------------------- -----------------------------------
  `index.html`                        Project website with explanations,
                                      architecture, ATT&CK mapping, and
                                      simulated demonstrations

  `detect_beaconing.py`               Python script that checks
                                      connection intervals for possible
                                      beacon-like patterns

  `analyse_traffic.py`                Python script that summarises
                                      sample network traffic and repeated
                                      destinations

  `sample_network_logs.csv`           Synthetic network-log dataset used
                                      by the Python scripts
  -----------------------------------------------------------------------

All files are stored in the repository root directory.

## Technologies and Tools

-   HTML, CSS, and JavaScript -- project website and browser-based
    demonstrations
-   Python -- sample log analysis and beaconing detection
-   CSV -- sample network traffic data
-   MITRE ATT&CK -- attacker behaviour classification
-   GitHub and GitHub Pages -- source-code hosting and website
    publication

 How to Run the Python Scripts

 Requirements

-   Python 3 installed
-   The project files downloaded or cloned to the same folder

 Steps

1.  Open a terminal in the project folder.

2.  Run the beaconing detection script:

    ``` bash
    python detect_beaconing.py
    ```

3.  Run the traffic analysis script:

    ``` bash
    python analyse_traffic.py
    ```

The scripts read `sample_network_logs.csv` from the same folder. If your
scripts use a different file path, update the path to match the location
of the CSV file.

## Understanding the Demonstrations

-   **C2 Beaconing Detection:** Uses synthetic timestamps to calculate
    intervals between repeated connections. Regular intervals may
    indicate beacon-like behaviour, but this alone is not proof of
    malware.
-   **Network Traffic Analysis:** Counts sample log entries and
    highlights destinations that appear repeatedly.
-   **Monitoring Dashboard:** Displays illustrative statistics for
    learning purposes; it is not connected to a live monitoring system.

## MITRE ATT&CK Mapping

The website discusses selected techniques that may be relevant to stages
of a RAT campaign. Technique mappings are illustrative and should be
validated against evidence from a specific sample or incident before
being treated as confirmed findings.

Reference: [MITRE ATT&CK](https://attack.mitre.org/)

## Project Website

-   GitHub repository:
    https://github.com/jenu5364-creator/APT-Campaign-Multi-Stage-RAT-Analysis/
-   GitHub Pages website:
    https://jenu5364-creator.github.io/APT-Campaign-Multi-Stage-RAT-Analysis/

## Project Role

**Project Lead:** Janifar J.\
**Assigned Role:** Lead Architect -- ATT&CK Mapping & C2 Beaconing
Architecture

## Learning Outcomes

-   Improved understanding of RAT attack stages and C2 communication.
-   Practised basic Python-based network-log analysis.
-   Learned to interpret repeated connection intervals.
-   Applied MITRE ATT&CK to organise observed or hypothesised
    behaviours.
-   Developed a simple cybersecurity project website.

## Disclaimer

This project is created for academic and educational purposes only. The
dataset and demonstrations are simulated. Do not use malware or testing
techniques against systems without proper authorisation. The project
does not provide evidence that a real Remcos infection or live C2
operation has occurred.
