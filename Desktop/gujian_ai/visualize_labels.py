import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']  # 解决中文显示
plt.rcParams['axes.unicode_minus'] = False

def visualize_labels():
    # 读取 labels.csv
    df = pd.read_csv("labels.csv")
    
    # 创建画布
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('古建筑图片标注数据可视化', fontsize=16, weight='bold')

    # 1. 含水率分布直方图
    axes[0,0].hist(df['moisture'], bins=6, color='#2E86AB', edgecolor='black', alpha=0.7)
    axes[0,0].axvline(20, color='red', linestyle='--', label='安全阈值 20%')
    axes[0,0].set_title('含水率(moisture)分布')
    axes[0,0].set_xlabel('含水率 %')
    axes[0,0].set_ylabel('样本数')
    axes[0,0].legend()

    # 2. 侵蚀等级柱状图
    erosion_counts = df['erosion'].value_counts().sort_index()
    axes[0,1].bar(erosion_counts.index, erosion_counts.values, color='#A23B72', alpha=0.7)
    axes[0,1].set_title('侵蚀等级(erosion)分布')
    axes[0,1].set_xlabel('等级 (0=无/轻, 1=轻度, 2=中度/重度)')
    axes[0,1].set_ylabel('样本数')
    for i, v in enumerate(erosion_counts.values):
        axes[0,1].text(i, v+0.1, str(v), ha='center')

    # 3. 防水等级柱状图
    waterproof_counts = df['waterproof'].value_counts().sort_index()
    axes[1,0].bar(waterproof_counts.index, waterproof_counts.values, color='#F18F01', alpha=0.7)
    axes[1,0].set_title('防水等级(waterproof)分布')
    axes[1,0].set_xlabel('等级 (0=良好, 1=一般, 2=差)')
    axes[1,0].set_ylabel('样本数')
    for i, v in enumerate(waterproof_counts.values):
        axes[1,0].text(i, v+0.1, str(v), ha='center')

    # 4. 含水率 vs 侵蚀等级散点图
    scatter = axes[1,1].scatter(df['moisture'], df['erosion'], c=df['waterproof'], cmap='coolwarm', s=100, alpha=0.8)
    axes[1,1].set_title('含水率 vs 侵蚀等级 (颜色=防水等级)')
    axes[1,1].set_xlabel('含水率 %')
    axes[1,1].set_ylabel('侵蚀等级')
    axes[1,1].set_yticks([0,1,2])
    plt.colorbar(scatter, ax=axes[1,1], label='防水等级')

    plt.tight_layout()
    plt.subplots_adjust(top=0.92)
    plt.savefig('labels_visualization.png', dpi=300)
    plt.show()
    print("✅ 图表已保存为 labels_visualization.png")

if __name__ == "__main__":
    visualize_labels()