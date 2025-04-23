# Dataset Utilizado

## Acidentes de trânsito em Nova York

Colisões de veículos motorizados relatadas pelo Departamento de Polícia da Cidade de Nova York de janeiro de 2021 a abril de 2023. Cada registro representa uma colisão individual, incluindo a data, hora e local do acidente (bairro, CEP, nome da rua, latitude/longitude), veículos e vítimas envolvidas e fatores contribuintes.

### Análise recomendada

- Compare a % do total de acidentes por mês. Você percebe algum padrão sazonal?

- Divida a frequência de acidentes por dia da semana e hora do dia. Com base nesses dados, quando os acidentes ocorrem com mais frequência?

- Em qual rua em particular foram relatados mais acidentes? O que isso representa como % de todos os acidentes relatados?

- Qual foi o fator contribuinte mais comum para os acidentes relatados? E quanto a acidentes fatais especificamente?

### Sumário com uma breve descrição de cada coluna

- **Collision ID**: Código único gerado pelo sistema para identificar o registro.
- **Date**: Data em que ocorreu o acidente.
- **Time**: Hora em que ocorreu o acidente.
- **Borough**: Bairro onde o acidente ocorreu.
- **Street Name**: Nome da rua onde ocorreu o acidente.
- **Cross Street**: Rua cruzada mais próxima ao local do acidente.
- **Latitude**: Coordenada de latitude no Sistema de Coordenadas Global WGS 1984 (graus decimais EPSG 4326).
- **Longitude**: Coordenada de longitude no Sistema de Coordenadas Global WGS 1984 (graus decimais EPSG 4326).
- **Contributing Factor**: Fatores que contribuíram para o acidente, especificamente para o veículo designado.
- **Vehicle Type**: Tipo de veículo envolvido no acidente.
- **Persons Injured**: Número total de pessoas feridas (pedestres, ciclistas, motoristas).
- **Persons Killed**: Número total de pessoas mortas (pedestres, ciclistas, motoristas).
- **Pedestrians Injured**: Número de pedestres feridos.
- **Pedestrians Killed**: Número de pedestres mortos.
- **Cyclists Injured**: Número de ciclistas feridos.
- **Cyclists Killed**: Número de ciclistas mortos.
- **Motorists Injured**: Número de motoristas feridos (ocupantes do veículo).
- **Motorists Killed**: Número de motoristas mortos (ocupantes do veículo).

#### Link para download dos dados

>- [NYC Traffic Accidents](https://mavenanalytics.io/data-playground?order=number_of_records%2Cdesc&page=3&pageSize=5)
