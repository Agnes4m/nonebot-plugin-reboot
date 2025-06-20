from nonebot import get_driver
from pydantic import BaseModel
from nonebot import get_plugin_config

class ConfigModel(BaseModel):
    reboot_load_command: bool = True
    reboot_grace_time_limit: int = 20

    class Config:
        extra = "ignore"


global_config = get_driver().config
try:
    plugin_config = ConfigModel(**global_config.model_dump())
except AttributeError:
    plugin_config = ConfigModel(**global_config.dict())
config = get_plugin_config(ConfigModel)
