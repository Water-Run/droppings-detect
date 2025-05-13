r"""
:author: WaterRun
:time: 2025-05-10
:file: video.py
:description: 排泄物视频检测
"""

import cv2
from pathlib import Path
from collections.abc import Generator

from .result import Result
from .config import DEFAULT_MODEL_PATH, CONFIDENCE_THRESHOLD
from .image import _load_model


def detect(video_path: str, frame_interval: int = 60, model_path: str | None = None,
           conf_threshold: float = CONFIDENCE_THRESHOLD) -> Generator[list[Result], None, None]:
    r"""
    识别视频中的动物排泄物(yield结果)

    Args:
        video_path: 识别的视频路径
        frame_interval: 检测间隔的帧数，0表示每一帧都检测
        model_path: 模型路径，如果为None，使用默认路径
        conf_threshold: 检测置信度阈值

    Yields:
        Result对象列表，每个列表对应一帧的检测结果
    """
    if not (isinstance(video_path, str) and isinstance(frame_interval, int) and frame_interval >= 0):
        raise ValueError('视频检测接收到了不合法的输入值')

    video_path = Path(video_path)
    if not video_path.exists():
        raise FileNotFoundError(f"视频文件不存在: {video_path}")

    # 加载模型
    model = _load_model(model_path)

    # 打开视频
    cap = cv2.VideoCapture(str(video_path))
    if not cap.isOpened():
        raise ValueError(f"无法打开视频: {video_path}")

    frame_count = 0

    try:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # 只在指定的帧间隔处理
            if frame_interval == 0 or frame_count % frame_interval == 0:
                # 执行检测
                results = model(frame, conf=conf_threshold)[0]

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

                yield detection_results

            frame_count += 1

    finally:
        cap.release()
