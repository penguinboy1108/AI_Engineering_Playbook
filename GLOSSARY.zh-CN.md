# AI Engineering Glossary — 简体中文

This glossary provides preferred Chinese explanations for stable AI-engineering terms. English remains canonical for product names, APIs, code identifiers, and source titles.

| English term | 建议中文表达 | Notes |
|---|---|---|
| agent | 智能体 / Agent | 在上下文明确时保留 Agent，避免与普通“代理”混淆。 |
| agentic workflow | 智能体式工作流 | 工作流包含模型驱动的动态决策，但不一定是完全自治 Agent。 |
| abstention | 证据不足时拒绝推断 | 不应简单翻译为“拒答”；重点是基于证据边界停止。 |
| blast radius | 潜在影响范围 | 指错误、攻击或误操作能够造成的最大影响。 |
| bounded workflow | 有边界的工作流 | 控制流、权限、输入候选、重试和动作范围受到明确限制。 |
| canonical page | 权威主页面 | 同一主题中默认用于检索和回答的当前页面。 |
| candidate reduction | 候选集缩减 | 在模型推理前用确定性规则减少合法候选。 |
| checkpoint | 检查点 / 断点状态 | 保存足够状态以安全恢复，而不是保存完整思维过程。 |
| context engineering | 上下文工程 | 设计模型在每一步看到的指令、数据、工具和状态。 |
| deterministic workflow | 确定性工作流 | 主要控制流由代码或规则预定义。 |
| eval / evaluation | 评估 / Eval | 指数据集、评分器、阈值和回归流程，不只是主观试用。 |
| evidence grounding | 基于证据约束回答 | 让结论受可追溯资料约束。 |
| failure-aware retry | 识别失败类型后的重试 | 只重试可能恢复的瞬态失败；缺失业务证据时不盲目重试。 |
| false auto-accept | 错误自动接受 | 高风险自动化中最重要的后果型指标之一。 |
| grounding | 基于权威资料进行事实约束 | 不等同于简单把更多文本塞入上下文。 |
| harness engineering | Harness Engineering（执行约束与反馈系统） | 为 Agent 提供上下文、计划、工具、测试、状态恢复和治理边界。 |
| human in the loop | 人工参与 / 人审闭环 | 人类负责审批、纠错、升级或风险接受。 |
| idempotency | 幂等性 | 同一操作重复执行不会产生额外副作用。 |
| inference | 工程推断 | 从证据和约束推导出的建议，不是官方明确要求。 |
| MCP | Model Context Protocol | 通常保留 MCP，并说明它用于连接工具、资源或提示能力。 |
| observability | 可观测性 | 通过日志、指标、Trace 和关联 ID 理解系统行为。 |
| policy gate | 策略门控 | 根据业务、安全或权限规则决定继续、阻断或人审。 |
| progressive disclosure | 渐进式披露 | 先提供最小必要上下文，需要时再加载更细内容。 |
| RAG | 检索增强生成 | 回答前从外部知识源检索证据，再约束生成。 |
| reversible action | 可逆动作 | 可以撤销、修正或在最终提交前审核的动作。 |
| source of truth | 权威数据源 / 事实来源 | 业务事实应以该系统为准，而不是以模型推断为准。 |
| structured outputs | 结构化输出 | 模型输出受 Schema 约束；仍需独立业务校验。 |
| superseded | 已被替代 | 旧内容保留历史上下文，但默认不再用于当前建议。 |
| tool contract | 工具契约 | 工具输入、输出、权限、副作用、错误和幂等语义。 |
| trace | 调用链追踪 / Trace | 记录多步骤执行及其关联关系。 |
| trust boundary | 信任边界 | 数据、身份或执行权限跨越后需要重新验证的边界。 |

## Translation rules

- Keep API names, SDK names, model identifiers, environment variables, class names, and configuration keys unchanged.
- On first use, prefer `English term（中文解释）` when the Chinese translation alone may be ambiguous.
- Do not translate a vendor marketing term into a stronger technical guarantee than the source provides.
- When an English term has no stable Chinese equivalent, keep the English term and explain its operational meaning.
