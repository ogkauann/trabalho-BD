import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                            QHBoxLayout, QPushButton, QLabel, QStackedWidget,
                            QScrollArea, QFrame, QMessageBox, QProgressDialog, QSpacerItem, QSizePolicy)
from PyQt6.QtCore import Qt, QSize, QTimer
from PyQt6.QtGui import QFont, QIcon, QPixmap
from qt_material import apply_stylesheet
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import seaborn as sns
import traceback

from leitura_dados import (
    carregar_entorpecentes,
    carregar_crimes_violentos,
    carregar_crimes_sexuais,
)
from entorpecentes import (
    tipo_entorpecente,
    peso_entorpecente,
    municipio_entorpecente,
    ais_entorpecente,
    ano_entorpecente,
    mes_entorpecente,
    dia_semana_entorpecente,
    horario_entorpecente,
)
from crimes_violentos import (
    meio_empregado_cv,
    natureza_cv,
    genero_cv,
    raca_cv,
    idade_cv,
    escolaridade_cv,
    municipio_cv,
    ais_cv,
    ano_cv,
    mes_cv,
    dia_semana_cv,
    horario_cv,
)
from crimes_sexuais import (
    genero_cs,
    raca_cs,
    idade_cs,
    escolaridade_cs,
    municipio_cs,
    ais_cs,
    ano_cs,
    mes_cs,
    dia_semana_cs,
    horario_cs,
)

class GraficoWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.figure = Figure(figsize=(8, 6))
        self.canvas = FigureCanvas(self.figure)
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)
        
        # Configurar estilo do seaborn
        sns.set_style("whitegrid")
        sns.set_palette("husl")
        
        # Configurar fonte padrão
        plt.rcParams['font.family'] = 'Arial'
        plt.rcParams['font.size'] = 10

    def plotar_grafico(self, funcao, *args):
        try:
            self.figure.clear()
            ax = self.figure.add_subplot(111)
            
            # Verificar se os dados são válidos
            if len(args) > 0 and args[0] is None:
                raise ValueError("Dados não disponíveis")
            
            # Plotar o gráfico
            funcao(*args, ax=ax)
            
            # Ajustar layout
            self.figure.tight_layout()
            self.canvas.draw()
            
        except Exception as e:
            print(f"DEBUG: Tipo do erro: {type(e)}")
            print(f"DEBUG: Valor do erro: {e}")
            error_message = f"Erro ao gerar gráfico: {str(e)}"
            detailed_error = traceback.format_exc()
            QMessageBox.critical(self, "Erro", f"{error_message}\n\nDetalhes:\n{detailed_error}")
            # Limpar a figura em caso de erro
            self.figure.clear()
            self.canvas.draw()

class MenuButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setMinimumHeight(50)
        self.setFont(QFont('Arial', 12, QFont.Weight.Bold))
        self.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                border: none;
                border-radius: 12px;
                padding: 10px;
                margin: 5px;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
            QPushButton:pressed {
                background-color: #0D47A1;
            }
            QPushButton:disabled {
                background-color: #BDBDBD;
            }
        """)

class InfoLabel(QLabel):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setFont(QFont('Arial', 10))
        self.setStyleSheet("""
            QLabel {
                color: #666;
                padding: 5px;
            }
        """)
        self.setWordWrap(True)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Análise de Criminalidade no Ceará")
        self.setMinimumSize(1200, 800)
        self.setWindowIcon(QIcon("logo_ceara.png"))
        
        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout principal
        layout = QHBoxLayout(central_widget)
        central_widget.setStyleSheet("""
            QWidget {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #e3f2fd, stop:1 #bbdefb);
            }
        """)
        
        # Menu lateral
        menu_frame = QFrame()
        menu_frame.setMaximumWidth(300)
        menu_frame.setStyleSheet("""
            QFrame {
                background-color: #f5f5f5;
                border-right: 1px solid #ddd;
                border-radius: 18px;
            }
        """)
        menu_layout = QVBoxLayout(menu_frame)
        
        # Logo do Ceará
        logo_label = QLabel()
        logo_pixmap = QPixmap("logo_ceara.png")
        logo_pixmap = logo_pixmap.scaledToWidth(120, Qt.TransformationMode.SmoothTransformation)
        logo_label.setPixmap(logo_pixmap)
        logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        menu_layout.addWidget(logo_label)
        
        # Separador visual
        separador = QFrame()
        separador.setFrameShape(QFrame.Shape.HLine)
        separador.setFrameShadow(QFrame.Shadow.Sunken)
        separador.setStyleSheet("color: #bdbdbd; margin: 8px 0;")
        menu_layout.addWidget(separador)
        
        # Título destacado
        titulo = QLabel("Análise de Criminalidade")
        titulo.setFont(QFont('Arial', 18, QFont.Weight.Bold))
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titulo.setStyleSheet("color: #1976D2;")
        menu_layout.addWidget(titulo)
        
        # Informações
        info = InfoLabel("Este aplicativo permite analisar dados de criminalidade no Ceará, incluindo apreensões de entorpecentes, crimes violentos e crimes sexuais.")
        menu_layout.addWidget(info)
        
        # Botões do menu
        self.btn_entorpecentes = MenuButton("ENTORPECENTES")
        self.btn_crimes_violentos = MenuButton("CRIMES VIOLENTOS")
        self.btn_crimes_sexuais = MenuButton("CRIMES SEXUAIS")
        
        menu_layout.addWidget(self.btn_entorpecentes)
        menu_layout.addWidget(self.btn_crimes_violentos)
        menu_layout.addWidget(self.btn_crimes_sexuais)
        menu_layout.addStretch()
        
        # Rodapé discreto
        rodape = QLabel("Desenvolvido para análise de dados públicos do Ceará • 2024")
        rodape.setAlignment(Qt.AlignmentFlag.AlignCenter)
        rodape.setStyleSheet("color: #aaa; font-size: 10px; margin-bottom: 8px;")
        menu_layout.addWidget(rodape)
        
        # Área de conteúdo
        self.stacked_widget = QStackedWidget()
        self.grafico_widget = GraficoWidget()
        self.stacked_widget.addWidget(self.grafico_widget)
        self.stacked_widget.setStyleSheet("""
            QStackedWidget {
                border-radius: 18px;
                background: transparent;
            }
        """)
        
        # Adicionar widgets ao layout principal
        layout.addWidget(menu_frame)
        layout.addWidget(self.stacked_widget)
        
        # Conectar sinais
        self.btn_entorpecentes.clicked.connect(self.mostrar_menu_entorpecentes)
        self.btn_crimes_violentos.clicked.connect(self.mostrar_menu_crimes_violentos)
        self.btn_crimes_sexuais.clicked.connect(self.mostrar_menu_crimes_sexuais)
        
        # Carregar dados após um pequeno delay para garantir que a interface esteja pronta
        QTimer.singleShot(100, self.carregar_dados)

    def _show_graph(self, plot_function, df):
        self.grafico_widget.plotar_grafico(plot_function, df)
        self.stacked_widget.setCurrentWidget(self.grafico_widget)

    def carregar_dados(self):
        try:
            # Criar diálogo de progresso
            progress = QProgressDialog("Carregando dados...", "Cancelar", 0, 3, self)
            progress.setWindowModality(Qt.WindowModality.WindowModal)
            progress.setWindowTitle("Carregando")
            progress.setMinimumDuration(0)
            
            # Carregar dados de entorpecentes
            progress.setLabelText("Carregando dados de entorpecentes...")
            self.df_entorpecentes = carregar_entorpecentes()
            progress.setValue(1)
            
            if progress.wasCanceled():
                return
                
            # Carregar dados de crimes violentos
            progress.setLabelText("Carregando dados de crimes violentos...")
            self.df_crimes_violentos = carregar_crimes_violentos()
            progress.setValue(2)
            
            if progress.wasCanceled():
                return
                
            # Carregar dados de crimes sexuais
            progress.setLabelText("Carregando dados de crimes sexuais...")
            self.df_crimes_sexuais = carregar_crimes_sexuais()
            progress.setValue(3)
            
            # Verificar se os dados foram carregados corretamente
            if self.df_entorpecentes is None:
                self.btn_entorpecentes.setEnabled(False)
                QMessageBox.warning(self, "Aviso", "Não foi possível carregar os dados de entorpecentes.")
            
            if self.df_crimes_violentos is None:
                self.btn_crimes_violentos.setEnabled(False)
                QMessageBox.warning(self, "Aviso", "Não foi possível carregar os dados de crimes violentos.")
            
            if self.df_crimes_sexuais is None:
                self.btn_crimes_sexuais.setEnabled(False)
                QMessageBox.warning(self, "Aviso", "Não foi possível carregar os dados de crimes sexuais.")
            
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao carregar dados: {str(e)}\n\nDetalhes:\n{traceback.format_exc()}")
            print(f"Erro ao carregar dados: {str(e)}")
            print("Detalhes do erro:")
            traceback.print_exc()

    def mostrar_menu_entorpecentes(self):
        if self.df_entorpecentes is None:
            QMessageBox.warning(self, "Aviso", "Dados de entorpecentes não disponíveis.")
            return
            
        menu = QWidget()
        layout = QVBoxLayout(menu)
        
        # Título
        titulo = QLabel("Análise de Entorpecentes")
        titulo.setFont(QFont('Arial', 14, QFont.Weight.Bold))
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(titulo)
        
        # Informações
        info = InfoLabel("Selecione uma opção para visualizar a análise de apreensões de entorpecentes no Ceará.")
        layout.addWidget(info)
        
        botoes = [
            ("Tipos de Entorpecentes", lambda: self._show_graph(tipo_entorpecente, self.df_entorpecentes)),
            ("Peso", lambda: self._show_graph(peso_entorpecente, self.df_entorpecentes)),
            ("Município", lambda: self._show_graph(municipio_entorpecente, self.df_entorpecentes)),
            ("AIS", lambda: self._show_graph(ais_entorpecente, self.df_entorpecentes)),
            ("Ano", lambda: self._show_graph(ano_entorpecente, self.df_entorpecentes)),
            ("Mês", lambda: self._show_graph(mes_entorpecente, self.df_entorpecentes)),
            ("Dia da Semana", lambda: self._show_graph(dia_semana_entorpecente, self.df_entorpecentes)),
            ("Horário", lambda: self._show_graph(horario_entorpecente, self.df_entorpecentes))
        ]
        
        for texto, funcao in botoes:
            btn = MenuButton(texto)
            btn.clicked.connect(funcao)
            layout.addWidget(btn)
        
        layout.addStretch()
        self.stacked_widget.addWidget(menu)
        self.stacked_widget.setCurrentWidget(menu)

    def mostrar_menu_crimes_violentos(self):
        if self.df_crimes_violentos is None:
            QMessageBox.warning(self, "Aviso", "Dados de crimes violentos não disponíveis.")
            return
            
        menu = QWidget()
        layout = QVBoxLayout(menu)
        
        # Título
        titulo = QLabel("Análise de Crimes Violentos")
        titulo.setFont(QFont('Arial', 14, QFont.Weight.Bold))
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(titulo)
        
        # Informações
        info = InfoLabel("Selecione uma opção para visualizar a análise de crimes violentos no Ceará.")
        layout.addWidget(info)
        
        botoes = [
            ("Meio Empregado", lambda: self._show_graph(meio_empregado_cv, self.df_crimes_violentos)),
            ("Natureza", lambda: self._show_graph(natureza_cv, self.df_crimes_violentos)),
            ("Gênero", lambda: self._show_graph(genero_cv, self.df_crimes_violentos)),
            ("Raça", lambda: self._show_graph(raca_cv, self.df_crimes_violentos)),
            ("Idade", lambda: self._show_graph(idade_cv, self.df_crimes_violentos)),
            ("Escolaridade", lambda: self._show_graph(escolaridade_cv, self.df_crimes_violentos)),
            ("Município", lambda: self._show_graph(municipio_cv, self.df_crimes_violentos)),
            ("AIS", lambda: self._show_graph(ais_cv, self.df_crimes_violentos)),
            ("Ano", lambda: self._show_graph(ano_cv, self.df_crimes_violentos)),
            ("Mês", lambda: self._show_graph(mes_cv, self.df_crimes_violentos)),
            ("Dia da Semana", lambda: self._show_graph(dia_semana_cv, self.df_crimes_violentos)),
            ("Horário", lambda: self._show_graph(horario_cv, self.df_crimes_violentos))
        ]
        
        for texto, funcao in botoes:
            btn = MenuButton(texto)
            btn.clicked.connect(funcao)
            layout.addWidget(btn)
        
        layout.addStretch()
        self.stacked_widget.addWidget(menu)
        self.stacked_widget.setCurrentWidget(menu)

    def mostrar_menu_crimes_sexuais(self):
        if self.df_crimes_sexuais is None:
            QMessageBox.warning(self, "Aviso", "Dados de crimes sexuais não disponíveis.")
            return
            
        menu = QWidget()
        layout = QVBoxLayout(menu)
        
        # Título
        titulo = QLabel("Análise de Crimes Sexuais")
        titulo.setFont(QFont('Arial', 14, QFont.Weight.Bold))
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(titulo)
        
        # Informações
        info = InfoLabel("Selecione uma opção para visualizar a análise de crimes sexuais no Ceará.")
        layout.addWidget(info)
        
        botoes = [
            ("Gênero", lambda: self._show_graph(genero_cs, self.df_crimes_sexuais)),
            ("Raça", lambda: self._show_graph(raca_cs, self.df_crimes_sexuais)),
            ("Idade", lambda: self._show_graph(idade_cs, self.df_crimes_sexuais)),
            ("Escolaridade", lambda: self._show_graph(escolaridade_cs, self.df_crimes_sexuais)),
            ("Município", lambda: self._show_graph(municipio_cs, self.df_crimes_sexuais)),
            ("AIS", lambda: self._show_graph(ais_cs, self.df_crimes_sexuais)),
            ("Ano", lambda: self._show_graph(ano_cs, self.df_crimes_sexuais)),
            ("Mês", lambda: self._show_graph(mes_cs, self.df_crimes_sexuais)),
            ("Dia da Semana", lambda: self._show_graph(dia_semana_cs, self.df_crimes_sexuais)),
            ("Horário", lambda: self._show_graph(horario_cs, self.df_crimes_sexuais))
        ]
        
        for texto, funcao in botoes:
            btn = MenuButton(texto)
            btn.clicked.connect(funcao)
            layout.addWidget(btn)
        
        layout.addStretch()
        self.stacked_widget.addWidget(menu)
        self.stacked_widget.setCurrentWidget(menu)

def main():
    try:
        app = QApplication(sys.argv)
        
        # Configurar estilo
        apply_stylesheet(app, theme='light_blue.xml')
        
        # Criar janela principal
        window = MainWindow()
        
        # Mostrar janela
        window.show()
        
        # Iniciar aplicação
        sys.exit(app.exec())
        
    except Exception as e:
        print(f"Erro ao iniciar a aplicação: {str(e)}")
        print("Detalhes do erro:")
        traceback.print_exc()
        input("Pressione Enter para sair...") 