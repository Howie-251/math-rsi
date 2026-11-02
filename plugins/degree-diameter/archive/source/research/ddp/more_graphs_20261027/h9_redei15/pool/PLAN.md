# Rédei15：固定F3群轨道与1120平面degree池

只生成候选池，不做覆盖补全。先与已有geometry.py核对F9=a+3bu、u²=−1编码，复用原PG2(F9)91点顺序；对给定15点mask求三个F3 projective生成元的轨道。保存每个orbit mask及parent/generator，可恢复具体变换。

复用原flat364和nonflat756的basis及91个rawpoint IDs；不重建H9 incidence、flatplanes、旧Baer masks或旧degreelegal池。N12固定42398/245889，N11固定37631/205329；读取绑定这两基图的已有degree和fold缓存。

每plane/orbit分别按两个base的实际degree<cap与distinct pin_count<=cap筛。按实际folded pins去重，保留原15点、basis、mask/local IDs、folded pins、degree/freeslots及全部plane/orbit引用。先10个planes测速，未超投影90CPU再完成余1110；已完成prefix不重放。

输出pool12.json、pool11.json、orbit.json及终态计数。完整候选池交给独立producer；本任务不做R4、anchor、图生成或重新验旧图。
