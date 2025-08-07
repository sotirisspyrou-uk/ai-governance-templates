from typing import Dict, List, Optional
from pydantic import BaseModel
from datetime import datetime


class StrategicObjective(BaseModel):
    id: str
    title: str
    description: str
    ai_alignment: str
    success_metrics: List[str]
    timeline: str
    owner: str


class AIStrategyFramework:
    def __init__(self):
        self.objectives: List[StrategicObjective] = []
        self.governance_charter: Dict = {}
        self.accountability_matrix: Dict = {}

    def align_ai_strategy(self, business_objectives: List[Dict]) -> List[StrategicObjective]:
        aligned_objectives = []
        for obj in business_objectives:
            ai_objective = StrategicObjective(
                id=f"ai_{obj['id']}",
                title=f"AI-Enabled {obj['title']}",
                description=f"Leverage AI to achieve: {obj['description']}",
                ai_alignment=self._determine_ai_alignment(obj),
                success_metrics=self._generate_ai_metrics(obj),
                timeline=obj.get('timeline', '12 months'),
                owner=obj.get('owner', 'Chief AI Officer')
            )
            aligned_objectives.append(ai_objective)
        
        self.objectives = aligned_objectives
        return aligned_objectives

    def generate_governance_charter(self, organization_context: Dict) -> Dict:
        charter = {
            "organization": organization_context.get("name", "Organization"),
            "effective_date": datetime.now().isoformat(),
            "purpose": "Establish comprehensive AI governance framework",
            "scope": "All AI systems and applications within the organization",
            "governance_structure": {
                "ai_ethics_committee": {
                    "chair": "Chief Risk Officer",
                    "members": ["CTO", "Legal Counsel", "Chief Privacy Officer", "Head of Data Science"],
                    "meeting_frequency": "Monthly",
                    "responsibilities": [
                        "Review AI system implementations",
                        "Ensure compliance with ethical guidelines",
                        "Approve high-risk AI deployments"
                    ]
                },
                "ai_steering_committee": {
                    "chair": "Chief AI Officer",
                    "members": ["CEO", "CRO", "CTO", "Head of Business Units"],
                    "meeting_frequency": "Quarterly",
                    "responsibilities": [
                        "Set AI strategic direction",
                        "Approve AI investment priorities",
                        "Monitor AI governance effectiveness"
                    ]
                }
            },
            "principles": [
                "Transparency and Explainability",
                "Fairness and Non-discrimination",
                "Privacy and Data Protection",
                "Human Oversight and Control",
                "Robustness and Safety"
            ],
            "compliance_requirements": [
                "EU AI Act compliance",
                "ISO 42001 certification",
                "NIST AI RMF alignment"
            ]
        }
        
        self.governance_charter = charter
        return charter

    def create_accountability_matrix(self) -> Dict:
        matrix = {
            "roles": {
                "Chief AI Officer": {
                    "responsibilities": [
                        "Overall AI strategy and governance",
                        "AI system portfolio management",
                        "Stakeholder communication"
                    ],
                    "accountabilities": [
                        "AI strategic alignment",
                        "Governance framework effectiveness",
                        "Regulatory compliance"
                    ]
                },
                "Chief Risk Officer": {
                    "responsibilities": [
                        "AI risk assessment and management",
                        "Risk governance oversight",
                        "Incident response coordination"
                    ],
                    "accountabilities": [
                        "Enterprise AI risk posture",
                        "Risk mitigation effectiveness",
                        "Incident management"
                    ]
                },
                "Data Protection Officer": {
                    "responsibilities": [
                        "Privacy impact assessments",
                        "Data protection compliance",
                        "Privacy by design implementation"
                    ],
                    "accountabilities": [
                        "GDPR compliance for AI systems",
                        "Privacy risk mitigation",
                        "Data subject rights"
                    ]
                },
                "AI Ethics Committee Chair": {
                    "responsibilities": [
                        "Ethical review processes",
                        "Bias assessment and mitigation",
                        "Fairness evaluation"
                    ],
                    "accountabilities": [
                        "Ethical AI deployment",
                        "Bias prevention and remediation",
                        "Fair AI outcomes"
                    ]
                }
            },
            "escalation_matrix": {
                "level_1": "Project Team Lead",
                "level_2": "Business Unit Head",
                "level_3": "Chief AI Officer",
                "level_4": "CEO/Board"
            }
        }
        
        self.accountability_matrix = matrix
        return matrix

    def assess_strategic_risk(self) -> Dict:
        risk_assessment = {
            "strategic_risks": [
                {
                    "risk": "Regulatory Non-compliance",
                    "impact": "High",
                    "probability": "Medium",
                    "mitigation": "Comprehensive compliance framework implementation"
                },
                {
                    "risk": "AI System Bias",
                    "impact": "High",
                    "probability": "Medium",
                    "mitigation": "Continuous bias monitoring and fairness testing"
                },
                {
                    "risk": "Data Privacy Violations",
                    "impact": "High",
                    "probability": "Low",
                    "mitigation": "Privacy by design and data minimization"
                },
                {
                    "risk": "AI System Failure",
                    "impact": "Medium",
                    "probability": "Medium",
                    "mitigation": "Robust testing and monitoring frameworks"
                }
            ],
            "risk_score": self._calculate_strategic_risk_score(),
            "recommendations": [
                "Implement comprehensive AI governance framework",
                "Establish continuous monitoring and alerting",
                "Regular compliance audits and assessments",
                "Stakeholder training and awareness programs"
            ]
        }
        return risk_assessment

    def _determine_ai_alignment(self, objective: Dict) -> str:
        ai_capabilities = [
            "automation", "prediction", "optimization", "personalization", 
            "natural language processing", "computer vision", "recommendation"
        ]
        
        description_lower = objective['description'].lower()
        for capability in ai_capabilities:
            if capability in description_lower:
                return f"AI {capability} alignment"
        
        return "General AI enhancement"

    def _generate_ai_metrics(self, objective: Dict) -> List[str]:
        base_metrics = [
            "AI system accuracy",
            "Processing efficiency",
            "User satisfaction",
            "Compliance score"
        ]
        
        if "cost" in objective.get('description', '').lower():
            base_metrics.append("Cost reduction percentage")
        if "time" in objective.get('description', '').lower():
            base_metrics.append("Time savings")
        if "quality" in objective.get('description', '').lower():
            base_metrics.append("Quality improvement")
            
        return base_metrics

    def _calculate_strategic_risk_score(self) -> float:
        return 6.5