import pandas as pd

# Matplotlib para criar gráficos e visualizações básicas
import matplotlib.pyplot as plt

# Seaborn para criar gráficos estatísticos com estilo bonito e fácil
import seaborn as sns

# Importar dados de Crimes Violentos Excel
from leitura_dados import carregar_crimes_violentos

# Funções para criar gráficos
def meio_empregado_cv(df, ax=None):
    if ax is None:
        ax = plt.gca()
    sns.countplot(y='Meio Empregado', data=df, order=df['Meio Empregado'].value_counts().index, ax=ax)
    ax.set_title('Distribuição dos Meios Empregados')
    ax.set_xlabel('Quantidade')
    ax.set_ylabel('Meio Empregado')

def natureza_cv(df, ax=None):
    if ax is None:
        ax = plt.gca()
    sns.countplot(y='Natureza', data=df, order=df['Natureza'].value_counts().index, ax=ax)
    ax.set_title('Natureza dos Crimes Violentos')
    ax.set_xlabel('Quantidade')
    ax.set_ylabel('Natureza')

def genero_cv(df, ax=None):
    if ax is None:
        ax = plt.gca()
    sns.countplot(x='Gênero', data=df, order=df['Gênero'].value_counts().index, ax=ax)
    ax.set_title('Gênero das Vítimas')
    ax.set_xlabel('Gênero')
    ax.set_ylabel('Quantidade')

def raca_cv(df, ax=None):
    if ax is None:
        ax = plt.gca()
    sns.countplot(x='Raça da Vítima', data=df, order=df['Raça da Vítima'].value_counts().index, ax=ax)
    ax.set_title('Raça das Vítimas')
    ax.set_xlabel('Raça')
    ax.set_ylabel('Quantidade')

def idade_cv(df, ax=None):
    if ax is None:
        ax = plt.gca()
    sns.countplot(y='Idade da Vítima', data=df, order=df['Idade da Vítima'].value_counts().index, ax=ax)
    ax.set_title('Idade das Vítimas')
    ax.set_xlabel('Quantidade')
    ax.set_ylabel('Idade')

def escolaridade_cv(df, ax=None):
    if ax is None:
        ax = plt.gca()
    sns.countplot(y='Escolaridade da Vítima', data=df, order=df['Escolaridade da Vítima'].value_counts().index, ax=ax)
    ax.set_title('Escolaridade das Vítimas')
    ax.set_xlabel('Quantidade')
    ax.set_ylabel('Escolaridade')

def municipio_cv(df, ax=None):
    if ax is None:
        ax = plt.gca()
    top_municipios = df['Municipio'].value_counts().head(20)
    sns.barplot(x=top_municipios.values, y=top_municipios.index, ax=ax)
    ax.set_title('Top 20 Municípios com Mais Crimes Violentos')
    ax.set_xlabel('Quantidade')
    # ax.set_ylabel('Município') # Temporariamente removido devido a erro

def ais_cv(df, ax=None):
    if ax is None:
        ax = plt.gca()
    sns.countplot(y='AIS', data=df, order=df['AIS'].value_counts().index, ax=ax)
    ax.set_title('Distribuição por Áreas Integradas de Segurança (AIS)')
    ax.set_xlabel('Quantidade')
    ax.set_ylabel('AIS')

def ano_cv(df, ax=None):
    if ax is None:
        ax = plt.gca()
    df = df.copy()
    df['Ano'] = pd.to_datetime(df['Data'], errors='coerce').dt.year
    sns.countplot(x='Ano', data=df, order=sorted(df['Ano'].dropna().unique()), ax=ax)
    ax.set_title('Quantidade de Crimes por Ano')
    ax.set_xlabel('Ano')
    ax.set_ylabel('Quantidade')
    ax.tick_params(axis='x', rotation=45)

def mes_cv(df, ax=None):
    if ax is None:
        ax = plt.gca()
    df = df.copy()
    df['Mês'] = pd.to_datetime(df['Data'], errors='coerce').dt.month
    sns.countplot(x='Mês', data=df, order=range(1,13), ax=ax)
    ax.set_title('Quantidade de Crimes por Mês')
    ax.set_xlabel('Mês')
    ax.set_ylabel('Quantidade')

def dia_semana_cv(df, ax=None):
    if ax is None:
        ax = plt.gca()
    dias_ordem = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
    sns.countplot(x='Dia da Semana', data=df, order=dias_ordem, ax=ax)
    ax.set_title('Quantidade de Crimes por Dia da Semana')
    ax.set_xlabel('Dia da Semana')
    ax.set_ylabel('Quantidade')

def horario_cv(df, ax=None):
    if ax is None:
        ax = plt.gca()
    df = df.copy()
    df['Hora'] = pd.to_datetime(df['Hora'], errors='coerce').dt.hour
    sns.countplot(x='Hora', data=df, ax=ax)
    ax.set_title('Distribuição dos Crimes por Horário')
    ax.set_xlabel('Hora do Dia')
    ax.set_ylabel('Quantidade')
