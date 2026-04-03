# Boss直聘爬虫方案技术调研报告

> 调研时间：2026年4月4日 | 覆盖12个搜索维度

---

## 一、项目总览（按Stars排序）

| # | 项目名 | Stars | 技术栈 | 类型 | 活跃度 |
|---|--------|-------|--------|------|--------|
| 1 | [get_jobs](https://github.com/loks666/get_jobs) | ⭐ 6145 | Java + Selenium/Playwright | 全平台自动投递 | 活跃 |
| 2 | [boss_batch_push](https://github.com/yangfeng20/boss_batch_push) | ⭐ 790 | JavaScript 油猴脚本 | 批量投递 | 作者已推荐迁移 |
| 3 | [boss-cli](https://github.com/jackwener/boss-cli) | ⭐ 550 | Python + 逆向API | CLI工具 | 2026.03活跃 |
| 4 | [mcp-bosszp](https://github.com/mucsbr/mcp-bosszp) | ⭐ 228 | Python + Playwright + MCP | AI Agent集成 | 活跃 |
| 5 | [Jobs_helper (BOSS海投助手)](https://github.com/YangShengzhou03/Jobs_helper) | ⭐ 220 | JavaScript 油猴脚本 | 批量投递+AI回复 | 活跃 |
| 6 | [geekgeekrun (牛人快跑)](https://github.com/geekgeekrun/geekgeekrun) | ⭐ ~100+ | Puppeteer + Electron | 桌面应用 | 活跃 |
| 7 | [BOSScript](https://github.com/Sunny-117/BOSScript) | ⭐ 84 | JavaScript 油猴脚本 | 极速批量投递 | 一般 |
| 8 | [auto_get_jobs](https://github.com/SanThousand/auto_get_jobs) | ⭐ 75 | Python + Selenium | AI匹配+自动投递 | 2025活跃 |
| 9 | [get-jobs-boss](https://github.com/uniStark/get-jobs-boss) | ⭐ 55 | Java + Selenium | 自动投递 | 一般 |
| 10 | [boss-zhipin-automation](https://github.com/wensia/boss-zhipin-automation) | ⭐ 28 | Python + Playwright + FastAPI | 全栈自动化 | 一般 |
| 11 | [BossZP-Spider](https://github.com/SolidifyTime/BossZP-Spider) | ⭐ ~10 | Python + Selenium | 数据爬取 | 2025 |
| 12 | [boss-crawl-analyzer](https://github.com/yj-liuzepeng/boss-crawl-analyzer) | ⭐ 6 | Python + FastAPI + Vue3 | 全栈爬虫+AI分析 | 2025 |
| 13 | [JobClaw](https://github.com/slothsheepking/jobclaw) | ⭐ ~5 | Python + Playwright | AI求职Agent | 新项目 |
| 14 | [百分投简历 (100Resume)](https://100resume.aitoolhub.top/) | - | Chrome扩展 | 爬取+AI匹配 | 活跃 |

---

## 二、各项目详细分析

### 1. get_jobs（⭐6145 — 最高星项目）

**GitHub**: https://github.com/loks666/get_jobs

**技术架构**:
- **语言**: Java (64%) + TypeScript (33.5%) + JavaScript (1.9%)
- **构建**: Gradle + JDK 21
- **浏览器自动化**: Selenium/Playwright 驱动 Chrome
- **前端**: Web图形化管理界面
- **AI集成**: OpenAI API 智能匹配+个性化打招呼语

**可爬字段**:
- ✅ 岗位名称、公司名称、薪资范围
- ✅ JD全文（通过详情页）
- ✅ HR信息（过滤不活跃/猎头）
- ✅ 自动投递+自定义招呼语
- ✅ 学历要求、经验要求

**防封策略**:
- Cookie持久登录（超长有效期）
- 智能过滤不活跃HR，减少无效请求
- 黑名单企业过滤
- 企业微信推送通知投递情况

**导出**: 投递日志保存在 `target/logs/`

**核心问题**: Boss直聘新增反检测机制，投递过程中页面频繁刷新。社区正在讨论 console函数劫持、DevTools检测规避等方案。

**关键代码思路**:
```
1. 自动检测系统环境 → 下载对应ChromeDriver
2. Cookie登录（部分平台每周仅需扫码一次）
3. 按配置关键词搜索岗位列表
4. AI分析JD匹配度 → 生成个性化招呼语
5. 自动点击"立即沟通" → 发送招呼语
6. 企业微信Webhook推送结果
```

---

### 2. boss_batch_push（⭐790 — 油猴方案经典）

**GitHub**: https://github.com/yangfeng20/boss_batch_push
**Greasy Fork**: https://greasyfork.org/zh-CN/scripts/468125

**技术架构**:
- **纯JavaScript** 油猴(Tampermonkey)脚本
- 前端交互层: `DOMApi` 类封装DOM操作
- 数据通信层: `TampermonkeyApi` 类封装 `GM_setValue/GM_getValue`
- UI层: `OperationPanel` 类负责控制面板

**核心功能**:
- 批量投递简历
- 多维度筛选：公司名包含/排除、岗位名包含/排除、薪资范围、公司规模
- HR活跃度过滤
- 自定义招呼语（Boss不支持默认招呼语）
- 词云图分析（分词权重+可视化）

**可爬字段**:
- ✅ 岗位名称、公司名称、薪资范围
- ✅ 公司规模、工作内容关键词
- ❌ 不直接爬取完整JD
- ✅ HR活跃状态

**防封策略**:
- 利用Tampermonkey在真实浏览器环境运行，不易被检测
- 随机延迟投递间隔

**导出**: 无直接导出功能

**当前状态**: ⚠️ 作者声明Boss直聘推出新职位页面后未适配，推荐迁移至"AI工作猎手"新项目。

---

### 3. boss-cli（⭐550 — 逆向API方案）

**GitHub**: https://github.com/jackwener/boss-cli

**技术架构**:
- **Python** 实现
- **核心方法**: 逆向工程Boss直聘API（非浏览器自动化）
- 安装: `uv tool install kabi-boss-cli`

**核心功能**:
- 自动提取浏览器Cookie（支持10+浏览器）
- 二维码登录
- 40+城市搜索
- 多维度筛选（薪资/经验/学历/行业/公司规模/融资阶段）
- 与招聘方聊天（1.5秒速率限制）
- 应聘管理、面试邀请查看

**可爬字段**:
- ✅ 岗位名称、公司名称、薪资范围
- ✅ 完整职位详情
- ✅ 推荐职位、浏览历史
- ✅ 个人资料/简历状态
- ✅ 已申请列表

**防封策略**:
- 使用真实浏览器Cookie（不模拟浏览器）
- 1.5秒速率限制
- 不生成额外流量（直接调API）

**导出**: ✅ CSV / JSON 格式

**评价**: 这是最轻量级的方案，直接调用API比浏览器自动化更高效，但依赖Cookie有效期和API稳定性。已知问题包括Token过期和Windows环境Cookie提取困难。

---

### 4. mcp-bosszp（⭐228 — MCP协议AI集成）

**GitHub**: https://github.com/mucsbr/mcp-bosszp

**技术架构**:
- **Python 3.12+**
- FastMCP框架
- Playwright（无头浏览器）
- PyCryptodome（加密）
- 支持Docker部署

**核心功能**:
- 为LLM提供Boss直聘交互能力（MCP协议）
- 自动二维码登录+安全验证
- 搜索职位、发送问候
- 简历解析（PDF/DOCX）
- 智能职位推荐

**架构缺陷**（来自Agent-Reach Issue#56的分析）:
- 登录用Playwright，但后续API用`requests`——两个会话不一致
- `__zp_stoken__`被硬编码
- User-Agent过时（Chrome 120）
- 被风控拦截后账号直接禁用

---

### 5. BOSS海投助手 / Jobs_helper（⭐220）

**GitHub**: https://github.com/YangShengzhou03/Jobs_helper
**Greasy Fork**: https://greasyfork.org/zh-CN/scripts/569600

**技术架构**:
- JavaScript ES6+ 油猴脚本
- 单文件模块化设计，无需构建工具
- AI集成：讯飞星火API + OpenAI API

**核心功能**:
- 自动批量投递
- 精准岗位筛选（关键词/地点/薪资）
- **AI智能回复HR**（根据HR问题+用户简历生成回复）
- 可视化控制面板
- 防重复投递机制

**可爬字段**:
- ✅ 岗位基本信息
- ✅ HR消息内容
- ✅ 投递状态

**防封策略**:
- 真实浏览器环境运行
- 防重复投递机制避免浪费配额

**导出**: 无直接导出

---

### 6. geekgeekrun / 牛人快跑（~100+ Stars）

**GitHub**: https://github.com/geekgeekrun/geekgeekrun

**技术架构**:
- **Puppeteer + Electron** 桌面应用
- 支持 Windows / macOS / Linux
- 集成大语言模型

**核心模块**:

**(1) Boss炸弹**:
- 按求职偏好自动筛选+与Boss开聊
- 检查Boss活跃度，过滤长期未活跃
- 职位名称/类型/描述匹配
- 每日开聊次数用完自动暂停60分钟

**(2) 已读不回提醒器**:
- 自动发送提醒消息给已读未回的Boss
- 支持自定义内容或LLM生成个性化消息
- 可设"跟进时限"和"跟进间隔"

**防封策略**:
- 达到每日上限后自动暂停60分钟
- 不合适职位自动标记跳过

---

### 7. JobClaw（AI求职Agent）

**GitHub**: https://github.com/slothsheepking/jobclaw

**技术架构**:
- **Python + Playwright** 模拟真人浏览器操作

**防封策略**（最详细的防封文档）:
- 🕐 **随机延迟**: 每次投递间隔3-8秒（可配置）
- 📊 **每日上限**: 默认100次/天
- 👻 **僵尸岗过滤**: 跳过HR超7天未活跃的岗位
- 🔄 **防重复投递**: JSON历史记录自动跳过已沟通岗位
- 🔐 **验证码检测**: 遇验证码自动暂停+Telegram通知

---

### 8. auto_get_jobs（⭐75 — Python AI方案）

**GitHub**: https://github.com/SanThousand/auto_get_jobs

**技术架构**:
- Python 3.10 + Selenium + BeautifulSoup
- AI: 硅基流动平台 Qwen2.5-72B-Instruct（¥1/M tokens）

**核心功能**:
- AI岗位匹配度分析
- 自动过滤不活跃HR
- 学历/城市/薪资/岗位筛选
- 自动打招呼

**使用流程**:
```
1. 配置.env（API Key）和 user_requirements（简历信息）
2. python main.py → 浏览器自动打开Boss直聘
3. 60秒内完成扫码登录
4. 自动运行：搜索→过滤→AI匹配→投递
```

---

### 9. boss-zhipin-automation（⭐28 — 全栈方案）

**GitHub**: https://github.com/wensia/boss-zhipin-automation

**技术架构**:
- **后端**: Python + FastAPI
- **前端**: React
- **浏览器**: Playwright
- 支持macOS和Windows安装脚本

**核心功能**:
- 二维码登录+多账号管理
- 职位筛选+自动打招呼
- 消息模板管理
- 任务管理和运行日志

---

### 10. 百分投简历 / 100Resume（Chrome扩展）

**官网**: https://100resume.aitoolhub.top/

**技术架构**:
- Chrome浏览器扩展
- 使用GPT技术进行AI匹配

**核心功能**:
- 一键爬取Boss直聘岗位信息
- AI匹配度打分+排序
- 批量自定义招呼语
- 隐藏不合适岗位
- **导出Excel** ✅

**字段**: 职位名称、地址、公司信息、薪资、JD全文

---

## 三、技术方案对比

### 3.1 按技术路线分类

| 技术路线 | 代表项目 | 优点 | 缺点 |
|----------|----------|------|------|
| **逆向API** | boss-cli | 速度快、资源占用低、稳定 | 需逆向__zp_stoken__，API变更风险高 |
| **Playwright** | boss-zhipin-automation, JobClaw, mcp-bosszp | 最接近真人操作，支持复杂交互 | 资源占用大，需处理无头检测 |
| **Selenium** | get_jobs, auto_get_jobs, BossZP-Spider | 生态成熟，教程多 | 性能差于Playwright，易被检测 |
| **Puppeteer** | geekgeekrun | Node生态好，Electron桌面化 | 仅限JS/TS |
| **油猴脚本** | boss_batch_push, Jobs_helper, BOSScript | 最安全(真实浏览器环境)，门槛低 | 功能受限于页面DOM |
| **DrissionPage** | 教程/博客方案 | 接口监听+浏览器二合一，简单高效 | 社区小，大项目少 |
| **Chrome扩展** | 100Resume | 用户友好，真实浏览器环境 | 不易分发，需手动安装 |

### 3.2 字段爬取能力对比

| 字段 | 列表页可获取 | 详情页需进入 | API可获取 |
|------|-------------|-------------|----------|
| 岗位名称 | ✅ | ✅ | ✅ |
| 公司名称 | ✅ | ✅ | ✅ |
| 薪资范围 | ✅ | ✅ | ✅ |
| 工作地点 | ✅ | ✅ | ✅ |
| 学历要求 | ✅ | ✅ | ✅ |
| 经验要求 | ✅ | ✅ | ✅ |
| **JD全文** | ❌ | ✅ | ✅（API接口） |
| 技能标签 | ✅（部分） | ✅ | ✅ |
| HR姓名/职位 | ✅ | ✅ | ✅ |
| HR活跃状态 | ❌ | ✅ | ✅ |
| 公司规模/行业 | ✅ | ✅ | ✅ |
| 投递/沟通链接 | ❌ | ✅ | ✅ |

### 3.3 防封策略总结

| 策略 | 使用项目 | 有效性 |
|------|----------|--------|
| **随机延迟(3-8秒)** | JobClaw, DrissionPage方案, get_jobs | ⭐⭐⭐⭐ 基础必备 |
| **每日投递上限** | JobClaw(100次/天), geekgeekrun(自动暂停) | ⭐⭐⭐⭐ 重要 |
| **Cookie复用** | 所有项目 | ⭐⭐⭐⭐⭐ 必须 |
| **真实浏览器环境** | 油猴脚本类 | ⭐⭐⭐⭐⭐ 最安全 |
| **过滤不活跃岗位** | JobClaw, geekgeekrun, get_jobs | ⭐⭐⭐ 减少无效请求 |
| **代理IP轮换** | BossZP-Spider, 博客方案 | ⭐⭐⭐ 有帮助但非必须 |
| **隐藏webdriver属性** | Playwright Stealth | ⭐⭐⭐ 对抗指纹检测 |
| **验证码暂停+通知** | JobClaw(Telegram) | ⭐⭐⭐ 灵活应对 |
| **防重复投递记录** | JobClaw, Jobs_helper | ⭐⭐⭐ 避免浪费配额 |
| **家庭IP（非服务器）** | Agent-Reach建议 | ⭐⭐⭐⭐ 风控更宽松 |

---

## 四、Boss直聘反爬机制深度分析

### 4.1 核心反爬手段

1. **`__zp_stoken__` 加密Cookie**
   - 首次访问返回302重定向到 `security-check.html`
   - URL含动态参数：`seed`、`name`、`ts`、`srcReferer`、`callbackUrl`
   - 加密入口：`code = new ABC().z(seed, parseInt(ts))`
   - 每天变化一次代码，采用大控制流混淆

2. **浏览器指纹检测**
   - `fp` 参数使用AES/CBC加密
   - 检测 `navigator.webdriver`、canvas指纹
   - 检测Node.js特有对象（`__filename`、`Buffer`等）

3. **DevTools检测**（新增）
   - 检测开发者工具是否打开
   - console函数劫持

4. **行为分析**
   - 请求频率监控
   - 鼠标/滚动行为模式
   - IP信誉评估

5. **账号级风控**
   - 检测到自动化直接封禁账号
   - 限制每日沟通次数上限
   - 搜索结果最多10页

### 4.2 逆向 `__zp_stoken__` 的方法

```
方法1: 补浏览器环境（可实现100%成功率）
  → Proxy自动捕获window属性访问
  → Hook Math.random、Date等内置函数
  → 模拟canvas、document等DOM对象

方法2: 使用Playwright真实浏览器（推荐）
  → 不需要逆向，自动处理token生成
  → 配合stealth插件隐藏自动化痕迹
```

---

## 五、DrissionPage方案详解（推荐用于数据爬取）

DrissionPage是一个比较理想的"纯爬取"方案（不投递，只收集数据）：

### 核心代码框架

```python
from DrissionPage import ChromiumPage
import time

dp = ChromiumPage()

# 1. 启动接口监听
dp.listen.start('joblist')

# 2. 访问搜索页
dp.get(f'https://www.zhipin.com/web/geek/job?query=Python&city=101010100')

# 3. 循环翻页
for page in range(10):
    # 等待接口响应
    resp = dp.listen.wait()
    json_data = resp.response.body
    job_list = json_data['zpData']['jobList']
    
    for job in job_list:
        # 提取字段
        name = job.get('jobName')
        salary = job.get('salaryDesc')
        company = job.get('brandName')
        # ... 更多字段
    
    # 翻页
    dp.scroll.to_bottom()
    time.sleep(3 + random.random() * 2)  # 随机延迟
```

**关键点**:
- 监听关键词: `joblist` 或 `/joblist.json`
- 翻页: `dp.scroll.to_bottom()` 触发懒加载
- 数据在 `zpData → jobList` JSON路径下
- 翻页间隔建议3-5秒

---

## 六、API接口总结

通过抓包发现的关键API端点（`wapi` 域名）：

| 接口路径 | 功能 |
|----------|------|
| `/wapi/zpgeek/search/joblist.json` | 岗位搜索列表 |
| `/wapi/zpjob/job/detail.json` | 岗位详情（含完整JD） |
| `/wapi/zprelation/friend/getGeekFriendList.json` | 聊天列表 |
| `/wapi/zpitem/web/online/setRemind` | VIP优先提醒 |
| `/wapi/zppassport/captcha/randkey` | 登录会话初始化 |
| `/wapi/zppassport/qrcode/scan` | 扫码状态检查（长轮询） |

---

## 七、推荐方案

### 场景A：只需爬取岗位数据 → DrissionPage + 接口监听

最简单高效，代码量小，直接拿到结构化JSON。

### 场景B：需要完整JD全文 → boss-cli 或 DrissionPage进入详情页

boss-cli直接调API最稳定；DrissionPage需逐个进入详情页，速度慢但可靠。

### 场景C：需要自动投递 → 油猴脚本（最安全）

Jobs_helper（BOSS海投助手）或 boss_batch_push 的油猴方案，在真实浏览器中运行，风控检测概率最低。

### 场景D：全自动化+AI匹配 → get_jobs（Java）或 auto_get_jobs（Python）

功能最全面但风控风险最高，需要关注DevTools检测规避。

### 场景E：集成到AI Agent → mcp-bosszp 或 boss-cli

boss-cli支持JSON/YAML输出，适合程序化调用；mcp-bosszp提供MCP协议但目前存在架构缺陷。

---

## 八、风险提示

1. **账号封禁**: Boss直聘检测到自动化后直接封号，难以解封
2. **法律风险**: 爬虫仅供学习和个人数据分析，禁止商业化
3. **频率控制**: 搜索结果最多10页，每日沟通次数有上限
4. **建议**: 
   - 使用小号测试
   - 在家庭网络（非服务器/VPN）运行
   - 控制频率（单次爬取间隔≥3秒）
   - 优先选择油猴脚本方案（最安全）
   - 不要在生产环境长期运行

---

## 附录：快速参考链接

| 项目 | 链接 |
|------|------|
| get_jobs | https://github.com/loks666/get_jobs |
| boss_batch_push | https://github.com/yangfeng20/boss_batch_push |
| boss-cli | https://github.com/jackwener/boss-cli |
| mcp-bosszp | https://github.com/mucsbr/mcp-bosszp |
| Jobs_helper | https://github.com/YangShengzhou03/Jobs_helper |
| geekgeekrun | https://github.com/geekgeekrun/geekgeekrun |
| BOSScript | https://github.com/Sunny-117/BOSScript |
| auto_get_jobs | https://github.com/SanThousand/auto_get_jobs |
| get-jobs-boss | https://github.com/uniStark/get-jobs-boss |
| boss-zhipin-automation | https://github.com/wensia/boss-zhipin-automation |
| BossZP-Spider | https://github.com/SolidifyTime/BossZP-Spider |
| boss-crawl-analyzer | https://github.com/yj-liuzepeng/boss-crawl-analyzer |
| JobClaw | https://github.com/slothsheepking/jobclaw |
| 100Resume | https://100resume.aitoolhub.top/ |
| DrissionPage教程 | https://www.wsisp.com/helps/67722.html |
| __zp_stoken__逆向 | https://blog.csdn.net/qq_57325259/article/details/136320269 |
