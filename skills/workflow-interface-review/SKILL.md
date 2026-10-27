---
name: workflow-interface-review
description: Review changed web interfaces for usability, accessibility, states, performance and responsive behavior using bundled Web Interface Guidelines. Use for a focused UI review or release review; report actionable evidence and preserve the approved design.
license: MIT
---

# Interface review adapter

Read the [preserved Web Interface Guidelines](references/upstream.md), from Vercel Labs under its [MIT license](LICENSE.txt), reviewed 27 October 2026. This [MIT-licensed adapter](ADAPTER_LICENSE.txt) uses a pinned snapshot that works offline. When current rules or a changing standard matter, verify the official source and name the version/date actually used.

Inspect the affected code and rendered interface, then relevant neighboring states and interactions. Follow the user's requested review scope. A review request authorizes findings; implement fixes only when the task also authorizes them. When invoked during an authorized implementation, fix in-scope defects and recheck them.

Apply the source in context:

- Treat semantic controls, accessible names, keyboard/focus behavior, contrast, reflow, clear validation and recovery as functional requirements. Native buttons and links already provide keyboard behavior; do not duplicate it with custom handlers.
- Preserve useful autocomplete tokens and input-purpose semantics for personal data. Do not blanket-disable autofill. Preserve user zoom, text selection and platform navigation.
- Treat typography/capitalization preferences, list-size thresholds and suggested libraries as heuristics. Respect the approved DESIGN.md and measure before adding dependencies or virtualization.
- Check realistic long/empty/error/loading/success content, responsive reading order, overflow, touch targets, themes and reduced-motion behavior when relevant. Check security-sensitive data and permissions through the actual boundary when changed.
- Distinguish code findings, automated scans, browser observations and assistive-technology/device evidence. Do not infer conformance or a passing interaction from a scan or screenshot alone.

Report actionable findings in priority order with file/element, observed failure, user impact and a concrete fix. Separate demonstrated defects from optional suggestions. State what was checked and what remains Not run or Blocked with its owner. If no actionable issue was found, say so with the scope and limits.
