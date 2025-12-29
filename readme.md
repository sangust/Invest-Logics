# Invest-Logics

Invest-Logics é um projeto de **SaaS financeiro** focado em **coleta, normalização e análise de dados do mercado acionário brasileiro**, com o objetivo final de gerar previsões de preços e retornos financeiros para ações listadas na B3.

O projeto prioriza **dados oficiais**, consistência histórica e controle total sobre a origem das informações, evitando dependência exclusiva de APIs externas.

---

## Objetivo do Projeto

- Centralizar dados financeiros históricos de ações brasileiras
- Corrigir inconsistências de dados públicos (especialmente CVM)
- Armazenar dados de forma estruturada e confiável
- Preparar base sólida para modelos de previsão de preços
- Oferecer, futuramente, um serviço SaaS funcional e estável

---

## Stack Tecnológica

### Backend
- **Python**
- **Flask** (API e backend do SaaS)
- **PostgreSQL**
- **psycopg** (driver PostgreSQL)

### Dados & Automação
- **Pandas** (tratamento de dados)
- **Regex** (validação de CNPJ)
- **PyAutoGUI** (automação de coleta quando APIs não existem)
- **Excel / CSV / ZIP (CVM)**



