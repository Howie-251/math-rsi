# Saved672相位兼容性诊断

只读原ALL_T_RESULTS.tsv的672行，按relative=(targetphase−t.phase)mod6归一；未重算源、U_t、参数或验证。

phase0: max106,fullcases0; phase1: max106,fullcases0; phase2: max106,fullcases0; phase3: max106,fullcases0; phase4: max106,fullcases0; phase5: max106,fullcases0。

事前预测REFUTED；最小不能同时满的相位数为1，lex首子集为[0]。全部最小子集、各相位最大覆盖参数见证和64subset兼容计数保存在JSON。这些是各相位最大覆盖106的参数见证；实际不存在局部满112的见证，空子集的见证仅为vacuous，不是完整图。全fixedmatching672NO不扩到任意matching。

实际postprocessCPU=0.016622949，准备保守charge=0.05，新增合计0.066622949/0.3；沿旧1.478501838累计1.545124787CPU秒。完成即停。
