import { useEffect, useState } from "react";

/** Viewport flags. Mobile ≤768; narrow <1100 (rail collapse). */
export function useViewport(mobileBreakpoint = 768, narrowBreakpoint = 1100): {
  isMobile: boolean;
  isNarrow: boolean;
  width: number;
} {
  const read = () => {
    const width = typeof window !== "undefined" ? window.innerWidth : 1440;
    return {
      width,
      isMobile: width <= mobileBreakpoint,
      isNarrow: width < narrowBreakpoint,
    };
  };
  const [state, setState] = useState(read);
  useEffect(() => {
    const mqMobile = window.matchMedia(`(max-width: ${mobileBreakpoint}px)`);
    const mqNarrow = window.matchMedia(`(max-width: ${narrowBreakpoint - 1}px)`);
    const update = () => setState(read());
    mqMobile.addEventListener("change", update);
    mqNarrow.addEventListener("change", update);
    window.addEventListener("resize", update);
    update();
    return () => {
      mqMobile.removeEventListener("change", update);
      mqNarrow.removeEventListener("change", update);
      window.removeEventListener("resize", update);
    };
  }, [mobileBreakpoint, narrowBreakpoint]);
  return state;
}

export function useIsMobile(breakpoint = 768): boolean {
  return useViewport(breakpoint).isMobile;
}
