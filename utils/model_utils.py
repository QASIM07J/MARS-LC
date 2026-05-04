import json
import os
from typing import Any

import torch
import torch.nn as nn
from PIL import Image
from torchvision import models, transforms


_BASE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "MODELS")

MODEL_CONFIGS = {
    "EfficientNet-B0": {
        "folder": os.path.join(_BASE, "Efficient Net"),
        "pth": "best_mars_efficientnet_model.pth",
        "config": "efficientnet_inference_config.json",
        "arch": "efficientnet_b0",
    },
    "MobileNet-V2": {
        "folder": os.path.join(_BASE, "MobileNet"),
        "pth": "best_mars_mobilenet_model.pth",
        "config": "mobilenet_inference_config.json",
        "arch": "mobilenet_v2",
    },
    "ResNet-50": {
        "folder": os.path.join(_BASE, "Resnet Model Result"),
        "pth": "best_mars_resnet_model.pth",
        "config": "resnet_inference_config.json",
        "arch": "resnet50",
    },
    "Custom CNN": {
        "folder": os.path.join(_BASE, "Custom Model Results"),
        "pth": "best_mars_customcnn_model.pth",
        "config": "customcnn_inference_config.json",
        "arch": "customcnn",
    },
}

MODEL_F1 = {
    "ResNet-50": 0.8621,
    "MobileNet-V2": 0.8368,
    "EfficientNet-B0": 0.8357,
    "Custom CNN": 0.7305,
}

BEST_MODEL_NAME = max(MODEL_F1, key=MODEL_F1.get)


class CustomCNN(nn.Module):
    def __init__(self, num_classes: int = 8) -> None:
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=3, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(inplace=True),
            nn.Conv2d(64, 64, kernel_size=3, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(2, 2),
            nn.Dropout(0.25),

            nn.Conv2d(64, 128, kernel_size=3, padding=1),
            nn.BatchNorm2d(128),
            nn.ReLU(inplace=True),
            nn.Conv2d(128, 128, kernel_size=3, padding=1),
            nn.BatchNorm2d(128),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(2, 2),
            nn.Dropout(0.25),

            nn.Conv2d(128, 256, kernel_size=3, padding=1),
            nn.BatchNorm2d(256),
            nn.ReLU(inplace=True),
            nn.Conv2d(256, 256, kernel_size=3, padding=1),
            nn.BatchNorm2d(256),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(2, 2),
            nn.Dropout(0.25),

            nn.Conv2d(256, 512, kernel_size=3, padding=1),
            nn.BatchNorm2d(512),
            nn.ReLU(inplace=True),
            nn.Conv2d(512, 512, kernel_size=3, padding=1),
            nn.BatchNorm2d(512),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(2, 2),
            nn.Dropout(0.25),

            nn.Conv2d(512, 512, kernel_size=3, padding=1),
            nn.BatchNorm2d(512),
            nn.ReLU(inplace=True),
        )
        self.classifier = nn.Sequential(
            nn.AdaptiveAvgPool2d((1, 1)),
            nn.Flatten(),
            nn.Linear(512, 256),
            nn.ReLU(inplace=True),
            nn.Dropout(0.5),
            nn.Linear(256, num_classes),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = self.features(x)
        x = self.classifier(x)
        return x


def _build_architecture(arch: str, num_classes: int) -> nn.Module:
    if arch == "efficientnet_b0":
        model = models.efficientnet_b0(weights=None)
        model.classifier[1] = nn.Linear(model.classifier[1].in_features, num_classes)
    elif arch == "mobilenet_v2":
        model = models.mobilenet_v2(weights=None)
        model.classifier[1] = nn.Linear(model.classifier[1].in_features, num_classes)
    elif arch == "resnet50":
        model = models.resnet50(weights=None)
        model.fc = nn.Linear(model.fc.in_features, num_classes)
    elif arch == "customcnn":
        model = CustomCNN(num_classes)
    else:
        raise ValueError(f"unknown architecture: {arch}")
    return model


def _load_single_model(name: str) -> dict[str, Any]:
    cfg = MODEL_CONFIGS[name]
    folder = cfg["folder"]

    config_path = os.path.join(folder, cfg["config"])
    with open(config_path, encoding="utf-8") as handle:
        inference_config = json.load(handle)

    num_classes = inference_config["num_classes"]
    class_names = inference_config["class_names"]
    image_size = inference_config["image_size"]
    mean = inference_config["mean"]
    std = inference_config["std"]

    model = _build_architecture(cfg["arch"], num_classes)
    pth_path = os.path.join(folder, cfg["pth"])
    state = torch.load(pth_path, map_location="cpu", weights_only=True)
    model.load_state_dict(state)
    model.eval()

    transform = transforms.Compose([
        transforms.Resize((image_size, image_size)),
        transforms.ToTensor(),
        transforms.Normalize(mean=mean, std=std),
    ])

    return {
        "model": model,
        "transform": transform,
        "class_names": class_names,
        "image_size": image_size,
    }


def load_models() -> dict[str, Any]:
    loaded: dict[str, Any] = {}
    for name in MODEL_CONFIGS:
        try:
            loaded[name] = _load_single_model(name)
        except Exception as exc:
            loaded[name] = {"error": str(exc)}
    return loaded


def preprocess_image(image: Image.Image) -> Image.Image:
    return image.convert("RGB")


def predict_with_model(model_entry: dict[str, Any], image: Image.Image) -> dict[str, Any]:
    if "error" in model_entry:
        return {
            "predicted_class": "model unavailable",
            "confidence": 0.0,
            "probabilities": {},
            "error": model_entry["error"],
        }

    transform = model_entry["transform"]
    model = model_entry["model"]
    class_names = model_entry["class_names"]

    tensor = transform(image.convert("RGB")).unsqueeze(0)

    with torch.no_grad():
        logits = model(tensor)
        probabilities = torch.softmax(logits, dim=1).squeeze(0)

    confidence, index = probabilities.max(0)
    predicted_class = class_names[index.item()]

    return {
        "predicted_class": predicted_class,
        "confidence": confidence.item(),
        "probabilities": {
            class_names[i]: round(probabilities[i].item(), 4)
            for i in range(len(class_names))
        },
    }