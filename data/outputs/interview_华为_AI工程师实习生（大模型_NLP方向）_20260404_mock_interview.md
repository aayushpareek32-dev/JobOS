# 华为 AI工程师实习生（大模型/NLP方向）模拟面试题

> 面试时长：约60-90分钟
> 岗位匹配度评估：候选人项目经验与岗位高度匹配，重点考察工程落地能力与理论深度

---

## 一、项目拷打（5题）

### 第1题：MiniMind全流程训练管线

**难度**：困难  
**考查重点**：系统工程能力、分布式训练理解、工程落地细节

**主问题**：
你提到从零训练了26M参数的MiniMind，覆盖Tokenizer→Pretrain→SFT→DPO全流程。请详细描述：

1. **Tokenizer训练阶段**：6400词表大小的BPE是如何确定的？为什么选择BPE而非WordPiece或SentencePiece？在1.6GB语料上训练BPE的具体参数和耗时是多少？

2. **Pretrain阶段**：数据预处理Pipeline具体是怎样的？如何处理中文和英文的混合tokenization？训练时用了什么优化器、学习率调度策略？26M模型在2块GPU上的训练效率如何（TFLOPS/小时）？

3. **SFT阶段**：训练数据的来源和清洗流程是什么？如何构建高质量的指令数据集？SFT阶段的数据格式和loss计算方式与Pretrain有何不同？

**追问方向**：
- **[追问A-工程细节]**：你在训练过程中遇到过OOM问题吗？如何诊断和解决的？如果让你训练一个1B参数的模型，数据并行和模型并行的策略你会如何设计？
- **[追问B-理论验证]**：你提到DPO阶段对齐效果提升23%，这个23%是如何计算的？用的什么评估指标？如果要进一步提升到30%+，你会从哪些方向优化？

---

### 第2题：DPO与RLHF深度对比

**难度**：困难  
**考查重点**：对齐技术理解、PPO实现复杂度、工程权衡

**主问题**：
你提到深入对比了PPO与DPO的loss收敛曲线，请详细回答：

1. **Loss设计**：PPO的reward model loss和PPO policy loss具体是如何计算的？为什么DPO可以不需要显式的reward model？DPO的loss function推导过程能否复述？

2. **收敛曲线分析**：你在实验中观察到PPO和DPO的收敛曲线有哪些显著差异？DPO在哪些情况下可能不如PPO？

3. **工程实现**：PPO训练需要同时维护4个模型（actor、critic、reward、reference），这对显存压力巨大。你在实际实现中如何做模型卸载和gradient checkpointing？如果显存只够放2个模型，PPO还能训练吗？

**追问方向**：
- **[追问A-原理深度]**：DPO的经典论文"Direct Preference Optimization"中，作者声称DPO避免了显式reward modeling的不稳定性。请从理论上分析：DPO真的完全避免了reward hacking吗？在你的实验中观察到了alignment faking的现象吗？
- **[追问B-实战经验]**：在DPO训练中，你是如何构建正负样本对的？正负样本的质量差异对训练影响有多大？如果正负样本的偏好概率差很小（如0.51 vs 0.49），DPO的梯度信号是否足够？

---

### 第3题：RAGFlow检索系统架构

**难度**：中等  
**考查重点**：RAG系统设计、工程实现能力、性能优化

**主问题**：
RAGFlow项目中你提到混合检索+重排序使MRR@10提升15%，请详细描述：

1. **检索架构**：稠密向量检索（Embedding）和稀疏检索（BM25）各用什么具体实现？Query和Document的embedding模型是什么？为什么需要两种检索方式结合？各自的优缺点是什么？

2. **重排序细节**：ReRanker模型具体用的什么架构（如Cross-Encoder）？重排序的特征输入包含哪些（原始query、document文本、embedding相似度等）？重排序的耗时在端到端延迟中占比多少？

3. **混合策略**：两种检索结果如何融合？简单的RRF（Reciprocal Rank Fusion）公式是什么？你是否有调整过融合权重？权重如何调参的？

**追问方向**：
- **[追问A-系统设计]**：当知识库规模很大（如1亿文档）时，向量检索的近似最近邻（ANN）算法会面临精度损失。请解释HNSW和IVF-PQ的原理区别，以及在不同召回率和延迟要求下如何选型？
- **[追问B-业务场景]**：在企业级RAG场景中，用户经常问"关于X项目的所有相关文档"，这需要做知识库级别的检索聚合。你在RAGFlow中是如何设计这种聚合能力的？如果文档之间存在依赖关系（如文档B引用了文档A），如何处理？

---

### 第4题：Multi-Agent协作机制

**难度**：困难  
**考查重点**：Agent系统设计、协作协议、工程实现

**主问题**：
MetaGPT项目中你设计了数据分析Agent团队（DataCollector→Analyst→Visualizer→Reporter），请深入回答：

1. **角色定义**：四个角色的system prompt是如何设计的？每个角色收到上游输出后，如何决定自己应该做什么？是纯LLM判断还是有结构化的状态机？

2. **通信机制**：Agent之间传递的消息格式是什么？除了文本内容，是否包含结构化的元数据（如数据类型、置信度、来源等）？消息过滤机制如何实现"语义相似度过滤"？

3. **协作稳定性**：Multi-Agent系统中，某个Agent出错或输出格式不符合预期时，如何做错误恢复和重试？是否有超时机制？如何避免某个Agent陷入死循环或无限重试？

**追问方向**：
- **[追问A-协议设计]**：你提到MCP（Model Context Protocol）工具注册中心，MCP协议相比Function Calling有什么优势？在MetaGPT中如何实现一个可插拔的工具注册机制？如果需要支持100+工具，Agent如何高效地选择使用哪些工具？
- **[追问B-评测方法]**：Multi-Agent系统的输出质量如何评估？与传统单Agent相比，如何量化"协作"带来的效果提升？是否有设计Agent之间的契约协议（Interface）来约束输出格式？

---

### 第5题：KV Cache与推理优化

**难度**：困难  
**考查重点**：推理优化、GPU内存管理、工程实现

**主问题**：
你提到优化KV Cache实现，单轮推理延迟降低40%，请详细描述：

1. **基础原理**：Standard Attention和KV Cache Attention的区别是什么？Pre-fill阶段和Decode阶段分别做了什么？KV Cache存储在GPU显存中，一个130B参数的模型，在FP16精度下，单个Token的KV cache占用多少显存？

2. **优化实现**：你具体用了哪些KV Cache优化技术？PagedAttention（vLLM）了解吗？它的分块管理策略相比传统连续分配有什么优势？你的实现与vLLM的PagedAttention有何区别？

3. **流式输出**：流式输出（Streaming）的技术原理是什么？如何实现Server-Sent Events（SSE）？端到端延迟（首Token延迟 vs 整体延迟）如何权衡？

**追问方向**：
- **[追问A-量化优化]**：除了KV Cache优化，你提到推理延迟降低40%，这个数据是否包含FP8/INT8量化带来的收益？如果让你用INT8量化来进一步加速，如何处理量化误差对生成质量的影响？SmoothQuant和AWQ各有什么特点？
- **[追问B-分布式推理]**：如果需要推理7B以上的大模型，单卡显存不足，需要做Tensor Parallel或Pipeline Parallel。请解释Tensor Parallel中，Attention计算如何做张量分片（以Multi-Head Attention为例）？通信开销如何估算？

---

## 二、AI技术深度（5题）

### 第6题：手撕Self-Attention

**难度**：困难  
**考查重点**：核心算法实现、数学推导能力、工程思维

**主问题**：
请在纸上或白板上实现一个完整的Self-Attention层，要求包含：

1. **基础实现**：标准的Scaled Dot-Product Attention（包含Mask处理）

```python
# 请补充完整这个函数
def scaled_dot_product_attention(Q, K, V, mask=None):
    """
    Q: (batch_size, num_heads, seq_len, d_k)
    K: (batch_size, num_heads, seq_len, d_k)
    V: (batch_size, num_heads, seq_len, d_v)
    mask: 可选，用于Mask的tensor
    
    返回: 
    - attention_output: (batch_size, num_heads, seq_len, d_v)
    - attention_weights: (batch_size, num_heads, seq_len, seq_len)
    """
    # 请实现
```

2. **MHA实现**：实现Multi-Head Attention的完整前向传播，包括linear projection

3. **复杂度分析**：标准Attention的时间复杂度和空间复杂度各是多少？为什么Transformer选择使用Self-Attention而非RNN？

**标准答案要点**：
- ✅ 正确实现softmax后除以√d_k
- ✅ 正确实现mask（ additive mask 或 multiply mask）
- ✅ 正确处理batch维度
- ✅ 理解causal mask vs padding mask的区别
- ✅ MHA中正确使用reshape和transpose
- ✅ 复杂度分析：O(n²d)时间，O(n²)空间（存储attention matrix）

**评分标准（1-5分）**：
- 1分：无法正确实现，概念错误
- 2分：能写出基本框架，但有关键bug
- 3分：核心逻辑正确，但缺少mask处理或broadcasting有误
- 4分：完整正确实现，包含mask和projection
- 5分：实现优雅高效，额外讨论FlashAttention原理或Causal Attention优化

---

### 第7题：大模型训练核心问题

**难度**：困难  
**考查重点**：训练稳定性、分布式训练理解

**主问题**：
大模型训练中存在几个核心问题，请分别解释：

1. **Loss Spike**：预训练过程中偶尔会出现Loss突然飙升（Loss Spike），请分析可能的原因是什么？如何快速诊断和恢复？

2. **Gradient Clipping**：为什么LLM训练中梯度裁剪（通常设为1.0）是必须的？与传统的CV/NLP任务相比，大模型训练对梯度裁剪的依赖程度有何不同？

3. **Mixed Precision**：混合精度训练中，BF16和FP16各有什么优劣？为什么大模型训练推荐使用BF16而非FP16？Loss Scaling机制是解决什么问题的？

**标准答案要点**：

| 问题 | 关键点 |
|------|--------|
| Loss Spike | 1. 学习率设置不当（尤其是LR warmup不足）<br>2. 异常数据batch（脏数据、NaN/Inf）<br>3. 梯度爆炸（需检查梯度范数）<br>4. 优化器状态不一致（分布式训练同步问题）<br>5. 恢复策略：回滚checkpoint + 调整LR |
| Gradient Clipping | 1. Transformer架构在深层时梯度易爆炸<br>2. 极端batch导致梯度范数过大<br>3. 配合学习率warmup使用 |
| Mixed Precision | 1. FP16：动态范围窄，精度损失大，gradient underflow<br>2. BF16：比FP32范围更宽，exponent位数相同，尾数位数不同<br>3. Loss Scaling：解决FP16梯度下溢问题 |

**评分标准（1-5分）**：
- 1分：无法回答或回答错误
- 2分：知道基本概念，但深度不足
- 3分：能解释2个问题，第三个较浅
- 4分：三个问题都能准确回答，有实践经验
- 5分：额外讨论ZeRO optimizer、DeepSpeed等技术细节

---

### 第8题：RAG全链路深度理解

**难度**：中等  
**考查重点**：RAG系统理解、召回质量评估、端到端优化

**主问题**：
RAG（Retrieval-Augmented Generation）是大模型落地的重要范式，请回答：

1. **召回质量评估**：RAG系统中，如何评估召回（Retrieval）阶段的质量？常用的指标有哪些？请解释MRR@K、Recall@K、NDCG@K的计算方式。

2. **Context长度限制**：当检索到的文档总长度超过LLM的Context窗口时，如何处理？请列举至少3种策略，并比较优劣。

3. **RAG vs Fine-tuning**：在什么场景下选择RAG而非Fine-tuning？请从训练成本、实时性、知识更新频率、领域适配性等维度分析。

**标准答案要点**：
- **MRR@K**：Mean Reciprocal Rank，第一个正确答案的排名倒数取平均
- **Recall@K**：在前K个结果中命中的比例
- **NDCG@K**：Normalized Discounted Cumulative Gain，考虑位置加权的相关性评分
- **Context超限处理**：1）按相关性排序后截断 2）先摘要再拼接 3）分块后多次调用LLM总结 4）基于图的上下文管理
- **RAG vs FT**：RAG适合知识频繁更新、需要可解释性、多知识源融合；FT适合通用能力提升、推理模式固化、领域强适配

**评分标准（1-5分）**：
- 1分：只知道RAG基本概念，无法深入
- 2分：能说出MRR等指标，但计算方式有误
- 3分：三个问题都能回答，但深度一般
- 4分：完整准确回答，有实际调优经验
- 5分：能讨论ReAct RAG、Corrective RAG、Self-RAG等高级范式

---

### 第9题：Prompt Engineering与Agent设计

**难度**：中等  
**考查重点**：Prompt技巧、Agent架构理解

**主问题**：
大模型应用开发中，Prompt Engineering至关重要，请回答：

1. **Chain-of-Thought**：CoT（思维链）提示为什么能提升模型推理能力？请分析其内在机制。Zero-shot CoT（"Let me think step by step"）和 Few-shot CoT 有何区别？

2. **Few-shot陷阱**：Few-shot Learning中，如何选择示例样本？如果正例效果不如负例（Negative Sampling），可能是什么原因？

3. **ReAct框架**：请解释ReAct（Reasoning + Acting）范式。相比于纯Reasoning（如CoT），ReAct在什么场景下更有优势？Tool Use在其中扮演什么角色？

**标准答案要点**：
- **CoT机制**：将复杂推理拆解为中间步骤，降低单步推理难度；激活模型的"思考过程"，生成更详细的推理链
- **Zero-shot vs Few-shot**：Zero-shot CoT依赖模型自身的涌现能力；Few-shot CoT通过示例引导推理模式
- **ReAct优势**：需要外部知识/工具交互的任务（动态环境、信息检索）；避免幻觉；可追溯决策过程
- **Few-shot陷阱**：示例分布不均衡；示例与query不相关；示例顺序偏差（recency bias）

**评分标准（1-5分）**：
- 1分：只知道简单prompt编写
- 2分：能使用CoT等基础技巧，但原理理解浅
- 3分：能准确解释CoT、ReAct等框架
- 4分：完整回答+有实战调优经验
- 5分：能讨论Tree of Thoughts、Reflexion、Self-Consistency等进阶技巧

---

### 第10题：MCP协议与Tool Calling

**难度**：中等  
**考查重点**：Agent协议理解、工具调用机制

**主问题**：
你简历中多次提到MCP（Model Context Protocol）工具注册，请回答：

1. **MCP核心设计**：MCP协议相比传统的Function Calling，最大的区别是什么？MCP的Architecture包含哪些核心组件（Host、Client、Server）？各自职责是什么？

2. **Tool Schema设计**：设计一个优秀的Tool Schema（描述、parameters）有哪些最佳实践？如何处理Tool返回结果过长的问题？

3. **Tool Selection**：当Agent面对一个复杂任务，需要从大量可用工具中选择时，如何做工具选择决策？有哪些策略可以避免"过度使用工具"或"工具滥用"？

**标准答案要点**：
- **MCP优势**：标准化、可插拔、多Agent共享工具生态、解耦模型与工具
- **Tool Schema**：清晰的description、严格的JSON Schema参数定义、示例输入输出、明确返回值格式
- **Tool Selection**：1）ReAct框架的自适应选择 2）Tool Ranker预筛选 3）预算控制（Token budget） 4）层级式工具分类
- **避免滥用**：限制最大调用次数、工具调用成本感知、结果质量反馈循环

**评分标准（1-5分）**：
- 1分：对MCP/Tool Calling了解有限
- 2分：能说出基本概念，但架构理解不深
- 3分：三个问题都能回答
- 4分：结合实际项目经验深入讨论
- 5分：能对比Anthropic MCP、OpenAI Function Calling、LangChain Tool的差异

---

## 三、基础技术 + 算法（3题）

### 第11题：Python高级特性

**难度**：中等  
**考查重点**：Python深度理解、工程代码能力

**主问题**：
请解释以下Python代码的执行结果，并说明原因：

```python
# 代码段1
def func1():
    result = []
    for i in range(3):
        result.append(lambda x: x + i)
    return result

f1, f2, f3 = func1()
print([f(10) for f in [f1, f2, f3]])  # 输出什么？

# 代码段2
def func2():
    result = []
    for i in range(3):
        result.append(lambda x, i=i: x + i)  # 闭包陷阱修复
    return result

f1, f2, f3 = func2()
print([f(10) for f in [f1, f2, f3]])  # 输出什么？

# 代码段3
import asyncio

async def async_worker(n):
    await asyncio.sleep(n)
    return n

async def main():
    tasks = [async_worker(i) for i in [1, 2, 0]]
    results = await asyncio.gather(*tasks)
    print(results)

asyncio.run(main())  # 输出什么？为什么？
```

**标准答案**：
- **代码段1**：输出 `[12, 12, 12]`（闭包捕获变量i，最后值为2）
- **代码段2**：输出 `[10, 11, 12]`（默认参数捕获当前值）
- **代码段3**：输出 `[1, 2, 0]`（gather并发执行，按任务列表顺序返回结果）

**追问**：
- Python中`__init__.py`的作用是什么？如何实现一个简单的Python包？
- 什么是Python的GIL？它对多线程编程有什么影响？在什么场景下应该选择多进程而非多线程？

---

### 第12题：LRU Cache实现

**难度**：中等  
**考查重点**：数据结构设计、算法复杂度分析

**主问题**：
请实现一个线程安全的LRU（Least Recently Used）缓存，要求：

```python
from threading import Lock
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()
        self.lock = Lock()
    
    def get(self, key: str) -> str:
        # 请实现：获取key，如果存在需要更新访问顺序
        pass
    
    def put(self, key: str, value: str) -> None:
        # 请实现：插入key-value，如果超容量需要淘汰最久未使用的
        pass
```

**要求**：
1. 线程安全（使用Lock）
2. 时间复杂度为O(1)
3. 容量超限时正确淘汰

**标准答案要点**：
```python
def get(self, key: str) -> str:
    with self.lock:
        if key not in self.cache:
            return None
        self.cache.move_to_end(key)  # 更新访问顺序
        return self.cache[key]

def put(self, key: str, value: str) -> None:
    with self.lock:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # 淘汰最旧的
```

**追问**：
- OrderedDict的底层实现是什么（链表+哈希表的组合）？
- 如果需要实现LFU（Least Frequently Used）缓存，如何修改？

---

### 第13题：TopK问题与堆排序

**难度**：简单  
**考查重点**：算法基础、复杂度分析

**主问题**：
给定一个超大数组（无法全部加载到内存），找出最大的K个数，要求：
1. 时间复杂度分析
2. 空间复杂度分析
3. 给出最优解法的代码

**标准答案**：

**方法对比**：
| 方法 | 时间复杂度 | 空间复杂度 | 适用场景 |
|------|-----------|-----------|---------|
| 全局排序 | O(n log n) | O(n) | K接近n |
| 堆排序（维护小顶堆） | O(n log k) | O(k) | ⭐最优，适合流式场景 |
| QuickSelect | O(n) | O(1) | 需要全部数据 |
| 分区法 | O(n) | O(n) | K很小 |

**最优解法**：
```python
import heapq

def top_k_smallest(arr, k):
    """
    找最大的K个数 -> 维护大小为K的小顶堆
    堆顶是最小的，保持堆后堆内都是比它大的
    """
    if k <= 0:
        return []
    heap = []
    for num in arr:
        if len(heap) < k:
            heapq.heappush(heap, num)
        elif num > heap[0]:
            heapq.heapreplace(heap, num)
    return sorted(heap, reverse=True)  # 返回最大的K个
```

**追问**：
- 堆的插入和删除操作的时间复杂度是多少？
- 在大数据流式场景（无法预知总数）下，如何动态计算TopK？

---

## 四、行为面试 + 反问（2题）

### 第14题：STAR法则行为面试

**难度**：中等  
**考查重点**：问题解决能力、学习能力、团队协作

**主问题**：
请用STAR法则（Situation-Task-Action-Result）描述一个你在项目开发中遇到的**最大挑战**，以及你是如何解决的。

**追问方向**：

**[追问A-技术深度]**：
- 在解决这个问题的过程中，你是如何确定排查方向的？是否有尝试过其他方案？为什么最终选择了当前方案？
- 如果这个问题放在现在来解决，你会有什么不同的处理方式？

**[追问B-团队协作]**：
- 在解决这个问题的过程中，你是否需要与他人协作？遇到分歧时如何处理？
- 这个问题解决后，你学到了什么？它如何影响了你后续的项目实践？

**评分参考**：
- **优秀**：STAR完整清晰，有量化结果（提升XX%、节省XX时间），能反思学习
- **良好**：STAR基本完整，有结果但量化不够
- **一般**：故事不完整或过于平淡，缺乏技术深度

---

### 第15题：反问环节（推荐问题）

**难度**：简单  
**考查重点**：岗位了解程度、职业规划、技术热情

**推荐反问问题**（候选人可选择2-3个）：

**技术方向**：
1. "华为盘古大模型目前主要在哪些业务场景落地？我如果加入实习，会参与到哪个环节的工作？"
2. "团队在Agent系统设计方向目前的重点研究方向是什么？是否有论文发表或开源计划？"

**团队文化**：
3. "华为的实习项目周期通常是怎样的？是否有转正机会？转正考核主要看什么维度？"
4. "团队平时的技术分享氛围如何？是否有定期的Paper Reading或技术交流活动？"

**个人发展**：
5. "对于这个岗位，您认为最核心的能力要求是什么？我在剩余的实习时间里可以重点准备哪些方面？"

---

## 面试评估表

| 维度 | 权重 | 评估标准 |
|------|------|---------|
| **项目深度** | 30% | 对简历项目理解深入，能回答追问，不回避弱点 |
| **AI理论** | 25% | Transformer/Attention/RLHF原理清晰，能手撕代码 |
| **工程能力** | 20% | 代码实现规范，数据结构算法扎实 |
| **学习能力** | 15% | 表达清晰，逻辑性强，能举一反三 |
| **文化匹配** | 10% | 技术热情，主动性好，有华为基因（奋斗者） |

---

> **面试官备注**：
> 1. 项目经历中"规划中"项目不作为主要提问点，但可引导讨论对盘古大模型的认知
> 2. 候选人开源项目Star数较高，需评估实际贡献度
> 3. 重点考察：全链路训练经验 vs 只做应用层的区别