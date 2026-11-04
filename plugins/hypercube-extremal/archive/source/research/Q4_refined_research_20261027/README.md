# 可选研究与搜索复现包

最终结论以最小证书包的独立整数核验为准。本目录保留搜索代码、候选快照与包括失败探索在内的日志；不把浮点搜索成功等同于证明。

测试环境：Python 3.13，NumPy 2.3.5，SciPy 1.17。列生成代码使用 SciPy 附带的私有 HiGHS 接口，其他 SciPy 版本可能需要适配；这不影响最小证书核验。

先生成约 0.5 GB 的可再生局部观察数据：

```bash
python prepare_data.py
python build_face_orbits.py
g++ -O3 -std=c++17 generate_models.cpp -o generate_models
./generate_models
g++ -O3 -shared -fPIC -fopenmp evaluate.cpp -o evaluate.so
python model.py
```

`full_C.npz`、`full_meta.npz`、`full_flags_best.npz` 是前轮压缩模型的输入，用于继承原证书和审计折叠；最终独立核验不使用它们。

可由已保存的 warm-start 继续重演搜索，例如：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=2 python adaptive.py --restart --cycles 20 --iterations 150
```

最后必须重新认证，不能把搜索日志中的 restricted_max 当作全局上界：

```bash
g++ -O3 -std=c++17 verify_six.cpp -o verify_six
OPENBLAS_NUM_THREADS=1 python certify_six.py --input certification_snapshot.npz --out rechecked.json
python verify_six.py rechecked.json
```

`adaptive/refine` 使用 Gram 因子，因此生成的矩阵半正定；舍入后必须改用整数 Gram 认证。`dual_target` 没有得到合法的 0.59 对偶可行点；`deep` 存在活跃约束过拟合的失败候选；这些不作为最终证书。`test_horn*` 仅为未采用的共正形式探索。
