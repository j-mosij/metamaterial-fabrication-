Digital Synthetic Alloy Repository & Adversarial Agent

"""
Digital Synthetic Alloy Repository & Material Loom Engine
Author: .j.mosij
Date: August 12, 2026
Description: A self-contained material design environment featuring a Loom layer compiler,
             a Digital Synthetic Engine for thermodynamic/physical attribute simulations,
             a formal repository index with embedded schematics, and a simulated 
             adversarial learning agent for system validation.
"""

import math
import random
import json
from datetime import datetime
from typing import Dict, List, Any, Tuple

# =====================================================================
# 1. REPOSITORY INDEX & VERSIONS
# =====================================================================

class RepositoryIndex:
    """Manages the source index, asset manifests, blueprints, and code file metadata."""
    def __init__(self):
        self.author = ".j.mosij"
        self.created_at = "2026-08-12"
        self.registry: Dict[str, Dict[str, Any]] = {}
        self._initialize_default_registry()

    def _initialize_default_registry(self):
        """Populates structural blueprints and code architecture mappings."""
        self.register_asset(
            path="core/loom.py",
            asset_type="Source Code",
            description="Compiles and weaves layer-by-layer atomic configurations for anisotropic materials."
        )
        self.register_asset(
            path="core/synthetic_engine.py",
            asset_type="Source Code",
            description="Predicts mechanical, thermodynamic, and phase-stability markers for synthetic alloys."
        )
        self.register_asset(
            path="blueprints/ti_al_superalloy.json",
            asset_type="Schematic Blueprint",
            description="High-temperature titanium-aluminide multi-layer matrix configuration.",
            data={
                "base_element": "Ti",
                "alloying_elements": {"Al": 45.0, "Nb": 8.0, "Cr": 2.0},
                "microstructure": "Gamma-TiAl Lamellar Matrix",
                "target_application": "Hypersonic Turbine Blades"
            }
        )
        self.register_asset(
            path="blueprints/heas_refractory.json",
            asset_type="Schematic Blueprint",
            description="Refractory High-Entropy Alloy (RHEA) for extreme thermal shielding.",
            data={
                "elements": {"W": 25.0, "Ta": 25.0, "Mo": 25.0, "Nb": 25.0},
                "microstructure": "Single-Phase BCC Solid Solution",
                "target_application": "Nuclear Fusion First Wall Shields"
            }
        )

    def register_asset(self, path: str, asset_type: str, description: str, data: Any = None):
        """Appends files, scripts, or structural schematics to the index."""
        self.registry[path] = {
            "type": asset_type,
            "description": description,
            "author": self.author,
            "last_modified": str(datetime.now()),
            "payload": data
        }

    def fetch_blueprint(self, path: str) -> Dict[str, Any]:
        """Retrieves targeted alloy schematics from the repository."""
        if path in self.registry:
            return self.registry[path]
        return {"error": f"Asset '{path}' not found in registry index."}

    def generate_manifest_report(self) -> str:
        """Returns a formatted view of the current code and schematic index."""
        report = f"--- REPOSITORY INDEX MANIFEST ---\nAuthor: {self.author}\n"
        for path, info in self.registry.items():
            report += f"[{info['type']}] {path} -> {info['description']}\n"
        return report


# =====================================================================
# 2. MATERIAL LOOM LAYER WEAVER
# =====================================================================

class Loom:
    """
    Weaves structural distributions and gradient spatial meshes for alloys.
    Handles layer-by-layer material architecture to model directional compositions.
    """
    def __init__(self, resolution_x: int = 10, resolution_y: int = 10):
        self.res_x = resolution_x
        self.res_y = resolution_y

    def weave_gradient_matrix(self, base_element: str, additive_element: str, gradient_direction: str = "vertical") -> List[List[Dict[str, float]]]:
        """
        Simulates a continuous structural deposition gradient.
        Creates a multi-dimensional matrix of composition variations.
        """
        mesh = []
        for y in range(self.res_y):
            row = []
            for x in range(self.res_x):
                # Calculate localized mix ratios based on spatial gradients
                if gradient_direction == "vertical":
                    factor = y / (self.res_y - 1) if self.res_y > 1 else 0.5
                elif gradient_direction == "horizontal":
                    factor = x / (self.res_x - 1) if self.res_x > 1 else 0.5
                else:
                    factor = (x + y) / ((self.res_x - 1) + (self.res_y - 1))

                additive_pct = round(factor * 100.0, 2)
                base_pct = round(100.0 - additive_pct, 2)
                
                row.append({
                    base_element: base_pct,
                    additive_element: additive_pct
                })
            mesh.append(row)
        return mesh

    def format_loom_visual(self, mesh: List[List[Dict[str, float]]], target_element: str) -> str:
        """Renders an ASCII text schematic layout of the woven concentration."""
        ascii_grid = ""
        for row in mesh:
            for cell in row:
                concentration = cell.get(target_element, 0.0)
                # Map concentration percentages to structural density visual flags
                if concentration < 20:
                    ascii_grid += " . "
                elif concentration < 50:
                    ascii_grid += " ░ "
                elif concentration < 80:
                    ascii_grid += " ▒ "
                else:
                    ascii_grid += " ▓ "
            ascii_grid += "\n"
        return ascii_grid


# =====================================================================
# 3. DIGITAL SYNTHETIC ENGINE
# =====================================================================

class DigitalSyntheticEngine:
    """
    Processes atomic configurations and compositions to predict theoretical
    thermodynamic states, mechanical limits, and potential vulnerabilities.
    """
    def __init__(self):
        # Base element material profiles: (Melting Point K, Density g/cm3, Young's Modulus GPa)
        self.element_db = {
            "Ti": {"mp": 1941, "density": 4.54, "modulus": 116},
            "Al": {"mp": 933, "density": 2.70, "modulus": 70},
            "Nb": {"mp": 2750, "density": 8.57, "modulus": 105},
            "Cr": {"mp": 2180, "density": 7.19, "modulus": 279},
            "W":  {"mp": 3695, "density": 19.25, "modulus": 411},
            "Ta": {"mp": 3290, "density": 16.69, "modulus": 186},
            "Mo": {"mp": 2896, "density": 10.28, "modulus": 329}
        }

    def compile_synthetic_alloy(self, composition: Dict[str, float]) -> Dict[str, Any]:
        """
        Executes structural calculations to derive physical markers.
        Applies linear rule-of-mixtures paired with non-linear entropy penalties.
        """
        total_fraction = sum(composition.values())
        if not math.isclose(total_fraction, 100.0, abs_tol=0.1):
            # Normalize to 100% if input profile deviates slightly
            composition = {k: (v / total_fraction) * 100.0 for k, v in composition.items()}

        calc_density = 0.0
        calc_melting_point = 0.0
        calc_modulus = 0.0
        config_valid = True
        warnings = []

        # Calculate configuration entropy (R * sum(c_i * ln(c_i))) for Phase Stability
        entropy_sum = 0.0
        
        for element, percentage in composition.items():
            fraction = percentage / 100.0
            if element in self.element_db:
                db = self.element_db[element]
                calc_density += fraction * db["density"]
                calc_melting_point += fraction * db["mp"]
                calc_modulus += fraction * db["modulus"]
                
                if fraction > 0:
                    entropy_sum += fraction * math.log(fraction)
            else:
                warnings.append(f"Element {element} missing from core database calibration profiles.")
                config_valid = False

        mixing_entropy = -8.314 * entropy_sum

        # Identify structural failure vulnerabilities
        if composition.get("Al", 0.0) > 60.0 and composition.get("Ti", 0.0) > 0.0:
            warnings.append("High aluminum concentration may provoke brittle intermetallic phase precipitation.")
        if mixing_entropy > 11.0:
            phase_state = "High-Entropy Solid Solution Configuration"
        else:
            phase_state = "Standard Multi-Phase Aggregation Matrix"

        return {
            "composition": {k: round(v, 2) for k, v in composition.items()},
            "predicted_properties": {
                "density_g_cm3": round(calc_density, 3),
                "theoretical_melting_point_K": round(calc_melting_point, 1),
                "elastic_modulus_GPa": round(calc_modulus, 1),
                "mixing_entropy_J_mol_K": round(mixing_entropy, 3)
            },
            "phase_state": phase_state,
            "structural_validity": config_valid,
            "vulnerabilities": warnings
        }


# =====================================================================
# 4. ADVERSARIAL LEARNING & TESTING AGENT
# =====================================================================

class AdversarialAgent:
    """
    Designated interactive evaluation module. Challenges alloy configurations
    with critical stress, environment, and thermodynamic failure questions.
    """
    def __init__(self, engine: DigitalSyntheticEngine):
        self.engine = engine
        self.agent_name = "Aegis-Material Validator"
        self.adversarial_scenarios = [
            {
                "topic": "Hydrogen Embrittlement",
                "challenge": "Under severe electrochemical loading environments, atomic hydrogen will trap near structural boundaries. How does your composition mitigate lattice expansion strains?",
                "keywords": ["interstitial", "trapping", "grain boundary", "passivation", "niobium", "Nb"]
            },
            {
                "topic": "High-Temperature Oxidation & Creep",
                "challenge": "At processing operations exceeding 1200K, phase volatility could trigger structural degradation. What dynamic kinetics shield your layout from rapid volume breakdown?",
                "keywords": ["passivating", "oxide layer", "alumina", "chromia", "diffusion barrier", "refractory"]
            },
            {
                "topic": "Brittle Phase Segregation",
                "challenge": "Rapid solidification loops can trigger severe localized chemical segregation. How will your processing design prevent intermetallic stress fracture paths?",
                "keywords": ["annealing", "homogenization", "cooling rate", "entropy stabilization", "solute"]
            }
        ]

    def query_agent_on_alloy(self, composition: Dict[str, float], user_defense: str, scenario_index: int = 0) -> str:
        """Evaluates user defense arguments against targeted adversarial stress questions."""
        if scenario_index >= len(self.adversarial_scenarios):
            return "Invalid scenario selection index sequence."

        scenario = self.adversarial_scenarios[scenario_index]
        compiled_profile = self.engine.compile_synthetic_alloy(composition)
        
        # Calculate defense confidence score based on structural keyword validation
        matching_tokens = [word for word in scenario["keywords"] if word.lower() in user_defense.lower()]
        score = len(matching_tokens) / len(scenario["keywords"])

        response = f"\n=== [{self.agent_name}] ADVERSARIAL COMPLIANCE AUDIT ===\n"
        response += f"Target Evaluation Domain: {scenario['topic']}\n"
        response += f"Core Stress Challenge: {scenario['challenge']}\n\n"
        response += f"Assessing Design Composition Metrics: {json.dumps(compiled_profile['composition'])}\n"
        response += f"Theoretical Elastic Response: {compiled_profile['predicted_properties']['elastic_modulus_GPa']} GPa\n"
        
        response += f"\n--- Defense Evaluation Analysis ---\n"
        response += f"Defense Stance Input Length: {len(user_defense)} characters.\n"
        response += f"Identified Valid Engineering Mitigators: {matching_tokens}\n"
        
        if score >= 0.5:
            response += "Audit Result: VERIFIED. Your configuration defense includes appropriate crystal stability safeguards.\n"
        elif score > 0.0:
            response += "Audit Result: CAUTION REQUIRED. Marginal structural justification. Increase stabilizing elements or clear up boundary trapping mechanics.\n"
        else:
            response += "Audit Result: CRITICAL CRACK FAILURE RISK. The defense argument neglects boundary constraints. Immediate alloy redesign advised.\n"
            
        if compiled_profile["vulnerabilities"]:
            response += f"Warning Flags Flagged by Engine: {compiled_profile['vulnerabilities']}\n"
            
        return response


# =====================================================================
# 5. PIPELINE EXECUTION SIMULATION
# =====================================================================

def execute_repository_demonstration():
    """Runs a programmatic demonstration of the repository code architecture components."""
    print("=====================================================================")
    print("INITIALIZING REPOSITORY INFRASTRUCTURE - AUTHOR: .j.mosij")
    print("=====================================================================\n")

    # 1. Instantiate the Global Source Code and Schematic Index Tracker
    repo = RepositoryIndex()
    print(repo.generate_manifest_report())

    # 2. Extract a layered structural schema blueprint from the index
    print("--- Fetching Target Schematic Blueprint Asset ---")
    blueprint_node = repo.fetch_blueprint("blueprints/ti_al_superalloy.json")
    print(json.dumps(blueprint_node, indent=2))
    print()

    # 3. Initialize Loom and weave a microstructural alloy spatial matrix
    print("--- Compiling Spatial Material Loom Gradient Structure ---")
    loom_weaver = Loom(resolution_x=12, resolution_y=6)
    gradient_mesh = loom_weaver.weave_gradient_matrix(base_element="Ti", additive_element="Al", gradient_direction="horizontal")
    # Visualize the gradient profile matrix of Aluminum concentration across the woven framework
    visual_grid = loom_weaver.format_loom_visual(gradient_mesh, target_element="Al")
    print("Woven Composition Gradient Blueprint Layout Display (Aluminum Concentration):")
    print(visual_grid)

    # 4. Process structural profiles within the Digital Synthetic Engine
    print("--- Executing Digital Synthetic Material Calculations ---")
    synthetic_engine = DigitalSyntheticEngine()
    
    # Extract composition dictionary directly from the structural blueprint asset payload
    target_comp = blueprint_node["payload"]["alloying_elements"].copy()
    target_comp[blueprint_node["payload"]["base_element"]] = 45.0  # Balance allocation
    
    compiled_alloy_profile = synthetic_engine.compile_synthetic_alloy(target_comp)
    print("Engine Structural Calculations Output File Result:")
    print(json.dumps(compiled_alloy_profile, indent=2))
    print()

    # 5. Execute Adversarial Agent verification challenge checks
    print("--- Triggering Adversarial Agent Compliance Simulation ---")
    agent = AdversarialAgent(engine=synthetic_engine)
    
    # Design a defensive structural engineering response text profile
    sample_defense_statement = (
        "We mitigate lattice distortion by introducing interstitial niobium (Nb) alloy additions. "
        "These elements alter grain boundary trap kinetics, preventing severe localized embrittlement segregation zones."
    )
    
    # Audit Scenario 0 (Hydrogen Embrittlement)
    audit_verdict = agent.query_agent_on_alloy(
        composition=target_comp,
        user_defense=sample_defense_statement,
        scenario_index=0
    )
    print(audit_verdict)


if __name__ == "__main__":
    execute_repository_demonstration()




