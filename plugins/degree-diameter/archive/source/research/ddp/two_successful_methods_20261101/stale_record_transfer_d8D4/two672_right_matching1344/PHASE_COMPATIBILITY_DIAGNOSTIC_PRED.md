# 保存672行的相位兼容性诊断：事前预测
只读ALL_T_RESULTS.tsv，不重算源图、word、U_t或任何t。
将target absolute phase归一为relative phase=(target−t.phase)mod6。
可推翻预测：六个relative phase各自都有112/112的保存见证，但存在无法同时满的phase pair。
若某单phase已永不满，或最小不兼容子集大小不是2，按实际值推翻此预测，不补新参数。
仅在保存672个fixed right-t matching内求compatibility；不外推任意matching。
新增CPU cap0.3秒，沿case旧1.478501838继续计账；stdlib一次postprocess，准备保守charge0.05，结束STOP。
