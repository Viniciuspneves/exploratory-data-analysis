# Análise de Acidentes de Trânsito em Nova York (2021-2023)

## Sobre o Projeto

Neste projeto, eu analiso dados sobre acidentes de trânsito em Nova York, ocorridos entre janeiro de 2021 e abril de 2023. O objetivo é entender melhor onde, quando e por que esses acidentes acontecem, identificando padrões como horários de pico, dias da semana e locais com maior incidência de colisões.

## Estrutura do Repositório

O repositório está organizado da seguinte forma:

- [**`data/`**](./data/) Dados brutos e processados;
- [**`docs/`**](./docs/) Documentação técnica, incluindo dicionário de dados;
- [**`notebooks/`**](./notebooks/) Jupyter Notebooks separados por etapas da análise;
- [**`src/`**](./src/) Scripts Python reutilizáveis para limpeza, visualização e funções auxiliares;
- [**`visualizations/`**](./visualizations/): Gráficos exportados organizados por tipo de análise;
- [**`README.md`**](./README.md) Uma breve descrição sobre o conjunto de dados, contexto e perguntas de negócio;
- [**`requirements.txt`**](./requirements.txt) Arquivo com as dependências do projeto, incluindo bibliotecas para análise de dados, visualizações e construção do dashboard interativo.

## Objetivo

Este projeto é uma oportunidade de aplicar e aprimorar minhas habilidades em análise de dados, enquanto compartilho o processo e os resultados de forma clara e acessível. Ele também serve como parte do meu portfólio para mostrar minha capacidade de trabalhar com dados e comunicar resultados de forma simples e eficaz.

---

## Storytelling

Entre 2021 e 2023, milhares de acidentes de trânsito foram registrados em Nova York. Este projeto busca entender os padrões por trás desses eventos: quando e por que eles acontecem com mais frequência? Com uma abordagem clara e visual, nosso objetivo é transformar os dados em respostas acessíveis para qualquer pessoa interessada no tema, incluindo profissionais da área de segurança, gestão urbana e análise de dados.

## Fonte dos Dados

Os dados foram obtidos do NYC Open Data e contêm informações sobre todos os acidentes de trânsito ocorridos na cidade de Nova York entre janeiro de 2021 e abril de 2023. As variáveis incluem data, hora, localização, fatores contribuintes, tipo de usuário afetado (pedestre, ciclista, motorista), número de feridos e mortos.

## Análise recomendada

- Compare a % do total de acidentes por mês. Você percebe algum padrão sazonal?

- Divida a frequência de acidentes por dia da semana e hora do dia. Com base nesses dados, quando os acidentes ocorrem com mais frequência?

- Em qual rua em particular foram relatados mais acidentes? O que isso representa como % de todos os acidentes relatados?

- Qual foi o fator contribuinte mais comum para os acidentes relatados? E quanto a acidentes fatais especificamente?

**Observação:**

- Ao longo da análise outros tipos de perguntas de negócio foram surgindo que resultaram na soma do projeto como um todo. Dividimos em etapas toda a análise, `data_cleaning`, `temporal`, `geographic`, `contribuing_factors` e `advanced_analysis`

## Tratamento de Dados

Antes de qualquer análise, é essencial garantir que os dados estejam limpos, organizados e prontos para uso. Dados com valores ausentes, formatos inconsistentes ou informações irrelevantes podem comprometer a qualidade da análise e levar a conclusões incorretas.

Nesta etapa, aplicamos um processo de tratamento focado na clareza, coerência e integridade dos dados. A seguir, explicamos de forma simples e direta quais decisões foram tomadas e por quê.

### Diagnóstico Inicial

O dataset original contém 238.421 registros e 18 colunas. Algumas dessas colunas apresentavam valores nulos. Para lidar com esses casos, adotamos um critério baseado na proporção de dados ausentes, conforme a tabela:

| Percentual de Nulos | Recomendação Geral |
|---------------------|--------------------|
| < 5%                | Pode manter e preencher (ex: com "Unknown", média, zero etc.) |
| 5% – 30%            | Avaliar com cuidado. Se for uma coluna importante, preencher. Se for irrelevante, pode remover. |
| > 30% – 50%         | Tendência a descartar, a menos que a variável seja muito relevante |
| > 50%               | Normalmente descartada, a menos que seja fundamental e não possa ser obtida de outra forma |

Com base nesse critério, analisamos individualmente as colunas com nulos e tomamos decisões alinhadas ao propósito do projeto.

#### Coluna: Cross Street

- Problema identificado: 53,32% dos registros estavam vazios.

- Impacto: A ausência de mais da metade dos dados compromete qualquer análise baseada nessa coluna.

- Decisão: Remoção da coluna. Temos outras variáveis com melhor cobertura e precisão para localização, como Street Name, Borough, Latitude e Longitude.

#### Coluna: Borough

- Problema identificado: 3,02% de registros sem bairro informado.

- Por que não inferimos: O nome da rua, por si só, não é suficiente para determinar o bairro com precisão, já que ruas podem atravessar múltiplos bairros. Sem número, interseção ou CEP, não é possível localizar com confiança.

- Decisão: Remoção dos registros com valores ausentes, garantindo consistência nas análises de localização. O impacto na base é pequeno e a confiabilidade dos dados restantes aumenta.

#### Coluna: Contributing Factor

- Problema identificado: 0,54% dos registros sem causa informada.

- Decisão: Preenchimento com o valor "Unknown". Como o volume de ausências é muito pequeno, a escolha evita perda de dados úteis e mantém coerência com o restante da base. Ainda é possível incluir esses registros nas análises gerais, sem enviesar os resultados.

#### Coluna: Street Name

- Problema identificado: Apenas 0,15% de registros estavam vazios.

- Decisão: Preenchimento com "Unknown". A baixa taxa de nulos não justifica a exclusão de registros, que ainda são valiosos para outras análises. Em visualizações específicas, esses registros podem ser filtrados.

#### Colunas: Latitude e Longitude

- Problema identificado: Cerca de 9,36% dos registros não possuem coordenadas geográficas.

- Decisão: Manutenção desses registros. Apesar da ausência de localização geográfica, os dados ainda são relevantes para outras análises. As coordenadas serão filtradas apenas em visualizações que exigem geolocalização, como mapas.

#### Crição de Novas Colunas

Criamos novas colunas derivadas a partir de `Time` para facilitar as análises a seguir. `Year`, ``Month``, ``Month Name``, ``Day of week``, ``Day`` e ``Season``

#### Dataset Após Tratamento

Após a etapa de tratamento, o dataset foi reduzido para 231.223 registros e 23 colunas. A coluna Cross Street foi removida, e os registros sem bairro foram descartados. Também houve ajustes de tipos de dados, como a conversão da coluna Date para o formato datetime. E a criação de novas colunas derivadas.

---
