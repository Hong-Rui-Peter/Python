import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import matplotlib.pyplot as plt

# 虛擬數據集
np.random.seed(42)
X = np.random.rand(100, 1)  # 100個隨機數
y = 3 * X + 1 + 0.2 * np.random.randn(100, 1)  # y = 3X + 1 + 噪音

# 將數據轉換為PyTorch張量
X_tensor = torch.tensor(X, dtype=torch.float32)
y_tensor = torch.tensor(y, dtype=torch.float32)


# 定義一個簡單的神經網絡模型
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.linear = nn.Linear(1, 1)

    def forward(self, x):
        return self.linear(x)


# 初始化模型和優化器
model = SimpleModel()
criterion = nn.MSELoss()  # 均方誤差作為損失函數
optimizer = optim.SGD(model.parameters(), lr=0.01)  # 隨機梯度下降優化器

# 訓練模型
num_epochs = 1000
for epoch in range(num_epochs):
    # 正向傳播
    outputs = model(X_tensor)
    loss = criterion(outputs, y_tensor)

    # 反向傳播和優化
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if (epoch + 1) % 100 == 0:
        print(f"Epoch [{epoch + 1}/{num_epochs}], Loss: {loss.item():.4f}")

# 可視化訓練結果
predicted = model(X_tensor).detach().numpy()
plt.scatter(X, y, label="True data")
plt.plot(X, predicted, label="Predicted data", color="red")
plt.legend()
plt.xlabel("X")
plt.ylabel("y")
plt.show()
