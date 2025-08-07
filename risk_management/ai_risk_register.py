from typing import Dict, List, Optional
from datetime import datetime, timedelta
from enum import Enum
from pydantic import BaseModel
import json


class RiskLevel(Enum):
    VERY_LOW = 1
    LOW = 2
    MEDIUM = 3
    HIGH = 4
    VERY_HIGH = 5


class RiskCategory(Enum):
    TECHNICAL = "technical"
    ETHICAL = "ethical"
    LEGAL = "legal"
    OPERATIONAL = "operational"
    REPUTATIONAL = "reputational"
    FINANCIAL = "financial"


class RiskStatus(Enum):
    IDENTIFIED = "identified"
    ASSESSED = "assessed"
    MITIGATED = "mitigated"
    MONITORED = "monitored"
    CLOSED = "closed"


class Risk(BaseModel):
    risk_id: str
    title: str
    description: str
    category: RiskCategory
    probability: RiskLevel
    impact: RiskLevel
    risk_score: float
    status: RiskStatus
    owner: str
    identified_date: datetime
    target_mitigation_date: Optional[datetime]
    actual_mitigation_date: Optional[datetime]
    mitigation_strategies: List[str]
    monitoring_metrics: List[str]
    related_systems: List[str]
    regulatory_implications: List[str]


class AIRiskRegister:
    def __init__(self):
        self.risks: Dict[str, Risk] = {}
        self.risk_templates = self._initialize_risk_templates()
        self.scoring_algorithm = self._initialize_scoring_algorithm()
        self.monitoring_alerts = {}

    def generate_risk_register(self, ai_systems: List[Dict]) -> Dict:
        register = {
            "register_id": f"risk_register_{datetime.now().strftime('%Y%m%d')}",
            "created_date": datetime.now().isoformat(),
            "total_systems_assessed": len(ai_systems),
            "risk_summary": self._generate_risk_summary(),
            "high_priority_risks": self._get_high_priority_risks(),
            "mitigation_progress": self._calculate_mitigation_progress(),
            "monitoring_status": self._get_monitoring_status(),
            "regulatory_compliance_risks": self._assess_regulatory_risks(),
            "recommendations": self._generate_risk_recommendations()
        }
        return register

    def assess_ai_system_risks(self, system_info: Dict) -> List[Risk]:
        system_risks = []
        
        # Technical risks assessment
        technical_risks = self._assess_technical_risks(system_info)
        system_risks.extend(technical_risks)
        
        # Ethical risks assessment
        ethical_risks = self._assess_ethical_risks(system_info)
        system_risks.extend(ethical_risks)
        
        # Legal/regulatory risks
        legal_risks = self._assess_legal_risks(system_info)
        system_risks.extend(legal_risks)
        
        # Operational risks
        operational_risks = self._assess_operational_risks(system_info)
        system_risks.extend(operational_risks)
        
        # Add to register
        for risk in system_risks:
            self.risks[risk.risk_id] = risk
            
        return system_risks

    def calculate_risk_score(self, probability: RiskLevel, impact: RiskLevel) -> float:
        base_score = probability.value * impact.value
        
        # Apply weighting factors
        weights = {
            "regulatory_multiplier": 1.5,
            "reputational_multiplier": 1.3,
            "technical_multiplier": 1.2
        }
        
        # Normalize to 0-10 scale
        normalized_score = (base_score / 25) * 10
        
        return round(normalized_score, 2)

    def prioritize_risks(self) -> List[Risk]:
        sorted_risks = sorted(
            self.risks.values(),
            key=lambda r: (r.risk_score, r.probability.value, r.impact.value),
            reverse=True
        )
        return sorted_risks

    def generate_mitigation_strategies(self, risk: Risk) -> List[str]:
        strategies = {
            RiskCategory.TECHNICAL: [
                "Implement robust testing protocols",
                "Deploy continuous monitoring systems",
                "Establish fallback mechanisms",
                "Regular security assessments",
                "Performance optimization"
            ],
            RiskCategory.ETHICAL: [
                "Bias detection and mitigation",
                "Fairness testing across demographics",
                "Transparency and explainability measures",
                "Human oversight implementation",
                "Stakeholder consultation processes"
            ],
            RiskCategory.LEGAL: [
                "Legal compliance review",
                "Regulatory gap analysis",
                "Documentation and audit trails",
                "Privacy impact assessments",
                "Contract and liability reviews"
            ],
            RiskCategory.OPERATIONAL: [
                "Process standardization",
                "Staff training and certification",
                "Incident response procedures",
                "Business continuity planning",
                "Change management protocols"
            ],
            RiskCategory.REPUTATIONAL: [
                "Stakeholder communication strategy",
                "Transparency reporting",
                "Community engagement",
                "Media response planning",
                "Brand protection measures"
            ],
            RiskCategory.FINANCIAL: [
                "Cost-benefit analysis",
                "Budget allocation for risk mitigation",
                "Insurance coverage assessment",
                "ROI optimization",
                "Financial impact modeling"
            ]
        }
        
        base_strategies = strategies.get(risk.category, [])
        
        # Add risk-specific strategies based on severity
        if risk.risk_score >= 7.0:
            base_strategies.extend([
                "Executive escalation protocol",
                "External expert consultation",
                "Accelerated mitigation timeline"
            ])
        
        return base_strategies

    def create_monitoring_system(self, risks: List[Risk]) -> Dict:
        monitoring_config = {
            "monitoring_id": f"risk_monitor_{datetime.now().strftime('%Y%m%d')}",
            "active_risks": len([r for r in risks if r.status != RiskStatus.CLOSED]),
            "monitoring_frequency": self._determine_monitoring_frequency(risks),
            "alert_thresholds": {
                "high_risk_threshold": 7.0,
                "new_risk_alert": True,
                "mitigation_overdue_days": 30,
                "compliance_risk_immediate": True
            },
            "automated_checks": {
                "bias_monitoring": "Daily",
                "performance_degradation": "Real-time",
                "compliance_status": "Weekly",
                "security_vulnerabilities": "Continuous"
            },
            "reporting_schedule": {
                "executive_summary": "Weekly",
                "detailed_risk_report": "Monthly",
                "board_report": "Quarterly",
                "regulatory_filing": "As required"
            },
            "escalation_matrix": {
                "level_1": "Risk Owner",
                "level_2": "Department Head",
                "level_3": "Chief Risk Officer",
                "level_4": "Executive Team",
                "level_5": "Board of Directors"
            }
        }
        
        self.monitoring_alerts = monitoring_config
        return monitoring_config

    def update_risk_status(self, risk_id: str, new_status: RiskStatus, notes: str = "") -> bool:
        if risk_id not in self.risks:
            return False
            
        risk = self.risks[risk_id]
        old_status = risk.status
        risk.status = new_status
        
        # Log status change
        status_change = {
            "timestamp": datetime.now().isoformat(),
            "risk_id": risk_id,
            "old_status": old_status.value,
            "new_status": new_status.value,
            "notes": notes
        }
        
        # Trigger appropriate actions based on status change
        if new_status == RiskStatus.MITIGATED:
            risk.actual_mitigation_date = datetime.now()
        
        return True

    def _initialize_risk_templates(self) -> Dict:
        return {
            "ai_bias_risk": {
                "category": RiskCategory.ETHICAL,
                "base_probability": RiskLevel.MEDIUM,
                "base_impact": RiskLevel.HIGH,
                "indicators": ["demographic_disparity", "protected_class_impact"]
            },
            "data_privacy_risk": {
                "category": RiskCategory.LEGAL,
                "base_probability": RiskLevel.MEDIUM,
                "base_impact": RiskLevel.VERY_HIGH,
                "indicators": ["personal_data_processing", "cross_border_transfer"]
            },
            "model_drift_risk": {
                "category": RiskCategory.TECHNICAL,
                "base_probability": RiskLevel.HIGH,
                "base_impact": RiskLevel.MEDIUM,
                "indicators": ["performance_degradation", "concept_drift"]
            },
            "regulatory_compliance_risk": {
                "category": RiskCategory.LEGAL,
                "base_probability": RiskLevel.MEDIUM,
                "base_impact": RiskLevel.VERY_HIGH,
                "indicators": ["eu_ai_act_requirements", "sector_specific_regulations"]
            }
        }

    def _initialize_scoring_algorithm(self) -> Dict:
        return {
            "base_formula": "probability * impact",
            "category_weights": {
                RiskCategory.LEGAL.value: 1.5,
                RiskCategory.ETHICAL.value: 1.3,
                RiskCategory.REPUTATIONAL.value: 1.3,
                RiskCategory.TECHNICAL.value: 1.2,
                RiskCategory.OPERATIONAL.value: 1.1,
                RiskCategory.FINANCIAL.value: 1.0
            },
            "system_criticality_multiplier": {
                "critical": 1.5,
                "high": 1.3,
                "medium": 1.0,
                "low": 0.8
            }
        }

    def _assess_technical_risks(self, system_info: Dict) -> List[Risk]:
        risks = []
        
        # Model drift risk
        if system_info.get("ml_model_type") in ["supervised", "deep_learning"]:
            drift_risk = Risk(
                risk_id=f"tech_drift_{system_info.get('system_id', 'unknown')}",
                title="Model Performance Drift",
                description="Risk of model performance degradation over time",
                category=RiskCategory.TECHNICAL,
                probability=RiskLevel.HIGH,
                impact=RiskLevel.MEDIUM,
                risk_score=self.calculate_risk_score(RiskLevel.HIGH, RiskLevel.MEDIUM),
                status=RiskStatus.IDENTIFIED,
                owner=system_info.get("technical_owner", "Unknown"),
                identified_date=datetime.now(),
                mitigation_strategies=[],
                monitoring_metrics=["accuracy", "precision", "recall", "f1_score"],
                related_systems=[system_info.get("system_name", "Unknown")],
                regulatory_implications=["EU AI Act Article 15 - Monitoring"]
            )
            risks.append(drift_risk)
        
        # Security vulnerability risk
        security_risk = Risk(
            risk_id=f"tech_security_{system_info.get('system_id', 'unknown')}",
            title="AI System Security Vulnerabilities",
            description="Risk of adversarial attacks or system breaches",
            category=RiskCategory.TECHNICAL,
            probability=RiskLevel.MEDIUM,
            impact=RiskLevel.HIGH,
            risk_score=self.calculate_risk_score(RiskLevel.MEDIUM, RiskLevel.HIGH),
            status=RiskStatus.IDENTIFIED,
            owner=system_info.get("security_owner", "Unknown"),
            identified_date=datetime.now(),
            mitigation_strategies=[],
            monitoring_metrics=["security_incidents", "vulnerability_scans"],
            related_systems=[system_info.get("system_name", "Unknown")],
            regulatory_implications=["NIS2 Directive", "EU AI Act Article 15"]
        )
        risks.append(security_risk)
        
        return risks

    def _assess_ethical_risks(self, system_info: Dict) -> List[Risk]:
        risks = []
        
        # Bias risk assessment
        if system_info.get("processes_personal_data", False):
            bias_risk = Risk(
                risk_id=f"ethical_bias_{system_info.get('system_id', 'unknown')}",
                title="AI System Bias and Discrimination",
                description="Risk of unfair treatment of protected groups",
                category=RiskCategory.ETHICAL,
                probability=RiskLevel.MEDIUM,
                impact=RiskLevel.HIGH,
                risk_score=self.calculate_risk_score(RiskLevel.MEDIUM, RiskLevel.HIGH),
                status=RiskStatus.IDENTIFIED,
                owner=system_info.get("ethics_owner", "Unknown"),
                identified_date=datetime.now(),
                mitigation_strategies=[],
                monitoring_metrics=["demographic_parity", "equalized_odds"],
                related_systems=[system_info.get("system_name", "Unknown")],
                regulatory_implications=["EU AI Act Article 10", "GDPR Article 22"]
            )
            risks.append(bias_risk)
        
        return risks

    def _assess_legal_risks(self, system_info: Dict) -> List[Risk]:
        risks = []
        
        # EU AI Act compliance risk
        if system_info.get("risk_category") in ["high_risk", "unacceptable_risk"]:
            compliance_risk = Risk(
                risk_id=f"legal_euai_{system_info.get('system_id', 'unknown')}",
                title="EU AI Act Compliance Risk",
                description="Risk of non-compliance with EU AI Act requirements",
                category=RiskCategory.LEGAL,
                probability=RiskLevel.MEDIUM,
                impact=RiskLevel.VERY_HIGH,
                risk_score=self.calculate_risk_score(RiskLevel.MEDIUM, RiskLevel.VERY_HIGH),
                status=RiskStatus.IDENTIFIED,
                owner=system_info.get("compliance_owner", "Unknown"),
                identified_date=datetime.now(),
                mitigation_strategies=[],
                monitoring_metrics=["compliance_score", "audit_findings"],
                related_systems=[system_info.get("system_name", "Unknown")],
                regulatory_implications=["EU AI Act - All Articles"]
            )
            risks.append(compliance_risk)
        
        return risks

    def _assess_operational_risks(self, system_info: Dict) -> List[Risk]:
        risks = []
        
        # Operational failure risk
        operational_risk = Risk(
            risk_id=f"ops_failure_{system_info.get('system_id', 'unknown')}",
            title="AI System Operational Failure",
            description="Risk of system downtime or operational disruption",
            category=RiskCategory.OPERATIONAL,
            probability=RiskLevel.MEDIUM,
            impact=RiskLevel.MEDIUM,
            risk_score=self.calculate_risk_score(RiskLevel.MEDIUM, RiskLevel.MEDIUM),
            status=RiskStatus.IDENTIFIED,
            owner=system_info.get("operations_owner", "Unknown"),
            identified_date=datetime.now(),
            mitigation_strategies=[],
            monitoring_metrics=["uptime", "response_time", "error_rate"],
            related_systems=[system_info.get("system_name", "Unknown")],
            regulatory_implications=["Business Continuity Requirements"]
        )
        risks.append(operational_risk)
        
        return risks

    def _generate_risk_summary(self) -> Dict:
        total_risks = len(self.risks)
        if total_risks == 0:
            return {"total_risks": 0, "risk_distribution": {}}
            
        risk_distribution = {}
        for level in RiskLevel:
            count = len([r for r in self.risks.values() if r.risk_score >= level.value * 2])
            risk_distribution[level.name.lower()] = count
            
        return {
            "total_risks": total_risks,
            "risk_distribution": risk_distribution,
            "average_risk_score": sum(r.risk_score for r in self.risks.values()) / total_risks
        }

    def _get_high_priority_risks(self) -> List[Dict]:
        high_priority = [r for r in self.risks.values() if r.risk_score >= 7.0]
        return [
            {
                "risk_id": r.risk_id,
                "title": r.title,
                "risk_score": r.risk_score,
                "status": r.status.value,
                "owner": r.owner
            } for r in high_priority
        ]

    def _calculate_mitigation_progress(self) -> Dict:
        total_risks = len(self.risks)
        if total_risks == 0:
            return {"progress_percentage": 0, "mitigated_risks": 0}
            
        mitigated = len([r for r in self.risks.values() if r.status in [RiskStatus.MITIGATED, RiskStatus.CLOSED]])
        progress = (mitigated / total_risks) * 100
        
        return {
            "progress_percentage": round(progress, 2),
            "mitigated_risks": mitigated,
            "in_progress_risks": len([r for r in self.risks.values() if r.status == RiskStatus.ASSESSED]),
            "identified_risks": len([r for r in self.risks.values() if r.status == RiskStatus.IDENTIFIED])
        }

    def _get_monitoring_status(self) -> Dict:
        return {
            "active_monitors": len(self.monitoring_alerts),
            "alert_status": "Normal",
            "last_assessment": datetime.now().isoformat()
        }

    def _assess_regulatory_risks(self) -> List[str]:
        return [
            "EU AI Act compliance gaps",
            "GDPR privacy violations",
            "Sector-specific regulatory requirements",
            "International regulatory divergence"
        ]

    def _generate_risk_recommendations(self) -> List[str]:
        return [
            "Implement comprehensive risk monitoring system",
            "Prioritize high-risk mitigation strategies",
            "Enhance regulatory compliance processes",
            "Establish regular risk review cycles",
            "Improve stakeholder communication on risks"
        ]

    def _determine_monitoring_frequency(self, risks: List[Risk]) -> Dict:
        high_risk_count = len([r for r in risks if r.risk_score >= 7.0])
        
        if high_risk_count > 5:
            return {"frequency": "Daily", "rationale": "High number of critical risks"}
        elif high_risk_count > 0:
            return {"frequency": "Weekly", "rationale": "Some critical risks identified"}
        else:
            return {"frequency": "Monthly", "rationale": "Low to moderate risk profile"}