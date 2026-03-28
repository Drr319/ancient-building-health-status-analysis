import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from model import GuJianModel
from utils import GuJianDataset, get_transform
import pandas as pd

# 超参数
BATCH_SIZE = 2
EPOCHS = 20
LR = 1e-4

# 1. 准备数据
dataset = GuJianDataset(
    csv_path="labels.csv",
    img_dir="data/train",
    transform=get_transform(train=True)
)
dataloader = DataLoader(dataset, batch_size=BATCH_SIZE, shuffle=True)

# 2. 初始化模型、损失函数和优化器
model = GuJianModel()
mse_loss = nn.MSELoss()  # 含水率用均方误差
ce_loss = nn.CrossEntropyLoss()  # 分类任务用交叉熵
optimizer = optim.Adam(model.parameters(), lr=LR)

# 3. 训练循环
for epoch in range(EPOCHS):
    model.train()
    total_loss = 0.0
    for imgs, moistures, erosions, waterproofs in dataloader:
        optimizer.zero_grad()
        
        moisture_pred, erosion_pred, waterproof_pred = model(imgs)
        # 计算各任务损失
        loss_moisture = mse_loss(moisture_pred.squeeze(), moistures)
        loss_erosion = ce_loss(erosion_pred, erosions)
        loss_waterproof = ce_loss(waterproof_pred, waterproofs)
        # 总损失
        loss = loss_moisture + loss_erosion + loss_waterproof
        
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    
    avg_loss = total_loss / len(dataloader)
    print(f"Epoch {epoch+1}/{EPOCHS}, Average Loss: {avg_loss:.4f}")

# 4. 保存模型
torch.save(model.state_dict(), "gujian_model.pth")
print("✅ 模型已保存为 gujian_model.pth")