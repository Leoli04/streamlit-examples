import json
import streamlit as st
from pathlib import Path
# 然后我们需要 Streamlit Elements 中的这些对象
# 有关全部对象及其用法的说明请见：https://github.com/okld/streamlit-elements#getting-started
from streamlit_elements import elements, dashboard, mui, editor, media, lazy, sync, nivo

st.set_page_config(layout="wide")

with st.sidebar:
    media_url = st.text_input("Media URL", value="https://www.youtube.com/watch?v=vIQQR_yq-8I")

with st.expander("about this app:"):
    st.write('''
    安装 `streamlit-elements`
    > pip install streamlit-elements==0.1.*
    
    用法参考：[Streamlit Elements README ](https://github.com/okld/streamlit-elements#getting-started)
    ''')





if "data" not in st.session_state:
    st.session_state.data = Path("./api-demo/data/data.json").read_text()

# 定义默认的仪表盘布局
# 默认情况下仪表盘会分为 12 列
#
# 更多可用参数见：
# https://github.com/react-grid-layout/react-grid-layout#grid-item-props

layout = [
    # 编辑器对象定位在坐标 x=0 且 y=0 处，占据 12 列中的 6 列以及 3 行
    dashboard.Item("editor", 0, 0, 6, 3),
    # 图表对象定位在坐标 x=6 且 y=0 处，占据 12 列中的 6 列以及 3 行
    dashboard.Item("chart", 6, 0, 6, 3),
    # 媒体播放器对象定位在坐标 x=0 且 y=3 处，占据 12 列中的 6 列以及 4 行
    dashboard.Item("media", 0, 3, 12, 4),
]

# 创建显示各元素的框体

with elements("demo"):

    # 使用以上指定的布局创建新仪表盘
    #
    # draggableHandle 是一个 CSS 查询选择器，定义了仪表盘中可拖拽的部分
    # 以下为将带 'draggable' 类名的元素变为可拖拽对象
    #
    # 更多仪表盘网格相关的可用参数请见：
    # https://github.com/react-grid-layout/react-grid-layout#grid-layout-props
    # https://github.com/react-grid-layout/react-grid-layout#responsive-grid-layout-props

    with dashboard.Grid(layout, draggableHandle=".draggable"):

        # 第一个卡片，代码编辑器
        #
        # 我们使用 'key' 参数来选择正确的仪表盘对象
        #
        # 为了让卡片的内容自动填充占满全部高度，我们将使用 flexbox CSS 样式
        # sx 是所有 Material UI 组件均可使用的参数，用于定义其 CSS 属性
        #
        # 有关卡片、flexbox 和 sx 的更多信息，请见：
        # https://mui.com/components/cards/
        # https://mui.com/system/flexbox/
        # https://mui.com/system/the-sx-prop/

        with mui.Card(key="editor", sx={"display": "flex", "flexDirection": "column"}):

            # 为了让标题可拖拽，我们只需要将其类名设为 'draggable'
            # 与 dashboard.Grid 当中 draggableHandle 的查询选择对应

            mui.CardHeader(title="编辑器", className="draggable")

            # 要使卡片内容占满全高，我们需要将 CSS 样式中 flex 的值设为 1
            # 同时我们也想要卡片内容随卡片缩放，因此将其 minHeight 设为 0

            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):

                # 以下是我们的 Monaco 代码编辑器
                #
                # 首先，我们将其默认值设为之前初始化好的 st.session_state.data
                # 其次，我们将设定所用的语言，这里我们设为 JSON
                #
                # 接下来，我们想要获取编辑器中内容的变动
                # 查阅 Monaco 文档后，我们发现可以用 onChange 属性指定一个函数
                # 这个函数会在每次变动发生后被调用，并且变更后的内容将被传入函数
                # (参考 onChange: https://github.com/suren-atoyan/monaco-react#props)
                #
                # Streamlit Elements 提供了一个特殊的 sync() 函数
                # 能够创建一个自动将其参数同步到 Streamlit 会话状态的回调函数
                #
                # 样例
                # --------
                # 创建一个自动将第一个参数同步至会话状态中 "data" 的回调函数：
                # >>> editor.Monaco(onChange=sync("data"))
                # >>> print(st.session_state.data)
                #
                # 创建一个自动将第二个参数同步至会话状态中 "ev" 的回调函数：
                # >>> editor.Monaco(onChange=sync(None, "ev"))
                # >>> print(st.session_state.ev)
                #
                # 创建一个自动将两个参数同步至会话状态的回调函数：
                # >>> editor.Monaco(onChange=sync("data", "ev"))
                # >>> print(st.session_state.data)
                # >>> print(st.session_state.ev)
                #
                # 那么问题来了：onChange 会在每次发生变动时被调用
                # 那么意味着每当你输入一个字符，整个 Streamlit 应用都会重新运行
                #
                # 为了避免这个问题，可以使用 lazy() 令 Streamlit Elements 等待其他事件发生
                # （比如点击按钮）然后再将更新后的数据传给回调函数
                #
                # 有关 Monaco 其他可用参数的说明，请见：
                # https://github.com/suren-atoyan/monaco-react
                # https://microsoft.github.io/monaco-editor/api/interfaces/monaco.editor.IStandaloneEditorConstructionOptions.html

                editor.Monaco(
                    defaultValue=st.session_state.data,
                    language="json",
                    onChange=lazy(sync("data"))
                )

            with mui.CardActions:

                # Monaco 编辑器已经将一个延迟回调函数绑定至 onChange 了，因此即便你更改了 Monaco 的内容
                # Streamlit 也不会立刻接收到，因此不会每次都重新运行
                # 因此我们需要另一个非延迟的事件来触发更新
                #
                # 解决方法就是创建一个在点击时回调的按钮
                # 我们的回调函数实际上不需要做任何事
                # 你可以创建一个空的函数，或者直接使用不带参数的 sync()
                #
                # 然后每当你点击按钮的时候，onClick 回调函数会被调用
                # 而期间其他延迟调用了的回调函数也会被一并执行

                mui.Button("Apply changes", onClick=sync())

        # 第二个卡片，Nivo Bump 图
        # 我们将使用和第一个卡片同样的 flexbox 配置来自动调整内容高度

        with mui.Card(key="chart", sx={"display": "flex", "flexDirection": "column"}):

            # 为了让标题可拖拽，我们只需要将其类名设为 'draggable'
            # 与 dashboard.Grid 当中 draggableHandle 的查询选择对应

            mui.CardHeader(title="Chart", className="draggable")

            # 和前面一样，我们想要让我们的内容随着用户缩放卡片而缩放
            # 因此将 flex 属性设为 1，minHeight 设为 0

            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):

                # 以下我们将绘制 Bump 图
                #
                # 在这个练习里，我们就借用一下 Nivo 的示例，将其用在 Streamlit Elements 里面
                # Nivo 的示例可以在这里此页面的 'code' 标签页中找到：https://nivo.rocks/bump/
                #
                # data 参数接收一个字典，因此我们需要用 `json.loads()` 将 JSON 数据从字符串转化为字典对象
                #
                # 有关更多其他类型的 Nivo 图表，请见：
                # https://nivo.rocks/

                nivo.Bump(
                    data=json.loads(st.session_state.data),
                    colors={ "scheme": "spectral" },
                    lineWidth=3,
                    activeLineWidth=6,
                    inactiveLineWidth=3,
                    inactiveOpacity=0.15,
                    pointSize=10,
                    activePointSize=16,
                    inactivePointSize=0,
                    pointColor={ "theme": "background" },
                    pointBorderWidth=3,
                    activePointBorderWidth=3,
                    pointBorderColor={ "from": "serie.color" },
                    axisTop={
                        "tickSize": 5,
                        "tickPadding": 5,
                        "tickRotation": 0,
                        "legend": "",
                        "legendPosition": "middle",
                        "legendOffset": -36
                    },
                    axisBottom={
                        "tickSize": 5,
                        "tickPadding": 5,
                        "tickRotation": 0,
                        "legend": "",
                        "legendPosition": "middle",
                        "legendOffset": 32
                    },
                    axisLeft={
                        "tickSize": 5,
                        "tickPadding": 5,
                        "tickRotation": 0,
                        "legend": "ranking",
                        "legendPosition": "middle",
                        "legendOffset": -40
                    },
                    margin={ "top": 40, "right": 100, "bottom": 40, "left": 60 },
                    axisRight=None,
                )

        # 仪表盘的第三个元素是媒体播放器


        with mui.Card(key="media", sx={"display": "flex", "flexDirection": "column"}):
            mui.CardHeader(title="Media Player", className="draggable")
            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):

                # 这个元素实现基于 ReactPlayer，它支持很多除了 YouTube 以外的媒体
                # 你能在这里查看完整列表：https://github.com/cookpete/react-player#props

                media.Player(url=media_url, width="100%", height="100%", controls=True)