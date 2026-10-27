---
name: workflow-mobile-web
description: Improve or verify mobile web behavior within the web-development workflow, including touch, viewport height, safe areas, keyboards, scrolling and PWA details. Use for actual phone-facing issues; preserve native browser behavior and require device evidence for device-specific claims.
license: MIT
---

# Mobile web adapter

Read the relevant sections of the [preserved Mobile Native guidance](references/upstream.md), from Emil Kowalski under its [MIT license](LICENSE.txt), reviewed 27 October 2026. This adapter is also [MIT-licensed](ADAPTER_LICENSE.txt). Apply the source to the actual task using these rules:

1. Inspect the symptom, intended devices/browsers, current layout and primary journey. Start the authorized task directly; a greeting convention does not require waiting when the task is already clear.
2. Apply only relevant viewport, safe-area, touch, focus, keyboard, scroll or PWA fixes. Preserve user zoom, selectable reading content, browser back/forward gestures and useful pull-to-refresh unless the particular interaction requires a scoped override. Do not copy every example as a global stylesheet.
3. Scope gesture ownership and overscroll rules to the component that needs them. Preserve vertical page scrolling and pinch zoom where appropriate. If removing a tap highlight, keep equivalent visible press/focus feedback. Do not globally disable selection to make an ordinary page feel like an app.
4. Keep normal document navigation and semantic controls. Handle virtual keyboards, long content, orientation and short screens where relevant. Use existing dependencies; do not introduce a PWA, gesture library or app-like shell without a product need.
5. Verify the affected journey in a browser and on representative actual hardware for device-specific behavior. Viewport emulation cannot prove virtual-keyboard behavior, Safari gestures or real touch performance. If hardware is unavailable, record those checks as Not run/Blocked with exact manual steps and the evidence owner.

Report the symptom fixed, scope, browser/emulated checks, actual-device checks and remaining limits separately. Use a motion specialist only for a concrete animation need.
