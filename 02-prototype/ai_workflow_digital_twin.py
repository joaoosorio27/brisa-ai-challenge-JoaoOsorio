"""
Digital Twin & Scenario Planner Prototype
Brisa Group – AI Office Challenge 2
Use case: Generative AI Digital Twin for Road Networks
"""

# === Imports ===
import json
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# === Simulated Data (mock input) ===
scenario_data = {
    "intervention": "Add one new lane on A2 Southbound between km 20–35",
    "metrics": {
        "expected_traffic_change": "+12%",
        "estimated_delay_reduction": "8 minutes during peak",
        "emissions_change": "-4.3% CO₂",
        "construction_cost": "€24M",
        "duration": "14 months"
    },
    "context": "Area prone to congestion and accidents during summer weekends"
}

# === Prompt Template ===
prompt_template = PromptTemplate(
    input_variables=["intervention", "metrics", "context"],
    template=(
        "You are an infrastructure planning analyst at Brisa. "
        "Based on the following intervention and metrics, produce a clear, concise impact summary "
        "for decision-makers and the public, highlighting benefits, risks, and sustainability impacts.\n\n"
        "Intervention: {intervention}\n"
        "Context: {context}\n"
        "Metrics: {metrics}\n\n"
        "Write in a factual, accessible tone with bullet points for key impacts."
    )
)

# === Initialize Model (uses OpenAI or compatible LLM) ===
llm = OpenAI(temperature=0.3)

# === Build and Run the Chain ===
chain = LLMChain(llm=llm, prompt=prompt_template)
summary = chain.run(
    intervention=scenario_data["intervention"],
    metrics=json.dumps(scenario_data["metrics"]),
    context=scenario_data["context"]
)

print("=== AI-Generated Scenario Summary ===\n")
print(summary)

# === Example Output ===
"""
 Key Impacts:
• The new lane will reduce average travel times by ~8 minutes during peak.
• CO₂ emissions expected to fall by ~4% due to smoother traffic flow.
• Total construction cost: €24M, with 14-month implementation window.
• Temporary traffic disruptions may occur but long-term congestion relief is significant.
• Safety expected to improve due to reduced stop-and-go conditions.
"""
