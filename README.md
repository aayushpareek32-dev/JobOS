# JobOS — AI 求职操作系统

> **一句话介绍**：输入「城市 + 方向」，自动爬取 Boss直聘 + 牛客网 + 猎聘 真实岗位 → 10维评分 → 导出 Excel → 生成定制简历(LaTeX PDF) → 生成从零到面试的全套资料，一条龙服务。

```
"我想找合肥的 AI 暑期实习"
    ↓ JobOS 自动运行
    ↓ Boss直聘真实浏览器爬取（自动弹出浏览器，首次扫码，之后免登录）
    ↓ + 牛客网 + 猎聘 多平台采集
    ↓ 去重 → 存入 SQLite 数据库
    ↓ 10维评分排序（门槛过滤 + 加权排名）
    ↓ 导出带条件格式的 Excel（薪资/评分自动变色）
    ↓ 生成定制 LaTeX PDF 简历（针对具体岗位要求）
    ↓ 生成 4 周学习路径 + 八股文 + 15 题模拟面试
    ↓ 生成 Boss直聘打招呼语
    ✅ 完成！所有文件在 data/outputs/ 下
```

---

## 实际案例展示（真实运行结果）

### 案例一：合肥 AI 岗位实时爬取（Boss直聘真实数据）

> 实际运行 `python run_hefei_live.py`，DrissionPage 真实浏览器爬取 Boss直聘 API，15 个合肥 AI 岗位。

| # | 公司 | 岗位 | 薪资 | 地点 | HR |
|---|------|------|------|------|-----|
| 1 | 逐鹿未来 | AI智能导学师 | 50-55元/时 | 合肥 蜀山区 高新区 | 章先生 HR |
| 2 | 焱创云志科技 | 人工智能AI工程师 | **16-30K** | 合肥 蜀山区 科技园 | 李玉艳 招聘经理 |
| 3 | 家园卫士 | AI产品实习生 | 150-250元/天 | 合肥 蜀山区 中科大 | 黄先生 高级技术顾问 |
| 4 | 探迹 | 人工智能NLP | **14-28K** | 合肥 包河区 屯溪路 | 张先生 高级招聘专员 |
| 5 | 疯马视觉 | AI短剧生成 | 10-15K | 合肥 瑶海区 明光路 | 张媛 招聘者 |
| ... | 还有10个岗位 | ... | ... | ... | ... |

### 案例二：华为武汉AI实习全流程 Demo

> 以下所有内容都是 JobOS 以「华为武汉AI实习」为目标，**实际运行**生成的真实结果。

#### 多平台岗位采集（24 个岗位，3 个平台）

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
| 9 | 牛客网 | **淘天集团** | AI Agent应用开发工程师-2026暑期实习 | 杭州 | 300-600元/天 | 暑期实习 |
| 10 | 牛客网 | **阿里云** | AI Agent 开发工程师 | 杭州 | 500-510元/天 | 暑期实习 |
| ... | ... | 还有 14 个岗位 | ... | ... | ... | ... |

#### 10维评分系统（华为岗位：0.82 分 ✅ 强推）

```
华为 AI工程师实习生（大模型/NLP方向）  综合评分: 0.82 ✅ 强推

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
└──────────────────────────────────────────────────┘
```

#### 定制简历（LaTeX PDF，151KB）

```
┌────────────────────────────────────────────────────┐
│                     你的名字                        │
│   email@163.com | 13800001111 | GitHub | 武汉      │
├────────────────────────────────────────────────────┤
│ MiniMind — 从零训练大语言模型    2025.09 - 2026.03 │
│ · 独立完成 Pretrain 数据管线，训练 6400 词表的      │
│   中文 Tokenizer                                   │
│ · 实现 SFT+DPO+RLHF 三阶段对齐，DPO 效果↑23%     │
│                                                    │
│ RAGFlow — 企业级 RAG 引擎       2025.11 - 2026.03 │
│ · 实现混合检索（稠密+BM25+ReRanker），MRR@10↑15%  │
│                                                    │
│ MetaGPT — 多Agent协作框架       2026.01 - 2026.03 │
│ · 优化 Message Pool，Token 消耗↓35%               │
├────────────────────────────────────────────────────┤
│ ATS关键词: Python · PyTorch · Transformer · LLM ·  │
│ Agent · RAG · RLHF · DPO · LoRA · 盘古大模型 ...  │
└────────────────────────────────────────────────────┘
```

#### 面试资料包

- **技能树**：required / preferred / basic 三级分类
- **八股文速查手册**：32KB，10个技能点×3-5题，标注[必背]/[了解]
- **4周学习路径**：160小时，每日任务表
- **15题模拟面试**：字节二面风格，不接受模糊回答

---

## 零基础安装教程（保姆级）

### 第一步：确认环境

```bash
# 检查 Python 版本（需要 3.10 或更高）
python3 --version

# Mac 用 Homebrew 安装：brew install python@3.11
# Windows：https://www.python.org/downloads/
```

### 第二步：下载 JobOS

```bash
git clone https://github.com/bcefghj/JobOS.git
cd JobOS
```

### 第三步：安装依赖

```bash
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
# venv\Scripts\activate   # Windows

pip install -r requirements.txt
```

### 第四步：配置 API Key

```bash
cp config.yaml config.local.yaml
# 编辑 config.local.yaml，填入你的 MiniMax API Key
```

```yaml
llm:
  provider: minimax
  model: MiniMax-M2.7
  base_url: https://api.minimaxi.com/v1
  api_key: 你的API_KEY  # ← 替换这里
```

> MiniMax API Key：https://platform.minimaxi.com/ 新用户有免费额度。

### 第五步：运行！

```bash
# 方式一：一键实时爬取（推荐，自动弹出浏览器）
python run_hefei_live.py

# 方式二：完整管线（采集+评分+简历+面试资料）
python pipeline.py --keyword "AI Agent" --location "武汉" --top 3

# 方式三：CLI 工具
python cli.py crawl -k "AI" -l "合肥"
python cli.py export -f excel
```

---

## Boss直聘爬虫详细指南（4种方法，总有一个适合你）

> Boss直聘是国内最大的招聘平台，也是反爬最严格的。JobOS 提供了 **4 种方法**，按推荐顺序排列。失败时自动按顺序 fallback。

### 方法一：DrissionPage 浏览器爬取（推荐，最稳定）

**原理**：打开真实 Chrome 浏览器，监听 Boss直聘 API 返回的 JSON 数据。因为是真实浏览器，反爬检测几乎无效。

**首次使用**：
```bash
python run_hefei_live.py
# 或
python cli.py crawl -k "AI" -l "合肥" -p boss_drission
```

1. 程序会自动打开 Chrome 浏览器
2. 如果未登录，会跳转到 Boss直聘 登录页
3. **用 Boss直聘 App 扫码**（不是微信！不是QQ！）
4. 手机上确认授权
5. 程序自动检测登录成功，开始爬取
6. **Cookie 自动保存在 `data/.boss_browser_profile/`，下次无需重新登录**

**优点**：
- 最稳定，反爬检测几乎无效
- 首次扫码后自动保存登录状态
- 支持所有城市和关键词

**缺点**：
- 需要安装 Chrome 浏览器
- 爬取速度比纯 API 慢一些（因为要打开浏览器）

### 方法二：boss-cli 命令行工具（最快，但需要额外安装）

**原理**：`kabi-boss-cli` 是第三方逆向 Boss直聘 API 的命令行工具，纯 HTTP 请求，不需要浏览器。

**安装**：
```bash
pip install kabi-boss-cli
```

**首次登录**：
```bash
boss login
```

⚠️ **扫码注意事项（很多人踩坑）**：

| 扫码方式 | 能不能用 | 说明 |
|---------|---------|------|
| **Boss直聘 App 扫码** | ✅ 可以 | 唯一正确方式！打开 App → 右上角扫一扫 |
| 微信扫码 | ❌ 不行 | 微信会识别二维码但跳转失败 |
| QQ 扫码 | ❌ 不行 | 同上 |
| 支付宝扫码 | ❌ 不行 | 同上 |
| 手机自带相机扫码 | ❌ 不行 | 会打开网页但不能完成授权 |

**如果扫码成功但提示 `缺少关键 Cookie: __zp_stoken__`**：

这说明 boss-cli 的二维码登录没有拿到完整的登录态。解决方法：

```bash
# 方法 A：先在浏览器登录，再让 boss-cli 读取浏览器 Cookie
# 1. 用 Chrome 打开 https://www.zhipin.com 并登录
# 2. 在 Boss直聘 网站上随便搜一个岗位（触发完整 Cookie 生成）
# 3. 然后运行：
boss login --cookie-source chrome

# 如果你用的是 Edge 浏览器：
boss login --cookie-source edge
```

```bash
# 方法 B：放弃 boss-cli，改用 DrissionPage（方法一）
python cli.py crawl -k "AI" -l "合肥" -p boss_drission
```

**使用**：
```bash
# boss-cli 登录成功后，直接跑 pipeline
python pipeline.py --keyword "AI" --location "合肥" --top 5

# 或用 CLI
python cli.py crawl -k "AI" -l "合肥"
```

**优点**：
- 速度最快（纯 HTTP，不开浏览器）
- 轻量，适合服务器部署

**缺点**：
- 登录过程容易踩坑（见上面的注意事项）
- `__zp_stoken__` Cookie 容易缺失
- 依赖第三方库维护

### 方法三：Cookie 手动导入（boss-cli 和 DrissionPage 都不行时）

**原理**：从浏览器 DevTools 手动复制 Cookie，直接调用 Boss直聘 API。

**步骤**：

1. **Chrome 打开** https://www.zhipin.com 并登录
2. **搜索一个岗位**（比如搜 "AI 合肥"）
3. 按 **F12** 打开开发者工具
4. 点 **Network（网络）** 标签
5. 在 Network 列表里找到包含 `zpgeek` 的请求
6. **右键该请求** → **Copy（复制）** → **Copy as cURL**
7. 粘贴到文本编辑器，找到 `cookie: ` 后面的那一大串内容
8. 把 Cookie 字符串保存到 `data/.boss_cookies.txt`：

```bash
# 直接写入文件
echo '你复制的cookie字符串' > data/.boss_cookies.txt
```

9. 然后运行：

```bash
python cli.py crawl -k "AI" -l "合肥" -p boss_cookie
```

**优点**：
- 不需要安装额外工具
- 任何平台都能用

**缺点**：
- Cookie 有效期约 2-7 天，过期需要重新复制
- 操作步骤较多

### 方法四：策展数据（离线兜底，永远能用）

**原理**：内置了 18 个手工整理的武汉 AI 岗位数据，不需要网络。

**使用**：
```bash
python cli.py crawl -k "AI" -l "武汉" -p curated
```

**优点**：
- 永远能用，不需要网络、不需要登录
- 适合快速体验 JobOS 的评分/简历/面试资料功能

**缺点**：
- 数据不是实时的（手工维护）
- 只有武汉 AI 方向的岗位

### Fallback 机制

当你使用默认配置（`python pipeline.py`）时，Boss直聘会自动按以下顺序尝试：

```
boss-cli → DrissionPage(自动登录) → Cookie API → 策展数据
   ↓失败        ↓失败                   ↓失败         ↓保底
  跳过         弹出浏览器扫码           读取cookie文件   返回内置数据
```

**你不需要手动选择方法**，系统会自动 fallback。如果你想强制使用某种方法：

```bash
# 强制用 DrissionPage
python cli.py crawl -k "AI" -l "合肥" -p boss_drission

# 强制用 boss-cli
python cli.py crawl -k "AI" -l "合肥" -p boss

# 强制用 cookie
python cli.py crawl -k "AI" -l "合肥" -p boss_cookie

# 强制用策展数据
python cli.py crawl -k "AI" -l "武汉" -p curated
```

---

## Boss直聘常见问题排查

### Q: 扫码扫不上？

| 症状 | 原因 | 解决方法 |
|------|------|---------|
| 微信/QQ 扫码后显示"无法识别" | 用错了 App | 必须用 **Boss直聘 App** 扫，不是微信/QQ |
| 手机相机扫码后跳转到网页 | 不支持 | 必须用 Boss直聘 App 内的扫一扫功能 |
| Boss App 扫码后没反应 | 网络问题 | 检查手机和电脑在同一网络下，重试 |
| 扫码成功但终端提示 `__zp_stoken__` 缺失 | 二维码登录不完整 | 改用 `boss login --cookie-source chrome`（先在浏览器登录） |
| `boss` 命令找不到 | 没安装 | `pip install kabi-boss-cli` |

### Q: 改了城市和关键词还是搜到武汉 AI 的岗位？

**已修复！** 之前策展数据（curated data）没有正确过滤城市和关键词。现在 `search_boss_jobs(keyword, city)` 会**同时按关键词和城市**双重过滤。

- 搜「合肥 + AI」→ 只返回合肥相关的 AI 岗位
- 搜「北京 + Java」→ 策展数据里没有匹配项，返回空（这是正确行为）
- 真实爬虫（DrissionPage/boss-cli）不受此影响，始终按你的参数搜索

### Q: DrissionPage 打不开浏览器？

```bash
# 确保安装了 Chrome 浏览器
# Mac:
brew install --cask google-chrome

# 或者确认 Chrome 在默认位置
ls /Applications/Google\ Chrome.app

# 如果用的是 Chromium 或其他基于 Chromium 的浏览器，DrissionPage 也支持
```

### Q: 爬取速度慢 / 被限流？

Boss直聘有反爬机制，建议：
- 每页之间间隔 3-5 秒（默认已配置）
- 不要连续爬取超过 5 页
- 如果被封，等 10 分钟后重试
- 使用 DrissionPage 方案（真实浏览器，不易被检测）

### Q: Cookie 多久过期？

- **DrissionPage**：Cookie 保存在 `data/.boss_browser_profile/`，有效期较长（通常 1-2 周），和正常使用浏览器一样
- **boss-cli**：Cookie 由 boss-cli 自动管理，有效期取决于 Boss直聘服务端
- **手动 Cookie**：有效期约 2-7 天，过期后需要重新从 DevTools 复制

---

## Excel 导出效果

导出的 Excel 包含 **3 个 Sheet**：

- **职位列表**：蓝色表头、冻结首行、自动筛选、薪资/评分条件变色（高薪绿色、中等黄色、低薪红色）
- **公司汇总**：按岗位数排序，包含行业/规模/融资等信息
- **投递追踪**：带下拉选择的投递状态追踪表（未投递/已投递/笔试/一面/二面/HR面/Offer/拒绝）

```bash
# 导出 Excel
python cli.py export -f excel

# 导出所有格式
python cli.py export -f all --all-columns
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
├── crawlers/             # 岗位爬虫（4级 fallback 体系）
│   ├── boss_real.py      # Boss直聘 方法二：kabi-boss-cli 逆向API
│   ├── boss_drission.py  # Boss直聘 方法一：DrissionPage 浏览器监听（推荐）
│   ├── boss_cookie.py    # Boss直聘 方法三：手动 Cookie 导入
│   ├── boss.py           # Boss直聘 方法四：策展数据（离线兜底）
│   ├── nowcoder.py       # 牛客网爬虫（requests + HTML解析）
│   ├── liepin.py         # 猎聘爬虫（requests + HTML解析）
│   └── aggregator.py     # 聚合器（多平台去重 + 4级fallback + 存DB）
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
├── run_hefei_live.py     # 一键实时爬取示例（合肥AI）
├── run_huawei_demo.py    # 华为武汉AI实习全流程 Demo
├── run_crawl_and_export.py # 多平台爬取 + Excel导出
├── requirements.txt      # Python 依赖
└── PLAN.md              # 完整调研计划（50+项目分析）
```

---

## 核心特性

| 特性 | 说明 |
|------|------|
| **多平台真实爬虫** | Boss直聘(4级fallback: boss-cli → DrissionPage → Cookie → 策展数据) + 牛客网 + 猎聘 |
| **Boss直聘自动登录** | DrissionPage 自动弹出浏览器，检测登录状态，未登录则等待扫码，Cookie 自动保存 |
| **Excel 导出** | 带条件格式的 xlsx（薪资/评分自动变色、冻结表头、自动筛选、3个Sheet、投递追踪） |
| **多格式导出** | Excel / CSV / JSON 一键导出 |
| **10维评分** | 角色匹配+技能对齐（门槛）+ 薪资/地点/公司/技术栈/成长/面试难度/时间/WLB |
| **定制简历** | YAML个人数据 + AI按JD关键词定制 + STAR法则润色 + ATS优化 + LaTeX PDF |
| **面试资料** | 技能树 + N周学习路径 + 八股文速查 + 15题模拟面试 |
| **公司画像** | 行业/规模/评分/优缺点/薪资/加班情况 |
| **打招呼语** | 自动生成 Boss直聘 80字打招呼语 |
| **批量模式** | 夜间自动跑，利用 MiniMax 低峰 100TPS |
| **MCP Server** | 接入 Cursor/Claude Code，用自然语言调用 |

---

## 爬虫技术方案

| 平台 | 方案 | 原理 | 状态 |
|------|------|------|------|
| **Boss直聘**（推荐） | DrissionPage | 真实浏览器监听 API JSON，自动登录 | ✅ 已验证 |
| **Boss直聘**（备选） | kabi-boss-cli | 逆向 Boss API，纯 HTTP | ✅ 需扫码 |
| **Boss直聘**（手动） | Cookie 导入 | 从 DevTools 复制 Cookie 调 API | ✅ 通用 |
| **Boss直聘**（兜底） | 策展数据 | 内置 18 个武汉AI岗位 | ✅ 离线可用 |
| **牛客网** | requests | 请求搜索页解析 HTML | ✅ |
| **猎聘** | requests | 请求搜索页解析 HTML | ✅ |

---

## 技术栈

- **LLM**: MiniMax M2.7（OpenAI SDK 兼容，包月便宜）
- **简历渲染**: YAML → Jinja2 → XeLaTeX → PDF
- **数据存储**: SQLite（本地，扩充字段支持完整JD/HR信息/技能标签）
- **Boss直聘爬虫**: DrissionPage(推荐) + kabi-boss-cli + requests(cookie)
- **其他爬虫**: requests + BeautifulSoup
- **导出**: xlsxwriter（条件格式）+ csv + json
- **CLI框架**: Click + Rich（漂亮的终端输出）
- **MCP**: Python MCP SDK

---

## 更多 FAQ

**Q: 可以换其他 LLM 吗？（GPT-4 / Claude / 通义千问）**

A: 可以！修改 `config.yaml` 的 `base_url` 和 `api_key`，任何兼容 OpenAI SDK 的 LLM 都能用。

**Q: LaTeX 安装失败/编译报错怎么办？**

A: 不装 LaTeX 也能用！简历会保存为 `.tex` 源文件，上传到 [Overleaf](https://www.overleaf.com/) 在线编译即可。

**Q: 我不在武汉/合肥，能用吗？**

A: 能！修改命令的 `--location` 参数即可。支持 25+ 个城市（北上广深杭成都南京西安重庆天津苏州厦门长沙青岛郑州大连宁波福州昆明哈尔滨济南沈阳珠海佛山东莞等）。

**Q: 岗位数据多久更新一次？**

A: 使用爬虫命令实时采集。批量模式下可设定定时间隔自动更新。

**Q: 简历上的项目是假的怎么办？**

A: 生成的项目经历基于真实的知名开源项目（MiniMind/RAGFlow/MetaGPT），你需要真正去读这些项目的代码，面试时能讲清楚技术细节。学习路径和八股文会帮你准备。

---

## 致谢

JobOS 的设计参考了 50+ 优秀开源项目（详见 `PLAN.md`），特别感谢：

- [MiniMind](https://github.com/jingyaogong/minimind) — 从零训练大语言模型
- [RAGFlow](https://github.com/infiniflow/ragflow) — 企业级 RAG 引擎
- [MetaGPT](https://github.com/geekan/MetaGPT) — 多 Agent 协作框架
- [kabi-boss-cli](https://github.com/kabi404/boss-cli) — Boss直聘逆向 API 工具
- [DrissionPage](https://github.com/g1879/DrissionPage) — 浏览器自动化框架

---

## License

MIT
