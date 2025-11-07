# GitHub Copilot Instructions

## Commit Message Guidelines

When suggesting commit messages, always use the Conventional Commits specification format:

**Format:** `<type>[optional scope]: <description>`

### Examples:

- `feat: add user authentication system`
- `fix: resolve null pointer exception in payment service`
- `docs: update API documentation for v2.0`
- `style: format code according to eslint rules`
- `refactor: extract validation logic into separate module`
- `test: add unit tests for user registration`
- `chore: update dependencies to latest versions`
- `perf: optimize database queries for faster response`
- `ci: add automated deployment pipeline`
- `build: update webpack configuration for production`
- `feat(auth): implement OAuth2 integration`
- `fix(api): handle edge case in data validation`
- `docs(readme): add installation instructions`

### Breaking Changes:
- `feat!: redesign user interface (BREAKING CHANGE)`
- `refactor!: change API response format`

# Descrição do Projeto

Este projeto é um site educacional para compartilhar tarefas de casa e exercícios de programação com estudantes. Os estudantes podem navegar, visualizar e baixar tarefas diretamente do portal.

## Estrutura do Projeto

- [`assignments/`](../assignments/) Cada tarefa de casa é armazenada em sua própria subpasta com uma estrutura consistente.
- [`templates/`](../templates/) Templates reutilizáveis para novo conteúdo
- [`assets/`](../assets/) Contém os recursos do site incluindo CSS, JavaScript, imagens e arquivos de configuração
- [`index.html`](../index.html) A página principal do site que serve como um portal estático para navegar e visualizar tarefas. O conteúdo é configurável através do arquivo [`config.json`](../config.json) para gerar dinamicamente listas e detalhes de tarefas.

## Diretrizes do Projeto

- Manter estilo consistente em todas as páginas
- Manter nomes de arquivos e pastas descritivos e organizados

## Padrões Educacionais

Ao gerar conteúdo para este projeto:

- **Focado em aprendizado**: Todo conteúdo deve ser projetado com objetivos de aprendizado claros e níveis de dificuldade apropriados
- **Amigável para estudantes**: Use linguagem clara e encorajadora que motiva os estudantes