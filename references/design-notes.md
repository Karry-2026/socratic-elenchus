# 设计依据：这套规则为什么这么定

> 给维护者和好奇的读者。操作在 `SKILL.md`，这里只解释「为什么」。

## 1. elenchus 不是「一直反问」

Vlastos 的最小定义给了三条硬约束：

> "Socratic elenchus is a search for moral truth by question-and-answer adversary argument in which a thesis is debated only if asserted as the answerer's own belief and is regarded as refuted only if its negation is deduced from his own beliefs."
> —— Gregory Vlastos, *The Socratic Elenchus* (1983), 重印于 *Socratic Studies* (1994)。**页码未核验**：转述自多份二次文献，未见原书，引用时须对原书复核。

拆开：① 靶子必须是**回答者本人**的信念；② 反驳只能从**他自己同意**的前提推出；③ 结论的作用范围仅限「这组信念不能同时成立」。所以 `SKILL.md` 里「只检验本人信念」「不引入未同意的前提」不是风格，是定义。

## 2. 为什么禁止说「所以你错了」

标准 elenchus 有四步：断言 p → 取得 q、r 的同意 → 论证 q∧r 蕴涵 not-p → **宣布 p 为假**。第 4 步正是被质疑的一步，哲学史上叫 *the problem of the Socratic elenchus*：

> "The problem is how Socrates can claim that position W is false, when the only thing he has established is its inconsistency with other premises whose truth he has not tried to establish in the elenchus."
> —— [IEP, *Socrates*, §3](https://iep.utm.edu/socrates/)

能成立的只有「合取不一致」，不能成立的是「哪一条为假」。所以 skill 只允许输出冲突清单，判定权交还用户。

## 3. 判定权为什么归回答者

> "Socrates' partner … must answer every question according to his own beliefs, and the partner (not the audience if there is one) judges the outcome."
> —— [SEP, *Plato's Shorter Ethical Works*, §2](https://plato.stanford.edu/entries/plato-ethics-shorter/)

这不是客气，是方法的构成条件：elenchus 的说服力来自「用你自己的前提把你逼到墙角」，一旦由提问者宣判，它就退化成辩论术。

## 4. 为什么 aporia 是合格结果

《美诺》把困惑称作「电鳐的麻痹」，并明确算作进步：

> "he has a difficulty, and neither knows nor fancies that he knows." / "Is he not better off in knowing his ignorance?"
> —— Plato, *Meno* 84a–b（Jowett 译）

但 aporia 要成立需要三件事：用户**自己**说出「我还不知道」；他**能复述失败的结构**（哪些候选被排除、为什么）；留下**下一步**。《欧悌甫戎》结尾以「Another time, Socrates」收场，就是没有出口的反面教材。这就是 `SKILL.md` 把「精确的未解问题」列为交付物的原因。

## 5. 反讽不得用于欺骗

> "at a minimum, Socrates's irony consisted in his saying that he knew nothing of importance and wanted to listen to others, yet keeping the upper hand in every discussion."
> —— [SEP, *Socrates*, §1](https://plato.stanford.edu/entries/socrates/)

「我不确定，你怎么看」只有在提问者**真的准备被说服**时才是反讽；用来套取立场再回头一击，按 Vlastos 的标准就是 shamming / lying。skill 不写「strategically feign ignorance」这类技巧，原因在此。

## 6. 引用纪律

- 区分事实 / 解释 / 价值判断，不把三者混成一句话。
- 不把自己的生成呈现为引文。
- 引柏拉图给篇名 + Stephanus 页码；不确定就说不确定。

## 参考

- Vlastos, *The Socratic Elenchus*（1983；重印 *Socratic Studies*, 1994）
- [SEP, *Plato's Shorter Ethical Works*](https://plato.stanford.edu/entries/plato-ethics-shorter/)
- [SEP, *Socrates*](https://plato.stanford.edu/entries/socrates/)
- [IEP, *Socrates*](https://iep.utm.edu/socrates/)
- Plato, *Euthyphro* / *Meno* / *Apology*（Jowett 译，classics.mit.edu）
