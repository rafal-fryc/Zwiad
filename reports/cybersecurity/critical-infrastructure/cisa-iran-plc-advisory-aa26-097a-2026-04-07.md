---
title: "CISA Joint Advisory AA26-097A: Iranian-Affiliated CyberAv3ngers Actively Exploiting Internet-Facing PLCs Across US Critical Infrastructure"
date: 2026-04-07
jurisdiction: "Federal"
category: "cybersecurity"
development_type: "guidance"
finding_id: "SCAN-20260427-006"
topic_key: "CISA-IRAN-ADVISORY-AA26097A-2026"
topic_type: "guidance"
first_reported: 2026-04-23
last_updated: 2026-04-29
status_history:
  - "2026-04-29: Revised per reviewer round 1 — corrected CVE-2021-22681 exploitation characterization; expanded Operation Epic Fury target description."
cluster: "IRGC CyberAv3ngers ICS/PLC Attacks on US Critical Infrastructure"
cluster_slug: "irgc-cyberav3ngers-ics-plc-attacks"
---

# CISA Joint Advisory AA26-097A: Iranian-Affiliated CyberAv3ngers Actively Exploiting Internet-Facing PLCs Across US Critical Infrastructure

**Jurisdiction:** Federal | **Category:** Cybersecurity | **Date:** April 7, 2026

## Summary [HIGH confidence]

On April 7, 2026, six US federal agencies -- FBI, CISA, NSA, EPA, Department of Energy, and US Cyber Command's Cyber National Mission Force -- jointly published [Advisory AA26-097A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-097a) confirming that Iranian-affiliated cyber actors linked to the Islamic Revolutionary Guard Corps Cyber Electronic Command (IRGC-CEC) have been actively exploiting internet-facing Rockwell Automation/Allen-Bradley programmable logic controllers (PLCs) across US critical infrastructure since at least March 2026. Confirmed compromises span the energy, water and wastewater systems, and government services and facilities sectors, with some victims experiencing operational disruption and financial loss. The advisory represents a significant escalation from prior IRGC-linked PLC campaigns and is directly linked to Iranian cyber retaliation following Operation Epic Fury, the February 28, 2026 US-Israeli military strikes on Iran.

## Key Facts [HIGH confidence]

- The joint advisory was co-authored by [FBI, CISA, NSA, EPA, Department of Energy, and US Cyber Command CNMF](https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-097a), making it one of the broadest interagency OT security warnings issued to date.
- The threat actor is [CyberAv3ngers](https://www.tenable.com/blog/what-to-know-about-cyberav3ngers-the-irgc-linked-group-targeting-critical-infrastructure), an IRGC-CEC-affiliated group also tracked as Shahid Kaveh Group, Hydro Kitten, Storm-0784, and UNC5691.
- Compromised devices include [Rockwell Automation CompactLogix and Micro850 PLCs](https://censys.com/blog/iranian-affiliated-apt-targeting-rockwell-allen-bradley-plcs/) -- the most widely deployed industrial automation controllers in North America.
- Actors exploited [CVE-2021-22681](https://thehackernews.com/2026/03/hikvision-and-rockwell-automation-cvss.html), a CVSS 9.8 authentication bypass in Rockwell Automation Logix products, by abusing an insufficiently protected cryptographic key shared between Studio 5000 Logix Designer and Logix controllers. This allowed unauthenticated remote access to exposed PLCs. CISA added CVE-2021-22681 to its [Known Exploited Vulnerabilities (KEV) catalog on March 5, 2026](https://thehackernews.com/2026/03/hikvision-and-rockwell-automation-cvss.html) with a mandatory federal remediation deadline of March 26, 2026. No vendor patch exists for this vulnerability.
- Malicious traffic was directed to devices on ports 44818 (EtherNet/IP), 2222, 102, 22, and 502; actors also deployed [Dropbear SSH software](https://securityaffairs.com/190485/apt/u-s-agencies-alert-iran-linked-actors-target-critical-infrastructure-plcs.html) on victim endpoints for persistent remote access via port 22.
- [Censys researchers identified 5,219 internet-exposed hosts globally](https://cybersecuritynews.com/censys-warns-5219-rockwell-allen-bradley-plcs/) responding to EtherNet/IP on port 44818 that self-identify as Rockwell Automation/Allen-Bradley devices.
- Attack effects included tampering with PLC project files and manipulation of data displayed on HMI and SCADA systems, causing operational disruption and financial loss at victim organizations.
- The advisory is linked to [Operation Epic Fury](https://flashpoint.io/blog/escalation-in-the-middle-east-operation-epic-fury/), the February 28, 2026 US-Israeli coordinated strikes targeting Iranian leadership nodes (including the Supreme Leader), air defense systems, missile launch infrastructure, missile production, and nuclear facilities -- which triggered a documented campaign of Iranian cyber retaliation against US critical infrastructure.
- This campaign follows [Advisory AA23-335A (November 2023)](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-335a), in which CyberAv3ngers targeted internet-exposed Unitronics Vision Series PLCs with default credentials, compromising at least 75 devices across US water and wastewater facilities.
- The 2026 campaign marks a significant tactical evolution: where the 2023 campaign relied on default credentials, the 2026 operation exploits CVE-2021-22681 via legitimate vendor engineering software to establish authenticated connections to exposed controllers without authorization.
- The [IC3 / FBI also published the advisory in PDF](https://www.ic3.gov/CSA/2026/260407.pdf) via the Internet Crime Complaint Center.

## Threat Actor Background [HIGH confidence]

CyberAv3ngers is an offensive cyber persona operated by Iran's [IRGC Cyber Electronic Command (IRGC-CEC)](https://www.tenable.com/blog/what-to-know-about-cyberav3ngers-the-irgc-linked-group-targeting-critical-infrastructure). The group has been active since at least October 2020 and has consistently targeted industrial control systems (ICS) and operational technology (OT) environments in the US, Israel, and allied nations. The group's multiple tracking aliases -- Shahid Kaveh Group (US government designation), Hydro Kitten (Microsoft), Storm-0784 (Microsoft), and UNC5691 (Mandiant/Google) -- reflect attribution by multiple independent intelligence teams converging on a single state-sponsored actor.

In late 2024, [IOCONTROL](https://www.tenable.com/blog/what-to-know-about-cyberav3ngers-the-irgc-linked-group-targeting-critical-infrastructure), a custom Linux-based malware platform designed for IoT and OT environments, was attributed to this group. IOCONTROL targets routers, PLCs, HMIs, IP cameras, firewalls, and fuel management systems using MQTT over TLS for command-and-control -- indicating a sustained investment in OT-specific offensive capabilities.

The 2026 campaign is explicitly framed in the advisory as retaliatory in nature. Following Operation Epic Fury, Iranian threat actors and pro-Iran hacktivist collectives publicly threatened attacks on US, Israeli, and allied critical infrastructure. The [Flashpoint analysis](https://flashpoint.io/blog/escalation-in-the-middle-east-operation-epic-fury/) documents multiple simultaneous campaigns by Iran-aligned groups beginning in early March 2026.

## Attack Vectors and Technical Details [HIGH confidence]

The 2026 campaign exploits two compounding conditions: a known software vulnerability in Rockwell Automation Logix products, and PLCs placed directly on the public internet without adequate network security controls.

**CVE-2021-22681 -- Authentication Bypass (CVSS 9.8):**

[CVE-2021-22681](https://1898advisories.burnsmcd.com/rockwell-automation-logix-products-actively-exploited-authentication-bypass-via-insufficiently-protected-cryptographic-key) is an insufficiently protected credentials vulnerability (CWE-522) affecting Rockwell Automation RSLogix 5000 (versions 16-20) and Studio 5000 Logix Designer (version 21.0 and later), as well as CompactLogix, ControlLogix, DriveLogix, GuardLogix, and SoftLogix 5800 controller hardware. The vulnerability arises from an insufficiently protected cryptographic key shared between engineering software and the controllers. An unauthenticated attacker who can reach an exposed controller over the network can discover or intercept this key, impersonate legitimate engineering software, bypass all authentication controls, and establish a fully authenticated session with the controller. No user interaction is required and attack complexity is low. Rockwell Automation has confirmed no patch is available; defense-in-depth mitigations are the primary remediation path. CISA added CVE-2021-22681 to its [Known Exploited Vulnerabilities catalog](https://thehackernews.com/2026/03/hikvision-and-rockwell-automation-cvss.html) on March 5, 2026.

**Attack chain:**

1. Actors scanned for internet-exposed Rockwell Automation PLCs using overseas-based IP addresses and leased third-party hosting infrastructure.
2. Actors exploited CVE-2021-22681 to bypass authentication by abusing the insufficiently protected cryptographic key, then used [Studio 5000 Logix Designer software](https://industrialcyber.co/cisa/ongoing-cyberattacks-targeting-internet-connected-plcs-disrupt-us-critical-infrastructure-agencies-warn/) to establish EtherNet/IP protocol connections to exposed CompactLogix and Micro850 controllers on port 44818.
3. Once authenticated, actors manipulated PLC project files -- the configuration files that govern physical process logic -- and altered data displayed on HMI and SCADA dashboards.
4. Actors deployed [Dropbear SSH](https://securityaffairs.com/190485/apt/u-s-agencies-alert-iran-linked-actors-target-critical-infrastructure-plcs.html) on victim endpoints for persistent remote access.

While no zero-day exploit was required -- CVE-2021-22681 has been publicly known since 2021 -- its combination with internet-exposed PLCs created an exploitable condition that actors have now actively weaponized at scale. The advisory provides downloadable IOC files in STIX XML and JSON formats.

Ports associated with malicious traffic: **44818** (EtherNet/IP), **2222**, **102** (S7/Siemens-protocol traffic also monitored), **22** (SSH/Dropbear), **502** (Modbus).

## Affected Sectors and Systems [HIGH confidence]

The advisory confirms compromises across three CISA-designated critical infrastructure sectors:

- **Water and Wastewater Systems (WWS)** -- historically the most heavily targeted sector in prior IRGC-linked PLC campaigns
- **Energy** -- includes electric utilities and related generation and distribution infrastructure
- **Government Services and Facilities** -- federal, state, and local government facility automation systems

The [Censys exposure scan](https://censys.com/blog/iranian-affiliated-apt-targeting-rockwell-allen-bradley-plcs/) identified 5,219 globally internet-exposed hosts answering on EtherNet/IP (port 44818) that self-identify as Rockwell/Allen-Bradley devices, indicating the potential attack surface extends well beyond confirmed compromises. While Censys does not disaggregate by sector, Rockwell Automation's dominant market position means exposure is likely distributed across all industrial sectors that rely on Allen-Bradley automation equipment.

## Mitigation Requirements [HIGH confidence]

The advisory's mitigation priorities, as summarized by [1898 & Co. (Burns & McDonnell)](https://1898advisories.burnsmcd.com/iranian-affiliated-cyber-actors-exploit-rockwell-automation-programmable-logic-controllers-across-u.s.-critical-infrastructure-cisa-aa26-097a) and [Crowell & Moring](https://www.crowell.com/en/insights/client-alerts/federal-agencies-warn-of-iranian-affiliated-cyber-actors-exploiting-internet-facing-operational-technology-devices):

**Immediate (Priority 1-4 per 1898 & Co.):**
1. **Remove PLCs from direct internet exposure** -- place all OT devices behind a firewall, secure gateway, or VPN. This eliminates internet reachability as an enabling condition for CVE-2021-22681 exploitation and requires no new technology investment.
2. **Review access logs** for IOCs provided in the advisory, with particular attention to EtherNet/IP (port 44818), Modbus (port 502), S7 (port 102), and SSH (port 22) traffic, especially connections originating from overseas-based or third-party hosting IP ranges.
3. **Audit PLC project files** for unauthorized modifications to logic or configuration.
4. **Harden SCADA/HMI displays** and verify that data shown on human-machine interfaces accurately reflects physical process states.

**Additional hardening:**
5. Implement multi-factor authentication on all remote access pathways to OT environments.
6. Apply the principle of least privilege -- limit which systems and users can initiate connections to PLCs.
7. Monitor for Dropbear SSH installations on OT network endpoints, which is atypical for industrial environments.
8. Download and ingest IOC files (STIX XML / JSON) from the advisory into security monitoring platforms.
9. Note that because no vendor patch exists for CVE-2021-22681, network segmentation and access controls are the only available mitigations. Organizations should treat this as a permanent architectural requirement rather than an interim workaround.

## Regulatory Implications [MEDIUM confidence]

**CIRCIA Reporting Obligations**

Critical infrastructure operators who experienced or are experiencing compromises consistent with the IOCs in AA26-097A must evaluate whether a CIRCIA-reportable incident has occurred. Under the [Cyber Incident Reporting for Critical Infrastructure Act of 2022 (CIRCIA)](https://www.cisa.gov/topics/cyber-threats-and-advisories/information-sharing/cyber-incident-reporting-critical-infrastructure-act-2022-circia), covered entities are required to report significant cyber incidents to CISA within **72 hours** and ransomware payments within **24 hours**.

As of the advisory date, CISA's CIRCIA implementing regulations remain in proposed rulemaking status -- the [final rule has been delayed to at least May 2026](https://cyberscoop.com/cisa-pushes-final-cyber-incident-reporting-rule-to-may-2026/). However, voluntary reporting is strongly encouraged and CISA has existing mechanisms to receive incident reports. Organizations experiencing operational disruptions from PLC tampering should immediately contact CISA's 24/7 Operations Center and engage their sector-specific agency (SSA), which for water utilities is EPA, for energy is DOE, and for government facilities is CISA itself.

**Sector-Specific Requirements**

Water utilities are subject to EPA cybersecurity survey requirements under the Safe Drinking Water Act (SDWA) and should assess whether PLC compromise triggers state-level breach notification or incident reporting obligations. Energy sector operators with bulk electric system (BES) assets may have concurrent [NERC CIP](https://www.nerc.com/pa/Stand/Pages/CIPStandards.aspx) incident reporting obligations under CIP-008.

**Law Firm Analysis**

The [Akin Gump client alert](https://www.akingump.com/en/insights/alerts/iran-conflict-spurs-cisa-warning-for-us-critical-infrastructure) and [Crowell & Moring advisory](https://www.crowell.com/en/insights/client-alerts/federal-agencies-warn-of-iranian-affiliated-cyber-actors-exploiting-internet-facing-operational-technology-devices) both emphasize that this advisory, combined with the geopolitical context of Operation Epic Fury, represents an elevated and enduring threat environment. Organizations should treat the advisory's mitigation requirements not as a one-time remediation but as a prompt to review OT network architecture holistically.

## Action Items

- **Immediately audit all internet-facing OT assets** -- identify any Rockwell Automation CompactLogix or Micro850 PLCs reachable from the public internet without a firewall or VPN intermediary and remediate.
- **Treat CVE-2021-22681 as unpatched permanently** -- no vendor fix exists. Network segmentation and removal of internet exposure are the only mitigations. Verify your affected Logix controller versions against the [CISA ICS advisory ICSA-21-056-03](https://www.cisa.gov/news-events/ics-advisories/icsa-21-056-03).
- **Ingest IOCs now** -- download the STIX XML and JSON IOC files from [CISA Advisory AA26-097A](https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-097a) and configure SIEM/EDR tools to alert on matches.
- **Check ports 44818, 2222, 102, 22, and 502** in network logs for any suspicious inbound or outbound traffic, particularly from overseas IP blocks or known third-party hosting providers.
- **Verify PLC project file integrity** -- compare current project files against known-good backups to identify unauthorized modifications to process logic.
- **Scan OT endpoints for Dropbear SSH** -- presence in an industrial environment is anomalous and may indicate prior compromise.
- **Engage your SSA** -- water utilities should contact EPA; energy operators should contact DOE; government facility operators should contact CISA. Do not wait for confirmed compromise before making contact.
- **Evaluate CIRCIA reporting obligations** -- if operational disruption has occurred, consult legal counsel on whether a CIRCIA voluntary report or state-level notification is warranted even prior to final rule publication.
- **Review NERC CIP obligations (energy sector)** -- BES operators must assess CIP-008 incident reporting requirements for any confirmed OT compromise.
- **Monitor the geopolitical environment** -- the advisory explicitly links this campaign to Operation Epic Fury. Sustained Iranian retaliatory cyber operations should be anticipated for the foreseeable future. Elevate OT security posture accordingly.

## Related Reports

- [CIRCIA Final Cyber Incident Reporting Rule Delayed Again -- Now Expected May 2026 at Earliest](reports/cybersecurity/incident-reporting/federal-circia-final-rule-delay-2026-04-07.md) -- Directly relevant: critical infrastructure operators affected by AA26-097A must understand the current CIRCIA rulemaking status when assessing their reporting obligations.
- [Government and Industry Response to AI-Enabled Cyberattacks: AISI Evaluation, UK Warning, and Emergency Guidance (April 2026)](reports/cybersecurity/standards-guidance/federal-ai-cyberattack-agency-response-2026-04-15.md) -- Related: contemporaneous federal guidance on state-sponsored cyberattacks, escalation of offensive cyber operations against US infrastructure in spring 2026.

## Sources

1. [CISA Advisory AA26-097A -- Official Advisory Page](https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-097a) -- Primary official source; co-authored by FBI, CISA, NSA, EPA, DOE, and US Cyber Command
2. [CISA AA26-097A -- Full PDF (508c)](https://www.cisa.gov/sites/default/files/2026-04/AA26-097A-Iranian-Affiliated-Cyber-Actors-Exploit-Programmable-Logic-Controllers-Across-US-Critical-Infrastructure_508c.pdf) -- Official advisory full text including IOC tables
3. [FBI/IC3 Publication of AA26-097A](https://www.ic3.gov/CSA/2026/260407.pdf) -- FBI Internet Crime Complaint Center parallel publication
4. [CISA Advisory AA23-335A -- Prior IRGC PLC Campaign (November 2023)](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-335a) -- Predecessor advisory; documents 2023 Unitronics PLC compromise
5. [CISA ICS Advisory ICSA-21-056-03 -- Rockwell Automation Logix Controllers](https://www.cisa.gov/news-events/ics-advisories/icsa-21-056-03) -- Original ICS advisory for CVE-2021-22681; lists affected products and versions
6. [Akin Gump Client Alert: Iran Conflict Spurs CISA Warning for US Critical Infrastructure](https://www.akingump.com/en/insights/alerts/iran-conflict-spurs-cisa-warning-for-us-critical-infrastructure) -- Law firm analysis with regulatory guidance for critical infrastructure operators
7. [Crowell & Moring: Federal Agencies Warn of Iranian-Affiliated Cyber Actors Exploiting Internet-Facing OT Devices](https://www.crowell.com/en/insights/client-alerts/federal-agencies-warn-of-iranian-affiliated-cyber-actors-exploiting-internet-facing-operational-technology-devices) -- Law firm client alert with prioritized mitigation recommendations
8. [1898 & Co. (Burns & McDonnell): CISA AA26-097A Analysis](https://1898advisories.burnsmcd.com/iranian-affiliated-cyber-actors-exploit-rockwell-automation-programmable-logic-controllers-across-u.s.-critical-infrastructure-cisa-aa26-097a) -- Engineering firm analysis with prioritized mitigation matrix
9. [1898 & Co.: Rockwell Automation CVE-2021-22681 -- Actively Exploited Authentication Bypass](https://1898advisories.burnsmcd.com/rockwell-automation-logix-products-actively-exploited-authentication-bypass-via-insufficiently-protected-cryptographic-key) -- Detailed technical analysis of CVE-2021-22681, affected products, and mitigation options
10. [Censys: Iranian-Affiliated APT Targeting Rockwell/Allen-Bradley PLCs](https://censys.com/blog/iranian-affiliated-apt-targeting-rockwell-allen-bradley-plcs/) -- Internet scan data identifying 5,219 exposed Rockwell/Allen-Bradley hosts
11. [Tenable: CyberAv3ngers FAQ -- Iran-Linked Threat Group Targeting US Critical Infrastructure](https://www.tenable.com/blog/what-to-know-about-cyberav3ngers-the-irgc-linked-group-targeting-critical-infrastructure) -- Comprehensive threat actor profile including IOCONTROL malware analysis
12. [Security Affairs: US Agencies Alert Iran-Linked Actors Target Critical Infrastructure PLCs](https://securityaffairs.com/190485/apt/u-s-agencies-alert-iran-linked-actors-target-critical-infrastructure-plcs.html) -- Technical analysis including port and Dropbear SSH details
13. [Industrial Cyber: Ongoing Cyberattacks Targeting Internet-Connected PLCs](https://industrialcyber.co/cisa/ongoing-cyberattacks-targeting-internet-connected-plcs-disrupt-us-critical-infrastructure-agencies-warn/) -- Technical reporting on Studio 5000 attack vector
14. [The Hacker News: Hikvision and Rockwell Automation CVSS 9.8 Flaws Added to CISA KEV Catalog (CVE-2021-22681)](https://thehackernews.com/2026/03/hikvision-and-rockwell-automation-cvss.html) -- Confirms March 5, 2026 KEV addition and March 26, 2026 federal remediation deadline
15. [Flashpoint: Escalation in the Middle East -- Operation Epic Fury](https://flashpoint.io/blog/escalation-in-the-middle-east-operation-epic-fury/) -- Geopolitical and cyber threat intelligence context for Operation Epic Fury
16. [AttackIQ: Defending Against Iranian Cyber Threats in the Wake of Operation Epic Fury](https://www.attackiq.com/2026/03/05/operation-epic-fury/) -- Threat defense analysis linked to Epic Fury context
17. [Army Recognition: US and Israel Launch Operation Epic Fury Against Iran Nuclear Program and Missile Arsenal](https://www.armyrecognition.com/news/army-news/2026/us-israel-launch-operation-epic-fury-against-iran-nuclear-program-and-missile-arsenal) -- Detailed reporting on Operation Epic Fury strike targets including leadership, air defenses, missile infrastructure
18. [CISA: Cyber Incident Reporting for Critical Infrastructure Act of 2022 (CIRCIA)](https://www.cisa.gov/topics/cyber-threats-and-advisories/information-sharing/cyber-incident-reporting-critical-infrastructure-act-2022-circia) -- Official CIRCIA overview and reporting guidance
19. [CyberScoop: CISA Pushes Final Cyber Incident Reporting Rule to May 2026](https://cyberscoop.com/cisa-pushes-final-cyber-incident-reporting-rule-to-may-2026/) -- CIRCIA rulemaking timeline context
20. [CybersecurityNews: Censys Warns 5,219 Rockwell/Allen-Bradley PLCs Are Exposed](https://cybersecuritynews.com/censys-warns-5219-rockwell-allen-bradley-plcs/) -- Coverage of Censys exposure scan findings
