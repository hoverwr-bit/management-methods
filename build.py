#!/usr/bin/env python3
"""把三份 README 嵌入 HTML 模板，生成可直接双击浏览的三语图解站点。

结构：
  index.html       中文（源：README.md）
  en/index.html    English（源：README.en.md）
  vi/index.html    Tiếng Việt（源：README.vi.md）

用法：python3 build.py
修改任何 README 后重新运行本脚本即可更新全部页面。
"""
import json
from pathlib import Path

HERE = Path(__file__).parent

LANGS = [
    # (代码, 显示名, markdown 源, 输出路径, 同级语言链接 {代码: href})
    ("zh", "中文", "README.md", "index.html",
     {"en": "en/", "vi": "vi/"}),
    ("en", "English", "README.en.md", "en/index.html",
     {"zh": "../", "vi": "../vi/"}),
    ("vi", "Tiếng Việt", "README.vi.md", "vi/index.html",
     {"zh": "../", "en": "../en/"}),
]

TEMPLATE = """<!DOCTYPE html>
<html lang="{lang_attr}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>
  body {{ max-width: 900px; margin: 0 auto; padding: 24px;
         font-family: -apple-system, "PingFang SC", "Helvetica Neue", sans-serif;
         line-height: 1.7; color: #24292f; }}
  .langnav {{ text-align: right; font-size: 14px; padding: 4px 0 12px;
              border-bottom: 1px solid #d0d7de; margin-bottom: 16px; }}
  .langnav b {{ font-weight: 600; }}
  .langnav a {{ color: #0969da; text-decoration: none; margin: 0 4px; }}
  h1 {{ border-bottom: 2px solid #d0d7de; padding-bottom: .3em; }}
  h2 {{ border-bottom: 1px solid #d0d7de; padding-bottom: .2em; margin-top: 1.8em; }}
  h3 {{ margin-top: 1.5em; }}
  table {{ border-collapse: collapse; margin: 1em 0; }}
  th, td {{ border: 1px solid #d0d7de; padding: 6px 12px; }}
  th {{ background: #f6f8fa; }}
  pre {{ background: #f6f8fa; padding: 12px; border-radius: 6px; overflow-x: auto; }}
  blockquote {{ margin: 0; padding: 0 1em; color: #57606a; border-left: 3px solid #d0d7de; }}
  code {{ background: #f6f8fa; padding: 2px 5px; border-radius: 4px; }}
  .mermaid {{ text-align: center; background: #fff; margin: 1em 0; }}
</style>
</head>
<body>
<nav class="langnav">{nav}</nav>
<main id="content">{loading}</main>
<script src="https://cdn.jsdelivr.net/npm/marked@12/marked.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js"></script>
<script>
const md = __MD_DATA__;
document.getElementById("content").innerHTML = marked.parse(md);
mermaid.initialize({{ startOnLoad: false, theme: "default", flowchart: {{ htmlLabels: true }} }});
mermaid.run({{ querySelector: ".language-mermaid" }});
</script>
</body>
</html>
"""

LANG_ATTR = {"zh": "zh-CN", "en": "en", "vi": "vi"}
LOADING = {"zh": "正在加载图解，请稍候……（需要联网加载渲染引擎）",
           "en": "Loading diagrams… (internet required for the rendering engine)",
           "vi": "Đang tải sơ đồ… (cần internet để tải công cụ render)"}
TITLES = {"zh": "管理方法论图解", "en": "Management Methodology Diagrams",
          "vi": "Sơ đồ các phương pháp quản trị"}


def build_nav(current: str, links: dict) -> str:
    parts = []
    for code, name, *_ in LANGS:
        if code == current:
            parts.append(f"<b>{name}</b>")
        else:
            parts.append(f'<a href="{links[code]}">{name}</a>')
    return " · ".join(parts)


for code, name, src, out, links in LANGS:
    md = (HERE / src).read_text(encoding="utf-8")
    html = (TEMPLATE
            .replace("{lang_attr}", LANG_ATTR[code])
            .replace("{title}", TITLES[code])
            .replace("{nav}", build_nav(code, links))
            .replace("{loading}", LOADING[code])
            .replace("__MD_DATA__", json.dumps(md, ensure_ascii=False)))
    target = HERE / out
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(html, encoding="utf-8")
    print(f"OK: {target} ({target.stat().st_size} bytes)")
