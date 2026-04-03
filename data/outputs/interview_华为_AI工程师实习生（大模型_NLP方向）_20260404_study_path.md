# 🚀 AI面试培训：4周从零到面试通关学习计划

> **目标岗位**：大模型算法工程师 / LLM研发工程师
> **适用人群**：2027届硕士/博士在读（有Python基础）
> **时间安排**：每周40小时，总计160小时

---

## 📅 第1周：工程基础夯实

### 🎯 本周目标
- 掌握Python高级编程技巧与工程实践
- 复习C++核心语法，重点面向算法实现
- 熟悉PyTorch张量操作与自动微分机制

### 📚 学习资源

| 类别 | 资源 | 链接/备注 |
|------|------|-----------|
| Python | Python高级编程 | 《Fluent Python》或《Python cookbook》 |
| Python | 数据结构与算法实现 | LeetCode Hot 100 (每天3题) |
| C++ | C++核心编程 | 《C++ Primer》或侯捷老师的视频 |
| PyTorch | 官方入门教程 | https://pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html |
| PyTorch | PyTorch深度学习实战 | 《动手学深度学习 PyTorch版》 |

### 📖 每日任务安排

| 日期 | 主题 | 任务 |
|------|------|------|
| **周一** | Python工程实践 | - 装饰器、上下文管理器、生成器实现<br>- 掌握typing模块类型注解 |
| **周二** | Python数据结构 | - 列表/字典/集合的高效用法<br>- 实现常见数据结构（栈、队列、堆） |
| **周三** | C++基础回顾 | - 指针、引用、内存管理<br>- STL容器与算法 |
| **周四** | C++面向对象 | - 类与继承、多态、虚函数<br>- 智能指针实现原理 |
| **周五** | PyTorch张量操作 | - 张量创建、索引、切片、变形<br>- GPU加速与设备管理 |
| **周六** | PyTorch自动微分 | - `torch.autograd`机制<br>- 自定义激活函数与损失函数 |
| **周日** | 整合实践 | - 用PyTorch实现多层感知机<br>- 完成C++实现LRU Cache |

### 🔬 周检验标准

**✅ 能够回答以下面试问题：**
1. Python中`list`和`tuple`的区别是什么？什么时候用哪个？
2. Python的GIL是什么？它如何影响多线程编程？
3. PyTorch中`tensor.clone()`和`tensor.detach()`的区别？
4. C++中`new`和`malloc`的区别？
5. 什么是智能指针？shared_ptr如何实现引用计数？

**✅ 能够完成以下小项目：**
- Python：实现一个简易的装饰器日志系统
- C++：实现一个线程安全的单例模式
- PyTorch：使用自定义数据集完成MNIST分类训练

---

## 📅 第2周：Transformer与NLP算法

### 🎯 本周目标
- 深入理解Transformer架构的每个组件
- 掌握Self-Attention的计算机制与实现
- 熟悉NLP常见任务与经典模型

### 📚 学习资源

| 类别 | 资源 | 链接/备注 |
|------|------|-----------|
| Transformer | Attention Is All You Need | [论文](https://arxiv.org/abs/1706.03762) + 李沐讲解 |
| Transformer | The Illustrated Transformer | http://jalammar.github.io/illustrated-transformer/ |
| Transformer | Harvard NLP注释版代码 | [The Annotated Transformer](http://nlp.seas.harvard.edu/annotated-transformer/) |
| NLP | Stanford CS224N | [B站搬运](https://www.bilibili.com/video/BV1p8411U7Ka/) |
| NLP | 《动手学深度学习》NLP章节 | d2l.ai |

### 📖 每日任务安排

| 日期 | 主题 | 任务 |
|------|------|------|
| **周一** | Transformer概述 | - 整体架构图理解<br>- Encoder-Decoder设计哲学 |
| **周二** | Self-Attention | - Q/K/V矩阵计算<br>- Scaled Dot-Product Attention公式推导 |
| **周三** | Multi-Head Attention | - 多头机制原理与代码实现<br>- 位置编码(Positional Encoding) |
| **周四** | Transformer组件 | - Feed Forward Network<br>- Layer Normalization vs Batch Normalization<br>- 残差连接 |
| **周五** | PyTorch实现Transformer | - 从零实现完整的Transformer Encoder<br>- 使用torch.nn.Transformer验证 |
| **周六** | NLP任务与模型 | - 分类、序列标注、序列到序列<br>- BERT/GPT架构对比 |
| **周日** | 经典NLP模型复现 | - 实现一个简化的BERT<br>- 复现TextCNN/TextRNN |

### 🔬 周检验标准

**✅ 能够回答以下面试问题：**
1. Transformer中为什么使用缩放点积注意力（Scaled Dot-Product Attention）？
2. 为什么Transformer需要多头注意力？头数如何选择？
3. Positional Encoding有哪些实现方式？各自优缺点？
4. Layer Normalization和Batch Normalization的区别？在Transformer中用哪个？
5. Transformer的参数量如何计算？1B参数的模型需要多少显存？

**✅ 能够完成以下小项目：**
- 使用PyTorch从零实现完整的Multi-Head Attention
- 实现一个基于Transformer的机器翻译模型（使用tiny-bleu验证）
- 复现BERT在文本分类任务上的效果

---

## 📅 第3周：大模型(LLM)与Agent系统

### 🎯 本周目标
- 理解主流LLM架构（GPT、LLaMA、PaLM等）
- 掌握大模型推理优化核心技术
- 了解Agent系统设计与工具调用机制

### 📚 学习资源

| 类别 | 资源 | 链接/备注 |
|------|------|-----------|
| LLM基础 | LLM课程（李沐） | [B站](https://space.bilibili.com/1567748478) |
| GPT系列 | GPT-1/2/3/4演进 | 论文精读 + 博客解读 |
| LLaMA | LLaMA系列 | [Meta官方](https://github.com/meta-llama) |
| 推理优化 | vLLM/FlashAttention | [GitHub](https://github.com/vllm-project/vllm) |
| Agent | LangChain文档 | https://python.langchain.com/ |
| 盘古 | 华为盘古大模型 | 官方论文 + 华为云文档 |

### 📖 每日任务安排

| 日期 | 主题 | 任务 |
|------|------|------|
| **周一** | GPT系列演进 | - GPT-1/2/3/4关键技术对比<br>- Next Token Prediction训练范式 |
| **周二** | LLaMA架构 | - RMSNorm、SwiGLU激活函数<br>- RoPE旋转位置编码详解 |
| **周三** | 大模型推理优化 | - KV Cache原理与实现<br>- 量化技术（INT8/INT4） |
| **周四** | 高效注意力机制 | - Flash Attention v1/v2原理<br>- Grouped Query Attention (GQA) |
| **周五** | Agent系统设计 | - ReAct、Chain-of-Thought<br>- Tool Use与Function Calling |
| **周六** | RAG与向量数据库 | - RAG架构设计与实现<br>- FAISS/Milvus使用 |
| **周日** | 盘古大模型专题 | - 盘古模型架构特点<br>- 华为云ModelArts使用 |

### 🔬 周检验标准

**✅ 能够回答以下面试问题：**
1. GPT和BERT的区别？各自的优缺点？
2. 什么是KV Cache？为什么能加速推理？
3. Flash Attention相比标准Attention的优势是什么？原理？
4. 什么是RoPE？为什么LLaMA要用RoPE？
5. Agent中如何解决幻觉问题？
6. RAG系统的核心组件有哪些？如何评估RAG效果？

**✅ 能够完成以下小项目：**
- 使用HuggingFace加载LLaMA-7B并进行推理
- 实现一个简单的KV Cache模块
- 构建一个基于LangChain的RAG问答系统
- 开发一个具备工具调用能力的Agent原型

---

## 📅 第4周：项目整合 + 模拟面试 + 查漏补缺

### 🎯 本周目标
- 整合前三周学习内容，完善项目经验
- 进行模拟面试，训练表达与应变能力
- 查漏补缺，确保核心知识点无死角

### 📚 学习资源

| 类别 | 资源 | 链接/备注 |
|------|------|-----------|
| 项目 | Transformers官方Examples | github.com/huggingface/transformers |
| 项目 | OpenAssistant | github.com/LAION-AI/Open-Assistant |
| 面试 | CodeTop企业面试题库 | codetop.cc |
| 面试 | 九章算法高频题 | jiuzhang.com |
| 简历 | STAR法则 | 情境、任务、行动、结果 |

### 📖 每日任务安排

| 日期 | 主题 | 任务 |
|------|------|------|
| **周一** | 项目梳理(一) | - 选定1-2个核心项目深入准备<br>- 画出项目架构图<br>- 准备技术难点与解决方案 |
| **周二** | 项目梳理(二) | - 完善GitHub项目README<br>- 准备项目演示Demo<br>- 撰写技术博客/文档 |
| **周三** | 模拟面试(一) | - 技术面：编程题（2道中等题）<br>- 自我介绍与项目介绍演练 |
| **周四** | 模拟面试(二) | - 技术面：算法与模型设计题（3道）<br>- 压力面试与行为面试准备 |
| **周五** | 知识回顾 | - 快速过一遍四周知识图谱<br>- 整理高频面试题库 |
| **周六** | 查漏补缺 | - 针对模拟面试暴露的问题专项复习<br>- 补充技术细节与边界情况 |
| **周日** | 最终准备 | - 模拟完整面试流程<br>- 调整状态，准备问题清单 |

### 🔬 周检验标准

**✅ 技术面能回答的核心问题：**

| 类别 | 问题 |
|------|------|
| **编程** | 能独立在30分钟内完成一道中等难度的LeetCode题（如合并K个有序链表） |
| **深度学习** | 解释梯度消失/爆炸的原因及解决方案 |
| **Transformer** | 从数学公式到代码实现完整推导Multi-Head Attention |
| **LLM** | 描述你参与过的大模型项目，包括架构、训练、部署等细节 |
| **系统设计** | 设计一个支持千万日活的对话系统 |

**✅ 具备完整的面试材料：**
- 📝 一份突出LLM相关经验的简历（STAR格式）
- 💻 GitHub主页包含3+个完整项目
- 🎤 1分钟/3分钟/5分钟版本的自我介绍
- 📋 10+道项目相关深度问题的回答提纲

---

## 📊 学习进度追踪表

| 周次 | 主题 | 核心技能 | 完成度 |
|------|------|----------|--------|
| 第1周 | 工程基础 | Python/C++/PyTorch | [ ] |
| 第2周 | Transformer | Self-Attention/NLP | [ ] |
| 第3周 | LLM/Agent | GPT/LLaMA/RAG | [ ] |
| 第4周 | 面试冲刺 | 项目/模拟/复盘 | [ ] |

---

## 🎁 附加资源推荐

### 📖 必读论文清单
1. **Transformer系列**: Attention Is All You Need → BERT → GPT-2 → GPT-3 → GPT-4
2. **高效Transformer**: Flash Attention, LoRA, RLHF
3. **Agent**: ReAct, AutoGPT, Toolformer

### 🛠️ 工具链
- **实验管理**: Weights & Biases / MLflow
- **模型版本**: HuggingFace Hub / ModelScope
- **算力平台**: 华为云ModelArts / AutoDL

### 📱 面试前必刷
- LeetCode Hot 100（至少完成80%）
- CodeTop 企业题库（按公司分类）
- 牛客网面经（实时更新）

---

> **💡 温馨提示**：
> - 学习是一个循序渐进的过程，不要急于求成
> - 每个知识点都要动手实践，不能只看理论
> - 模拟面试非常重要，建议找伙伴互相练习
> - 保持良好的作息，面试状态同样关键

祝你面试成功！🎉