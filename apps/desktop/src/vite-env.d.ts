/// <reference types="vite/client" />

interface ImportMetaEnv {
  readonly ENGINE_API_BASE_URL?: string;
  readonly VITE_ENGINE_API_BASE_URL?: string;
}

interface ImportMeta {
  readonly env: ImportMetaEnv;
}
