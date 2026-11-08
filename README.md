# Data Engineering & Analytics Engineering

Projeto de estudos práticos de Engenharia de Dados e Analytics Engineering, utilizando Python, DuckDB, dbt Core e uv.

O objetivo é desenvolver um pipeline de dados reproduzível, explorando ingestão, organização, transformação, modelagem dimensional, testes e documentação.

## Arquitetura inicial


### Tecnologias

| Tecnologia | Responsabilidade |
|---|---|
| Python | Ingestão e preparação dos dados |
| uv | Gerenciamento de dependências e ambiente Python |
| DuckDB | Banco analítico local |
| dbt Core | Transformação, modelagem e testes |
| Git | Versionamento do projeto |

## Setup

### 1. Clonar o repositório

```bash
git clone <REPOSITORY_URL>
cd dbt-analytics
```

### 2. Instalar as dependências

O projeto utiliza uv para gerenciar as dependências Python.

```bash
uv sync
```

O comando instala as dependências definidas no `pyproject.toml`, respeitando as versões registradas no `uv.lock`.

### 3. Baixar os dados

Execute o script de download:

```bash
chmod +x scripts/download_data.sh
./scripts/download_data.sh
```

Os arquivos serão armazenados em `data/raw/`.

Dataset utilizado: [Jaffle Shop Classic](https://github.com/dbt-labs/jaffle-shop-classic).

### 4. Executar a ingestão

A ingestão utiliza Python e DuckDB para carregar os arquivos CSV no banco local.

```bash
uv run python src/dbt_analytics/ingestion.py
```

O banco será criado em:

```text
data/warehouse/jaffle_shop.duckdb
```

Os dados serão carregados no schema `raw`, nas seguintes tabelas:

- `raw.raw_customers`
- `raw.raw_orders`
- `raw.raw_payments`

### 5. Validar a conexão com o dbt

```bash
uv run dbt debug \
  --project-dir dbt/jaffle_shop \
  --profiles-dir dbt
```

A configuração local do banco é definida em `dbt/profiles.yml`.

**Observação:** esse arquivo não é versionado, pois pode conter configurações específicas do ambiente ou credenciais.

## Próximas etapas

- [x] Configuração inicial do ambiente Python com uv.
- [x] Configuração do dbt Core com DuckDB.
- [x] Download dos dados do Jaffle Shop.
- [x] Ingestão dos arquivos CSV para o schema raw.
- [ ] Configuração das sources no dbt.
- [ ] Desenvolvimento dos modelos staging.
- [ ] Desenvolvimento dos modelos intermediate.
- [ ] Construção dos marts e modelo dimensional.
- [ ] Implementação de testes e documentação.
- [ ] Automatização e orquestração do pipeline.