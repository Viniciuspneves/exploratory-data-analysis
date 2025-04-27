import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()

def plot_bar_from_column(df,
                         column,
                         title=None,
                         xlabel=None,
                         ylabel="Quantidade",
                         figsize=(12, 6),
                         top_n=None,
                         rotation=0,
                         percent=False,
                         save_path=None):
    '''
    Cria um gráfico de barras mostrando o total de acidentes ou a porcentagem.

    Parameters:
    df : pandas.DataFrame
        DataFrame com os dados processados
    column : str
        Nome da coluna do DataFrame a ser analisada
    title : str, opcional
        Título do gráfico
    xlabel : str, opcional
        Legenda do eixo x
    ylabel : str, default="Quantidade"
        Legenda do eixo y
    figsize : tuple, default=(12, 6)
        Tamanho da figura
    top_n : int, opcional
        Número máximo de categorias a exibir (ex: top 10)
    rotation : int, default=0
        Rotação dos rótulos no eixo X
    percent : bool, default=False
        Se True, plota as porcentagens ao invés da contagem
    save_path : str, opcional
        Caminho completo onde salvar a imagem. Se None, apenas exibe.
    '''
    # Conta os valores
    counts = df[column].value_counts()

    # Se top_n for definido, filtra os N primeiros
    if top_n is not None:
        counts = counts.head(top_n)

    # Se percent for True, converte counts para porcentagem
    if percent:
        counts = (counts / counts.sum()) * 100
        ylabel = "Porcentagem (%)"

    # Cria o gráfico
    ax = sns.barplot(x=counts.index, y=counts.values)
    ax.figure.set_size_inches(*figsize)

    # Títulos
    ax.set_title(title or f"Distribuição de {column}", fontsize=16)
    ax.set_xlabel(xlabel or column)
    ax.set_ylabel(ylabel)

    # Rotação dos rótulos do eixo x
    plt.xticks(rotation=rotation)

    # Rótulos nas barras
    if percent:
        ax.bar_label(ax.containers[0], fmt="%.2f%%")
    else:
        ax.bar_label(ax.containers[0])

    # Layout e exibição
    ax.figure.tight_layout()

    # Salva a imagem se o caminho for fornecido
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')

    plt.show()


import folium
from folium.plugins import HeatMap, MarkerCluster
import os

def folium_accident_map(df, column, min_value=1, output_dir='docs'):
    """
    Gera um mapa com heatmap e marcadores clusterizados para acidentes com pelo menos 1 ocorrência.

    Parâmetros:
        df (DataFrame): DataFrame com colunas 'Latitude', 'Longitude' e a coluna de interesse.
        column (str): Nome da coluna que representa a quantidade (ex: 'Persons Killed').
        min_value (int): Valor mínimo da coluna para filtrar os dados (padrão: 1).
        output_dir (str): Pasta onde o mapa será salvo. Padrão: 'docs'.

    Retorna:
        folium.Map: Mapa com visualização dos acidentes.
    """
    # Filtra coordenadas válidas e acidentes com pelo menos 1 ocorrência
    df_valid = df.dropna(subset=['Latitude', 'Longitude', column])
    df_valid = df_valid[df_valid[column] >= min_value]

    # Define coordenadas centrais de NYC
    ny_coords = [40.7128, -74.0060]
    mapa_ny = folium.Map(location=ny_coords, zoom_start=11)

    # Cria o HeatMap
    heat_data = df_valid[['Latitude', 'Longitude', column]].values.tolist()
    HeatMap(heat_data, radius=5, max_zoom=13).add_to(mapa_ny)

    # Adiciona marcadores em cluster
    cluster = MarkerCluster().add_to(mapa_ny)
    for _, row in df_valid.iterrows():
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=f"{column}: {int(row[column])}",
            icon=folium.Icon(color='red', icon='plus-sign')
        ).add_to(cluster)

    # Garante que a pasta de destino exista fora do notebook
    raiz_dir = os.path.abspath(os.path.join(os.getcwd(), '../..'))  # Pega o diretório raiz
    docs_dir = os.path.join(raiz_dir, output_dir)  # Junta com 'docs' na raiz
    os.makedirs(docs_dir, exist_ok=True)

    # Salva com nome baseado na coluna
    nome_arquivo = f"{column.replace(' ', '_')}.html"
    caminho_arquivo = os.path.join(docs_dir, nome_arquivo)
    mapa_ny.save(caminho_arquivo)

    return mapa_ny

