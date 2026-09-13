# AI-learning

## AI 阅读约定

- `#` 普通注释
- `##` 我自己写的注释
- `##?` 我不懂，请解释
- `##!` 我觉得可能有问题，请检查

请优先检查 `##?` 和 `##!`，不要重写全部代码。




记录我从 Python 与数学地基走向大模型系统理解的长期学习过程。

> 当前原则：  
> **阶段 0 不碰 PyTorch、不看 Transformer 论文、不研究 Kimi K3。**  
> 每个阶段以“可运行产出 + 白纸复述 + commit 记录”为验收标准，不以“看过/听懂”为进度。

---

## 长期路线图：阶段 0 - 阶段 5

### 阶段 0：地基期

**目标**：拥有进入 AI 领域的最低门槛能力。

| 模块 | 内容 | 验收标准 |
|---|---|---|
| Python | 基础语法、NumPy、面向对象、装饰器、生成器 | 能独立写出带类的数据管道，无 bug |
| 数学 | 线性代数、多元微积分、概率论 | 能手推矩阵求导、理解正态分布 KL 散度 |
| 工具 | Git、Linux、Conda、VS Code、LaTeX | 能在 Linux 服务器配环境、写技术文档 |

**当前状态**：非完全零基础，执行 10 周加速版。  
**进入下一阶段条件**：阶段 0 八条硬性门槛全部通过。

---

### 阶段 1：深度学习入门

**目标**：理解神经网络如何工作，能独立训练简单模型。

| 模块 | 内容 | 验收标准 |
|---|---|---|
| 机器学习基础 | 监督/无监督学习、损失函数、梯度下降、正则化、偏差-方差权衡 | 能用 NumPy 手写逻辑回归和浅层神经网络 |
| PyTorch | Tensor 操作、自动求导、DataLoader、模型定义、训练循环 | 能独立在 CIFAR-10 上训练 ResNet-18 达到 90%+ 准确率 |
| 经典网络 | CNN、RNN/LSTM、Adam、BatchNorm、Dropout | 能口述每层输入输出维度变化 |
| 第一个项目 | 端到端项目，如图像分类 + 部署 | GitHub 仓库、README 清晰、可复现 |

**关键提醒**：阶段 1 才开始系统使用 PyTorch；阶段 0 不许提前滑入调包式学习。

---

### 阶段 2：Transformer 与 NLP 深入

**目标**：彻底理解 Transformer，能从头实现 GPT-2 规模模型。

| 模块 | 内容 | 验收标准 |
|---|---|---|
| 注意力机制 | Self-Attention、Multi-Head Attention、Masked Attention、位置编码 | 能手写 Attention 矩阵运算过程，包括 Q/K/V 维度变化 |
| Transformer 架构 | Encoder-Decoder、LayerNorm、残差连接、FFN | 能用 PyTorch 从头写完整 Transformer，不抄 HuggingFace |
| 预训练与微调 | MLM、CLM、Prompt Tuning、LoRA、指令微调 | 能在小型语料上预训练 GPT-small，约 100M 参数 |
| HuggingFace 生态 | Transformers、Datasets、Tokenizers、Accelerate | 能微调 BERT 做文本分类，理解 BPE |

**关键里程碑**：不看任何资料，在白纸上画出 Transformer 完整架构图，并写出 Attention 伪代码。

---

### 阶段 3：大模型与 MoE 专项

**目标**：理解 MoE、长上下文、推理优化和系统级优化。

| 模块 | 内容 | 验收标准 |
|---|---|---|
| MoE 架构 | Switch Transformer、Mixtral 8x7B、专家路由、负载均衡损失、容量因子 | 能解释 Top-K 路由数学过程，理解 auxiliary loss |
| 分布式训练 | DDP、TP、PP、ZeRO | 能在 4 卡 GPU 上训练 MoE 模型，理解通信开销 |
| 长上下文 | ALiBi、RoPE、YaRN、LongRoPE、Ring Attention、稀疏注意力 | 能把 4K 上下文模型扩展到 32K，理解位置编码外推 |
| 推理优化 | KV Cache、PageAttention/vLLM、GPTQ/AWQ、投机采样 | 能用 vLLM 部署 7B 模型并做性能 profiling |
| 系统级优化 | 通信计算重叠、双批次、EP | 理解 DeepSpeed-MoE 与 Megatron-LM 的 MoE 实现差异 |

**关键难点**：MoE 的系统级优化比算法更难，需要补 GPU 内存层次、NCCL 通信原语、CUDA kernel 基础。

---

### 阶段 4：Kimi K3 深度解剖

**目标**：完全理解 K3 的每一个设计选择，并能提出改进。

| 模块 | 内容 | 验收标准 |
|---|---|---|
| K3 技术报告精读 | KDA、Stable LatentMoE、训练策略 | 能写出 K3 完整架构说明文档，包括每一层维度 |
| KDA 机制 | Key-Dependent Attention 数学形式，与 MHA/GQA 的区别 | 能手推 KDA 公式，理解 Key 如何影响注意力计算 |
| 权重分析 | 加载 K3 开放权重，分析专家激活、注意力头特化、层间信息流 | 能画出专家路由热力图，发现专家任务特化 |
| 社区实现 | 精读 MLX 社区 1138 行 K3 推理代码 | 能添加一个功能，如新的采样策略 |
| 对比研究 | K3 对比 DeepSeek-V3、Qwen3、Llama 4 | 能写技术博客，指出 K3 的 3 个优势和 2 个潜在改进点 |

**最大难点**：KDA 是 Kimi 原创机制，公开资料少，需要“读报告公式 + 社区实现反推 + 小规模实验验证”。

---

### 阶段 5：L5 专家 / 终局

**目标**：能提出原创改进，产出研究或工程成果。

达到阶段 5 的标志不是“学完了”，而是至少完成一项输出：

- 发表一篇关于 MoE 路由改进或注意力机制优化的论文，至少顶会 workshop 级别；
- 或主导一个大规模模型训练/推理优化项目；
- 或向 K3 社区实现提交有意义的 PR。

**本阶段产出要求**：  
所有博客、论文草稿、实验记录、性能 profiling 报告都必须沉淀到本仓库或关联仓库中，不允许只停留在口头理解。