# linode

由於 linode 提供的 python lib 尚未支援 lke 功能,因此透過 API request 來實作此功能.

### 使用前，需安裝 pytest 套件
```
pip install pytest
```

### 設定使用者金鑰
點擊連結 [linode](https://cloud.linode.com/kubernetes/clusters)登入系統

點擊token取得linode token，記得取得token務必保留好，因為無法再度查詢

![image](https://github.com/edward0128/linode/blob/master/linode_token.png)

```
def test_linode_api():
    token="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
 　　.......
 
```

### 開始測試
```
pytest linode_lke.py
```
