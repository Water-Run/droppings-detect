r"""
:author: WaterRun
:time: 2025-05-06
:file: result.py
:description: 检测结果封装
"""


class Result:
    r"""

    """

    def __init__(self, up_left: int, down_right: int, confidence: float):
        self.up_left = up_left
        self.down_right = down_right
        self.confidence = confidence

    def __repr__(self):
        return (f"droppings-detect result: \n"
                f"")
