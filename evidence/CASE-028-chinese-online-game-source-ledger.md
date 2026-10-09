# CASE-028 Evidence Ledger — 中国式网游 / 648工作室

- Last verified: 2026-10-06
- Status: RESEARCHING
- Case: [`../cases/CASE-028-chinese-online-game.md`](../cases/CASE-028-chinese-online-game.md)

## E001 — 开发者 Steam 自述：2018、solo、业余时间、约五年

- Source class: P0 / developer-authored Steam post
- Title: 《中国式网游》Demo试玩即将上线！将参加6月新品节！
- Author / Institution: 项目官方 Steam 公告；正文为开发者第一人称，实名 UNKNOWN。
- Published: 2024-06-07。
- Accessed: 2026-10-05。
- URL: https://store.steampowered.com/news/app/1416920/view/5746109972551802070
- API locator: Steam ISteamNews/GetNewsForApp/v2, appid=1416920, gid=5746109972551802070。
- Claim use:
  - 项目 2018 年立项；
  - 策划、程序和“极其简单的美术”等主要工作由其一人利用业余时间完成；
  - 开发历时约五年。
- Confidence: HIGH
- Boundary:
  - 这是核心开发者自述，不是 contributor credits audit；
  - “均由我一个人”不能自动排除音乐、配音、商用素材、QA、发行等外围 contributors。

Direct quotes (verbatim, 原文重读 2026-10-09；经 Steam ISteamNews API 取回 gid=5746109972551802070):

开发者自述（第一人称）:
- “游戏在2018年就已经立项了。游戏全部的策划-程序-极其简单的美术等杂七杂八的工作，均由我一个人业余时间独立完成，历经5年时间，现在终于到了能和玩家见面的时候。”
- 对受众的称呼本身即产品语言：“Hi 各位‘氪佬’们大家好。”
- 自我定位：“游戏定位为小品级抽象、整活、搞笑、模拟类游戏，希望游戏可以给大家带来会心一笑的欢乐体验~”

Boundary additions:
- 用“氪佬”指称受众是自嘲式的市场语言，不是玩家构成数据。
- “均由我一个人”仍属核心开发者自述，不构成 contributor audit；音乐、配音、商用素材、QA 与发行仍可能有外部贡献。

## E002 — 原二手页面失效（待核）

- Source class: H — unverified research-intake lead。
- Former locator: https://www.gamersky.com/news/202407/1787810.shtml
- Accessed: 2026-10-05；HTTP 404，标题、作者和原文未核。
- Claim use: 不支持现有事实；单人、业余与约五年口径由 E001 官方原文独立承担。
- Confidence: UNKNOWN。
- Boundary: 不把失效页面称为“独立复述”，也不据此核定开发者姓名或职业履历。

## E003 — Steam 新品节参与（与 E001 为同一公告）

- Source class: P0 / official announcement。
- Title: 《中国式网游》Demo试玩即将上线！将参加6月新品节！
- Author / Institution: 项目官方 Steam 公告。
- Published: 2024-06-07。
- Accessed: 2026-10-05。
- URL: https://store.steampowered.com/news/app/1416920/view/5746109972551802070
- Claim use:
  - 官方公告明确宣布 Demo 参与 6.10–6.17 新品节；
  - 用于证明 market access 包含平台节庆与 Demo，而不是“零营销上传即爆”。
- Confidence: HIGH for participation announcement only。
- Boundary:
  - 同一公告拆分不同用途，不算两个独立来源；
  - 不证明热门排序、曝光或销量；
  - 尚未找到 Valve 后台 impression / wishlist 转化数据。

## E004 — Steam 商店身份：648工作室 / Wise Games

- Source class: P0 / platform listing
- Title: 中国式网游 — Steam store。
- Author / Institution: Valve / Steam；项目方提供商店信息。
- Published: UNKNOWN（动态页面）。
- Accessed: 2026-10-05。
- URL: https://store.steampowered.com/app/1416920/_/
- Claim use:
  - Developer: 648工作室；
  - Publisher: Wise Games；
  - 证明 solo core 与外部 publisher perimeter 并存。
- Confidence: HIGH
- Boundary:
  - 商店字段不能说明 publisher 合同、融资金额、分成或实际 labor contribution。

## E005 — 小黑盒 2024 金盒奖：刘永涛 / 《中国式网游》制作人

- Source class: P1 / public event listing。
- Title: 小黑盒金盒奖 2024。
- Author / Institution: 小黑盒 / Heybox。
- Published: UNKNOWN（2024 年度活动页）。
- Accessed: 2026-10-06。
- URL: https://web.xiaoheihe.cn/activity/heybox_gold_2024
- Claim use:
  - 公开标注“刘永涛 / 《中国式网游》制作人”；
  - 用于核定制作人实名。
- Confidence: HIGH for public identity label。
- Boundary:
  - 不证明其此前任职公司、岗位、年限或参与项目；
  - 不说明 648 工作室完整 production perimeter。

## E006 — Firsthand personal communication：此前任凉屋游戏程序岗位

- Source class: P0 / firsthand personal communication, non-public。
- Title: 刘永涛对其此前凉屋游戏程序岗位的直接确认。
- Author / Institution: 刘永涛 / research contributor。
- Published: UNKNOWN（non-public personal communication）。
- Accessed: 2026-10-06。
- Locator: PERSONAL COMMUNICATION — non-public; retained by research contributor。
- Source description: 研究贡献者报告曾直接向刘永涛本人询问；刘永涛本人确认此前曾任凉屋游戏程序岗位。
- Claim use:
  - 支持“刘永涛此前曾任凉屋游戏程序岗位”这一有限职业履历事实。
- Confidence: HIGH as direct subject testimony。
- Boundary:
  - 普通读者无法通过公开 URL 独立复核，引用时必须保留 personal communication provenance；
  - 不证明具体任职年份、参与项目、职级、是否承担制作人/策划职责、离职原因；
  - 若未来出现公开采访、credits 或履历，应追加公开 corroboration，而不是把本条改写成公开网页证据。

## E007 — Steam 官方公告档案：销量节点与更新节奏

- Source class: P0 — 官方公告档案（经 Steam ISteamNews API 逐条取回，非网页抓取）。
- Source: 《中国式网游》Steam 官方公告，appid=1416920。
- API: https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=1416920&count=300&maxlength=0
- Accessed: 2026-10-09。
- Returned: 74 条，可回溯至 2024-08-14。

Source-derived facts:
- 2024-11-28 公告标题载明“销量突破:40W+ 回馈——新史低、免费DLC、免费手游版本”。
- 2024-09-27 与 2024-12-20 两次以**免费 DLC** 形式推出大更新（“爽文模式”“彩票模式”）。
- 2024-08 至 2024-12 之间公告密度很高，含多条“《中国式网游》开发者日志”（坐骑、换装、帮派建设等）。
- 2025-07-23 一周年公告标题为“感谢所有氪佬”。

Boundary:
- 公告是营销材料；“40W+”为官方口径，未经审计，也不区分本体与 DLC。
- 公告密度不证明更新质量、留存或口碑。
- 该 API 可复现，比抓取 Steam 新闻网页稳定（网页为客户端渲染）。
- 本条记录的是**平台公告**，与 E001 的开发者第一人称自述不是同一类材料，不能互相替代。

## Unresolved evidence gap — prior industry career

截至 2026-10-06，制作人实名“刘永涛”已由 E005 公开资料核定；E006 以当事人直接个人通信确认其此前曾任凉屋游戏程序岗位。具体任职年份、参与项目、职级与职责边界仍缺少可公开复核的完整来源。

因此制作人身份不再是 UNKNOWN，但此前职业履历仍不能仅凭作品题材或私人线索写成公开已核事实。产品对中国网游的熟悉度可以支持“领域知识很深”，不能替代完整职业履历证据。
