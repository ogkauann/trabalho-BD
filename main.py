from interface import main

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Erro ao iniciar a interface: {str(e)}")
        input("Pressione Enter para sair...")
