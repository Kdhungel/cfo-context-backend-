**CFO Context API – Frontend Integration Guide**

**Author:** Kritish Dhungel

**Date:** 2026-01-12

**Purpose:** Guide frontend integration with the CFO Context API

**API Endpoint**

*   **URL:** GET /api/clients/{client\_id}/context
    
*   **Example:** http://127.0.0.1:8000/api/clients/client\_acme/context
    
*   **Method:** GET
    
*   **Description:** Returns a JSON snapshot of client context for CFO pre-call briefing
    

**Response JSON Structure**

*   client\_id – string, the client’s identifier
    
*   generated\_at – timestamp of snapshot generation
    
*   headline – top-level summary, based on alerts
    
*   alerts – list of alerts with type, severity, and message
    
*   key\_metrics – dictionary of key financial metrics (cash balance, burn rate, runway months, revenue growth, etc.)
    
*   recent\_changes – list of recent month-over-month changes in metrics
    
*   open\_decisions – list of pending decisions with id, question, and severity
    
*   last\_interaction – last client touchpoint summary
    

Example JSON snippet:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   {    "client_id": "client_acme",    "generated_at": "2026-01-12T23:39:49.943321",    "headline": "Cash runway at 5.2 months — focus on burn control before growth",    "alerts": [      {"type": "runway", "severity": "high", "message": "Cash runway at 5.2 months"}    ],    "key_metrics": {      "cash_balance": 4200000.0,      "monthly_burn": 810000.0,      "runway_months": 5.2,      "revenue_mom_growth": 0.06,      "days_since_last_contact": 7.0    },    "recent_changes": [      "AWS Spend changed from 42000.0 to 50000.0 (19.0% MoM)",      "Monthly Burn changed from 750000.0 to 810000.0 (8.0% MoM)"    ],    "open_decisions": [      {"id": "dec_001", "question": "Approve Q2 hiring plan?", "severity": "high"}    ],    "last_interaction": {      "type": "client_call",      "date": "2026-01-05",      "summary": "Discussed burn rate and Q1 hiring plan"    }  }   `

**Integration Notes**

*   CORS: Local testing works, headers can be added if needed for the web frontend
    
*   Path Parameter: Use client\_id in URL (e.g., client\_acme for demo)
    
*   *   headline → main banner/summary
        
    *   alerts → urgent items (color-coded/highlighted)
        
    *   key\_metrics → metrics table
        
    *   recent\_changes → highlight recent MoM changes
        
    *   open\_decisions → list of pending decisions
        
    *   last\_interaction → last client touchpoint
        

**Demo Client Script**

Python script to test API:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   import requests  url = "http://127.0.0.1:8000/api/clients/client_acme/context"  resp = requests.get(url)  data = resp.json()  print(data)   `

*   Runs with Python 3.x
    
*   Prints the full JSON snapshot
    

**Recommended Frontend Workflow**

1.  Make GET request to /api/clients/{client\_id}/context
    
2.  *   Metrics table for key\_metrics
        
    *   Alerts panel for alerts
        
    *   Recent changes list for recent\_changes
        
    *   Open decisions list for open\_decisions
        
    *   Last interaction summary for last\_interaction
        
3.  Use headline as main banner for call preparation
    

**Notes**

*   Data is static for demo purposes, but backend is ready for dynamic integration
    
*   API is lightweight and self-contained