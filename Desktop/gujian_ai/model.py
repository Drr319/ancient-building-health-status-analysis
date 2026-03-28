import torch
import torch.nn as nn
import torchvision.models as models

class GuJianModel(nn.Module):
    def __init__(self):
        super().__init__()
        # 用预训练的 ResNet18 作为 backbone
        self.backbone = models.resnet18(pretrained=True)
        # 替换最后一层全连接层，输出 3 个任务的结果
        in_features = self.backbone.fc.in_features
        self.backbone.fc = nn.Identity()  # 去掉原来的全连接层
        
        # 分支1：预测含水率（回归任务）
        self.moisture_head = nn.Linear(in_features, 1)
        # 分支2：预测侵蚀等级（分类任务，0/1/2）
        self.erosion_head = nn.Linear(in_features, 3)
        # 分支3：预测防水等级（分类任务，0/1/2）
        self.waterproof_head = nn.Linear(in_features, 3)

    def forward(self, x):
        feat = self.backbone(x)
        moisture = self.moisture_head(feat)
        erosion = self.erosion_head(feat)
        waterproof = self.waterproof_head(feat)
        return moisture, erosion, waterproof