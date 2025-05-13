r"""
:author: WaterRun
:time: 2025-05-10
:file: config.py
:description: 排泄物检测配置
"""

import os

# 默认模型路径（在包内model目录）
DEFAULT_MODEL_PATH = os.path.join(os.path.dirname(__file__), "model", "best.pt")

# 检测阈值
CONFIDENCE_THRESHOLD = 0.5

# 处理图像时的默认大小
IMAGE_SIZE = 640
