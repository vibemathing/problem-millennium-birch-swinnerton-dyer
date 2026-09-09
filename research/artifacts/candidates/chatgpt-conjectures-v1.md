# Candidate-only Eight-Category Conjecture Map (ChatGPT export)

- Repository: vibemathing/problem-millennium-birch-swinnerton-dyer
- Problem: problem:millennium-birch-swinnerton-dyer
- Source chat content SHA-256: `b4a38af0ec6ee591133fba197c6db79f9daff98ccb047fa737fd7c8ecc27abcd`
- Status: candidate_only; statement_faithfulness pending; prior-art review pending; independent verification pending
- Transport classification: computation (bounded classification/catalog audit). This file claims no proof, counterexample, Evidence, Result, or Solution.
- Excerp from CONJECTURE_CATALOG.md section below (verbatim).

输入：`ChatGPT-开始猜想制定-20260909-1842.md`
1. `BSD-E` 存在：解析秩 `2` 的椭圆曲线存在至少一个非扭有理点；这是根 BSD 的弱化方向。
2. `BSD-U` 全称：对每个 `E/Q`，解析秩等于 Mordell–Weil 秩；根命题。
3. `BSD-R` 刚性：解析秩 `2` 的代数秩唯一被约束为 `2`，或探测素数上的 Sha 缺陷满足指定偶性；需先冻结 Selmer 定义。
4. `BSD-Q` 对应：`L(E,1)=0` 当且仅当 `E(Q)` 无限/正秩；这是弱 BSD 后果，不应伪装成新证明。
5. `BSD-K` 分类：按解析秩的曲线分层与按代数秩的曲线分层完全相同；与根 BSD 逻辑等价。
6. `BSD-B` 界：解析秩 `2` 推出代数秩 `<=2`，可经 Selmer 上界或广义 Kato 可探测性路线攻击。
7. `BSD-A` 渐近：固定曲线二次扭曲族中解析秩与 `2`-Selmer corank 一致的比例趋于 `1`；必须锁定扭曲范围和秩计算证书。
8. `BSD-D` 复杂度：每条曲线存在有限、机械可检查的完整秩证书；要分别规定有理点下界、下降/Euler-system 上界和解析阶数证书。
首选后续路线：先做 `BSD-R/BSD-B` 的定义审计；聊天材料中的 `s_p=r_alg+sigma_p` 等等式不能未经精确 Selmer 假设直接写入候选。
