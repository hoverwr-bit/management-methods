#!/usr/bin/env python3
"""把 README.md 嵌入 HTML 模板，生成双击即可浏览的图解页面。

用法：python3 build.py
修改 README.md 后重新运行本脚本即可更新 index.html。
"""
import json
from pathlib import Path

HERE = Path(__file__).parent
md = (HERE / "README.md").read_text(encoding="utf-8")

TEMPLATE = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>管理方法论图解</title>
<style>
  body { max-width: 900px; margin: 0 auto; padding: 24px;
         font-family: -apple-system, "PingFang SC", "Helvetica Neue", sans-serif;
         line-height: 1.7; color: #24292f; }
  h1 { border-bottom: 2px solid #d0d7de; padding-bottom: .3em; }
  h2 { border-bottom: 1px solid #d0d7de; padding-bottom: .2em; margin-top: 1.8em; }
  h3 { margin-top: 1.5em; }
  table { border-collapse: collapse; margin: 1em 0; }
  th, td { border: 1px solid #d0d7de; padding: 6px 12px; }
  th { background: #f6f8fa; }
  pre { background: #f6f8fa; padding: 12px; border-radius: 6px; overflow-x: auto; }
  blockquote { margin: 0; padding: 0 1em; color: #57606a; border-left: 3px solid #d0d7de; }
  code { background: #f6f8fa; padding: 2px 5px; border-radius: 4px; }
  .mermaid { text-align: center; background: #fff; margin: 1em 0; }
</style>
</head>
<body>
<main id="content">正在加载图解，请稍候……（需要联网加载渲染引擎）</main>
<script src="https://cdn.jsdelivr.net/npm/marked@12/marked.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js"></script>
<script>
const md = __MD_DATA__;
document.getElementById("content").innerHTML = marked.parse(md);
mermaid.initialize({ startOnLoad: false, theme: "default", flowchart: { htmlLabels: true } });
mermaid.run({ querySelector: ".language-mermaid" });
</script>
</body>
</html>
"""

(HERE / "index.html").write_text(TEMPLATE.replace("__MD_DATA__", json.dumps(md, ensure_ascii=False)), encoding="utf-8")
print(f"OK: {HERE / 'index.html'} ({(HERE / 'index.html').stat().st_size} bytes)")
