# -*- coding: utf-8 -*-
"""
古建筑分析展示系统 - 稳定版
解决500报错问题，确保服务稳定运行
"""
from flask import Flask, render_template, request, jsonify
import logging

# 初始化Flask应用
app = Flask(__name__)

# 配置日志，方便排查问题
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 模拟古建筑数据（实际项目中可替换为数据库查询）
ancient_building_data = {
    "name": "故宫太和殿",
    "location": "北京故宫",
    "build_year": "1695年",
    "structure": "木构建筑，斗拱体系",
    "maintenance": "良好",
    "description": "中国古代宫殿建筑的代表，具有极高的历史和艺术价值。"
}

@app.route('/')
def index():
    """主页路由"""
    try:
        # 模拟数据处理逻辑
        logger.info("访问主页，返回古建筑基础信息")
        return render_template('index.html', building=ancient_building_data)
    except Exception as e:
        logger.error(f"主页加载失败: {str(e)}")
        return f"系统繁忙，请稍后重试。错误信息: {str(e)}", 500

@app.route('/analyze')
def analyze():
    """分析页面路由"""
    try:
        logger.info("访问分析页面")
        # 模拟分析数据
        analysis_result = {
            "structural_integrity": "优秀",
            "material_status": "良好",
            "maintenance_suggestion": "定期检查，无需大规模维修",
            "risk_level": "低"
        }
        return render_template('analyze.html', result=analysis_result)
    except Exception as e:
        logger.error(f"分析页面加载失败: {str(e)}")
        return f"分析数据获取失败，请稍后重试。错误信息: {str(e)}", 500

@app.route('/api/building-info')
def get_building_info():
    """API接口：返回古建筑信息（供前端调用）"""
    try:
        return jsonify({
            "code": 200,
            "message": "获取成功",
            "data": ancient_building_data
        })
    except Exception as e:
        logger.error(f"API接口调用失败: {str(e)}")
        return jsonify({
            "code": 500,
            "message": f"获取失败: {str(e)}",
            "data": None
        }), 500

if __name__ == '__main__':
    # 生产环境建议使用更稳定的启动方式
    app.run(host='0.0.0.0', port=5000, debug=False)