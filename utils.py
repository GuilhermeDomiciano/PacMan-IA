def get_user_input(prompt):
    """Captura entrada do usuário de forma segura."""
    try:
        return input(prompt)
    except KeyboardInterrupt:
        print("\nJogo encerrado.")
        exit()
