# pre-run：固定首P的28port联合匹配

继承原10000随机配置UNKNOWN，不重抽样。固定旧cuts(43,58)/(151,314)，P={43,58,151,314}。预测存在另一个28port perfectmatching，使365新根的R5覆盖全部旧364；这不预言旧旧D5。根据JOINT_PORT_INTERFACE_READ和独立paper攻击，新根覆盖恰等价于allowed无向port图有perfectmatching。

只解析既有自然364/714源一次、复用PORT_CLASSES和port缓存语义，求四个固定core的source闭R4支持（深度4，不是源全D5验证）。所有cut端点属于P，最短P到t路线可避cuts。hole t的唯一owner b与β<=2给d(P,mate(b))+β<=3；按每class最大β合并，并施加双方约束。先查需要β2尾腿的owner集合是否比d(P,port)<=1的可用mate集合更大；这是可直接复核的Hall必要反例。若无此证据，使用现有networkx最大基数匹配；包不存在或超时返回UNKNOWN，不安装。

命中则构造365/730/all4regular完整图，先ordinary全365roots；真正完整合法才交fresh/Lean/最新基线/ARIS。负例只排这个固定P的所有portmatching，不自动换cuts/seed/全cutpair。原case cap20CPU，旧1.537876879、jointread.3、新prep.3不清零，本worker硬16CPU。
