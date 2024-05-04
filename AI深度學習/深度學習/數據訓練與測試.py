import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

# 生成隨機數據
np.random.seed(42)
X = np.random.rand(100, 2)  # 100個樣本，每個樣本有兩個特徵
y = (X[:, 0] + X[:, 1] > 1).astype(int)  # 簡單的二元分類任務

# 將數據轉換為PyTorch張量
X = torch.FloatTensor(X)
y = torch.FloatTensor(y)


# 定義神經網絡模型
class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(2, 4)  # 隱藏層，2個輸入特徵，4個神經元
        self.fc2 = nn.Linear(4, 1)  # 輸出層，1個輸出

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.sigmoid(self.fc2(x))
        return x


# 初始化模型
model = SimpleNN()

# 定義損失函數和優化器
criterion = nn.BCELoss()  # 二元交叉熵損失函數
optimizer = optim.SGD(model.parameters(), lr=0.1)

# 訓練模型
for epoch in range(1000):
    optimizer.zero_grad()  # 清零梯度
    outputs = model(X)  # 前向傳播
    loss = criterion(outputs, y.view(-1, 1))  # 計算損失
    loss.backward()  # 反向傳播
    optimizer.step()  # 更新權重

    if (epoch + 1) % 100 == 0:
        print(f"Epoch [{epoch+1}/1000], Loss: {loss.item():.4f}")

# 測試模型
with torch.no_grad():
    test_data = torch.FloatTensor([[0.8, 0.4]])  # 測試數據
    prediction = model(test_data)
    print(f"Prediction: {prediction.item():.4f}")
