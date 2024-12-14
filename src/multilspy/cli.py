from multilspy import SyncLanguageServer
from multilspy.multilspy_config import MultilspyConfig
from multilspy.multilspy_logger import MultilspyLogger

def main(lang: str):
    """Entry point for the multilspy-init command."""
    print(f"Initializing Multilspy for {lang}")
    config = MultilspyConfig.from_dict({"code_language": lang})
    logger = MultilspyLogger()
    SyncLanguageServer.create(config, logger, ".")
    print(f"Multilspy for {lang} initialized successfully")

if __name__ == "__main__":
    main() 