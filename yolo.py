from ultralytics import YOLO

model=YOLO("yolov8m_seg_custom.pt");
model.predict(source="gun2.mp4",show=True,save=True,hide_labels=False,hide_conf=False,save_txt=True,save_crop=True,line_thickness=2)

