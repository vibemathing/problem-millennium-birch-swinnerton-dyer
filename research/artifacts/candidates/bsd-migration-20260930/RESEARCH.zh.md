# Imported exploratory draft; admission pending

This packages prior local work for review, not a newly admitted research execution. No novelty, formal proof, verifier receipt, or root closure is asserted.

## 4. BSD 根命题、否定和六个子问题

B0：对所有定义于 Q 的椭圆曲线 E，ord_{s=1}L(E,s)=rank E(Q)。否定为存在一条 E/Q，使经严格认证的两个整数不等。使用全 Hasse–Weil L 函数；Wiles Clay 文本用缺有限 Euler 因子的版本陈述秩问题，这些删去因子在 s=1 非零，不改变零点阶。精细首项常数公式和 Sha 有限性是额外目标，不偷偷加到此合约中。[B1]

1. B1-analytic：准确复用 E/Q 模性带来的 L 延拓和函数方程，固定导数归一化。已知。
2. B2-lower：由显式有理点和独立性证书给秩下界。一般是逐曲线任务；本次 E5 的一个点无限阶已证，给下界1。
3. B3-upper：用2-descent/Selmer群及扭点维数给同一 E 的秩上界。方法已知；本包尚未计算 E5 的 Selmer 群，不能说秩恰为1。
4. B4-analytic-order：认证某条 E 的 L 在1的确切零点阶，包括低阶精确消失和首个非零导数的严格误差界。浮点“小于阈值”不能认证消失。本包未执行。
5. B5-low-rank-transfer：对解析秩0或1复用 Gross–Zagier/Kolyvagin 与模性推出秩等式。已知；不能误写为对所有代数秩0/1均由同一单向定理自动推出，也不等于完整精细 BSD。[B1]
6. B6-high-rank：对任意解析秩≥2 的 E/Q 建立完整秩等式。一般开放；“存在很多已知特殊曲线/族”不闭合全称量词。真正全局缺口在此，而非再举几个秩1例子。

DAG：B1-analytic→B4-analytic-order；{B2-lower,B3-upper}→某曲线代数秩证书；{代数秩证书,B4-analytic-order}→某曲线 BSD 等式（仅当两整数相同）；{B1-analytic,B5-low-rank-transfer,B6-high-rank}→B0，后两支按解析秩≤1和≥2穷尽。B2 的单个例子不是通往 B0 的充分边。

项目级下一叶子：先为 E5 建立显式2-descent上界证书，并把“rank≥1”与“rank=1”作为两个不同输出状态的回归测试；随后做 L'(E5,1) 的严格非零界并核对函数方程符号。此工作是建立可信逐曲线管线，不是新证明一般 BSD。真正开放的 B6 必须保留独立节点。

## 5. BSD 已执行：一个完整无限阶证明

命题：若 n 是非零奇整数，P=(x,y)∈E_n(Q):y²=x³−n²x 且 v₂(x)<0，则 P 无限阶。

证明：曲线判别式64n^6≠0。设 a=v₂(x)<0。因 v₂(n²)=0，而 v₂(x²)=2a<0，超度量等号给

v₂(x²+n²)=v₂(x²−n²)=2a。

特别地 x≠0 且 x²≠n²，因此 y≠0，可以倍点。弦切法斜率 m=(3x²−n²)/(2y)，x(2P)=m²−2x。用 y²=x(x²−n²) 合并分式：

x(2P)=[(3x²−n²)²−8x²(x²−n²)]/[4x(x²−n²)]
       =(x²+n²)²/[4x(x²−n²)]。

因此 v₂(x(2P))=4a−(2+a+2a)=a−2<0。可无限递推，v₂(x(2^kP))=a−2k。这些赋值两两不同，故这些有理点两两不同。若 P 是有限阶，倍点序列只能取有限多个值，矛盾。所以 P 无限阶。证毕。

特化 n=5, P=(25/4,75/8)：y²=5625/64，x³−25x=15625/64−10000/64=5625/64，a=−2。由 Mordell 有限生成性，E5(Q)含无限阶点即 rank≥1。此证据不涉及 L 函数，不能单独证明 BSD。P 还给有理直角三角形边长 (x²−25)/y=3/2、10x/y=20/3、(x²+25)/y=41/6，面积5；该对应是经典 congruent-number 构造。[B1,B2]

execute.py 精确计算 P,2P,…,32P；每次检查曲线方程、两种倍点公式一致及赋值 −2,−4,−6,−8,−10,−12。完整坐标在 results.json。另给不在曲线上的 (25/4,74/8) 作负例，必须拒绝。

失败标准：输入不满足曲线方程；n=0或n非奇数却套用本命题；v₂(x)≥0却套用本命题；y=0仍除法；给出的有限点列无无限归纳；误推 rank=1 或解析秩=1。此处证明给出全部量词的归纳，有限计算仅回归检查。


## Sources and reproduction

Official source: https://www.claymath.org/wp-content/uploads/2022/05/birchswin.pdf

RH Li criterion is an external dependency: Bombieri–Lagarias, JNT 77 (1999), 274–287; no full-paper verification asserted. BSD group/valuation arguments are in the draft. Run `python execute.py` in this directory (standard library; timeout 30 seconds). Finite output is only a regression check; the general BSD claim depends on the written argument.
