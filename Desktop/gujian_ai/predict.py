import torch
from PIL import Image
from model import GuJianModel
from utils import get_transform

def predict_image(img_path, model_path="gujian_model.pth"):
    # 1. 加载模型
    model = GuJianModel()
    model.load_state_dict(torch.load(model_path))
    model.eval()

    # 2. 预处理图片
    transform = get_transform(train=False)
    img = Image.open(img_path).convert("RGB")
    img_tensor = transform(img).unsqueeze(0)  # 增加 batch 维度

    # 3. 模型预测
    with torch.no_grad():
        moisture_pred, erosion_pred, waterproof_pred = model(img_tensor)
    
    # 4. 解析结果
    moisture = moisture_pred.squeeze().item()
    erosion = torch.argmax(erosion_pred, dim=1).item()
    waterproof = torch.argmax(waterproof_pred, dim=1).item()

    # 5. 映射为文字说明
    erosion_desc = {0: "无/轻度侵蚀", 1: "轻度侵蚀", 2: "中度/重度侵蚀"}
    waterproof_desc = {0: "良好", 1: "一般", 2: "隐患/差"}

    return {
        "moisture": round(moisture, 1),
        "erosion": erosion,
        "erosion_desc": erosion_desc[erosion],
        "waterproof": waterproof,
        "waterproof_desc": waterproof_desc[waterproof]
    }

if __name__ == "__main__":
    # 测试图片路径（你可以改成自己的图片）
    test_img = "test.jpg"
    result = predict_image(test_img)

    print("=" * 40)
    print("        古建筑图片分析结果")
    print("=" * 40)
    print(f"📊 含水率：{result['moisture']}%")
    print(f"🐜 侵蚀等级：{result['erosion']} → {result['erosion_desc']}")
    print(f"💧 防水等级：{result['waterproof']} → {result['waterproof_desc']}")
    print("=" * 40)