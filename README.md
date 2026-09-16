# LeetCode Notes 📒

> 我的 LeetCode 解题笔记仓库。
> 每道题的**思路剖析、最优解法、复杂度评估与优化过程**都沉淀在这里 —— 不只是"抄答案"，而是记录**为什么这样解、还能不能更好**。

![Notes](https://img.shields.io/badge/notes-23-blue)
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
| 3 | [无重复字符的最长子串](04-two-pointers/3-%E6%97%A0%E9%87%8D%E5%A4%8D%E5%AD%97%E7%AC%A6%E7%9A%84%E6%9C%80%E9%95%BF%E5%AD%90%E4%B8%B2.md) | 🟡 中等 | 哈希表 · 字符串 · 滑动窗口 | [LeetCode](https://leetcode.cn/problems/longest-substring-without-repeating-characters/) |
| 209 | [长度最小的子数组](04-two-pointers/209-%E9%95%BF%E5%BA%A6%E6%9C%80%E5%B0%8F%E7%9A%84%E5%AD%90%E6%95%B0%E7%BB%84.md) | 🟡 中等 | 数组 · 二分查找 · 前缀和 · 滑动窗口 | [LeetCode](https://leetcode.cn/problems/minimum-size-subarray-sum/) |
| 904 | [水果成篮](04-two-pointers/904-%E6%B0%B4%E6%9E%9C%E6%88%90%E7%AF%AE.md) | 🟡 中等 | 数组 · 哈希表 · 滑动窗口 | [LeetCode](https://leetcode.cn/problems/fruit-into-baskets/) |
| 1004 | [最大连续1的个数 III](04-two-pointers/1004-%E6%9C%80%E5%A4%A7%E8%BF%9E%E7%BB%AD1%E7%9A%84%E4%B8%AA%E6%95%B0III.md) | 🟡 中等 | 数组 · 二分查找 · 前缀和 · 滑动窗口 | [LeetCode](https://leetcode.cn/problems/max-consecutive-ones-iii/) |
| 1052 | [爱生气的书店老板](04-two-pointers/1052-%E7%88%B1%E7%94%9F%E6%B0%94%E7%9A%84%E4%B9%A6%E5%BA%97%E8%80%81%E6%9D%BF.md) | 🟡 中等 | 数组 · 滑动窗口 | [LeetCode](https://leetcode.cn/problems/grumpy-bookstore-owner/) |
| 1100 | [长度为 K 的无重复字符子串](04-two-pointers/1100-%E9%95%BF%E5%BA%A6%E4%B8%BAK%E7%9A%84%E6%97%A0%E9%87%8D%E5%A4%8D%E5%AD%97%E7%AC%A6%E5%AD%90%E4%B8%B2.md) | 🟡 中等 | 哈希表 · 字符串 · 滑动窗口 | [LeetCode](https://leetcode.cn/problems/find-k-length-substrings-with-no-repeated-characters/) |
| 1151 | [最少交换次数来组合所有的 1](04-two-pointers/1151-%E6%9C%80%E5%B0%91%E4%BA%A4%E6%8D%A2%E6%AC%A1%E6%95%B0%E6%9D%A5%E7%BB%84%E5%90%88%E6%89%80%E6%9C%89%E7%9A%841.md) | 🟡 中等 | 数组 · 滑动窗口 | [LeetCode](https://leetcode.cn/problems/minimum-swaps-to-group-all-1s-together/) |
| 1176 | [健身计划评估](04-two-pointers/1176-%E5%81%A5%E8%BA%AB%E8%AE%A1%E5%88%92%E8%AF%84%E4%BC%B0.md) | 🟢 简单 | 数组 · 滑动窗口 | [LeetCode](https://leetcode.cn/problems/diet-plan-performance/) |
| 1208 | [尽可能使字符串相等](04-two-pointers/1208-%E5%B0%BD%E5%8F%AF%E8%83%BD%E4%BD%BF%E5%AD%97%E7%AC%A6%E4%B8%B2%E7%9B%B8%E7%AD%89.md) | 🟡 中等 | 字符串 · 滑动窗口 · 前缀和 · 二分查找 | [LeetCode](https://leetcode.cn/problems/get-equal-substrings-within-budget/) |
| 1493 | [删掉一个元素以后全为 1 的最长子数组](04-two-pointers/1493-%E5%88%A0%E6%8E%89%E4%B8%80%E4%B8%AA%E5%85%83%E7%B4%A0%E4%BB%A5%E5%90%8E%E5%85%A8%E4%B8%BA1%E7%9A%84%E6%9C%80%E9%95%BF%E5%AD%90%E6%95%B0%E7%BB%84.md) | 🟡 中等 | 数组 · 滑动窗口 | [LeetCode](https://leetcode.cn/problems/longest-subarray-of-1s-after-deleting-one-element/) |
| 1695 | [删除子数组的最大得分](04-two-pointers/1695-%E5%88%A0%E9%99%A4%E5%AD%90%E6%95%B0%E7%BB%84%E7%9A%84%E6%9C%80%E5%A4%A7%E5%BE%97%E5%88%86.md) | 🟡 中等 | 数组 · 哈希表 · 滑动窗口 | [LeetCode](https://leetcode.cn/problems/maximum-erasure-value/) |
| 1852 | [每个子数组的数字种类数](04-two-pointers/1852-%E6%AF%8F%E4%B8%AA%E5%AD%90%E6%95%B0%E7%BB%84%E7%9A%84%E6%95%B0%E5%AD%97%E7%A7%8D%E7%B1%BB%E6%95%B0.md) | 🟡 中等 | 数组 · 哈希表 · 滑动窗口 | [LeetCode](https://leetcode.cn/problems/distinct-numbers-in-each-subarray/) |
| 2024 | [考试的最大困扰度](04-two-pointers/2024-%E8%80%83%E8%AF%95%E7%9A%84%E6%9C%80%E5%A4%A7%E5%9B%B0%E6%89%B0%E5%BA%A6.md) | 🟡 中等 | 字符串 · 滑动窗口 · 前缀和 · 二分查找 | [LeetCode](https://leetcode.cn/problems/maximize-the-confusion-of-an-exam/) |
| 2107 | [分享 K 个糖果后独特口味的数量](04-two-pointers/2107-%E5%88%86%E4%BA%ABK%E4%B8%AA%E7%B3%96%E6%9E%9C%E5%90%8E%E7%8B%AC%E7%89%B9%E5%8F%A3%E5%91%B3%E7%9A%84%E6%95%B0%E9%87%8F.md) | 🟡 中等 | 数组 · 哈希表 · 滑动窗口 | [LeetCode](https://leetcode.cn/problems/number-of-unique-flavors-after-sharing-k-candies/) |
| 2730 | [找到最长的半重复子字符串](04-two-pointers/2730-%E6%89%BE%E5%88%B0%E6%9C%80%E9%95%BF%E7%9A%84%E5%8D%8A%E9%87%8D%E5%A4%8D%E5%AD%90%E5%AD%97%E7%AC%A6%E4%B8%B2.md) | 🟡 中等 | 字符串 · 滑动窗口 | [LeetCode](https://leetcode.cn/problems/find-the-longest-semi-repetitive-substring/) |
| 2779 | [数组的最大美丽值](04-two-pointers/2779-%E6%95%B0%E7%BB%84%E7%9A%84%E6%9C%80%E5%A4%A7%E7%BE%8E%E4%B8%BD%E5%80%BC.md) | 🟡 中等 | 数组 · 排序 · 滑动窗口 · 双指针 · 二分查找 | [LeetCode](https://leetcode.cn/problems/maximum-beauty-of-an-array-after-applying-operation/) |
| 2958 | [最多 K 个重复元素的最长子数组](04-two-pointers/2958-%E6%9C%80%E5%A4%9AK%E4%B8%AA%E9%87%8D%E5%A4%8D%E5%85%83%E7%B4%A0%E7%9A%84%E6%9C%80%E9%95%BF%E5%AD%90%E6%95%B0%E7%BB%84.md) | 🟡 中等 | 数组 · 哈希表 · 滑动窗口 | [LeetCode](https://leetcode.cn/problems/length-of-longest-subarray-with-at-most-k-frequency/) |
| 3090 | [每个字符最多出现两次的最长子字符串](04-two-pointers/3090-%E6%AF%8F%E4%B8%AA%E5%AD%97%E7%AC%A6%E6%9C%80%E5%A4%9A%E5%87%BA%E7%8E%B0%E4%B8%A4%E6%AC%A1%E7%9A%84%E6%9C%80%E9%95%BF%E5%AD%90%E5%AD%97%E7%AC%A6%E4%B8%B2.md) | 🟢 简单 | 哈希表 · 字符串 · 滑动窗口 | [LeetCode](https://leetcode.cn/problems/maximum-length-substring-with-two-occurrences/) |
| 3439 | [重新安排会议得到最多空余时间 I](04-two-pointers/3439-%E9%87%8D%E6%96%B0%E5%AE%89%E6%8E%92%E4%BC%9A%E8%AE%AE%E5%BE%97%E5%88%B0%E6%9C%80%E5%A4%9A%E7%A9%BA%E4%BD%99%E6%97%B6%E9%97%B4I.md) | 🟡 中等 | 数组 · 滑动窗口 | [LeetCode](https://leetcode.cn/problems/reschedule-meetings-for-maximum-free-time-i/) |
| 3634 | [使数组平衡的最少移除数目](04-two-pointers/3634-%E4%BD%BF%E6%95%B0%E7%BB%84%E5%B9%B3%E8%A1%A1%E7%9A%84%E6%9C%80%E5%B0%91%E7%A7%BB%E9%99%A4%E6%95%B0%E7%9B%AE.md) | 🟡 中等 | 数组 · 排序 · 滑动窗口 · 双指针 | [LeetCode](https://leetcode.cn/problems/minimum-removals-to-balance-array/) |
| 3641 | [最长半重复子数组](04-two-pointers/3641-%E6%9C%80%E9%95%BF%E5%8D%8A%E9%87%8D%E5%A4%8D%E5%AD%90%E6%95%B0%E7%BB%84.md) | 🟡 中等 | 数组 · 哈希表 · 滑动窗口 | [LeetCode](https://leetcode.cn/problems/longest-semi-repeating-subarray/) |
| 3679 | [使库存平衡的最少丢弃次数](04-two-pointers/3679-%E4%BD%BF%E5%BA%93%E5%AD%98%E5%B9%B3%E8%A1%A1%E7%9A%84%E6%9C%80%E5%B0%91%E4%B8%A2%E5%BC%83%E6%AC%A1%E6%95%B0.md) | 🟡 中等 | 数组 · 哈希表 · 滑动窗口 | [LeetCode](https://leetcode.cn/problems/minimum-discards-to-balance-inventory/) |
| 4032 | [至多 K 个不同质因数集合的最长子数组](04-two-pointers/4032-%E8%87%B3%E5%A4%9AK%E4%B8%AA%E4%B8%8D%E5%90%8C%E8%B4%A8%E5%9B%A0%E6%95%B0%E9%9B%86%E5%90%88%E7%9A%84%E6%9C%80%E9%95%BF%E5%AD%90%E6%95%B0%E7%BB%84.md) | 🟡 中等 | 数组 · 哈希表 · 滑动窗口 · 数论 | [LeetCode](https://leetcode.cn/problems/longest-subarray-with-at-most-k-distinct-prime-factors/) |
<!-- INDEX:END -->

---

## 进度统计

<!-- STATS:START -->
| 题型 | 已整理题数 |
| :--- | ---: |
| 双指针与滑动窗口 | 23 |
| **合计** | **23** |

_按难度分布：简单 2 · 中等 21 · 困难 0_
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
