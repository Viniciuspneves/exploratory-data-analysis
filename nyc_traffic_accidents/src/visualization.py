import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()

def plot_bar_from_column(df, column, title=None, xlabel=None, ylabel="Quantidade", figsize=(12, 6), top_n=None, rotation=0):
    '''
    Cria um gráfico de barras mostrando o total de acidentes

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
    '''
    # Conta os valores
    counts = df[column].value_counts()

    # Se top_n for definido, filtra os N primeiros
    if top_n is not None:
        counts = counts.head(top_n)

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
    ax.bar_label(ax.containers[0])

    # Layout e exibição
    ax.figure.tight_layout()
    plt.show()
