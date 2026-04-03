# AI大模型面试八股文速查手册

> 适用岗位：大模型算法工程师、NLP算法工程师、AI研发工程师  
> 目标公司：字节跳动、阿里巴巴、腾讯、美团、快手等

---

## 📌 Python

### [了解]

**1. Python中is和==的区别？**

**核心答案**：  
`is`比较的是对象身份（内存地址），`==`比较的是值是否相等。`is`返回True的两个对象一定是同一个对象，但值相等的对象不一定`is`返回True。整数缓存机制（-5~256）会导致小整数`is`返回True。

**追问方向**：Python整数缓存范围？哪些操作会产生新对象？

---

### [必背]

**2. Python装饰器的原理和写法？**

**核心答案**：  
装饰器本质是高阶函数，接受函数作为参数并返回新函数。Python支持带参数的装饰器（双层嵌套）。常用`@functools.wraps`保留原函数元信息。类装饰器通过`__call__`方法实现。可装饰类、方法，实现日志、计时、缓存等功能。

**追问方向**：装饰器如何保留原函数元信息？多个装饰器执行顺序？类装饰器实现？

---

### [必背]

**3. 什么是GIL？为什么Python多线程无法真正实现并行？**

**核心答案**：  
GIL（全局解释器锁）是CPython的机制，同一时刻只允许一个线程执行Python字节码。目的是保证线程安全但牺牲了多核并行能力。I/O密集型任务可用多线程（切换发生在I/O时），CPU密集型任务需用多进程。`asyncio`通过协程实现并发而非并行，`concurrent.futures`提供多进程方案。

**追问方向**：哪些场景适合多线程？multiprocessing和threading区别？如何绕过GIL？

---

### [必背]（字节真题）

**4. Python生成器和迭代器的区别？**

**核心答案**：  
迭代器是实现了`__iter__`和`__next__`方法的对象，需手动实现迭代逻辑。生成器是特殊的迭代器，使用`yield`关键字自动实现迭代协议，惰性计算、节省内存。生成器表达式类似列表推导式但用圆括号，返回生成器对象。

**追问方向**：yield from的作用？生成器如何实现协程？`range`和`range`对象区别？

---

### [了解]

**5. Python中的浅拷贝和深拷贝区别？**

**核心答案**：  
浅拷贝创建新对象，复制顶层元素，但嵌套对象仍引用原对象。深拷贝递归复制所有层级，完全独立。`copy.copy()`是浅拷贝，`copy.deepcopy()`是深拷贝。不可变对象（int、str、tuple）无拷贝问题，因为引用同一个对象。

**追问方向**：Python中的引用机制？哪些情况需要深拷贝？

---

## 📌 PyTorch

### [必背]（腾讯真题）

**1. PyTorch中torch.nn.Module的forward是如何被调用的？**

**核心答案**：  
`nn.Module`实现了`__call__`方法，当调用模型实例时会自动执行`forward`方法。开发时只需定义`forward`，框架自动处理钩子（hooks）、梯度清零、推理/训练模式等。`model(x)`等价于`model.forward(x)`，但前者会触发更多生命周期管理。

**追问方向**：register_forward_hook的作用？eval()和train()模式区别？

---

### [必背]

**2. PyTorch自动微分机制（autograd）原理？**

**核心答案**：  
`torch.autograd`基于计算图实现反向传播。每个Tensor的`requires_grad=True`时，PyTorch记录操作构建DAG。`backward()`从叶子节点反向累积梯度。`detach()`截断计算图，`no_grad()`禁用梯度追踪节省显存。非叶子节点的梯度默认不会保留，需手动`retain_grad()`。

**追问方向**：叶子节点和非叶子节点区别？in-place操作对autograd的影响？

---

### [必背]（阿里真题）

**3. PyTorch训练流程关键步骤？**

**核心答案**：  
1) 设置`model.train()`模式；2) 清零梯度`optimizer.zero_grad()`；3) 前向传播计算loss；4) `loss.backward()`反向传播；5) `optimizer.step()`更新参数；6) 梯度裁剪`clip_grad_norm_`。分布式训练需`DistributedSampler`切分数据，`torch.nn.parallel`实现多卡同步。

**追问方向**：梯度累加的作用？如何选择优化器？学习率调度策略？

---

### [必背]

**4. torch.cuda.empty_cache()的使用场景？**

**核心答案**：  
释放未使用显存给GPU，但不会释放被Tensor占用的显存。适合batch size调参或模型切换时调用。配合`del`删除无用Tensor效果更好。分布式训练中，`torch.distributed.barrier()`用于同步。监控显存使用：`nvidia-smi`、PyTorch的`torch.cuda.memory_allocated()`。

**追问方向**：显存碎片化问题？如何诊断显存泄漏？

---

### [了解]

**5. PyTorch的分布式训练方式？**

**核心答案**：  
主要有`DataParallel`（DP，单机多卡，梯度汇总到主卡）和`DistributedDataParallel`（DDP，多机多卡，各卡独立反向同步，更高效）。DDP通过`torch.distributed`初始化，支持NCCL/GLOO后端。混合精度训练用`torch.cuda.amp`实现FP16加速。

**追问方向**：DP和DDP通讯开销差异？ZeRO优化器原理？

---

## 📌 HuggingFace

### [必背]

**1. HuggingFace Transformers加载模型的常见方式？**

**核心答案**：  
`AutoModel`根据预训练权重自动匹配模型结构，如`AutoModel.from_pretrained()`。`AutoTokenizer.from_pretrained()`加载对应分词器。`pipeline`提供零代码推理接口。支持本地路径加载，支持`revision`指定版本、`trust_remote_code=True`执行自定义模型。

**追问方向**：模型下载的缓存目录？如何修改模型配置？

---

### [必背]

**2. Tokenizer的encode和decode方法区别？**

**核心答案**：  
`encode`将文本转为token ID列表，`decode`将token ID列表转回文本。`__call__`方法返回字典包含input_ids、attention_mask等。分词策略包括BPE、WordPiece、SentencePiece。`padding=True`可将不同长度序列padding到统一长度，`truncation=True`截断超长序列。

**追问方向**：不同分词器对中文的影响？特殊token（[PAD]、[UNK]、[CLS]）作用？

---

### [了解]

**3. HuggingFace Trainer的优势和使用场景？**

**核心答案**：  
`Trainer`封装了训练循环、评估、logging、early stopping等通用逻辑，减少样板代码。支持TPU、多GPU训练，集成`wandb`、`tensorboard`日志。通过`TrainingArguments`配置超参数。适用于标准NLP任务微调，自定义训练需重写`Trainer`或使用原生PyTorch。

**追问方向**：Trainer如何实现分布式训练？如何添加自定义评估指标？

---

### [必背]（字节真题）

**4. 如何用HuggingFace实现模型微调（Fine-tuning）？**

**核心答案**：  
加载预训练模型和tokenizer，用自定义数据集构造`Dataset`，定义`DataCollator`处理batchpadding。使用`Trainer`或原生PyTorch训练循环。LoRA等参数高效微调方法通过`peft`库实现。保存时用`model.save_pretrained()`和`tokenizer.save_pretrained()`。

**追问方向**：全量微调和LoRA的区别？如何选择学习率和batch size？

---

### [了解]

**5. HuggingFace的datasets库如何使用？**

**核心答案**：  
`load_dataset()`支持本地和远程数据集，自动处理常见数据格式。`Dataset.map()`对数据预处理，`filter()`过滤样本，`shuffle()`打乱数据。支持流式加载`streaming=True`处理大数据集。Arrow格式实现高效序列化存储。

**追问方向**：流式加载适用场景？内存映射机制？

---

## 📌 深度学习基础

### [必背]

**1. 反向传播算法原理？**

**核心答案**：  
反向传播通过链式法则计算损失函数对各参数的梯度。前向传播计算每层输出并保存中间变量，反向从输出层向输入层逐层计算梯度并累积。梯度消失发生在深层网络连乘效应下，ReLU、BatchNorm、残差连接可缓解。梯度爆炸可通过对梯度裁剪控制。

**追问方向**：为什么ResNet能缓解梯度消失？LSTM如何解决梯度问题？

---

### [必背]

**2. Batch Normalization的作用和实现细节？**

**核心答案**：  
对mini-batch在单层特征维度上做标准化（均值0方差1），再学习scale和shift参数。作用：加速收敛、缓解梯度消失、正则化效果。训练时使用batch统计量，推理时使用移动平均的全局统计量。BN需要足够大的batch size，小batch或GAN中效果不稳定。

**追问方向**：BN和LN、IN、GN区别？推理时为何使用移动平均？

---

### [必背]

**3. 过拟合的解决方法？**

**核心答案**：  
1) 数据增强（扩充训练集）；2) 正则化（L1/L2、Dropout）；3) Early Stopping；4) 减少模型复杂度（参数量、网络深度）；5) 增加噪声或标签平滑；6) Cross-validation评估泛化能力。欠拟合则需增加模型复杂度、训练轮次或特征工程。

**追问方向**：Dropout的实现原理？训练和推理行为差异？

---

### [必背]

**4. 常用优化器及优缺点？**

**核心答案**：  
**SGD**：简单高效，需手动调学习率，收敛慢；**Momentum**：加入动量项加速收敛；**Adagrad**：自适应学习率，适合稀疏数据；**Adam**：结合动量和RMSProp，自适应学习率，是最常用选择。AdamW在Adam基础上加入权重衰减正则化，大模型训练推荐使用。

**追问方向**：Adam为何可能不收敛？学习率warmup的作用？

---

### [了解]

**5. CNN中感受野的计算？**

**核心答案**：  
感受野是特征图上某位置对应原图区域大小。第L层感受野 = 第L-1层感受野 + (kernel_sizeL - 1) × 深层卷积 stride 乘积。深层网络后面层能看到更大范围信息。大感受野有利于捕获长距离依赖，但增加计算量。空洞卷积可扩大感受野而不增加参数量。

**追问方向**：空洞卷积的gridding问题？FPN如何融合多尺度特征？

---

## 📌 大模型项目经验

### [必背]

**1. 分布式训练中数据并行和模型并行的区别？**

**核心答案**：  
**数据并行**：各卡保存完整模型副本，不同batch数据分布到各卡，计算后同步梯度。适合模型可单卡加载的场景。**模型并行**：单个模型切分到多卡（前向/反向分片），通信量更大。包括张量并行（TT）、流水线并行（PP）。Megatron-LM、DeepSpeed提供成熟方案。

**追问方向**：3D并行如何组合？梯度同步的通信开销如何优化？

---

### [必背]（阿里真题）

**2. 大模型训练中混合精度训练原理？**

**核心答案**：  
使用FP16/BF16存储权重和梯度，FP32做梯度累加和优化器状态更新，避免精度损失。PyTorch用`torch.cuda.amp.autocast`和`GradScaler`实现。BF16比FP16数值范围更大、梯度下溢问题更少，AMP需开启`device_type='cuda'`。损失缩放防止梯度下溢。

**追问方向**：混合精度训练如何选择FP16/BF16？NaN梯度问题如何排查？

---

### [必背]

**3. ZeRO优化器原理和三个Stage？**

**核心答案**：  
ZeRO（Zero Redundancy Optimizer）通过分片优化器状态、梯度、参数减少显存冗余。Stage1：分片optimizer states；Stage2：分片gradients；Stage3：分片parameters。Stage3显存节省最多但通信量最大。DeepSpeed的ZeRO-Infinity进一步支持参数卸载到CPU/NVMe。

**追问方向**：ZeRO和其他并行策略兼容性？通信开销如何估算？

---

### [必背]

**4. 大模型训练的关键超参数设置经验？**

**核心答案**：  
学习率：1e-4到3e-4（GPT-3风格warmup+cosine decay）；Batch size：参数量大时可用gradient accumulation；Weight decay：0.1（AdamW）；梯度裁剪：1.0；上下文长度大时注意attention开销。预训练tokens数量通常为数百亿到万亿级别。

**追问方向**：不同模型规模的学习率缩放规律？warmup步数选择？

---

### [了解]

**5. 如何评估大模型性能？**

**核心答案**：  
**标准Benchmark**：MMLU、BBH、GSM8K、HellaSwag等；**人类评估**：胜率、A/B测试；**特定任务**：任务相关指标（BLEU、ROUGE、F1）；**能力维度**：理解、推理、代码生成、数学等。Chatbot Arena通过Elo排名众包评估。

**追问方向**：Benchmark的局限性？如何构建私有评估集？

---

## 📌 LLM相关研发经验

### [必背]

**1. LLM预训练和微调的区别？**

**核心答案**：  
预训练在大规模无标注语料上学习语言模型能力，用Next Token Prediction目标训练，需要海量计算资源。微调在特定任务数据上调整模型参数，包括SFT（有监督微调）和RLHF（人类反馈强化学习）。预训练决定模型基座能力上限，微调决定任务适配效果。

**追问方向**：预训练语料如何清洗？Continue Pre-train和SFT区别？

---

### [必背]（腾讯真题）

**2. SFT（监督微调）和RLHF的区别？**

**核心答案**：  
SFT用标注的问答对直接训练模型，方法简单但依赖标注质量。RLHF包含三个步骤：训练Reward Model、SFT模型作为Policy、用PPO强化学习优化Policy。RLHF能使模型输出更符合人类偏好，但训练复杂、不稳定。ChatGPT/InstructGPT采用此路线。

**追问方向**：Reward Model如何训练？PPO的训练技巧？

---

### [必背]

**3. LLM推理优化方法？**

**核心答案**：  
1) **Batching**：连续batch提高GPU利用率；2) **KV Cache**：缓存已计算过的key/value避免重复计算；3) **量化**：INT8/INT4权重量化减少显存；4) **投机解码**：小模型生成draft token，大模型验证加速；5) **Flash Attention**：IO感知的注意力计算优化。

**追问方向**：PagedAttention原理？不同量化方法精度损失对比？

---

### [必背]

**4. Prompt Engineering常用技巧？**

**核心答案**：  
1) **Few-shot**：提供示例帮助模型理解格式；2) **Chain-of-Thought**：让模型输出推理步骤提升复杂推理；3) **Role Prompting**：赋予角色提升表现；4) **结构化输出**：JSON模式约束输出格式；5) **分隔符**：用XML标签等区分不同部分。

**追问方向**：如何评估Prompt效果？如何系统性优化Prompt？

---

### [了解]

**5. 模型幻觉（Hallucination）如何缓解？**

**核心答案**：  
幻觉指模型生成看似合理但实际错误的内容。缓解方法：1) RAG增强检索提供真实知识；2) Chain-of-Verification验证生成内容；3) 增加模型置信度信号；4) 后处理检测和修正；5) 改进训练数据质量。无法完全消除，但可通过工程手段降低发生率。

**追问方向**：幻觉和知识过期的区别？不同模型架构幻觉率差异？

---

## 📌 Agent开发经验

### [必背]

**1. ReAct（Reasoning + Acting）范式原理？**

**核心答案**：  
ReAct让模型交替执行"思考"和"行动"。思考（Thought）分析当前状态决定下一步，行动（Action）调用外部工具（如搜索、计算），观察（Observation）获取结果反馈给模型，形成"Thought→Action→Observation"循环。适用于需要推理+外部知识的复杂任务。

**追问方向**：ReAct和CoT区别？Tool选择策略如何设计？

---

### [必背]（字节真题）

**2. Tool Learning在Agent中的作用？**

**核心答案**：  
Tool Learning使LLM能调用外部工具扩展能力边界。常见工具：搜索API、代码执行、数据库查询、文件操作等。Function Calling是LLM调用工具的标准接口，模型输出结构化的参数JSON。工具描述需清晰定义功能、参数、返回值，帮助模型准确调用。

**追问方向**：如何处理工具调用失败？多工具协调执行策略？

---

### [必背]

**3. Multi-Agent系统的架构设计？**

**核心答案**：  
多个Agent协作完成复杂任务，通常包含：Manager Agent（分解任务、协调）、Specialist Agent（执行特定子任务）、Memory（共享知识）。协作模式：层级式（Manager主导）、去中心式（Agent自主协商）、竞争式。需设计Agent间通信协议和状态同步机制。

**追问方向**：Agent间通信瓶颈如何解决？冲突如何处理？

---

### [了解]

**4. Agent的记忆系统设计？**

**核心答案**：  
短期记忆：当前对话上下文或当前任务执行轨迹；长期记忆：持久化存储历史经验、用户偏好、知识库。实现方式：向量数据库存储、键值对结构、图数据库表示关系。记忆检索时用Embedding相似度匹配，过滤无关记忆减少干扰。

**追问方向**：记忆压缩和总结方法？记忆过期策略？

---

### [了解]

**5. 如何评估Agent系统？**

**核心答案**：  
**任务完成率**：是否达成目标；**步骤效率**：使用最少步骤完成任务；**工具使用准确性**：正确调用工具和参数；**容错能力**：错误恢复能力。构建评估集，覆盖不同难度和场景的Task，可用LLM-as-Judge评估轨迹质量。

**追问方向**：Agent评估和传统NLP评估区别？长程任务评估难点？

---

## 📌 RAG系统开发经验

### [必背]

**1. RAG系统整体架构？**

**核心答案**：  
RAG（Retrieval-Augmented Generation）由检索模块和生成模块组成。检索阶段：文档切分→Embedding向量化→建立向量索引；生成阶段：检索Top-K相关片段→拼接为Context→送入LLM生成答案。核心价值：让LLM获取最新/私有知识，解决知识截止问题。

**追问方向**：RAG vs Fine-tuning何时选择？RAG增强生成效果原理？

---

### [必背]（阿里真题）

**2. 文档Chunking策略？**

**核心答案**：  
**固定长度分块**：简单但可能切断语义；**语义分块**：按句子/段落切分，保留完整语义；**层级分块**：父子chunk维护层级关系。Chunk大小影响检索精度和Context长度，通常256-512 tokens。重叠分块可缓解边界信息丢失，但增加计算量。

**追问方向**：代码和表格如何特殊处理？如何确定最优chunk size？

---

### [必背]

**3. 向量检索方法？**

**核心答案**：  
**稠密检索**：Embedding模型编码，cosine相似度匹配；**稀疏检索**：BM25等传统关键词匹配；**混合检索**：结合稠密和稀疏。向量索引常用FAISS（IVF、HNSW）、Milvus、Pinecone等。HNSW适合在线低延迟场景，IVF-PQ适合大规模压缩。

**追问方向**：HNSW的ef/M参数调优？向量检索的召回率如何评估？

---

### [必背]

**4. RAG优化的关键技术？**

**核心答案**：  
1) **Query改写**：同义词扩展、问题分解提升检索召回；2) **重排序**：用Cross-Encoder对候选片段重排序；3) **混合检索**：结合向量和关键词检索；4) **Self-RAG**：让模型自己判断是否需要检索；5) **迭代RAG**：多轮检索-生成逐步精炼答案。

**追问方向**：RAG Fusion原理？如何处理检索到无关内容的问题？

---

### [了解]

**5. RAG和知识图谱结合？**

**核心答案**：  
知识图谱提供结构化知识，RAG提供非结构化检索能力。融合方式：1) 图谱辅助检索（实体链接→关系路径→相关文档）；2) 图谱作为Context增强生成；3) GraphRAG用社区检测和图摘要增强检索。适用场景：需要多跳推理、复杂关系查询的知识密集型任务。

**追问方向**：GraphRAG vs Naive RAG？图谱构建和维护成本？

---

## 📌 Transformer架构理解

### [必背]（字节/腾讯高频）

**1. Self-Attention的计算过程？**

**核心答案**：  
输入经过三个线性变换得到Q、K、V。对Q和K做scaled dot-product attention：$Attention(Q,K,V)=softmax(\frac{QK^T}{\sqrt{d_k}})V$。除以$\sqrt{d_k}$防止点积过大导致softmax梯度消失。多头注意力将Q/K/V分多头计算，捕获不同子空间特征，最后拼接并线性变换。

**追问方向**：为什么用多头？不同头的分工如何可视化？Flash Attention改进点？

---

### [必背]

**2. Transformer中的位置编码（Positional Encoding）？**

**核心答案**：  
Self-Attention本身是排列不变的，需要位置编码注入序列顺序信息。原始使用正弦/余弦函数（绝对位置）。旋转位置编码RoPE通过旋转矩阵实现相对位置编码，在LLM中广泛使用（如LLaMA）。ALiBi使用线性偏置替代位置编码，支持更长序列外推。

**追问方向**：RoPE为何适合LLM？位置编码如何处理128K超长上下文？

---

### [必背]

**3. Layer Normalization在Transformer中的位置？**

**核心答案**：  
Pre-LN将LN放在残差连接之前（Transformer原始使用Post-LN），训练更稳定。LN在每个样本内对特征维度做标准化，统计均值和方差。RMSNorm只计算均方根，省略均值计算，效率更高，效果相当。BatchNorm不适合序列模型因为依赖batch统计量。

**追问方向**：Pre-LN vs Post-LN训练稳定性差异？LN在推理时的作用？

---

### [必背]

**4. Transformer的FFN层作用？**

**核心答案**：  
Feed-Forward Network通常是两层全连接+激活函数（ReLU/GELU/SwiGLU）。公式：$FFN(x) = W_2 \sigma(W_1 x + b_1) + b_2$。FFN约占Transformer参数2/3，提供非线性变换和特征提取能力，是MLP在注意力机制上的扩展。SwiGLU等变体在大模型中表现更好。

**追问方向**：FFN和Attention参数量比例？SwiGLU的具体形式？

---

### [了解]

**5. Attention机制中的KV Cache作用？**

**核心答案**：  
自回归生成时，生成第t个token需要attend到前面所有token。KV Cache缓存已计算的K、V，避免每步重新计算全序列的attention。推理时空间复杂度从O(n²)降为O(n)，时间复杂度不变。需要足够显存存储KV，量化和PagedAttention可优化显存占用。

**追问方向**：MHA、MQA、GQA区别？GQA如何平衡质量和效率？

---

## 📌 面试高频追问汇总

| 问题类型 | 追问方向 |
|---------|---------|
| 模型结构 | 计算参数量、FLOPs、推理延迟估算 |
| 训练问题 | Loss不收敛、NaN、梯度爆炸排查 |
| 工程优化 | 显存估算、速度优化方法选择 |
| 原理理解 | 公式推导、与传统方法的对比 |
| 项目细节 | 数据规模、训练细节、失败经验 |

---

## 📌 快速自检清单

- [ ] 能手写Attention计算公式
- [ ] 能解释Pre-LN和Post-LN区别
- [ ] 知道AdamW vs Adam的区别
- [ ] 能描述大模型训练的关键步骤
- [ ] 能说明RAG的核心组件和流程
- [ ] 理解ReAct范式和Tool Calling
- [ ] 了解LoRA/QLoRA原理
- [ ] 知道向量检索常用算法

---

> 💡 **面试技巧**：遇到开放性问题，先给出核心答案框架，再补充细节和项目经验。主动提及与目标岗位匹配的技术栈，展示解决问题的思路。