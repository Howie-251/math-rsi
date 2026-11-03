# N11 changed-base retries：19项终态，无新增

基图为已验37631/205329边。只重试上次失败base<37631的canonical indices [0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20]；accepted3/17/21及已在37631失败22/23跳过。

实际状态：{'EXACT_NO_AT_MOST_ONE_ANCHOR_ON_THIS_BASE': 19}。全部19项结束，0新增，最终仍37631。单worker CPU 0.483733020秒，232次实际radius4检查；0全源BFS、0外审、0第二anchor、0oldcache拒绝。

冻结列表见PREDICTION.json/frozen_items.json，完整逐项证据见RESULT.json，accepted_sequence.json为空。没有新接受，所以本批base未变化；不改旧37629/37631或delivery38快照，不自动扩线或续轮。

无需重枚举即可得到固定族止损：原37628全nonH9 Q-line度数池恰24个10pin项；只添边后degree只增，池外线不会变可行。3/17/21已用线的mandatory pins已满度，余下21个由本次19个37631失败及原22/23同base失败全部覆盖。因此固定37631、原37471-core fold、完整nonH9 Q-line像直接加点（最多1anchor）的族已关闭。这是复用旧全池证据的推论，不是新5m-line枚举；不排H9 incidence-lines、改变fold/旧图、其他邻接机制或一般N(11,5)提升。
