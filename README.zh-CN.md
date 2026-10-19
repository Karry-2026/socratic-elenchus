# socratic-elenchus

一个给 AI 用的苏格拉底式反诘 skill：它不给你答案，它让你自己的信念露出形状。

版本 1.0.0 · 适配 DSH 本地 skill provider（`.agents/skills` 或 `.dsh/skills`）；其他宿主尚未验证。

## 它是什么

一份按需加载的说明书，把柏拉图早期对话里的 **elenchus（反诘法）** 跑成一个五步循环：

**取靶子 → 澄清定义 → 用反例击穿 → 摆出矛盾 → 修订，或收在 aporia。**

它不是「苏格拉底人格」，是一套带硬规则的流程：一次只问一个问题、只检验你本人相信的东西、提问者永远不下判决、复述时引用你的原话。

## 它做什么

- 把一句模糊的判断（「我觉得 X 是 Y」）压成一句可被检验的话。
- 逼抽象词落地：给我一个能用来判断任何情况的标准。
- 把矛盾摆成**一句冲突陈述**，不是宣布哪一条为假。
- 允许「一个精确的未解问题」作为结果。没有结论也是合格产出。

## 它不做什么

- 不教有标准答案的题（数学、代码、考试）——那种直接问解释。
- 不做心理治疗、法律、医疗、投资建议；出现危机信号会停止追问。
- 不做「抬杠式反问」，也不主持多人研讨或课堂。
- 不写「永不回答」：你说「直接告诉我」，它给答案并标注不确定处。

## 安装

把文件夹放到被扫描的 skills 目录下，让 `SKILL.md` 位于该位置：

```text
<项目>/.agents/skills/socratic-elenchus/SKILL.md
<项目>/.dsh/skills/socratic-elenchus/SKILL.md
~/.agents/skills/socratic-elenchus/SKILL.md
```

发下一条消息（或新开一个会话），它就会出现在技能目录里。

平铺成 `socratic-elenchus.md` 也能被 DSH 本地 skill provider 加载，但那样没有同级 `references/` 目录，可选参考文件不可用；建议用文件夹形式。

## 怎么用

```text
帮我检验一下：我觉得好内容就是有人看的内容。

用苏格拉底的方式问我：我们团队应该更早上线。

这段话主张远程办公会毁掉文化——这是在论证，还是在断言？
```

也可以直接输入 `/socratic-elenchus` 调用。

## 文件结构

```text
SKILL.md                    操作流程，中文版（内容以此为准）
SKILL.en.md                 同一套流程的英文版（可与中文版互换）
references/design-notes.md  为什么这么定（elenchus、aporia、判定权）
references/decision.md      可选工具：现实条件、替换测试、复合排序、档位细节
references/question-types.md 九类问题自查表（卡住时换哪类问法）
examples/                   四段示例（中文），英文版在 examples/en/
docs/design.md              设计决策，比规则高一层
docs/rubric.md              10 维评测 rubric
docs/self-audit.md          两轮审查发现了什么、还剩什么
scripts/validate.py         结构校验（frontmatter、链接、一次一问、中英对齐）
test/scenarios.md           五个固定行为场景
test/RESULTS.md             实跑结果：得分、证据、发现
```

`SKILL.md` 与 `SKILL.en.md` 内容等价：中文用户直接用前者；宿主需要英文说明书时，把 `SKILL.en.md` 覆盖成 `SKILL.md` 即可。

## 参与

小修（错字、表述更清楚）欢迎直接提 PR。改规则请先开 issue：这里的每条规则都在承重，放松一条，skill 就会退回成审讯。见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 协议

MIT，见 [LICENSE](LICENSE)。
