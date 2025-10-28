```markdown
# Week 4 Report — AI in Software Engineering

Group: [Names and GitHub usernames]
Date: [YYYY-MM-DD]

---

## Part 1: Theoretical Analysis

Q1: How AI-driven code generation tools reduce development time and limitations
Answer:
AI code completion tools like GitHub Copilot reduce development time by suggesting boilerplate, common idioms, and small helper functions which speeds up routine tasks and reduces context switching. They accelerate prototyping, provide examples for unfamiliar APIs, and can improve productivity in pair-programming style work. Limitations include: hallucinated or insecure code, suggestions that may not follow project-specific patterns, potential license and attribution concerns, and over-reliance causing skill degradation. They also struggle with highly domain-specific logic and can introduce subtle bugs that require careful review.

Q2: Supervised vs Unsupervised learning for automated bug detection
Answer:
Supervised learning requires labeled examples of buggy vs non-buggy code and can learn direct mappings to predict bug-proneness or classify bug types. It typically yields high precision when labeled data is abundant. Unsupervised learning identifies anomalies or outliers (e.g., code that deviates from common patterns) and is useful when labeled bug data is scarce; it can surface unusual code that may warrant inspection. In practice, semi-supervised and hybrid approaches often perform best.

Q3: Why bias mitigation is critical in UX personalization
Answer:
Personalization affects diverse user groups; biased models can amplify disparities (e.g., recommending features that favor one demographic). This degrades user experience for underrepresented groups, harms inclusivity, and can cause regulatory and reputational damage. Mitigation ensures fairness, improves retention across demographics, and aligns products with ethical and legal standards.

Case Study: AIOps in deployments (short)
AIOps improves deployment efficiency by automating repetitive operations, detecting anomalies before deployment, and enabling predictive scaling. Examples:
1) Automated rollback: AIOps can detect abnormal post-deploy metrics and trigger an automated rollback, reducing downtime.
2) Predictive resource provisioning: Using historical telemetry, AIOps predicts load and adjusts capacity ahead of deployment to prevent performance regressions.

---

## Part 2: Practical Implementation

Task 1: AI-Powered Code Completion
- Files: code_completion.py
- Deliverables:
  * Two implementations provided: ai_suggested_sort and manual_sort.
  * Benchmark and a ~200-word analysis printed by the script.
  * Key findings: both are O(n log n); the ai_suggested version is shorter and idiomatic; manual version is explicit and useful when precomputing keys.

Task 2: Automated Testing with AI
- Files: selenium_login_test.py
- Deliverables:
  * Selenium script for valid/invalid login cases.
  * Save screenshots to assets/login_valid.png and assets/login_invalid.png (after updating selectors/URL).
  * A ~150-word summary printed by script describing benefits and AI enhancements for testing.

Task 3: Predictive Analytics
- Files: predictive_analytics.py
- Deliverables:
  * Preprocessing (scaling), training RandomForest, grid search, evaluation.
  * Prints Accuracy and Macro F1; saves model and scaler to assets/priority_rf.joblib and assets/priority_scaler.joblib.
  * Note: Uses sklearn's breast cancer dataset as a stand-in; replace with Kaggle issue-priority data as needed.

Screenshots / graphs:
- Include: training logs, confusion matrix, or test-run screenshots in the PDF (place in assets/ and reference them here).

---

## Part 3: Ethical Reflection

Potential dataset biases:
- Team composition bias: if training data contains more issues from certain teams, model may unfairly prioritize their tickets.
- Labeling bias: human-assigned priorities may reflect manager preferences rather than objective urgency.
- Mitigation with AI Fairness 360:
  - Assess disparate impact across groups (e.g., teams, product areas).
  - Apply pre-processing (reweighting), in-processing (fair classifiers), or post-processing (adjusted thresholds).
  - Regular audits and human-in-the-loop review for high-stakes decisions.

---

## Bonus: Innovation Challenge (1-page proposal)
- Title: "AutoDocs — Context-aware automated documentation assistant"
- Purpose: Automatically produce and maintain API/docs for codebases by combining static analysis, LLM summarization, and CI integration.
- Workflow: Analyze code changes in PR -> extract functions/modules -> generate docstrings and example usage -> create PR with docs or suggestions -> maintain doc health metrics.
- Impact: Reduces documentation debt, speeds onboarding, and keeps docs synchronized with code.

---

## Appendix
- Dependencies: requirements.txt
- How to reproduce:
  1. pip install -r requirements.txt
  2. Update selenium_login_test.py with correct TEST_URL and selectors
  3. Run the scripts and collect screenshots
```