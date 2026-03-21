# SideNav — Pathway Design System Component Spec

> **Purpose of this document:** Provide a complete, implementation-ready reference for the SideNav component. If you have access to the Figma file (`3sw45aVcngFAmpbP6cfrXP`) and its variable definitions, this document plus those tokens is sufficient to build a pixel-accurate implementation.

---

## 1. Component Overview

The `SideNav` is the primary navigation shell of the Pathway product. It sits on the left edge of the viewport, contains a vertical list of navigation items, and supports two layout states: **expanded** (250px wide, labels visible) and **collapsed** (64px wide, icons only).

### Figma source
- **File:** [Pathway Design System Master File MB 2.0](https://www.figma.com/design/3sw45aVcngFAmpbP6cfrXP/)
- **SideNav component:** [Open in Figma](https://www.figma.com/design/3sw45aVcngFAmpbP6cfrXP/?node-id=40003951-2927)

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
> - 📋 **Required for production** — standard spec for this pattern, not yet in the demo
> - ❓ **Unconfirmed** — not yet validated; Figma does not supply an annotation for this

---

### 13.0 ARIA Pattern

The SideNav uses the **ARIA Tree View pattern** (`role="tree"`). The component has two levels of hierarchy — expandable Level 0 groupers with Level 1 child destinations — which maps directly to the [WAI-ARIA treeview specification](https://www.w3.org/WAI/ARIA/apg/patterns/treeview/).

The entire nav is a single Tab stop. Arrow keys navigate within it (see §13.3). This is the correct pattern for a hierarchical, expandable navigation structure of this kind.

Do not use `role="menu"` / `role="menuitem"` — that is for application context-menus, not site navigation, and screen readers will announce it incorrectly.

> **Note on the reference demo (`SideNav.html`):** The demo currently uses `<nav>` with `role="button"` divs as a visual scaffolding baseline. This is not a production-ready implementation. Production code requires native `<button>` / `<a>` elements, roving-tabindex focus management, and the full arrow key handlers documented in §13.3.

---

### 13.1 Touch & Pointer Targets

| Token | Value | Source |
|---|---|---|
| `Accessibility/Touch Target/Optimal/Size` | `48px` | Figma ✅ |
| `Accessibility/Icon Wrapping/Large/Size` | `24×24px` | Figma ✅ |

Both values come from named Figma tokens. `min-height: 48px` on every `SideNavItem` satisfies WCAG 2.5.5 Target Size.

---

### 13.2 ARIA Markup

```html
<nav aria-label="Main navigation">

  <ul role="tree" aria-label="Main navigation">

    <!-- Level 0 — Destination (no children) -->
    <li role="treeitem" tabindex="-1" aria-current="page">
      <!-- aria-current="page" on the active item only -->
      Reports
    </li>

    <!-- Level 0 — Grouper (has children) -->
    <li role="treeitem" tabindex="-1" aria-expanded="true">
      Applications
      <ul role="group">
        <li role="treeitem" tabindex="-1">Child Item A</li>
        <li role="treeitem" tabindex="-1">Child Item B</li>
      </ul>
    </li>

    <!-- Level 0 — Grouper (collapsed) -->
    <li role="treeitem" tabindex="-1" aria-expanded="false">
      Modify
      <!-- ul[role="group"] not rendered (or aria-hidden="true") when collapsed -->
    </li>

  </ul>

</nav>

<!-- Collapse/Expand control — outside the tree, separate button -->
<button type="button" aria-label="Collapse navigation">
  <!-- collapse_nav icon -->
</button>
```

**Key rules:**
- The `<ul role="tree">` contains the first level of items only. Children sit inside `<ul role="group">` nested within their parent `<li role="treeitem">`.
- Only **one** `treeitem` should have `tabindex="0"` at a time (the currently focused item). All others use `tabindex="-1"`. This is roving-tabindex focus management.
- `aria-expanded` is only valid on grouper treeitems — omit it entirely from leaf (destination) items.
- `aria-current="page"` goes on the active destination `treeitem` only.
- The Collapse/Expand button sits **outside** the tree — it is a separate `<button>`, not a `treeitem`.

---

### 13.3 Keyboard Interaction

The entire nav is a single Tab stop. Arrow keys navigate within it.

| Key | Behaviour | Status |
|---|---|---|
| `Tab` | Moves focus **into** the tree (to the roving focus item) — or **out** of the tree to the next focusable element on the page | 📋 Requires roving-tabindex implementation |
| `Shift+Tab` | Moves focus out of the tree backward | 📋 Requires roving-tabindex implementation |
| `↓` (Down Arrow) | Moves focus to the **next visible treeitem** (skips hidden children of collapsed groupers) | 📋 Not in demo |
| `↑` (Up Arrow) | Moves focus to the **previous visible treeitem** | 📋 Not in demo |
| `→` (Right Arrow) | On a **collapsed grouper**: expands it. On an **expanded grouper**: moves focus to its first child. On a leaf item: no action. | 📋 Not in demo |
| `←` (Left Arrow) | On an **expanded grouper**: collapses it. On a **child item (Level 1)**: moves focus to its parent grouper. On a Level 0 leaf: no action. | 📋 Not in demo |
| `Enter` | Activates the focused item: navigates (destination) or toggles expand/collapse (grouper) | ✅ Implemented (via click handler) |
| `Space` | Same as Enter for treeitems | 📋 Not in demo |
| `Home` | Moves focus to the first treeitem in the tree | 📋 Not in demo — recommended |
| `End` | Moves focus to the last visible treeitem in the tree | 📋 Not in demo — recommended |
| `Escape` | If a grouper is focused and expanded, collapse it | 📋 Not in demo — recommended |

> **Focus management — roving tabindex:** Only the currently focused item has `tabindex="0"`. When focus moves to a new item (via arrow key), set the old item to `tabindex="-1"` and the new item to `tabindex="0"`. This ensures Tab always lands on the last-focused item when the user returns to the tree.

---

### 13.4 Focus Styles

| Requirement | Status |
|---|---|
| Visible focus ring on all interactive items | ❓ Not styled in demo — browser default outline only |
| Focus ring must not be suppressed (`outline: none` without replacement) | 📋 Required — WCAG 2.4.11 |
| Focus ring should use `:focus-visible` (not `:focus`) to avoid painting on mouse click | 📋 Recommended |
| Suggested focus style | `outline: 2px solid #3555a0; outline-offset: 2px;` (uses `Icon/Contextual/NavItem/Active`) |

> Figma does not contain a "focused" state variant in the `SideNavItem` component variants. This is a documentation gap — a focused state should be added to the component before production. See §15.

---

### 13.5 Screen Reader Announcements

| Concern | Recommendation | Status |
|---|---|---|
| Tree label | `<ul role="tree" aria-label="Main navigation">` — ensures the landmark is named and SR announces "tree" on entry | 📋 Required |
| Grouper state | `aria-expanded="true/false"` on grouper treeitems only — SR announces "expanded" or "collapsed". Do not put `aria-expanded` on leaf destination items. | 📋 Required |
| Active page | `aria-current="page"` on the active destination — SR announces "current page" | ✅ Implemented in demo |
| Icon-only collapsed sidebar | When collapsed to 64px, labels are hidden visually. Each item needs a text alternative: `aria-label` on the item or a visually-hidden `<span>`. Do not rely on the icon alone. | 📋 Not in demo |
| Collapsed grouper children | When a grouper is collapsed, its children must be removed from DOM or `aria-hidden="true"` — not just visually hidden with CSS | 📋 Demo uses conditional render — correct approach |
| Collapse/Expand button | `aria-label="Collapse navigation"` when expanded, `aria-label="Expand navigation"` when collapsed. Update dynamically as state changes. | 📋 Not in demo |
| Depth announcement | Screen readers announce depth automatically from the markup nesting — do not add manual "level 1 / level 2" text | ✅ Handled by correct markup |

#### Expected screen reader output (VoiceOver / NVDA)

These are approximate strings. Exact wording varies by screen reader and browser.

| Scenario | Expected announcement |
|---|---|
| Tab into the nav | *"Main navigation, tree"* |
| Focus on a leaf destination item (resting) | *"Reports, treeitem, 3 of 7"* |
| Focus on the active destination | *"Enter, current page, treeitem, 2 of 7"* |
| Focus on a collapsed grouper | *"Applications, collapsed, treeitem, 1 of 7"* |
| Focus on an expanded grouper | *"Applications, expanded, treeitem, 1 of 7"* |
| Focus on a Level 1 child | *"Enter Journal, treeitem, 1 of 3, level 2"* |
| Pressing → on a collapsed grouper | *"Applications, expanded"* (state change announced) |
| Pressing ← on an expanded grouper | *"Applications, collapsed"* |
| Focus on Collapse button | *"Collapse navigation, button"* |
| Sidebar collapsed, focus on icon-only item | *"Reports, treeitem"* — only if `aria-label` is set; without it: *"treeitem"* (no label — broken) |


---

### 13.6 Colour Contrast

All values below use token resolved values. Verify with a tool (e.g. Colour Contrast Analyser).

| State | Text token → hex | Background | Approx. ratio | WCAG AA (4.5:1) |
|---|---|---|---|---|
| Base | `Text/NavItem/Base` → `#4b4b4b` on `#fafafa` | ~6.3:1 | ✅ Pass |
| Hover | `Text/NavItem/Hover` → `#363636` on `≈#f5f5f5` | ~9.3:1 | ✅ Pass |
| Active | `Text/NavItem/Active` → `#02060d` on `≈#eef1f8` | ~19:1 | ✅ Pass |
| Trail (expanded) | `Text/NavItem/Active` → `#02060d` on `≈#f5f5f5` | ~19:1 | ✅ Pass |
| `indicator.stripe` | `Icon/NavItem/Active` → `#3555a0` on `#fafafa` | Non-text UI component | ✅ 3:1 (WCAG 1.4.11) |
| Focus ring (proposed) | `#3555a0` outline on `#fafafa` | Non-text UI component | ✅ 3:1 — verify with tool |

> ⚠ Contrast ratios are approximated on the `#fafafa` nav surface. Alpha-blended fills (`rgba(...)`) will vary on other backgrounds.

---

### 13.7 Figma Accessibility Gaps

The ARIA pattern, keyboard tables, screen reader strings, and contrast ratios all live in this spec (single source of truth). Figma does not need to duplicate that content — it should link to this document instead.

The only things that genuinely need to be **done in Figma** (because they are design artifacts, not documentation):

| Gap | Priority | Action needed in Figma |
|---|---|---|
| No "focused" state variant in `SideNavItem` | HIGH | Design and add a focused variant to the component — suggested style: `2px solid #3555a0` outline, `2px` offset. This is a visual design decision that must exist in Figma. |
| No link to this spec in Dev Mode | HIGH | In Figma Dev Mode → Resources panel, add the spec URL: `https://helloimjolopez-collab.github.io/pathwaytokens/SideNav-spec.md`. Takes 30 seconds and means devs always have one click to the full reference. |
| Accessibility section in Figma doc frame is outdated | MEDIUM | Replace with a short plain-text summary (component description, key decisions, any gaps that require design work) and a link to this spec. Do not duplicate tables. |

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
