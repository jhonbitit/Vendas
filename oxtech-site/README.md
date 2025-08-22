# Oxtech - Site tipo POSSE

Site estático responsivo com tema escuro, visual minimalista e integrações com Instagram e Facebook.

## Estrutura
- `index.html`: página principal
- `styles.css`: estilos do tema
- `script.js`: navegação e utilitários
- `assets/logo.png`: sua logo (adicione o arquivo)

## Como usar
Abra o arquivo `index.html` no navegador ou sirva a pasta com qualquer servidor estático.

### Colocar a logo
1. Copie sua imagem para `assets/logo.png`.
2. Use PNG 512x512+ preferencialmente com fundo transparente.

### Instagram Embed
1. Obtenha o link de um post/reel do seu perfil.
2. No `index.html`, troque o valor do atributo `data-instgrm-permalink` por esse link.
3. O script oficial do Instagram (`https://www.instagram.com/embed.js`) já está incluído.

### Facebook Page Plugin
1. No `index.html`, localize o bloco `.fb-page`.
2. Troque `data-href` pela URL da sua página.
3. A SDK do Facebook já está adicionada.

### Formulário de contato
- O formulário usa um endpoint do Formspree como exemplo. Crie o seu form e substitua `https://formspree.io/f/your-id` no atributo `action`.
- Alternativamente, remova o `form` e use um link `mailto:`.

## Deploy rápido
- GitHub Pages, Netlify, Vercel ou qualquer serviço de hosting estático funcionam.

## Licença
Uso livre para projetos da Oxtech.