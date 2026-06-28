print("hello world")

# 定义一个简单的问候函数
def greet(name):
    """向指定的人问好"""
    return f"你好，{name}！欢迎来到Python世界！"

# 定义一个简单的计算器类
class SimpleCalculator:
    """简单的计算器类"""

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "错误：除数不能为零"
        return a / b

# 主程序
if __name__ == "__main__":
    # 测试问候函数
    print(greet("小明"))

    # 使用计算器
    calc = SimpleCalculator()
    print(f"10 + 5 = {calc.add(10, 5)}")
    print(f"10 - 5 = {calc.subtract(10, 5)}")
    print(f"10 × 5 = {calc.multiply(10, 5)}")
    print(f"10 ÷ 5 = {calc.divide(10, 5)}")