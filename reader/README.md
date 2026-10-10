# Reader — 阅读视图

这是《独立游戏英雄传说》的**阅读界面**，不是新的事实源，也不是书稿本体。

## Canonical source

页面只消费 `book/` 下的 Markdown 原文：

- `book/README.md`（首页，同时提供阅读顺序）；
- `book/chapters/*.md`；
- `book/profiles/*.md`；
- 由章节正文链接到的 Case / Evidence / Claim 文件。

页面本身不得维护：

- 章节清单与顺序；
- 正文文本；
- 标题；
- 阅读进度以外的任何事实。

如果页面和 Markdown 冲突，以 Markdown 为准。正文不因为进了阅读页而发生任何改写。

## 当前能力

v0 支持：

- 以 `book/README.md` 为首页，目录即入口；
- 点击内部 `.md` 链接在原位打开，不跳走；
- hash 路由（`#book/chapters/...`），可分享、可前进后退；
- 上一节 / 下一节，顺序取自 `book/README.md` 中链接的首次出现顺序；
- 表格、列表、引用块、加粗、行内代码的渲染（书稿实际用到的子集）；
- 跟随系统的明暗配色；
- 零外部资源，不加载 CDN、字体或第三方脚本。

不做的事：不生成 EPUB / PDF，不复制一份正文进页面，不发明第二套章节顺序。

## 本地使用

推荐在仓库根目录启动静态服务器：

```bash
python -m http.server 8000
```

然后打开：

```text
http://localhost:8000/reader/
```

直接双击 `index.html` 时，浏览器会阻止 `file://` 页面读取相邻文件；页面会回退到 GitHub `main` 的 raw 内容。这只适合阅读已经合并的正文，不能预览尚未合并的分支。

## 为什么现在不直接开 GitHub Pages

与 `explorer/README.md` 相同：先验证这个阅读形态是否真的比在 GitHub 上一章一章点开更好用，再决定是否需要部署。部署基础设施不应先于真实消费需求。

## 边界

- 阅读页是 **view**。它改变阅读顺序与呈现密度，不产生 canonical fact。
- `book/chapters/*.md` 仍受 `book/BOOK-ARCHITECTURE.md` 的写作规则约束；阅读页不豁免任何一条。
- 读者层的后台术语边界由 `tools/chapter_copy_lint.py` 在 CI 中检查，与本页无关。
- 若正文里出现指向仓库外的链接，页面按普通链接处理，不接管。
