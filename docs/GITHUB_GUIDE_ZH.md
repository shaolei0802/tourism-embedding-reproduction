# GitHub 最新上传与发布流程

## 一 这次上传什么

本版可公开资料包保留两个案例：北京约 4.09 km²、海花岛约 48.36 km²；均比较 2021 与 2025 年，使用 64 维嵌入和 10 米网格。北京热力图为 60% 不透明度，海花岛为 100%。

正文的准确题名为：Democratizing Tourism Land Use Monitoring: An Exploratory Proof of Concept Using Precomputed Earth Embeddings。不要再使用 5.2 km²、37 km²，或将 TPPI 描述为已经构建的指标。

资料包已移除论文 manuscript 文件夹，并同步更新 README 和校验清单。你无需再次手动删除 Word 或修改清单。docs 中的 Word 是本操作指南，不是论文稿。解压后上传内部内容，让 README.md 位于仓库根目录，不要只上传 ZIP。

## 二 建立仓库并上传

1. Owner：选择你的账号。
2. Repository name：tourism-embedding-reproduction。
3. Description：Reproduction materials for exploratory tourism destination surface-change screening using OlmoEarth v1.3 annual embeddings in Beijing and Hainan.
4. Visibility：可先 Private 整理；用于论文公开访问前设为 Public。
5. Add README：关闭，本包已有新版 README。
6. Add .gitignore：None，本包已有 .gitignore。
7. Add license：暂选 None。不要给平台代码、数据和底图统一套用 MIT。
8. 点击 Create repository，随后 uploading an existing file 或 Add file → Upload files。
9. 上传解压目录内部的全部内容，填写 Add reproduction materials 并提交。
10. 用未登录窗口确认 README、两个 notebook、AOI、TIFF 和图片可访问。

新版 README 已提供双案例示例、快速运行步骤、复现状态、数据源和引用入口。RIGHTS_AND_LICENSING.md 说明许可范围；它不是授予 MIT 权限的 LICENSE。作者后续可对有权授权的原创部分单独选择许可。

不要把 JPEG 或 TIFF 直接改扩展名为 PNG；文件格式和清晰度不会因此改变。原始 notebook 和截图在本包中均保留原字节，只采用英文文件名整理。

## 三 完整复运行与发布版本

在仓库根目录用 Python 3.10 或以上建立环境：

```bash
python -m venv .venv
```

Windows PowerShell：

```powershell
.\.venv\Scripts\Activate.ps1
```

macOS 或 Linux：

```bash
source .venv/bin/activate
```

安装并运行：

```bash
python -m pip install -r requirements.txt
python scripts/verify_package.py
python tests/test_score_logic.py
python scripts/reproduce.py --case beijing
python scripts/reproduce.py --case hainan
```

截至本次打包，离线校验和合成数据小测试已通过，但两案例联网完整复运行尚未执行。原始 notebook 没有保存运行输出。不要仅凭检查通过，就把 README 改成“已成功独立复现”。

现有 TIFF 是 RGBA 颜色可视化图；运行脚本后得到的一波段 float32 TIFF 才是该次新计算的余弦距离。新结果写入 outputs 时间戳目录，并记录软件版本、AOI、年份、有效像元比例和分数摘要。新图不会覆盖原始浏览器截图，300 dpi 也不会提升原始 10 米数据的空间分辨率。

上游数据页面截至 2026 年 10 月 27 日已声明完成 2021—2025 年全球覆盖。这个产品级说明不等于两个 AOI 每个像元均有效；有效比例仍需实际计算。本包不包含源嵌入的冻结快照，后续复运行须记录日期与环境。

上传完成后，进入 Releases → Draft a new release，创建标签 v0.1.0；若该标签已经发布，应使用新的标签保留历史。Release notes 只写真实完成的工作。尚未联网复运行时可填写：

> This release contains original platform exports, AOI boundaries, screenshots, georeferenced RGBA visualizations, and supporting reproduction scripts. Offline checks passed. A full live-archive rerun has not been completed, and no independent accuracy validation is provided.

若实际运行完成，可将结果 ZIP 作为 Release 附件，并记录具体案例、日期和环境。脚本成功不等于精度验证通过。

## 四 让别人方便引用

CITATION.cff 已写入作者和最新论文题名，并设置 preferred-citation。它不声称论文已在 SSRN 发布，也没有虚构 DOI。论文公开后，补充核实过的论文 URL 或 DOI，并在 README 加入论文链接。

MIT 并不要求别人引用你的学术论文，它要求保留版权与许可声明。学术引用请求放在 README/CITATION.cff 中。对平台生成代码、模型数据和底图，应保留各自适用条款和来源，而不是全仓库直接使用 MIT。

为固定引用，可在仓库公开后连接 Zenodo，启用仓库归档，再创建 Release。取得真实 DOI 后才写回论文；GitHub Release 自身不自动给 DOI。引用增长无法保证，完整资料、稳定版本和易用引用信息有助于读者使用你的研究。

## 五 仓库公开后更新论文

正文与完整附录 A 保留在同一个投稿 PDF 中。GitHub 放代码、AOI、证据资料和运行说明；不必公开可编辑论文 Word。

只有公开地址已经能访问时，才将论文当前“尚无公开仓库”的声明改为以下模板，并替换 REPOSITORY_URL、VERSION 和 COMMIT_SHA：

> Reproduction materials, including the original platform-exported notebooks, AOI boundaries, browser screenshots, georeferenced RGBA visualizations, and supporting documentation, are publicly available at REPOSITORY_URL (release VERSION, commit COMMIT_SHA). The original notebooks contain no saved execution outputs. The included TIFFs are visualization layers rather than raw single-band distance rasters. Source embeddings are accessed through the upstream OlmoEarth archive.

只有真正完成并公开两案例复运行后，才追加：

> Executed rerun outputs, valid-data summaries, and the resolved software environment are archived with the release.

若仅完成一个案例，要明确该案例。无论是否复运行，不能删除“未进行独立精度验证”的事实。

论文中的覆盖年份也需更新：初始发布时全球覆盖为 2023—2025 年；数据页面于 2026 年 10 月 27 日已声明完成 2021—2025 年全球覆盖。可写为：

> The dataset page reports completed global coverage for 2021–2025 as of 27 October 2026. This product-level statement does not establish complete valid-pixel coverage within either study AOI, which was not quantified in the present analysis.

## 官方参考

- 数据与覆盖：https://source.coop/olmoearth/olmoearth-v1-3-embeddings
- 创建仓库：https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository
- 上传文件：https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository
- 发布版本：https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository
- 引用文件：https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files
- Zenodo 与 DOI：https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content
- MIT 条款：https://choosealicense.com/licenses/mit/

核对日期：2026 年 10 月 27 日。当前版本为准备上传的资料包，未代表你创建远程仓库、发布 Release 或申请 DOI。
