"""
ZIP 檔案解壓縮

需要下載範例檔案，請先安裝 wget
$ pip install wget

參考資料
[1] Python 使用 zipfile 模組壓縮、解壓縮 ZIP 檔案教學與範例
https://officeguide.cc/python-zipfile-module-compression-decompression-tutorial-examples/
"""

import os, zipfile, wget

# 存放路徑 (將解壓縮的內容另存到這裡)
path_folder = "C:/Users/hongr/OneDrive/桌面/Programming Language/Python/Python_Basics/Examples Code/zip/downloads"

# 確認 資料夾是否存在
if not os.path.exists(path_folder):
    # 建立資料夾
    os.makedirs(path_folder)


# zip 檔案若是不存在
if not os.path.exists(
    "C:/Users/hongr/OneDrive/桌面/Programming Language/Python/Python_Basics/Examples Code/zip/downloads/master.zip"
):
    # 下載 zip
    wget.download(
        url="https://github.com/otrees/autoFtpDownloadZipTest/archive/refs/heads/master.zip",
        out="C:/Users/hongr/OneDrive/桌面/Programming Language/Python/Python_Basics/Examples Code/zip/downloads/master.zip",
    )


try:
    # 對 zip 檔案解壓縮 至 指定路徑
    with zipfile.ZipFile(
        "C:/Users/hongr/OneDrive/桌面/Programming Language/Python/Python_Basics/Examples Code/zip/downloads/master.zip",
        "r",
    ) as zf:
        # 檢視 zip 檔案內容 (zf.namelist()[0] 通常是放置檔案的資料夾)
        print(zf.namelist())

        # 解壓縮
        zf.extractall(path=path_folder)
except Exception as err:
    print("zip 無法開啟")
    print(err)
else:
    print("zip 解壓縮成功")
