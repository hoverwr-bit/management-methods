# Management Methodology Diagrams (Open Source · Editable · 20 Frameworks)

**Language Ngôn ngữ 语言**：[中文](README.md) · **English** · [Tiếng Việt](README.vi.md)

All diagrams are drawn with **Mermaid** text syntax (open format, [mermaid-js/mermaid](https://github.com/mermaid-js/mermaid) 82k+ stars).
Any Mermaid-compatible tool can render them directly:

- **`index.html` in this folder**: double-click to view the full set of rendered diagrams in your browser (no installation needed)
- **GitHub / Gitee**: upload directly, auto-rendered
- **VS Code**: install the extension "Markdown Preview Mermaid Support"
- **Typora / Obsidian**: native support

To edit a diagram, just change the text — no drawing software required.

## Quick Finder by Scenario

| What you need to do | Recommended tools |
|---|---|
| Set goals | SMART, OKR, 5W2H |
| Plan / break down tasks | 5W2H, WBS, Gantt chart |
| Find root causes | 5Why, fishbone, 80/20 rule |
| Make decisions / analyze | SWOT, Eisenhower matrix, Six Thinking Hats, BCG matrix, Porter's Five Forces |
| Execute / continuous improvement | PDCA, DMAIC, 8D |
| Communicate and present | Pyramid Principle, Golden Circle |
| Retrospect and review | GRAI |

## Tool Selection Roadmap

```mermaid
flowchart TB
    Q{"What are you working on?"}
    Q --> A["Set goals"] --> A1["SMART / OKR"]
    Q --> B["Make a plan"] --> B1["5W2H / WBS / Gantt"]
    Q --> C["Find causes"] --> C1["5Why / Fishbone"]
    Q --> D["Make decisions"] --> D1["SWOT / Matrix / Six Thinking Hats"]
    Q --> E["Execute"] --> E1["PDCA / DMAIC / 8D"]
    Q --> F["Retrospect"] --> F1["GRAI / Pyramid Principle"]
    style Q fill:#dae8fc,stroke:#6c8ebf
```

---

## I. Goal & Planning

### 1. SMART (Goal Setting)

**One-liner:** A good goal must be Specific, Measurable, Achievable, Relevant, and Time-bound.

```mermaid
flowchart LR
    G["SMART Goal"] --> S["S Specific<br/>Clear, not vague"]
    G --> M["M Measurable<br/>Has numbers, verifiable"]
    G --> A["A Achievable<br/>Stretch but reachable"]
    G --> R["R Relevant<br/>Aligned with overall goal"]
    G --> T["T Time-bound<br/>Has a clear deadline"]
    style G fill:#dae8fc,stroke:#6c8ebf
    style S fill:#d5e8d4,stroke:#82b366
    style M fill:#ffe6cc,stroke:#d79b00
    style A fill:#fff2cc,stroke:#d6b656
    style R fill:#e1d5e7,stroke:#9673a6
    style T fill:#f8cecc,stroke:#b85450
```

**Bad example:** "Improve customer satisfaction" (vague)
**Good example:** "Within 3 months, reduce first-response time from 4 hours to under 1 hour" (meets all SMART criteria)

---

### 2. 5W2H (Think Through a Task)

**One-liner:** Use seven questions to capture the full picture of a task or plan, preventing omissions and blind action.

```mermaid
flowchart TB
    C["5W2H Seven Questions"]
    C --> W1["What<br/>Task content and goal"]
    C --> W2["Why<br/>Reason and purpose"]
    C --> W3["Who<br/>Owner and collaborators"]
    C --> W4["When<br/>Timing and deadline"]
    C --> W5["Where<br/>Location and scope"]
    C --> H1["How<br/>Method and path"]
    C --> H2["How much<br/>Cost and benefit"]
    style C fill:#dae8fc,stroke:#6c8ebf
    style H2 fill:#ffe6cc,stroke:#d79b00
```

**When to use:** Assigning tasks, writing proposals, making reports, or checking for missed points in a retrospective.

---

### 3. OKR (Objectives and Key Results)

**One-liner:** The Objective is an inspiring qualitative goal; Key Results are measurable outcomes that show whether the goal is met.

```mermaid
flowchart TB
    O["O Objective<br/>Qualitative and aspirational<br/>Become the most trusted supplier this quarter"]
    O --> KR1["KR1 On-time delivery rate >= 98%"]
    O --> KR2["KR2 100% of complaints responded to within 24 hours"]
    O --> KR3["KR3 Customer satisfaction score >= 4.5"]
    style O fill:#dae8fc,stroke:#6c8ebf
    style KR1 fill:#d5e8d4,stroke:#82b366
    style KR2 fill:#d5e8d4,stroke:#82b366
    style KR3 fill:#d5e8d4,stroke:#82b366
```

**Key points:** One O with 3-5 KRs; 60-70% completion is ideal (shows the goal is challenging); do not tie directly to bonuses.

---

### 4. WBS Work Breakdown Structure (Decompose Tasks)

**One-liner:** Break a large project down by deliverables into small tasks that are actionable, assignable, and estimable.

```mermaid
flowchart TB
    P["Project: Company Annual Party"] --> A["1 Planning"]
    P --> B["2 Venue"]
    P --> C["3 Program"]
    P --> D["4 Logistics"]
    A --> A1["1.1 Set theme"]
    A --> A2["1.2 Prepare budget"]
    B --> B1["2.1 Compare hotels"]
    B --> B2["2.2 Sign contract"]
    C --> C1["3.1 Collect acts"]
    C --> C2["3.2 Rehearsal"]
    D --> D1["4.1 Catering"]
    D --> D2["4.2 Transport"]
    style P fill:#dae8fc,stroke:#6c8ebf
```

**Key points:** 100% rule — decomposition must cover all project work; lowest-level tasks should be finishable in 1-2 days.

---

### 5. Gantt Chart (Schedule)

**One-liner:** A horizontal timeline showing who does what when, and the dependencies between tasks.

```mermaid
gantt
    title Website Redesign Project Plan (Example)
    dateFormat YYYY-MM-DD
    section Planning
    Requirements research     :a1, 2026-11-01, 7d
    Solution design     :a2, after a1, 5d
    section Execution
    Development         :b1, after a2, 10d
    Integration testing     :b2, after b1, 5d
    section Closure
    Launch     :c1, after b2, 2d
    Retrospective     :c2, after c1, 3d
```

**When to use:** Project scheduling, cross-functional collaboration, and progress reporting to leadership.

---

## II. Problem Analysis

### 6. 5Why (Drill Down to Root Cause)

**One-liner:** Ask "why" repeatedly to get past symptoms and reach an actionable root cause.

```mermaid
flowchart TB
    Q0["Problem: Machine stopped on production line"]
    Q1["Why 1: Why did it stop?<br/>Overload fuse blew"]
    Q2["Why 2: Why did it overload?<br/>Lubrication pump strained"]
    Q3["Why 3: Why was it strained?<br/>Pump shaft worn, not turning smoothly"]
    Q4["Why 4: Why was it worn?<br/>Metal chips entered lubrication system"]
    Q5["Why 5: Why were there chips?<br/>No filter installed <- root cause"]
    A["Countermeasure: Install a filter to fix it permanently"]
    Q0 --> Q1 --> Q2 --> Q3 --> Q4 --> Q5 --> A
    style Q5 fill:#f8cecc,stroke:#b85450
    style A fill:#d5e8d4,stroke:#82b366
```

**Key points:** Ask "why," not "whose fault"; each link in the causal chain needs evidence — stop and check data when you cannot answer.

---

### 7. Fishbone / Cause-and-Effect Diagram (Find Causes Comprehensively)

**One-liner:** Brainstorm possible causes across dimensions such as Man, Machine, Material, Method, and Environment to avoid fixating on one angle.

```mermaid
flowchart LR
    M1["Man<br/>Skills, attitude, headcount"] --> P(("Product quality issue"))
    M2["Machine<br/>Equipment, tools, maintenance"] --> P
    M3["Material<br/>Raw materials, suppliers"] --> P
    M4["Method<br/>Process, standards, training"] --> P
    M5["Environment<br/>Temperature, lighting, site"] --> P
    style P fill:#f8cecc,stroke:#b85450
```

**Usage:** First diverge (brainstorm to fill every bone), then converge and use 5Why to dig deeper into the most suspicious bones. On shop floors, 4M1E / 6M are common (adding Measurement and Mother Nature).

---

### 8. 80/20 Rule / Pareto Principle (Catch the Main Contradiction)

**One-liner:** 80% of results often come from 20% of key factors — find that 20% first.

```mermaid
flowchart LR
    A["20% Vital Few<br/>Key customers / core issues / high-value work"] --> B["Drive 80% of results / loss"]
    C["80% Trivial Many"] --> D["Only 20% of results"]
    style A fill:#ffe6cc,stroke:#d79b00
    style B fill:#d5e8d4,stroke:#82b366
    style C fill:#f5f5f5,stroke:#999999
    style D fill:#f5f5f5,stroke:#999999
```

**When to use:** Prioritization, locating quality hotspots (Pareto chart), time management (eat the frog first).

---

## III. Decision & Analysis

### 9. SWOT (Strategic Direction)

**One-liner:** Lay internal strengths and weaknesses against external opportunities and threats, then derive action strategies.

```mermaid
quadrantChart
    title SWOT (X: Internal -> External; Y: Favorable -> Unfavorable)
    x-axis Internal --> External
    y-axis Favorable --> Unfavorable
    quadrant-2 Strengths S
    quadrant-1 Threats T
    quadrant-3 Opportunities O
    quadrant-4 Weaknesses W
```

**Example:** Strengths = strong technology, good brand; Weaknesses = weak channels, talent shortage; Opportunities = policy support, market growth; Threats = intensifying competition, substitutes emerging.

**Cross-quadrant strategies:**

| Combo | Strategy | Meaning |
|---|---|---|
| S + O | SO Growth | Use strengths to seize opportunities; attack aggressively |
| W + O | WO Turnaround | Fix weaknesses to capture opportunities |
| S + T | ST Defense | Use strengths to withstand threats |
| W + T | WT Contraction | Reduce investment and survive first |

---

### 10. Eisenhower Matrix (Time Management)

**One-liner:** Sort tasks by importance and urgency, and reserve energy for "important but not urgent" work.

```mermaid
quadrantChart
    title Eisenhower Matrix (X: Urgent -> Not Urgent; Y: Not Important -> Important)
    x-axis Urgent --> Not Urgent
    y-axis Not Important --> Important
    quadrant-2 1 Do First
    quadrant-1 2 Schedule - Focus Here
    quadrant-3 3 Delegate / Handle Quickly
    quadrant-4 4 Reduce / Drop
```

- **1 Important + Urgent** (crises, deadlines) → Do immediately
- **2 Important + Not Urgent** (planning, learning, prevention, exercise) → Do with a plan, **highest value**
- **3 Not Important + Urgent** (interruptions, some meetings) → Delegate or handle quickly
- **4 Not Important + Not Urgent** (mindless scrolling, idle chat) → Reduce or skip

**Core insight:** High performers spend most of their time in Q2; Q1 keeps catching fire precisely because Q2 is neglected.

---

### 11. Six Thinking Hats (Team Discussion)

**One-liner:** Wear one hat at a time and use only one mode of thinking, avoiding arguments and mental chaos.

```mermaid
flowchart LR
    M["Topic"] --- W1["White Hat<br/>Facts and data"]
    M --- W2["Red Hat<br/>Intuition and feelings"]
    M --- W3["Black Hat<br/>Risks and criticism"]
    M --- W4["Yellow Hat<br/>Value and benefits"]
    M --- W5["Green Hat<br/>Creativity and new options"]
    M --- W6["Blue Hat<br/>Process and summary"]
    style W1 fill:#f5f5f5,stroke:#999999
    style W2 fill:#f8cecc,stroke:#b85450
    style W3 fill:#333333,color:#ffffff
    style W4 fill:#ffe6cc,stroke:#d79b00
    style W5 fill:#d5e8d4,stroke:#82b366
    style W6 fill:#dae8fc,stroke:#6c8ebf
```

**Typical sequence:** Blue (set process) → White (state facts) → Green (generate options) → Yellow (see value) → Black (find risks) → Red (share feelings) → Blue (decide).

---

### 12. BCG Boston Matrix (Portfolio Decision)

**One-liner:** Classify businesses by market growth rate and relative market share, then decide whether to invest or harvest.

```mermaid
quadrantChart
    title BCG Matrix (X: Low Relative Share -> High; Y: Low Market Growth -> High)
    x-axis Low Share --> High Share
    y-axis Low Growth --> High Growth
    quadrant-2 Question Mark - Selective nurture
    quadrant-1 Star - Invest more
    quadrant-3 Dog - Shrink or exit
    quadrant-4 Cash Cow - Harvest cash to feed stars
```

---

### 13. Porter's Five Forces (Industry Competition)

**One-liner:** Industry attractiveness is shaped by five forces; analyze them before deciding whether and how to enter.

```mermaid
flowchart TB
    T1["Rivalry among existing competitors<br/>Concentration, price wars"] --- C(("Industry<br/>Profit potential"))
    T2["Supplier bargaining power"] --- C
    T3["Buyer bargaining power"] --- C
    T4["Threat of new entrants<br/>Barrier height"] --- C
    T5["Threat of substitutes"] --- C
    style C fill:#dae8fc,stroke:#6c8ebf
```

**The stronger the five forces, the lower the industry's average profit.**

---

### 14. MECE (Structured Breakdown)

**One-liner:** Categorize so categories are Mutually Exclusive and Collectively Exhaustive — no overlap, no omission.

```mermaid
flowchart TB
    T["Question: How to improve user satisfaction?"] --> A["Product experience"]
    T --> B["Pricing"]
    T --> C["Service quality"]
    A --- B
    B --- C
    style T fill:#dae8fc,stroke:#6c8ebf
    style A fill:#d5e8d4,stroke:#82b366
    style B fill:#ffe6cc,stroke:#d79b00
    style C fill:#e1d5e7,stroke:#9673a6
```

**Test:** If any two items can be merged, they are not mutually exclusive; if you can name a counterexample, they are not collectively exhaustive. MECE is a foundational skill of the pyramid principle and McKinsey-style consulting.

---

## IV. Communication & Expression

### 15. Pyramid Principle / SCQA (Reporting and Writing)

**One-liner:** Lead with the conclusion, support from above, group by category, and progress logically.

```mermaid
flowchart TB
    S1["S Situation<br/>Start with shared background"] --> C1["C Complication<br/>What changed / what is the problem"]
    C1 --> Q1["Q Question<br/>Naturally raises the key question"]
    Q1 --> A1["A Answer<br/>Give conclusion and solution (main point first)"]
    style A1 fill:#d5e8d4,stroke:#82b366
```

**Contrast:** "Boss, here is the budget, headcount, and progress... so I want to add people" (long buildup)
**SCQA:** "Boss, the project is at risk of delay (C). I recommend adding 2 developers (A). The reason is... (S + Q details)"

---

### 16. Golden Circle (Inspirational Communication)

**One-liner:** Great organizations communicate from "why"; mediocre ones only talk about "what."

```mermaid
flowchart TB
    WHY["WHY<br/>Purpose and belief (moves people)"] --> HOW["HOW<br/>Method and differentiation"] --> WHAT["WHAT<br/>Product and result (everyone says this)"]
    style WHY fill:#f8cecc,stroke:#b85450
    style HOW fill:#ffe6cc,stroke:#d79b00
    style WHAT fill:#d5e8d4,stroke:#82b366
```

**Example:** Apple does not say "We make computers (What)"; it says "We believe in challenging the status quo (Why), so we design differently (How), and that produces great computers (What)."

---

## V. Execution & Improvement

### 17. PDCA Cycle (Continuous Improvement)

**One-liner:** Plan, Do, Check, Act — repeat the cycle, and level up with each turn.

```mermaid
flowchart LR
    P["1 Plan<br/>Find problem, set goal, design solution"] --> D["2 Do<br/>Pilot implement, record data"]
    D --> C["3 Check<br/>Compare with goal, find gaps"]
    C --> A["4 Act<br/>Standardize; remaining issues go to next cycle"]
    A -->|"New cycle, step up"| P
    style P fill:#dae8fc,stroke:#6c8ebf
    style D fill:#d5e8d4,stroke:#82b366
    style C fill:#ffe6cc,stroke:#d79b00
    style A fill:#f8cecc,stroke:#b85450
```

**Key points:** Check is the step most people skip; in Act, practices proven effective should be standardized (this is the basis of "big cycle containing small cycles" improvement).

---

### 18. DMAIC (Six Sigma Improvement)

**One-liner:** A data-driven five-step process for solving complex quality problems; heavier on measurement and statistics than PDCA.

```mermaid
flowchart LR
    D["Define<br/>Clarify problem and customer needs"] --> M["Measure<br/>Collect data, quantify current state"]
    M --> A["Analyze<br/>Use statistics to find key causes"]
    A --> I["Improve<br/>Design and validate solution"]
    I --> C["Control<br/>Standardize and monitor to prevent relapse"]
    C -.->|"Continuous monitoring"| D
    style D fill:#dae8fc,stroke:#6c8ebf
    style M fill:#d5e8d4,stroke:#82b366
    style A fill:#ffe6cc,stroke:#d79b00
    style I fill:#e1d5e7,stroke:#9673a6
    style C fill:#f8cecc,stroke:#b85450
```

**When to use:** Manufacturing quality improvement, high defect rates, complex problems with sufficient data.

---

### 19. 8D Report (Customer Complaint / Quality Incident Handling)

**One-liner:** The automotive industry's standard team-based problem-solving process: D3 stops the bleeding first, then D4-D5 fix the root cause.

```mermaid
flowchart TB
    D0["D0 Prepare: decide if 8D is needed"] --> D1["D1 Build the team"]
    D1 --> D2["D2 Describe the problem (5W2H)"]
    D2 --> D3["D3 Containment action (stop the bleeding)"]
    D3 --> D4["D4 Root cause analysis (5Why / fishbone)"]
    D4 --> D5["D5 Permanent corrective action"]
    D5 --> D6["D6 Verify effectiveness"]
    D6 --> D7["D7 Prevent recurrence (standardize)"]
    D7 --> D8["D8 Recognize team and close the issue"]
    style D3 fill:#ffe6cc,stroke:#d79b00
    style D5 fill:#d5e8d4,stroke:#82b366
```

**Note:** Talking about a permanent fix without D3 containment is like performing surgery while the patient is bleeding out.

---

### 20. GRAI Retrospective (Turn Experience into Capability)

**One-liner:** Goal-Result-Analysis-Insight — four steps to turn "what happened" into "what to do next time."

```mermaid
flowchart LR
    G["G Goal Review<br/>What did we originally want?"] --> R["R Result Assessment<br/>What actually happened? Where are the gaps?"]
    R --> A["A Analysis<br/>Root causes of what went right / wrong"]
    A --> I["I Insight<br/>Reusable patterns: stop / continue / start"]
    I --> G2["Feed into next goal (PDCA closed loop)"]
    style G fill:#dae8fc,stroke:#6c8ebf
    style R fill:#d5e8d4,stroke:#82b366
    style A fill:#ffe6cc,stroke:#d79b00
    style I fill:#f8cecc,stroke:#b85450
```

**Key point:** A retrospective is not a blame session; judge the issue, not the person. Insight must translate into "what specifically to do next time."

---

## Ready-Made Open Resources

| Resource | Description |
|---|---|
| [mermaid-js/mermaid](https://github.com/mermaid-js/mermaid) | The open-source chart engine used for all diagrams in this file |
| [MackDing/mentalModelMap](https://github.com/MackDing/mentalModelMap) | 79 classic mental-model visual maps (Chinese, open source) |
| ["12 Tools for Life" PDF](http://chenweixiang.github.io/docs/12_tools_for_everyone.pdf) | Illustrated collection of SWOT/PDCA/6W2H/SMART/WBS/80-20 and more |
| [drawio (diagrams.net)](https://app.diagrams.net) | Free open-source diagramming tool with built-in management chart templates |
| [Excalidraw](https://excalidraw.com) | Open-source hand-drawn style whiteboard, great for quick framework sketches |
| [Miro Templates](https://miro.com/templates) | Huge library of ready-made templates for SWOT, fishbone, 5Why, etc. (some free) |
| [5xWhys Free Tools](https://5xwhys.com/tools/) | Online generators for 5Why, fishbone, and Pareto charts with export options |

## Usage Tips

1. **Start with the roadmap:** Pick a tool by your current task type; do not try to use all 20.
2. **Combine tools:** Use 5W2H to describe the problem (D2 in 8D) → fishbone to diverge → 5Why to converge on root cause → PDCA to track improvement.
3. **Edit diagrams:** Just change the text inside the `mermaid` code blocks; GitHub, Typora, and `index.html` will update automatically.
