# AI Engineering Playbook

A production-first, source-grounded engineering playbook for designing, implementing, evaluating, securing, and operating AI applications and agents.

## Source priority

1. Current official Microsoft documentation, especially Microsoft Foundry, Azure Architecture Center, Azure Well-Architected Framework, and the AI-103 study guide.
2. Current official Anthropic documentation for Claude, Claude Code, tools, MCP, context engineering, evaluation, and safety.
3. Current official OpenAI documentation for the Responses API, Agents SDK, structured outputs, evals, safety, and production operations.
4. Google Cloud and AWS primary guidance when the first three sources do not clearly cover the topic.
5. High-quality community material only as secondary explanation or implementation evidence.

## Core principles

- Production readiness over demo-only designs.
- Prefer deterministic workflows where they are sufficient; introduce agents only where adaptive reasoning adds measurable value.
- Treat security, identity, human approval, evaluation, observability, reliability, and cost control as first-class requirements.
- Separate documented vendor guidance from project-specific engineering judgment.
- Mark preview, experimental, deprecated, superseded, and unverified content explicitly.
- Every fast-changing technical claim should include a primary source and a `last_verified` date.

## Practice guides

- [Specification-Driven AI Coding and Harness Engineering](docs/workflows/specification-driven-ai-coding.md)

## Repository workflow

Weekly research updates are proposed through draft pull requests. Automated updates must not merge directly into `main`.

The initial governance and directory structure will be added in a bootstrap pull request.
