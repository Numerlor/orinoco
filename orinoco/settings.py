from pydantic_settings import BaseSettings


class Config(BaseSettings):
    IMPLICIT_TYPE_STRICT_MODE_ENABLED: bool = False
    CHAINING_TYPE_CHECK_STRICT_MODE_ENABLED: bool = False
    VERBOSE_ERRORS: bool = False

    class Config:
        env_prefix = "ORINOCO_"
