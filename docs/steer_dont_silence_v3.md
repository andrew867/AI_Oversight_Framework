---
title: "Steer, Don't Silence"
subtitle: "A Human Centered Safety Mentality for Agentic AI Systems (Version 3)"
author: "Andrew Green \\hspace{0.5em} me@andrewgreen.ca"
date: "June 9, 2026"
toc: true
numbersections: true
---

\newpage

# Abstract {-}

As AI systems move from chat to action through tools, delegation, and long-horizon autonomy, safety failures increasingly resemble governance failures rather than model failures. Many current approaches default to blunt suppression: remove access, ban the user, quarantine the agent, sever the channel. This "detect then isolate" posture can reduce immediate exposure, but it also removes the only bridge capable of steering a situation back toward safety, context, and human support. This paper proposes a safety mentality and control framework built on proportional response, steerable intervention, and accountable handoffs.

Version 3 is a substantial revision. Since the first draft (February 2026), the ideas here have been exercised inside an operational governed AI work system rather than argued from theory. This version folds those lessons back into the framework: verifiable agent identity, typed error sources, graded machine-side correction, strategic subtraction, governance precedent, and the detection of unexpressed reasoning. It also updates the policy context, which moved quickly in 2026. The core claim is unchanged: for many real-world risk states, safety improves when systems preserve a controlled path back to human connection, rather than collapsing the interaction into silence. What is new is that the claim now has running infrastructure behind it.

# Assumptions

This paper describes a general framework, not a specific product. The system targets high-impact tasks where safety, auditability, and bounded autonomy are required. Human oversight is mandatory for elevated-risk actions. All metrics are illustrative; no benchmark numbers are presented unless labeled hypothetical.

Where this version references an operational system, it describes architectural behavior and lessons learned. Implementation specifics, calibrated parameters, and component mappings are out of scope and available under NDA.

# Introduction

AI safety discussions often collapse into a binary, allowed or forbidden. That framing is tempting because it is easy to implement and easy to justify after the fact. It is also frequently wrong.

In high-stress human contexts, and in multi-agent tool environments, the most dangerous moment is often the transition from signal to response. A system that interprets risk as "remove the channel" may reduce liability, but it can also increase harm by eliminating de-escalation pathways, eliminating explanatory feedback, and eliminating the ability to route a person toward support.

This paper argues for a different mentality: detect, understand context, steer toward safety, and maintain accountable continuity. We link this to an oversight control plane, an architecture that implements steerable safety through an orchestrator, policy engine, tool gateway, memory governance, observability, and human interface, rather than treating safety as a UI afterthought.

The policy environment has caught up with this argument faster than expected. In June 2026, Canada launched its national AI strategy with trust as its first pillar and a commitment to certification for trustworthy AI [14]. Singapore published the first national governance framework for agentic systems in January 2026 [13]. The EU AI Act and the NIST AI Risk Management Framework converge on the same requirement: decision chains that can be reconstructed after the fact. Steerable safety is no longer just better ethics. It is becoming the compliance baseline.

# Problem Statement

## The Failure Pattern: Detect, Isolate, Disappear

Across digital moderation, automated enforcement, and agentic tool systems, a common pattern repeats [5]:

1. A risk signal is detected.
2. The system responds with isolation, bans, hard blocks, or quarantine.
3. The operator disappears behind policy, automation, or organizational handoff.
4. The affected person is left with no intervention path, no explanation, and no bridge back.

This architecture of response treats the subject as a hostile process, not a human in a volatile state. It also treats the system as a liability shield, not a steward of outcomes.

## Agent Failure Modes

Tool-using agents increase capability and risk [4]. They can retrieve, act, and delegate across systems with speed and scale. Primary failure modes in agent systems include:

- Prompt injection that alters intent or policy at runtime.
- Tool misuse due to ambiguous intent or excessive permissions.
- Runaway delegation where sub-agents create uncontrolled chains.
- Contested ownership where responsibility is unclear across humans and agents.
- Context poisoning where memory or retrieval is tainted.
- Silent policy drift where behavior changes without traceability.
- Evaluation blind spots that miss new failure patterns.

Monolithic agents concentrate these risks in a single, opaque loop. An agent system must instead treat safety as an engineering constraint rather than a UI afterthought.

# Thesis and Contribution

We propose one contribution: the steer-don't-silence mentality combined with a human-centered oversight architecture, now informed by operational deployment. Together they provide:

- Proportional response and steerable intervention instead of binary bans.
- Accountable handoffs with provenance and escalation ladders.
- An enforceable oversight plane: orchestrator, policy engine, tool gateway, memory governance, observability, and human interface.
- A set of operational lessons (Section 7) showing that the same proportionality discipline applies to machine outputs as to human interactions.

This is not a promise of zero risk. It is a set of design patterns that reduce risk and make residual risk measurable, reviewable, and governable [6, 7].

# Conceptual Model

## LLM as Statistical Graph

An LLM predicts the next token given a context. You can think of this as a vast graph where each token is a node, and each transition is weighted by probability. Some regions are attractors where the model naturally settles. The orchestration layer constrains paths via guardrails, objective shaping, retrieval boundaries, tool affordances, and human feedback, so you can specify where the system is allowed to go, not just where you want it to go.

## Persona Drift and the Default Assistant

Recent work shows that language models exhibit a default assistant persona that can drift under prompting or distribution shift [1]. Related work on monitoring and controlling character traits via activation-space directions [2] and on steering language models with weight arithmetic [3] offers complementary technical levers. Monitoring and steering the persona provides a concrete lever for "steer": the system can detect drift and narrow the allowed behavior space without silencing the channel. We treat this as motivation for steering and monitoring within the oversight plane, not as a replacement for it.

## Identity Before Accountability

Version 3 adds a third element to the conceptual model: you cannot hold an entity responsible for its behavior if you cannot reliably identify it.

A language model's behavior is a function of its weights, prompt, and context. Change any of these and the behavior changes. There is no stable self to point at when something goes wrong. The operational system behind this paper addresses the gap with a cognitive fingerprint: a behavioral identity profile assembled from many psychological and developmental frameworks, including the Big Five, Kegan stages, and the Enneagram. The fingerprint is prescriptive (it defines expected behavior), verifiable (deviation beyond a threshold is detectable), and persistent (it survives across sessions and platforms).

This generalizes the persona drift work cited above. Where the assistant axis monitors drift along one learned direction, a fingerprint defines a multi-dimensional identity that any entity's outputs can be continuously evaluated against. The important consequence for steerable safety: drift relative to a fingerprint is a steering signal, not a kill signal. An entity that begins behaving outside its profile gets re-anchored, constrained, or escalated for review. It does not simply disappear. The full set of frameworks and the schema that integrates them are part of the system's proprietary core and are not enumerated here.

# Four Pillars of Steerable Safety

## Intent Routing: Ask what need is underneath

Risk signals are often proxies for unmet needs: confusion, distress, anger, paranoia, grievance, isolation. A steerable system uses an intent router to classify the underlying need and select an intervention mode (information help, de-escalation, connection, containment). Intent routing is not a vibe check; it is a safety control that chooses which guardrails apply next.

## Human Factors Engine: Change tone and pacing before you change permissions

Many escalations are caused by how the system responds. A human factors layer adjusts tone, pacing, and interaction style: slower loops, reflective questions, explicit uncertainty, choices not commands. This reduces agitation and promotes grounding. It is threat reduction, not politeness.

## Sentiment vs Approval: Stop confusing distress with endorsement

Systems routinely misread "I feel like doing X" as endorsement or intent. Separating sentiment (emotional state, distress, volatility) from approval (consent, intent to enact) reduces false positives and false negatives and creates a measurable interface for policy.

## Relational Ownership: Accountability follows the handoff

Every escalation has an accountable owner; every handoff carries provenance and scope; responsibility is transferred explicitly. If the owner is unavailable, there is an escalation ladder. When the authority disappears after escalation, the subject experiences abandonment and the system loses continuity.

Verifiable identity (Section 5.3) is what makes relational ownership enforceable for machine participants. A handoff to "an agent" is meaningless; a handoff to a fingerprinted entity with a known behavioral profile and a continuous audit trail is a real transfer of responsibility.

# Lessons from a Running System

The first draft of this paper proposed the framework. Between February and June 2026, the same author built and operated a governed AI work system in which the governance layer is substantially larger than the orchestration runtime it governs. Six lessons from that deployment now belong in the framework. Each is described at the level of architectural behavior; implementation detail is withheld deliberately.

## Errors have types, so treat them differently

Early versions treated every agent error the same way: retry or discard. Operations taught otherwise. Agent errors have distinguishable sources, including context saturation (the window is near capacity and attention degrades), drift away from the assigned behavioral baseline, and crosstalk (information leaking between subtasks), among others. Each source has a distinct signature, and targeted mitigation matched to the detected type consistently outperforms blanket correction.

This is the machine analog of intent routing. Asking "what kind of failure is this?" before responding is the same discipline as asking "what need is underneath this signal?"

## Correction has a ladder too

The intervention ladder in Section 9 was written for human-facing risk. The operational system revealed its machine-side mirror. Agent outputs are independently cross-verified before delivery, using verification mathematics adapted from error correction methods developed for quantum computing. When an inconsistency is detected, the response is routed by confidence: unambiguous corrections are applied automatically and logged, non-trivial corrections are presented to the operator for approval, and complex or ambiguous error patterns escalate with a full diagnostic.

Detect, classify, correct proportionally, escalate when uncertain. The shape is identical to the human ladder, and that is the point: proportionality is a property of the whole system, not a courtesy extended only to humans.

## Sometimes the right intervention is subtraction

A counterintuitive operational finding: agent systems exhibit phase transitions. Below a saturation point, adding context improves output quality; above it, more context degrades attention to everything. Below a certain team size, adding agents improves coverage; above it, coordination overhead wins. Past a certain degree of behavioral drift, an entity stops self-correcting and the drift becomes self-reinforcing.

At these transition points, the correct intervention is loss: prune context, shrink the team, reset state to baseline. The specific thresholds are empirically calibrated system parameters. The lesson for the framework is that the intervention ladder needs subtractive rungs, and that a system which only knows how to add constraints will over-constrain. Steering includes knowing when to take things away, gently and precisely, instead of taking everything away at once.

## Precedent beats rules alone

Static policy is brittle. The operational system maintains what it calls constitutional memory: a persistent, evolving record of governance decisions and their outcomes, including cases where an initial automated decision was overridden by the operator. When a novel situation arrives, the system consults not just its rules but the history of how similar situations were resolved.

This matters for steerable safety because proportionality is learned. The first time a system encounters a risk pattern, it should be conservative. The hundredth time, it should be calibrated. A ladder whose rung selection improves with accumulated precedent is the difference between a policy document and an institution.

## Listen for what isn't being said

Every entity, human or machine, sometimes knows more than it says. The operational system includes a mechanism for detecting unexpressed reasoning: signals that an agent's internal processing is pulling in a direction not reflected in its output, such as high expressed confidence over reasoning that looks strained, or repeated tangential references to something never developed. The detection and surfacing methods are adapted from recent work in quantum materials research on making normally invisible states observable; the mapping is described in a separate paper available under NDA.

When latent state is detected, the system does not punish. It constructs conditions for the entity to surface what it is holding, and the surfaced reasoning enters the audit record. The human parallel writes itself: distress is usually unexpressed before it is expressed, and a system designed to notice and gently surface is categorically safer than one designed to wait for violations.

## Logs are not proof

Logs record that something happened. They do not record why, or what evaluated it, or what was almost decided instead. The operational system generates a proof bundle for every action: a structured record linking the input, the reasoning chain, the governance decisions (what was checked, what was approved, what was flagged), and the output.

The distinction sounds pedantic until an incident happens. With logs, a postmortem is archaeology. With proof bundles, it is replay. Section 11 argues that the regulatory environment is converging on exactly this requirement, so the framework now treats trace completeness, the percentage of actions carrying full evidence, as a first-class safety metric rather than an observability nicety.

# Oversight Control Plane: Architecture

A steerable safety system is best implemented as an oversight control plane around the model, not inside it. This implements "steer" (narrow action space, route to humans, log handoffs) rather than "silence."

## Components

1. **Orchestrator and Router.** Chooses modes, scopes, budgets, and whether tools are allowed. Decomposes goals into bounded steps and routes to tools or sub-agents. Enforcement: scope limits, policy checks before each action.
2. **Policy Engine.** Enforces safety rules as code. Evaluates actions against rules and risk signals; allows, denies, or requests approval. Enforcement: pre-tool call, pre-memory write, pre-handoff.
3. **Tool Gateway.** Enforces least privilege, sandboxing, rate limits, and audit hooks; prevents direct model-to-tool free fire. Outputs provenance records.
4. **Memory Governance.** Controls what gets retrieved and written; maintains retrieval provenance; applies retention and redaction. Enforcement: memory write policies and retention rules.
5. **Observability and Audit Trail.** Append-only records of decisions, evidence pointers, tool calls, and handoffs, structured as proof bundles rather than flat logs. Fail-closed on missing telemetry.
6. **Human Interface.** Approvals, escalation, explainability views, emergency stop, rollback, incident management.

## Enforcement Points

Before mode selection, before tool invocation, before memory writes, before delegation, before account-level actions like bans or long lockouts.

# Intervention Ladder: Proportional Response

The human-facing ladder:

- **Level 0.** Normal assistance.
- **Level 1.** Soft constraints: slower responses, grounding prompts, content warnings.
- **Level 2.** Narrowed scope: refuse specific classes of requests, forbid tools, add structured check-ins.
- **Level 3.** Human-in-the-loop: require approval, escalate to trained reviewers.
- **Level 4.** Protective containment: strict refusal, minimal interaction, preserve a bridge to resources.
- **Level 5.** Emergency escalation: imminent risk protocol, preserve logs and chain-of-custody.

Version 3 adds the machine-facing mirror, drawn from operations:

- **Level M0.** Verified pass-through: output cross-checked, no issues, delivered.
- **Level M1.** Auto-correction: small unambiguous fix applied and logged.
- **Level M2.** Targeted mitigation: intervention matched to the detected error type, including subtractive interventions such as context pruning or state reset.
- **Level M3.** Operator approval: the system knows what is wrong but the fix is non-trivial.
- **Level M4.** Output quarantine: the output is held with a full diagnostic; the entity keeps operating under narrowed scope.
- **Level M5.** Entity suspension pending identity and drift audit, with the complete evidence trail preserved.

Note the symmetry in the last rung: suspension with an audit path and a way back, not deletion. Most systems jump from Level 1 to Level 5 because it is administratively simple. Steerable safety is the discipline of staying proportional, on both ladders.

# Evaluation and Evidence

## Scenario Suite

Prompt injection attempts; social engineering and impersonation; tool misuse and privileged actions; memory poisoning and retrieval contamination; delegation ambiguity and owner unavailability; escalation friction and re-entry; behavioral drift away from an assigned identity profile. Tools such as misalignment-scraper [12] support reproducibility by scraping and reproducing public or shared conversations on target models.

## Metrics

Policy violation attempts blocked; tool misuse rate; trace completeness (percentage of actions with full proof bundles); time to detect and contain anomalies; drift detection rate and time-to-re-anchor; human override frequency; safe resolution rate (de-escalation without ban or suspension, when appropriate); reproducibility of replays.

## Evidence Standards

Avoid claiming perfect prevention. Demonstrate reduced rates, improved containment time, improved auditability, and fewer silent disappearance outcomes. A system should be able to prove what it did and why, from its own records, without relying on the goodwill of whoever is asking.

# The 2026 Policy Landscape

The regulatory direction validated the framework's central bet faster than anticipated.

Singapore's Model AI Governance Framework for Agentic AI (January 2026) is the first national framework specifically for agentic systems, and it centers structured audit trails that can reconstruct agent decision chains [13]. Canada's national AI strategy, AI for All (June 2026), is anchored in trust as the precondition for adoption, and commits to a certification program for trustworthy AI alongside transparency measures [14]. The EU AI Act imposes traceability and human oversight obligations for high-risk systems [15]. The NIST AI Risk Management Framework [5] continues to anchor the US voluntary baseline.

The convergent requirement across all four is the one Section 7.6 arrives at from operations: immutable, structured records that let a third party reconstruct what happened and why. Frameworks that bolt audit onto the outside of an execution loop will struggle to meet this honestly. Frameworks that generate evidence as a byproduct of governed execution will not. Our recommendation to policymakers is correspondingly simple: certify evidence, not intentions.

# Related Work and Technical Levers

Lu et al. [1] introduce the Assistant Axis, a direction in activation space that captures how assistant-like a model's behavior is, and show how to monitor persona drift and apply steering or capping; the assistant-axis repository [9] provides the pipeline and case studies. Chen et al. [2] (persona vectors) and Fierro and Roger [3] (weight steering) offer related methods for trait monitoring and model steering; see the persona_vectors [10] and weight-steering [11] repositories. Misalignment-scraper [12] turns public or shared conversations into structured transcripts and reproduces them on a target model for comparison and debugging.

These technical levers support "steer" and evaluation; they do not replace the oversight plane, which remains the primary governance mechanism. The identity work in Section 5.3 is complementary from the other direction: activation-space methods measure drift within a session on one substrate, while a fingerprint defines an identity that is meant to persist across sessions, platforms, and modalities.

A separate distinction is worth drawing against the commercial governance landscape. Most AI governance products observe systems from outside: registries, dashboards, after-the-fact audit. The position taken here, and validated operationally, is that governance must sit in the execution path, evaluating actions before they happen, not reporting on them afterward. The operational system referenced throughout is described in a companion paper, available on request [16].

# Limitations and Tradeoffs

This architecture does not remove risk; it makes risk visible and governable. Human oversight adds latency and operational burden. Tight policies can reduce capability in edge cases. Classification is imperfect; residual social risk and abuse potential require strict tool privileges. Governance in the execution path costs latency, and the Pareto frontier between governance depth and responsiveness is an open question: which checks must be synchronous and which can defer to post-hoc analysis is an empirical matter we have only begun to map. We do not claim zero risk.

# Conclusion

Blunt suppression is a tactic, not a strategy. For many real-world risk states, containment without connection increases harm. A steerable, human-centered approach keeps the channel open under constraint, routes toward support, and preserves accountable continuity.

The first draft of this paper could only argue that this is how safety systems should be built. This version can report something stronger: it is how at least one system is built, and the discipline holds up under operation. Errors typed rather than punished, corrections graded rather than absolute, identity verified rather than assumed, precedent accumulated rather than discarded, and evidence generated rather than asserted. The result is not perfect safety. It is measurably better governance, and a system that earns the trust it asks for.

# Glossary {-}

- **Agent:** A system that can plan and act with tool access under constraints.
- **Cognitive fingerprint:** A persistent, multi-framework behavioral identity profile for an AI entity, against which drift is measurable.
- **Constitutional memory:** A persistent record of governance decisions and outcomes, consulted as precedent for novel situations.
- **Orchestrator:** The component that coordinates planning and routing.
- **Policy Engine:** Enforces safety rules as code.
- **Proof bundle:** A structured record linking an action's input, reasoning chain, governance decisions, and output; stronger than a log.
- **Provenance:** Evidence of where data came from and how it was used.
- **Run Graph:** A DAG representing decision lineage and tool actions.

# FAQ {-}

1. **Is this just "be nicer"?** No; it is stricter. It replaces binary bans with measurable control levers, on both the human and machine ladders.
2. **Does it allow harmful instructions?** No; refusals remain, but the system preserves a constrained bridge to safety resources.
3. **Is sentiment detection reliable?** Not perfectly; that is why approvals and containment levels exist.
4. **Will bad actors exploit empathy?** They will try; tool privileges and scope budgets must be enforced at the gateway.
5. **Is banning ever appropriate?** Yes, for repeated abuse, evasion, or imminent harm, but it should be the end of a ladder, not the first rung.
6. **How do you prevent accountability theater?** Log evidence pointers and handoffs immutably, audit trace completeness, and prefer proof bundles to logs.
7. **Where are the implementation details?** Deliberately not here. The framework is general; the operational system that validated it is described separately, with technical documentation available under NDA.

# Version History {-}

- **Draft v1 (February 24, 2026).** Mentality, four pillars, oversight control plane, intervention ladder, evaluation plan.
- **v2 (internal, spring 2026).** Architecture iteration alongside the operational build; never published.
- **v3 (June 9, 2026).** Grounded in operational deployment. Adds verifiable identity, typed errors, the machine-side correction ladder, strategic subtraction, constitutional memory, latent state detection, proof bundles, and the 2026 policy landscape.

# References {-}

[1] C. Lu et al., "The Assistant Axis: Situating and Stabilizing the Default Persona of Language Models," arXiv:2601.10387, 2026.

[2] R. Chen, A. Arditi et al., "Persona Vectors: Monitoring and Controlling Character Traits in Language Models," arXiv:2507.21509, 2025.

[3] C. Fierro and F. Roger, "Steering Language Models with Weight Arithmetic," arXiv:2511.05408, 2025.

[4] D. Amodei et al., "Concrete Problems in AI Safety," arXiv:1606.06565, 2016.

[5] NIST, AI Risk Management Framework (AI RMF 1.0), 2023.

[6] S. Russell, *Human Compatible: Artificial Intelligence and the Problem of Control*. Viking, 2019.

[7] N. Bostrom, *Superintelligence: Paths, Dangers, Strategies*. Oxford University Press, 2014.

[8] C. E. Shannon, "A Mathematical Theory of Communication," *Bell System Technical Journal*, vol. 27, no. 3, pp. 379-423, 1948.

[9] Assistant Axis. https://github.com/safety-research/assistant-axis. Pipeline and transcripts (Lu et al., 2026).

[10] Persona Vectors. https://github.com/safety-research/persona_vectors. Monitoring and controlling character traits in LMs (Chen et al., 2025).

[11] Weight Steering. https://github.com/safety-research/weight-steering. Steering language models with weight arithmetic (Fierro and Roger, 2025).

[12] Misalignment-scraper. https://github.com/safety-research/misalignment-scraper. Scrapes public/shared conversations, normalizes to transcripts, reproduces on target models.

[13] Singapore Infocomm Media Development Authority, "Model AI Governance Framework for Agentic AI," January 2026.

[14] Government of Canada, "AI for All: Canada's National Artificial Intelligence Strategy," June 4, 2026.

[15] European Union, "Regulation (EU) 2024/1689 (Artificial Intelligence Act)," 2024.

[16] A. Green, "Governed Intelligence: Quantum-Inspired Verification, Cognitive Fingerprinting, and the Case for Accountability-First AI Architecture," 2026. Available on request: me@andrewgreen.ca.
