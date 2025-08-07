from typing import Dict, List, Optional, Any
from datetime import datetime, timedelta
from enum import Enum
from pydantic import BaseModel
import json


class IncidentSeverity(Enum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class IncidentCategory(Enum):
    BIAS = "bias"
    PRIVACY_BREACH = "privacy_breach"
    SYSTEM_FAILURE = "system_failure"
    SECURITY_BREACH = "security_breach"
    COMPLIANCE_VIOLATION = "compliance_violation"
    ETHICAL_CONCERN = "ethical_concern"
    DATA_QUALITY = "data_quality"
    PERFORMANCE_DEGRADATION = "performance_degradation"


class IncidentStatus(Enum):
    DETECTED = "detected"
    TRIAGED = "triaged"
    INVESTIGATING = "investigating"
    MITIGATING = "mitigating"
    RESOLVED = "resolved"
    CLOSED = "closed"
    POST_MORTEM = "post_mortem"


class Incident(BaseModel):
    incident_id: str
    title: str
    description: str
    category: IncidentCategory
    severity: IncidentSeverity
    status: IncidentStatus
    affected_systems: List[str]
    detection_time: datetime
    response_time: Optional[datetime]
    resolution_time: Optional[datetime]
    assigned_responder: str
    stakeholders_notified: List[str]
    impact_assessment: Dict[str, Any]
    mitigation_actions: List[str]
    root_cause: Optional[str]
    lessons_learned: List[str]


class IncidentResponseAutomation:
    def __init__(self):
        self.active_incidents: Dict[str, Incident] = {}
        self.response_playbooks = self._initialize_response_playbooks()
        self.escalation_matrix = self._initialize_escalation_matrix()
        self.notification_config = self._initialize_notification_config()
        self.sla_thresholds = self._initialize_sla_thresholds()

    def detect_and_classify_incident(self, incident_data: Dict) -> Incident:
        incident_id = f"ai_incident_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        # Classify incident category and severity
        category = self._classify_incident_category(incident_data)
        severity = self._assess_incident_severity(incident_data, category)
        
        # Create incident record
        incident = Incident(
            incident_id=incident_id,
            title=incident_data.get("title", f"AI System Incident - {category.value}"),
            description=incident_data.get("description", "AI system incident detected"),
            category=category,
            severity=severity,
            status=IncidentStatus.DETECTED,
            affected_systems=incident_data.get("affected_systems", []),
            detection_time=datetime.now(),
            response_time=None,
            resolution_time=None,
            assigned_responder="",
            stakeholders_notified=[],
            impact_assessment={},
            mitigation_actions=[],
            root_cause=None,
            lessons_learned=[]
        )
        
        # Store incident
        self.active_incidents[incident_id] = incident
        
        # Trigger automated response
        self._trigger_automated_response(incident)
        
        return incident

    def orchestrate_response_workflow(self, incident: Incident) -> Dict:
        workflow = {
            "workflow_id": f"response_{incident.incident_id}",
            "incident_id": incident.incident_id,
            "initiated_time": datetime.now().isoformat(),
            "workflow_steps": self._get_response_workflow_steps(incident),
            "automated_actions": self._execute_automated_actions(incident),
            "human_actions_required": self._identify_human_actions(incident),
            "escalation_triggered": self._check_escalation_triggers(incident),
            "notifications_sent": self._send_stakeholder_notifications(incident),
            "monitoring_activated": self._activate_incident_monitoring(incident)
        }
        
        # Update incident status
        incident.status = IncidentStatus.TRIAGED
        incident.response_time = datetime.now()
        
        return workflow

    def generate_impact_assessment(self, incident: Incident) -> Dict:
        impact_assessment = {
            "assessment_id": f"impact_{incident.incident_id}",
            "assessment_time": datetime.now().isoformat(),
            "business_impact": self._assess_business_impact(incident),
            "technical_impact": self._assess_technical_impact(incident),
            "regulatory_impact": self._assess_regulatory_impact(incident),
            "stakeholder_impact": self._assess_stakeholder_impact(incident),
            "reputation_impact": self._assess_reputation_impact(incident),
            "financial_impact": self._estimate_financial_impact(incident),
            "overall_impact_score": 0,
            "priority_classification": incident.severity.value,
            "recommended_actions": self._recommend_immediate_actions(incident)
        }
        
        # Calculate overall impact score
        impact_assessment["overall_impact_score"] = self._calculate_overall_impact_score(impact_assessment)
        
        # Update incident with impact assessment
        incident.impact_assessment = impact_assessment
        
        return impact_assessment

    def execute_mitigation_strategies(self, incident: Incident) -> Dict:
        mitigation_plan = {
            "plan_id": f"mitigation_{incident.incident_id}",
            "incident_id": incident.incident_id,
            "mitigation_start_time": datetime.now().isoformat(),
            "immediate_actions": self._execute_immediate_mitigation(incident),
            "short_term_actions": self._plan_short_term_mitigation(incident),
            "long_term_actions": self._plan_long_term_mitigation(incident),
            "success_criteria": self._define_mitigation_success_criteria(incident),
            "monitoring_requirements": self._define_mitigation_monitoring(incident),
            "rollback_plan": self._create_rollback_plan(incident),
            "validation_steps": self._define_validation_steps(incident)
        }
        
        # Update incident status and actions
        incident.status = IncidentStatus.MITIGATING
        incident.mitigation_actions.extend(mitigation_plan["immediate_actions"])
        
        return mitigation_plan

    def automate_stakeholder_notifications(self, incident: Incident) -> Dict:
        notification_plan = {
            "plan_id": f"notifications_{incident.incident_id}",
            "incident_id": incident.incident_id,
            "notification_time": datetime.now().isoformat(),
            "immediate_notifications": self._send_immediate_notifications(incident),
            "follow_up_notifications": self._schedule_follow_up_notifications(incident),
            "external_notifications": self._determine_external_notifications(incident),
            "regulatory_notifications": self._assess_regulatory_notification_requirements(incident),
            "public_communications": self._evaluate_public_communication_needs(incident),
            "notification_tracking": []
        }
        
        # Update incident with notification records
        incident.stakeholders_notified = notification_plan["immediate_notifications"]
        
        return notification_plan

    def generate_incident_documentation(self, incident: Incident) -> Dict:
        documentation = {
            "document_id": f"doc_{incident.incident_id}",
            "incident_summary": self._create_incident_summary(incident),
            "timeline": self._create_incident_timeline(incident),
            "impact_analysis": incident.impact_assessment,
            "response_actions": self._document_response_actions(incident),
            "stakeholder_communications": self._document_stakeholder_communications(incident),
            "technical_details": self._document_technical_details(incident),
            "regulatory_implications": self._document_regulatory_implications(incident),
            "lessons_learned": incident.lessons_learned,
            "recommendations": self._generate_improvement_recommendations(incident),
            "post_mortem_required": self._determine_post_mortem_requirement(incident)
        }
        
        return documentation

    def conduct_post_incident_analysis(self, incident: Incident) -> Dict:
        post_mortem = {
            "analysis_id": f"postmortem_{incident.incident_id}",
            "incident_id": incident.incident_id,
            "analysis_date": datetime.now().isoformat(),
            "incident_overview": self._summarize_incident_overview(incident),
            "root_cause_analysis": self._conduct_root_cause_analysis(incident),
            "response_effectiveness": self._analyze_response_effectiveness(incident),
            "process_improvements": self._identify_process_improvements(incident),
            "system_improvements": self._identify_system_improvements(incident),
            "training_needs": self._identify_training_needs(incident),
            "policy_updates": self._recommend_policy_updates(incident),
            "action_items": self._create_action_items(incident),
            "follow_up_schedule": self._schedule_follow_up_actions(incident)
        }
        
        # Update incident status and lessons learned
        incident.status = IncidentStatus.POST_MORTEM
        incident.lessons_learned = post_mortem["process_improvements"]
        
        return post_mortem

    def create_incident_dashboard(self, time_period: str = "30_days") -> Dict:
        dashboard = {
            "dashboard_id": f"incident_dashboard_{datetime.now().strftime('%Y%m%d')}",
            "time_period": time_period,
            "generated_time": datetime.now().isoformat(),
            "metrics": {
                "total_incidents": len(self.active_incidents),
                "open_incidents": len([i for i in self.active_incidents.values() if i.status not in [IncidentStatus.RESOLVED, IncidentStatus.CLOSED]]),
                "critical_incidents": len([i for i in self.active_incidents.values() if i.severity == IncidentSeverity.CRITICAL]),
                "average_response_time": self._calculate_average_response_time(),
                "average_resolution_time": self._calculate_average_resolution_time()
            },
            "category_breakdown": self._get_incident_category_breakdown(),
            "severity_distribution": self._get_incident_severity_distribution(),
            "top_affected_systems": self._get_top_affected_systems(),
            "trending_issues": self._identify_trending_issues(),
            "sla_compliance": self._calculate_sla_compliance(),
            "improvement_areas": self._identify_improvement_areas()
        }
        
        return dashboard

    def _initialize_response_playbooks(self) -> Dict:
        return {
            IncidentCategory.BIAS.value: {
                "immediate_actions": [
                    "Isolate affected AI system",
                    "Document bias evidence",
                    "Notify ethics committee",
                    "Assess impact on affected groups"
                ],
                "investigation_steps": [
                    "Analyze bias metrics",
                    "Review training data",
                    "Examine model predictions",
                    "Identify root cause"
                ],
                "mitigation_options": [
                    "Implement bias correction",
                    "Retrain model with balanced data",
                    "Apply post-processing fairness",
                    "Temporarily disable system"
                ]
            },
            IncidentCategory.PRIVACY_BREACH.value: {
                "immediate_actions": [
                    "Contain data exposure",
                    "Notify privacy officer",
                    "Document breach details",
                    "Preserve evidence"
                ],
                "investigation_steps": [
                    "Assess scope of data exposure",
                    "Identify affected individuals",
                    "Analyze breach cause",
                    "Review security controls"
                ],
                "mitigation_options": [
                    "Implement additional security controls",
                    "Notify affected individuals",
                    "Report to regulatory authorities",
                    "Provide identity protection services"
                ]
            },
            IncidentCategory.SYSTEM_FAILURE.value: {
                "immediate_actions": [
                    "Activate failover systems",
                    "Notify operations team",
                    "Begin system diagnostics",
                    "Communicate service status"
                ],
                "investigation_steps": [
                    "Analyze system logs",
                    "Check resource utilization",
                    "Review recent changes",
                    "Test system components"
                ],
                "mitigation_options": [
                    "Restart affected services",
                    "Scale system resources",
                    "Deploy system patches",
                    "Implement workarounds"
                ]
            }
        }

    def _initialize_escalation_matrix(self) -> Dict:
        return {
            IncidentSeverity.CRITICAL.value: {
                "level_1": ["Incident Response Team", "System Owner"],
                "level_2": ["Department Head", "Chief Risk Officer"],
                "level_3": ["CTO", "CEO"],
                "level_4": ["Board of Directors"],
                "timeline": {"level_1": 15, "level_2": 30, "level_3": 60, "level_4": 120}  # minutes
            },
            IncidentSeverity.HIGH.value: {
                "level_1": ["Incident Response Team", "System Owner"],
                "level_2": ["Department Head"],
                "level_3": ["CTO"],
                "timeline": {"level_1": 30, "level_2": 60, "level_3": 120}  # minutes
            },
            IncidentSeverity.MEDIUM.value: {
                "level_1": ["System Owner"],
                "level_2": ["Department Head"],
                "timeline": {"level_1": 60, "level_2": 240}  # minutes
            },
            IncidentSeverity.LOW.value: {
                "level_1": ["System Owner"],
                "timeline": {"level_1": 480}  # minutes (8 hours)
            }
        }

    def _initialize_notification_config(self) -> Dict:
        return {
            "channels": {
                "email": {"enabled": True, "priority": 1},
                "slack": {"enabled": True, "priority": 2},
                "sms": {"enabled": True, "priority": 3, "severity_threshold": "high"},
                "dashboard": {"enabled": True, "priority": 4}
            },
            "stakeholder_groups": {
                "incident_team": ["incident_responders", "system_owners"],
                "management": ["department_heads", "cto", "ceo"],
                "legal": ["legal_counsel", "privacy_officer"],
                "communications": ["pr_team", "customer_success"],
                "external": ["customers", "partners", "regulators"]
            }
        }

    def _initialize_sla_thresholds(self) -> Dict:
        return {
            IncidentSeverity.CRITICAL.value: {
                "response_time_minutes": 15,
                "resolution_time_hours": 4,
                "update_frequency_minutes": 30
            },
            IncidentSeverity.HIGH.value: {
                "response_time_minutes": 30,
                "resolution_time_hours": 8,
                "update_frequency_minutes": 60
            },
            IncidentSeverity.MEDIUM.value: {
                "response_time_minutes": 60,
                "resolution_time_hours": 24,
                "update_frequency_minutes": 240
            },
            IncidentSeverity.LOW.value: {
                "response_time_minutes": 480,
                "resolution_time_hours": 72,
                "update_frequency_minutes": 1440
            }
        }

    def _classify_incident_category(self, incident_data: Dict) -> IncidentCategory:
        description = incident_data.get("description", "").lower()
        
        # Category keywords mapping
        category_keywords = {
            IncidentCategory.BIAS: ["bias", "discrimination", "unfair", "disparity"],
            IncidentCategory.PRIVACY_BREACH: ["privacy", "data breach", "personal data", "unauthorized access"],
            IncidentCategory.SYSTEM_FAILURE: ["system down", "failure", "outage", "unavailable"],
            IncidentCategory.SECURITY_BREACH: ["security", "breach", "attack", "vulnerability"],
            IncidentCategory.COMPLIANCE_VIOLATION: ["compliance", "regulation", "violation", "gdpr"],
            IncidentCategory.ETHICAL_CONCERN: ["ethics", "moral", "concern", "inappropriate"],
            IncidentCategory.DATA_QUALITY: ["data quality", "corrupt data", "missing data"],
            IncidentCategory.PERFORMANCE_DEGRADATION: ["performance", "slow", "degradation", "latency"]
        }
        
        # Check for category matches
        for category, keywords in category_keywords.items():
            for keyword in keywords:
                if keyword in description:
                    return category
        
        # Default category
        return IncidentCategory.SYSTEM_FAILURE

    def _assess_incident_severity(self, incident_data: Dict, category: IncidentCategory) -> IncidentSeverity:
        # Base severity by category
        category_severities = {
            IncidentCategory.PRIVACY_BREACH: IncidentSeverity.HIGH,
            IncidentCategory.SECURITY_BREACH: IncidentSeverity.HIGH,
            IncidentCategory.COMPLIANCE_VIOLATION: IncidentSeverity.HIGH,
            IncidentCategory.BIAS: IncidentSeverity.MEDIUM,
            IncidentCategory.ETHICAL_CONCERN: IncidentSeverity.MEDIUM,
            IncidentCategory.SYSTEM_FAILURE: IncidentSeverity.MEDIUM,
            IncidentCategory.PERFORMANCE_DEGRADATION: IncidentSeverity.LOW,
            IncidentCategory.DATA_QUALITY: IncidentSeverity.LOW
        }
        
        base_severity = category_severities.get(category, IncidentSeverity.MEDIUM)
        
        # Adjust based on impact indicators
        impact_indicators = incident_data.get("impact_indicators", {})
        
        if impact_indicators.get("customer_facing", False) or impact_indicators.get("high_volume", False):
            # Escalate severity
            severity_escalation = {
                IncidentSeverity.LOW: IncidentSeverity.MEDIUM,
                IncidentSeverity.MEDIUM: IncidentSeverity.HIGH,
                IncidentSeverity.HIGH: IncidentSeverity.CRITICAL
            }
            base_severity = severity_escalation.get(base_severity, base_severity)
        
        return base_severity

    def _trigger_automated_response(self, incident: Incident) -> None:
        # Execute immediate automated actions based on category and severity
        playbook = self.response_playbooks.get(incident.category.value, {})
        immediate_actions = playbook.get("immediate_actions", [])
        
        for action in immediate_actions:
            # In real implementation, these would trigger actual system actions
            incident.mitigation_actions.append(f"Automated: {action}")

    def _get_response_workflow_steps(self, incident: Incident) -> List[Dict]:
        return [
            {"step": "Detection and Classification", "status": "completed", "timestamp": incident.detection_time.isoformat()},
            {"step": "Initial Response", "status": "in_progress", "estimated_completion": "+15 minutes"},
            {"step": "Impact Assessment", "status": "pending", "estimated_completion": "+30 minutes"},
            {"step": "Mitigation", "status": "pending", "estimated_completion": "+2 hours"},
            {"step": "Resolution", "status": "pending", "estimated_completion": "+4 hours"},
            {"step": "Post-Incident Review", "status": "pending", "estimated_completion": "+1 week"}
        ]

    def _execute_automated_actions(self, incident: Incident) -> List[str]:
        automated_actions = [
            f"Incident {incident.incident_id} logged in tracking system",
            f"Severity {incident.severity.value} response team notified",
            f"Automated monitoring activated for affected systems",
            f"Initial stakeholder notifications sent"
        ]
        
        return automated_actions

    def _identify_human_actions(self, incident: Incident) -> List[str]:
        human_actions = [
            "Detailed technical investigation required",
            "Stakeholder impact assessment needed",
            "Root cause analysis to be conducted",
            "Mitigation strategy decision required"
        ]
        
        return human_actions

    def _check_escalation_triggers(self, incident: Incident) -> bool:
        # Check if incident meets escalation criteria
        return incident.severity in [IncidentSeverity.HIGH, IncidentSeverity.CRITICAL]

    def _send_stakeholder_notifications(self, incident: Incident) -> List[str]:
        notifications_sent = []
        
        # Determine notification recipients based on severity and category
        if incident.severity == IncidentSeverity.CRITICAL:
            notifications_sent.extend([
                "CEO notification sent",
                "Board notification scheduled",
                "Regulatory notification prepared"
            ])
        
        if incident.category in [IncidentCategory.PRIVACY_BREACH, IncidentCategory.COMPLIANCE_VIOLATION]:
            notifications_sent.extend([
                "Legal team notified",
                "Privacy officer alerted",
                "Compliance team engaged"
            ])
        
        return notifications_sent

    def _activate_incident_monitoring(self, incident: Incident) -> Dict:
        return {
            "monitoring_activated": True,
            "affected_systems_monitoring": incident.affected_systems,
            "alert_thresholds_adjusted": True,
            "real_time_dashboards_enabled": True
        }

    def _assess_business_impact(self, incident: Incident) -> Dict:
        return {
            "revenue_impact": "Medium" if incident.severity in [IncidentSeverity.HIGH, IncidentSeverity.CRITICAL] else "Low",
            "customer_impact": "High" if "customer_facing" in str(incident.affected_systems) else "Medium",
            "operational_disruption": incident.severity.value,
            "brand_reputation": "Medium" if incident.category in [IncidentCategory.BIAS, IncidentCategory.PRIVACY_BREACH] else "Low"
        }

    def _assess_technical_impact(self, incident: Incident) -> Dict:
        return {
            "system_availability": "Degraded" if incident.category == IncidentCategory.SYSTEM_FAILURE else "Normal",
            "data_integrity": "Compromised" if incident.category in [IncidentCategory.PRIVACY_BREACH, IncidentCategory.DATA_QUALITY] else "Intact",
            "performance_impact": incident.severity.value,
            "recovery_complexity": "High" if incident.severity == IncidentSeverity.CRITICAL else "Medium"
        }

    def _assess_regulatory_impact(self, incident: Incident) -> Dict:
        regulatory_risk = "High" if incident.category in [
            IncidentCategory.PRIVACY_BREACH, 
            IncidentCategory.COMPLIANCE_VIOLATION,
            IncidentCategory.BIAS
        ] else "Low"
        
        return {
            "regulatory_risk": regulatory_risk,
            "reporting_required": regulatory_risk == "High",
            "compliance_implications": ["EU AI Act", "GDPR"] if regulatory_risk == "High" else [],
            "potential_penalties": "Significant" if regulatory_risk == "High" else "Minimal"
        }

    def _assess_stakeholder_impact(self, incident: Incident) -> List[str]:
        affected_stakeholders = ["Internal Operations Team"]
        
        if incident.severity in [IncidentSeverity.HIGH, IncidentSeverity.CRITICAL]:
            affected_stakeholders.extend(["Customers", "Partners", "Executive Leadership"])
        
        if incident.category in [IncidentCategory.PRIVACY_BREACH, IncidentCategory.BIAS]:
            affected_stakeholders.extend(["Affected Individuals", "Regulators", "Public"])
        
        return affected_stakeholders

    def _assess_reputation_impact(self, incident: Incident) -> str:
        if incident.category in [IncidentCategory.BIAS, IncidentCategory.PRIVACY_BREACH, IncidentCategory.ETHICAL_CONCERN]:
            return "High"
        elif incident.severity == IncidentSeverity.CRITICAL:
            return "Medium"
        else:
            return "Low"

    def _estimate_financial_impact(self, incident: Incident) -> Dict:
        # Simplified financial impact estimation
        base_costs = {
            IncidentSeverity.CRITICAL: {"min": 100000, "max": 1000000},
            IncidentSeverity.HIGH: {"min": 25000, "max": 250000},
            IncidentSeverity.MEDIUM: {"min": 5000, "max": 50000},
            IncidentSeverity.LOW: {"min": 1000, "max": 10000}
        }
        
        cost_estimate = base_costs.get(incident.severity, base_costs[IncidentSeverity.MEDIUM])
        
        return {
            "estimated_cost_range": f"${cost_estimate['min']:,} - ${cost_estimate['max']:,}",
            "cost_categories": [
                "Incident response costs",
                "System recovery costs",
                "Potential regulatory fines",
                "Business disruption costs",
                "Reputation recovery costs"
            ]
        }

    def _calculate_overall_impact_score(self, impact_assessment: Dict) -> float:
        # Simplified scoring algorithm (0-10 scale)
        return 6.5 if "High" in str(impact_assessment) else 4.0

    def _recommend_immediate_actions(self, incident: Incident) -> List[str]:
        playbook = self.response_playbooks.get(incident.category.value, {})
        return playbook.get("immediate_actions", [
            "Assess incident scope and impact",
            "Implement immediate containment measures",
            "Notify relevant stakeholders",
            "Begin detailed investigation"
        ])

    def _execute_immediate_mitigation(self, incident: Incident) -> List[str]:
        playbook = self.response_playbooks.get(incident.category.value, {})
        return playbook.get("mitigation_options", [])[:2]  # First 2 immediate actions

    def _plan_short_term_mitigation(self, incident: Incident) -> List[str]:
        return [
            "Implement temporary workarounds",
            "Enhanced monitoring and alerting",
            "Stakeholder communication plan",
            "Resource allocation for resolution"
        ]

    def _plan_long_term_mitigation(self, incident: Incident) -> List[str]:
        return [
            "Root cause remediation",
            "Process improvements",
            "System hardening",
            "Training and awareness programs"
        ]

    def _define_mitigation_success_criteria(self, incident: Incident) -> List[str]:
        return [
            "Incident contained and no longer spreading",
            "Affected systems restored to normal operation",
            "Stakeholders informed of resolution",
            "Root cause identified and addressed"
        ]

    def _define_mitigation_monitoring(self, incident: Incident) -> Dict:
        return {
            "monitoring_frequency": "Every 15 minutes for critical, hourly for others",
            "key_metrics": ["system_availability", "error_rates", "performance_metrics"],
            "alert_thresholds": "Adjusted for incident recovery",
            "reporting_schedule": "Updates every 2 hours during active response"
        }

    def _create_rollback_plan(self, incident: Incident) -> List[str]:
        return [
            "Document current system state",
            "Prepare system backups",
            "Define rollback triggers",
            "Test rollback procedures"
        ]

    def _define_validation_steps(self, incident: Incident) -> List[str]:
        return [
            "Verify system functionality",
            "Confirm stakeholder satisfaction",
            "Validate regulatory compliance",
            "Check monitoring and alerting"
        ]

    def _send_immediate_notifications(self, incident: Incident) -> List[str]:
        return [
            "Incident Response Team",
            "System Owner",
            "Department Head" if incident.severity in [IncidentSeverity.HIGH, IncidentSeverity.CRITICAL] else None
        ]

    def _schedule_follow_up_notifications(self, incident: Incident) -> List[Dict]:
        return [
            {"audience": "Management", "schedule": "Every 2 hours", "format": "Status update"},
            {"audience": "Stakeholders", "schedule": "Daily", "format": "Progress report"},
            {"audience": "Customers", "schedule": "As needed", "format": "Service status"}
        ]

    def _determine_external_notifications(self, incident: Incident) -> List[str]:
        external_notifications = []
        
        if incident.category in [IncidentCategory.PRIVACY_BREACH, IncidentCategory.COMPLIANCE_VIOLATION]:
            external_notifications.extend(["Customers", "Regulators"])
        
        if incident.severity == IncidentSeverity.CRITICAL:
            external_notifications.extend(["Key Partners", "Media (if required)"])
        
        return external_notifications

    def _assess_regulatory_notification_requirements(self, incident: Incident) -> Dict:
        requirements = {
            "required": False,
            "timeline": None,
            "authorities": []
        }
        
        if incident.category in [IncidentCategory.PRIVACY_BREACH, IncidentCategory.COMPLIANCE_VIOLATION]:
            requirements.update({
                "required": True,
                "timeline": "72 hours for data protection authorities",
                "authorities": ["Data Protection Authority", "Relevant Regulatory Bodies"]
            })
        
        return requirements

    def _evaluate_public_communication_needs(self, incident: Incident) -> Dict:
        return {
            "public_statement_required": incident.severity == IncidentSeverity.CRITICAL,
            "media_response_needed": incident.category in [IncidentCategory.PRIVACY_BREACH, IncidentCategory.BIAS],
            "customer_communication": "customer_facing" in str(incident.affected_systems),
            "social_media_monitoring": True
        }

    def _create_incident_summary(self, incident: Incident) -> str:
        return f"""
        Incident {incident.incident_id}: {incident.title}
        Category: {incident.category.value} | Severity: {incident.severity.value}
        Status: {incident.status.value}
        Detection Time: {incident.detection_time.isoformat()}
        Affected Systems: {', '.join(incident.affected_systems)}
        """

    def _create_incident_timeline(self, incident: Incident) -> List[Dict]:
        timeline = [
            {"timestamp": incident.detection_time.isoformat(), "event": "Incident detected and logged"}
        ]
        
        if incident.response_time:
            timeline.append({
                "timestamp": incident.response_time.isoformat(),
                "event": "Response initiated and team notified"
            })
        
        if incident.resolution_time:
            timeline.append({
                "timestamp": incident.resolution_time.isoformat(),
                "event": "Incident resolved"
            })
        
        return timeline

    def _document_response_actions(self, incident: Incident) -> List[str]:
        return incident.mitigation_actions

    def _document_stakeholder_communications(self, incident: Incident) -> List[str]:
        return [f"Notified: {stakeholder}" for stakeholder in incident.stakeholders_notified]

    def _document_technical_details(self, incident: Incident) -> Dict:
        return {
            "affected_systems": incident.affected_systems,
            "impact_assessment": incident.impact_assessment,
            "root_cause": incident.root_cause or "Under investigation"
        }

    def _document_regulatory_implications(self, incident: Incident) -> List[str]:
        implications = []
        
        if incident.category == IncidentCategory.PRIVACY_BREACH:
            implications.extend(["GDPR Article 33 notification required", "Data subject notification may be required"])
        
        if incident.category == IncidentCategory.BIAS:
            implications.extend(["EU AI Act Article 10 compliance review", "Bias mitigation measures required"])
        
        return implications

    def _generate_improvement_recommendations(self, incident: Incident) -> List[str]:
        return [
            "Review and update incident response procedures",
            "Enhance monitoring and alerting capabilities",
            "Improve stakeholder communication processes",
            "Strengthen preventive controls"
        ]

    def _determine_post_mortem_requirement(self, incident: Incident) -> bool:
        return incident.severity in [IncidentSeverity.HIGH, IncidentSeverity.CRITICAL]

    def _summarize_incident_overview(self, incident: Incident) -> Dict:
        return {
            "incident_id": incident.incident_id,
            "category": incident.category.value,
            "severity": incident.severity.value,
            "duration": self._calculate_incident_duration(incident),
            "impact": incident.impact_assessment
        }

    def _conduct_root_cause_analysis(self, incident: Incident) -> Dict:
        return {
            "primary_cause": incident.root_cause or "System configuration error",
            "contributing_factors": [
                "Insufficient monitoring",
                "Delayed detection",
                "Process gaps"
            ],
            "analysis_method": "5 Whys and Fishbone analysis",
            "evidence": "System logs and stakeholder interviews"
        }

    def _analyze_response_effectiveness(self, incident: Incident) -> Dict:
        return {
            "response_time_met": True,  # Based on SLA comparison
            "communication_effectiveness": "Good",
            "mitigation_success": "Effective",
            "areas_for_improvement": [
                "Faster initial detection",
                "Better stakeholder coordination"
            ]
        }

    def _identify_process_improvements(self, incident: Incident) -> List[str]:
        return [
            "Enhanced automated monitoring",
            "Improved escalation procedures",
            "Better stakeholder communication",
            "Regular response training"
        ]

    def _identify_system_improvements(self, incident: Incident) -> List[str]:
        return [
            "Implement additional safeguards",
            "Enhance error handling",
            "Improve system resilience",
            "Better logging and monitoring"
        ]

    def _identify_training_needs(self, incident: Incident) -> List[str]:
        return [
            "Incident response training for all team members",
            "Category-specific response procedures",
            "Stakeholder communication training",
            "Technical skills development"
        ]

    def _recommend_policy_updates(self, incident: Incident) -> List[str]:
        return [
            "Update incident response policy",
            "Enhance escalation procedures",
            "Improve notification requirements",
            "Strengthen compliance processes"
        ]

    def _create_action_items(self, incident: Incident) -> List[Dict]:
        return [
            {
                "action": "Implement monitoring improvements",
                "owner": "Technical Team",
                "due_date": (datetime.now() + timedelta(days=30)).isoformat(),
                "priority": "High"
            },
            {
                "action": "Update response procedures",
                "owner": "Process Team",
                "due_date": (datetime.now() + timedelta(days=14)).isoformat(),
                "priority": "Medium"
            }
        ]

    def _schedule_follow_up_actions(self, incident: Incident) -> Dict:
        return {
            "30_day_review": "Check implementation of immediate improvements",
            "90_day_review": "Assess long-term effectiveness",
            "annual_review": "Include in annual incident response assessment"
        }

    def _get_incident_category_breakdown(self) -> Dict:
        category_counts = {}
        for incident in self.active_incidents.values():
            category = incident.category.value
            category_counts[category] = category_counts.get(category, 0) + 1
        return category_counts

    def _get_incident_severity_distribution(self) -> Dict:
        severity_counts = {}
        for incident in self.active_incidents.values():
            severity = incident.severity.value
            severity_counts[severity] = severity_counts.get(severity, 0) + 1
        return severity_counts

    def _get_top_affected_systems(self) -> List[Dict]:
        system_counts = {}
        for incident in self.active_incidents.values():
            for system in incident.affected_systems:
                system_counts[system] = system_counts.get(system, 0) + 1
        
        return [
            {"system": system, "incident_count": count}
            for system, count in sorted(system_counts.items(), key=lambda x: x[1], reverse=True)[:5]
        ]

    def _identify_trending_issues(self) -> List[str]:
        return [
            "Increase in bias-related incidents",
            "System performance degradation trending up",
            "Privacy concerns growing"
        ]

    def _calculate_sla_compliance(self) -> Dict:
        return {
            "response_time_compliance": "95%",
            "resolution_time_compliance": "87%",
            "notification_compliance": "98%"
        }

    def _identify_improvement_areas(self) -> List[str]:
        return [
            "Reduce average resolution time",
            "Improve early detection capabilities",
            "Enhance automated response procedures",
            "Better cross-team coordination"
        ]

    def _calculate_average_response_time(self) -> str:
        response_times = []
        for incident in self.active_incidents.values():
            if incident.response_time:
                delta = incident.response_time - incident.detection_time
                response_times.append(delta.total_seconds() / 60)  # minutes
        
        if response_times:
            avg = sum(response_times) / len(response_times)
            return f"{avg:.1f} minutes"
        return "N/A"

    def _calculate_average_resolution_time(self) -> str:
        resolution_times = []
        for incident in self.active_incidents.values():
            if incident.resolution_time:
                delta = incident.resolution_time - incident.detection_time
                resolution_times.append(delta.total_seconds() / 3600)  # hours
        
        if resolution_times:
            avg = sum(resolution_times) / len(resolution_times)
            return f"{avg:.1f} hours"
        return "N/A"

    def _calculate_incident_duration(self, incident: Incident) -> str:
        if incident.resolution_time:
            delta = incident.resolution_time - incident.detection_time
            hours = delta.total_seconds() / 3600
            return f"{hours:.1f} hours"
        else:
            delta = datetime.now() - incident.detection_time
            hours = delta.total_seconds() / 3600
            return f"{hours:.1f} hours (ongoing)"