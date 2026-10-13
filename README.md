# 管理方法论图解（开源 · 可编辑 · 共 20 个）

**语言 Language Ngôn ngữ**：**中文** · [English](README.en.md) · [Tiếng Việt](README.vi.md)

所有图解均使用 **Mermaid** 文本语法绘制（开源格式，[mermaid-js/mermaid](https://github.com/mermaid-js/mermaid) 82k+ stars）。
任何支持 Mermaid 的工具都能直接渲染成图：

- **本目录的 `index.html`**：双击即可在浏览器中查看渲染好的全套图解（无需安装任何东西）
- **GitHub / Gitee**：直接上传，自动渲染
- **VS Code**：装插件 "Markdown Preview Mermaid Support"
- **Typora / Obsidian**：原生支持

修改图解只需改文本，无需绘图软件。

## 按场景速查

| 你要做的事 | 推荐工具 |
|---|---|
| 定目标 | SMART、OKR、5W2H |
| 做计划 / 拆解任务 | 5W2H、WBS、甘特图 |
| 找问题根因 | 5Why、鱼骨图、二八法则 |
| 做决策 / 分析 | SWOT、艾森豪威尔四象限、六顶思考帽、BCG 矩阵、波特五力 |
| 抓执行 / 持续改进 | PDCA、DMAIC、8D |
| 沟通与表达 | 金字塔原理、黄金圈法则 |
| 复盘总结 | GRAI 复盘法 |

## 工具选择路线图

```mermaid
flowchart TB
    Q{"你现在要做什么？"}
    Q --> A["定目标"] --> A1["SMART / OKR"]
    Q --> B["做计划"] --> B1["5W2H / WBS / 甘特图"]
    Q --> C["找原因"] --> C1["5Why / 鱼骨图"]
    Q --> D["做决策"] --> D1["SWOT / 四象限 / 六顶思考帽"]
    Q --> E["抓执行"] --> E1["PDCA / DMAIC / 8D"]
    Q --> F["做复盘"] --> F1["GRAI / 金字塔原理"]
    style Q fill:#dae8fc,stroke:#6c8ebf
```

---

## 一、目标与计划类

### 1. SMART 原则（定目标）

**一句话**：好目标必须具体、可衡量、可实现、相关联、有时限。

```mermaid
flowchart LR
    G["SMART 好目标"] --> S["S 具体 Specific<br/>目标清晰，不模糊"]
    G --> M["M 可衡量 Measurable<br/>有数字，可验证"]
    G --> A["A 可实现 Achievable<br/>跳一跳够得着"]
    G --> R["R 相关联 Relevant<br/>与总目标对齐"]
    G --> T["T 有时限 Time-bound<br/>有明确 deadline"]
    style G fill:#dae8fc,stroke:#6c8ebf
    style S fill:#d5e8d4,stroke:#82b366
    style M fill:#ffe6cc,stroke:#d79b00
    style A fill:#fff2cc,stroke:#d6b656
    style R fill:#e1d5e7,stroke:#9673a6
    style T fill:#f8cecc,stroke:#b85450
```

**反例**：「提升客户满意度」（模糊）
**正例**：「3 个月内，将客服首次响应时间从 4 小时降至 1 小时以内」（SMART 全满足）

---

### 2. 5W2H 分析法（把一件事想清楚）

**一句话**：用 7 个问题把任务/方案的全貌问出来，防止遗漏、杜绝盲目。

```mermaid
flowchart TB
    C["5W2H 七问分析法"]
    C --> W1["What 做什么？<br/>任务内容与目标"]
    C --> W2["Why 为什么？<br/>理由与目的"]
    C --> W3["Who 谁来做？<br/>负责人与协作方"]
    C --> W4["When 何时？<br/>时间与期限"]
    C --> W5["Where 何处？<br/>地点与范围"]
    C --> H1["How 怎么做？<br/>方法与路径"]
    C --> H2["How much 多少？<br/>成本与收益"]
    style C fill:#dae8fc,stroke:#6c8ebf
    style H2 fill:#ffe6cc,stroke:#d79b00
```

**何时用**：布置任务、写方案、做汇报、复盘检查遗漏。

---

### 3. OKR（目标与关键结果）

**一句话**：O 是鼓舞人心的定性目标，KR 是衡量目标是否达成的量化结果。

```mermaid
flowchart TB
    O["O 目标（定性、有挑战）<br/>本季度成为客户最信赖的供应商"]
    O --> KR1["KR1 准时交付率 ≥ 98%"]
    O --> KR2["KR2 客诉 24 小时响应率 100%"]
    O --> KR3["KR3 客户满意度评分 ≥ 4.5 分"]
    style O fill:#dae8fc,stroke:#6c8ebf
    style KR1 fill:#d5e8d4,stroke:#82b366
    style KR2 fill:#d5e8d4,stroke:#82b366
    style KR3 fill:#d5e8d4,stroke:#82b366
```

**要点**：1 个 O 配 3-5 个 KR；完成 60-70% 最佳（说明目标有挑战）；不与奖金直接挂钩。

---

### 4. WBS 工作分解结构（拆任务）

**一句话**：把大项目按「可交付成果」逐层拆解到「可执行、可分配、可估算」的小任务。

```mermaid
flowchart TB
    P["项目：公司年会"] --> A["1 策划"]
    P --> B["2 场地"]
    P --> C["3 节目"]
    P --> D["4 后勤"]
    A --> A1["1.1 确定主题"]
    A --> A2["1.2 编制预算"]
    B --> B1["2.1 酒店比选"]
    B --> B2["2.2 签订合同"]
    C --> C1["3.1 节目征集"]
    C --> C2["3.2 彩排"]
    D --> D1["4.1 餐饮安排"]
    D --> D2["4.2 车辆调度"]
    style P fill:#dae8fc,stroke:#6c8ebf
```

**要点**：100% 原则——拆解要覆盖项目全部工作；最底层任务 1-2 天内能完成。

---

### 5. 甘特图（排进度）

**一句话**：横向时间轴上看清「谁在什么时间做什么、前后依赖关系」。

```mermaid
gantt
    title 网站改版项目计划（示例）
    dateFormat YYYY-MM-DD
    section 规划
    需求调研     :a1, 2026-11-01, 7d
    方案设计     :a2, after a1, 5d
    section 执行
    开发         :b1, after a2, 10d
    联调测试     :b2, after b1, 5d
    section 收尾
    上线发布     :c1, after b2, 2d
    复盘总结     :c2, after c1, 3d
```

**何时用**：项目排期、跨部门协作、向上汇报进度。

---

## 二、问题分析类

### 6. 5Why 分析法（追问根因）

**一句话**：对一个连续追问「为什么」，穿过表象直到找到可采取行动的根本原因。

```mermaid
flowchart TB
    Q0["问题：生产线机器停了"]
    Q1["Why 1：为什么停了？<br/>过载保险丝烧断"]
    Q2["Why 2：为什么过载？<br/>润滑泵超负荷运转"]
    Q3["Why 3：为什么超负荷？<br/>泵轴磨损、转动不畅"]
    Q4["Why 4：为什么磨损？<br/>金属屑进入润滑系统"]
    Q5["Why 5：为什么有金属屑？<br/>没装过滤器 ← 根本原因"]
    A["对策：加装过滤器，根治问题"]
    Q0 --> Q1 --> Q2 --> Q3 --> Q4 --> Q5 --> A
    style Q5 fill:#f8cecc,stroke:#b85450
    style A fill:#d5e8d4,stroke:#82b366
```

**要点**：问「为什么」不是问「谁的责任」；每条因果链要有证据，回答不了就停下来查数据。

---

### 7. 鱼骨图 / 因果图（全面找原因）

**一句话**：从人、机、料、法、环等维度穷举所有可能原因，避免只盯一个方向。

```mermaid
flowchart LR
    M1["人 Man<br/>技能、态度、数量"] --> P(("产品质量问题"))
    M2["机 Machine<br/>设备、工具、维护"] --> P
    M3["料 Material<br/>原料、供应商"] --> P
    M4["法 Method<br/>流程、标准、培训"] --> P
    M5["环 Environment<br/>温度、照明、现场"] --> P
    style P fill:#f8cecc,stroke:#b85450
```

**用法**：先发散（头脑风暴把鱼骨填满），收敛后用 5Why 对最可疑的几根骨头深挖。生产现场常用 4M1E / 6M（再加测量 Measurement、自然 Mother Nature）。

---

### 8. 二八法则 / 帕累托法则（抓主要矛盾）

**一句话**：80% 的结果往往由 20% 的关键因素决定，先找到那 20%。

```mermaid
flowchart LR
    A["20% 关键少数<br/>主要客户 / 核心问题 / 高价值工作"] --> B["贡献 80% 的业绩 / 损失"]
    C["80% 琐碎多数"] --> D["只贡献 20% 的结果"]
    style A fill:#ffe6cc,stroke:#d79b00
    style B fill:#d5e8d4,stroke:#82b366
    style C fill:#f5f5f5,stroke:#999999
    style D fill:#f5f5f5,stroke:#999999
```

**何时用**：排优先级、找质量问题集中点（帕累托图）、时间管理（先吃掉那只青蛙）。

---

## 三、决策与分析类

### 9. SWOT 分析（定战略方向）

**一句话**：把内部优劣与外部机会威胁摆到一张图上，组合出行动策略。

```mermaid
quadrantChart
    title SWOT 分析（横轴：内部 → 外部；纵轴：有利 → 不利）
    x-axis 内部 --> 外部
    y-axis 有利 --> 不利
    quadrant-2 优势 S
    quadrant-1 威胁 T
    quadrant-3 机会 O
    quadrant-4 劣势 W
```

**示例**：优势=技术强、品牌好；劣势=渠道弱、人才缺；机会=政策扶持、市场增长；威胁=竞争加剧、替代品出现。

**四象组合策略**：

| 组合 | 策略 | 含义 |
|---|---|---|
| S + O | SO 增长型 | 用优势抓机会，全力进攻 |
| W + O | WO 扭转型 | 补短板抓机会 |
| S + T | ST 防御型 | 用优势抵御威胁 |
| W + T | WT 收缩型 | 减少投入，先活下来 |

---

### 10. 艾森豪威尔四象限（时间管理）

**一句话**：按「重要 / 紧急」分四类，把精力留给「重要不紧急」的事。

```mermaid
quadrantChart
    title 艾森豪威尔四象限（横轴：紧急 → 不紧急；纵轴：不重要 → 重要）
    x-axis 紧急 --> 不紧急
    y-axis 不重要 --> 重要
    quadrant-2 ① 立即做
    quadrant-1 ② 计划做（重点投入）
    quadrant-3 ③ 授权 / 速办
    quadrant-4 ④ 少做 / 不做
```

- **① 重要 + 紧急**（危机、临期任务）→ 立即做
- **② 重要 + 不紧急**（规划、学习、预防、锻炼）→ 有计划地做，**价值最高**
- **③ 不重要 + 紧急**（临时打扰、部分会议）→ 授权他人或速办
- **④ 不重要 + 不紧急**（无目的刷屏、闲聊）→ 减少或不做

**核心洞察**：高效的人把大部分时间投在 Q2；Q1 之所以总着火，正是因为 Q2 做得不够。

---

### 11. 六顶思考帽（团队讨论）

**一句话**：一次只戴一顶帽子、只用一种思维方式讨论，避免争吵和思维混乱。

```mermaid
flowchart LR
    M["议题"] --- W1["白帽<br/>客观事实与数据"]
    M --- W2["红帽<br/>直觉与感受"]
    M --- W3["黑帽<br/>风险与批判"]
    M --- W4["黄帽<br/>价值与收益"]
    M --- W5["绿帽<br/>创意与新方案"]
    M --- W6["蓝帽<br/>流程与总结"]
    style W1 fill:#f5f5f5,stroke:#999999
    style W2 fill:#f8cecc,stroke:#b85450
    style W3 fill:#333333,color:#ffffff
    style W4 fill:#ffe6cc,stroke:#d79b00
    style W5 fill:#d5e8d4,stroke:#82b366
    style W6 fill:#dae8fc,stroke:#6c8ebf
```

**典型顺序**：蓝（定流程）→ 白（摆事实）→ 绿（出方案）→ 黄（看价值）→ 黑（找风险）→ 红（表态度）→ 蓝（拍结论）。

---

### 12. BCG 波士顿矩阵（业务组合决策）

**一句话**：按「市场增长率 × 相对份额」把业务分成四类，决定投入还是收割。

```mermaid
quadrantChart
    title BCG 波士顿矩阵（横轴：相对市场份额低 → 高；纵轴：市场增长率低 → 高）
    x-axis 份额低 --> 份额高
    y-axis 增长率低 --> 增长率高
    quadrant-2 问号：选择性培育
    quadrant-1 明星：加大投入
    quadrant-3 瘦狗：收缩或退出
    quadrant-4 现金牛：收割现金，反哺明星
```

---

### 13. 波特五力模型（行业竞争分析）

**一句话**：行业吸引力由五种力量决定，分析清楚再决定进不进、怎么进。

```mermaid
flowchart TB
    T1["现有竞争者的竞争<br/>集中度、价格战"] --- C(("行业<br/>盈利潜力"))
    T2["供应商议价能力"] --- C
    T3["购买者议价能力"] --- C
    T4["新进入者威胁<br/>壁垒高低"] --- C
    T5["替代品威胁"] --- C
    style C fill:#dae8fc,stroke:#6c8ebf
```

**五种力量越强，行业平均利润越低。**

---

### 14. MECE 原则（结构化拆解）

**一句话**：分类要做到「相互独立、完全穷尽」——不重、不漏。

```mermaid
flowchart TB
    T["问题：如何提升用户满意度？"] --> A["产品体验"]
    T --> B["价格因素"]
    T --> C["服务质量"]
    A --- B
    B --- C
    style T fill:#dae8fc,stroke:#6c8ebf
    style A fill:#d5e8d4,stroke:#82b366
    style B fill:#ffe6cc,stroke:#d79b00
    style C fill:#e1d5e7,stroke:#9673a6
```

**检验方法**：把任意两项放一起，能合并就说明不独立；能举出反例就说明不穷尽。它是金字塔原理和麦肯锡式咨询的基本功。

---

## 四、沟通与表达类

### 15. 金字塔原理 / SCQA（汇报与写作）

**一句话**：结论先行、以上统下、归类分组、逻辑递进。

```mermaid
flowchart TB
    S1["S 情境 Situation<br/>先讲双方认可的背景"] --> C1["C 冲突 Complication<br/>发生了什么变化 / 问题"]
    C1 --> Q1["Q 疑问 Question<br/>自然引出关键问题"]
    Q1 --> A1["A 回答 Answer<br/>给出结论和方案（先说重点）"]
    style A1 fill:#d5e8d4,stroke:#82b366
```

**对比**：「领导，预算、人手、进度是这样的……所以我想申请加人」（铺垫半天）
**SCQA**：「领导，项目有延期风险（C）。建议增加 2 名开发（A）。原因是……（S+Q 细节）」

---

### 16. 黄金圈法则（激励性表达）

**一句话**：卓越的组织从「为什么」开始沟通，平庸的组织只讲「做什么」。

```mermaid
flowchart TB
    WHY["WHY 为什么做<br/>使命、信念（打动人）"] --> HOW["HOW 怎么做<br/>方法、差异化"] --> WHAT["WHAT 做什么<br/>产品、结果（人人会说）"]
    style WHY fill:#f8cecc,stroke:#b85450
    style HOW fill:#ffe6cc,stroke:#d79b00
    style WHAT fill:#d5e8d4,stroke:#82b366
```

**例子**：苹果公司不说「我们造电脑（What）」，而说「我们相信挑战现状（Why），所以我们用与众不同的方式设计（How），造出好用的电脑（What）」。

---

## 五、执行与改进类

### 17. PDCA 循环（持续改进）

**一句话**：计划—执行—检查—处理，循环不止，每转一圈水平上一个台阶。

```mermaid
flowchart LR
    P["① Plan 计划<br/>找问题、定目标、定方案"] --> D["② Do 执行<br/>小范围实施、记录数据"]
    D --> C["③ Check 检查<br/>对比目标、找偏差"]
    C --> A["④ Act 处理<br/>标准化；遗留问题进入下轮"]
    A -->|"新一轮循环，阶梯式上升"| P
    style P fill:#dae8fc,stroke:#6c8ebf
    style D fill:#d5e8d4,stroke:#82b366
    style C fill:#ffe6cc,stroke:#d79b00
    style A fill:#f8cecc,stroke:#b85450
```

**要点**：Check 是多数人跳过的环节；Act 里被验证有效的做法要固化为标准（这是「大环套小环」改进的基础）。

---

### 18. DMAIC（六西格玛改进流程）

**一句话**：用数据驱动五步流程解决复杂质量问题，比 PDCA 更重测量与统计。

```mermaid
flowchart LR
    D["Define 定义<br/>明确问题与客户需求"] --> M["Measure 测量<br/>收集数据，量化现状"]
    M --> A["Analyze 分析<br/>用统计方法找关键原因"]
    A --> I["Improve 改进<br/>设计并验证解决方案"]
    I --> C["Control 控制<br/>固化标准，监控防反弹"]
    C -.->|"持续监控"| D
    style D fill:#dae8fc,stroke:#6c8ebf
    style M fill:#d5e8d4,stroke:#82b366
    style A fill:#ffe6cc,stroke:#d79b00
    style I fill:#e1d5e7,stroke:#9673a6
    style C fill:#f8cecc,stroke:#b85450
```

**何时用**：制造业质量改进、流程缺陷率高、数据充分的复杂问题。

---

### 19. 8D 报告（客诉 / 质量事故处理）

**一句话**：汽车行业标准的团队化问题解决流程，D3 先止血，D4-D5 再根治。

```mermaid
flowchart TB
    D0["D0 准备：判定是否需要 8D"] --> D1["D1 组建团队"]
    D1 --> D2["D2 描述问题（5W2H）"]
    D2 --> D3["D3 临时围堵措施（先止血）"]
    D3 --> D4["D4 根因分析（5Why / 鱼骨图）"]
    D4 --> D5["D5 永久纠正措施"]
    D5 --> D6["D6 验证措施有效性"]
    D6 --> D7["D7 预防再发（标准化）"]
    D7 --> D8["D8 表彰团队，关闭问题"]
    style D3 fill:#ffe6cc,stroke:#d79b00
    style D5 fill:#d5e8d4,stroke:#82b366
```

**注意**：没有 D3 止血就谈根治，等于一边流血一边做手术。

---

### 20. GRAI 复盘法（把经验变成能力）

**一句话**：目标—结果—分析—总结，四步把「发生过的事」变成「下次用得上的经验」。

```mermaid
flowchart LR
    G["G Goal 目标回顾<br/>当初想达成什么？"] --> R["R Result 结果评估<br/>实际发生了什么？差距在哪？"]
    R --> A["A Analysis 原因分析<br/>做对/做错的根本原因"]
    A --> I["I Insight 经验总结<br/>可复用的规律，停止/继续/开始做"]
    I --> G2["进入下一轮目标（PDCA 闭环）"]
    style G fill:#dae8fc,stroke:#6c8ebf
    style R fill:#d5e8d4,stroke:#82b366
    style A fill:#ffe6cc,stroke:#d79b00
    style I fill:#f8cecc,stroke:#b85450
```

**关键**：复盘不是追责会，只对事不对人；Insight 必须落到「下次具体怎么做」。

---

## 现成的开源资源

| 资源 | 说明 |
|---|---|
| [mermaid-js/mermaid](https://github.com/mermaid-js/mermaid) | 本文件全部图解使用的开源图表引擎 |
| [MackDing/mentalModelMap](https://github.com/MackDing/mentalModelMap) | 79 个经典思维模型可视化导图（中文，开源） |
| [《12 个人生工具》PDF](http://chenweixiang.github.io/docs/12_tools_for_everyone.pdf) | SWOT/PDCA/6W2H/SMART/WBS/二八原则等图解合集 |
| [drawio（diagrams.net）](https://app.diagrams.net) | 开源免费绘图工具，自带管理图表模板库 |
| [Excalidraw](https://excalidraw.com) | 开源手绘风白板，适合快速画框架图 |
| [Miro 模板库](https://miro.com/templates) | SWOT/鱼骨图/5Why 等海量现成模板（部分免费） |
| [5xWhys 免费工具](https://5xwhys.com/tools/) | 5Why / 鱼骨图 / 帕累托在线生成，可导出 |

## 使用建议

1. **先看路线图**：按你当前的任务类型选工具，不要 20 个全用。
2. **组合使用**：5W2H 描述问题（8D 的 D2）→ 鱼骨图发散 → 5Why 收敛根因 → PDCA 跟踪改进。
3. **修改图解**：直接改 ```mermaid 代码块里的文字即可，保存后 GitHub / Typora / `index.html` 会自动更新。
