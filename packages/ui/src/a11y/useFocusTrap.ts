import { useEffect, type RefObject } from "react";
import { cycleFocus, getFocusable } from "./focusable";

/** Traps Tab inside `ref` while `active`. Restores prior focus on teardown. */
export function useFocusTrap(ref: RefObject<HTMLElement | null>, active: boolean): void {
  useEffect(() => {
    if (!active) return;
    const node = ref.current;
    if (!node) return;
    const prior = document.activeElement instanceof HTMLElement ? document.activeElement : null;
    const focusables = getFocusable(node);
    (focusables[0] ?? node).focus();

    const onKey = (event: KeyboardEvent) => {
      cycleFocus(node, event);
    };
    node.addEventListener("keydown", onKey);
    return () => {
      node.removeEventListener("keydown", onKey);
      prior?.focus();
    };
  }, [ref, active]);
}
