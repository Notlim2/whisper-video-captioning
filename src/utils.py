def load_env():
    from dotenv import load_dotenv
    import os

    load_dotenv()

def validate_file(file_path):
    import os
    
    # Remove espaços em branco no início e fim
    file_path = file_path.strip()
    
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    return True