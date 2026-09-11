export function Ico({ d, size = 15, stroke = "currentColor" }) {
  return (
    <svg viewBox="0 0 16 16" width={size} height={size} fill="none" stroke={stroke} strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round">
      <path d={d} />
    </svg>
  );
}

export function SearchIco({ size = 14 }) {
  return (
    <svg viewBox="0 0 16 16" width={size} height={size} fill="none" stroke="currentColor" strokeWidth="1.5">
      <circle cx="7.2" cy="7.2" r="4.4" />
      <path d="M10.5 10.5 14 14" strokeLinecap="round" />
    </svg>
  );
}

export const PATHS = {
  rail: "M2 3h12v10H2z M6.2 3v10",
  plus: "M8 3.2v9.6M3.2 8h9.6",
  bell: "M4 6.6a4 4 0 0 1 8 0c0 3 .9 4 .9 4H3.1s.9-1 .9-4 M6.6 13a1.6 1.6 0 0 0 2.8 0",
  star: "M8 2.4 9.6 6 13.6 8 9.6 10 8 13.6 6.4 10 2.4 8 6.4 6z",
  today: "M2.4 6.8 8 2.4l5.6 4.4V13a.6.6 0 0 1-.6.6H3a.6.6 0 0 1-.6-.6z",
  work: "M2.2 5.4h11.6v8H2.2zM5.8 5.4V3.6h4.4v1.8",
  inbox: "M2.2 9.2h3l1 1.9h3.6l1-1.9h3M2.2 9.2l1.9-6h7.8l1.9 6v4.2H2.2z",
  people: "M6.2 7.6a2.2 2.2 0 1 0 0-4.4 2.2 2.2 0 0 0 0 4.4M1.9 13.4c0-2.3 1.9-3.5 4.3-3.5s4.3 1.2 4.3 3.5M11 4.1a2 2 0 0 1 0 4M12.6 13.4c0-1.5-.4-2.5-1.3-3.1",
  data: "M2.6 13.2V8.4M6.2 13.2V3.6M9.8 13.2V9.8M13.4 13.2V6.2",
  files: "M2.2 4.6A1.4 1.4 0 0 1 3.6 3.2h2.3l1.4 1.8h5.1a1.4 1.4 0 0 1 1.4 1.4v6a1.4 1.4 0 0 1-1.4 1.4H3.6a1.4 1.4 0 0 1-1.4-1.4z",
  plug: "M6 2.4v3M10 2.4v3M4.6 5.4h6.8v3.7a3.4 3.4 0 0 1-6.8 0zM8 12.2v1.6",
  settings: "M8 10.2a2.2 2.2 0 1 1 0-4.4 2.2 2.2 0 0 1 0 4.4M13.1 8.9l1.2.9-1.3 2.2-1.4-.5a5 5 0 0 1-1.6 1L9.7 14H7.1l-.3-1.5a5 5 0 0 1-1.6-1l-1.4.5-1.3-2.2 1.2-.9a5 5 0 0 1 0-1.8l-1.2-.9 1.3-2.2 1.4.5a5 5 0 0 1 1.6-1L7.1 2h2.6l.3 1.5a5 5 0 0 1 1.6 1l1.4-.5 1.3 2.2-1.2.9a5 5 0 0 1 0 1.8",
  sun: "M8 1.8v1.6M8 12.6v1.6M1.8 8h1.6M12.6 8h1.6M3.6 3.6l1.1 1.1M11.3 11.3l1.1 1.1M12.4 3.6l-1.1 1.1M4.7 11.3l-1.1 1.1M10.5 8a2.5 2.5 0 1 1-5 0 2.5 2.5 0 0 1 5 0",
  moon: "M13.2 9.6A5.6 5.6 0 0 1 6.4 2.8 5.6 5.6 0 1 0 13.2 9.6Z",
};
