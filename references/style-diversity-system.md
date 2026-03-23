# Style Diversity System

## 目标

把“样式多样性”从临场发挥，升级成可配置、可分配、可复检的工作流能力。

这份方法综合吸收了两个参考方向：

- `ppt-agent-main`
  - 强在风格令牌、页型覆盖、评分门槛
- `ppt-agent-workflow-san-main`
  - 强在叙事页型样片和页面角色差异

## 一. 多样性来自三层，而不是模板数量

真正可复用的样式系统，至少要有三层：

1. 风格令牌
2. 页型分配
3. 质量门槛

### 1. 风格令牌

每套 deck 都应先定义：

- `mood`
- `color_scheme`
- `typography`
- `card_style`
- `gradients`
- `elevation`
- `decoration`
- `slide_type_overrides`

### 2. 页型分配

不要只说“这是一套科技风 PPT”，还要说明：

- 哪一页是开场页
- 哪一页是核心判断页
- 哪一页是场景拆分页
- 哪一页是飞轮 / 流程 / 系统图
- 哪一页是风险页
- 哪一页是结尾收束页

### 3. 质量门槛

每页都应被判断：

- 是否可读
- 是否平衡
- 是否密度过载
- 是否和前后页过于相似

## 二. 先定义风格族，不要只写“高级感”

推荐先选一个风格族，再按当前主题重建颜色。

### 常用风格族

- `business`
- `tech`
- `creative`
- `minimal`
- `security-report`
- `editorial-tech`
- `product-launch`

## 三. 叙事页型族

从 `ppt-agent-workflow-san-main` 可以直接吸收的一点是：

**好的 deck 不是“同一模板换内容”，而是“不同页面角色各有自己的表达语法”。**

推荐页型族：

### 1. `cover`

- 全幅开场
- 低密度
- 强标题和品牌锚点

### 2. `core_conclusion`

- 一页只打一个核心判断
- 大结论条 + 3-4 个支撑点

### 3. `positioning`

- 定位页 / 为什么它是一个新变量
- 适合主张 + 对照逻辑

### 4. `users_scenarios`

- 左侧人群 / 标签
- 右侧场景 / 入口
- 适合“人群 + 用法”的双区拆分

### 5. `growth_flywheel`

- 中央结构图主导
- 周围步骤卡 + 右侧判断栏

### 6. `comparison`

- 表格式对比 / 竞品对比 / 正反做法

### 7. `risks`

- 风险条 + 多风险卡并列
- 适合横向风险展开

### 8. `summary`

- 结尾判断条
- watchouts / 行动项 / 最终收束

### 9. `process`

- 编译管线 / 流水线 / 回环修复

### 10. `matrix`

- 象限 / 迁移范式 / 分类地图

### 11. `dashboard`

- 数据看板 / 指标卡 / 漏斗

### 12. `system_diagram`

- 职责边界 / 闭环 / 架构关系图

## 四. Deck 节奏必须先写进文件

开始逐页画图前，先写 `page_family_plan.md`。

最低字段：

- Slide 编号
- 页面角色
- 页面类型
- 信息密度
- 主要模板参考
- 主要强调方式

## 五. 节奏硬规则

- 连续两页以内可以同族，但不要连续三页同族
- 相邻页至少变化 2 项：
  - 信息密度
  - 卡片语法
  - 背景处理
  - 主要强调方式
  - 图形方向
- 8-15 页 deck 至少包含：
  - 1 页低密度开场页
  - 1 页核心判断页
  - 1 页流程或飞轮页
  - 1 页矩阵或对比页
  - 1 页风险或限制页
  - 1 页总结收束页

## 六. 模板的正确用途

模板应服务页型，而不是反过来绑死整套 deck。

### 推荐做法

- 开场页选开场母版
- 流程页选 process 母版
- 指标页选 dashboard 母版
- 范式页选 matrix 母版
- 收束页选 summary 母版

### 错误做法

- 整套都用一个深色圆角卡模板
- 只通过换颜色制造“变化”

## 七. 评分门槛

可直接吸收 `ppt-agent-main` 的审查结构：

- Layout Balance: 25%
- Readability: 25%
- Typography: 20%
- Information Density: 20%
- Color Harmony: 10%

通过门槛建议：

- 总分 `>= 7.0`
- Layout Balance `>= 6`
- Readability `>= 6`
- 无 critical issue

修正语义：

- `>= 7.0`：通过
- `5.0 - 6.9`：允许 1-2 轮定向修复
- `3.0 - 4.9`：优先换结构，不要只挪字
- `< 3.0`：直接重做页型

## 八. 对当前 skill 的直接要求

应把以下内容写成显式步骤：

1. 先定风格族，再写 `style_draft.md`
2. 在 `design_spec.md` 中写风格令牌和 `slide_type_overrides`
3. 在 `page_family_plan.md` 中先分配页型和节奏
4. 候选页不仅要换风格，也要换页型语法
5. deck-level review 不只查重叠，还要查是否“连续多页同构”

## 九. 一句话结论

样式多样性真正来自：

- 风格令牌明确
- 页面角色明确
- 页型分配明确
- 跨页节奏明确
- 质量门槛明确
