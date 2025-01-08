try:
    from colorama import init, Fore, Back, Style
    init(autoreset=True)
except ImportError:
    class ColorFallback:
        def __getattr__(self, name):
            return ''

    Fore = ColorFallback()
    Back = ColorFallback()
    Style = ColorFallback()


def convert_comma_to_dot(value):
    return value.replace(',', '.')


def detail_prod(product, show_id=False):
    print(f"{Fore.BLUE}Detalhes do produto:")
    keys = [k for k in product.__dict__.keys() if k != 'id']
    values = [v for v in product.__dict__.values() if v !=
              product.id]
    for k, v in zip(keys, values):
        print(f"{Fore.CYAN}{k}:{Fore.LIGHTGREEN_EX}{
              " R$ " if k == 'preco' else " "}"+Style.RESET_ALL+f"{v}")
    if show_id:
        print(f"{Fore.MAGENTA}id: "+Style.RESET_ALL+f"{product.id}")


def is_not_empty(value):
    return bool(value and value.strip())


def is_valid_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def is_valid_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def request_input(mensagem, tipo, obrigatorio=True):
    while True:
        entrada = input(mensagem)
        if obrigatorio and not is_not_empty(entrada):
            print(f"{Fore.RED}Erro: Campo obrigatório não pode ser vazio.")
            continue
        if len(entrada) != 0:
            if tipo == 'int' and not is_valid_integer(entrada):
                print(f"{Fore.RED}Erro: Deve ser um número inteiro.")
                continue
            if tipo == 'float' and not is_valid_float(convert_comma_to_dot(entrada)):
                print(f"{Fore.RED}Erro: Deve ser um número decimal.")
                continue
        return entrada


def truncate_string(string, max_length):
    return string if len(string) <= max_length else string[:max_length - 3] + '...'


def wait_to_continue():
    input(f"\n{Fore.LIGHTBLUE_EX}Pressione [enter] para continuar...")
