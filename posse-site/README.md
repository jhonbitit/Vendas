# POSSE Site

Site criado com Next.js 14 (App Router) e Tailwind CSS.

## Rodando localmente

```bash
npm install
npm run dev
```

Abra `http://localhost:3000`.

## Variáveis de ambiente

Copie `.env.local.example` para `.env.local` e preencha:

- `IG_ACCESS_TOKEN`: token de acesso do Instagram Basic Display/Graph API
- `IG_USER_ID` (opcional): ID do usuário do Instagram
- `NEXT_PUBLIC_FB_PAGE_URL`: URL da página do Facebook para embed
- `NEXT_PUBLIC_FB_CHAT_ENABLED`: `true` para habilitar Chat Plugin

## Build

```bash
npm run build && npm run start
```

## Logo

Substitua `public/logo.svg` pela sua imagem desejada (pode ser .svg ou .png) mantendo o nome `logo.svg` ou ajuste em `src/components/Header.tsx` e em `src/app/page.tsx`.
