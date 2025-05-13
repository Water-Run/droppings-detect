from setuptools import setup, find_packages
import os
from pathlib import Path

# 读取README.md文件内容作为长描述
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# 确保model目录存在
model_dir = Path("droppings_detect/model")
model_dir.mkdir(exist_ok=True, parents=True)

# 模型文件路径列表
model_files = []
if model_dir.exists():
    model_files = [str(f.relative_to("droppings_detect")) for f in model_dir.glob("*.pt")]

setup(
    name="droppings-detect",
    version="0.1.0",
    author="WaterRun",
    author_email="your.email@example.com",  # 替换为你的电子邮件
    description="识别图片或视频中的动物排泄物",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Water-Run/droppings-detect",
    packages=find_packages(),
    package_data={
        "droppings_detect": ["model/*.pt"],  # 包括模型文件
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Image Recognition",
    ],
    python_requires=">=3.12",  # 指定Python 3.12+
    install_requires=[
        "ultralytics>=8.0.0",  # YOLOv8
        "opencv-python>=4.8.0",  # 图像处理
        "numpy>=1.24.0",  # 数值计算
        "torch>=2.0.0",  # PyTorch
    ],
    extras_require={
        "train": [
            "roboflow>=1.1.0",  # 用于数据集管理
            "matplotlib>=3.7.0",  # 可视化
        ],
        "dev": [
            "pytest>=7.0.0",  # 测试
            "black>=23.0.0",  # 代码格式化
            "isort>=5.12.0",  # 导入排序
        ],
    },
    entry_points={
        "console_scripts": [
            "dd-detect=droppings_detect.cli:main",  # 可选：命令行接口
        ],
    },
)
