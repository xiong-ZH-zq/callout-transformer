from callout_transformer.utils import REGEX_CALLOUT_BLOCKS
import re



test = """我们把事件 $A$ 定义为 $\varOmega$ 的一个子集，事件的发生等价于其中的样本点有至少一个发生. 但是，并不是一切子集都是事件，如果将**不可测集合**也作为事件，将会出现难以克服的困难.

### $\sigma$ 域和事件域

>[!note] 定义： $\sigma$ 域
> 空间 $\varOmega$ 上满足如下三个要求的集类 $\mathscr{F}$ 为 $\sigma$ **域**，也称为 $\sigma$ **代数**:
> 1. $\varOmega\in \mathscr{F}$ ；
> 2. 若 $A\in \mathscr{F}$ ，则 $\overline{A}\in \mathscr{F}$ ；
> 3. 若 $A_n\in \mathscr{F},n=1,2,\cdots$ ，则 $\displaystyle\bigcup_{n=1}^\infty A_n \in \mathscr{F}$ .

$\sigma$ 域保证了逆运算和可列次并运算的封闭性，那么根据 De Morgan 律和差运算的交并表示，可以判断逆、并、交、差都可列次运算封闭。

例如，$\mathscr{F}=\left\lbrace \varnothing,\varOmega \right\rbrace$ 为事件域，但是此时**只有** $\varnothing$ 和 $\varOmega$ 为事件，其余的样本点均不为事件. 

- 最小的 $\sigma$ 域：$\left\lbrace \varnothing, \varOmega \right\rbrace$ ;
- 最大的 $\sigma$ 域：$\left\lbrace A| A\subseteq \varOmega  \right\rbrace$ ；
- 包含事件 $A$ 的最小 $\sigma$ 域为： $\left\lbrace \varnothing,A, \overline{A}, \varOmega \right\rbrace$ .

>[!faq] 例题：包含 $\mathscr{G}$ 的最小 $\sigma$ 域
>证明：给定 $\varOmega$ 的一个非空集类 $\mathscr{G}$ ，必存在唯一的一个 $\varOmega$ 上的 $\sigma$ 域 $\mathfrak{m}(\mathscr{G})$ ，满足如下两个性质：
>(1) 包含 $\mathscr{G}$ ；
>(2) 若有其它 $\sigma$ 域包含 $\mathscr{G}$ ，则必然包含 $\mathfrak{m}(\mathscr{G})$ .
>也就是说，$\mathfrak{m}(\mathscr{G})$ 为包含 $\mathscr{G}$ 的最小 $\sigma$ 域. 也称为 $\mathscr{G}$ **产生的** $\sigma$ 域.

首先证明存在包含 $\mathscr{G}$ 的 $\sigma$ 域，由于 $\varOmega$ 的一切子集构成的集类包含了 $\mathscr{G}$ ，并且易知其为 $\sigma$ 域，因此存在性得证.

现在取一切"""

OBSIDIAN = re.compile(REGEX_CALLOUT_BLOCKS["obsidian"],flags=re.M)

result = OBSIDIAN.search(test)

if result:
    print("成功")
    print(result.group())