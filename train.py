from ultralytics import YOLO

model = YOLO("yolov8x-seg.pt")
model.train(
    # Project
    project="football",
    name="YOLOV8-segmentation",

    # Random Seed parameters
    deterministic=True,
    seed=43,

    # Data & model parameters
    data="dataset.yaml",
    save=True,
    save_period=5,
    pretrained=True,
    imgsz=(1920,1080),

    # Training parameters
    epochs=2,
    batch=1,
    workers=4,
    val=True,
    device=0,

    # Optimization parameters
    lr0=0.018,
    patience=3,
    optimizer="Adam",
    momentum=0.947,
    weight_decay=0.0005,
    close_mosaic=3,
)