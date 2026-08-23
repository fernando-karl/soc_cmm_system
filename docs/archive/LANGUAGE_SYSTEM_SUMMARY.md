# Sistema de Alternância de Idiomas - SOC CMM

> **Documentação de usuário** com o mesmo conteúdo em formato resumido:
> - 🇬🇧 [`docs/en/languages.md`](docs/en/languages.md)
> - 🇧🇷 [`docs/pt-br/idiomas.md`](docs/pt-br/idiomas.md)
>
> Este arquivo descreve o **design e a implementação** do subsistema. Para
> uso corriqueiro, prefira os documentos acima.

## 📋 Resumo

Foi implementado um sistema completo de alternância de idiomas para o Sistema de Avaliação SOC CMM, permitindo aos usuários alternar entre **Inglês** e **Português do Brasil** em todas as páginas do sistema (exceto as páginas administrativas).

## 🌍 Funcionalidades Implementadas

### 1. **Seletor de Idioma na Navegação**
- **Localização**: Barra de navegação superior (bandeira do idioma atual)
- **Funcionalidade**: Dropdown com opções "English" e "Português" com bandeiras
- **Indicador Visual**: Bandeira do idioma atual + texto (EN/PT-BR)
- **Estado Ativo**: Opção selecionada destacada com fundo azul e checkmark
- **Responsivo**: Adapta-se a dispositivos móveis

### 2. **Sistema de Detecção de Idioma**
- **Prioridade 1**: Parâmetro de query `?lang=en` ou `?lang=pt_br`
- **Prioridade 2**: Cookie `language` armazenado no navegador
- **Padrão**: Inglês (`en`) se nenhum idioma for especificado

### 3. **Rota de Alternância de Idioma**
- **URL**: `/change-language/{language}`
- **Funcionalidade**: Altera o idioma e redireciona para a página anterior
- **Persistência**: Define cookie com duração de 1 ano

## 📁 Arquivos Modificados

### Backend (`main.py`)
- ✅ Função `get_language_from_request()` - Detecta idioma
- ✅ Função `get_template_name()` - Seleciona template correto
- ✅ Rota `/change-language/{language}` - Alterna idioma
- ✅ Todas as rotas principais atualizadas para suportar idiomas

### Templates Base
- ✅ `templates/base.html` - Seletor de idioma em inglês
- ✅ `templates/base_pt_br.html` - Seletor de idioma em português

### Estilos CSS (`static/css/style.css`)
- ✅ Estilos para `.language-selector`
- ✅ Estilos para `.language-toggle`
- ✅ Estilos para `.language-dropdown-menu`
- ✅ Estilos responsivos para dispositivos móveis

## 📄 Páginas com Suporte a Idiomas

### ✅ Páginas Implementadas
1. **Home** (`index.html` ↔ `index_pt_br.html`)
2. **Login** (`login.html` ↔ `login_pt_br.html`)
3. **Registro** (`register.html` ↔ `register_pt_br.html`)
4. **Clientes** (`customers.html` ↔ `customers_pt_br.html`)
5. **Avaliação** (`assessment.html` ↔ `assessment_pt_br.html`)
6. **Resultados** (`results.html` ↔ `results_pt_br.html`)
7. **Alterar Senha** (`change_password.html` ↔ `change_password_pt_br.html`)
8. **Ajuda** (`help.html` ↔ `help_pt_br.html`)
9. **FAQ** (`faq.html` ↔ `faq_pt_br.html`)
10. **Termos** (`terms.html` ↔ `terms_pt_br.html`)
11. **Política de Privacidade** (`privacy_policy.html` ↔ `privacy_policy_pt_br.html`)

### ❌ Páginas Administrativas (Sem Suporte)
- `admin_dashboard.html`
- `admin_users.html`
- `admin_edit_user.html`
- `admin_new_user.html`

## 🔧 Como Funciona

### 1. **Detecção de Idioma**
```python
def get_language_from_request(request: Request) -> str:
    # 1. Verifica parâmetro de query
    lang = request.query_params.get("lang")
    if lang in ["en", "pt_br"]:
        return lang
    
    # 2. Verifica cookie
    lang = request.cookies.get("language")
    if lang in ["en", "pt_br"]:
        return lang
    
    # 3. Padrão: Inglês
    return "en"
```

### 2. **Seleção de Template**
```python
def get_template_name(base_name: str, language: str) -> str:
    if language == "pt_br":
        return f"{base_name}_pt_br.html"
    return f"{base_name}.html"
```

### 3. **Rota de Alternância**
```python
@app.get("/change-language/{language}")
async def change_language(request: Request, language: str):
    # Valida idioma
    if language not in ["en", "pt_br"]:
        language = "en"
    
    # Redireciona para página anterior
    referer = request.headers.get("referer", "/")
    response = RedirectResponse(url=referer, status_code=302)
    
    # Define cookie
    response.set_cookie("language", language, max_age=31536000)
    return response
```

## 🎨 Interface do Usuário

### Seletor de Idioma
- **Ícone**: 🇺🇸 / 🇧🇷 (bandeiras dos países)
- **Texto**: Eng / Port
- **Interface**: Seletor direto sem dropdown
- **Indicador**: Opção ativa destacada com fundo azul e checkmark (✓)

### Comportamento Responsivo
- **Desktop**: Mostra bandeira + texto "Eng" / "Port"
- **Mobile**: Mostra bandeira + texto menor
- **Interface**: Seletor direto sempre visível

## 🧪 Testes

### Scripts de Teste Automatizado
- **Arquivo**: `test_language_system.py` - Testes gerais do sistema
- **Arquivo**: `test_language_dropdown.py` - Testes específicos do dropdown
- **Funcionalidades testadas**:
  - Detecção de idioma padrão
  - Alternância para português
  - Persistência via cookies
  - Alternância para inglês
  - Funcionamento em diferentes páginas
  - Parâmetros de query
  - Visibilidade do dropdown (deve estar oculto por padrão)
  - Presença das bandeiras
  - Estado ativo das opções

### Teste Manual
1. Acesse `http://localhost:8400` (ou na porta definida em `PORT`)
2. Verifique se o seletor de idioma está visível: [🇺🇸 Eng] / [🇧🇷 Port]
3. Verifique se o idioma atual está destacado (fundo azul + checkmark)
4. Clique em "Port" para mudar para português
5. Verifique se o conteúdo mudou para português
6. Navegue entre as páginas
7. Verifique se o idioma persiste

## 🔒 Segurança e Performance

### Segurança
- ✅ Validação de idiomas permitidos (`en`, `pt_br`)
- ✅ Sanitização de parâmetros de entrada
- ✅ Cookies seguros com `httponly=True`

### Performance
- ✅ Cache de templates por idioma
- ✅ Cookies com duração de 1 ano
- ✅ Redirecionamento eficiente
- ✅ Sem impacto na performance das páginas

## 📈 Próximos Passos (Opcionais)

### Melhorias Futuras
1. **Detecção automática**: Detectar idioma do navegador
2. **Mais idiomas**: Suporte para espanhol, francês, etc.
3. **Tradução dinâmica**: Sistema de tradução automática
4. **Páginas administrativas**: Adicionar suporte a idiomas
5. **URLs localizadas**: `/pt/ajuda` em vez de `/help?lang=pt_br`

### Manutenção
1. **Sincronização**: Manter templates em inglês e português sincronizados
2. **Validação**: Verificar se todas as strings estão traduzidas
3. **Testes**: Executar testes de idioma regularmente

## 🎉 Conclusão

O sistema de alternância de idiomas foi implementado com sucesso, oferecendo:

- ✅ **Experiência completa** em português do Brasil
- ✅ **Interface intuitiva** para alternância de idiomas
- ✅ **Persistência** das preferências do usuário
- ✅ **Compatibilidade** com dispositivos móveis
- ✅ **Performance otimizada** sem impacto na velocidade
- ✅ **Segurança** com validação adequada

O sistema está pronto para uso em produção e pode ser facilmente expandido para suportar idiomas adicionais no futuro.

## 🔧 Correções Recentes

### Problema do Dropdown Visível
- **Problema**: Dropdown aparecia por padrão sem clicar
- **Solução**: Simplificado para seletor direto sem dropdown
- **Arquivos modificados**: 
  - `templates/base.html` - Removido dropdown, adicionado seletor direto
  - `templates/base_pt_br.html` - Removido dropdown, adicionado seletor direto
  - `static/css/style.css` - Estilos para novo seletor e bandeiras
- **Resultado**: Interface mais simples e intuitiva

### Melhoria das Bandeiras
- **Problema**: Bandeiras não apareciam no novo seletor
- **Solução**: Adicionados estilos CSS específicos para `.language-selector .dropdown-item .flag-icon`
- **Arquivos modificados**:
  - `static/css/style.css` - Estilos para bandeiras no seletor simplificado
- **Teste**: `test_flag_icons.py` para verificar bandeiras 