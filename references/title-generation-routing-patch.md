# 标题段路由补丁

> 本文件是 `title-generation.md` 的路由补丁，不替代原始标题生成规则。
> 标题段开始前先读本文件，用于判断当前标题任务应该走哪条路径。

## 一、先分类，再取标题

方比比标题任务开始时，先判断内容形态：

| 内容形态 | 判断特征 | 优先路径 | 默认句式 |
|---|---|---|---|
| 情感口播 | 妈妈、母子、亲情、红包、礼物、花钱、低调家风、潮汕妈妈、孩子长大 | `references/title-generation-emotional-patch.md` + `references/title-generation-emotional-handbook.md` | `年入百万00后 + 钩子` |
| 小号老板 Vlog | 员工视角、老板日常、团队、会议、大会、出差、公司、创业、网红老板 | `references/title-generation-boss-vlog.md` + `references/title-generation-boss-vlog-handbook.md` | 不固定句式，按内容定制 |

## 二、情感口播路径

如果判断为情感口播：

1. 先读取 `references/title-generation-emotional-patch.md`。
2. 再读取 `references/title-generation-emotional-handbook.md`。
3. 保留 `年入百万00后 + 钩子` 的 IP 锚点。
4. 优先抓妈妈粉会点赞转发的关系张力：妈妈 + 钱、妈妈 + 礼物、妈妈 + 低调、妈妈 + 家风、妈妈 + 孩子长大。
5. 主标题负责点击，不要提前讲答案；副标题和收尾可以更温情、更金句。

## 三、小号老板 Vlog 路径

如果判断为小号老板 Vlog：

1. 先读取 `references/title-generation-boss-vlog.md`。
2. 再读取 `references/title-generation-boss-vlog-handbook.md`。
3. 不强行套 `年入百万00后` 固定句式。
4. 优先使用四要素：人物关系 + 事件 + 冲突 + 悬念。
5. 目标是扩张方比比老板人设宽度，允许更网感、更外放。

## 四、video-title-gen 的融合边界

`video-title-gen` 是通用视频标题能力，只作为补充，不作为方比比标题主系统。

可以吸收：
- 悬念型
- 数字型
- 情感型
- 痛点型
- 对比型
- 热点型

不能裸用：
- 通用标题模板
- 泛平台口号
- 与方比比人设冲突的表达

使用原则：

- 情感口播：`video-title-gen` 只补点击感和平台感，不能覆盖 06 手册。
- 小号老板 Vlog：`video-title-gen` 只补风格变体，不能覆盖 08 手册。
- 方比比 IP 方向永远优先于通用标题方法。

## 五、历史 Check 的读取边界

标题生成的主流程读 `references/title-generation.md`。如果任务命中红包、礼物、妈妈低调、家庭主心骨、妈妈报喜不报忧等已沉淀题材，或用户要求“按之前 check 再看一下”，再读取：

- `references/title-generation-case-checks.md`

后续新增标题 check 写入该文件，不继续堆进 `title-generation.md`。
