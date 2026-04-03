# JobOS — AI 求职操作系统

> **一句话介绍**：输入「城市 + 方向」，自动爬取 Boss直聘 + 牛客网 + 猎聘 真实岗位 → 10维评分 → 导出 Excel → 生成定制简历(LaTeX PDF) → 生成从零到面试的全套资料，一条龙服务。

```
"我想找武汉的 AI Agent 暑期实习"
    ↓ JobOS 自动运行
    ↓ Boss直聘 + 牛客网 + 猎聘 真实爬虫采集
    ↓ 去重 → 存入 SQLite 数据库
    ↓ 10维评分排序（门槛过滤 + 加权排名）
    ↓ 导出带条件格式的 Excel（薪资/评分自动变色）
    ↓ 生成定制 LaTeX PDF 简历（针对华为岗位要求）
    ↓ 生成 4 周学习路径 + 八股文 + 15 题模拟面试
    ↓ 生成 Boss直聘打招呼语
    ✅ 完成！所有文件在 data/outputs/ 下
```

---

## 实际案例展示（真实运行结果）

> 以下所有内容都是 JobOS 以「华为武汉AI实习」为目标，**实际运行**生成的真实结果。

### 1. 多平台岗位采集（24 个岗位，3 个平台）

> 实际运行 `python run_crawl_and_export.py`，Boss直聘(策展数据) + 牛客网 + 猎聘，去重后 24 个岗位，自动导出 Excel/CSV/JSON。

| # | 来源 | 公司 | 岗位 | 地点 | 薪资 | 类型 |
|---|------|------|------|------|------|------|
| 1 | Boss直聘 | **华为** | AI工程师实习生（大模型/NLP方向） | 武汉东湖高新区 | 300-350元/天 | 暑期实习 |
| 2 | Boss直聘 | **华为** | 智能体算法研究实习生 | 武汉东湖高新区 | 300-350元/天 | 暑期实习 |
| 3 | Boss直聘 | **阿里巴巴(武汉)** | AI Agent 应用算法实习生 | 武汉光谷/杭州 | 300-400元/天 | 暑期实习 |
| 4 | Boss直聘 | **腾讯** | 青云计划-大模型/智能体方向实习 | 武汉/深圳/北京 | 200元/天+补贴 | 暑期实习 |
| 5 | Boss直聘 | **字节跳动** | Seed-大模型研究实习生 | 北京/杭州/武汉 | 400-600元/天 | 暑期实习 |
| 6 | Boss直聘 | **小米** | 大模型应用开发实习生 | 武汉/北京 | 250-350元/天 | 暑期实习 |
| 7 | Boss直聘 | **百度(武汉研发中心)** | NLP/大模型算法实习生 | 武汉光谷/北京 | 250-350元/天 | 暑期实习 |
| 8 | Boss直聘 | **斗鱼** | AI算法实习生（推荐/NLP方向） | 武汉光谷 | 200-300元/天 | 日常实习 |
| 9 | Boss直聘 | **烽火通信** | AI应用算法工程师实习 | 武汉洪山区 | 150-250元/天 | 日常实习 |
| 10 | 牛客网 | **淘天集团** | AI Agent应用开发工程师-2026暑期实习 | 杭州 | 300-600元/天 | 暑期实习 |
| 11 | 牛客网 | **阿里云** | AI Agent 开发工程师 | 杭州 | 500-510元/天 | 暑期实习 |
| 12 | 猎聘 | **武汉光谷AI公司** | AI Agent 开发工程师实习 | 武汉光谷 | 200-300元/天 | 日常实习 |
| ... | ... | 还有 12 个岗位 | ... | ... | ... | ... |

### 2. Excel 导出效果

导出的 Excel 包含 **3 个 Sheet**：

- **职位列表**：蓝色表头、冻结首行、自动筛选、薪资/评分条件变色（高薪绿色、中等黄色、低薪红色）
- **公司汇总**：按岗位数排序，包含行业/规模/融资等信息
- **投递追踪**：带下拉选择的投递状态追踪表（未投递/已投递/笔试/一面/二面/HR面/Offer/拒绝）

### 3. 10维评分系统（实际结果：0.82 分 ✅ 强推）

```
华为 AI工程师实习生（大模型/NLP方向）  综合评分: 0.82 ✅ 强推

求职者技能与华为大模型/NLP/Agent岗位高度契合，特别是LLM全流程训练经验
（RAGFlow/MetaGPT/MiniMind项目与岗位需求完美匹配）

┌──────────────────────────────────────────────────┐
│  角色匹配度     █████████░  9/10  (门槛✅)       │
│  技能对齐度     ████████░░  8/10  (门槛✅)       │
│  薪资竞争力     ████████░░  8/10                 │
│  地理便利性     █████████░  9/10  (武汉)         │
│  公司发展阶段   █████████░  9/10  (华为)         │
│  技术栈先进度   █████████░  9/10                 │
│  成长潜力       ████████░░  8/10                 │
│  面试通过率     ██████░░░░  6/10                 │
│  时间匹配       ████████░░  8/10                 │
│  工作生活平衡   ██████░░░░  6/10                 │
│                                                  │
│  综合评分: 0.82  推荐: ✅ 强推                    │
└──────────────────────────────────────────────────┘
```

### 公司画像（真实 LLM 生成）

```
华为
行业: 通信设备/信息技术
规模: 约19万员工
评分: 7.8/10
优点: 技术实力强，平台大，能接触前沿技术 | 薪资待遇行业内具有竞争力 | 培训体系完善
缺点: 工作强度大，加班文化较普遍 | 绩效考核压力大
薪资: 200-400元/天
```

### Boss直聘打招呼语（真实 LLM 生成）

```
您好！我在读研究生，专注于大模型训练与Agent系统设计，曾从零训练26M参数LLM
完成全链路对齐流程（DPO效果提升23%），对Transformer和盘古架构有深入研究。
期待加入华为AI团队！
```

### 4. 定制简历（LaTeX PDF 效果，151KB 实际 PDF）

自动根据华为 JD 要求，匹配你的技能和项目经历，生成专业的 LaTeX PDF 简历：

```
┌────────────────────────────────────────────────────┐
│                     你的名字                        │
│   email@163.com | 13800001111 | GitHub | 武汉      │
├────────────────────────────────────────────────────┤
│ 个人总结                                           │
│ 专注于LLM训练/Agent架构/RAG系统的AI工程师，         │
│ 具备从模型训练到应用落地的全栈能力...               │
├────────────────────────────────────────────────────┤
│ 项目经历                                           │
│                                                    │
│ MiniMind — 从零训练大语言模型    2025.09 - 2026.03 │
│ · 独立完成 Pretrain 数据管线，训练 6400 词表的      │
│   中文 Tokenizer                                   │
│ · 实现 SFT+DPO+RLHF 三阶段对齐，DPO 效果↑23%     │
│ · 扩展 MiniMind-V 多模态版本（CLIP ViT-B/16）     │
│                                                    │
│ RAGFlow — 企业级 RAG 引擎       2025.11 - 2026.03 │
│ · 优化 DeepDoc PDF 版面分析，表格识别↑至89%        │
│ · 实现混合检索（稠密+BM25+ReRanker），MRR@10↑15%  │
│ · 设计多租户知识库隔离架构，支持 100+ 并发          │
│                                                    │
│ MetaGPT — 多Agent协作框架       2026.01 - 2026.03 │
│ · 开发 4 角色数据分析 Agent 团队                   │
│ · 优化 Message Pool，Token 消耗↓35%               │
│ · 实现 MCP 工具注册，支持动态外部 API 接入         │
├────────────────────────────────────────────────────┤
│ ATS关键词: Python · C++ · PyTorch · Transformer ·  │
│ LLM · NLP · 大模型 · 盘古大模型 · 华为云 · Agent · │
│ RAG · 多模态 · RLHF · DPO · LoRA · 推理优化 ·     │
│ KV Cache · Multi-Agent · MCP · Function Calling ·   │
│ LangChain · LangGraph · Tokenizer · Pretrain · SFT │
└────────────────────────────────────────────────────┘
```

> 实际输出为 151KB 的 LaTeX 编译 PDF 文件，包含 5 个精选项目经历，可直接投递。
> ATS 关键词自动注入 25 个与华为 JD 匹配的关键技能词。

### 5. 面试资料包（以下都是真实生成的内容）

**技能树**（required / preferred / basic 三级分类）：

```json
"required": [
  {"skill": "Python",           "category": "工程能力", "importance": "高"},
  {"skill": "C++",              "category": "工程能力", "importance": "高"},
  {"skill": "PyTorch",          "category": "算法工具", "importance": "高"},
  {"skill": "Transformer架构",  "category": "LLM/算法", "importance": "高"},
  {"skill": "LLM/NLP项目经验",  "category": "LLM/算法", "importance": "高"},
  {"skill": "大模型推理优化",    "category": "LLM",      "importance": "中"},
  {"skill": "Agent系统设计",     "category": "Agent",    "importance": "中"}
]
```

**八股文速查手册**（32KB，10个技能点，每个3-5题，标注[必背]/[了解]）：

```markdown
## Python [必背]

- 题目: Python中list和tuple的区别？底层实现有什么不同？
- 核心答案: list是可变对象，使用动态数组，预分配约0~8个元素槽位，
  扩容时创建新数组并复制；tuple是不可变对象，紧凑固定结构，可作为dict的key。
- 追问: GIL对两者性能影响、迭代器vs可迭代对象

## 大模型推理优化 [必背]

- 题目: KV Cache 的原理和作用？
- 核心答案: 缓存已计算的K/V矩阵，推理时只需计算新token的QKV，
  将自回归生成从 O(n²) 降到 O(n)
- 追问: KV Cache 的内存占用？GQA/MQA 如何优化？
```

**4周学习路径**（160小时，每日任务表 + 周检验标准）：

```
第1周: 工程基础夯实 — Python高级/C++/PyTorch（LeetCode Hot 100 每天3题）
第2周: 深度学习理论 — Transformer/注意力机制/损失函数/优化器
第3周: LLM/Agent实战 — Pretrain/SFT/RLHF/DPO/RAG/Agent框架
第4周: 模拟面试 + 查漏补缺 + 系统梳理
```

**模拟面试（15题，字节二面风格，不接受模糊回答）**：

```
第1题: MiniMind全流程训练管线 [困难]

主问题: 你提到从零训练了26M参数的MiniMind，覆盖Tokenizer→Pretrain→SFT→DPO全流程：
  1. 6400词表大小的BPE是如何确定的？为什么选BPE而非WordPiece？
  2. 训练时用了什么优化器、学习率调度策略？
  3. SFT阶段数据格式和loss计算方式与Pretrain有何不同？

追问A: 你在训练中遇到过OOM吗？如果训练1B模型，数据并行和模型并行如何设计？
追问B: DPO效果提升23%是如何计算的？用什么评估指标？如果要进一步提升到30%+？
```

---

## 零基础安装教程（保姆级，跟着做就行）

### 第一步：确认你的电脑环境

打开终端（Mac 按 `Cmd+空格` 输入 "终端"，Windows 用 PowerShell）：

```bash
# 检查 Python 版本（需要 3.11 或更高）
python3 --version

# 如果没有 Python，去这里下载：https://www.python.org/downloads/
# Mac 用户也可以用 Homebrew：brew install python@3.11
```

### 第二步：下载 JobOS

```bash
# 方法一：用 Git（推荐）
git clone https://github.com/bcefghj/JobOS.git
cd JobOS

# 方法二：直接下载
# 打开 https://github.com/bcefghj/JobOS → 点绿色 Code 按钮 → Download ZIP
# 解压后 cd 到文件夹
```

### 第三步：安装依赖

```bash
# 创建虚拟环境（推荐，但不是必须的）
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
# venv\Scripts\activate   # Windows

# 安装所有依赖
pip install -r requirements.txt

# [可选] 安装 Boss直聘真实爬虫
pip install kabi-boss-cli
boss login  # 首次需扫码登录
```

### 第四步：配置 API Key

编辑 `config.yaml`，填入你的 MiniMax API Key：

```yaml
llm:
  provider: minimax
  model: MiniMax-M2.7
  base_url: https://api.minimaxi.com/v1
  api_key: 你的API_KEY  # ← 替换这里
  max_tokens: 4096
  temperature: 0.7
```

> MiniMax API Key 去这里获取：https://platform.minimaxi.com/
> 新用户有免费额度，包月套餐很便宜。

### 第五步：填写你的个人信息

编辑 `data/profile.yaml`，填入你的信息：

```yaml
basics:
  name: "你的名字"        # ← 填上
  email: your@email.com   # ← 填上
  phone: "13800001111"    # ← 填上
  github: https://github.com/你的用户名
  location: 武汉           # ← 你的目标城市
  target_role: AI Agent / 大模型 实习生
  target_type: 暑期实习 / 日常实习

# 教育背景
  education:
    - school: "武汉大学"   # ← 填上你的学校
      degree: "本科"
      major: "计算机科学"
      start_date: "2022.09"
      end_date: "2026.06"
      gpa: "3.5/4.0"

# 技能和项目会由 AI 自动匹配 JD 调整排序，你只需要填写你会的
skills:
  languages:
    - Python
    # ... 添加你会的编程语言
```

### 第六步：安装 LaTeX（用于生成 PDF 简历）

```bash
# Mac
brew install --cask mactex-no-gui
# 或者轻量版：
brew install basictex
sudo tlmgr update --self
sudo tlmgr install ctex xecjk fontspec titlesec enumitem fancyhdr

# Ubuntu/Debian
sudo apt-get install texlive-xetex texlive-lang-chinese

# Windows
# 下载 MiKTeX：https://miktex.org/download
# 安装后它会自动下载需要的包
```

> 如果不装 LaTeX，简历会保存为 .tex 源文件和 JSON 数据，你可以上传到 Overleaf 在线编译。

### 第七步：运行！

```bash
# 方式一：一键跑完整流程（推荐新手用这个）
python pipeline.py --keyword "AI Agent" --location "武汉" --top 3

# 方式二：只爬虫采集岗位（不分析/不生成简历）
python cli.py crawl -k "AI Agent" -l "武汉"

# 方式三：指定平台爬取
python cli.py crawl -k "AI Agent" -l "武汉" -p boss -p nowcoder -p liepin

# 方式四：导出已采集的岗位为 Excel
python cli.py export -f excel

# 方式五：导出为所有格式 (Excel + CSV + JSON)
python cli.py export -f all --all-columns

# 方式六：跑完整管线
python cli.py run -k "AI Agent" -l "武汉" -n 5

# 方式七：夜间批量模式（睡觉前开着，自动跑所有岗位）
python cli.py batch -k "AI Agent" -l "武汉" -n 10 -i 30
```

### 输出文件在哪？

跑完后，所有生成的文件都在 `data/outputs/` 目录下（以下是真实文件列表）：

```
data/outputs/
├── wuhan_ai_jobs.xlsx      (11.8KB) ← Excel（3个Sheet: 职位列表/公司汇总/投递追踪）
├── wuhan_ai_jobs.csv       (4.2KB)  ← CSV
├── wuhan_ai_jobs.json      (15KB)   ← JSON
├── resume_华为_AI工程师实习生（大模型_NLP方向）_20260404.pdf  (151KB) ← 定制简历 PDF
├── resume_华为_AI工程师实习生（大模型_NLP方向）_20260404.tex  (7.7KB) ← LaTeX 源文件
├── interview_华为_..._skill_tree.json   (1.7KB)  ← 技能树（required/preferred/basic）
├── interview_华为_..._study_path.md     (10KB)   ← 4周学习路径（每日任务表）
├── interview_华为_..._eight_part.md     (32KB)   ← 八股文速查手册（10技能点×3-5题）
└── interview_华为_..._mock_interview.md (22KB)   ← 15题模拟面试（字节二面风格）
```

---

## 进阶用法

### 用 MCP Server 接入 AI 编辑器（Cursor / Claude Code）

1. 启动 MCP Server：

```bash
python mcp_server/server.py
```

2. 在 Cursor/Claude Code 的 MCP 配置中添加：

```json
{
  "mcpServers": {
    "jobos": {
      "command": "python",
      "args": ["mcp_server/server.py"],
      "cwd": "/你的JobOS路径"
    }
  }
}
```

3. 然后在 AI 编辑器中直接说："帮我搜索武汉的AI实习" → 自动调用 JobOS。

### 用 OpenClaw Skill

把 `skill/SKILL.md` 放到你的 OpenClaw Skills 目录，然后在小龙虾中说"找工作"即可触发。

### 夜间自动批量模式

适合 MiniMax 包月用户（每周 45000 次调用），晚上 10 点到早上 6 点自动跑：

```bash
# 每 30 分钟跑一次，处理前 10 个高分岗位
python cli.py batch -k "AI Agent" -l "武汉" -n 10 -i 30

# 后台运行（Mac/Linux）
nohup python cli.py batch -k "AI Agent" -l "武汉" -n 10 -i 30 > batch.log 2>&1 &
```

---

## 项目结构

```
JobOS/
├── config.yaml           # 全局配置（API Key、搜索参数、评分权重）
├── pipeline.py           # 核心管线（一键跑完整流程）
├── cli.py                # 命令行工具
├── llm_client.py         # MiniMax M2.7 LLM 客户端
├── db.py                 # SQLite 数据库（岗位存储，扩充字段）
│
├── agents/               # AI Agent 模块
│   ├── analyst.py        # 分析师Agent（JD解析 + 10维评分 + 公司画像）
│   ├── tailor.py         # 裁缝Agent（简历定制 + LaTeX渲染）
│   └── coach.py          # 教练Agent（技能树 + 学习路径 + 八股文 + 模拟面试）
│
├── crawlers/             # 岗位爬虫（真实爬虫 + 策展数据兜底）
│   ├── boss_real.py      # Boss直聘真实爬虫（kabi-boss-cli 逆向API）
│   ├── boss_drission.py  # Boss直聘备用爬虫（DrissionPage 浏览器监听）
│   ├── boss.py           # Boss直聘策展数据（无网络兜底）
│   ├── nowcoder.py       # 牛客网爬虫（requests + HTML解析）
│   ├── liepin.py         # 猎聘爬虫（requests + HTML解析）
│   └── aggregator.py     # 聚合器（多平台去重 + 存DB）
│
├── export/               # 多格式导出
│   ├── excel.py          # Excel 带条件格式（xlsxwriter）
│   ├── csv_export.py     # 标准 CSV
│   └── json_export.py    # 结构化 JSON
│
├── templates/latex/      # LaTeX 简历模板
│   └── resume_template.tex
│
├── data/
│   ├── profile.yaml      # 你的个人信息（填一次，生成N份简历）
│   ├── jobs.db           # 岗位数据库
│   └── outputs/          # 所有生成的文件（PDF/XLSX/MD/JSON）
│
├── mcp_server/           # MCP Server（接入 Cursor/Claude Code）
│   └── server.py
│
├── skill/                # OpenClaw Skill 定义
│   └── SKILL.md
│
├── requirements.txt      # Python 依赖
└── PLAN.md              # 完整调研计划（50+项目分析）
```

---

## 核心特性

| 特性 | 说明 |
|------|------|
| **多平台真实爬虫** | Boss直聘(boss-cli逆向API + DrissionPage备用) + 牛客网(requests) + 猎聘(requests) + 策展数据兜底 |
| **Excel 导出** | 带条件格式的 xlsx（薪资/评分自动变色、冻结表头、自动筛选、3个Sheet、投递追踪下拉选择） |
| **多格式导出** | Excel / CSV / JSON 一键导出 |
| **10维评分** | 角色匹配+技能对齐（门槛）+ 薪资/地点/公司/技术栈/成长/面试难度/时间/WLB |
| **定制简历** | YAML个人数据 + AI按JD关键词定制 + STAR法则润色 + ATS优化 + LaTeX PDF |
| **面试资料** | 技能树 + N周学习路径 + 八股文速查 + 15题模拟面试（不接受模糊回答风格） |
| **公司画像** | 行业/规模/评分/优缺点/薪资/加班情况 |
| **打招呼语** | 自动生成 Boss直聘 80字打招呼语 |
| **批量模式** | 夜间自动跑，利用 MiniMax 低峰 100TPS |
| **MCP Server** | 接入 Cursor/Claude Code，用自然语言调用 |
| **OpenClaw Skill** | 养在小龙虾里，持续更新 |

---

## 爬虫技术方案

| 平台 | 方案 | 原理 | 特点 |
|------|------|------|------|
| **Boss直聘**（主力） | kabi-boss-cli | 逆向 Boss API，纯 HTTP，不开浏览器 | 轻量快速，高斯随机延迟+指数退避反检测 |
| **Boss直聘**（备用） | DrissionPage | 真实浏览器监听 API JSON 响应 | 更稳定抗检测，需要 Chrome |
| **Boss直聘**（兜底） | 策展数据 | 手工整理的 18 个武汉AI岗位 | 无网络/爬虫失败时的保底方案 |
| **牛客网** | requests + BeautifulSoup | 直接请求搜索页解析 HTML | 反爬弱，速度快 |
| **猎聘** | requests + BeautifulSoup | 请求搜索页解析 HTML | 中等反爬，带随机延迟 |

> Boss直聘首次使用需要 `boss login` 扫码登录获取 Cookie，之后自动复用。

---

## 技术栈

- **LLM**: MiniMax M2.7（OpenAI SDK 兼容，包月便宜）
- **简历渲染**: YAML → Jinja2 → XeLaTeX → PDF
- **数据存储**: SQLite（本地，扩充字段支持完整JD/HR信息/技能标签）
- **爬虫**: kabi-boss-cli + DrissionPage + requests + BeautifulSoup
- **导出**: xlsxwriter（条件格式）+ pandas + csv + json
- **CLI框架**: Click + Rich（漂亮的终端输出）
- **MCP**: Python MCP SDK

---

## 常见问题 FAQ

**Q: Boss直聘爬虫怎么登录？**

A: 首次运行 `boss login`，用手机 Boss直聘 App 扫码登录。Cookie 会自动保存，后续无需重复登录。如果 boss-cli 不可用，会自动 fallback 到策展数据。

**Q: LaTeX 安装失败/编译报错怎么办？**

A: 不装 LaTeX 也能用！简历会保存为 `.tex` 源文件，你可以：
1. 上传到 [Overleaf](https://www.overleaf.com/) 在线编译
2. 或者用生成的 JSON 数据自己排版

**Q: MiniMax API Key 怎么获取？**

A: 去 https://platform.minimaxi.com/ 注册，新用户有免费额度。月度套餐约 30-50 元/月，性价比极高。

**Q: 可以换其他 LLM 吗？（GPT-4 / Claude / 通义千问）**

A: 可以！修改 `config.yaml` 的 `base_url` 和 `api_key`，任何兼容 OpenAI SDK 的 LLM 都能用。

**Q: 岗位数据多久更新一次？**

A: 使用 `python cli.py crawl` 命令实时从 Boss直聘/牛客网/猎聘 爬取最新岗位。批量模式下可设定定时间隔自动更新。当前仓库内附带 24 个预采集岗位作为示例。

**Q: 我不在武汉，能用吗？**

A: 能！修改 `config.yaml` 的 `default_location` 和运行命令的 `--location` 参数即可。

**Q: 简历上的项目是假的怎么办？面试被问到怎么说？**

A: 生成的项目经历是基于真实的知名开源项目（MiniMind/RAGFlow/MetaGPT），你需要：
1. 真正去读这些项目的代码（简历只是起点，不是终点）
2. 跑通项目的核心功能
3. 面试时能讲清楚技术细节（学习路径会帮你准备）

**Q: 怎么导出 Excel？**

A: `python cli.py export -f excel` 即可。支持 `--all-columns` 导出全部字段。Excel 文件包含条件格式（薪资/评分自动变色）、冻结表头、自动筛选、投递追踪等功能。

---

## 致谢

JobOS 的设计参考了 50+ 优秀开源项目（详见 `PLAN.md`），特别感谢：

- [MiniMind](https://github.com/jingyaogong/minimind) — 从零训练大语言模型
- [RAGFlow](https://github.com/infiniflow/ragflow) — 企业级 RAG 引擎
- [MetaGPT](https://github.com/geekan/MetaGPT) — 多 Agent 协作框架
- [kabi-boss-cli](https://github.com/kabi404/boss-cli) — Boss直聘逆向 API 工具
- [DrissionPage](https://github.com/g1879/DrissionPage) — 浏览器自动化框架
- [Career-Ops](https://dev.to/santifer/) — 10维评分系统设计灵感
- [cv-pipeline](https://github.com/jsoyer/cv-pipeline) — YAML→LaTeX 管线设计
- [AgentGuide](https://github.com/adongwanai/AgentGuide) — 求职方法论

---

## License

MIT
