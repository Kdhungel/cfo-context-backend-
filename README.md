
**CFO Context Backend**
=======================

**Demo Backend for CFO Pre-Call Context**

This backend provides CFO-ready context snapshots for clients. It is a lightweight FastAPI service that generates pre-call insights, alerts, metrics, and open decisions for a client.

**API**
-------

### **Get Client Context**

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   GET /api/clients/{client_id}/context   `

**Parameters:**

*   client\_id (string): ID of the client, e.g., client\_acme.
    

**Response:**

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   {    "client_id": "client_acme",    "generated_at": "2026-01-12T23:39:49.943321",    "headline": "Cash runway at 5.2 months — focus on burn control before growth",    "alerts": [      {        "type": "runway",        "severity": "high",        "message": "Cash runway at 5.2 months"      }    ],    "key_metrics": {      "cash_balance": 4200000.0,      "monthly_burn": 810000.0,      "runway_months": 5.2,      "revenue_mom_growth": 0.06,      "days_since_last_contact": 7.0,      "aws_spend": 50000.0,      "payroll": 500000.0,      "marketing": 75000.0    },    "recent_changes": [      "Cash balance changed from 4000000.0 to 4200000.0 (5.0% MoM)",      "Monthly burn changed from 750000.0 to 810000.0 (8.0% MoM)",      "... more changes ..."    ],    "open_decisions": [      {        "id": "dec_001",        "question": "Approve Q2 hiring plan?",        "severity": "high"      }    ],    "last_interaction": {      "type": "client_call",      "date": "2026-01-05",      "summary": "Discussed burn rate and Q1 hiring plan"    }  }   `

**Local Demo**
--------------

You can run a quick test locally:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   # Activate virtual environment  source .venv/bin/activate  # Install dependencies  pip install -r requirements.txt  # Run the FastAPI backend  uvicorn main:app --reload   `

Then, in Python or Postman, you can do:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   from app.context.builder import build_context_snapshot  snapshot = build_context_snapshot("client_acme")  print(snapshot.model_dump_json(indent=2))   `

**Frontend Integration Notes**
------------------------------

*   Endpoint: /api/clients/{client\_id}/context
    
*   Returns full snapshot in JSON format.
    
*   Frontend can use generated\_at for timestamps, headline for display, alerts and key\_metrics for dashboard widgets, recent\_changes for highlighting changes, open\_decisions for actionable items, and last\_interaction for call prep.
    

**Example Usage (JS/React):**

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML``   const res = await fetch(`https://your-backend.com/api/clients/client_acme/context`);  const data = await res.json();  console.log(data.headline); // Display headline   ``

**What’s Included**
-------------------

*   main.py – FastAPI entry point
    
*   app/context/builder.py – Core logic generating context snapshots
    
*   demo\_client.py – Simple Python client to test API
    
*   Documentation here in README for integration
    

**Next Steps for Igwe (Frontend)**
----------------------------------

1.  Clone the repo:
    

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   git clone https://github.com/Kdhungel/cfo-context-backend-.git   `

1.  Start backend locally or on a dev server.
    
2.  Consume /api/clients/{client\_id}/context endpoint in frontend.
    
3.  Reference the frontend integration section for how JSON is structured.
    

