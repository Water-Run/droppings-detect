r"""
:author: WaterRun
:time: 2025-05-06
:file: image.py
:description: 排泄物检测配置
"""


class Config:
    r"""
    配置
    """

    @staticmethod
    def get_model() -> str:
        r"""
        返回模型路径
        :return: 模型路径
        """
        return ""

    @staticmethod
    def get_config() -> dict:
        r"""
        返回配置
        :return: 配置
        """
        return {}

    @staticmethod
    def show() -> None:
        r"""
        输出配置
        :return: None
        """
        print(f"")
