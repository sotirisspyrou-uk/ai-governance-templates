from typing import Dict, List, Optional, Tuple
from datetime import datetime, timedelta
from enum import Enum
from pydantic import BaseModel
import json


class AISystemRiskLevel(Enum):
    UNACCEPTABLE = "unacceptable"
    HIGH_RISK = "high_risk"
    LIMITED_RISK = "limited_risk" 
    MINIMAL_RISK = "minimal_risk"


class EUAIActArticle(Enum):
    ARTICLE_5 = "article_5"  # Prohibited practices
    ARTICLE_6 = "article_6"  # Classification rules for high-risk AI systems
    ARTICLE_8 = "article_8"  # Conformity assessment
    ARTICLE_9 = "article_9"  # Risk management system
    ARTICLE_10 = "article_10"  # Data and data governance
    ARTICLE_11 = "article_11"  # Technical documentation
    ARTICLE_12 = "article_12"  # Record-keeping
    ARTICLE_13 = "article_13"  # Transparency and provision of information
    ARTICLE_14 = "article_14"  # Human oversight
    ARTICLE_15 = "article_15"  # Accuracy, robustness and cybersecurity


class ComplianceStatus(Enum):
    COMPLIANT = "compliant"
    NON_COMPLIANT = "non_compliant"
    PARTIALLY_COMPLIANT = "partially_compliant"
    NOT_ASSESSED = "not_assessed"


class AISystemClassification(BaseModel):
    system_id: str
    system_name: str
    risk_level: AISystemRiskLevel
    classification_rationale: str
    applicable_annexes: List[str]
    high_risk_categories: List[str]
    compliance_requirements: List[str]
    conformity_assessment_required: bool
    ce_marking_required: bool


class EUAIActCompliance:
    def __init__(self):
        self.classification_rules = self._initialize_classification_rules()
        self.compliance_requirements = self._initialize_compliance_requirements()
        self.prohibited_practices = self._initialize_prohibited_practices()
        self.high_risk_categories = self._initialize_high_risk_categories()

    def classify_ai_system(self, system_data: Dict) -> AISystemClassification:
        """Automatically classify AI system according to EU AI Act risk levels"""
        
        # Check for unacceptable risk practices
        if self._is_unacceptable_risk(system_data):
            risk_level = AISystemRiskLevel.UNACCEPTABLE
            rationale = "System uses prohibited AI practices under Article 5"
            applicable_annexes = []
            high_risk_cats = []
            conformity_required = False
            ce_required = False
        
        # Check for high-risk classification
        elif self._is_high_risk_system(system_data):
            risk_level = AISystemRiskLevel.HIGH_RISK
            rationale = "System falls under high-risk categories in Annex III"
            applicable_annexes = self._determine_applicable_annexes(system_data)
            high_risk_cats = self._identify_high_risk_categories(system_data)
            conformity_required = True
            ce_required = True
            
        # Check for limited risk
        elif self._is_limited_risk_system(system_data):
            risk_level = AISystemRiskLevel.LIMITED_RISK
            rationale = "System requires transparency obligations under Article 52"
            applicable_annexes = []
            high_risk_cats = []
            conformity_required = False
            ce_required = False
            
        # Default to minimal risk
        else:
            risk_level = AISystemRiskLevel.MINIMAL_RISK
            rationale = "System does not fall under specific regulatory requirements"
            applicable_annexes = []
            high_risk_cats = []
            conformity_required = False
            ce_required = False

        compliance_reqs = self._get_compliance_requirements(risk_level)

        return AISystemClassification(
            system_id=system_data.get("system_id", "unknown"),
            system_name=system_data.get("name", "Unknown System"),
            risk_level=risk_level,
            classification_rationale=rationale,
            applicable_annexes=applicable_annexes,
            high_risk_categories=high_risk_cats,
            compliance_requirements=compliance_reqs,
            conformity_assessment_required=conformity_required,
            ce_marking_required=ce_required
        )

    def generate_compliance_checklist(self, classification: AISystemClassification) -> Dict:
        """Generate detailed compliance checklist based on AI system classification"""
        
        checklist = {
            "checklist_id": f"eu_ai_act_{classification.system_id}_{datetime.now().strftime('%Y%m%d')}",
            "system_name": classification.system_name,
            "risk_level": classification.risk_level.value,
            "generated_date": datetime.now().isoformat(),
            "compliance_deadline": self._calculate_compliance_deadline(),
            "requirements": self._generate_detailed_requirements(classification),
            "documentation_needed": self._identify_required_documentation(classification),
            "assessment_procedures": self._define_assessment_procedures(classification),
            "ongoing_obligations": self._define_ongoing_obligations(classification),
            "compliance_score": 0,
            "completion_status": "Not Started"
        }

        return checklist

    def assess_compliance_gaps(self, system_data: Dict, current_controls: List[Dict]) -> Dict:
        """Analyze gaps between current implementation and EU AI Act requirements"""
        
        classification = self.classify_ai_system(system_data)
        required_controls = self._get_required_controls(classification)
        
        gap_analysis = {
            "analysis_id": f"gap_analysis_{classification.system_id}_{datetime.now().strftime('%Y%m%d')}",
            "system_name": classification.system_name,
            "analysis_date": datetime.now().isoformat(),
            "current_compliance_level": self._assess_current_compliance(current_controls, required_controls),
            "identified_gaps": self._identify_compliance_gaps(current_controls, required_controls),
            "critical_gaps": self._identify_critical_gaps(current_controls, required_controls),
            "remediation_plan": self._create_remediation_plan(current_controls, required_controls),
            "implementation_timeline": self._create_implementation_timeline(classification.risk_level),
            "resource_requirements": self._estimate_compliance_resources(classification),
            "risk_assessment": self._assess_non_compliance_risks(classification)
        }

        return gap_analysis

    def prepare_ce_marking_documentation(self, classification: AISystemClassification, system_data: Dict) -> Dict:
        """Prepare documentation package for CE marking process"""
        
        if not classification.ce_marking_required:
            return {"message": "CE marking not required for this system"}

        documentation_package = {
            "package_id": f"ce_marking_{classification.system_id}",
            "system_name": classification.system_name,
            "preparation_date": datetime.now().isoformat(),
            "eu_declaration_of_conformity": self._generate_eu_declaration(classification, system_data),
            "technical_documentation": self._compile_technical_documentation(classification, system_data),
            "risk_management_documentation": self._compile_risk_management_docs(classification, system_data),
            "quality_management_system": self._document_quality_management(classification, system_data),
            "conformity_assessment_procedure": self._define_conformity_assessment(classification),
            "post_market_monitoring_plan": self._create_post_market_monitoring_plan(classification),
            "instructions_for_use": self._generate_instructions_for_use(classification, system_data),
            "ce_marking_guidelines": self._provide_ce_marking_guidelines()
        }

        return documentation_package

    def create_compliance_monitoring_system(self, ai_systems: List[Dict]) -> Dict:
        """Create ongoing compliance monitoring and reporting system"""
        
        monitoring_system = {
            "monitoring_id": f"eu_ai_act_monitoring_{datetime.now().strftime('%Y%m%d')}",
            "systems_monitored": len(ai_systems),
            "monitoring_framework": {
                "continuous_monitoring": {
                    "high_risk_systems": "Real-time monitoring of performance and bias metrics",
                    "limited_risk_systems": "Quarterly transparency compliance checks",
                    "all_systems": "Annual compliance review and gap assessment"
                },
                "reporting_schedule": {
                    "internal_reports": "Monthly compliance dashboard updates",
                    "management_reports": "Quarterly compliance summary to board",
                    "regulatory_reports": "Annual compliance report to authorities",
                    "incident_reports": "Immediate notification of serious incidents"
                },
                "alert_system": {
                    "compliance_violations": "Immediate alert to legal and compliance teams",
                    "performance_degradation": "Alert when AI system performance drops below thresholds",
                    "bias_detection": "Immediate alert for detected algorithmic bias",
                    "regulatory_changes": "Alert when new EU AI Act guidance is published"
                }
            },
            "automated_checks": self._define_automated_compliance_checks(),
            "audit_preparation": self._prepare_audit_framework(),
            "stakeholder_communication": self._define_stakeholder_communication_plan()
        }

        return monitoring_system

    def generate_regulatory_impact_assessment(self, system_data: Dict) -> Dict:
        """Assess regulatory impact and requirements for AI system"""
        
        classification = self.classify_ai_system(system_data)
        
        impact_assessment = {
            "assessment_id": f"regulatory_impact_{classification.system_id}",
            "system_name": classification.system_name,
            "assessment_date": datetime.now().isoformat(),
            "regulatory_scope": {
                "eu_ai_act_applicable": True,
                "risk_classification": classification.risk_level.value,
                "geographical_scope": system_data.get("deployment_regions", ["EU"]),
                "sector_specific_rules": self._identify_sector_specific_requirements(system_data)
            },
            "compliance_obligations": {
                "mandatory_requirements": self._list_mandatory_requirements(classification),
                "optional_best_practices": self._list_best_practices(classification),
                "ongoing_obligations": self._list_ongoing_obligations(classification)
            },
            "business_impact": {
                "compliance_costs": self._estimate_compliance_costs(classification),
                "implementation_timeline": self._estimate_implementation_timeline(classification),
                "operational_changes": self._identify_operational_changes(classification),
                "competitive_implications": self._assess_competitive_implications(classification)
            },
            "risk_mitigation": {
                "regulatory_risks": self._identify_regulatory_risks(classification),
                "mitigation_strategies": self._propose_mitigation_strategies(classification),
                "contingency_plans": self._develop_contingency_plans(classification)
            },
            "recommendations": self._generate_regulatory_recommendations(classification)
        }

        return impact_assessment

    def _initialize_classification_rules(self) -> Dict:
        return {
            "prohibited_practices": [
                "Subliminal techniques beyond consciousness",
                "Exploitation of vulnerabilities (age, disability, social/economic circumstances)",
                "Social scoring by public authorities",
                "Real-time remote biometric identification in public spaces"
            ],
            "high_risk_categories": [
                "Biometric identification and categorisation",
                "Management of critical infrastructure",
                "Education and vocational training",
                "Employment, worker management, and self-employment",
                "Access to essential services",
                "Law enforcement",
                "Migration, asylum and border control",
                "Administration of justice and democratic processes"
            ],
            "limited_risk_indicators": [
                "Interaction with natural persons",
                "Emotion recognition",
                "Biometric categorisation",
                "Content generation (deepfakes)"
            ]
        }

    def _initialize_compliance_requirements(self) -> Dict:
        return {
            AISystemRiskLevel.HIGH_RISK.value: [
                "Risk management system (Article 9)",
                "Data governance and quality (Article 10)", 
                "Technical documentation (Article 11)",
                "Record-keeping (Article 12)",
                "Transparency and information provision (Article 13)",
                "Human oversight (Article 14)",
                "Accuracy, robustness and cybersecurity (Article 15)",
                "Conformity assessment procedure",
                "CE marking",
                "Registration in EU database"
            ],
            AISystemRiskLevel.LIMITED_RISK.value: [
                "Transparency obligations (Article 52)",
                "Information to users about AI interaction",
                "Clear disclosure of AI-generated content"
            ],
            AISystemRiskLevel.MINIMAL_RISK.value: [
                "Voluntary codes of conduct",
                "Best practice implementation"
            ],
            AISystemRiskLevel.UNACCEPTABLE.value: [
                "Prohibition of deployment and use",
                "Immediate cessation of operations"
            ]
        }

    def _initialize_prohibited_practices(self) -> List[str]:
        return [
            "AI systems that deploy subliminal techniques beyond consciousness",
            "AI systems that exploit vulnerabilities of specific groups",
            "AI systems for social scoring by public authorities", 
            "Real-time remote biometric identification in publicly accessible spaces"
        ]

    def _initialize_high_risk_categories(self) -> Dict:
        return {
            "biometric": [
                "Remote biometric identification systems",
                "Biometric categorisation systems"
            ],
            "infrastructure": [
                "Safety components in road traffic management",
                "Water, gas, heating, electricity supply management"
            ],
            "education": [
                "AI systems for educational/vocational training assessment",
                "AI systems for admission or assignment to educational institutions"
            ],
            "employment": [
                "AI systems for recruitment and personnel selection",
                "AI systems for work performance evaluation",
                "AI systems for promotion and termination decisions"
            ],
            "essential_services": [
                "AI systems for credit scoring and creditworthiness evaluation",
                "AI systems for risk assessment and pricing of insurance"
            ],
            "law_enforcement": [
                "AI systems for individual risk assessment by law enforcement",
                "AI systems for detection of deep fakes",
                "AI systems for evaluation of reliability of evidence"
            ]
        }

    def _is_unacceptable_risk(self, system_data: Dict) -> bool:
        """Check if system uses prohibited AI practices"""
        
        description = system_data.get("description", "").lower()
        use_case = system_data.get("use_case", "").lower()
        
        prohibited_indicators = [
            "subliminal",
            "social scoring",
            "real-time biometric identification",
            "exploit vulnerabilities"
        ]
        
        for indicator in prohibited_indicators:
            if indicator in description or indicator in use_case:
                return True
                
        return False

    def _is_high_risk_system(self, system_data: Dict) -> bool:
        """Check if system falls under high-risk categories"""
        
        use_case = system_data.get("use_case", "").lower()
        sector = system_data.get("sector", "").lower()
        
        high_risk_indicators = [
            "biometric", "identification", "categorisation",
            "infrastructure", "critical", "safety",
            "education", "training", "assessment",
            "employment", "recruitment", "hiring",
            "credit", "insurance", "essential services",
            "law enforcement", "border control"
        ]
        
        for indicator in high_risk_indicators:
            if indicator in use_case or indicator in sector:
                return True
                
        return False

    def _is_limited_risk_system(self, system_data: Dict) -> bool:
        """Check if system requires transparency obligations"""
        
        features = system_data.get("features", [])
        interactions = system_data.get("user_interactions", "").lower()
        
        limited_risk_indicators = [
            "chatbot", "virtual assistant", "human interaction",
            "emotion recognition", "deepfake", "content generation"
        ]
        
        for indicator in limited_risk_indicators:
            if indicator in interactions or indicator in str(features).lower():
                return True
                
        return False

    def _determine_applicable_annexes(self, system_data: Dict) -> List[str]:
        """Identify which EU AI Act annexes apply to the system"""
        
        applicable_annexes = []
        use_case = system_data.get("use_case", "").lower()
        
        # Annex III - High-risk AI systems
        if self._is_high_risk_system(system_data):
            applicable_annexes.append("Annex III - High-risk AI systems")
            
        # Annex IV - Technical documentation
        if self._is_high_risk_system(system_data):
            applicable_annexes.append("Annex IV - Technical documentation")
            
        # Annex VIII - Conformity assessment
        if self._is_high_risk_system(system_data):
            applicable_annexes.append("Annex VIII - Conformity assessment")
            
        return applicable_annexes

    def _identify_high_risk_categories(self, system_data: Dict) -> List[str]:
        """Identify specific high-risk categories that apply"""
        
        categories = []
        use_case = system_data.get("use_case", "").lower()
        
        category_mapping = {
            "biometric": ["biometric", "identification", "recognition"],
            "infrastructure": ["infrastructure", "critical", "safety"],
            "education": ["education", "training", "learning", "assessment"],
            "employment": ["employment", "recruitment", "hiring", "hr"],
            "essential_services": ["credit", "insurance", "banking", "finance"],
            "law_enforcement": ["law enforcement", "police", "security"]
        }
        
        for category, keywords in category_mapping.items():
            for keyword in keywords:
                if keyword in use_case:
                    categories.append(category)
                    break
                    
        return categories

    def _get_compliance_requirements(self, risk_level: AISystemRiskLevel) -> List[str]:
        """Get compliance requirements based on risk level"""
        return self.compliance_requirements.get(risk_level.value, [])

    def _calculate_compliance_deadline(self) -> str:
        """Calculate compliance deadline based on EU AI Act timeline"""
        # EU AI Act becomes applicable August 2, 2024 for prohibited practices
        # February 2, 2025 for general-purpose AI models
        # August 2, 2026 for high-risk systems
        
        high_risk_deadline = datetime(2026, 8, 2)
        return high_risk_deadline.isoformat()

    def _generate_detailed_requirements(self, classification: AISystemClassification) -> List[Dict]:
        """Generate detailed compliance requirements with implementation guidance"""
        
        requirements = []
        base_requirements = self._get_compliance_requirements(classification.risk_level)
        
        requirement_details = {
            "Risk management system (Article 9)": {
                "description": "Establish and maintain risk management system",
                "implementation": [
                    "Identify and analyze known and foreseeable risks",
                    "Estimate and evaluate risks that may emerge",
                    "Adopt suitable risk management measures",
                    "Test the AI system and document results"
                ],
                "deliverables": ["Risk management plan", "Risk assessment documentation"],
                "timeline": "90 days"
            },
            "Data governance and quality (Article 10)": {
                "description": "Ensure appropriate data governance and quality",
                "implementation": [
                    "Implement data governance practices",
                    "Examine and assess training data quality",
                    "Apply data preparation and processing techniques",
                    "Document data lineage and quality measures"
                ],
                "deliverables": ["Data governance framework", "Data quality documentation"],
                "timeline": "60 days"
            },
            "Technical documentation (Article 11)": {
                "description": "Prepare comprehensive technical documentation",
                "implementation": [
                    "Document AI system design and development",
                    "Record training and testing procedures",
                    "Document risk management measures",
                    "Maintain up-to-date documentation"
                ],
                "deliverables": ["Technical documentation package"],
                "timeline": "45 days"
            }
        }
        
        for req in base_requirements:
            if req in requirement_details:
                requirements.append({
                    "requirement": req,
                    **requirement_details[req]
                })
            else:
                requirements.append({
                    "requirement": req,
                    "description": f"Implement {req}",
                    "implementation": ["Review requirement details", "Implement necessary measures"],
                    "deliverables": [f"{req} implementation"],
                    "timeline": "30 days"
                })
                
        return requirements

    def _identify_required_documentation(self, classification: AISystemClassification) -> List[str]:
        """Identify all documentation required for compliance"""
        
        base_docs = [
            "System description and intended purpose",
            "Risk assessment and management documentation",
            "Data governance and quality documentation"
        ]
        
        if classification.risk_level == AISystemRiskLevel.HIGH_RISK:
            base_docs.extend([
                "Technical documentation per Annex IV",
                "EU Declaration of Conformity",
                "Quality management system documentation",
                "Post-market monitoring plan",
                "Instructions for use",
                "Conformity assessment procedure documentation"
            ])
            
        return base_docs

    def _define_assessment_procedures(self, classification: AISystemClassification) -> List[str]:
        """Define conformity assessment procedures required"""
        
        if classification.risk_level == AISystemRiskLevel.HIGH_RISK:
            return [
                "Internal control procedure (Annex VI)",
                "Quality assurance procedure (Annex VII)", 
                "Third-party assessment (if applicable)",
                "Notified body involvement (if required)"
            ]
        else:
            return ["Self-assessment against applicable requirements"]

    def _define_ongoing_obligations(self, classification: AISystemClassification) -> List[str]:
        """Define ongoing compliance obligations"""
        
        base_obligations = [
            "Monitor AI system performance",
            "Report serious incidents",
            "Maintain compliance documentation"
        ]
        
        if classification.risk_level == AISystemRiskLevel.HIGH_RISK:
            base_obligations.extend([
                "Continuous monitoring and updating",
                "Annual compliance review",
                "Database registration updates",
                "Post-market surveillance"
            ])
            
        return base_obligations

    def _get_required_controls(self, classification: AISystemClassification) -> List[str]:
        """Get required controls based on classification"""
        
        base_controls = [
            "Documentation management",
            "Risk assessment procedures",
            "Performance monitoring"
        ]
        
        if classification.risk_level == AISystemRiskLevel.HIGH_RISK:
            base_controls.extend([
                "Quality management system",
                "Human oversight mechanisms",
                "Bias detection and mitigation",
                "Cybersecurity measures",
                "Data governance framework"
            ])
            
        return base_controls

    def _assess_current_compliance(self, current_controls: List[Dict], required_controls: List[str]) -> str:
        """Assess current compliance level"""
        
        implemented_controls = [control.get("name", "") for control in current_controls]
        compliance_score = 0
        
        for required_control in required_controls:
            if any(required_control.lower() in impl.lower() for impl in implemented_controls):
                compliance_score += 1
                
        compliance_percentage = (compliance_score / len(required_controls)) * 100 if required_controls else 0
        
        if compliance_percentage >= 90:
            return "High compliance"
        elif compliance_percentage >= 70:
            return "Moderate compliance"
        elif compliance_percentage >= 50:
            return "Low compliance"
        else:
            return "Non-compliant"

    def _identify_compliance_gaps(self, current_controls: List[Dict], required_controls: List[str]) -> List[Dict]:
        """Identify specific compliance gaps"""
        
        gaps = []
        implemented_controls = [control.get("name", "").lower() for control in current_controls]
        
        for required_control in required_controls:
            if not any(required_control.lower() in impl for impl in implemented_controls):
                gaps.append({
                    "gap": required_control,
                    "severity": "High" if "risk" in required_control.lower() or "security" in required_control.lower() else "Medium",
                    "effort": "High" if "system" in required_control.lower() else "Medium"
                })
                
        return gaps

    def _identify_critical_gaps(self, current_controls: List[Dict], required_controls: List[str]) -> List[str]:
        """Identify critical compliance gaps requiring immediate attention"""
        
        critical_keywords = ["risk", "security", "human oversight", "bias", "governance"]
        critical_gaps = []
        implemented_controls = [control.get("name", "").lower() for control in current_controls]
        
        for required_control in required_controls:
            if not any(required_control.lower() in impl for impl in implemented_controls):
                if any(keyword in required_control.lower() for keyword in critical_keywords):
                    critical_gaps.append(required_control)
                    
        return critical_gaps

    def _create_remediation_plan(self, current_controls: List[Dict], required_controls: List[str]) -> Dict:
        """Create detailed remediation plan for compliance gaps"""
        
        gaps = self._identify_compliance_gaps(current_controls, required_controls)
        
        return {
            "total_gaps": len(gaps),
            "critical_gaps": len(self._identify_critical_gaps(current_controls, required_controls)),
            "phases": {
                "phase_1": {
                    "timeline": "0-30 days",
                    "focus": "Critical gaps and risk management",
                    "activities": ["Implement risk management system", "Establish data governance"]
                },
                "phase_2": {
                    "timeline": "30-90 days", 
                    "focus": "Documentation and quality systems",
                    "activities": ["Complete technical documentation", "Implement quality management"]
                },
                "phase_3": {
                    "timeline": "90-180 days",
                    "focus": "Monitoring and continuous improvement",
                    "activities": ["Deploy monitoring systems", "Complete conformity assessment"]
                }
            }
        }

    def _create_implementation_timeline(self, risk_level: AISystemRiskLevel) -> Dict:
        """Create implementation timeline based on risk level"""
        
        base_timeline = {
            "preparation_phase": "30 days",
            "implementation_phase": "90 days",
            "testing_phase": "30 days",
            "documentation_phase": "30 days"
        }
        
        if risk_level == AISystemRiskLevel.HIGH_RISK:
            base_timeline.update({
                "conformity_assessment": "60 days",
                "ce_marking_process": "30 days",
                "market_entry": "After compliance verification"
            })
            
        return base_timeline

    def _estimate_compliance_resources(self, classification: AISystemClassification) -> Dict:
        """Estimate resources required for compliance"""
        
        base_resources = {
            "personnel": {
                "legal_expertise": "1 FTE for 6 months",
                "technical_expertise": "2 FTE for 3 months",
                "project_management": "0.5 FTE for 6 months"
            },
            "budget": {
                "internal_costs": 150000,
                "external_consultants": 75000,
                "tools_and_systems": 50000
            }
        }
        
        if classification.risk_level == AISystemRiskLevel.HIGH_RISK:
            base_resources["budget"]["conformity_assessment"] = 100000
            base_resources["budget"]["ongoing_monitoring"] = 25000
            
        return base_resources

    def _assess_non_compliance_risks(self, classification: AISystemClassification) -> List[Dict]:
        """Assess risks of non-compliance"""
        
        risks = [
            {
                "risk": "Regulatory fines and penalties",
                "impact": "High",
                "likelihood": "High" if classification.risk_level == AISystemRiskLevel.HIGH_RISK else "Medium",
                "potential_cost": "Up to €30M or 6% of global turnover"
            },
            {
                "risk": "Market access restrictions",
                "impact": "High",
                "likelihood": "High",
                "potential_cost": "Loss of EU market access"
            },
            {
                "risk": "Reputational damage",
                "impact": "Medium",
                "likelihood": "Medium",
                "potential_cost": "Brand value impact"
            }
        ]
        
        return risks

    def _generate_eu_declaration(self, classification: AISystemClassification, system_data: Dict) -> Dict:
        """Generate EU Declaration of Conformity"""
        
        return {
            "declaration_id": f"eu_doc_{classification.system_id}",
            "product_identification": {
                "name": classification.system_name,
                "model": system_data.get("model_version", "1.0"),
                "serial_number": system_data.get("serial_number", "N/A"),
                "manufacturer": system_data.get("manufacturer", "Organization")
            },
            "conformity_statement": f"This AI system conforms to the requirements of Regulation (EU) 2024/1689 (AI Act)",
            "applicable_standards": [
                "EN ISO/IEC 23053:2022",
                "EN ISO/IEC 23094-1:2023",
                "Additional harmonized standards as applicable"
            ],
            "notified_body": system_data.get("notified_body", "N/A"),
            "declaration_date": datetime.now().isoformat(),
            "authorized_representative": system_data.get("eu_representative", "To be appointed")
        }

    def _compile_technical_documentation(self, classification: AISystemClassification, system_data: Dict) -> List[str]:
        """Compile required technical documentation"""
        
        return [
            "General description of AI system and intended purpose",
            "Detailed description of AI system elements and development process", 
            "Risk management system documentation",
            "Data governance and training data documentation",
            "Design specifications and architecture",
            "Human oversight measures",
            "Cybersecurity and accuracy measures",
            "Quality management system",
            "Conformity assessment procedure"
        ]

    def _compile_risk_management_docs(self, classification: AISystemClassification, system_data: Dict) -> List[str]:
        """Compile risk management documentation"""
        
        return [
            "Risk management methodology",
            "Risk identification and analysis",
            "Risk evaluation and treatment",
            "Residual risk assessment",
            "Risk monitoring and review procedures"
        ]

    def _document_quality_management(self, classification: AISystemClassification, system_data: Dict) -> Dict:
        """Document quality management system requirements"""
        
        return {
            "quality_policy": "Organizational commitment to AI system quality",
            "quality_objectives": "Specific, measurable quality targets",
            "quality_procedures": [
                "Design and development procedures",
                "Risk management procedures", 
                "Data governance procedures",
                "Testing and validation procedures",
                "Corrective and preventive action procedures"
            ],
            "quality_records": [
                "Design review records",
                "Testing and validation records",
                "Risk assessment records",
                "Corrective action records"
            ]
        }

    def _define_conformity_assessment(self, classification: AISystemClassification) -> Dict:
        """Define conformity assessment procedure"""
        
        return {
            "procedure_type": "Internal control (Annex VI)" if classification.risk_level == AISystemRiskLevel.HIGH_RISK else "Self-assessment",
            "assessment_steps": [
                "Technical documentation preparation",
                "Quality management system implementation",
                "Conformity verification testing",
                "Risk assessment validation",
                "Declaration of conformity preparation"
            ],
            "required_documentation": self._identify_required_documentation(classification),
            "testing_requirements": [
                "Performance testing",
                "Bias testing", 
                "Robustness testing",
                "Cybersecurity testing"
            ]
        }

    def _create_post_market_monitoring_plan(self, classification: AISystemClassification) -> Dict:
        """Create post-market monitoring plan"""
        
        return {
            "monitoring_objectives": [
                "Ensure continued conformity with requirements",
                "Identify and address emerging risks",
                "Monitor AI system performance",
                "Collect user feedback and incident reports"
            ],
            "monitoring_activities": [
                "Performance monitoring and analysis",
                "Incident reporting and investigation",
                "User feedback collection and analysis",
                "Market surveillance cooperation"
            ],
            "reporting_requirements": [
                "Serious incident reporting to authorities",
                "Annual monitoring report preparation",
                "Database registration updates",
                "Corrective action documentation"
            ]
        }

    def _generate_instructions_for_use(self, classification: AISystemClassification, system_data: Dict) -> Dict:
        """Generate instructions for use"""
        
        return {
            "system_identification": classification.system_name,
            "intended_purpose": system_data.get("intended_purpose", "AI system for specified use case"),
            "user_instructions": [
                "Installation and setup procedures",
                "Operating instructions and guidelines",
                "Maintenance and update procedures",
                "Troubleshooting and support information"
            ],
            "limitations_and_restrictions": [
                "Specified operating conditions",
                "Known limitations and constraints", 
                "Prohibited uses and applications",
                "Risk mitigation measures for users"
            ],
            "human_oversight_requirements": [
                "Required human oversight measures",
                "User training and competency requirements",
                "Decision-making responsibilities",
                "Override and intervention procedures"
            ]
        }

    def _provide_ce_marking_guidelines(self) -> Dict:
        """Provide CE marking application guidelines"""
        
        return {
            "marking_requirements": {
                "visibility": "Clearly visible, legible, and indelible",
                "size": "At least 5mm height",
                "placement": "On AI system or packaging",
                "format": "Official CE marking format only"
            },
            "application_procedure": [
                "Complete conformity assessment",
                "Prepare EU Declaration of Conformity",
                "Apply CE marking to system",
                "Register in EU database",
                "Maintain documentation"
            ],
            "ongoing_obligations": [
                "Maintain technical documentation",
                "Monitor system performance",
                "Report serious incidents", 
                "Update registration as needed"
            ]
        }

    def _define_automated_compliance_checks(self) -> Dict:
        """Define automated compliance monitoring checks"""
        
        return {
            "performance_monitoring": {
                "frequency": "Continuous",
                "metrics": ["accuracy", "bias_metrics", "response_time"],
                "thresholds": "System-specific performance thresholds",
                "alerts": "Immediate alert on threshold breach"
            },
            "bias_monitoring": {
                "frequency": "Daily",
                "methods": ["statistical_parity", "equalized_odds"],
                "scope": "All protected attributes",
                "alerts": "Immediate alert on bias detection"
            },
            "security_monitoring": {
                "frequency": "Continuous", 
                "scope": ["vulnerability_scans", "access_monitoring", "data_integrity"],
                "integration": "SIEM system integration",
                "alerts": "Real-time security alerts"
            },
            "documentation_compliance": {
                "frequency": "Monthly",
                "checks": ["document_completeness", "version_control", "approval_status"],
                "automation": "Document management system integration"
            }
        }

    def _prepare_audit_framework(self) -> Dict:
        """Prepare framework for compliance audits"""
        
        return {
            "audit_types": {
                "internal_audits": "Quarterly compliance audits",
                "external_audits": "Annual third-party audits",
                "regulatory_inspections": "Ad-hoc regulatory inspections"
            },
            "audit_preparation": [
                "Documentation review and organization",
                "Evidence collection and validation",
                "Process walkthrough preparation",
                "Staff interview preparation"
            ],
            "audit_support": {
                "documentation_portal": "Centralized audit documentation access",
                "process_maps": "Visual compliance process representations",
                "evidence_management": "Systematic evidence organization",
                "response_procedures": "Audit response and follow-up procedures"
            }
        }

    def _define_stakeholder_communication_plan(self) -> Dict:
        """Define stakeholder communication plan for compliance"""
        
        return {
            "internal_stakeholders": {
                "executive_team": "Monthly compliance dashboards",
                "legal_team": "Real-time compliance alerts",
                "development_teams": "Weekly compliance updates",
                "operations_team": "Daily operational compliance metrics"
            },
            "external_stakeholders": {
                "regulators": "Annual compliance reports and incident notifications",
                "customers": "Transparency reports and service updates",
                "partners": "Quarterly compliance status updates",
                "auditors": "Audit preparation and response communications"
            },
            "communication_channels": {
                "compliance_portal": "Centralized compliance information",
                "automated_reporting": "System-generated compliance reports",
                "alert_systems": "Real-time compliance notifications",
                "documentation_system": "Compliance documentation access"
            }
        }

    def _identify_sector_specific_requirements(self, system_data: Dict) -> List[str]:
        """Identify sector-specific regulatory requirements"""
        
        sector = system_data.get("sector", "").lower()
        
        sector_requirements = {
            "healthcare": ["Medical Device Regulation (MDR)", "GDPR health data provisions"],
            "finance": ["PCI DSS", "Basel III", "MiFID II"],
            "automotive": ["UN Regulation No. 157", "ISO 26262"],
            "aviation": ["EASA AI roadmap", "DO-178C"],
            "telecommunications": ["ePrivacy Regulation", "NIS2 Directive"]
        }
        
        return sector_requirements.get(sector, ["General data protection requirements"])

    def _list_mandatory_requirements(self, classification: AISystemClassification) -> List[str]:
        """List mandatory compliance requirements"""
        return self._get_compliance_requirements(classification.risk_level)

    def _list_best_practices(self, classification: AISystemClassification) -> List[str]:
        """List optional best practices"""
        
        return [
            "Voluntary codes of conduct adoption",
            "Industry best practices implementation",
            "Additional transparency measures",
            "Enhanced user consultation processes",
            "Proactive bias mitigation measures"
        ]

    def _list_ongoing_obligations(self, classification: AISystemClassification) -> List[str]:
        """List ongoing compliance obligations"""
        return self._define_ongoing_obligations(classification)

    def _estimate_compliance_costs(self, classification: AISystemClassification) -> Dict:
        """Estimate compliance implementation costs"""
        
        base_costs = {
            "initial_compliance": {
                AISystemRiskLevel.HIGH_RISK.value: 500000,
                AISystemRiskLevel.LIMITED_RISK.value: 100000,
                AISystemRiskLevel.MINIMAL_RISK.value: 25000
            },
            "ongoing_costs": {
                AISystemRiskLevel.HIGH_RISK.value: 150000,
                AISystemRiskLevel.LIMITED_RISK.value: 30000,
                AISystemRiskLevel.MINIMAL_RISK.value: 10000
            }
        }
        
        risk_level = classification.risk_level.value
        
        return {
            "initial_implementation": base_costs["initial_compliance"].get(risk_level, 100000),
            "annual_ongoing": base_costs["ongoing_costs"].get(risk_level, 50000),
            "cost_breakdown": {
                "legal_and_compliance": "40%",
                "technical_implementation": "35%",
                "documentation_and_processes": "15%",
                "training_and_change_management": "10%"
            }
        }

    def _estimate_implementation_timeline(self, classification: AISystemClassification) -> str:
        """Estimate implementation timeline"""
        
        timelines = {
            AISystemRiskLevel.HIGH_RISK.value: "12-18 months",
            AISystemRiskLevel.LIMITED_RISK.value: "6-9 months",
            AISystemRiskLevel.MINIMAL_RISK.value: "3-6 months"
        }
        
        return timelines.get(classification.risk_level.value, "6-12 months")

    def _identify_operational_changes(self, classification: AISystemClassification) -> List[str]:
        """Identify required operational changes"""
        
        base_changes = [
            "Compliance monitoring processes",
            "Documentation management procedures",
            "Staff training programs"
        ]
        
        if classification.risk_level == AISystemRiskLevel.HIGH_RISK:
            base_changes.extend([
                "Quality management system implementation",
                "Risk management process integration",
                "Human oversight procedure establishment",
                "Incident reporting system deployment"
            ])
            
        return base_changes

    def _assess_competitive_implications(self, classification: AISystemClassification) -> Dict:
        """Assess competitive implications of compliance"""
        
        return {
            "market_differentiation": "Compliance as competitive advantage",
            "barrier_to_entry": "High compliance costs may limit competition",
            "customer_trust": "Compliance certification builds customer confidence", 
            "innovation_impact": "Compliance requirements may slow innovation cycles",
            "global_competitiveness": "EU compliance facilitates global market access"
        }

    def _identify_regulatory_risks(self, classification: AISystemClassification) -> List[Dict]:
        """Identify regulatory compliance risks"""
        
        return [
            {
                "risk": "Non-compliance penalties",
                "impact": "Financial and reputational damage",
                "likelihood": "High if not properly managed",
                "mitigation": "Comprehensive compliance program"
            },
            {
                "risk": "Regulatory interpretation changes",
                "impact": "Additional compliance requirements",
                "likelihood": "Medium",
                "mitigation": "Continuous regulatory monitoring"
            },
            {
                "risk": "Technical standard evolution",
                "impact": "Need for system updates and re-certification",
                "likelihood": "Medium",
                "mitigation": "Flexible architecture and regular reviews"
            }
        ]

    def _propose_mitigation_strategies(self, classification: AISystemClassification) -> List[str]:
        """Propose regulatory risk mitigation strategies"""
        
        return [
            "Implement comprehensive compliance management system",
            "Establish regulatory monitoring and intelligence function",
            "Build flexible and adaptable AI system architecture",
            "Maintain strong legal and compliance expertise",
            "Develop industry partnerships and knowledge sharing",
            "Implement continuous monitoring and improvement processes"
        ]

    def _develop_contingency_plans(self, classification: AISystemClassification) -> Dict:
        """Develop contingency plans for compliance issues"""
        
        return {
            "compliance_violation": {
                "immediate_actions": ["System shutdown if required", "Legal team activation", "Regulatory notification"],
                "remediation": ["Gap analysis", "Corrective action plan", "Implementation and verification"],
                "communication": ["Stakeholder notification", "Public disclosure if required"]
            },
            "regulatory_changes": {
                "monitoring": ["Regulatory intelligence", "Industry consultation", "Legal analysis"],
                "adaptation": ["Impact assessment", "Compliance gap analysis", "Implementation planning"],
                "communication": ["Internal updates", "Customer communications", "Partner notifications"]
            }
        }

    def _generate_regulatory_recommendations(self, classification: AISystemClassification) -> List[str]:
        """Generate regulatory compliance recommendations"""
        
        return [
            "Prioritize compliance implementation based on risk level and timeline",
            "Invest in comprehensive compliance management systems and processes",
            "Establish dedicated AI governance and compliance team",
            "Implement continuous monitoring and improvement processes",
            "Build strong relationships with legal and regulatory expertise",
            "Consider compliance as competitive advantage and market differentiator",
            "Prepare for ongoing regulatory evolution and adaptation requirements"
        ]