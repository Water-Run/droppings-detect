r"""
:author: WaterRun
:time: 2025-05-12
:file: image.py
:description: 排泄物图像检测
"""

import os
import cv2
import numpy as np
from pathlib import Path
from ultralytics import YOLO

from .result import Result
from .config import DEFAULT_MODEL_PATH, CONFIDENCE_THRESHOLD

# 懒加载模型
_model = None


def _load_model(model_path: str | None = None) -> YOLO:
    """
    加载YOLO模型

    Args:
        model_path: 模型路径，如果为None，使用默认路径
    """
    global _model
    if _model is not None:
        return _model

    if model_path is None:
        model_path = DEFAULT_MODEL_PATH

    model_path = Path(model_path)
    if not model_path.exists():
        raise FileNotFoundError(f"模型文件不存在: {model_path}")

    _model = YOLO(str(model_path))
    return _model


def detect(image_path: str, model_path: str | None = None,
           conf_threshold: float = CONFIDENCE_THRESHOLD) -> list[Result]:
    r"""
    识别单张图像中的动物排泄物

    Args:
        image_path: 识别的图片路径
        model_path: 模型路径，如果为None，使用默认路径
        conf_threshold: 检测置信度阈值

    Returns:
        结果Result列表
    """
    if not isinstance(image_path, str):
        raise ValueError('图像检测接收到了不合法的输入值')

    img_path = Path(image_path)
    if not img_path.exists():
        raise FileNotFoundError(f"图像文件不存在: {img_path}")

    # 加载模型
    model = _load_model(model_path)

    # 读取图像
    img = cv2.imread(str(img_path))
    if img is None:
        raise ValueError(f"无法读取图像: {img_path}")

    # 执行检测
    results = model(img, conf=conf_threshold)[0]

    # 解析结果
    detection_results: list[Result] = []
    for detection in results.boxes.data.cpu().numpy():
        x1, y1, x2, y2, confidence, class_id = detection
        detection_results.append(
            Result(
                up_left=(int(x1), int(y1)),
                down_right=(int(x2), int(y2)),
                confidence=float(confidence)
            )
        )

    return detection_results
