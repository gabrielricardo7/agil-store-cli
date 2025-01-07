def convert_comma_to_dot(value):
    return value.replace(',', '.')


def truncate_string(string, max_length):
    return string if len(string) <= max_length else string[:max_length - 3] + '...'


def wait_to_continue():
    input("\nPressione [enter] para continuar...")
