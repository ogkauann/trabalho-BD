# Matplotlib para criar gráficos e visualizações básicas
import matplotlib.pyplot as plt

# Seaborn para criar gráficos estatísticos com estilo bonito e fácil
import seaborn as sns

# Importar dados de Entorpecentes Excel
from leitura_dados import carregar_entorpecentes


# Carregar os dados de Entorpecentes
# df = carregar_entorpecentes()  # Remover carregamento global

# Funções para criar gráficos
def tipo_entorpecente(df, ax=None):
    if ax is None:
        ax = plt.gca()
    sns.countplot(data=df, y='Tipo de Entorpecente', order=df['Tipo de Entorpecente'].value_counts().index, ax=ax)
    ax.set_title('Total de Apreensões por Tipo de Entorpecente')
    ax.set_xlabel('Ocorrencias')
    ax.set_ylabel('Tipo de Entorpecente')


def peso_entorpecente(df, ax=None):
    if ax is None:
        ax = plt.gca()
    # Filtrar valores maiores que zero para melhor visualização da distribuição
    df_filtrado = df[df['Quantidade (Kg)'] > 0]
    if not df_filtrado.empty:
        # Limitar ao percentil 99 para evitar distorção por outliers
        limite = df_filtrado['Quantidade (Kg)'].quantile(0.99)
        df_filtrado = df_filtrado[df_filtrado['Quantidade (Kg)'] <= limite]
        sns.histplot(
            df_filtrado['Quantidade (Kg)'],
            bins=30,
            kde=True,
            ax=ax,
        )
        ax.set_xscale('log')
        ax.set_title('Distribuição de Peso das Apreensões (até o percentil 99)')
        ax.set_xlabel('Peso (Kg) [escala log]')
        ax.set_ylabel('Frequência')
    else:
        ax.text(0.5, 0.5, 'Não há dados de peso > 0 para exibir.', horizontalalignment='center',
                verticalalignment='center', transform=ax.transAxes, fontsize=12, color='gray')
        ax.set_title('Distribuição de Peso das Apreensões')
        ax.set_xlabel('Peso (Kg)')
        ax.set_ylabel('Frequência')


def municipio_entorpecente(df, ax=None):
    if ax is None:
        ax = plt.gca()
    top_municipios = df['Municipio'].value_counts().head(10)
    sns.barplot(x=top_municipios.values, y=top_municipios.index, ax=ax)
    ax.set_title('Top 10 Municípios com Mais Apreensões de Entorpecentes')
    ax.set_xlabel('Ocorrencias')
    ax.set_ylabel('Município')


def ais_entorpecente(df, ax=None):
    if ax is None:
        ax = plt.gca()
    sns.countplot(data=df, y='AIS', order=df['AIS'].value_counts().index, ax=ax)
    ax.set_title('Apreensões por Área Integrada de Segurança (AIS)')
    ax.set_xlabel('Ocorrencias')
    ax.set_ylabel('AIS')


def ano_entorpecente(df, ax=None):
    if ax is None:
        ax = plt.gca()
    df['Ano'] = df['Data'].dt.year
    sns.countplot(data=df, x='Ano', ax=ax)
    ax.set_title('Apreensões por Ano')
    ax.set_xlabel('Ano')
    ax.set_ylabel('Ocorrencias')


def mes_entorpecente(df, ax=None):
    if ax is None:
        ax = plt.gca()
    df['Mês'] = df['Data'].dt.month
    sns.countplot(data=df, x='Mês', ax=ax)
    ax.set_title('Apreensões por Mês')
    ax.set_xlabel('Mês')
    ax.set_ylabel('Ocorrencias')


def dia_semana_entorpecente(df, ax=None):
    if ax is None:
        ax = plt.gca()
    dias_ordem = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']
    sns.countplot(data=df, x='Dia da Semana', order=dias_ordem, ax=ax)
    ax.set_title('Apreensões por Dia da Semana')
    ax.set_xlabel('Dia da Semana')
    ax.set_ylabel('Ocorrencias')
    ax.tick_params(axis='x', rotation=45)


def horario_entorpecente(df, ax=None):
    if ax is None:
        ax = plt.gca()
    df = df.copy()
    df['Hora'] = df['Hora'].astype(str).str[:2]
    df = df[df['Hora'].str.isdigit()]
    df['Hora'] = df['Hora'].astype(int)
    sns.countplot(data=df, x='Hora', order=sorted(df['Hora'].unique()), ax=ax)
    ax.set_title('Apreensões por Hora do Dia')
    ax.set_xlabel('Hora (24h)')
    ax.set_ylabel('Ocorrencias')