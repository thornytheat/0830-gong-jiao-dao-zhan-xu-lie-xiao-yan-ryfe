# 公交到站序列校验

公交运营数据员可在工作台上传来源 CSV，对照规则判断差异，签发合格批次或记录暂缓意见。

在允许绕行缺站时选择得分最高的单调站序，排除逆序定位点。

## 启动

```sh
docker compose up --build -d --wait
```

打开 <http://localhost:18329>。页面预览带异常样例。选中阶段查看计算证据，选择可签发样例并执行批次，然后提交复核意见。

## 核验

```sh
docker compose exec -T app pytest -q
```

[输入字段](docs/DATA-DICTIONARY.md) · [阶段接口](docs/HTTP.md) · [操作步骤](docs/OPERATIONS.md) · [规则与测试](docs/DEPTH.md)
