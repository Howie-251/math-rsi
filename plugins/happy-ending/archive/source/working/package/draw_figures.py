"""Write deterministic vector illustrations for the reading report."""

from html import escape
from pathlib import Path
import json


OUTPUT = Path(__file__).resolve().parent / 'figures'
INK = '#172535'
BLUE = '#26528f'
RED = '#ac3640'
TEAL = '#1d6367'
GRID = '#aab9c1'
FILL = '#d6e6f1'
AMBER = '#a16723'


def text(x, y, label, *, size=19, color=INK, anchor='middle', bold=False):
    weight = ' font-weight="700"' if bold else ''
    return f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}" text-anchor="{anchor}"{weight}>{escape(label)}</text>'


def line(x1, y1, x2, y2, color=GRID, width=2, *, dash=False, arrow=False):
    decoration = (' stroke-dasharray="8 6"' if dash else '') + (' marker-end="url(#n7-arrow)"' if arrow else '')
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}" stroke-linecap="round"{decoration}/>'


def rect(x, y, width, height, fill, stroke=GRID, radius=0):
    return f'<rect x="{x}" y="{y}" width="{width}" height="{height}" fill="{fill}" stroke="{stroke}" rx="{radius}"/>'


def dot(x, y, color, radius=5):
    return f'<circle cx="{x}" cy="{y}" r="{radius}" fill="{color}"/>'


def frame(title, width, height, elements):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-label="{escape(title, quote=True)}">'
            f'<title>{escape(title)}</title>' + ''.join(elements) + '</svg>\n')


def paths():
    elements = [line(380, 20, 380, 250, '#dce3e5', 1)]
    blue = [(0, 0), (1.2, 1.9), (3, 2.2), (5, 0)]
    reds = [[(0, 0), (1, -1.5), (2.4, -2.1), (4, -1.5), (5, 0)],
            [(-.5, -.3), (.8, -1.6), (2.2, -2.2), (3.8, -1.5), (5, 0)]]
    for offset, red, heading, shared_start in zip((69, 449), reds, ('共同左右端点 · weak 7-gon', '只共右端点 · split 7-gon'), (True, False)):
        elements.append(text(offset + 109, 29, heading, bold=True))
        for points, color, dashed in ((blue, BLUE, False), (red, RED, True)):
            mapped = [(round(offset + 43 * x, 2), round(144 - 41 * y, 2)) for x, y in points]
            elements.extend(line(*start, *end, color, 3, dash=dashed) for start, end in zip(mapped, mapped[1:]))
            elements.extend(dot(*point, color, 4.7) for point in mapped)
        elements.append(dot(offset + 215, 144, INK, 5.2))
        elements.append(text(offset + 231, 150, 't', anchor='start', size=17))
        if shared_start:
            elements.extend((dot(offset, 144, INK, 5.2), text(offset - 15, 149, 's', anchor='end', size=17)))
        else:
            elements.extend((text(offset - 10, 126, 'sᴮ', anchor='end', size=17), text(offset - 29, 174, 'sᴿ', anchor='end', size=17)))
        elements.extend((text(offset + 110, 105, '蓝 4 帽', color=BLUE), text(offset + 111, 192, '红 5 杯', color=RED)))
    return frame('共左右端点与只共右端点的路径示意', 760, 258, elements)


def states():
    elements = ['<text x="130" y="30" fill="#ac3640" font-size="19">纵轴　L<tspan baseline-shift="sub" font-size="12">R</tspan> − 1</text>',
                '<text x="204" y="298" fill="#26528f" font-size="19" text-anchor="middle">横轴　L<tspan baseline-shift="sub" font-size="12">B</tspan> − 1</text>']
    heights = (3, 2, 0)
    for column in range(1, 4):
        for row in range(1, 5):
            x = 130 + 49 * (column - 1)
            y = 47 + 49 * (4 - row)
            elements.append(rect(x, y, 49, 49, FILL if row <= heights[column - 1] else '#fff'))
    for column, row in ((1, 3), (2, 2)):
        x = 130 + 49 * (column - 1)
        y = 47 + 49 * (4 - row)
        elements.append(dot(x + 24.5, y + 24.5, BLUE, 6))
        elements.append(text(x + 33, y + 15, f'({column},{row})', anchor='start', size=15))
    elements.extend(text(130 + 49 * (col - .5), 267, str(col), size=17, color=BLUE) for col in range(1, 4))
    elements.extend(text(111, 78 + 49 * (4 - row), str(row), size=17, color=RED) for row in range(1, 5))
    elements.extend((text(378, 88, '列高  (3,2,0)', bold=True, anchor='start', size=24),
                     text(378, 128, '宽 2，高 3', anchor='start'), text(378, 171, '深色圆点是生成点', anchor='start'),
                     text(378, 204, '浅蓝 5 格是它们的向下闭包', anchor='start')))
    return frame('3 × 4 状态框内由两个实际末对生成的普通下集', 720, 319, elements)


def exceptional():
    heights = [(4, middle, last) for middle in range(1, 5) for last in range(1, middle + 1)]
    elements = [text(380, 29, '同一个 3 × 4 外框，宽 3 且高 4', bold=True)]
    for index, columns in enumerate(heights):
        origin_x = 42 + 145 * (index % 5)
        origin_y = 49 + 142 * (index // 5)
        for column, height in enumerate(columns):
            for row in range(1, 5):
                x = origin_x + 25 * column
                y = origin_y + 25 * (4 - row)
                highlight = index == 0 and (column, row) in ((0, 4), (2, 1))
                fill = '#7295b5' if highlight else FILL if row <= height else '#fff'
                elements.append(rect(x, y, 25, 25, fill))
        elements.append(text(origin_x + 37.5, origin_y + 126, str(columns).replace(' ', ''), size=18))
    return frame('10 种异常下集状态及各自的列高', 760, 330, elements)


def bounds():
    elements = ['<defs><marker id="n7-arrow" markerWidth="7" markerHeight="7" refX="6" refY="3" orient="auto"><path d="M0 0 L6 3 L0 6" fill="none" stroke="#71848c" stroke-width="1.2"/></marker></defs>']
    elements.extend((rect(45, 12, 168, 50, '#eaf3f1', '#bdd6d3', 7), text(129, 44, 'a = 16', bold=True),
                     rect(306, 12, 168, 50, '#eaf3f1', '#bdd6d3', 7), text(390, 44, 'b = 25', bold=True),
                     line(129, 63, 128, 112, '#71848c', arrow=True)))
    for x, title, formula in ((18, 'N(7,5,7) ≤ 40', 'a + b − 1'), (280, 'N(7,6,6) ≤ 50', '2b'), (542, 'N(7,6,7) ≤ 76', '3b + 1')):
        elements.append(line(390, 63, x + 110, 112, '#71848c', arrow=True))
        elements.extend((rect(x, 116, 220, 69, '#faf1df', '#e7ceaa', 7), text(x + 110, 146, title, bold=True, size=22), text(x + 110, 171, formula, size=17, color=AMBER)))
    elements.extend((line(652, 186, 652, 222, '#71848c', arrow=True), text(631, 212, '精确一点归约：+1', anchor='end', size=17), rect(542, 227, 220, 54, '#faf1df', '#e7ceaa', 7), text(652, 261, 'N(7,7,7) ≤ 77', bold=True, size=22), line(652, 282, 652, 324, '#71848c', arrow=True), text(631, 309, '几何阈值换算', anchor='end', size=17), rect(542, 329, 220, 52, '#faf1df', '#e7ceaa', 7), text(652, 362, 'ES(7) ≤ 78', bold=True, size=22)))
    return frame('从容量输入到四个组合工作上界和几何阈值', 780, 394, elements)


def matching():
    xs = (82, 281, 499, 697)
    ys = (90, 151, 212)
    elements = [rect(24, 128, 733, 46, '#eaf3f1', 'none', 5)]
    for x, title in zip(xs, ('左外匹配', '中间首点', '中间末点', '右外匹配')):
        elements.append(text(x, 37, title, bold=True, size=17))
    for index, y in enumerate(ys):
        elements.append(line(xs[1], y, xs[2], y, RED, 3 if index == 1 else 2))
        elements.extend((dot(xs[1], y, RED), dot(xs[2], y, RED)))
        if index < 2:
            elements.extend((line(xs[0], y, xs[1], y, TEAL, 3 if index == 1 else 2), dot(xs[0], y, TEAL)))
        if index > 0:
            elements.extend((line(xs[2], y, xs[3], y, TEAL, 3 if index == 1 else 2), dot(xs[3], y, TEAL)))
    elements.extend((text(390, 144, '共同覆盖', size=15, color=TEAL), text(390, 254, '同一份中间红五匹配上的外覆盖', size=17),
                     line(38, 273, 742, 273, '#dce3e5', 1), text(390, 304, '交会给出同端蓝四与红五', bold=True, size=19)))
    j, r, s, k = 172, 317, 463, 608
    level = 430
    red_path = [(j, level), (268, 375), (390, 350), (512, 375), (k, level)]
    for start, end in zip(red_path, red_path[1:]):
        elements.append(line(*start, *end, RED, 2.4, dash=True))
    elements.extend(dot(x, y, RED, 4) for x, y in red_path[1:-1])
    for left, right in zip((j, r, s), (r, s, k)):
        elements.append(line(left, level, right, level, BLUE, 3.3))
    for x, label in zip((j, r, s, k), ('j', 'r', 's', 'k')):
        elements.extend((dot(x, level, INK, 5.4), text(x, 458, label, size=20)))
    elements.extend((text(390, 384, '实际红 5', color=RED, size=17), text(390, 420, '蓝 4', color=BLUE, size=16),
                     '<path d="M172 467 V479 H317 V467 M463 467 V479 H608 V467" fill="none" stroke="#ac3640" stroke-width="1.7"/>',
                     text(244, 510, '某红 6 的末对', color=RED, size=16), text(535, 510, '某红 6 的首对', color=RED, size=16),
                     text(390, 547, 'j < r < s < k', size=18)))
    return frame('三匹配交会与同端路径关系示意', 780, 563, elements)


def main():
    OUTPUT.mkdir(exist_ok=True)
    for name, draw in {'paths': paths, 'states': states, 'exceptional': exceptional, 'bounds': bounds, 'matching': matching}.items():
        (OUTPUT / f'{name}.svg').write_text(draw(), encoding='utf-8')
    captions = {
        'paths': '图 1　蓝实线表示四顶点帽，红虚线表示五顶点杯。左图的两条路径共用左右端点，形成七顶点凸形。右图画出的两条路径只共右端点，共有八点，其中仍可能存在由其他路径组成的凸七边形。',
        'states': '图 2　下集的列高为 (3,2,0)，宽 2、高 3。格心表示整数点。深色生成点 (1,3)、(2,2) 的向下闭包共有 5 格。',
        'exceptional': '图 3　全部 10 种异常状态。第一种的深色格表示分别达到高 4 和宽 3 的格点。',
        'bounds': '图 4　容量输入到工作上界的依赖关系。76、77 是最大允许点数的上界，78 是几何强迫阈值的工作上界。',
        'matching': '图 5　绿色底纹标出同时得到左右供应的中间边。下图从交会读出共同端点 j、k。这是路径关系图，不是平面坐标实现。',
    }
    (OUTPUT / 'captions.json').write_text(json.dumps(captions, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
