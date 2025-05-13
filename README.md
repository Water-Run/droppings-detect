# `droppings-detect`: 动物排泄物识别  

一个定制的项目,识别图片或视频中的动物排泄物.  

## 使用前准备  

### 安装  

在`setup.py`目录下运行`pip install .`进行安装.  
然后,导入该包(使用下划线;以`dd`为别名):  

```python
import droppings_detect as dd
```

## 使用  

### 结果封装  

一个只读的定制类`Result`封装识别出的一个动物排泄物.    
`Result`包括以下属性:  
- `up_left`: 识别出的排泄物的坐标范围左上角  
- `down_right`: 识别出的排泄物的坐标范围右下角  
- `confidence`: 识别出的排泄物的置信度  
可以直接打印`Result`.  

### 识别  

基础的识别是识别单张图片:  

```python
import droppings_detect as dd
dd.image.detect('your path') # 更换为待识别的图片路径
```

返回`Result`列表,对应每个识别出的排泄物.  

还可以对视频进行直接识别:  

> 和图像检测不同的是,视频检测的结果是使用`yield`动态更新的.  

```python
import droppings_detect as dd
results: list[dd.Result] = [
    result for result in dd.video.detect('your path', 0) # 第一个参数为更换为待识别的图片路径. 第二个参数表示检测的间隔帧数,比如,0就表示每一帧都检测.该参数是可选的,默认为60.  
]
```
