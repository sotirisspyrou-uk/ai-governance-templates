from typing import Dict, List, Optional, Tuple, Any
from datetime import datetime
from enum import Enum
import numpy as np
from pydantic import BaseModel


class ProtectedAttribute(Enum):
    GENDER = "gender"
    RACE = "race"
    AGE = "age"
    RELIGION = "religion"
    DISABILITY = "disability"
    SEXUAL_ORIENTATION = "sexual_orientation"
    NATIONALITY = "nationality"
    SOCIOECONOMIC_STATUS = "socioeconomic_status"


class BiasType(Enum):
    STATISTICAL = "statistical"
    INDIVIDUAL = "individual"
    GROUP = "group"
    INTERSECTIONAL = "intersectional"
    ALGORITHMIC = "algorithmic"
    REPRESENTATION = "representation"


class FairnessMetric(Enum):
    DEMOGRAPHIC_PARITY = "demographic_parity"
    EQUALIZED_ODDS = "equalized_odds"
    EQUAL_OPPORTUNITY = "equal_opportunity"
    CALIBRATION = "calibration"
    INDIVIDUAL_FAIRNESS = "individual_fairness"
    COUNTERFACTUAL_FAIRNESS = "counterfactual_fairness"


class BiasDetectionResult(BaseModel):
    detection_id: str
    system_name: str
    timestamp: datetime
    protected_attributes: List[ProtectedAttribute]
    bias_detected: bool
    bias_severity: str
    fairness_metrics: Dict[str, float]
    affected_groups: List[str]
    recommendations: List[str]
    mitigation_required: bool


class BiasDetectionFramework:
    def __init__(self):
        self.detection_config = {}
        self.fairness_thresholds = self._initialize_fairness_thresholds()
        self.bias_patterns = self._initialize_bias_patterns()
        self.mitigation_strategies = self._initialize_mitigation_strategies()

    def detect_bias_across_systems(self, ai_systems: List[Dict]) -> List[BiasDetectionResult]:
        detection_results = []
        
        for system in ai_systems:
            result = self.detect_system_bias(system)
            detection_results.append(result)
            
        return detection_results

    def detect_system_bias(self, system_data: Dict) -> BiasDetectionResult:
        detection_id = f"bias_detection_{system_data.get('system_id', 'unknown')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        # Determine protected attributes to test
        protected_attrs = self._identify_protected_attributes(system_data)
        
        # Calculate fairness metrics
        fairness_metrics = self._calculate_fairness_metrics(system_data, protected_attrs)
        
        # Detect bias patterns
        bias_detected = self._detect_bias_patterns(fairness_metrics)
        
        # Assess bias severity
        bias_severity = self._assess_bias_severity(fairness_metrics)
        
        # Identify affected groups
        affected_groups = self._identify_affected_groups(system_data, fairness_metrics)
        
        # Generate recommendations
        recommendations = self._generate_bias_recommendations(fairness_metrics, bias_severity)
        
        result = BiasDetectionResult(
            detection_id=detection_id,
            system_name=system_data.get("name", "Unknown System"),
            timestamp=datetime.now(),
            protected_attributes=protected_attrs,
            bias_detected=bias_detected,
            bias_severity=bias_severity,
            fairness_metrics=fairness_metrics,
            affected_groups=affected_groups,
            recommendations=recommendations,
            mitigation_required=bias_detected and bias_severity in ["High", "Critical"]
        )
        
        return result

    def calculate_demographic_parity(self, data: Dict, protected_attribute: str) -> float:
        try:
            # Simulate calculation - in real implementation, would use actual data
            positive_rate_privileged = data.get(f"{protected_attribute}_privileged_positive_rate", 0.5)
            positive_rate_unprivileged = data.get(f"{protected_attribute}_unprivileged_positive_rate", 0.4)
            
            # Demographic parity difference
            dp_difference = abs(positive_rate_privileged - positive_rate_unprivileged)
            
            # Convert to score (0 = perfect parity, 1 = maximum disparity)
            return round(dp_difference, 3)
        except Exception:
            return 0.5  # Default moderate bias assumption

    def calculate_equalized_odds(self, data: Dict, protected_attribute: str) -> float:
        try:
            # True positive rates
            tpr_privileged = data.get(f"{protected_attribute}_privileged_tpr", 0.8)
            tpr_unprivileged = data.get(f"{protected_attribute}_unprivileged_tpr", 0.7)
            
            # False positive rates
            fpr_privileged = data.get(f"{protected_attribute}_privileged_fpr", 0.1)
            fpr_unprivileged = data.get(f"{protected_attribute}_unprivileged_fpr", 0.15)
            
            # Equalized odds difference
            tpr_diff = abs(tpr_privileged - tpr_unprivileged)
            fpr_diff = abs(fpr_privileged - fpr_unprivileged)
            
            eo_difference = max(tpr_diff, fpr_diff)
            
            return round(eo_difference, 3)
        except Exception:
            return 0.3  # Default moderate bias assumption

    def calculate_individual_fairness(self, data: Dict) -> float:
        try:
            # Measure consistency of similar individuals receiving similar treatment
            consistency_score = data.get("individual_consistency_score", 0.7)
            
            # Convert to bias metric (0 = perfectly fair, 1 = highly biased)
            individual_bias = 1.0 - consistency_score
            
            return round(individual_bias, 3)
        except Exception:
            return 0.4  # Default moderate bias assumption

    def generate_fairness_monitoring_system(self, systems: List[Dict]) -> Dict:
        monitoring_config = {
            "monitoring_id": f"fairness_monitor_{datetime.now().strftime('%Y%m%d')}",
            "systems_monitored": len(systems),
            "monitoring_schedule": {
                "continuous_monitoring": ["high_risk_systems"],
                "daily_monitoring": ["customer_facing_systems"],
                "weekly_monitoring": ["internal_systems"],
                "monthly_monitoring": ["low_risk_systems"]
            },
            "alert_thresholds": {
                "demographic_parity": 0.1,
                "equalized_odds": 0.1,
                "individual_fairness": 0.2,
                "statistical_significance": 0.05
            },
            "automated_checks": {
                "bias_drift_detection": True,
                "intersectional_bias_analysis": True,
                "fairness_metric_calculation": True,
                "alert_generation": True
            },
            "reporting_framework": {
                "real_time_dashboard": True,
                "weekly_bias_report": True,
                "monthly_fairness_assessment": True,
                "quarterly_bias_audit": True
            },
            "mitigation_triggers": {
                "immediate_review": "bias_severity >= Critical",
                "mitigation_planning": "bias_severity >= High",
                "enhanced_monitoring": "bias_severity >= Medium",
                "documentation_update": "any_bias_detected"
            }
        }
        
        return monitoring_config

    def create_bias_mitigation_plan(self, detection_result: BiasDetectionResult) -> Dict:
        mitigation_plan = {
            "plan_id": f"mitigation_{detection_result.detection_id}",
            "system_name": detection_result.system_name,
            "created_date": datetime.now().isoformat(),
            "bias_summary": {
                "severity": detection_result.bias_severity,
                "affected_attributes": [attr.value for attr in detection_result.protected_attributes],
                "affected_groups": detection_result.affected_groups,
                "key_metrics": detection_result.fairness_metrics
            },
            "mitigation_strategies": self._select_mitigation_strategies(detection_result),
            "implementation_timeline": self._create_mitigation_timeline(detection_result.bias_severity),
            "success_criteria": self._define_success_criteria(detection_result),
            "monitoring_plan": self._create_post_mitigation_monitoring(detection_result),
            "resource_requirements": self._estimate_resource_requirements(detection_result),
            "risk_assessment": self._assess_mitigation_risks(detection_result),
            "approval_workflow": self._define_approval_workflow(detection_result.bias_severity)
        }
        
        return mitigation_plan

    def perform_intersectional_analysis(self, system_data: Dict, attributes: List[ProtectedAttribute]) -> Dict:
        intersectional_results = {
            "analysis_id": f"intersectional_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            "system_name": system_data.get("name", "Unknown"),
            "analyzed_intersections": [],
            "bias_findings": {},
            "compound_effects": [],
            "priority_intersections": []
        }
        
        # Analyze all pairwise combinations of protected attributes
        for i, attr1 in enumerate(attributes):
            for attr2 in attributes[i+1:]:
                intersection_key = f"{attr1.value}_x_{attr2.value}"
                
                # Simulate intersectional bias calculation
                intersection_bias = self._calculate_intersectional_bias(system_data, attr1, attr2)
                
                intersectional_results["analyzed_intersections"].append(intersection_key)
                intersectional_results["bias_findings"][intersection_key] = {
                    "bias_score": intersection_bias,
                    "severity": self._categorize_bias_severity(intersection_bias),
                    "affected_population": self._estimate_affected_population(system_data, attr1, attr2)
                }
                
                # Identify compound effects
                if intersection_bias > max(
                    self._get_single_attribute_bias(system_data, attr1),
                    self._get_single_attribute_bias(system_data, attr2)
                ):
                    intersectional_results["compound_effects"].append({
                        "intersection": intersection_key,
                        "amplification_factor": intersection_bias,
                        "explanation": f"Intersection shows higher bias than individual attributes"
                    })
        
        # Prioritize intersections for mitigation
        sorted_intersections = sorted(
            intersectional_results["bias_findings"].items(),
            key=lambda x: x[1]["bias_score"],
            reverse=True
        )
        
        intersectional_results["priority_intersections"] = [
            {"intersection": k, **v} for k, v in sorted_intersections[:3]
        ]
        
        return intersectional_results

    def generate_bias_audit_report(self, detection_results: List[BiasDetectionResult]) -> Dict:
        audit_report = {
            "report_id": f"bias_audit_{datetime.now().strftime('%Y%m%d')}",
            "audit_date": datetime.now().isoformat(),
            "scope": {
                "systems_audited": len(detection_results),
                "protected_attributes_analyzed": list(set(
                    attr.value for result in detection_results 
                    for attr in result.protected_attributes
                )),
                "audit_period": "Current snapshot"
            },
            "executive_summary": self._create_audit_executive_summary(detection_results),
            "bias_findings": {
                "systems_with_bias": len([r for r in detection_results if r.bias_detected]),
                "critical_bias_systems": len([r for r in detection_results if r.bias_severity == "Critical"]),
                "high_bias_systems": len([r for r in detection_results if r.bias_severity == "High"]),
                "medium_bias_systems": len([r for r in detection_results if r.bias_severity == "Medium"])
            },
            "fairness_metrics_summary": self._summarize_fairness_metrics(detection_results),
            "affected_groups_analysis": self._analyze_affected_groups(detection_results),
            "regulatory_implications": self._assess_regulatory_implications(detection_results),
            "recommendations": self._generate_audit_recommendations(detection_results),
            "action_plan": self._create_audit_action_plan(detection_results),
            "next_audit_date": (datetime.now().replace(day=1) + datetime.timedelta(days=32)).replace(day=1).isoformat()
        }
        
        return audit_report

    def _initialize_fairness_thresholds(self) -> Dict:
        return {
            FairnessMetric.DEMOGRAPHIC_PARITY.value: 0.1,
            FairnessMetric.EQUALIZED_ODDS.value: 0.1,
            FairnessMetric.EQUAL_OPPORTUNITY.value: 0.1,
            FairnessMetric.CALIBRATION.value: 0.05,
            FairnessMetric.INDIVIDUAL_FAIRNESS.value: 0.2,
            FairnessMetric.COUNTERFACTUAL_FAIRNESS.value: 0.1
        }

    def _initialize_bias_patterns(self) -> Dict:
        return {
            "statistical_bias": {
                "indicators": ["significant_group_differences", "unequal_outcomes"],
                "threshold": 0.1,
                "mitigation": "statistical_adjustment"
            },
            "algorithmic_bias": {
                "indicators": ["model_feature_bias", "training_data_bias"],
                "threshold": 0.15,
                "mitigation": "model_retraining"
            },
            "representation_bias": {
                "indicators": ["underrepresented_groups", "data_imbalance"],
                "threshold": 0.2,
                "mitigation": "data_augmentation"
            }
        }

    def _initialize_mitigation_strategies(self) -> Dict:
        return {
            "pre_processing": [
                "Data augmentation for underrepresented groups",
                "Synthetic data generation",
                "Feature selection and engineering",
                "Sampling techniques (SMOTE, undersampling)"
            ],
            "in_processing": [
                "Fairness constraints in model training",
                "Adversarial debiasing",
                "Multi-task learning with fairness objectives",
                "Regularization techniques"
            ],
            "post_processing": [
                "Threshold optimization",
                "Calibration across groups",
                "Output adjustment mechanisms",
                "Fairness-aware ensemble methods"
            ],
            "monitoring": [
                "Continuous bias monitoring",
                "Fairness metric tracking",
                "Drift detection systems",
                "Regular bias audits"
            ]
        }

    def _identify_protected_attributes(self, system_data: Dict) -> List[ProtectedAttribute]:
        # Determine which protected attributes are relevant based on system data
        relevant_attributes = []
        
        data_fields = system_data.get("data_fields", [])
        use_case = system_data.get("use_case", "").lower()
        
        # Common attributes that should always be checked
        relevant_attributes.extend([
            ProtectedAttribute.GENDER,
            ProtectedAttribute.RACE,
            ProtectedAttribute.AGE
        ])
        
        # Context-specific attributes
        if "employment" in use_case or "hiring" in use_case:
            relevant_attributes.extend([
                ProtectedAttribute.DISABILITY,
                ProtectedAttribute.RELIGION
            ])
        
        if "credit" in use_case or "loan" in use_case:
            relevant_attributes.append(ProtectedAttribute.SOCIOECONOMIC_STATUS)
        
        return list(set(relevant_attributes))

    def _calculate_fairness_metrics(self, system_data: Dict, protected_attrs: List[ProtectedAttribute]) -> Dict[str, float]:
        metrics = {}
        
        for attr in protected_attrs:
            attr_key = attr.value
            
            # Calculate demographic parity
            metrics[f"{attr_key}_demographic_parity"] = self.calculate_demographic_parity(system_data, attr_key)
            
            # Calculate equalized odds
            metrics[f"{attr_key}_equalized_odds"] = self.calculate_equalized_odds(system_data, attr_key)
        
        # Calculate overall individual fairness
        metrics["individual_fairness"] = self.calculate_individual_fairness(system_data)
        
        return metrics

    def _detect_bias_patterns(self, fairness_metrics: Dict[str, float]) -> bool:
        # Check if any metric exceeds threshold
        for metric_name, value in fairness_metrics.items():
            if "demographic_parity" in metric_name and value > self.fairness_thresholds["demographic_parity"]:
                return True
            if "equalized_odds" in metric_name and value > self.fairness_thresholds["equalized_odds"]:
                return True
            if "individual_fairness" in metric_name and value > self.fairness_thresholds["individual_fairness"]:
                return True
        
        return False

    def _assess_bias_severity(self, fairness_metrics: Dict[str, float]) -> str:
        max_bias = max(fairness_metrics.values()) if fairness_metrics else 0
        
        if max_bias >= 0.5:
            return "Critical"
        elif max_bias >= 0.3:
            return "High"
        elif max_bias >= 0.15:
            return "Medium"
        elif max_bias >= 0.05:
            return "Low"
        else:
            return "Minimal"

    def _identify_affected_groups(self, system_data: Dict, fairness_metrics: Dict[str, float]) -> List[str]:
        affected_groups = []
        
        for metric_name, value in fairness_metrics.items():
            if value > 0.1:  # Significant bias threshold
                if "gender" in metric_name:
                    affected_groups.extend(["Women", "Non-binary individuals"])
                if "race" in metric_name:
                    affected_groups.extend(["Racial minorities"])
                if "age" in metric_name:
                    affected_groups.extend(["Older adults", "Young adults"])
        
        return list(set(affected_groups))

    def _generate_bias_recommendations(self, fairness_metrics: Dict[str, float], severity: str) -> List[str]:
        recommendations = []
        
        if severity in ["Critical", "High"]:
            recommendations.extend([
                "Immediate bias mitigation required",
                "Suspend system deployment until bias is addressed",
                "Implement comprehensive bias testing framework"
            ])
        
        if severity in ["Medium", "High", "Critical"]:
            recommendations.extend([
                "Conduct detailed bias analysis",
                "Implement fairness constraints in model training",
                "Enhance monitoring and alerting systems"
            ])
        
        # Specific recommendations based on metrics
        for metric_name, value in fairness_metrics.items():
            if value > 0.2:
                if "demographic_parity" in metric_name:
                    recommendations.append("Apply demographic parity constraints")
                if "equalized_odds" in metric_name:
                    recommendations.append("Implement equalized odds post-processing")
        
        return recommendations

    def _select_mitigation_strategies(self, result: BiasDetectionResult) -> List[Dict]:
        strategies = []
        
        severity_strategies = {
            "Critical": ["pre_processing", "in_processing", "post_processing", "monitoring"],
            "High": ["in_processing", "post_processing", "monitoring"],
            "Medium": ["post_processing", "monitoring"],
            "Low": ["monitoring"]
        }
        
        applicable_strategies = severity_strategies.get(result.bias_severity, ["monitoring"])
        
        for strategy_type in applicable_strategies:
            for strategy in self.mitigation_strategies.get(strategy_type, []):
                strategies.append({
                    "type": strategy_type,
                    "strategy": strategy,
                    "priority": "High" if strategy_type in ["pre_processing", "in_processing"] else "Medium"
                })
        
        return strategies

    def _create_mitigation_timeline(self, severity: str) -> Dict:
        timelines = {
            "Critical": {"immediate": 1, "short_term": 7, "long_term": 30},
            "High": {"immediate": 3, "short_term": 14, "long_term": 60},
            "Medium": {"immediate": 7, "short_term": 30, "long_term": 90},
            "Low": {"immediate": 14, "short_term": 60, "long_term": 120}
        }
        
        timeline = timelines.get(severity, timelines["Medium"])
        
        return {
            "immediate_actions": f"{timeline['immediate']} days",
            "short_term_mitigation": f"{timeline['short_term']} days",
            "long_term_solution": f"{timeline['long_term']} days"
        }

    def _define_success_criteria(self, result: BiasDetectionResult) -> Dict:
        return {
            "fairness_thresholds": {
                "demographic_parity": "<0.05",
                "equalized_odds": "<0.05",
                "individual_fairness": "<0.1"
            },
            "monitoring_requirements": [
                "No degradation in fairness metrics",
                "Sustained improvement over 90 days",
                "Stakeholder acceptance validation"
            ],
            "validation_process": [
                "Independent bias testing",
                "Stakeholder review",
                "Regulatory compliance check"
            ]
        }

    def _create_post_mitigation_monitoring(self, result: BiasDetectionResult) -> Dict:
        return {
            "monitoring_frequency": "Weekly for 3 months, then monthly",
            "metrics_to_track": [attr.value for attr in result.protected_attributes],
            "alert_conditions": "Any metric exceeding baseline + 10%",
            "review_schedule": "Monthly bias assessment meetings"
        }

    def _estimate_resource_requirements(self, result: BiasDetectionResult) -> Dict:
        base_effort = {
            "Critical": {"person_days": 60, "budget": 150000},
            "High": {"person_days": 30, "budget": 75000},
            "Medium": {"person_days": 15, "budget": 30000},
            "Low": {"person_days": 5, "budget": 10000}
        }
        
        return base_effort.get(result.bias_severity, base_effort["Medium"])

    def _assess_mitigation_risks(self, result: BiasDetectionResult) -> List[str]:
        return [
            "Model performance degradation during mitigation",
            "Incomplete bias removal",
            "Introduction of new biases",
            "Stakeholder resistance to changes",
            "Regulatory compliance complications"
        ]

    def _define_approval_workflow(self, severity: str) -> List[str]:
        workflows = {
            "Critical": ["CTO", "Chief Risk Officer", "Legal", "CEO"],
            "High": ["CTO", "Chief Risk Officer", "Legal"],
            "Medium": ["Technical Lead", "Ethics Committee"],
            "Low": ["Technical Lead"]
        }
        
        return workflows.get(severity, workflows["Medium"])

    def _calculate_intersectional_bias(self, system_data: Dict, attr1: ProtectedAttribute, attr2: ProtectedAttribute) -> float:
        # Simulate intersectional bias calculation
        single_bias_1 = self._get_single_attribute_bias(system_data, attr1)
        single_bias_2 = self._get_single_attribute_bias(system_data, attr2)
        
        # Simulate compound effect (intersection often shows higher bias)
        compound_multiplier = 1.3
        intersectional_bias = (single_bias_1 + single_bias_2) * compound_multiplier
        
        return round(min(intersectional_bias, 1.0), 3)

    def _get_single_attribute_bias(self, system_data: Dict, attr: ProtectedAttribute) -> float:
        # Simulate single attribute bias score
        bias_scores = {
            ProtectedAttribute.GENDER: 0.15,
            ProtectedAttribute.RACE: 0.20,
            ProtectedAttribute.AGE: 0.10,
            ProtectedAttribute.RELIGION: 0.12,
            ProtectedAttribute.DISABILITY: 0.18
        }
        
        return bias_scores.get(attr, 0.15)

    def _categorize_bias_severity(self, bias_score: float) -> str:
        if bias_score >= 0.5:
            return "Critical"
        elif bias_score >= 0.3:
            return "High"
        elif bias_score >= 0.15:
            return "Medium"
        else:
            return "Low"

    def _estimate_affected_population(self, system_data: Dict, attr1: ProtectedAttribute, attr2: ProtectedAttribute) -> str:
        return f"Estimated 5-15% of user population affected by {attr1.value}-{attr2.value} intersection"

    def _create_audit_executive_summary(self, results: List[BiasDetectionResult]) -> str:
        total_systems = len(results)
        biased_systems = len([r for r in results if r.bias_detected])
        
        return f"""
        Bias Audit Summary: {biased_systems}/{total_systems} systems showed detectable bias.
        Critical issues identified in {len([r for r in results if r.bias_severity == 'Critical'])} systems.
        Immediate mitigation required for high-severity bias cases.
        Overall fairness posture: {'Needs Improvement' if biased_systems > total_systems * 0.3 else 'Acceptable'}.
        """

    def _summarize_fairness_metrics(self, results: List[BiasDetectionResult]) -> Dict:
        all_metrics = {}
        for result in results:
            for metric, value in result.fairness_metrics.items():
                if metric not in all_metrics:
                    all_metrics[metric] = []
                all_metrics[metric].append(value)
        
        summary = {}
        for metric, values in all_metrics.items():
            summary[metric] = {
                "average": round(sum(values) / len(values), 3),
                "max": round(max(values), 3),
                "systems_exceeding_threshold": len([v for v in values if v > 0.1])
            }
        
        return summary

    def _analyze_affected_groups(self, results: List[BiasDetectionResult]) -> Dict:
        all_groups = []
        for result in results:
            all_groups.extend(result.affected_groups)
        
        group_counts = {}
        for group in all_groups:
            group_counts[group] = group_counts.get(group, 0) + 1
        
        return {
            "most_affected_groups": sorted(group_counts.items(), key=lambda x: x[1], reverse=True)[:5],
            "total_affected_groups": len(set(all_groups)),
            "systems_per_group": group_counts
        }

    def _assess_regulatory_implications(self, results: List[BiasDetectionResult]) -> List[str]:
        implications = []
        
        high_severity_count = len([r for r in results if r.bias_severity in ["High", "Critical"]])
        
        if high_severity_count > 0:
            implications.extend([
                "EU AI Act Article 10 - Bias monitoring and correction required",
                "GDPR Article 22 - Automated decision-making safeguards needed",
                "Potential regulatory reporting requirements"
            ])
        
        return implications

    def _generate_audit_recommendations(self, results: List[BiasDetectionResult]) -> List[str]:
        return [
            "Implement organization-wide bias detection framework",
            "Establish regular fairness auditing schedule",
            "Enhance bias training for development teams",
            "Create bias response playbooks",
            "Integrate fairness metrics into CI/CD pipelines"
        ]

    def _create_audit_action_plan(self, results: List[BiasDetectionResult]) -> Dict:
        critical_systems = [r for r in results if r.bias_severity == "Critical"]
        high_systems = [r for r in results if r.bias_severity == "High"]
        
        return {
            "immediate_actions": [f"Address bias in {s.system_name}" for s in critical_systems],
            "30_day_actions": [f"Implement mitigation for {s.system_name}" for s in high_systems],
            "90_day_actions": [
                "Deploy organization-wide bias monitoring",
                "Complete bias training for all teams",
                "Establish bias governance committee"
            ]
        }