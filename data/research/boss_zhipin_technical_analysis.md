# Boss直聘（zhipin.com）技术逆向分析报告

> 生成时间：2026-04-04
> 调研来源：公开技术博客、GitHub开源项目、CSDN、掘金、博客园、Bilibili等
> 声明：本报告仅供学习研究使用，请遵守平台服务条款

---

## 一、搜索结果页数据来源分析

### 1.1 结论：Ajax API 请求（非 SSR）

Boss直聘搜索结果页采用 **Ajax 异步加载 + 前端动态渲染** 模式，**不是** SSR（服务端渲染）。

- 前端技术栈：**Vue.js + jQuery** 混合架构
- 数据通过 XHR/Fetch 请求后端 API，返回 JSON，前端渲染
- jQuery 处理 AJAX 请求，且使用了 AJAX 代理拦截，直接 hook 原生 XHR 无法获取响应

### 1.2 核心搜索 API

```
GET https://www.zhipin.com/wapi/zpgeek/search/joblist.json
```

**请求参数：**
| 参数 | 说明 | 示例 |
|------|------|------|
| query | 搜索关键词 | `AI实习` |
| city | 城市编码 | `101200100`（武汉） |
| page | 页码 | `1` |
| pageSize | 每页条数 | `30`（固定） |
| experience | 工作经验 | `101`（不限） |
| degree | 学历要求 | `204`（本科） |

**响应结构：**
```json
{
  "code": 0,
  "message": "Success",
  "zpData": {
    "jobList": [
      {
        "encryptJobId": "xxx",       // 加密职位ID，构造详情页URL用
        "encryptBossId": "xxx",      // 加密Boss ID
        "securityId": "xxx",         // 安全ID（唯一标识）
        "jobName": "AI算法实习生",
        "salaryDesc": "4-6K",
        "jobLabels": ["实习", "AI"],
        "jobDegree": "本科",
        "jobExperience": "在校/应届",
        "cityName": "武汉",
        "areaDistrict": "洪山区",
        "businessDistrict": "光谷",
        "brandName": "XX科技",
        "brandScaleName": "100-499人",
        "brandIndustry": "人工智能",
        "brandStageName": "B轮",
        "bossName": "张先生",
        "bossTitle": "技术总监",
        "bossCert": 1,
        "skills": ["Python", "PyTorch", "NLP"],
        "wt": 1            // 在线状态
      }
      // ... 每页30条
    ],
    "hasMore": true,
    "lastJobId": "xxx",
    "resCount": 256        // 搜索结果总数
  }
}
```

### 1.3 其他已知 API 端点

| 端点 | 用途 |
|------|------|
| `/wapi/zpgeek/search/joblist.json` | 搜索职位列表 |
| `/wapi/zpgeek/recommend/job/list.json` | 推荐职位列表 |
| `/wapi/zpgeek/history/joblist.json` | 历史浏览职位 |
| `/wapi/zpgeek/view/job/card.json` | 职位卡片详情 |
| `/wapi/zpgeek/recommend/conditions.json` | 推荐筛选条件 |
| `/wapi/zpCommon/data/city.json` | 城市数据 |
| `/wapi/zpCommon/data/position.json` | 职位分类数据 |
| `/wapi/zpCommon/data/oldindustry.json` | 行业分类数据 |

---

## 二、岗位详情页完整 JD 获取

### 2.1 详情页 URL 构造

```
https://www.zhipin.com/job_detail/{encryptJobId}.html
```

其中 `encryptJobId` 从搜索结果 API 响应中获取。

### 2.2 详情页数据获取方式

**重要发现：详情页是 HTML 页面，不是纯 API 接口。** 需要通过以下方式获取完整 JD：

#### 方式一：浏览器自动化 + HTML 解析（推荐）

```python
# 使用 Playwright
page.goto(f"https://www.zhipin.com/job_detail/{encrypt_job_id}.html")
# 职位描述在 .job-sec-text 元素中
jd_text = page.locator(".job-sec-text").inner_text()
# 或使用 page.evaluate
jd_html = page.evaluate('document.querySelector(".job-sec-text").innerHTML')
```

#### 方式二：DrissionPage 监听 + 元素定位

```python
# DrissionPage 方式
tab.get(url)
jd_elements = tab.eles(".job-sec-text")
jd_content = jd_elements[0].html if jd_elements else ""
```

#### 方式三：BeautifulSoup 解析

```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
jd = soup.select_one('.detail-content .text')
# 或 '.job-sec-text'
```

### 2.3 详情页关键 CSS 选择器

| 选择器 | 内容 |
|--------|------|
| `.job-sec-text` | 职位描述（完整JD） |
| `.job-detail .name h1` | 职位名称 |
| `.job-detail .salary` | 薪资范围 |
| `.job-detail .info-primary .sider-info` | 公司信息 |
| `.job-tags .tag-item` | 职位标签 |
| `.detail-figure-btn` | Boss头像/联系按钮 |

### 2.4 注意事项

- 详情页需要 **登录态** 才能看到完整信息
- 未登录时部分内容可能被折叠或隐藏
- 频繁访问详情页会触发验证码

---

## 三、HR 联系方式 / 在线聊天链接

### 3.1 获取方式

Boss直聘的设计理念是「直接沟通」，**不提供HR电话/邮箱等直接联系方式**，所有沟通通过平台内聊天完成。

#### 聊天入口构造

```
https://www.zhipin.com/web/geek/chat?id={encryptBossId}&securityId={securityId}
```

其中：
- `encryptBossId` — 从搜索结果中获取
- `securityId` — 从搜索结果中获取

#### 发起沟通

在详情页点击「立即沟通」按钮等同于：
1. 向 `/wapi/zpgeek/friend/add.json` 发送添加好友请求
2. 成功后跳转到聊天页面

### 3.2 聊天系统技术架构

Boss直聘的即时通讯系统采用：

| 组件 | 技术 |
|------|------|
| 传输层 | WebSocket |
| 协议层 | MQTT（基于 Paho MQTT 库） |
| 序列化 | Google Protocol Buffers (protobuf) |
| 服务端 | `wss://ws.zhipin.com:443` |
| Topic | `/chatws` |

**连接参数：**
- Host: `ws.zhipin.com`
- Port: 443 (SSL)
- Client ID: `ws-{随机16字符HEX}`
- 需要用户名和密码（从登录态获取）

### 3.3 自动化沟通限制

- 每天沟通次数有上限（约100-200次/天）
- 沟通后需等待HR回复，才能发送简历
- 频繁沟通会触发风控，账号可能被临时禁用
- **2025年9月新规**：使用自动化工具的账号会被 **禁用PC/网页端登录2个月**

---

## 四、反爬机制深度分析

### 4.1 核心反爬：`__zp_stoken__` Cookie

这是Boss直聘最关键的反爬机制。

#### 生成流程

```
1. 客户端发送初始请求
2. 服务器返回 set-cookie，包含 seed 和 ts 参数
3. 浏览器端 JS 执行：code = (new ABC).z(seed, parseInt(ts))
4. 生成的 code 写入 cookie 作为 __zp_stoken__
5. 后续 API 请求携带该 cookie
```

#### 技术特征

- **动态代码**：生成算法的 JS 代码每天变化
- **环境检测**：检测 Node.js 特征（`__filename`、`Buffer`等）
- **大控制流混淆**：JS 代码采用 OB 混淆 + 控制流平坦化
- **浏览器指纹**：检测 `OfflineAudioContext`、`canvas` 等 API
- `Math.random()` 和 `Date` 是造成 token 动态变化的关键因素

#### 错误码含义

| 错误码 | 含义 |
|--------|------|
| 0 | 请求成功 |
| 35 | 触发图片验证码 |
| 37 | `zp_stoken` 无效或过期 |

#### 绕过方案

| 方案 | 难度 | 成功率 | 维护成本 |
|------|------|--------|----------|
| Playwright 浏览器自动化 | ★★☆ | 高 | 低 |
| DrissionPage 监听 API | ★★☆ | 高 | 低 |
| WebSocket RPC 补环境 | ★★★★ | 极高(100%) | 高（每日更新） |
| 纯 JS 逆向补环境 | ★★★★★ | 极高 | 极高 |
| requests 直接调用 | ★☆☆ | 极低 | — |

**推荐方案**：使用 **Playwright / DrissionPage 浏览器自动化**，通过监听网络请求获取 API 响应数据，无需逆向 token 算法。

### 4.2 验证码体系

Boss直聘集成了 **双验证码系统**：

| 验证码供应商 | 识别特征 | 类型 |
|-------------|----------|------|
| 极验 (GeeTest) | 圆形按钮 | 滑动验证、文字点选 |
| 网易易盾 (NetEase) | 盾牌标识 | 图标点选、九宫格 |

**触发条件：**
- 同一 IP 短时间内大量请求
- 未携带有效 `zp_stoken`
- 异常行为检测（非人类操作模式）
- 新设备/新IP首次访问

**无感验证**：后台通过行为指纹分析用户操作轨迹、鼠标速度、点击频率等特征，可能在用户无感知情况下完成验证。

### 4.3 Cookie / 会话管理

- 登录状态依赖 Cookie 维持
- 每次新开浏览器会丢失登录态
- 关键 Cookie：`wt2`（登录凭证）、`__zp_stoken__`（反爬token）、`Hm_lvt_*`（百度统计）
- Cookie 有效期有限，需定期刷新

### 4.4 频率限制 & IP 封禁

| 限制类型 | 详情 |
|----------|------|
| IP 级别 | 同一 IP 频繁请求会被暂时封禁 |
| 账号级别 | 单账号每日投递/沟通次数有上限 |
| 建议间隔 | 请求之间 3-5 秒随机延迟 |
| 恢复方式 | 切换 IP（WiFi/飞行模式重连） |

### 4.5 其他反爬措施

- **请求头检测**：必须携带正确的 `User-Agent`、`Referer`
- **TLS 指纹**：可能检测 TLS ClientHello 指纹
- **WebDriver 检测**：检测 `navigator.webdriver` 属性
- **jQuery AJAX 代理**：平台使用 AJAX 代理，直接拦截原生 XHR 无法获取响应

---

## 五、2025-2026 年新反爬措施

### 5.1 AI 风控系统全面上线（2025年）

**重大变化**：Boss直聘在2025年部署了 AI 大模型风控系统：

- **全年封禁账号中 80% 由 AI 系统主动拦截**
- AI 具备语义识别和行为建模两大核心能力
- 能识别「简历工具人」（被用于刷单/诈骗的账号），准确率超 80%
- 全年推送安全提示近 **2.5 亿次**

### 5.2 自动化工具封禁（2025年9月）

**关键政策调整**：
- 平台对账号登录策略进行调整
- **使用自动化工具（Selenium/Playwright/AutoJS等）的账号会被禁用 PC 客户端和网页端登录 2 个月**
- 检测维度包括：WebDriver 属性、操作频率、行为模式、设备指纹

### 5.3 三道防线框架

Boss直聘建立了完整的安全防线体系：

1. **核心守护区**：登录/注册环节的强验证
2. **风险缓冲区**：行为异常的中间拦截
3. **生态共治区**：用户举报 + AI 巡检的联合治理

### 5.4 2026年趋势预判

基于2025年的升级趋势，预计2026年：
- AI 行为检测会更加精准，覆盖更多操作维度
- 设备指纹采集更加深入（GPU/Audio/Canvas/WebGL 指纹）
- 可能引入更多生物特征验证（人脸识别登录已在App端使用）
- 对自动化工具的检测和惩罚力度持续加大

---

## 六、推荐技术方案

### 6.1 最佳实践：Playwright 持久化上下文

```python
from playwright.async_api import async_playwright

async def create_boss_browser():
    p = await async_playwright().start()
    browser = await p.chromium.launch_persistent_context(
        user_data_dir="./boss_user_data",
        headless=False,    # 首次需要 headed 手动登录
        args=[
            "--disable-blink-features=AutomationControlled",
            "--no-sandbox",
        ],
        user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) ...",
        viewport={"width": 1920, "height": 1080},
    )
    return browser

# 登录状态检测
async def is_logged_in(page):
    try:
        await page.wait_for_selector('a[href*="/web/geek/chat"]', timeout=5000)
        return True
    except:
        return False

# 监听 API 响应获取数据
async def intercept_job_list(page):
    jobs = []
    async def handle_response(response):
        if "/wapi/zpgeek/search/joblist.json" in response.url:
            data = await response.json()
            if data.get("code") == 0:
                jobs.extend(data["zpData"]["jobList"])
    page.on("response", handle_response)
    return jobs
```

### 6.2 数据提取流程

```
1. 启动持久化浏览器（首次手动登录，后续自动复用）
2. 访问搜索页，监听 /wapi/zpgeek/search/joblist.json 响应
3. 从响应中提取 jobList（基本信息 + encryptJobId）
4. 逐个访问详情页，提取 .job-sec-text 中的完整 JD
5. 控制请求频率：3-5 秒随机间隔
6. 遇到验证码暂停，人工处理或调用识别服务
7. 数据存入本地数据库
```

### 6.3 风险控制建议

| 建议 | 说明 |
|------|------|
| 使用家庭网络 | 家庭 IP 风控相对宽松 |
| 控制频率 | 请求间隔 3-5 秒 + 随机延迟 |
| 不用主号 | 测试时使用备用账号 |
| 持久化浏览器 | 避免反复登录触发风控 |
| 拟人化操作 | 添加鼠标移动、滚动等行为 |
| 限制日请求量 | 每天采集量控制在合理范围 |
| 备用方案 | 准备好 IP 切换策略 |

---

## 七、与 JobForge 集成建议

### 7.1 推荐架构

```
JobForge Boss采集模块
├── boss_browser.py        # Playwright 浏览器管理（持久化登录）
├── boss_search.py         # 搜索API监听 + 结果解析
├── boss_detail.py         # 详情页JD提取
├── boss_chat.py           # 沟通链接构造（不建议自动化聊天）
├── boss_antibot.py        # 反爬策略（频率控制/验证码处理）
└── boss_models.py         # 数据模型定义
```

### 7.2 数据获取优先级

1. **搜索列表API**（高优先）— 获取基本信息+加密ID，结构化JSON，效率最高
2. **详情页HTML**（中优先）— 获取完整JD，需要逐页访问，有频率限制
3. **聊天链接构造**（低优先）— 仅构造链接，实际聊天由用户手动完成
4. **WebSocket聊天**（不建议）— 风险极高，容易封号

### 7.3 替代方案

如果直接爬取风险太高，可考虑：
- **Greasemonkey/Tampermonkey 用户脚本**：用户手动浏览时自动提取数据（参考 greasyfork.org 上的「Boss直聘JD/HR信息提取」脚本）
- **浏览器扩展**：开发 Chrome 扩展，在用户正常浏览时后台提取数据
- **剪贴板模式**：用户复制页面内容，工具解析提取结构化数据

---

## 八、参考资源

| 资源 | 链接 | 说明 |
|------|------|------|
| boss-cli | github.com/jackwener/boss-cli | Python CLI工具，逆向API |
| boss-crawl-analyzer | github.com/yj-liuzepeng/boss-crawl-analyzer | Web界面爬虫+分析 |
| BossZP-Spider | github.com/SolidifyTime/BossZP-Spider | 爬虫工具 |
| boss-zhipin-automation | github.com/wensia/boss-zhipin-automation | 自动化投递 |
| Playwright爬虫Boss直聘 | blog.felicx.eu.org | 完整教程 |
| zp_stoken逆向 | 掘金/CSDN多篇 | token算法分析 |
| BOSS直聘JD/HR提取脚本 | greasyfork.org | 用户脚本 |
| Apify Boss Zhipin Scraper | apify.com | 云端采集服务 |
