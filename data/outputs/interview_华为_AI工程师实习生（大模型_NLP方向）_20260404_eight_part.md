# 🎯 AI大模型面试八股文速查手册

> 适用岗位：算法工程师、NLP工程师、大模型研发、AI研究员
> 
> 标注说明：[必背] = 面试高频/必须掌握 | [了解] = 加分项/深度延伸

---

## 📌 技能点目录

1. [Python](#1-python)
2. [C++](#2-c)
3. [PyTorch](#3-pytorch)
4. [Transformer架构](#4-transformer架构)
5. [LLM/NLP项目经验](#5-llmnlp项目经验)
6. [大模型推理优化](#6-大模型推理优化)
7. [NLP算法开发](#7-nlp算法开发)
8. [Agent系统设计](#8-agent系统设计)
9. [顶会论文发表](#9-顶会论文发表)
10. [竞赛获奖经历](#10-竞赛获奖经历)

---

## 1. Python [必背]

### 面试题1

- **题目**: Python中`list`和`tuple`的区别是什么？底层实现有什么不同？

- **核心答案**: list是可变对象，支持append、insert等操作；tuple是不可变对象，可作为dict的key。底层实现上，list使用动态数组，预分配约0~8个元素槽位，扩容时创建新数组并复制（overhead大）；tuple使用紧凑固定结构，内存连续访问更快。list开销约64字节/元素，tuple约56字节/元素（64位系统）。

- **追问方向**: 追问GIL对两者性能影响、迭代器vs可迭代对象、内存分配机制

- **级别**: [必背]

---

### 面试题2

- **题目**: 解释Python的GIL（全局解释器锁）以及它对多线程的影响。如何规避？

- **核心答案**: GIL是CPython的互斥锁，保证同一时刻只有一个线程执行Python字节码。多线程适合IO密集型任务，但CPU密集型任务会被GIL限制。规避方法：① 多进程（multiprocessing）绕过GIL；② 使用C扩展释放GIL（如NumPy）；③ 异步IO（asyncio）处理并发；④ PyTorch等库计算在C/CUDA层执行，不受GIL影响。

- **追问方向**: 追问Python 3.8的per-interpreter GIL、multiprocessing vs threading场景选择

- **级别**: [必背]

---

### 面试题3

- **题目**: 什么是Python装饰器？写一个计时装饰器并说明其原理。

- **核心答案**: 装饰器是高阶函数，接受函数作为输入并返回增强后的函数。原理：wrapper函数闭包捕获原函数，在调用前后添加额外逻辑。语法糖`@decorator`等同于`func = decorator(func)`。标准模板：
```python
def timer(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        print(f"耗时: {time.time()-start:.2f}s")
        return result
    return wrapper
```

- **追问方向**: 追问带参数的装饰器、类装饰器、functools.wraps的作用

- **级别**: [必背]

---

### 面试题4

- **题目**: 字节跳动高频：描述Python中的生成器（Generator）和迭代器（Iterator）的区别与联系。

- **核心答案**: 迭代器是实现`__iter__`和`__next__`方法的对象；生成器是使用yield关键字的函数，返回迭代器。生成器是惰性计算，省内存，适合大数据处理。创建方式：① 生成器函数（yield）；② 生成器表达式（列表推导式的小写版）。可迭代对象需要实现`__iter__`方法，可使用iter()获取迭代器。

- **追问方向**: 追问yield from、生成器协程、生成器vs列表推导式的内存占用对比

- **级别**: [必背]

---

### 面试题5

- **题目**: [了解] 腾讯面试：Python中`__slots__`的作用是什么？什么时候使用？

- **核心答案**: `__slots__`限定类实例只能拥有指定的属性，替代动态`__dict__`。优点：① 减少内存占用（约40%）；② 防止随意添加属性。缺点：① 不能动态添加新属性；② 多继承时较复杂。适用于需要创建大量实例的数据类（如深度学习中的Dataset返回的样本对象）。注意：定义slots的子类也需要定义slots，否则仍有__dict__。

- **追问方向**: 追问__dict__内存模型、 dataclasses.field() vs __slots__

- **级别**: [了解]

---

## 2. C++ [必背]

### 面试题1

- **题目**: C++中`new`和`malloc`的区别是什么？智能指针有哪些？

- **核心答案**: new是运算符，调用构造函数，返回对象指针，失败抛异常；malloc是C函数，只分配内存，不调用构造函数，失败返回NULL。智能指针三种：① unique_ptr（独占所有权，不可复制，只能move）；② shared_ptr（引用计数，线程安全，额外开销）；③ weak_ptr（解决shared_ptr循环引用问题）。C++11后优先使用智能指针管理内存，避免手动delete。

- **追问方向**: 追问移动语义、右值引用、make_unique/make_shared实现原理

- **级别**: [必背]

---

### 面试题2

- **题目**: 解释C++的多态实现机制（虚函数、虚表）。

- **核心答案**: C++多态通过virtual关键字实现。每个含虚函数的类有一个虚表（vtable），存储函数指针；每个对象有一个虚指针（vptr）指向类的虚表。运行时通过vptr找到虚表，再调用相应函数，实现动态绑定（晚绑定）。构造函数不能是虚函数，析构函数通常设为虚函数（基类指针删除子类对象时正确调用析构）。纯虚函数（=0）定义抽象类。

- **追问方向**: 追问虚表布局、多继承虚表、virtual析构函数必要性

- **级别**: [必背]

---

### 面试题3

- **题目**: 阿里高频：什么是C++的RAII机制？请举例说明。

- **核心答案**: RAII（Resource Acquisition Is Initialization）即资源获取即初始化，利用对象构造/析构函数自动管理资源。典型应用：① 智能指针；② 文件句柄；③ 互斥锁。示例：构造函数获取锁，析构函数释放锁，作用域结束时自动释放，避免忘记unlock导致的死锁问题。这是C++的核心编程惯用法，比手动try-catch更安全。

- **追问方向**: 追问RAII在CUDA内存管理中的应用、lock_guard实现

- **级别**: [必背]

---

### 面试题4

- **题目**: C++中`std::vector`扩容机制是什么？如何避免频繁扩容？

- **核心答案**: vector底层是动态数组。当size==capacity时，触发扩容，典型策略是容量翻倍（GCC 2倍，MSVC 1.5倍）。扩容需要：① 分配新内存；② 拷贝/移动所有元素；③ 释放旧内存。频繁扩容导致O(n)拷贝开销。优化方式：① 使用reserve()预分配容量；② 估算大小后一次性reserve；③ 小心push_back，避免逐个插入。

- **追问方向**: 追问移动语义减少拷贝开销、vector vs list场景选择、emplace_back优势

- **级别**: [必背]

---

### 面试题5

- **题目**: [了解] C++11的lambda表达式 capture列表有哪些模式？

- **核心答案**: lambda语法：`[capture](params) -> ret { body }`。capture模式：① `[=]` 按值捕获所有变量；② `[&]` 按引用捕获所有变量；③ `[x, &y]` 混合模式；④ `[this]` 捕获this指针；⑤ `[=, &x]` 值捕获但x按引用；⑥ 初始化捕获（C++14）：`[x = std::move(x)]` 可移动语义捕获。注意：lambda本身不能修改捕获的变量（除非mutable），因为operator()默认const。

- **追问方向**: 追问泛型lambda（C++14）、STL算法中lambda使用技巧

- **级别**: [了解]

---

## 3. PyTorch [必背]

### 面试题1

- **题目**: PyTorch中`nn.Module`的`forward`和`__call__`有什么关系？如何实现hook机制？

- **核心答案**: `__call__`内部调用`forward`，但额外执行：① forward_pre_hook（forward前）；② forward；③ forward_hook（forward后）。Hook机制用于特征可视化、中间层修改、梯度捕获。API：`register_forward_hook`、`register_backward_hook`。Hook函数签名：`hook(module, input, output) -> None or output (modified)`。常用场景：提取中间层特征、debug梯度流、修改forward行为。

- **追问方向**: 追问hook与named_modules.children()的区别、如何批量remove_hook

- **级别**: [必背]

---

### 面试题2

- **题目**: PyTorch中`torch.no_grad()`和`@torch.inference_mode()`有什么区别？

- **核心答案**: 两者都禁用梯度计算，但有细微差别：① `no_grad()`设PyTorch的grad_mode=False；② `inference_mode()`更激进，同时禁止inplace写入（可能修改tensor的视图操作会被禁止），通常推理更快。两者都用于推理阶段，减少显存占用（不保存中间激活值）。训练时loss.backward()需要梯度，推理时必须使用。

- **追问方向**: 追问.eval()模式、torch.set_grad_enabled灵活控制、梯度与显存关系

- **级别**: [必背]

---

### 面试题3

- **题目**: PyTorch的DataLoader中`num_workers`参数如何设置？`pin_memory`的作用是什么？

- **核心答案**: num_workers：子进程数，0表示主进程加载（阻塞训练）。典型设置：GPU训练设4-8，CPU bound任务设2-4。过多会导致进程间通信开销、内存压力。pin_memory：锁页内存（host memory固定），加速CPU→GPU数据传输（避免中间复制）。小batch、多GPU训练时效果明显。配合`persistent_workers=True`可减少epoch间worker重启开销。

- **追问方向**: 追问多卡训练DataLoader策略、collate_fn自定义批处理、PrefetchDataLoader原理

- **级别**: [必背]

---

### 面试题4

- **题目**: 字节跳动高频：解释PyTorch的自动求导机制（autograd），包括`backward`函数和计算图。

- **核心答案**: PyTorch使用动态计算图（DCG）。前向传播构建计算图（叶子节点requires_grad=True）。反向传播时，autograd根据链式法则自动计算梯度，存储在.grad属性。`backward()`默认累积梯度（非replace），需`.zero_grad()`清零。非叶子节点梯度默认不保存（除非retain_grad()）。`torch.autograd.Function`自定义算子需实现forward和backward。

- **追问方向**: 追问DDP下梯度同步、detach与detach_区别、计算图构建开销

- **级别**: [必背]

---

### 面试题5

- **题目**: [了解] PyTorch FSDP（Fully Sharded Data Parallel）的工作原理是什么？

- **核心答案**: FSDP将模型参数分片到不同GPU，减少单卡显存。原理：① 训练step：AllGather收集完整参数→计算局部loss→AllReduce同步梯度→Gradient AllReduce→本地optimizer更新。关键参数：sharding_strategy（FULL_SHARD/ SHARD_GRAD_OP / NO_SHARD）、cpu_offload（卸载到CPU）。相比DDP，FSDP显存随GPU数量线性减少，适合超大模型。PyTorch原生支持（torch.distributed.fsdp）。

- **追问方向**: 追问ZeRO优化器区别、混合精度训练与FSDP结合

- **级别**: [了解]

---

## 4. Transformer架构 [必背]

### 面试题1

- **题目**: 详细解释Self-Attention的计算过程，复杂度是多少？

- **核心答案**: Self-Attention计算：① 输入X通过三个线性层得到Q、K、V；② 计算`S = QK^T / √d_k`（缩放点积注意力）；③ softmax归一化得到注意力权重；④ `O = SV`。复杂度：O(n²·d)，n是序列长度，d是隐层维度。Multi-head Attention将d分为h个头，独立计算后concat再线性变换。核心优势：捕获任意距离依赖（相比RNN的O(n)），可并行计算。

- **追问方向**: 追问Multi-head Attention的动机、为什么用√d_k缩放、FlashAttention原理

- **级别**: [必背]

---

### 面试题2

- **题目**: Transformer中Position Encoding的实现方式有哪些？为什么用Sinusoidal？

- **核心答案**: 位置编码方式：① Sinusoidal（绝对位置，公式：`PE(pos,2i)=sin(pos/10000^(2i/d))`）；② 可学习位置编码（BERT）；③ Relative Position Encoding（RoPE旋转位置编码，Qwen/LLaMA使用）；④ ALiBi（线性偏置）。Sinusoidal优势：① 可外推（任意长度）；② 表示相对位置（sin(a-b)可推导）；③ 无需学习参数。外推问题是当前研究热点（NTK-aware scaling、YaRN等）。

- **追问方向**: 追问RoPE的旋转矩阵实现、外推长度扩展方法

- **级别**: [必背]

---

### 面试题3

- **题目**: 阿里高频：Layer Normalization和Batch Normalization有什么区别？在Transformer中为什么用LN？

- **核心答案**: BN对batch维度归一化（均值/方差跨batch），适合CNN和batch稳定场景；LN对hidden维度归一化（均值/方差跨d_model），不依赖batch。Transformer用LN原因：① NLP任务batch常较小（1-32），BN统计不稳定；② 动态句子长度，BN处理变长序列困难；③ LN可应用于RNN（对时序步归一化）。Post-LN vs Pre-LN：Pre-LN在残差前LN（梯度更稳定），是目前主流。

- **追问方向**: 追问RMSNorm、DeepNorm、Norm位置对训练稳定性的影响

- **级别**: [必背]

---

### 面试题4

- **题目**: 腾讯面试：Transformer的FFN层作用是什么？为什么隐藏维度是输入的4倍？

- **核心答案**: FFN（Feed-Forward Network）是两层层级：Linear(d→4d) → ReLU/GELU → Linear(4d→d)。作用：① 引入非线性能力（注意力是线性+softmax）；② 跨特征空间变换，增加表达能力。4倍维度是经验值（来自原始Transformer），约等效于两个非线性变换可表达任意维度映射。更多研究探索：GELU比ReLU更平滑（Transformer使用GELU）；SwiGLU等变体进一步提升。

- **追问方向**: 追问FFN在Transformer中的参量占比（2/3）、SwiGLU实现

- **级别**: [必背]

---

### 面试题5

- **题目**: [了解] Rotary Position Embedding（RoPE）的核心思想是什么？

- **核心答案**: RoPE通过旋转矩阵对Q、K进行位置编码，避免显式加法。核心：将位置信息编码为旋转角度，Q、K乘以旋转矩阵。公式：`R(d,θ,m) = diag(cos(mθ), cos(mθ), cos(mθ+θ), cos(mθ+θ), ...)`。内积结果天然包含相对位置信息（cos(a-b)）。优势：① 无需额外参数；② 可外推；③ 与FlashAttention兼容性好（FlashAttention-2支持）。LLaMA、Qwen、ChatGLM等均使用RoPE。

- **追问方向**: 追问RoPE的数学推导、与ALiBi的对比

- **级别**: [了解]

---

## 5. LLM/NLP项目经验 [必背]

### 面试题1

- **题目**: 请介绍你参与过的一个完整NLP/大模型项目，包括数据处理、模型训练、部署上线的全流程。

- **核心答案**: 以对话系统为例：① 数据收集：爬虫/开源语料→清洗（去重、过滤低质）→标注（意图分类、实体识别）；② 训练：选基座模型→SFT（有监督微调）→RLHF（PPO/DPO）；③ 评测：自动指标（Bleu/ROUGE/PPL）+人工评估；④ 部署：量化（INT8/INT4）→加速框架（vLLM/TensorRT-LLM）→服务化（API网关、限流）；⑤ 监控：Bad Case收集→迭代优化。强调：业务理解比模型创新更重要。

- **追问方向**: 追问数据清洗具体方法、评测指标选择依据、bad case优化case

- **级别**: [必背]

---

### 面试题2

- **题目**: 字节跳动高频：你如何处理LLM的长上下文问题？有哪些优化方法？

- **核心答案**: 长上下文挑战：注意力O(n²)复杂度、显存占用大。外推优化：① 位置编码：RoPE外推（NTK scaling、YaRN）；② 分块处理：Sliding Window Attention；③ 近似注意力：FlashAttention（IO优化）、Sparse Attention。显存优化：① 量化（Qwen/LLaMA量化方案）；② 梯度checkpointing；③ 混合精度训练。业务上：评估任务是否真正需要长上下文，考虑截断+检索增强（RAG）。

- **追问方向**: 追问Longformer、BigBird稀疏注意力对比、100K+上下文实践

- **级别**: [必背]

---

### 面试题3

- **题目**: 描述一下SFT（有监督微调）和RLHF的流程与区别。

- **核心答案**: SFT：使用标注数据直接微调，格式通常为`<user> <assistant>`。优点：简单、收敛快；缺点：依赖标注质量、可能过拟合。RLHF三步：① SFT；② 训练RM（奖励模型）；③ PPO强化学习优化。核心目标：使模型输出符合人类偏好。替代方案：DPO（Direct Preference Optimization）直接用偏好数据优化，无需RM和PPO，简化流程。KL散度约束防止模型偏离SFT太远。

- **追问方向**: 追问DPO loss公式、PPO KL penalty计算、Reward Hacking问题

- **级别**: [必背]

---

### 面试题4

- **题目**: [了解] 阿里：LoRA的原理是什么？为什么能大幅减少微调参数量？

- **核心答案**: LoRA在预训练权重旁添加低秩分解矩阵。公式：`W' = W + ΔW = W + BA`（B∈R^{d×r}, A∈R^{r×k}, r<<min(d,k)）。训练时冻结W，只更新A、B。推理时将ΔW加回W（可合并）。参数量从d×k降至r×(d+k)，当r=4时，参数量减少约100倍。优势：① 显存减少（只优化小矩阵）；② 可组合多个LoRA（多任务切换）；③ 原模型不变，保留泛化能力。QLoRA进一步结合4-bit NormalFloat量化。

- **追问方向**: 追问LoRA rank选择、Adapter vs LoRA、DoRA新方法

- **级别**: [了解]

---

### 面试题5

- **题目**: [了解] 腾讯：你对模型量化有什么了解？INT8/INT4量化的区别和使用场景？

- **核心答案**: 量化将float32→int8/int4，减少显存和加速。方式：① PTQ（训练后量化）：简单但精度损失大；② QAT（量化感知训练）：训练时模拟量化。INT8：每值1字节（约4x显存压缩），精度损失可接受，适合推理加速。INT4：每值0.5字节（约8x压缩），精度损失明显，需配合AWQ/GPTQ等方法。LLM用SmoothQuant（平滑异常值）、AWQ（Activation-aware权重量化）等先进方法保持精度。

- **追问方向**: 追问量化误差来源、LLM.int8()论文核心观点

- **级别**: [了解]

---

## 6. 大模型推理优化 [必背]

### 面试题1

- **题目**: 解释LLM推理的两个阶段：Prefill和Decode，它们的特点和优化方向是什么？

- **核心答案**: Prefill阶段：处理用户输入prompt，计算KV Cache。特点：计算密集，batch_size可较大，适合并行优化。Decode阶段：自回归逐token生成。特点：序列短但逐个生成，访存密集（每次只生成1 token但需读取大模型），batching效率低。Prefill优化：Prompt Cache、Batched Prefill。Decode优化：KV Cache管理、Continuous Batching（iteration-level batching）、Speculative Decoding（投机解码）。

- **追问方向**: 追问Continuous Batching vs Static Batching、Decode的访存瓶颈

- **级别**: [必背]

---

### 面试题2

- **题目**: 什么是Continuous Batching（持续批处理）？相比Static Batching有什么优势？

- **核心答案**: Static Batching：整个batch全部完成才处理新请求，空转等待最慢的序列，GPU利用率低。Continuous Batching：iteration完成后立即移出完成的序列，插入新序列，实现动态batch。Orca论文提出。优势：大幅提升吞吐（3-5x），减少平均TTFT（首token延迟）。代价：调度更复杂，需处理变长序列。vLLM的PagedAttention是实现之一。

- **追问方向**: 追问preemption处理（OOM时抢占）、prefill与decode混合调度

- **级别**: [必背]

---

### 面试题3

- **题目**: 字节跳动高频：Speculative Decoding的原理是什么？能达到什么效果？

- **核心答案**: Speculative Decoding（投机解码）：使用小模型（Drafter）快速生成多个候选token，再用大模型（Verifier）并行验证。接受率通常>80%。流程：① 小模型生成k个token；② 大模型并行计算这k+1个位置的logits；③ 按接受规则（贪婪/采样）决定接受多少token；④ 如果需要，回退到贪婪。大模型单步计算时间≈小模型k步，加速比约k倍（受接受率影响）。关键：小模型与大模型分布一致性好。

- **追问方向**: 追问不同Drafter选择、树结构解码、Medusa方法

- **级别**: [必背]

---

### 面试题4

- **题目**: 什么是KV Cache？为什么它对LLM推理至关重要？有什么优化方法？

- **核心答案**: KV Cache：缓存已计算的Key-Value，避免重复计算。每个token生成都需要访问之前所有token的K/V。显存占用：2×layers×seq_len²×head_dim×fp16，约等于`2 * num_layers * batch_size * seq_len² * hidden_dim / 1024` MB。优化：① PagedAttention/vLLM分页管理；② FlashAttention减少HBM访问；③ KV Cache量化（INT8/FP8）；④ Prefix Caching（前缀复用）；⑤ 跨请求共享系统提示的KV。

- **追问方向**: 追问MHA vs MQA vs GQA的区别与显存占用对比

- **级别**: [必背]

---

### 面试题5

- **题目**: [了解] TensorRT-LLM和vLLM的区别是什么？各自适用场景？

- **核心答案**: vLLM：专注Throughput，使用PagedAttention优化显存管理，支持Continuous Batching，适合高并发在线服务。TensorRT-LLM：专注Latency，使用TensorRT深度优化（kernel fusion、INT8/FP8），但batch管理较简单，适合低延迟场景。量化支持：vLLM支持AWQ、GPTQ；TensorRT-LLM支持FP8、INT8。A的女儿国：追求高吞吐选vLLM，追求单次请求低延迟选TensorRT-LLM。实际可结合：前端vLLM，后端TensorRT-LLM做推理引擎。

- **追问方向**: 追问SGLang、LightLLM等新框架特点

- **级别**: [了解]

---

## 7. NLP算法开发 [必背]

### 面试题1

- **题目**: 请介绍常见的文本表示方法：Word2Vec、BERT、Sentence-BERT的区别和适用场景。

- **核心答案**: Word2Vec：词级别embedding，静态表示（bank在所有语境相同）。训练快，词表内效果好。BERT： token级别上下文表示（bank不同语境不同），适合序列标注、分类等fine-tuning任务。SBERT：在BERT基础上加入Pooling，输出句子向量，适合语义相似度、聚类、检索。Sentence-BERT训练使用对比学习。选型：词义消歧→BERT；句子匹配/检索→SBERT；词级别任务→Word2Vec/ERNIE。

- **追问方向**: 追问Embedding的维度选择、向量检索工具（Faiss/Milvus）、embedding召回率

- **级别**: [必背]

---

### 面试题2

- **题目**: 阿里高频：NER（命名实体识别）的常用方法有哪些？如何处理嵌套实体？

- **核心答案**: NER方法演进：① 规则+词典（早期）；② CRF（BiLSTM-CRF）；③ BERT+CRF/BERT+Softmax；④ 指针网络（多头标注）；⑤ 多任务学习。嵌套实体处理：① 序列标注扩展（标注所有实体的起止）；② 指针网络+层叠指针；③ MRC（阅读理解）：问"谁在上海？"提取组织；④ Global Pointer：统一建模起止位置，内积判断是否构成实体。Span层叠可能导致标签不平衡。

- **追问方向**: 追问损失函数设计（Focal Loss）、实体类型不平衡处理

- **级别**: [必背]

---

### 面试题3

- **题目**: 腾讯面试：TextCNN、BiLSTM、Transformer在文本分类中的优缺点对比。

- **核心答案**: TextCNN：卷积核捕获n-gram特征，并行度高、速度快；缺点：感受野有限、长距离依赖弱。BiLSTM：捕获序列依赖，语义连贯性好；缺点：并行度低、长序列训练慢。Transformer：全局注意力、并行好、支持长依赖；缺点：短文本任务可能过拟合、计算量O(n²)。选型建议：短文本/特征提取→TextCNN；中等长度→BiLSTM；长文本/复杂语义→Transformer/BERT。

- **追问方向**: 追问TextCNN卷积核设计、Hierarchical Attention Network

- **级别**: [必背]

---

### 面试题4

- **题目**: [了解] 你对RAG（检索增强生成）系统有什么理解？核心组件有哪些？

- **核心答案**: RAG核心思想：检索相关知识+LLM生成回答，解决LLM幻觉、知识过时问题。核心组件：① 文档处理：PDF/HTML解析→chunking（语义分块）；② 向量数据库：Milvus/Pinecone/Weaviate，存储embedding；③ 检索：dense retrieval（Embedding匹配）+稀疏检索（BM25）+混合检索；④ 生成：构建prompt（query+context+instruction）；⑤ 优化：rerank、重排序、query改写、Self-RAG。评估：RAGAS指标。

- **追问方向**: 追问向量数据库选型、Chunk size策略、RAG vs Fine-tuning场景

- **级别**: [了解]

---

### 面试题5

- **题目**: [了解] 介绍一下Attention Is All You Need论文的核心贡献。

- **核心答案**: 核心贡献：① 提出Transformer架构，完全基于Attention机制（取代RNN）；② Scale Dot-Product Attention + Multi-Head Attention；③ Position Encoding引入序列位置信息；④ 机器翻译任务SOTA；⑤ 证明了注意力机制的强大表达力。后续影响：BERT（双向下下文）、GPT（LMR）、ViT（CV领域）等。论文发表自Google Brain/NIPS 2017，被引用超10万次，是深度学习里程碑工作。

- **追问方向**: 追问与GPT的区别、原始论文的实验细节

- **级别**: [了解]

---

## 8. Agent系统设计 [必背]

### 面试题1

- **题目**: 什么是AI Agent？核心组件有哪些？请举例一个你设计的Agent系统。

- **核心答案**: Agent = LLM + Memory + Planning + Tools。核心组件：① 规划（Planning）：任务拆解（CoT/SCoT）、自我反思；② 记忆（Memory）：短期记忆（上下文窗口）、长期记忆（向量数据库）；③ 工具（Tools）：API调用、代码执行、搜索；④ 行动（Action）：执行计划、调用工具、输出结果。以客服Agent为例：理解意图→检索知识库→调用API查询→生成回复→评估满意度→持续学习。ReAct范式：Thought+Action+Observation循环。

- **追问方向**: 追问Multi-Agent协作、Agent安全边界、Hallucination控制

- **级别**: [必背]

---

### 面试题2

- **题目**: 字节跳动高频：Tool Learning和Function Calling有什么区别？如何设计一个Function Calling系统？

- **核心答案**: Function Calling是LLM调用外部工具的技术范式，本质是让LLM输出结构化JSON（函数名+参数）。设计要点：① 定义清晰的函数schema（名称、描述、参数类型）；② Few-shot示例引导；③ 参数校验和错误处理；④ 降级策略（function call失败时fallback）。常见场景：查询天气、订机票、数据库查询。GPT-4/OpenAI提供原生支持，LangChain有实现。对比Tool Learning：更结构化、依赖模型原生支持。

- **追问方向**: 追问并行function calling、function calling评估指标

- **级别**: [必背]

---

### 面试题3

- **题目**: 如何解决Agent系统的Planning能力不足问题？

- **核心答案**: Planning改进方法：① Chain-of-Thought：让Agent先思考步骤再执行；② Self-Correction：Plan→Execute→Evaluate→Refine；③ Tree-of-Thought：探索多条路径；④ ReWOO：分离观察与计划，减少token消耗；⑤ MUSE：使用LLM作为规划器微调。关键：提供足够上下文（工具说明、示例）、限制搜索深度防止组合爆炸、让Agent明确子目标。

- **追问方向**: 追问ReAct vs Plan-and-Execute架构、Reflexion自我反思

- **级别**: [必背]

---

### 面试题4

- **题目**: [了解] Multi-Agent系统如何设计？Agent间如何通信？

- **核心答案**: Multi-Agent架构：① 层级式：一个主Agent协调多个子Agent；② 对等式：Agent间平等协作；③ 竞争式：多个Agent协商决策。通信方式：① 共享内存/消息队列；② 共享LLM上下文（通过系统prompt）；③ 结构化协议（Actor模型）。设计挑战：① 任务分解与分配；② 避免Agent重复工作；③ 状态同步；④ 通信开销控制。案例：ChatDev（软件开发）、MetaGPT（软件工程）。

- **追问方向**: 追问Agent角色定义、共识机制、冲突解决

- **级别**: [了解]

---

### 面试题5

- **题目**: [了解] 腾讯：如何评估Agent系统的效果？有哪些评测指标？

- **核心答案**: Agent评测维度：① 任务完成率：正确调用工具序列达到目标；② 准确率：函数参数正确性；③ 效率：调用次数、token消耗；④ 稳定性：多次运行一致性。评测方法：① 人工评估（gold标准）；② 规则匹配（检查关键步骤）；③ LLM-as-Judge（让GPT-4评估）；④ 特定任务Benchmark（ToolBench、API-Bank）。注意：Agent系统端到端评估困难，需要细粒度拆解。

- **追问方向**: 追问评估集构建、Agent幻觉率统计

- **级别**: [了解]

---

## 9. 顶会论文发表 [了解]

### 面试题1

- **题目**: 请介绍一下你发表/阅读过的与LLM相关的顶会论文。

- **核心答案**: 以LLM相关论文为例，介绍框架：① 问题动机：现有方法痛点；② 核心方法：创新点；③ 实验验证：数据集、Baseline对比、效果提升；④ 局限性&未来工作。示例：《LLaMA: Open and Efficient Foundation Models》- 动机：小模型+大数据Scaling；方法：Chinchilla-optimal训练；效果：7B模型超越GPT-3(175B)。强调：面试官更关注你对论文核心思想的理解，而非逐字背诵。

- **追问方向**: 追问论文细节、实验设置、复现可能性

- **级别**: [了解]

---

### 面试题2

- **题目**: [了解] 你对ICLR/NeurIPS/ACL/EMNLP等NLP/AI顶会的审稿流程有什么了解？

- **核心答案**: ACL/EMNLP：ACL Rolling Review（ACR）+ Area Chair双盲审；NeurIPS/ICLR：OpenReview（署名审稿），可看到审稿意见和作者 rebuttal。审稿周期：投稿→分配AC→分配审稿人→审稿→Rebuttal→Meta Review→Accept/Reject。顶会关注创新性（Novelty）、实验完整性（Solidity）、可复现性（Reproducibility）、写作质量。AC通常10-20篇，审稿人3-5篇/论文。

- **追问方向**: 追问rebuttal技巧、如何回答"What is your contribution?"

- **级别**: [了解]

---

### 面试题3

- **题目**: [了解] 阿里：如果让你设计一个论文实验，你会考虑哪些维度？

- **核心答案**: 实验设计维度：① 主实验：核心贡献是否成立，对比SOTA；② 消融实验：每个组件的贡献；③ 鲁棒性：不同随机种子、数据集规模、模型大小；④ 敏感度分析：超参数影响；⑤ 可视化：注意力、特征分析；⑥ 人类评估：主观质量；⑦ 错误分析：Bad Case归类。统计显著性：多次实验求均值±std。开源代码：提升论文可复现性和影响力。

- **追问方向**: 追问实验资源预算分配、如何确定Baseline

- **级别**: [了解]

---

## 10. 竞赛获奖经历 [了解]

### 面试题1

- **题目**: 请介绍一下你参与/获奖的竞赛经历，包括赛题理解、方案设计、最终排名。

- **核心答案**: 介绍框架：① 赛题背景：任务类型（分类/排序/生成）、数据特点；② 团队分工：算法/特征/后处理；③ 方案演进：Baseline→最终方案的关键迭代；④ 创新点：哪些设计带来显著提升；⑤ 最终成绩：Top X%。强调：不仅是排名，更要突出解决问题的思路、团队协作、快速迭代能力。提到具体数据：如将准确率从80%提升到85%。

- **追问方向**: 追问团队协作分工、为何放弃某些方案

- **级别**: [了解]

---

### 面试题2

- **题目**: [了解] 竞赛中如何进行数据分析和特征工程？

- **核心答案**: 数据分析：① 分布统计（类别、长尾）；② 缺失值/异常值检测；③ 相关性分析。特征工程：① 文本特征：TF-IDF、词频、长度统计；② BERT embedding统计量（mean pooling）；③ 伪标签（半监督）；④ 数据增强（回译、同义词替换）。竞赛技巧：① 查看公开讨论区；② 分析public/private leaderboard差异（防过拟合）；③ 模型融合（加权平均、stacking）。

- **追问方向**: 追问数据泄露检测、时间序列比赛注意点

- **级别**: [了解]

---

### 面试题3

- **题目**: [了解] 腾讯：如何处理竞赛中的过拟合和