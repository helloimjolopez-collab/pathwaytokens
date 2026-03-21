# SideNav — Pathway Design System Component Spec

> **Purpose of this document:** Provide a complete, implementation-ready reference for the SideNav component. If you have access to the Figma file (`3sw45aVcngFAmpbP6cfrXP`) and its variable definitions, this document plus those tokens is sufficient to build a pixel-accurate implementation.

---

## 1. Component Overview

The `SideNav` is the primary navigation shell of the Pathway product. It sits on the left edge of the viewport, contains a vertical list of navigation items, and supports two layout states: **expanded** (250px wide, labels visible) and **collapsed** (64px wide, icons only).

### Figma source
- **File:** `3sw45aVcngFAmpbP6cfrXP` — Pathway Design System Master File MB 2.0
- **SideNav component page:** node `40003951:2927`
- **Real accounting example:** node `40004790:47259`

---

## 2. Component Anatomy

```
SideNav.Container
└── SideNavMenu
│   ├── SideNavItem (Level 0 — Destination)
│   ├── SideNavItem (Level 0 — Grouper, expanded)
│   │   ├── SideNavItem (Level 1 — child Destination)
│   │   └── SideNavItem (Level 1 — child Destination)
│   └── SideNavItem (Level 0 — Destination)
└── Collapse_Expand_Nav_Container
    ├── Divider
    └── Collapse (SideNavItem-like row, no indicator stripe)
```

### SideNavItem internal structure

**Level 0:**
```
[container.indicator 4px] [Container.rowStart px-8]
  [Container.Main]
    [Container.LeadingIcon 24×24] → [Icon.Leading 14×14]
    [text.label px-6]
  [Container.RowEnd 40×24]       ← groupers only
    [Container.RowEnd.Icon 24×24]
      [chevron 10pt]
```

**Level 1 (child):**
```
[container.indicator 4px] [child.container]
  [Container.rowStart px-8]
    [container.main pl-24]
      [text.label]
```
> **Annotation from Figma:** "Children are always a destination and never a grouper — only 2 levels of depth are allowed."

---

## 3. Design Tokens

### 3.1 Surface

| Semantic Token | Primitive | Resolved Value | Usage |
|---|---|---|---|
| `Surface/Nav/Light` | — | `#fafafa` | SideNav container background |
| *(canvas surface — see §8.1)* | — | `#fafafa` | Page/viewport background |

> **⚠ Gap:** The canvas/page background token name has not been confirmed from the Figma variable set queried. It shares the same hex as `Surface/Nav/Light`.

### 3.2 Fill (NavItem states)

| Semantic Token | Primitive | Resolved Value | Used In |
|---|---|---|---|
| `Fill/Contextual/NavItem/Base` | — | `#fafafa` | Resting item fill |
| `Fill/Contextual/NavItem/Hover` | — | `rgba(17,17,17,0.04)` | Hover fill |
| `Fill/Contextual/NavItem/Active` | — | `rgba(53,85,160,0.08)` | Active destination + collapsed-trail grouper |
| `Fill/Contextual/NavItem/Trail` | — | `rgba(17,17,17,0.04)` | Expanded grouper (distinct token from Hover — do not merge) |
| `Fill/Static/Info/Subtle` | — | `#edf0f9` | Divider (`h-[1px]`) + nav container `border-right` |

> **Note:** `Fill/Contextual/NavItem/Trail` and `Fill/Contextual/NavItem/Hover` resolve to the same hex today. They must remain **separate tokens** because they have distinct semantic meaning and may diverge in a future design update.

> **⚠ Gap:** Primitive token names are not surfaced by `get_variable_defs` — the tool resolves alias chains to final hex only. The full `Semantic → Primitive → Hex` chain requires the Figma REST API or a dedicated token documentation frame.

### 3.3 Text (NavItem states)

| Semantic Token | Primitive | Resolved Value | Used In |
|---|---|---|---|
| `Text/Contextual/NavItem/Base` | — | `#4b4b4b` | Label default |
| `Text/Contextual/NavItem/Hover` | — | `#363636` | Label hover |
| `Text/Contextual/NavItem/Active` | — | `#02060d` | Active destination **and** all trail states |

> Trail text color = `Text/Contextual/NavItem/Active`. This applies to both **expanded** trail (grouper showing children) and **collapsed** trail (grouper with hidden active child). Do not use `Text/Contextual/NavItem/Base` for trail.

### 3.4 Icon (NavItem states)

| Semantic Token | Primitive | Resolved Value | Used In |
|---|---|---|---|
| `Icon/Contextual/NavItem/Base` | — | `#606060` | Icon default + expanded-trail icon |
| `Icon/Contextual/NavItem/Hover` | — | `#3b3b3b` | Icon hover |
| `Icon/Contextual/NavItem/Active` | — | `#3555a0` | Active icon + collapsed-trail icon + `indicator.stripe` color |

> `Icon/Contextual/NavItem/Active` (`#3555a0`) is used for **three things simultaneously**: the leading icon, the indicator stripe, and the collapsed-trail icon. They share the same token.

> Expanded trail icon = `Icon/Contextual/NavItem/Base` (`#606060`). Do not use active blue for expanded trail icons.

### 3.5 Geometry

| Semantic Token | Primitive | Resolved Value | Usage |
|---|---|---|---|
| `Component/NavItem/Large/Radius/Radius` | `Border/S` | `8px` | Item `border-radius` |
| `Accessibility/Touch Target/Optimal/Size` | — | `48px` | Item `min-height` |
| `Accessibility/Icon Wrapping/Large/Size` | — | `24×24px` | `Container.LeadingIcon` dimensions |

### 3.6 Typography

All `SideNavItem` labels at all levels use **the same** text style. There is no size variation between Level 0 and Level 1 items.

#### Semantic token: `Label/Menu/L/Medium`

> **Note on naming:** The Figma variable set abbreviates the size tier as `L` (not `Large`). The full canonical token name is `Label/Menu/L/Medium`.

| Property | CSS Variable (from Figma code output) | Resolved Value |
|---|---|---|
| Font family | `--label/menu/l/medium/fontfamily` | `'Red Hat Text', sans-serif` |
| Font weight | `--label/menu/l/medium/fontweight` | `500` (Medium) |
| Font size | `--label/menu/l/medium/fontsize` | `16px` |
| Line height | `--label/menu/l/medium/lineheight` | `22px` |
| Letter spacing | `--label/menu/l/medium/letterspacing` | `0px` |

#### Implementation (CSS)

```css
/* Using CSS custom properties */
.sidenav-label {
  font-family: var(--label/menu/l/medium/fontfamily, 'Red Hat Text', sans-serif);
  font-weight: var(--label/menu/l/medium/fontweight, 500);
  font-size: var(--label/menu/l/medium/fontsize, 16px);
  line-height: var(--label/menu/l/medium/lineheight, 22px);
  letter-spacing: var(--label/menu/l/medium/letterspacing, 0px);
}

/* Hard-coded fallback (no token system) */
.sidenav-label {
  font-family: 'Red Hat Text', sans-serif;
  font-weight: 500;
  font-size: 16px;
  line-height: 22px;
  letter-spacing: 0px;
}
```

> **Google Font:** `Red Hat Text` must be loaded via `@import url('https://fonts.googleapis.com/css2?family=Red+Hat+Text:wght@400;500;600&display=swap')` or equivalent if not already provided by the app shell.

> **No font-size variation** between Level 0 and Level 1 items. The visual hierarchy of child items is achieved solely through the `pl-[24px]` left-indent and the absence of a leading icon — not via smaller text.

---

## 4. Layout & Spacing

> **⚠ Gap:** The values in this section appear as raw Tailwind utility classes in Figma (`px-[12px]`, `gap-[8px]`, etc.) with **no named spacing/layout tokens**. This is a documentation gap in the design system. Recommend creating spacing tokens for these values so implementations can reference them semantically.

| Value | Figma class | px | Semantic token |
|---|---|---|---|
| Nav container horizontal padding | `px-[12px]` | 12 | **None** |
| Nav container vertical padding | `py-[14px]` | 14 | **None** |
| SideNav expanded width | — | 250 | **None** |
| SideNav collapsed width | — | 64 | **None** |
| Gap between nav items | `gap-[8px]` | 8 | **None** |
| SideNavMenu bottom padding | `pb-[24px]` | 24 | **None** |
| `Container.rowStart` horizontal padding | `px-[8px]` | 8 | **None** |
| `text.label` horizontal padding | `px-[6px]` | 6 | **None** |
| Level 1 `container.main` left indent | `pl-[24px]` | 24 | **None** |
| `indicator.stripe` width | — | 4 | **None** |
| `indicator.stripe` border-radius (right only) | — | `0 8px 8px 0` | Assumed `Border/S` — **unconfirmed** |
| Collapse row left padding | `pl-[12px]` | 12 | **None** |
| Collapse row right padding | `pr-[8px]` | 8 | **None** |
| `Collapse_Expand_Nav_Container` top padding / gap | `pt-[4px]` `gap-[4px]` | 4 | **None** |
| Icon.Leading inner size | — | 14 | **None** — `Accessibility/Icon Wrapping/Large` covers 24px wrapper only |
| `Container.RowEnd` dimensions | — | 40×24px | **None** |
| `Container.RowEnd.Icon` dimensions | — | 24×24px | `Accessibility/Icon Wrapping/Large` |
| Chevron icon size | — | 10pt | **None** |

---

## 5. Item Variants

### Level 0 — Destination
- Has `Container.LeadingIcon` (24×24) with `Icon.Leading` (14pt fill-style icon)
- Has `Container.RowEnd` (40×24) — **empty** for destinations (no chevron)
- Interacts: click → sets active state

### Level 0 — Grouper
- Has `Container.LeadingIcon` (24×24) with `Icon.Leading` (14pt fill-style icon)
- Has `Container.RowEnd` (40×24) — **contains chevron** (10pt)
- Chevron direction: **▼ down** when collapsed, **▲ up** when expanded
- Interacts: click → toggles expand/collapse (does not navigate)

### Level 1 — Child (always Destination)
- Uses `child.container` wrapper
- **No** `Container.LeadingIcon`, **no** icon of any kind
- `container.main` has `pl-[24px]` left indent to create visual hierarchy
- Same font (`Label/Menu/Large/Medium`) as Level 0
- Always a destination, never a grouper
- Only 2 levels of depth allowed

---

## 6. State Matrix

| Condition | Fill token | Text token | Icon token | `indicator.stripe` |
|---|---|---|---|---|
| **Base** | `NavItem/Base` | `NavItem/Base` | `NavItem/Base` | hidden |
| **Hover** | `NavItem/Hover` | `NavItem/Hover` | `NavItem/Hover` | hidden |
| **Active** (destination) | `NavItem/Active` | `NavItem/Active` | `NavItem/Active` | **visible** |
| **Trail — expanded** (grouper is open) | `NavItem/Trail` | `NavItem/Active` | `NavItem/Base` | hidden |
| **Trail — collapsed** (grouper closed, child is active) | `NavItem/Active` | `NavItem/Active` | `NavItem/Active` | **visible** |

### State logic rules

1. **Any expanded grouper** (children are visible) → Trail-expanded state. This applies regardless of whether a child item is currently active.
2. **Collapsed grouper with active child** (children hidden because grouper is closed, OR sidebar is fully collapsed) → Trail-collapsed state. Visually identical to Active state — same fill, same icon color, same stripe.
3. When the sidebar collapses, any grouper that was in expanded-trail automatically transitions to collapsed-trail if it has an active child.
4. `indicator.stripe` is only visible in **Active** and **Trail-collapsed** states.
5. `indicator.stripe` color = `Icon/Contextual/NavItem/Active` (`#3555a0`) — same token as icon active.

---

## 7. `indicator.stripe` Sub-component

```
container.indicator (structural, 4px wide, full item height)
└── indicator.stripe (visible stripe)
    border-radius: 0 8px 8px 0   ← rounded on right only
    width: 4px
    color: var(--icon/contextual/navitem/active, #3555a0)
    padding: 4px 0  (top/bottom inset within container)
```

The `container.indicator` column is **always present** on every `SideNavItem` (Level 0 and Level 1). It is a structural 4px spacer. The `indicator.stripe` inside it is only visually painted when the item is in Active or Trail-collapsed state.

---

## 8. SideNav Container

### 8.1 Surface
- Background: `Surface/Nav/Light` → `#fafafa`
- Right border: `1px solid` `Fill/Static/Info/Subtle` → `#edf0f9`

### 8.2 Dimensions & Padding
```
Expanded:  width 250px, padding 14px 12px
Collapsed: width  64px, padding 14px 12px (same, text hidden)
```
> No semantic tokens for width or padding — see §4 for gap documentation.

### 8.3 Transition
```
width: transition 0.25s cubic-bezier(0.4, 0, 0.2, 1)
```

---

## 9. Collapse_Expand_Nav_Container

Sits at the **bottom of the scroll flow** — it scrolls with the nav items, it is not sticky/fixed.

```
Collapse_Expand_Nav_Container
├── Divider
│   height: 1px
│   background: Fill/Static/Info/Subtle (#edf0f9)
└── Collapse row
    container.rowStart: pl-[12px] pr-[8px]   ← note: different padding from SideNavItem
    └── container.main
        ├── Icon wrapper 24×24: collapse_nav icon (18pt)
        └── text.label px-[6px]: "Collapse"
    container.rowEnd: empty (no chevron)
```

**Key difference from `SideNavItem`:** The Collapse row does **not** have a `container.indicator` / `indicator.stripe` column. It also uses `pl-[12px]` instead of the item's `px-[8px]`.

When sidebar is collapsed: show `expand_nav` icon, hide label.
When sidebar is expanded: show `collapse_nav` icon, show "Collapse" label.

Icons are fill-style from the design system (`collapse_nav`, `expand_nav`), not generic chevrons.

---

## 10. Sidebar Collapsed State

When `isSidebarCollapsed = true`:
- Nav width: 64px
- All labels hidden
- `Container.RowEnd` (chevrons) hidden
- Level 1 children hidden (groupers act like icon-only destinations)
- Hovering a grouper shows a **flyout popover** with the group label and all children
- Grouper in trail-collapsed state: `Container.LeadingIcon` icon shows in `Icon/Contextual/NavItem/Active` (`#3555a0`) with active fill and stripe

> **⚠ Gap:** The `SideNavItem.Collapsed` Figma variants were partially inaccessible during implementation. The exact spacing of collapsed items needs further verification in Figma.

---

## 11. Iconography

- All leading icons are **fill-style** (solid/filled, not outline)
- Icons live at `14×14pt` inside a `24×24pt` `Container.LeadingIcon` wrapper
- Icon source: design system iconography page (node `40002909:32275` in file `3sw45aVcngFAmpbP6cfrXP`)
- **Figma CDN asset URLs cannot be used directly in browsers** — they require auth headers that only the Figma MCP server provides. Implementations must either use the design system icon component library or embed SVG assets at build time.

### Accounting SideNav icon mapping

| Nav Item | Icon name | Grouper |
|---|---|---|
| Applications | `apps` | ✓ |
| Enter | `add_doc` | — |
| Manage | `tune` (Vector) | — |
| View | `view` (eye Vector) | ✓ |
| Reports | `reports` | — |
| Modify | `table_edit` | ✓ |
| Help | `help` (Vector) | — |

---

## 12. Interaction Patterns

| Trigger | Behavior |
|---|---|
| Click destination (L0 or L1) | Set that item as active |
| Click grouper (expanded sidebar) | Toggle expand/collapse |
| Click grouper (collapsed sidebar) | No expand — show flyout popover instead |
| Hover any item | Hover fill + hover text + hover icon |
| Hover grouper in collapsed sidebar | Show flyout popover with group label + children |
| Click Collapse button | Sidebar width transition to 64px |
| Click Expand button | Sidebar width transition to 250px |

---

## 13. Accessibility

> **Legend used in this section:**
> - ✅ **Implemented** — present in the current reference demo (`SideNav.html`)
> - 📋 **Required by WCAG / ARIA** — standard spec for this pattern, not yet fully verified in Figma annotations or the demo
> - ❓ **Unconfirmed** — not yet validated; Figma does not supply an accessibility annotation for this

### 13.1 Touch & Pointer Targets

| Token | Value | Source |
|---|---|---|
| `Accessibility/Touch Target/Optimal/Size` | `48px` | Figma ✅ |
| `Accessibility/Icon Wrapping/Large/Size` | `24×24px` | Figma ✅ |

Both values come from named Figma tokens. `min-height: 48px` on every `SideNavItem` satisfies WCAG 2.5.5 Target Size.

### 13.2 HTML Semantics

| Element | Recommendation | Status |
|---|---|---|
| Outer nav container | `<nav aria-label="Main navigation">` | ✅ Implemented |
| Level 0 and Level 1 interactive items | `role="button"` + `tabIndex="0"` (or native `<button>`) | ✅ Implemented |
| Grouper items | `aria-expanded="true|false"` | ✅ Implemented |
| Active destination | `aria-current="page"` | ✅ Implemented |
| Children list (expanded grouper) | `role="group"` or `role="list"` wrapping Level 1 items | ❓ Not in demo — Figma does not annotate this |
| Collapse/expand button | `aria-label="Collapse navigation"` / `"Expand navigation"` | 📋 Recommended — Figma does not annotate |

> **Note on `<button>` vs `role="button"`:** Using a native `<button>` element is preferred over `role="button"` because it inherits keyboard behaviour and focus styling for free. The current demo uses `<div role="button" tabIndex={0}>` which requires explicit keyboard handlers and focus styles. A production implementation should use `<button>` with `type="button"`.

### 13.3 Keyboard Interaction

The following patterns are standard for navigation menus (ARIA authoring practices):

| Key | Behaviour | Status |
|---|---|---|
| `Tab` | Move focus forward through interactive items | ✅ Works (browser default via `tabIndex=0`) |
| `Shift+Tab` | Move focus backward | ✅ Works (browser default) |
| `Enter` | Activate focused item (navigate or toggle grouper) | ✅ Implemented |
| `Space` | Same as Enter for `role="button"` items | 📋 Not in demo — should be added |
| `Escape` | Close expanded grouper if one is open | 📋 Not in demo — recommended |
| Arrow keys (`↑` / `↓`) | Move between items within the nav | 📋 Not in demo — required for `role="menu"` pattern; optional for `role="navigation"` |

> **Which ARIA pattern applies?** The SideNav uses `<nav>` (landmark), not `role="menu"`. The `role="menu"` / `role="menuitem"` pattern requires arrow key navigation. The `<nav>` + `role="button"` pattern (used here) only requires `Tab` and `Enter`, which are already implemented. If the team wants to adopt the menu pattern, arrow key support becomes mandatory. This decision should be made explicitly and documented in Figma.

### 13.4 Focus Styles

| Requirement | Status |
|---|---|
| Visible focus ring on all interactive items | ❓ Not styled in demo — browser default outline only |
| Focus ring must not be suppressed (`outline: none` without replacement) | 📋 Required — WCAG 2.4.11 |
| Focus ring color should meet 3:1 contrast against adjacent colours | 📋 Suggested color: `Icon/Contextual/NavItem/Active` (#3555a0) — ❓ contrast not verified |

> Figma does not contain a "focused" variant in the `SideNavItem` component variants as observed via MCP. This is a documentation gap (see §15). Until a Figma focus spec exists, use the browser default outline or apply a `2px solid #3555a0` outline with `outline-offset: 2px` on `:focus-visible`.

### 13.5 Screen Reader Experience

| Concern | Recommendation | Status |
|---|---|---|
| Grouper label includes state | `aria-expanded` communicates open/close — ensure SR announces it | ✅ `aria-expanded` present |
| Active page communicated | `aria-current="page"` on the active item | ✅ Implemented |
| Icon-only collapsed sidebar | When collapsed (64px), items have no visible label — tooltips or `aria-label` on items needed | 📋 Not implemented — should add `title` or a tooltip |
| Grouper children visibility | When grouper is collapsed, children should be `aria-hidden="true"` or removed from DOM | 📋 Demo removes from DOM (conditional render) — correct approach |
| Collapse/Expand button | Should announce its action: `aria-label="Collapse navigation"` / `"Expand navigation"` | 📋 Not in demo |

### 13.6 Colour Contrast

All colour decisions below use token resolved values. Contrast ratios are approximate and should be verified with a tool (e.g. Colour Contrast Analyser).

| State | Text | Background | Approximate ratio | WCAG AA (4.5:1) |
|---|---|---|---|---|
| Base | `#4b4b4b` on `#fafafa` | Text on surface | ~6.3:1 | ✅ Pass |
| Hover | `#363636` on `rgba(17,17,17,0.04)` ≈ `#f5f5f5` | ~9.3:1 | ✅ Pass |
| Active | `#02060d` on `rgba(53,85,160,0.08)` ≈ `#eef1f8` | ~19:1 | ✅ Pass |
| Trail (expanded) | `#02060d` on `rgba(17,17,17,0.04)` ≈ `#f5f5f5` | ~19:1 | ✅ Pass |
| indicator.stripe | `#3555a0` on `#fafafa` | 3px stripe non-text | ✅ 3:1 for non-text (WCAG 1.4.11) |

> ⚠ These ratios are approximations. The alpha-based fill tokens (`rgba(...)`) mean the actual contrast depends on what's behind the item. On the `#fafafa` nav surface the calculations above hold. On other backgrounds they may differ.

### 13.7 Figma Accessibility Gaps

The following accessibility specifications are **absent from the Figma component** as observed via MCP:
- No "focused" state variant in `SideNavItem` component
- No focus ring colour or style annotation
- No `aria-label` annotation on the Collapse/Expand button
- No keyboard interaction annotation in component notes
- No tooltip/label specification for collapsed (icon-only) sidebar items

These should be added to the Figma component as design-time annotations before a production implementation is finalised.

---

## 14. What to Pass Claude to Implement This Component

To implement SideNav from scratch with correct design system alignment, provide:

1. **This document**
2. **Figma variable export** for file `3sw45aVcngFAmpbP6cfrXP` — specifically the token values for `Fill/Contextual/NavItem/*`, `Text/Contextual/NavItem/*`, `Icon/Contextual/NavItem/*`, `Surface/Nav/Light`, `Fill/Static/Info/Subtle`, and `Component/NavItem/Large/Radius/Radius`
3. **Icon assets** — either the design system icon React component library, or SVG files for the fill-style icons embedded at build time
4. **Specific nav content** — the nav items, their labels, icon names, and which are groupers vs destinations

---

## 15. Figma Gaps — Blocks to Full Token-Driven Implementation

The following are gaps in the current Figma documentation that prevent a fully semantic implementation:

### 15.1 Missing spacing/layout tokens (HIGH priority)
No named tokens exist for: nav container padding (12px H / 14px V), item gap (8px), stripe width (4px), row padding (8px), child indent (24px), collapse row padding, nav width (250px / 64px), or `Container.RowEnd` dimensions. These are raw Tailwind values. **Recommend creating a spacing scale** and referencing it with semantic names like `Spacing/Nav/ContainerPaddingH`.

### 15.2 Primitive token names not surfaced (MEDIUM priority)
`get_variable_defs` (Figma MCP tool) resolves semantic token alias chains to their final hex value but does not expose intermediate primitive token names. The full chain `Semantic → Primitive → Hex` cannot be reconstructed from MCP alone. This blocks documentation of the full token lineage. **Recommend:** either expose primitives in a dedicated Figma frame/page, or use the Figma REST API (`GET /v1/files/:key/variables`) which does return the full alias chain.

### 15.3 Canvas surface token name unconfirmed (LOW priority)
The page/viewport background is `#fafafa` (same as `Surface/Nav/Light`). The semantic token name for the canvas surface has not been retrieved from Figma. This should be confirmed and documented.

### 15.4 Icon inner size token missing (LOW priority)
`Icon.Leading` inside `Container.LeadingIcon` renders at `14×14pt`. `Accessibility/Icon Wrapping/Large` documents the `24px` wrapper but there is no token for the inner icon size. Recommend `Accessibility/Icon/Leading/Size` or similar.

### 15.5 indicator.stripe border-radius unconfirmed (LOW priority)
The stripe uses `border-radius: 0 8px 8px 0` (rounded right only). The `8px` is assumed to match `Border/S` (same as the item radius token) but has not been explicitly confirmed in Figma.

### 15.6 Collapsed sidebar item layout unconfirmed (MEDIUM priority)
`SideNavItem.Collapsed` variants were partially inaccessible via MCP during implementation. The exact icon centering, spacing, and state behavior of collapsed items needs explicit Figma documentation.

### 15.7 Grouper collapsed with no active child — state unconfirmed (LOW priority)
The state matrix above specifies that a collapsed grouper with **no** active child shows in Base state. This should be explicitly documented in the Figma component annotations to avoid ambiguity.
