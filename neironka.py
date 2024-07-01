from ultralytics import YOLO


model = YOLO('yolov8m.pt')

result = model.train(data='my_dataset_yolo/data.yaml', epochs=20, imgsz=640, model='yolov8m.pt')

