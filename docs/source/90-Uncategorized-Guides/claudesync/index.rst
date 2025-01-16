Claude Sync
==============================================================================
`Claude Sync <https://github.com/jahwag/ClaudeSync>`_ 是一个可以将本地文件同步到 Claude Project 中的 Knowledge Base 的一个工具. 一直以来 Claude 官方可能是出于担心 Claude Project 的 API 功能包括创建 Project, 更新 Knowledge Base 功能被人滥用变成 Multi Tenant 的服务, 所以不想将其开放给用户. 而 Claude Sync 工具的作者对网页版 Claude Project 进行了彻底分析, 找到了官方隐藏的 API 以及是如何用 Cookie 来进行登录的, 于是在此基础上开发了这个工具从而实现了将其自动化.

这个工具有一个核心风险是 `Anthropic Term of Service <https://www.anthropic.com/legal/consumer-terms>`_, 如果你使用了官方没有允许的 API 进行自动化行为, 官方是有权利将你的账号封禁的. 官方并没有对这个工具进行评价, 态度未知, 所以使用这个工具的时候要自负风险.

我个人对这个工具的源码进行分析后得出一个观点, 这种对类 Claude Project 项目的 AI 项目管理本质上包含两个模块:

1. 对 Project 的 metadata, 包含名字, Description, Instruction 进行增删插改的 API.
2. 把所有需要的文件整理到一个文件夹 (广义概念上的) 的知识提取器.

这个作者可能缺乏经验, 并没有将这两个模块解耦合而是揉进了一个库中. 想象一下, 如果这两个模块分别提供, 我们使用知识提取器将所有文件整理到一个文件夹中以后, 就完全可以手动的将其上传到 Claude Project 中, 而不需要使用这个工具. 这样就避免了风险. 而如果哪天官方同意, 我们就再使用 API 将其同步到 Claude Project 中既可. 这样做才更佳灵活.

受此启发, 我觉得更为通用的工具应该是这个知识提取器, 通过某种简单的方式能将各种系统中的知识提取到一个 "目录" 下, 这就已经解决了 90% 的问题. 至于如何给 AI 装上这个知识库, 以后可能可以用 Claude Project 的 API 进行上传, 也可以写入到各种知识库向量数据中, 也可以存到 AWS S3 这种对象存储中. 这之后就可以各种玩了.
