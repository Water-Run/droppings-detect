r"""
:author: WaterRun
:time: 2025-05-10
:file: result.py
:description: 检测结果封装
"""


class Result:
    r"""
    单个结果封装.一但创建,不可重写

    :param up_left: 检测结果的左上角坐标
    :param down_right: 检测结果的右下角坐标
    :param confidence: 检测结果的置信度
    """

    def __init__(self, up_left: (int, int), down_right: (int, int), confidence: float):
        self._up_left = up_left
        self._down_right = down_right
        self._confidence = confidence

    def __repr__(self):
        return (f"droppings-detect result: \n"
                f"  up_left: {self._up_left}\n"
                f"  down_right: {self._down_right}\n"
                f"  confidence: {self._confidence:.2f}")

    @property
    def up_left(self) -> (int, int):
        """获取左上角坐标"""
        return self._up_left

    @property
    def down_right(self) -> (int, int):
        """获取右下角坐标"""
        return self._down_right

    @property
    def confidence(self) -> float:
        """获取置信度"""
        return self._confidence

    def __setattr__(self, name: str, value: any) -> None:
        r"""
        禁止修改 Result 的属性。
        :raises AttributeError: 如果尝试修改已存在的属性
        """
        if hasattr(self, name):
            raise AttributeError(f"不可修改属性`{name}`: Result类是不可变的")
        super().__setattr__(name, value)

    def __delattr__(self, name: str) -> None:
        r"""
        禁止删除 Result 的属性。
        :raises AttributeError: 如果尝试删除属性
        """
        raise AttributeError(f"不可删除属性`{name}`: Result类是不可变的")
