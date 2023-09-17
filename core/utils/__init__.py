

def env_to_bool(value:str) -> bool:
    if not value : return False
    return (lambda V: True if V != '0' else False)(value)
