# LeetCode Notes 📒

> 我的 LeetCode 解题笔记仓库。
> 每道题的**思路剖析、最优解法、复杂度评估与优化过程**都沉淀在这里 —— 不只是"抄答案"，而是记录**为什么这样解、还能不能更好**。

![Notes](https://img.shields.io/badge/notes-1-blue)
![Status](https://img.shields.io/badge/status-active-brightgreen)

---

## 目录结构

仓库按**算法题型**分类，每道题的笔记归入其**主要题型**所在目录：

| 目录 | 题型 | 覆盖内容 |
| :--- | :--- | :--- |
| [`01-array`](01-array/) | **数组** | 遍历、原地修改、矩阵、前缀和、差分数组 |
| [`02-string`](02-string/) | **字符串** | 模拟、字符统计、KMP / Z 函数、Manacher、字符串哈希、AC 自动机、后缀数组 |
| [`03-hash-table`](03-hash-table/) | **哈希表** | 计数、去重、映射、前缀和 + 哈希、滑动窗口 + 哈希 |
| [`04-two-pointers`](04-two-pointers/) | **双指针与滑动窗口** | 定长 / 不定长窗口、单序列 / 双序列、三指针、分组循环 |
| [`05-binary-search`](05-binary-search/) | **二分查找** | 二分答案、最小化最大值 / 最大化最小值、第 K 小 |
| [`06-linked-list`](06-linked-list/) | **链表** | 反转、快慢指针、环形检测、合并 / 拆分、LRU |
| [`07-stack-queue`](07-stack-queue/) | **栈与队列** | 括号匹配、表达式求值、单调队列、优先队列、设计题 |
| [`08-monotonic-stack`](08-monotonic-stack/) | **单调栈** | 基础模型、矩形面积 / 贡献法、最小字典序 |
| [`09-tree`](09-tree/) | **树** | 二叉树遍历、二叉搜索树、BFS / DFS、LCA、路径问题、树的构造 |
| [`10-backtracking`](10-backtracking/) | **回溯** | 子集 / 组合 / 排列、切割、棋盘问题、去重剪枝 |
| [`11-greedy`](11-greedy/) | **贪心** | 基本贪心策略、反悔贪心、区间调度、字典序、构造 |
| [`12-dynamic-programming`](12-dynamic-programming/) | **动态规划** | 入门 / 背包 / 划分、状态机、区间 DP、状压 DP、数位 DP、树形 DP、博弈与概率期望 |
| [`13-graph`](13-graph/) | **图论** | DFS / BFS、拓扑排序、基环树、最短路、最小生成树、网络流 |
| [`14-grid`](14-grid/) | **网格图** | 网格 DFS / BFS、多源 BFS、网格上的综合应用 |
| [`15-bit-manipulation`](15-bit-manipulation/) | **位运算** | 基础性质、拆位、试填、恒等式与思维题 |
| [`16-math`](16-math/) | **数学** | 数论、组合数学、概率期望、博弈、计算几何、随机算法 |
| [`17-data-structures`](17-data-structures/) | **常用数据结构** | 并查集、字典树、堆 / 对顶堆、树状数组、线段树、有序集合 |
| [`18-others`](18-others/) | **其他** | 暂未归类或跨多题型的题目 |

辅助目录：

| 目录 | 用途 |
| :--- | :--- |
| [`templates/`](templates/) | 笔记模板与完整示例笔记（格式参考） |
| [`scripts/`](scripts/) | 工具脚本，用于自动重建下方索引与统计 |

---

## 笔记规范

每份笔记为**一个 Markdown 文件**，命名规则：

```text
题号-题目名.md          # 例：1-两数之和.md、146-LRU缓存.md
```

存放位置：`<题型目录>/题号-题目名.md`

每份笔记**必须包含**以下六个部分：

| # | 章节 | 内容要求 |
| :-: | :--- | :--- |
| 1 | **题目信息** | 题号、题名、难度、标签、LeetCode 原题链接 |
| 2 | **题目描述** | 题意复述、示例、约束条件 |
| 3 | **解题思路** | 核心思想、思路演进（从暴力到最优的推导过程）、关键点 |
| 4 | **代码实现** | 最终提交的代码（默认语言：**Python**） |
| 5 | **复杂度分析** | 时间复杂度 / 空间复杂度，与理论下界对比 |
| 6 | **优化评估** | 瓶颈分析、是否有优化空间；**若可优化则附优化代码与理由**，若已最优则说明依据 |

笔记头部使用 YAML frontmatter 记录结构化元信息，便于脚本自动汇总索引：

```yaml
---
number: 1
title: 两数之和
title_en: Two Sum
difficulty: 简单
tags: [数组, 哈希表]
category: 01-array
leetcode: https://leetcode.cn/problems/two-sum/
status: 已通过
date: 2026-09-13
---
```

---

## 笔记索引

<!-- INDEX:START -->
### 双指针与滑动窗口 <sub>`04-two-pointers`</sub>

| # | 题目 | 难度 | 标签 | 原题 |
| ---: | :--- | :--- | :--- | :-: |
| 1176 | [健身计划评估](04-two-pointers/1176-%E5%81%A5%E8%BA%AB%E8%AE%A1%E5%88%92%E8%AF%84%E4%BC%B0.md) | 🟢 简单 | 数组 · 滑动窗口 | [LeetCode](https://leetcode.cn/problems/diet-plan-performance/) |
<!-- INDEX:END -->

---

## 进度统计

<!-- STATS:START -->
| 题型 | 已整理题数 |
| :--- | ---: |
| 双指针与滑动窗口 | 1 |
| **合计** | **1** |

_按难度分布：简单 1 · 中等 0 · 困难 0_
<!-- STATS:END -->

---

## 工作流

```text
拿到已解决的题目
      ↓
分析题型 → 归入对应分类目录
      ↓
按 templates/note-template.md 生成笔记
（链接 / 难度 / 思路 / 代码 / 复杂度 / 优化评估）
      ↓
保存为 题号-题目名.md
      ↓
重建索引 → 提交并推送到 GitHub
```

### 手动重建索引

新增笔记后，运行以下命令即可刷新上方的「笔记索引」与「进度统计」：

```bash
python scripts/update_index.py
```

---

## 说明

- 题解语言默认为 **Python**，个别题目会额外给出其他语言版本作为对照。
- 复杂度一律用**渐进记法**（Big-O）标注；涉及常数优化时会在「优化评估」中单独说明。
- 笔记侧重**可复用性**：同一题型内会标注该题体现的通用套路，便于二刷时快速回忆。
- 题目版权归 [LeetCode](https://leetcode.cn/) 所有，本仓库仅用于个人学习记录。

---

<p align="center">
  <sub>由 <b>ASKY</b> 持续更新 · Powered by WorkBuddy 🐸</sub>
</p>
