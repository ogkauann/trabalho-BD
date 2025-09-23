# 📊 Sistema de Análise de Criminalidade no Ceará

Um sistema completo para análise e visualização de dados de criminalidade no estado do Ceará, desenvolvido em Python com interface gráfica moderna.

## 🎯 Sobre o Projeto

Este projeto foi desenvolvido como parte de um trabalho de Big Data para analisar estatísticas criminais no Ceará entre 2009-2024. O sistema permite visualizar e analisar três categorias principais de dados:

- **Apreensão de Entorpecentes** (2009-2024)
- **Crimes Violentos Letais Intencionais - CVLI** (2009-2024)  
- **Crimes Sexuais** (2009-2024)

## 🚀 Funcionalidades

### 📈 Análises de Entorpecentes
- Distribuição por tipo de entorpecente
- Análise de peso das apreensões
- Distribuição geográfica (municípios e AIS)
- Análises temporais (ano, mês, dia da semana, horário)

### 🔍 Análises de Crimes Violentos
- Meios empregados nos crimes
- Natureza dos crimes violentos
- Perfil demográfico das vítimas (gênero, raça, idade, escolaridade)
- Distribuição geográfica e temporal

### 👥 Análises de Crimes Sexuais
- Perfil das vítimas
- Distribuição geográfica
- Padrões temporais
- Análises demográficas

### 🖥️ Interface Gráfica
- Interface moderna com PyQt6
- Tema Material Design
- Gráficos interativos com Matplotlib e Seaborn
- Navegação intuitiva entre diferentes análises

## 🛠️ Tecnologias Utilizadas

### Linguagem
- **Python 3.x**

### Bibliotecas Principais
- **PyQt6** - Interface gráfica moderna
- **qt-material** - Tema Material Design
- **pandas** - Manipulação e análise de dados
- **matplotlib** - Criação de gráficos
- **seaborn** - Visualizações estatísticas estilizadas
- **openpyxl** - Leitura de arquivos Excel
- **numpy** - Computação numérica

## 📋 Pré-requisitos

- Python 3.7 ou superior
- Pip (gerenciador de pacotes Python)

## ⚙️ Instalação

1. **Clone ou baixe o projeto:**
   ```bash
   git clone [URL_DO_REPOSITORIO]
   cd trabalho-BD-main
   ```

2. **Instale as dependências:**
   ```bash
   pip install pandas matplotlib seaborn openpyxl PyQt6 qt-material numpy
   ```

3. **Verifique se os arquivos Excel estão no diretório:**
   - `Entorpecente_2009-a-2024.xlsx`
   - `CVLI_2009-2024.xlsx`
   - `Crimes-Sexuais_2009-a-2024.xlsx`

## 🚀 Como Executar

Execute o arquivo principal:
```bash
python main.py
```

A interface gráfica será aberta com o menu principal permitindo navegar entre as diferentes análises.

## 📁 Estrutura do Projeto

```
trabalho-BD-main/
│
├── main.py                          # Arquivo principal
├── interface.py                     # Interface gráfica PyQt6
├── leitura_dados.py                 # Módulo para carregamento e limpeza dos dados
├── entorpecentes.py                 # Análises específicas de entorpecentes
├── crimes_violentos.py              # Análises de crimes violentos
├── crimes_sexuais.py                # Análises de crimes sexuais
│
├── Entorpecente_2009-a-2024.xlsx    # Dados de entorpecentes
├── CVLI_2009-2024.xlsx              # Dados de crimes violentos
├── Crimes-Sexuais_2009-a-2024.xlsx  # Dados de crimes sexuais
│
└── __pycache__/                     # Cache Python (gerado automaticamente)
```

## 📊 Tipos de Visualizações

### Gráficos Disponíveis
- **Gráficos de Barras** - Distribuições categóricas
- **Histogramas** - Distribuições numéricas
- **Gráficos de Linha** - Séries temporais
- **Gráficos de Pizza** - Proporções
- **Mapas de Calor** - Correlações

### Análises Temporais
- Tendências anuais (2009-2024)
- Sazonalidade mensal
- Padrões por dia da semana
- Distribuição por horário

### Análises Geográficas
- Distribuição por município
- Análise por Área Integrada de Segurança (AIS)

## 🔧 Funcionalidades Técnicas

### Tratamento de Dados
- Limpeza automática de colunas
- Normalização de caracteres especiais
- Validação de integridade dos dados
- Tratamento de valores nulos

### Interface
- Design responsivo
- Tema escuro moderno
- Navegação por abas
- Indicadores de progresso para carregamento

## 📖 Como Usar

1. **Inicie o sistema** executando `python main.py`
2. **Selecione a categoria** de dados que deseja analisar
3. **Escolha o tipo de análise** no menu lateral
4. **Visualize os gráficos** gerados automaticamente
5. **Navegue entre diferentes visualizações** usando os botões

## 🐛 Solução de Problemas

### Erro: Módulo não encontrado
```bash
pip install [nome_do_modulo]
```

### Erro: Arquivo Excel não encontrado
Verifique se os arquivos `.xlsx` estão no mesmo diretório do projeto.

### Erro: Problemas com PyQt6
No Windows, pode ser necessário instalar:
```bash
pip install PyQt6-tools
```

## 🤝 Contribuição

Este é um projeto acadêmico. Para contribuições:

1. Faça um fork do projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📄 Licença

Este projeto é desenvolvido para fins acadêmicos e de pesquisa.

## 👥 Autores

Projeto desenvolvido como trabalho de Big Data para análise de criminalidade no Ceará.

## 📞 Suporte

Para dúvidas ou problemas, verifique:
- Se todas as dependências estão instaladas
- Se os arquivos Excel estão no diretório correto
- Se a versão do Python é compatível

---

⚡ **Desenvolvido com Python e PyQt6** - Sistema de Análise de Criminalidade no Ceará
