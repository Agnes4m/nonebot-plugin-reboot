from .config import plugin_config, ConfigModel
from nonebot.plugin import PluginMetadata
from .reloader import Reloader

__version__ = "0.1.2"
__plugin_meta__ = PluginMetadata(
    name="nonebot_plugin_reboot [重启 bot]",
    description="用命令重启机器人",
    usage="",
    type="application",
    homepage="https://github.com/18870/nonebot-plugin-reboot",
    config=ConfigModel,
    supported_adapters={"~onebot.v11"},
    extra={
        "version": __version__,
        "author": ["18870 <a20110123@163.com>", "Agnes4m <Z735803792@163.com>"],
    },
)

if plugin_config.reboot_load_command:
    from .command import reboot_matcher