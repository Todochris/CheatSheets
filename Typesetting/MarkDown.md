
[comment]: <> (pandoc -o 'Markdown_pandoc_render.pdf' MarkDown_pandoc_header.yaml 'Markdown.md')

# Markdown Cheatsheet

---

## Headings

# H1 — Main title
## H2 — Section
### H3 — Subsection
#### H4 — Sub-subsection

---

## Text Formatting

**bold** &nbsp;&nbsp; *italic* &nbsp;&nbsp; ~~strikethrough~~ &nbsp;&nbsp; `inline code`

---

## Lists

Unordered:

- Item A
- Item B
  - Nested item

Ordered:

1. First
2. Second
3. Third

---

## Links and Images

[Example link](https://example.com)

![Example image](img/picture.png){width=50%}

---

## Code Block

```python
print("Hello world")
```

---

## Table

| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| A        | B        | C        |
| D        | E        | F        |

---

## Blockquote

> This is a quote.
> It can span multiple lines.

---

## Footnote

This sentence has a footnote.[^1]

[^1]: This is the footnote content.

---

## Math

Inline: $E = mc^2$

Block:

$$
\int_0^\infty e^{-x} dx = 1
$$

---

## Escaping Special Characters

\*  \#  \_  \`  \[  \]

---

## Comment (invisible in output)

[comment]: <> (This comment does not appear in the rendered PDF or on GitHub)

---

## Pandoc Compile Command

[comment]: <> (pandoc -o 'markdown_cheatsheet.pdf' 'markdown_cheatsheet.md')
