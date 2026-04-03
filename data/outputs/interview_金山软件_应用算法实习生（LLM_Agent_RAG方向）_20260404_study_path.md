# AI/ML 实习面试通关 · 4周学习计划

> **目标岗位**: 大模型(LLM)/Agent/RAG 相关研发实习  
> **前置假设**: 你已具备 Python 编程基础、高等数学、线性代数、概率论基础  

---

## 📋 整体规划概览

| 周次 | 主题 | 核心技能 | 每日投入建议 |
|:---:|------|---------|:-----------:|
| **Week 1** | 深度学习理论基础 | 神经网络原理、优化算法 | 6-8小时/天 |
| **Week 2** | PyTorch 实战 | 模型实现、训练流程、调试 | 6-8小时/天 |
| **Week 3** | HuggingFace生态 | Transformer架构、预训练模型使用 | 6-8小时/天 |
| **Week 4** | 项目实战 + 模拟面试 | Agent/RAG、项目整合、面试准备 | 6-8小时/天 |

---

# Week 1 · 深度学习理论基础

## 🎯 本周目标

- [ ] 理解神经网络的核心概念（前向传播、反向传播）
- [ ] 掌握经典网络结构（CNN、RNN/LSTM/GRU）
- [ ] 理解注意力机制（Attention Mechanism）
- [ ] 能够从零推导关键公式

---

## 📅 每日学习计划

### Day 1-2: 神经网络基础

**上午 · 理论学习**
- 感知机（Perceptron）与多层感知机（MLP）
- 激活函数：Sigmoid、Tanh、ReLU、GeLU
- 前向传播（Forward Propagation）原理
- 损失函数：交叉熵、MSE

**下午 · 代码实现**
- 用 NumPy 实现一个简单的 MLP
- 参考仓库：`https://github.com/patrickloeber/numpy-from-scratch`

**晚间 · 复习巩固**
- 整理笔记：绘制前向/反向传播的计算图

---

### Day 3-4: 卷积神经网络（CNN）

**上午 · 理论学习**
- 卷积层、池化层原理
- 经典架构：LeNet、AlexNet、VGG、ResNet
- 残差连接（Residual Connection）为什么有效

**下午 · 实践**
- 用 PyTorch 实现 ResNet 关键模块
- 实践仓库：`https://github.com/patrickloeber/pytorch-from-scratch`

**晚间 · 思考题**
- 为什么 ResNet 能训练深层网络？
- Group Convolution 和 Depthwise Separable Conv 的区别？

---

### Day 5: 循环神经网络（RNN/LSTM/GRU）

**上午 · 理论学习**
- RNN 的梯度消失/爆炸问题
- LSTM 的门机制（输入门、遗忘门、输出门）
- GRU 的简化设计
- Seq2Seq 架构

**下午 · 代码实现**
- 用 PyTorch 实现 LSTM 文本分类
- 参考：`https://pytorch.org/tutorials/beginner/nlp/sequence_models_tutorial.html`

---

### Day 6: 注意力机制（Attention）

**上午 · 核心概念**
- Seq2Seq 的 Bottleneck 问题
- Attention 的 Q/K/V 思想
- Self-Attention 计算流程
- Scaled Dot-Product Attention 公式

$$Attention(Q, K, V) = softmax\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$

**下午 · 深入理解**
- Multi-Head Attention 的意义
- 为什么用 $\sqrt{d_k}$ 缩放？

**晚间 · 预习**
- 预览 Transformer 架构图

---

### Day 7: 本周复盘与检验

**上午 · 知识梳理**
- 绘制本週知识思维导图
- 整理核心公式卡片

**下午 · 模拟面试问答**

| 问题 | 考核点 | 参考答案要点 |
|-----|-------|------------|
| "解释反向传播的原理" | 链式法则 | 计算图、梯度逐层回传 |
| "LSTM是如何解决梯度消失的" | 门机制 | 遗忘门、细胞状态 |
| "为什么Transformer比RNN更适合长序列" | 注意力优势 | 并行化、无长距离依赖衰减 |
| "Multi-Head Attention的作用是什么" | 注意力变体 | 多子空间学习、表达能力 |

---

## 📚 Week 1 推荐资源

### 课程
| 资源 | 类型 | 链接 | 备注 |
|-----|------|------|-----|
| 深度学习教程 0.0.1 | 在线书籍 | https://nn.labulagion.org | 吴恩达课程配套 |
| CS231n | 课程视频 | B站搜索 | CNN基础必看 |
| 台大李宏毅机器学习 | B站课程 | 搜索"李宏毅" | 中文讲解、易理解 |

### 书籍
- 📖《深度学习入门：基于Python的理论与实现》（斋藤康毅）- 适合零基础
- 📖《动手学深度学习》(D2L) - PyTorch版：https://zh.d2l.ai/

### GitHub
- `https://github.com/patrickloeber/pytorch-from-scratch` - 从零实现PyTorch
- `https://github.com/rlabbe/Kalman-and-Bayesian-Filters-in-Python` - 滤波器的直观理解

---

# Week 2 · PyTorch 深度学习框架

## 🎯 本周目标

- [ ] 熟练使用 PyTorch 张量操作
- [ ] 掌握模型定义、数据加载、训练循环
- [ ] 理解 GPU 加速与调试技巧
- [ ] 能够独立完成一个完整的训练项目

---

## 📅 每日学习计划

### Day 1: PyTorch 基础

**上午 · 张量操作**
- 张量创建、形状变换、索引切片
- 常用运算：matmul、sum、mean、softmax
- GPU 迁移：`.cuda()` / `.to('cuda')`

**下午 · 官方文档学习**
- 重点阅读：https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html
- 完成所有示例代码

**晚间 · 练习**
- 实现矩阵分解：MovieLens 评分预测

---

### Day 2: 模型构建

**上午 · Module 结构**
- `nn.Module` 的 `__init__` 和 `forward`
- 常用层：`nn.Linear`、`nn.Conv2d`、`nn.LSTM`
- 激活函数和 Dropout

**下午 · 实践**
- 用 Module 方式重写 Week 1 的 MLP
- 学习参数管理：`model.parameters()`、`named_parameters()`

**晚间 · 挑战**
- 实现一个自定义层：带有可学习温度参数的 Softmax

---

### Day 3: 数据处理

**上午 · Dataset 和 DataLoader**
- 自定义 Dataset 的 `__len__` 和 `__getitem__`
- DataLoader 的 `batch_size`、`shuffle`、`num_workers`
- collate_fn 的使用场景

**下午 · 数据增强**
- 图像：torchvision.transforms
- 文本：tokenization、padding

**晚间 · 实践**
- 使用 HuggingFace datasets 加载 GLUE 任务数据

---

### Day 4: 训练流程

**上午 · 完整训练循环**
```python
# 标准训练模板
model.train()
for batch in dataloader:
    optimizer.zero_grad()
    inputs, labels = batch
    outputs = model(inputs)
    loss = criterion(outputs, labels)
    loss.backward()
    optimizer.step()
```

**下午 · 实践项目**
- 完成 CIFAR-10 图像分类
- 参考：`https://pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html`

**晚间 · 调优技巧**
- 学习率调度（LR Scheduler）
- Early Stopping
- Gradient Clipping

---

### Day 5: 调试与优化

**上午 · 调试技巧**
- 设置随机种子保证可复现性
- 使用 `torch.autograd.set_detect_anomaly(True)`
- Hook 机制查看中间激活值

**下午 · 性能优化**
- 混合精度训练（AMP）
- torch.compile 加速
- 梯度累积实现大 batch

**晚间 · 实践**
```python
# 混合精度训练示例
from torch.cuda.amp import autocast, GradScaler
scaler = GradScaler()
with autocast():
    outputs = model(inputs)
    loss = criterion(outputs, labels)
scaler.scale(loss).backward()
scaler.step(optimizer)
scaler.update()
```

---

### Day 6: 高级主题

**上午 · 分布式训练（选学）**
- DataParallel vs DistributedDataParallel
- 何时需要多卡训练

**下午 · 模型保存与部署**
- 模型权重保存：`torch.save`、`state_dict`
- ONNX 导出
- 加载预训练模型

**晚间 · 整理代码库**
- 建立自己的 PyTorch 工具箱仓库

---

### Day 7: 本周检验

**下午 · 实践检验**

完成以下任务并提交代码：

| 任务 | 要求 | 验收标准 |
|-----|------|---------|
| 任务1 | 用 PyTorch 实现 LSTM 语言模型 | 能生成文本、有困惑度指标 |
| 任务2 | CIFAR-10 分类训练 | 准确率 > 85%、有训练曲线 |
| 任务3 | 自定义 Dataset | 能处理任意格式数据 |

**晚间 · 面试问答**

| 问题 | 考核点 |
|-----|-------|
| "PyTorch 的动态图和 TensorFlow 的静态图有什么区别？" | 动态图优势 |
| "nn.Module 的 forward 和 __call__ 是什么关系？" | PyTorch 机制 |
| "训练时梯度爆炸如何诊断和解决？" | 调试能力 |
| "Dataloader 的 num_workers 设置多少合适？" | 工程经验 |

---

## 📚 Week 2 推荐资源

### 官方文档（必读）
| 文档 | 链接 | 重要程度 |
|-----|------|:-------:|
| PyTorch 60分钟入门 | https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html | ⭐⭐⭐ |
| 新手教程 | https://pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html | ⭐⭐⭐ |
| 官方Examples | https://github.com/pytorch/examples | ⭐⭐ |

### GitHub 项目
- `https://github.com/younggyoseo/pytorch-lambda` - 简洁的训练模板
- `https://github.com/Lightning-AI/pytorch-lightning` - 高级训练框架（选学）

### 实践项目推荐
- Kaggle 竞赛入门：Titanic、CIFAR-10
- 天池/DataFountain 入门赛

---

# Week 3 · HuggingFace 生态与 Transformer

## 🎯 本周目标

- [ ] 深入理解 Transformer 架构细节
- [ ] 熟练使用 HuggingFace Transformers 库
- [ ] 掌握预训练模型的使用、微调、部署
- [ ] 理解大模型时代的关键技术（RLHF、LoRA等）

---

## 📅 每日学习计划

### Day 1: Transformer 架构详解

**上午 · 理论深挖**
- Encoder-Decoder 结构
- Positional Encoding（正弦/旋转位置编码）
- Feed-Forward Network 设计
- Layer Normalization vs Batch Normalization

**下午 · 论文精读**
- 必读论文："Attention is All You Need"
- 关键章节：3.2/3.5/5.3（模型结构、位置编码、训练）

**晚间 · 绘图练习**
- 手绘 Transformer 完整架构图
- 标注每个模块的输入输出维度

---

### Day 2: HuggingFace Transformers 入门

**上午 · 核心概念**
- Pipeline 的使用场景
- AutoModel / AutoTokenizer 机制
- 常用模型：BERT、GPT-2、T5

**下午 · 实践**
```python
from transformers import pipeline, AutoTokenizer, AutoModel

# 3行代码完成任务
classifier = pipeline("sentiment-analysis")
result = classifier("I love learning PyTorch!")
```

**晚间 · 深入**
- 分词器原理：WordPiece、BPE、SentencePiece
- 特殊 tokens：[CLS]、[SEP]、[PAD]

---

### Day 3: 预训练模型使用

**上午 · 模型加载与保存**
- 本地加载：`AutoModel.from_pretrained("path/to/model")`
- 在线加载：HuggingFace Hub
- 模型下载加速：镜像站点设置

**下午 · 下游任务微调**
- 文本分类微调
- 命名实体识别（NER）
- 参考：`https://huggingface.co/docs/transformers/training`

**晚间 · 实践**
```python
from transformers import Trainer, TrainingArguments

training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=3,
    per_device_train_batch_size=16,
    learning_rate=2e-5,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=eval_dataset,
)

trainer.train()
```

---

### Day 4: 大模型时代技术

**上午 · GPT 系列原理**
- GPT-1/2/3/4 的演进
- In-Context Learning（上下文学习）
- Prompt Engineering 基础

**下午 · LLaMA / ChatGLM**
- 开源大模型概览
- 本地部署 ChatGLM-6B
- 参考仓库：`https://github.com/THUDM/ChatGLM-6B`

**晚间 · 思考**
- 为什么大模型能"涌现"能力？
- 模型规模与能力的 Scaling Laws

---

### Day 5: 高效微调技术

**上午 · LoRA 原理**
- Low-Rank Adaptation
- 为什么有效：矩阵分解视角
- 论文精读："LoRA: Low-Rank Adaptation of Large Language Models"

**下午 · PEFT 库实践**
```python
from peft import LoraConfig, get_peft_model

config = LoraConfig(
    r=8,
    lora_alpha=16,
    target_modules=["q_proj", "v_proj"],
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM"
)
model = get_peft_model(model, config)
```

**晚间 · 实验对比**
- 全参数微调 vs LoRA 效果对比
- 资源消耗对比

---

### Day 6: RLHF 与人类反馈

**上午 · 理论**
- Reinforcement Learning from Human Feedback
- Reward Model 训练
- PPO 算法在LLM中的应用

**下午 · 实践框架**
- TRL 库：`https://github.com/huggingface/transformers/tree/main/examples/pytorch/supervised-fine-tuning`
- 了解 SFT / RM / PPO 三阶段

**晚间 · 综述阅读**
- 综述论文："A Survey of Large Language Models"

---

### Day 7: 本周检验

**上午 · 架构理解测试**

| 问题 | 考核点 | 满分标准 |
|-----|-------|---------|
| "画出 Transformer 完整架构图" | 整体理解 | 包含所有模块和连接 |
| "解释 Rotary Position Embedding 的原理" | 位置编码 | 能数学推导 |
| "LayerNorm 为什么不使用 batch 维度？" | 归一化 | 理解NLP中BN的问题 |

**下午 · 实践任务**

| 任务 | 验收标准 |
|-----|---------|
| 任务1：使用 BERT 微调 GLUE 任务 | Accuracy > 85% |
| 任务2：LoRA 微调 GPT-2 生成特定风格文本 | 生成质量明显提升 |
| 任务3：本地部署 ChatGLM-6B 并完成问答 | 能正常运行、有demo |

**晚间 · 面试预测**

| 高频问题 | 参考回答框架 |
|---------|------------|
| "Transformer 相比 RNN 的优势？" | 并行计算、长距离依赖、位置编码 |
| "注意力机制的计算复杂度？" | O(n²d)，可优化方向 |
| "为什么用 LayerNorm 而不是 BatchNorm？" | 序列长度可变、batch size 不稳定 |
| "LoRA 的核心思想是什么？" | 低秩分解、减少参数量 |

---

## 📚 Week 3 推荐资源

### 必读论文
| 论文 | 链接 | 优先级 |
|-----|------|:-----:|
| Attention is All You Need | https://arxiv.org/abs/1706.03762 | ⭐⭐⭐ |
| BERT: Pre-training | https://arxiv.org/abs/1810.04805 | ⭐⭐⭐ |
| LoRA | https://arxiv.org/abs/2106.09685 | ⭐⭐ |
| LLaMA | https://arxiv.org/abs/2302.13971 | ⭐⭐ |

### HuggingFace 官方教程
- 官方文档：https://huggingface.co/docs/transformers/
- Course：https://huggingface.co/course
- 文档翻译：https://huggingface.co/docs/transformers/index

### GitHub 资源
- `https://github.com/huggingface/transformers` - 官方仓库
- `https://github.com/huggingface/peft` - PEFT 库
- `https://github.com/THUDM/ChatGLM-6B` - 中文大模型
- `https://github.com/nichtdax/awesome-totally-open-chatgpt` - 开源LLM列表

---

# Week 4 · 项目实战 + 模拟面试

## 🎯 本周目标

- [ ] 完成一个 Agent/RAG 实战项目
- [ ] 整理项目经历并准备 STAR 法则回答
- [ ] 完成至少 3 轮模拟面试
- [ ] 查漏补缺，补充技术盲区

---

## 📅 每日学习计划

### Day 1: Agent 开发入门

**上午 · Agent 理论**
- 什么是 AI Agent？
- ReAct / AutoGPT / BabyAGI 原理
- Agent 的核心组件：规划、记忆、工具

**下午 · 项目实战：LangChain Agent**

```python
from langchain.agents import load_tools, initialize_agent, AgentType
from langchain.llms import OpenAI

llm = OpenAI(temperature=0)
tools = load_tools(["serpapi", "llm-math"], llm=llm)
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION)
agent.run("今天北京的天气如何？顺便帮我算一下 234*567")
```

**晚间 · 项目延伸**
- 使用本地模型（ChatGLM）替代 OpenAI
- 接入自有知识库

---

### Day 2: RAG 系统开发

**上午 · RAG 原理**
- Retrieval-Augmented Generation
- Embedding 模型选择
- 向量数据库：Chroma / FAISS / Milvus

**下午 · 项目实战：本地知识库问答**

```python
# 核心流程
documents = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500)
chunks = text_splitter.split_documents(documents)

# Embedding + 存储
embeddings = HuggingFaceEmbeddings(model_name="moka-ai/m3e-base")
vectorstore = Chroma.from_documents(chunks, embeddings)

# 检索 + 生成
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
qa_chain = RetrievalQA.from_chain_type(llm=local_llm, retriever=retriever)
```

**晚间 · 项目完善**
- 添加重排序（Rerank）
- 实现多跳推理

---

### Day 3: 项目整合与文档

**上午 · 项目整理**
- 选择最优项目提交 GitHub
- 编写完整 README
- 添加 demo 视频/GIF

**下午 · 项目准备 STAR 回答**

| 项目 | Situation | Task | Action | Result |
|-----|-----------|------|--------|--------|
| RAG知识库 | 公司需要智能客服 | 构建本地知识库问答 | 用LangChain+ChatGLM实现 | QA准确率提升30% |
| Agent系统 | 重复性数据收集 | 开发自动化爬取Agent | ReAct+工具调用 | 效率提升10倍 |

**晚间 · 简历更新**
- 技术栈量化
- 突出大模型相关经验

---

### Day 4: 模拟面试（上）

**上午 · 自我介绍 + 项目讲解**
- 3分钟自我介绍模板
- 项目讲解的"电梯演讲"版本

**下午 · 技术面试 I**

**Q1: 编程题**
```python
# 经典题：实现 Transformer 的 Scaled Dot-Product Attention
def scaled_dot_product_attention(Q, K, V, mask=None):
    """
    Q: [batch, heads, seq_len, d_k]
    K: [batch, heads, seq_len, d_k]
    V: [batch, heads, seq_len, d_v]
    返回: attention output 和 attention weights
    """
    d_k = Q.shape[-1]
    scores = torch.matmul(Q, K.transpose(-2, -1)) / math.sqrt(d_k)
    if mask is not None:
        scores = scores.masked_fill(mask == 0, -1e9)
    weights = F.softmax(scores, dim=-1)
    return torch.matmul(weights, V), weights
```

**Q2: 概念题**
- "解释一下 PagedAttention"
- "如何解决 LLM 的幻觉问题？"
- "LoRA 的秩 r 怎么选择？"

**晚间 · 复盘记录**
- 回答不流畅的题目
- 需要补充的知识点

---

### Day 5: 模拟面试（中）

**上午 · 系统设计**
- 设计一个 GPTs/Agent 系统
- 设计一个企业级 RAG 系统

**系统设计框架**：
1. 需求澄清（5分钟）
2. 整体架构（10分钟）
3. 核心组件设计
4. 扩展性讨论
5. 监控与运维

**下午 · 行为面试准备**

| 问题类型 | 回答框架 | 示例问题 |
|---------|---------|---------|
| 项目经历 | STAR法则 | "最复杂的项目是什么？" |
| 困难挑战 | STAR法则 | "遇到过最大的技术难题？" |
| 学习能力 | 具体例子 | "最近学习的新技术？" |
| 团队协作 | 具体场景 | "和同事意见不一致怎么办？" |

**晚间 · 查漏补缺**
- 补充阅读：KV Cache、Prefix Tuning、Quantization

---

### Day 6: 模拟面试（下）+ 收尾

**上午 · 模拟面试 III**
- 完整45分钟模拟面试
- 录音/录像回放分析

**下午 · 技术弱点强化**

| 薄弱点 | 快速补充方案 |
|-------|------------|
| 分布式训练 | 读 Deepspeed/Megatron 文档关键部分 |
| CUDA 编程 | 跳过，面试较少考察 |
| 数学推导 | 复习 Attention、Scaled 的推导 |
| 最新论文 | 读 2024 年 LLM Survey 的关键章节 |

**晚间 · 收尾准备**
- 准备 3-5 个向面试官的问题
- 检查所有代码仓库
- 准备面试环境（双屏、稳定的网络）

---

### Day 7: 最终准备 + 心态调整

**上午 · 最终梳理**
- 核心概念速记卡（50张）
- 代码模板复习（面试时可能手写）

**下午 · 面试清单**

| 检查项 | 状态 |
|-------|:---:|
| Transformer 架构能画出来 | ✅ |
| Self-Attention 能手写代码 | ✅ |
| BERT/GPT 区别能说清楚 | ✅ |
| LoRA 原理能解释 | ✅ |
| RAG 流程能画出来 | ✅ |
| Agent 组件能列举 | ✅ |
| PyTorch 训练流程能默写 | ✅ |
| 项目经历能用 STAR 讲述 | ✅ |

**晚间 · 心态调整**
- 预演可能的失败场景
- 准备"你有什么问题问我吗"的最佳问题

---

## 📚 Week 4 推荐资源

### Agent 框架
| 框架 | GitHub | 特点 |
|-----|--------|-----|
| LangChain | https://github.com/langchain-ai/langchain | 最流行 |
| AutoGPT | https://github.com/Significant-Gravitas/AutoGPT | Agent先驱 |
| LlamaIndex | https://github.com/jerryjliu/llama_index | 专注RAG |

### RAG 工具链
| 组件 | 推荐工具 |
|-----|---------|
| Embedding | moka-ai/m3e-base、bge-large-zh |
| 向量库 | Chroma（轻量）、FAISS（Meta） |
| OCR | PaddleOCR |
| 框架 | LangChain/LlamaIndex |

### 面试准备
- 刷题：LeetCode Hot 100 / 剑指 Offer
- ML 面试题库：https://github.com/khangich/machine-learning-interview
- LLM 面试指南：https://github.com/22437302/llm-interview-notes

---

# 🎓 面试核心问题清单

## 理论必备（必须能流畅回答）

| 优先级 | 问题 | 答案要点 |
|:---:|------|---------|
| 🔴高 | Self-Attention 的计算公式 | $softmax(QK^T/\sqrt{d})V$ |
| 🔴高 | Transformer 架构图 | Encoder-Decoder 完整结构 |
| 🔴高 | BERT vs GPT 区别 | 双向 vs 因果、MLM vs CLM |
| 🔴高 | LLM 幻觉原因 | 概率生成、训练数据、缺乏 grounding |
| 🟡中 | LoRA 原理 | 低秩分解、更新 $W = W_0 + BA$ |
| 🟡中 | RAG 流程 | 切分→Embedding→检索→重排→生成 |
| 🟡中 | LayerNorm vs BatchNorm | NLP 不依赖 batch 维度 |
| 🟡中 | 位置编码类型 | 正弦、旋转（RoPE）、ALiBi |
| 🟢低 | RLHF 三步骤 | SFT → Reward Model → PPO |

## 手写代码必备

```python
# 1. Attention 实现（必须能写）
def attention(Q, K, V, mask=None):
    d_k = Q.shape[-1]
    scores = torch.matmul(Q, K.transpose(-2, -1)) / math.sqrt(d_k)
    if mask is not None:
        scores = scores.masked_fill(mask == 0, -1e9)
    return torch.matmul(F.softmax(scores, dim=-1), V)

# 2. 单层 Transformer（理解即可）
class TransformerLayer(nn.Module):
    def __init__(self, d_model, nhead):
        super().__init__()
        self.self_attn = MultiheadAttention(d_model, nhead)
        self.ff = FeedForward(d_model)
        self.norm1 = LayerNorm(d_model)
        self.norm2 = LayerNorm(d_model)
    
    def forward(self, x, mask):
        x = self.norm1(x + self.self_attn(x, x, x, mask)[0])
        x = self.norm2(x + self.ff(x))
        return x

# 3. LSTM 门机制（理解原理）
class LSTMCell(nn.Module):
    def __init__(self, input_size, hidden_size):
        super().__init__()
        self.f = nn.Linear(input_size + hidden_size, hidden_size)  # 遗忘门
        self.i = nn.Linear(input_size + hidden_size, hidden_size)  # 输入门
        self.o = nn.Linear(input_size + hidden_size, hidden_size)  # 输出门
```

---

# 📋 4周学习计划总结

```
Week 1: 深度学习理论 ──────────────────→ 理论扎实
Week 2: PyTorch 框架 ──────────────────→ 代码熟练  
Week 3: HuggingFace + Transformer ─────→ 工具掌握
Week 4: 项目 + 模拟面试 ────────────────→ 面试通关
```

## 最终检查清单

- [ ] 深度学习基础：CNN/RNN/Attention 原理清晰
- [ ] PyTorch：能独立完成训练流程
- [ ] HuggingFace：会使用 Bert/GPT/LLaMA
- [ ] Agent：理解 ReAct 范式
- [ ] RAG：能搭建本地知识库
- [ ] 项目：1-2 个可演示的项目
- [ ] 面试：能流畅回答 20 道核心问题
- [ ] 代码：能手写 Attention 和 LSTM

---

> **最后提醒**：面试中展现学习热情和思考能力比完美答案更重要！如果遇到不会的问题，展示你的分析思路会加分不少。祝你面试成功！🎉