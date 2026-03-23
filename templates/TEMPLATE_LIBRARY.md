# Template Library

这是一组可直接参考的原创 SVG 母版，用来降低候选页阶段的随机性。

它们不是“照抄即交付”的成品，而是经过归纳后的结构骨架。后续真正做 PPT 时，应优先从这些母版中挑选 3 个方向生成候选页，再让用户选择。

但模板库不是样式系统的全部。真正的多样性还应来自：

- 风格令牌
- 页面类型覆盖
- 跨页节奏分配
- 质量复检门槛

可视化索引页：

- [`TEMPLATE_INDEX.html`](./TEMPLATE_INDEX.html)

## 使用原则

- 先按主题、受众、场景筛选 3-6 个母版
- 再从中挑 3 个差异明显的方向生成候选页
- 模板保留结构，文案必须按当前任务重写
- 模板默认只绑定结构，不绑定颜色；颜色系统要按当前主题单独设计
- 模板选择应服务 `page_family_plan.md`，而不是整套只认一个模板
- 若模板不完全适配，可混搭骨架，但必须记录到 `template_choice.md`
- 若当前任务出现新页面类型，先补模板，再开始大规模生成

## 模板清单

### 01. `01_dark_signal_opening.svg`

- 类型：深色叙事开场页
- 适合：技术分享开场、风险主题、方法论主张页
- 特征：大标题 + 结论卡 + 信号路径 + 标签胶囊

### 02. `02_consulting_split_argument.svg`

- 类型：咨询式论证页
- 适合：为什么做、问题定义、三段式论证
- 特征：三栏论证卡 + 底部路径线 + 克制配色

### 03. `03_process_compiler_pipeline.svg`

- 类型：流程/编译管线页
- 适合：方法流程、阶段拆解、从输入到交付
- 特征：主轨道 + 回环修复 + 角色分层说明

### 04. `04_editorial_compare.svg`

- 类型：编辑式对比页
- 适合：反模式 vs 正确做法、旧方案 vs 新方案
- 特征：左右对照 + 注解栏 + 细线辅助

### 05. `05_bento_metric_dashboard.svg`

- 类型：指标/看板页
- 适合：指标解释、数据闭环、运营监控
- 特征：数据卡 + 漏斗区 + 看板式网格

### 06. `06_quadrant_pattern_map.svg`

- 类型：二维矩阵/范式页
- 适合：场景迁移、方法分类、风险定位
- 特征：象限图 + 标签点 + 侧边结论区

### 07. `07_story_chapter_break.svg`

- 类型：章节切换/观点强化页
- 适合：章节页、观点转折、强记忆点页
- 特征：大号编号 + 垂直标题 + 重点引言

### 08. `08_summary_manifesto.svg`

- 类型：总结收束页
- 适合：结论页、原则页、行动页
- 特征：原则组块 + 收束陈述 + 金句区

### 09. `09_nature_timeline_band.svg`

- 类型：自然渐变时间线页
- 适合：历史沿革、阶段里程碑、品牌历程
- 特征：深绿渐变底 + 横向年份主轴 + 上下交错节点

### 10. `10_nature_data_split.svg`

- 类型：自然渐变数据拆分页
- 适合：图表 + 表格 + 两条解读并列
- 特征：左侧条形图，右侧表格，底部双结论区

### 11. `11_nature_loop_infographic.svg`

- 类型：自然渐变环状信息图
- 适合：循环流程、生态系统、四模块关系图
- 特征：细线闭环 + 中央图标节点 + 四角文本说明

### 12. `12_core_conclusion_banner.svg`

- 类型：核心结论页
- 适合：一页讲清一个判断、战略结论、观点先行页
- 特征：大判断横幅 + 四个支撑卡 + 底部一句话结论条

### 13. `13_users_scenarios_split.svg`

- 类型：人群与场景拆分页
- 适合：目标用户、画像标签、使用场景、入口分析
- 特征：左侧标签画像区 + 右侧场景堆叠区 + 底部收束条

### 14. `14_growth_flywheel_signal.svg`

- 类型：增长飞轮 / 闭环页
- 适合：增长逻辑、循环系统、推荐飞轮、机制演进
- 特征：中心飞轮 + 四步卡 + 右侧判断栏

### 15. `15_risks_strip_grid.svg`

- 类型：风险栅格页
- 适合：风险拆解、限制条件、挑战列表、治理重点
- 特征：顶部风险条 + 多风险卡横向展开 + 底部总结条

## 模板筛选建议

- 需要“技术叙事 + 高压感”时：
  - `01_dark_signal_opening.svg`
  - `03_process_compiler_pipeline.svg`
  - `08_summary_manifesto.svg`

- 需要“管理层沟通 + 克制”时：
  - `02_consulting_split_argument.svg`
  - `05_bento_metric_dashboard.svg`
  - `08_summary_manifesto.svg`

- 需要“结构图为主 + 方法论清楚”时：
  - `03_process_compiler_pipeline.svg`
  - `04_editorial_compare.svg`
  - `06_quadrant_pattern_map.svg`

- 需要“自然渐变 + 轻信息图 + 模块丰富”时：
  - `09_nature_timeline_band.svg`
  - `10_nature_data_split.svg`
  - `11_nature_loop_infographic.svg`

## Deck 组合建议

- 不要整套只用同一模板家族
- 开场 / 方法 / 对比 / 指标 / 总结，至少应覆盖 3 种以上模板语法
- 推荐把模板映射到页面类型：
  - `cover`: `01`, `07`
  - `core_conclusion`: `02`, `08`
  - `core_conclusion / claim page`: `12`
  - `process`: `03`
  - `comparison`: `04`
  - `dashboard`: `05`, `10`
  - `matrix`: `06`
  - `timeline`: `09`
  - `system_diagram`: `11`
  - `users_scenarios`: `13`
  - `growth_flywheel`: `14`
  - `risks`: `15`

- 若 deck 连续三页都来自同一模板家族，应主动打断节奏

## 来源说明

本模板库不是从第三方模板站直接下载后重分发。

它是基于公开模板站和演示页面观察后，抽象出的原创 SVG 母版。参考来源见：

- [`../references/template-inspirations.md`](../references/template-inspirations.md)
- 可视化索引页见：[`TEMPLATE_INDEX.html`](./TEMPLATE_INDEX.html)
