QUESTIONS = [
    # A. BUSINESS OVERVIEW (Non-scoring but captured)
    {
        "id": "A1",
        "section": "Business Overview",
        "label": "What industry does your organization operate in?",
        "type": "text"
    },
    {
        "id": "A2",
        "section": "Business Overview",
        "label": "What are your top 3 business priorities for the next 12 months?",
        "type": "text"
    },
    {
        "id": "A3",
        "section": "Business Overview",
        "label": "What operational challenges are you looking to solve?",
        "type": "text"
    },
    {
        "id": "A4",
        "section": "Business Overview",
        "label": "How large is your user/customer base?",
        "type": "text"
    },

    # B. DATA FOUNDATION READINESS
    {
        "id": "B1",
        "section": "Data Foundation Readiness",
        "label": "Where does your data primarily reside?",
        "type": "multi_choice",
        "options": ["Databases", "Cloud storage", "Spreadsheets", "Legacy apps"],
        "dimension": "data",
        "weight": 1.0
    },
    {
        "id": "B2",
        "section": "Data Foundation Readiness",
        "label": "How structured is your data?",
        "type": "single_choice",
        "options": ["Fully structured", "Partially structured", "Mostly unstructured"],
        "dimension": "data",
        "weight": 1.0
    },
    {
        "id": "B3",
        "section": "Data Foundation Readiness",
        "label": "Do you have a centralized data warehouse or lake?",
        "type": "single_choice",
        "options": ["Yes", "No", "Planning"],
        "dimension": "data",
        "weight": 1.0
    },
    {
        "id": "B4",
        "section": "Data Foundation Readiness",
        "label": "How confident are you in your data quality and accuracy?",
        "type": "rating",
        "dimension": "data",
        "weight": 2.0
    },
    {
        "id": "B5",
        "section": "Data Foundation Readiness",
        "label": "Do your teams currently use BI dashboards or analytics tools?",
        "type": "rating",
        "dimension": "adoption",
        "weight": 1.5
    },

    # C. AUTOMATION & PROCESS MATURITY
    {
        "id": "C1",
        "section": "Automation & Process Maturity",
        "label": "What percentage of your workflows are still manual?",
        "type": "rating",
        "dimension": "adoption",
        "weight": 2.0,
        "invert": True
    },
    {
        "id": "C2",
        "section": "Automation & Process Maturity",
        "label": "Have you implemented RPA or any automation tools?",
        "type": "single_choice",
        "options": ["Yes", "No", "Pilot / Limited"],
        "dimension": "adoption",
        "weight": 1.5
    },
    {
        "id": "C3",
        "section": "Automation & Process Maturity",
        "label": "Where do delays or errors occur frequently?",
        "type": "text"
    },
    {
        "id": "C4",
        "section": "Automation & Process Maturity",
        "label": "Which areas are you looking to automate?",
        "type": "multi_choice",
        "options": ["Finance", "HR", "Operations", "Customer Support", "IT processes"],
        "dimension": "business_fit",
        "weight": 1.0
    },
    {
        "id": "C5",
        "section": "Automation & Process Maturity",
        "label": "Are your workflows documented and standardized?",
        "type": "rating",
        "dimension": "workforce",
        "weight": 1.5
    },

    # D. APPLICATION & CLOUD READINESS
    {
        "id": "D1",
        "section": "Application & Cloud Readiness",
        "label": "What is your current application environment?",
        "type": "single_choice",
        "options": ["On-prem", "Cloud", "Hybrid"],
        "dimension": "adoption",
        "weight": 1.0
    },
    {
        "id": "D2",
        "section": "Application & Cloud Readiness",
        "label": "Are your applications API-enabled for integration?",
        "type": "rating",
        "dimension": "adoption",
        "weight": 1.5
    },
    {
        "id": "D3",
        "section": "Application & Cloud Readiness",
        "label": "Do you face issues with speed, scale, or performance?",
        "type": "rating",
        "dimension": "business_fit",
        "weight": 1.5
    },
    {
        "id": "D4",
        "section": "Application & Cloud Readiness",
        "label": "What modernization initiatives have you planned or started?",
        "type": "text"
    },
    {
        "id": "D5",
        "section": "Application & Cloud Readiness",
        "label": "Do you already use services like Azure AI, AWS AI, or GCP AI?",
        "type": "single_choice",
        "options": ["Yes", "No", "Experimenting"],
        "dimension": "leadership",
        "weight": 1.0
    },

    # E. AI OPPORTUNITY & READINESS
    {
        "id": "E1",
        "section": "AI Opportunity & Readiness",
        "label": "Have you implemented any AI/ML models previously?",
        "type": "single_choice",
        "options": ["Yes", "No", "Pilot / POC"],
        "dimension": "adoption",
        "weight": 1.5
    },
    {
        "id": "E2",
        "section": "AI Opportunity & Readiness",
        "label": "Which areas do you believe AI can impact most?",
        "type": "multi_choice",
        "options": [
            "Customer service", "Predictive maintenance", "Sales & marketing",
            "Fraud detection", "Personalization", "Operations", "IT service management"
        ],
        "dimension": "business_fit",
        "weight": 1.0
    },
    {
        "id": "E3",
        "section": "AI Opportunity & Readiness",
        "label": "What type of AI use cases are you interested in?",
        "type": "multi_choice",
        "options": [
            "Generative AI", "Predictive analytics", "Recommendation engines",
            "Chatbots / Virtual agents", "Document processing"
        ],
        "dimension": "business_fit",
        "weight": 1.0
    },
    {
        "id": "E4",
        "section": "AI Opportunity & Readiness",
        "label": "What is your internal AI skill availability?",
        "type": "single_choice",
        "options": ["Strong team", "Basic knowledge", "Exploring", "None"],
        "dimension": "workforce",
        "weight": 2.0
    },
    {
        "id": "E5",
        "section": "AI Opportunity & Readiness",
        "label": "How urgent is your AI initiative?",
        "type": "single_choice",
        "options": ["Immediate", "Within 3 months", "Within 6–12 months", "Just exploring"],
        "dimension": "leadership",
        "weight": 1.5
    }
]
