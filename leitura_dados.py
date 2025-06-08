# Pandas para análise e manipulação de dados
import pandas as pd
import numpy as np

# Unicodedata para normalização de strings
import unicodedata


# Função para limpar os colunas dos arquivos Excel
def limpar_colunas(df):
    """Limpa os nomes das colunas e valores removendo espaços extras e acentos"""
    if df is None:
        return None
        
    # Limpar nomes das colunas
    df.columns = [unicodedata.normalize('NFKD', str(col)).encode('ASCII', 'ignore').decode('ASCII').strip() 
                 for col in df.columns]
    
    # Limpar valores nas colunas
    for col in df.columns:
        if df[col].dtype == 'object':  # Apenas para colunas de texto
            df[col] = df[col].apply(lambda x: str(x).strip() if pd.notnull(x) else x)
    
    return df


# Função para carregar e limpar o arquivo Entorpecentes Excel
def carregar_entorpecentes(caminho='Entorpecente_2009-a-2024.xlsx'):
    """Carrega e limpa os dados de entorpecentes"""
    try:
        print(f"\nCarregando dados de entorpecentes de {caminho}...")
        df = pd.read_excel(caminho)
        df = limpar_colunas(df)
        df = tratar_dados(df)
        df = validar_dados(df)
        return df
    except Exception as e:
        print(f"Erro ao carregar dados de entorpecentes: {str(e)}")
        return None


# Função para carregar e limpar o arquivo Crimes Violentos Excel
def carregar_crimes_violentos(caminho='CVLI_2009-2024.xlsx'):
    """Carrega e limpa os dados de crimes violentos"""
    try:
        print(f"\nCarregando dados de crimes violentos de {caminho}...")
        df = pd.read_excel(caminho)
        df = limpar_colunas(df)
        df = tratar_dados(df)
        df = validar_dados(df)
        return df
    except Exception as e:
        print(f"Erro ao carregar dados de crimes violentos: {str(e)}")
        return None

# Função para carregar e limpar o arquivo Crimes Sexuais Excel
def carregar_crimes_sexuais(caminho='Crimes-Sexuais_2009-a-2024.xlsx'):
    """Carrega e limpa os dados de crimes sexuais"""
    try:
        print(f"\nCarregando dados de crimes sexuais de {caminho}...")
        df = pd.read_excel(caminho)
        df = limpar_colunas(df)
        df = tratar_dados(df)
        df = validar_dados(df)
        return df
    except Exception as e:
        print(f"Erro ao carregar dados de crimes sexuais: {str(e)}")
        return None

# Função para tratar valores nulos e inconsistentes
def tratar_dados(df):
    """Trata valores nulos e converte tipos de dados"""
    if df is None:
        return None
        
    # Substituir valores nulos por NaN
    df = df.replace(['', 'nan', 'NaN', 'NULL', 'null', 'None', 'none'], np.nan)
    
    # Converter colunas numéricas
    colunas_numericas = ['Peso', 'Idade']
    for col in colunas_numericas:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
    
    # Tratar datas e horas
    if 'Data' in df.columns:
        df['Data'] = pd.to_datetime(df['Data'], errors='coerce')
    
    if 'Hora' in df.columns:
        # Tentar diferentes formatos de hora
        def converter_hora(hora):
            if pd.isna(hora) or str(hora).strip().lower() == 'nan':
                return np.nan
            try:
                # Tentar converter diretamente, o pandas pode inferir
                return pd.to_datetime(hora).time()
            except Exception as e:
                try:
                    # Tentar formato HH:MM
                    if ':' in str(hora):
                        return pd.to_datetime(str(hora), format='%H:%M').time()
                    # Tentar formato HHMM
                    elif len(str(hora)) == 4 and str(hora).isdigit():
                        return pd.to_datetime(str(hora), format='%H%M').time()
                    # Tentar formato HH
                    elif len(str(hora)) == 2 and str(hora).isdigit():
                        return pd.to_datetime(str(hora), format='%H').time()
                    else:
                        print(f"DEBUG: Formato de hora desconhecido: '{hora}'")
                        return np.nan
                except Exception as inner_e:
                    print(f"DEBUG: Erro ao converter hora '{hora}': {e} / {inner_e}")
                    return np.nan
        
        df['Hora'] = df['Hora'].apply(converter_hora)
        
        # Calcular estatísticas dos valores nulos
        total_registros = len(df)
        registros_sem_hora = df['Hora'].isna().sum()
        percentual_sem_hora = (registros_sem_hora / total_registros) * 100
        
        print(f"\nEstatísticas da coluna Hora:")
        print(f"Total de registros: {total_registros}")
        print(f"Registros sem hora: {registros_sem_hora} ({percentual_sem_hora:.2f}%)")
    
    return df

# Função para validar dados
def validar_dados(df):
    """Valida os dados e retorna informações sobre valores nulos e únicos"""
    if df is None:
        return None
        
    print("\nValidação dos dados:")
    
    # Verificar valores nulos
    nulos = df.isnull().sum()
    if nulos.any():
        print("\nValores nulos por coluna:")
        for col, count in nulos[nulos > 0].items():
            print(f"{col}: {count} valores nulos")
    
    # Verificar valores únicos
    print("\nValores únicos por coluna:")
    for col in df.columns:
        n_unicos = df[col].nunique()
        print(f"{col}: {n_unicos} valores únicos")
    
    return df
