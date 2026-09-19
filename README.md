# LeetCode Notes 📒

> 我的 LeetCode 解题笔记仓库。
> 每道题的**思路剖析、最优解法、复杂度评估与优化过程**都沉淀在这里 —— 不只是"抄答案"，而是记录**为什么这样解、还能不能更好**。

![Notes](https://img.shields.io/badge/notes-63-blue)
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
| 76 | [最小覆盖子串](04-two-pointers/76-%E6%9C%80%E5%B0%8F%E8%A6%86%E7%9B%96%E5%AD%90%E4%B8%B2.md) | 🔴 困难 | 哈希表 · 字符串 · 滑动窗口 | [LeetCode](https://leetcode.cn/problems/minimum-window-substring/) |
| 209 | [长度最小的子数组](04-two-pointers/209-%E9%95%BF%E5%BA%A6%E6%9C%80%E5%B0%8F%E7%9A%84%E5%AD%90%E6%95%B0%E7%BB%84.md) | 🟡 中等 | 数组 · 二分查找 · 前缀和 · 滑动窗口 | [LeetCode](https://leetcode.cn/problems/minimum-size-subarray-sum/) |
| 632 | [最小区间](04-two-pointers/632-%E6%9C%80%E5%B0%8F%E5%8C%BA%E9%97%B4.md) | 🔴 困难 | 数组 · 哈希表 · 滑动窗口 · 排序 · 堆（优先队列） | [LeetCode](https://leetcode.cn/problems/smallest-range-covering-elements-from-k-lists/) |
| 713 | [乘积小于 K 的子数组](04-two-pointers/713-%E4%B9%98%E7%A7%AF%E5%B0%8F%E4%BA%8E%20K%20%E7%9A%84%E5%AD%90%E6%95%B0%E7%BB%84.md) | 🟡 中等 | 数组 · 滑动窗口 | [LeetCode](https://leetcode.cn/problems/subarray-product-less-than-k/) |
| 825 | [适龄的朋友](04-two-pointers/825-%E9%80%82%E9%BE%84%E7%9A%84%E6%9C%8B%E5%8F%8B.md) | 🟡 中等 | 数组 · 双指针 · 滑动窗口 · 计数 | [LeetCode](https://leetcode.cn/problems/friends-of-appropriate-ages/) |
| 904 | [水果成篮](04-two-pointers/904-%E6%B0%B4%E6%9E%9C%E6%88%90%E7%AF%AE.md) | 🟡 中等 | 数组 · 哈希表 · 滑动窗口 | [LeetCode](https://leetcode.cn/problems/fruit-into-baskets/) |
| 930 | [和相同的二元子数组](04-two-pointers/930-%E5%92%8C%E7%9B%B8%E5%90%8C%E7%9A%84%E4%BA%8C%E5%85%83%E5%AD%90%E6%95%B0%E7%BB%84.md) | 🟡 中等 | 数组 · 滑动窗口 · 前缀和 · 哈希表 | [LeetCode](https://leetcode.cn/problems/binary-subarrays-with-sum/) |
| 992 | [K 个不同整数的子数组](04-two-pointers/992-K%E4%B8%AA%E4%B8%8D%E5%90%8C%E6%95%B4%E6%95%B0%E7%9A%84%E5%AD%90%E6%95%B0%E7%BB%84.md) | 🔴 困难 | 数组 · 哈希表 · 滑动窗口 · 计数 | [LeetCode](https://leetcode.cn/problems/subarrays-with-k-different-integers/) |
| 1004 | [最大连续1的个数 III](04-two-pointers/1004-%E6%9C%80%E5%A4%A7%E8%BF%9E%E7%BB%AD1%E7%9A%84%E4%B8%AA%E6%95%B0III.md) | 🟡 中等 | 数组 · 二分查找 · 前缀和 · 滑动窗口 | [LeetCode](https://leetcode.cn/problems/max-consecutive-ones-iii/) |
| 1052 | [爱生气的书店老板](04-two-pointers/1052-%E7%88%B1%E7%94%9F%E6%B0%94%E7%9A%84%E4%B9%A6%E5%BA%97%E8%80%81%E6%9D%BF.md) | 🟡 中等 | 数组 · 滑动窗口 | [LeetCode](https://leetcode.cn/problems/grumpy-bookstore-owner/) |
| 1100 | [长度为 K 的无重复字符子串](04-two-pointers/1100-%E9%95%BF%E5%BA%A6%E4%B8%BAK%E7%9A%84%E6%97%A0%E9%87%8D%E5%A4%8D%E5%AD%97%E7%AC%A6%E5%AD%90%E4%B8%B2.md) | 🟡 中等 | 哈希表 · 字符串 · 滑动窗口 | [LeetCode](https://leetcode.cn/problems/find-k-length-substrings-with-no-repeated-characters/) |
| 1151 | [最少交换次数来组合所有的 1](04-two-pointers/1151-%E6%9C%80%E5%B0%91%E4%BA%A4%E6%8D%A2%E6%AC%A1%E6%95%B0%E6%9D%A5%E7%BB%84%E5%90%88%E6%89%80%E6%9C%89%E7%9A%841.md) | 🟡 中等 | 数组 · 滑动窗口 | [LeetCode](https://leetcode.cn/problems/minimum-swaps-to-group-all-1s-together/) |
| 1156 | [单字符重复子串的最大长度](04-two-pointers/1156-%E5%8D%95%E5%AD%97%E7%AC%A6%E9%87%8D%E5%A4%8D%E5%AD%90%E4%B8%B2%E7%9A%84%E6%9C%80%E5%A4%A7%E9%95%BF%E5%BA%A6.md) | 🟡 中等 | 哈希表 · 字符串 · 滑动窗口 | [LeetCode](https://leetcode.cn/problems/swap-for-longest-repeated-character-substring/) |
| 1176 | [健身计划评估](04-two-pointers/1176-%E5%81%A5%E8%BA%AB%E8%AE%A1%E5%88%92%E8%AF%84%E4%BC%B0.md) | 🟢 简单 | 数组 · 滑动窗口 | [LeetCode](https://leetcode.cn/problems/diet-plan-performance/) |
| 1208 | [尽可能使字符串相等](04-two-pointers/1208-%E5%B0%BD%E5%8F%AF%E8%83%BD%E4%BD%BF%E5%AD%97%E7%AC%A6%E4%B8%B2%E7%9B%B8%E7%AD%89.md) | 🟡 中等 | 字符串 · 滑动窗口 · 前缀和 · 二分查找 | [LeetCode](https://leetcode.cn/problems/get-equal-substrings-within-budget/) |
| 1234 | [替换子串得到平衡字符串](04-two-pointers/1234-%E6%9B%BF%E6%8D%A2%E5%AD%90%E4%B8%B2%E5%BE%97%E5%88%B0%E5%B9%B3%E8%A1%A1%E5%AD%97%E7%AC%A6%E4%B8%B2.md) | 🟡 中等 | 字符串 · 滑动窗口 · 计数 | [LeetCode](https://leetcode.cn/problems/replace-the-substring-for-balanced-string/) |
| 1248 | [统计「优美子数组」](04-two-pointers/1248-%E7%BB%9F%E8%AE%A1%E3%80%8C%E4%BC%98%E7%BE%8E%E5%AD%90%E6%95%B0%E7%BB%84%E3%80%8D.md) | 🟡 中等 | 滑动窗口 · 数组 · 哈希表 · 数学 | [LeetCode](https://leetcode.cn/problems/count-number-of-nice-subarrays/) |
| 1358 | [包含所有三种字符的子字符串数目](04-two-pointers/1358-%E5%8C%85%E5%90%AB%E6%89%80%E6%9C%89%E4%B8%89%E7%A7%8D%E5%AD%97%E7%AC%A6%E7%9A%84%E5%AD%90%E5%AD%97%E7%AC%A6%E4%B8%B2%E6%95%B0%E7%9B%AE.md) | 🟡 中等 | 哈希表 · 字符串 · 滑动窗口 | [LeetCode](https://leetcode.cn/problems/number-of-substrings-containing-all-three-characters/) |
| 1493 | [删掉一个元素以后全为 1 的最长子数组](04-two-pointers/1493-%E5%88%A0%E6%8E%89%E4%B8%80%E4%B8%AA%E5%85%83%E7%B4%A0%E4%BB%A5%E5%90%8E%E5%85%A8%E4%B8%BA1%E7%9A%84%E6%9C%80%E9%95%BF%E5%AD%90%E6%95%B0%E7%BB%84.md) | 🟡 中等 | 数组 · 滑动窗口 | [LeetCode](https://leetcode.cn/problems/longest-subarray-of-1s-after-deleting-one-element/) |
| 1695 | [删除子数组的最大得分](04-two-pointers/1695-%E5%88%A0%E9%99%A4%E5%AD%90%E6%95%B0%E7%BB%84%E7%9A%84%E6%9C%80%E5%A4%A7%E5%BE%97%E5%88%86.md) | 🟡 中等 | 数组 · 哈希表 · 滑动窗口 | [LeetCode](https://leetcode.cn/problems/maximum-erasure-value/) |
| 1852 | [每个子数组的数字种类数](04-two-pointers/1852-%E6%AF%8F%E4%B8%AA%E5%AD%90%E6%95%B0%E7%BB%84%E7%9A%84%E6%95%B0%E5%AD%97%E7%A7%8D%E7%B1%BB%E6%95%B0.md) | 🟡 中等 | 数组 · 哈希表 · 滑动窗口 | [LeetCode](https://leetcode.cn/problems/distinct-numbers-in-each-subarray/) |
| 2024 | [考试的最大困扰度](04-two-pointers/2024-%E8%80%83%E8%AF%95%E7%9A%84%E6%9C%80%E5%A4%A7%E5%9B%B0%E6%89%B0%E5%BA%A6.md) | 🟡 中等 | 字符串 · 滑动窗口 · 前缀和 · 二分查找 | [LeetCode](https://leetcode.cn/problems/maximize-the-confusion-of-an-exam/) |
| 2062 | [统计字符串中的元音子字符串](04-two-pointers/2062-%E7%BB%9F%E8%AE%A1%E5%AD%97%E7%AC%A6%E4%B8%B2%E4%B8%AD%E7%9A%84%E5%85%83%E9%9F%B3%E5%AD%90%E5%AD%97%E7%AC%A6%E4%B8%B2.md) | 🟢 简单 | 哈希表 · 字符串 · 滑动窗口 | [LeetCode](https://leetcode.cn/problems/count-vowel-substrings-of-a-string/) |
| 2107 | [分享 K 个糖果后独特口味的数量](04-two-pointers/2107-%E5%88%86%E4%BA%ABK%E4%B8%AA%E7%B3%96%E6%9E%9C%E5%90%8E%E7%8B%AC%E7%89%B9%E5%8F%A3%E5%91%B3%E7%9A%84%E6%95%B0%E9%87%8F.md) | 🟡 中等 | 数组 · 哈希表 · 滑动窗口 | [LeetCode](https://leetcode.cn/problems/number-of-unique-flavors-after-sharing-k-candies/) |
| 2302 | [统计得分小于 K 的子数组数目](04-two-pointers/2302-%E7%BB%9F%E8%AE%A1%E5%BE%97%E5%88%86%E5%B0%8F%E4%BA%8E%20K%20%E7%9A%84%E5%AD%90%E6%95%B0%E7%BB%84%E6%95%B0%E7%9B%AE.md) | 🔴 困难 | 数组 · 二分查找 · 前缀和 · 滑动窗口 | [LeetCode](https://leetcode.cn/problems/count-subarrays-with-score-less-than-k/) |
| 2401 | [最长优雅子数组](04-two-pointers/2401-%E6%9C%80%E9%95%BF%E4%BC%98%E9%9B%85%E5%AD%90%E6%95%B0%E7%BB%84.md) | 🟡 中等 | 滑动窗口 · 位运算 · 数组 | [LeetCode](https://leetcode.cn/problems/longest-nice-subarray/) |
| 2495 | [乘积为偶数的子数组数](04-two-pointers/2495-%E4%B9%98%E7%A7%AF%E4%B8%BA%E5%81%B6%E6%95%B0%E7%9A%84%E5%AD%90%E6%95%B0%E7%BB%84%E6%95%B0.md) | 🟡 中等 | 数组 · 数学 · 动态规划 | [LeetCode](https://leetcode.cn/problems/number-of-subarrays-having-even-product/) |
| 2537 | [统计好子数组的数目](04-two-pointers/2537-%E7%BB%9F%E8%AE%A1%E5%A5%BD%E5%AD%90%E6%95%B0%E7%BB%84%E7%9A%84%E6%95%B0%E7%9B%AE.md) | 🟡 中等 | 数组 · 哈希表 · 滑动窗口 | [LeetCode](https://leetcode.cn/problems/count-the-number-of-good-subarrays/) |
| 2730 | [找到最长的半重复子字符串](04-two-pointers/2730-%E6%89%BE%E5%88%B0%E6%9C%80%E9%95%BF%E7%9A%84%E5%8D%8A%E9%87%8D%E5%A4%8D%E5%AD%90%E5%AD%97%E7%AC%A6%E4%B8%B2.md) | 🟡 中等 | 字符串 · 滑动窗口 | [LeetCode](https://leetcode.cn/problems/find-the-longest-semi-repetitive-substring/) |
| 2743 | [计算没有重复字符的子字符串数量](04-two-pointers/2743-%E8%AE%A1%E7%AE%97%E6%B2%A1%E6%9C%89%E9%87%8D%E5%A4%8D%E5%AD%97%E7%AC%A6%E7%9A%84%E5%AD%90%E5%AD%97%E7%AC%A6%E4%B8%B2%E6%95%B0%E9%87%8F.md) | 🟡 中等 | 哈希表 · 字符串 · 滑动窗口 | [LeetCode](https://leetcode.cn/problems/count-substrings-without-repeating-character/) |
| 2762 | [不间断子数组](04-two-pointers/2762-%E4%B8%8D%E9%97%B4%E6%96%AD%E5%AD%90%E6%95%B0%E7%BB%84.md) | 🟡 中等 | 滑窗 · 滑动窗口 · 单调队列 · 哈希表 · 数组 | [LeetCode](https://leetcode.cn/problems/continuous-subarrays/) |
| 2779 | [数组的最大美丽值](04-two-pointers/2779-%E6%95%B0%E7%BB%84%E7%9A%84%E6%9C%80%E5%A4%A7%E7%BE%8E%E4%B8%BD%E5%80%BC.md) | 🟡 中等 | 数组 · 排序 · 滑动窗口 · 双指针 · 二分查找 | [LeetCode](https://leetcode.cn/problems/maximum-beauty-of-an-array-after-applying-operation/) |
| 2799 | [统计完全子数组的数目](04-two-pointers/2799-%E7%BB%9F%E8%AE%A1%E5%AE%8C%E5%85%A8%E5%AD%90%E6%95%B0%E7%BB%84%E7%9A%84%E6%95%B0%E7%9B%AE.md) | 🟡 中等 | 滑窗 · 数组 · 哈希表 | [LeetCode](https://leetcode.cn/problems/count-complete-subarrays-in-an-array/) |
| 2875 | [无限数组的最短子数组](04-two-pointers/2875-%E6%97%A0%E9%99%90%E6%95%B0%E7%BB%84%E7%9A%84%E6%9C%80%E7%9F%AD%E5%AD%90%E6%95%B0%E7%BB%84.md) | 🟡 中等 | 数组 · 滑动窗口 | [LeetCode](https://leetcode.cn/problems/minimum-size-subarray-in-infinite-array/) |
| 2904 | [最短且字典序最小的美丽子字符串](04-two-pointers/2904-%E6%9C%80%E7%9F%AD%E4%B8%94%E5%AD%97%E5%85%B8%E5%BA%8F%E6%9C%80%E5%B0%8F%E7%9A%84%E7%BE%8E%E4%B8%BD%E5%AD%90%E5%AD%97%E7%AC%A6%E4%B8%B2.md) | 🟡 中等 | 字符串 · 滑动窗口 | [LeetCode](https://leetcode.cn/problems/shortest-and-lexicographically-smallest-beautiful-string/) |
| 2958 | [最多 K 个重复元素的最长子数组](04-two-pointers/2958-%E6%9C%80%E5%A4%9AK%E4%B8%AA%E9%87%8D%E5%A4%8D%E5%85%83%E7%B4%A0%E7%9A%84%E6%9C%80%E9%95%BF%E5%AD%90%E6%95%B0%E7%BB%84.md) | 🟡 中等 | 数组 · 哈希表 · 滑动窗口 | [LeetCode](https://leetcode.cn/problems/length-of-longest-subarray-with-at-most-k-frequency/) |
| 2962 | [统计最大元素出现至少 K 次的子数组](04-two-pointers/2962-%E7%BB%9F%E8%AE%A1%E6%9C%80%E5%A4%A7%E5%85%83%E7%B4%A0%E5%87%BA%E7%8E%B0%E8%87%B3%E5%B0%91%20K%20%E6%AC%A1%E7%9A%84%E5%AD%90%E6%95%B0%E7%BB%84.md) | 🟡 中等 | 数组 · 滑动窗口 | [LeetCode](https://leetcode.cn/problems/count-subarrays-where-max-element-appears-at-least-k-times/) |
| 3090 | [每个字符最多出现两次的最长子字符串](04-two-pointers/3090-%E6%AF%8F%E4%B8%AA%E5%AD%97%E7%AC%A6%E6%9C%80%E5%A4%9A%E5%87%BA%E7%8E%B0%E4%B8%A4%E6%AC%A1%E7%9A%84%E6%9C%80%E9%95%BF%E5%AD%90%E5%AD%97%E7%AC%A6%E4%B8%B2.md) | 🟢 简单 | 哈希表 · 字符串 · 滑动窗口 | [LeetCode](https://leetcode.cn/problems/maximum-length-substring-with-two-occurrences/) |
| 3258 | [统计满足 K 约束的子字符串数量 I](04-two-pointers/3258-%E7%BB%9F%E8%AE%A1%E6%BB%A1%E8%B6%B3%20K%20%E7%BA%A6%E6%9D%9F%E7%9A%84%E5%AD%90%E5%AD%97%E7%AC%A6%E4%B8%B2%E6%95%B0%E9%87%8F%20I.md) | 🟢 简单 | 滑动窗口 · 字符串 · 计数 | [LeetCode](https://leetcode.cn/problems/count-substrings-that-satisfy-k-constraint-i/) |
| 3298 | [统计重新排列后包含另一个字符串的子字符串数目 II](04-two-pointers/3298-%E7%BB%9F%E8%AE%A1%E9%87%8D%E6%96%B0%E6%8E%92%E5%88%97%E5%90%8E%E5%8C%85%E5%90%AB%E5%8F%A6%E4%B8%80%E4%B8%AA%E5%AD%97%E7%AC%A6%E4%B8%B2%E7%9A%84%E5%AD%90%E5%AD%97%E7%AC%A6%E4%B8%B2%E6%95%B0%E7%9B%AE%20II.md) | 🔴 困难 | 滑动窗口 · 哈希表 · 字符串 | [LeetCode](https://leetcode.cn/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-ii/) |
| 3306 | [元音辅音字符串计数 II](04-two-pointers/3306-%E5%85%83%E9%9F%B3%E8%BE%85%E9%9F%B3%E5%AD%97%E7%AC%A6%E4%B8%B2%E8%AE%A1%E6%95%B0%20II.md) | 🟡 中等 | 滑窗 · 字符串 · 哈希表 | [LeetCode](https://leetcode.cn/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/) |
| 3325 | [字符至少出现 K 次的子字符串 I](04-two-pointers/3325-%E5%AD%97%E7%AC%A6%E8%87%B3%E5%B0%91%E5%87%BA%E7%8E%B0K%E6%AC%A1%E7%9A%84%E5%AD%90%E5%AD%97%E7%AC%A6%E4%B8%B2I.md) | 🟡 中等 | 滑动窗口 · 哈希表 · 字符串 · 计数 | [LeetCode](https://leetcode.cn/problems/count-substrings-with-k-frequency-characters-i/) |
| 3439 | [重新安排会议得到最多空余时间 I](04-two-pointers/3439-%E9%87%8D%E6%96%B0%E5%AE%89%E6%8E%92%E4%BC%9A%E8%AE%AE%E5%BE%97%E5%88%B0%E6%9C%80%E5%A4%9A%E7%A9%BA%E4%BD%99%E6%97%B6%E9%97%B4I.md) | 🟡 中等 | 数组 · 滑动窗口 | [LeetCode](https://leetcode.cn/problems/reschedule-meetings-for-maximum-free-time-i/) |
| 3634 | [使数组平衡的最少移除数目](04-two-pointers/3634-%E4%BD%BF%E6%95%B0%E7%BB%84%E5%B9%B3%E8%A1%A1%E7%9A%84%E6%9C%80%E5%B0%91%E7%A7%BB%E9%99%A4%E6%95%B0%E7%9B%AE.md) | 🟡 中等 | 数组 · 排序 · 滑动窗口 · 双指针 | [LeetCode](https://leetcode.cn/problems/minimum-removals-to-balance-array/) |
| 3641 | [最长半重复子数组](04-two-pointers/3641-%E6%9C%80%E9%95%BF%E5%8D%8A%E9%87%8D%E5%A4%8D%E5%AD%90%E6%95%B0%E7%BB%84.md) | 🟡 中等 | 数组 · 哈希表 · 滑动窗口 | [LeetCode](https://leetcode.cn/problems/longest-semi-repeating-subarray/) |
| 3679 | [使库存平衡的最少丢弃次数](04-two-pointers/3679-%E4%BD%BF%E5%BA%93%E5%AD%98%E5%B9%B3%E8%A1%A1%E7%9A%84%E6%9C%80%E5%B0%91%E4%B8%A2%E5%BC%83%E6%AC%A1%E6%95%B0.md) | 🟡 中等 | 数组 · 哈希表 · 滑动窗口 | [LeetCode](https://leetcode.cn/problems/minimum-discards-to-balance-inventory/) |
| 3795 | [不同元素和至少为 K 的最短子数组长度](04-two-pointers/3795-%E4%B8%8D%E5%90%8C%E5%85%83%E7%B4%A0%E5%92%8C%E8%87%B3%E5%B0%91%E4%B8%BA%20K%20%E7%9A%84%E6%9C%80%E7%9F%AD%E5%AD%90%E6%95%B0%E7%BB%84%E9%95%BF%E5%BA%A6.md) | 🟡 中等 | 数组 · 哈希表 · 滑动窗口 | [LeetCode](https://leetcode.cn/problems/minimum-subarray-length-with-distinct-sum-at-least-k/) |
| 3859 | [统计包含 K 个不同整数的子数组](04-two-pointers/3859-%E7%BB%9F%E8%AE%A1%E5%8C%85%E5%90%AB%20K%20%E4%B8%AA%E4%B8%8D%E5%90%8C%E6%95%B4%E6%95%B0%E7%9A%84%E5%AD%90%E6%95%B0%E7%BB%84.md) | 🔴 困难 | 滑窗 · 哈希表 · 计数 | [LeetCode](https://leetcode.cn/problems/count-subarrays-with-k-distinct-integers/) |
| 4032 | [至多 K 个不同质因数集合的最长子数组](04-two-pointers/4032-%E8%87%B3%E5%A4%9AK%E4%B8%AA%E4%B8%8D%E5%90%8C%E8%B4%A8%E5%9B%A0%E6%95%B0%E9%9B%86%E5%90%88%E7%9A%84%E6%9C%80%E9%95%BF%E5%AD%90%E6%95%B0%E7%BB%84.md) | 🟡 中等 | 数组 · 哈希表 · 滑动窗口 · 数论 | [LeetCode](https://leetcode.cn/problems/longest-subarray-with-at-most-k-distinct-prime-factors/) |
| LCP 68 | [美观的花束](04-two-pointers/LCP%2068-%E7%BE%8E%E8%A7%82%E7%9A%84%E8%8A%B1%E6%9D%9F.md) | 🟡 中等 | 数组 · 滑动窗口 | [LeetCode](https://leetcode.cn/problems/1GxJYY/) |

### 二分查找 <sub>`05-binary-search`</sub>

| # | 题目 | 难度 | 标签 | 原题 |
| ---: | :--- | :--- | :--- | :-: |
| 34 | [在排序数组中查找元素的第一个和最后一个位置](05-binary-search/34-%E5%9C%A8%E6%8E%92%E5%BA%8F%E6%95%B0%E7%BB%84%E4%B8%AD%E6%9F%A5%E6%89%BE%E5%85%83%E7%B4%A0%E7%9A%84%E7%AC%AC%E4%B8%80%E4%B8%AA%E5%92%8C%E6%9C%80%E5%90%8E%E4%B8%80%E4%B8%AA%E4%BD%8D%E7%BD%AE.md) | 🟡 中等 | 数组 · 二分查找 | [LeetCode](https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/) |
| 704 | [二分查找](05-binary-search/704-%E4%BA%8C%E5%88%86%E6%9F%A5%E6%89%BE.md) | 🟢 简单 | 数组 · 二分查找 | [LeetCode](https://leetcode.cn/problems/binary-search/) |
| 744 | [寻找比目标字母大的最小字母](05-binary-search/744-%E5%AF%BB%E6%89%BE%E6%AF%94%E7%9B%AE%E6%A0%87%E5%AD%97%E6%AF%8D%E5%A4%A7%E7%9A%84%E6%9C%80%E5%B0%8F%E5%AD%97%E6%AF%8D.md) | 🟢 简单 | 二分查找 · 数组 | [LeetCode](https://leetcode.cn/problems/find-smallest-letter-greater-than-target/) |
| 1146 | [快照数组](05-binary-search/1146-%E5%BF%AB%E7%85%A7%E6%95%B0%E7%BB%84.md) | 🟡 中等 | 设计 · 二分查找 · 哈希表 | [LeetCode](https://leetcode.cn/problems/snapshot-array/) |
| 1170 | [比较字符串最小字母出现频次](05-binary-search/1170-%E6%AF%94%E8%BE%83%E5%AD%97%E7%AC%A6%E4%B8%B2%E6%9C%80%E5%B0%8F%E5%AD%97%E6%AF%8D%E5%87%BA%E7%8E%B0%E9%A2%91%E6%AC%A1.md) | 🟡 中等 | 数组 · 字符串 · 二分查找 · 排序 | [LeetCode](https://leetcode.cn/problems/compare-strings-by-frequency-of-the-smallest-character/) |
| 1385 | [两个数组间的距离值](05-binary-search/1385-%E4%B8%A4%E4%B8%AA%E6%95%B0%E7%BB%84%E9%97%B4%E7%9A%84%E8%B7%9D%E7%A6%BB%E5%80%BC.md) | 🟢 简单 | 数组 · 二分查找 · 排序 | [LeetCode](https://leetcode.cn/problems/find-the-distance-value-between-two-arrays/) |
| 2080 | [区间内查询数字的频率](05-binary-search/2080-%E5%8C%BA%E9%97%B4%E5%86%85%E6%9F%A5%E8%AF%A2%E6%95%B0%E5%AD%97%E7%9A%84%E9%A2%91%E7%8E%87.md) | 🟡 中等 | 设计 · 线段树 · 数组 · 哈希表 · 二分查找 | [LeetCode](https://leetcode.cn/problems/range-frequency-queries/) |
| 2300 | [咒语和药水的成功对数](05-binary-search/2300-%E5%92%92%E8%AF%AD%E5%92%8C%E8%8D%AF%E6%B0%B4%E7%9A%84%E6%88%90%E5%8A%9F%E5%AF%B9%E6%95%B0.md) | 🟡 中等 | 数组 · 二分查找 · 排序 | [LeetCode](https://leetcode.cn/problems/successful-pairs-of-spells-and-potions/) |
| 2389 | [和有限的最长子序列](05-binary-search/2389-%E5%92%8C%E6%9C%89%E9%99%90%E7%9A%84%E6%9C%80%E9%95%BF%E5%AD%90%E5%BA%8F%E5%88%97.md) | 🟢 简单 | 贪心 · 数组 · 二分查找 · 前缀和 · 排序 | [LeetCode](https://leetcode.cn/problems/longest-subsequence-with-limited-sum/) |
| 2529 | [正整数和负整数的最大计数](05-binary-search/2529-%E6%AD%A3%E6%95%B4%E6%95%B0%E5%92%8C%E8%B4%9F%E6%95%B4%E6%95%B0%E7%9A%84%E6%9C%80%E5%A4%A7%E8%AE%A1%E6%95%B0.md) | 🟢 简单 | 数组 · 二分查找 · 计数 | [LeetCode](https://leetcode.cn/problems/maximum-count-of-positive-integer-and-negative-integer/) |
| 2563 | [统计公平数对的数目](05-binary-search/2563-%E7%BB%9F%E8%AE%A1%E5%85%AC%E5%B9%B3%E6%95%B0%E5%AF%B9%E7%9A%84%E6%95%B0%E7%9B%AE.md) | 🟡 中等 | 数组 · 双指针 · 二分查找 · 排序 | [LeetCode](https://leetcode.cn/problems/count-the-number-of-fair-pairs/) |
| 3488 | [距离最小相等元素查询](05-binary-search/3488-%E8%B7%9D%E7%A6%BB%E6%9C%80%E5%B0%8F%E7%9B%B8%E7%AD%89%E5%85%83%E7%B4%A0%E6%9F%A5%E8%AF%A2.md) | 🟡 中等 | 二分查找 · 数组 · 哈希表 · 环形数组 · 预处理 | [LeetCode](https://leetcode.cn/problems/closest-equal-element-queries/) |
<!-- INDEX:END -->

---

## 进度统计

<!-- STATS:START -->
| 题型 | 已整理题数 |
| :--- | ---: |
| 双指针与滑动窗口 | 51 |
| 二分查找 | 12 |
| **合计** | **63** |

_按难度分布：简单 9 · 中等 48 · 困难 6_
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
