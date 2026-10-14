# 装甲板检测作业

基于 YOLOv8 的 RoboMaster 装甲板检测视频推理。

## 文件说明
- infer.py: 推理脚本
- best.pt: 模型权重
- original_video.mp4: 原始输入视频
- result.mp4: 推理结果视频

## 检测效果
模型可正确输出装甲板类别(如 B3)、置信度(如 0.60)、四角关键点。

环境依赖
Python 3.10+
依赖安装：pip install -r requirements.txt
运行方法
python infer.py
验证结果
输入：original_video.mp4（D414 实验室实拍）
输出：result.mp4，画面中包含检测框、类别（如 B3）、置信度（如 0.60）及四角关键点
