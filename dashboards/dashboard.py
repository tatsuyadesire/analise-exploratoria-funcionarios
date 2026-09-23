import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit.components.v1 as components
from pathlib import Path


st.set_page_config(
    page_title="Análise de Funcionários",
    layout="wide",
    initial_sidebar_state="expanded",
)


st.markdown(
    """
    <style>

    html, body, [data-testid="stAppViewContainer"], .stApp {
        background: #070c16 !important;
        color: #f4f7fb !important;
    }

    [data-testid="stHeader"] {
        display: none !important;
    }

    [data-testid="stToolbar"] {
        display: none !important;
    }

    [data-testid="stDecoration"] {
        display: none !important;
    }

    [data-testid="stStatusWidget"] {
        display: none !important;
    }

    [data-testid="stAppDeployButton"] {
        display: none !important;
    }

    #MainMenu {
        display: none !important;
    }

    footer {
        display: none !important;
    }

    .block-container {
        max-width: 100% !important;
        padding: 16px 10px 8px 10px !important;
        margin: 0 !important;
    }

    [data-testid="stSidebar"] {
        background: #0b111d !important;
        border-right: 1px solid #26364d !important;
    }

    [data-testid="stSidebar"] > div:first-child {
        padding-top: 18px !important;
    }

    [data-testid="stSidebar"] * {
        color: #e8edf5;
    }

    [data-testid="stSidebar"] label {
        color: #aebbd0 !important;
        font-size: 12px !important;
    }

    [data-testid="stSidebar"] .stMultiSelect {
        margin-bottom: 4px !important;
    }

    [data-testid="stSidebar"] [data-baseweb="select"] {
        background: #0e1624 !important;
        border-color: #273852 !important;
    }

    [data-testid="stSidebar"] .stSlider {
        margin-top: -3px !important;
        margin-bottom: 4px !important;
    }

    .dashboard-title {
        font-family: Arial, Helvetica, sans-serif;
        font-size: clamp(26px, 2.4vw, 38px);
        font-weight: 800;
        letter-spacing: -0.8px;
        color: #f7f9fc;
        line-height: 1;
        margin: 2px 0 4px 0;
    }

    .dashboard-subtitle {
        font-family: Arial, Helvetica, sans-serif;
        color: #8ea0b8;
        font-size: 12px;
        margin-bottom: 12px;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


BASE_DIR = Path(__file__).resolve().parent.parent
CSV_PATH = BASE_DIR / "data" / "funcionarios.csv"


@st.cache_data
def carregar_dados():

    if not CSV_PATH.exists():
        st.error(
            f"Arquivo não encontrado:\n\n{CSV_PATH}\n\n"
            "Verifique se o arquivo está em data/funcionarios.csv"
        )
        st.stop()

    try:
        df = pd.read_csv(
            CSV_PATH,
            sep=None,
            engine="python",
            encoding="utf-8-sig"
        )
    except UnicodeDecodeError:
        df = pd.read_csv(
            CSV_PATH,
            sep=None,
            engine="python",
            encoding="latin1"
        )

    colunas_numericas = [
        "Idade",
        "Experiência (anos)",
        "Horas Trabalhadas",
        "Salário",
        "Satisfação",
        "Desempenho",
    ]

    for coluna in colunas_numericas:
        if coluna in df.columns:
            if df[coluna].dtype == object:
                df[coluna] = (
                    df[coluna]
                    .astype(str)
                    .str.replace(".", "", regex=False)
                    .str.replace(",", ".", regex=False)
                )

            df[coluna] = pd.to_numeric(
                df[coluna],
                errors="coerce"
            )

    return df


df = carregar_dados()


st.sidebar.markdown(
    """
    <div style="
        font-family:Arial,Helvetica,sans-serif;
        font-size:20px;
        font-weight:800;
        color:#00d9ff;
        margin-bottom:2px;
    ">
        FILTROS
    </div>
    """,
    unsafe_allow_html=True,
)


departamentos = sorted(
    df["Departamento"].dropna().unique().tolist()
)

cargos = sorted(
    df["Cargo"].dropna().unique().tolist()
)


f_departamento = st.sidebar.multiselect(
    "DEPARTAMENTO",
    departamentos,
    default=departamentos,
)


f_cargo = st.sidebar.multiselect(
    "CARGO",
    cargos,
    default=cargos,
)


idade_min = int(df["Idade"].min())
idade_max = int(df["Idade"].max())

f_idade = st.sidebar.slider(
    "FAIXA ETÁRIA",
    min_value=idade_min,
    max_value=idade_max,
    value=(idade_min, idade_max),
)


sal_min = int(df["Salário"].min())
sal_max = int(df["Salário"].max())

f_salario = st.sidebar.slider(
    "FAIXA SALARIAL",
    min_value=sal_min,
    max_value=sal_max,
    value=(sal_min, sal_max),
    step=500,
)


exp_min = float(df["Experiência (anos)"].min())
exp_max = float(df["Experiência (anos)"].max())

f_experiencia = st.sidebar.slider(
    "EXPERIÊNCIA",
    min_value=exp_min,
    max_value=exp_max,
    value=(exp_min, exp_max),
    step=0.5,
)


sat_min = float(df["Satisfação"].min())
sat_max = float(df["Satisfação"].max())

f_satisfacao = st.sidebar.slider(
    "SATISFAÇÃO",
    min_value=sat_min,
    max_value=sat_max,
    value=(sat_min, sat_max),
    step=0.1,
)


horas_min = int(df["Horas Trabalhadas"].min())
horas_max = int(df["Horas Trabalhadas"].max())

f_horas = st.sidebar.slider(
    "HORAS TRABALHADAS",
    min_value=horas_min,
    max_value=horas_max,
    value=(horas_min, horas_max),
)


df_filtrado = df[
    df["Departamento"].isin(f_departamento)
    & df["Cargo"].isin(f_cargo)
    & df["Idade"].between(
        f_idade[0],
        f_idade[1]
    )
    & df["Salário"].between(
        f_salario[0],
        f_salario[1]
    )
    & df["Experiência (anos)"].between(
        f_experiencia[0],
        f_experiencia[1]
    )
    & df["Satisfação"].between(
        f_satisfacao[0],
        f_satisfacao[1]
    )
    & df["Horas Trabalhadas"].between(
        f_horas[0],
        f_horas[1]
    )
].copy()


if df_filtrado.empty:

    st.warning(
        "Nenhum funcionário corresponde aos filtros selecionados."
    )

    st.stop()


st.markdown(
    """
    <div class="dashboard-title">
        ANÁLISE DE FUNCIONÁRIOS
    </div>

    <div class="dashboard-subtitle">
        Indicadores de desempenho, remuneração, satisfação e jornada de trabalho
    </div>
    """,
    unsafe_allow_html=True,
)


total = len(df_filtrado)

media_salario = df_filtrado["Salário"].mean()

media_satisfacao = df_filtrado["Satisfação"].mean()

media_horas = df_filtrado["Horas Trabalhadas"].mean()

media_desempenho = df_filtrado["Desempenho"].mean()


def moeda(valor):
    return (
        f"R$ {valor:,.0f}"
        .replace(",", ".")
    )


kpis = [
    ("FUNCIONÁRIOS", f"{total}"),
    ("SALÁRIO MÉDIO", moeda(media_salario)),
    ("SATISFAÇÃO MÉDIA", f"{media_satisfacao:.1f}"),
    ("HORAS MÉDIAS", f"{media_horas:.1f} h"),
    ("DESEMPENHO MÉDIO", f"{media_desempenho:.1f}"),
]


kpi_html = ""

for titulo, valor in kpis:

    kpi_html += f"""
    <div class="kpi">
        <div class="kpi-label">{titulo}</div>
        <div class="kpi-value">{valor}</div>
    </div>
    """


salario_dep = (
    df_filtrado
    .groupby("Departamento", as_index=False)["Salário"]
    .mean()
    .sort_values("Salário", ascending=True)
)


fig1 = px.bar(
    salario_dep,
    x="Salário",
    y="Departamento",
    orientation="h",
    text="Salário",
)


fig1.update_traces(
    marker_color="#08c9e8",
    texttemplate="R$ %{x:,.0f}",
    textposition="outside",
    cliponaxis=False,
)


sat_dep = (
    df_filtrado
    .groupby("Departamento", as_index=False)["Satisfação"]
    .mean()
    .sort_values("Satisfação", ascending=True)
)


fig2 = px.bar(
    sat_dep,
    x="Satisfação",
    y="Departamento",
    orientation="h",
    text="Satisfação",
)


fig2.update_traces(
    marker_color="#ff2990",
    texttemplate="%{x:.1f}",
    textposition="outside",
    cliponaxis=False,
)


ordem_departamento = sorted(
    df_filtrado["Departamento"].unique()
)


cores_departamento = {
    "Vendas": "#4c7ee8",
    "TI": "#f39b32",
    "RH": "#43cf9b",
    "Finanças": "#0cc7e6",
    "Marketing": "#f42c8c",
}


fig3 = go.Figure()


for departamento in ordem_departamento:

    dados_dep = df_filtrado[
        df_filtrado["Departamento"] == departamento
    ]

    fig3.add_trace(
        go.Box(
            y=dados_dep["Salário"],
            x=[departamento] * len(dados_dep),
            name=departamento,
            marker_color=cores_departamento.get(
                departamento,
                "#4c7ee8"
            ),
            line_color=cores_departamento.get(
                departamento,
                "#4c7ee8"
            ),
            boxmean=True,
            hovertemplate=(
                "<b>%{x}</b><br>"
                "Salário: R$ %{y:,.0f}"
                "<extra></extra>"
            ),
            showlegend=False,
        )
    )


fig4 = px.scatter(
    df_filtrado,
    x="Salário",
    y="Satisfação",
    color="Departamento",
    color_discrete_map=cores_departamento,
    hover_name="Nome",
    hover_data=[
        "Cargo",
        "Idade",
        "Experiência (anos)",
        "Horas Trabalhadas",
        "Desempenho",
    ],
)


fig4.update_traces(
    marker=dict(
        size=9,
        opacity=0.9
    )
)


fig5 = px.scatter(
    df_filtrado,
    x="Horas Trabalhadas",
    y="Salário",
    color="Departamento",
    color_discrete_map=cores_departamento,
    hover_name="Nome",
    hover_data=[
        "Cargo",
        "Idade",
        "Experiência (anos)",
        "Satisfação",
        "Desempenho",
    ],
)


fig5.update_traces(
    marker=dict(
        size=9,
        opacity=0.9
    )
)


FUNDO = "#0b1321"
PAPER = "#0b111d"
GRID = "#26364d"
TEXTO = "#dce5f2"
EIXO = "#91a1b7"


def configurar_figura(
    fig,
    titulo,
    x_title="",
    y_title="",
    legenda=False,
):

    fig.update_layout(
        autosize=True,
        paper_bgcolor=PAPER,
        plot_bgcolor=FUNDO,
        font=dict(
            family="Arial, Helvetica, sans-serif",
            color=TEXTO,
            size=10,
        ),
        title=dict(
            text=titulo.upper(),
            font=dict(
                family="Arial, Helvetica, sans-serif",
                size=13,
                color="#f4f7fb",
            ),
            x=0.02,
            xanchor="left",
            y=0.97,
            yanchor="top",
        ),
        margin=dict(
            l=45,
            r=18,
            t=34,
            b=38,
        ),
        showlegend=legenda,
        legend=dict(
            orientation="v",
            x=0.98,
            xanchor="right",
            y=0.98,
            yanchor="top",
            bgcolor="rgba(11,17,29,0.88)",
            bordercolor="#30425c",
            borderwidth=1,
            font=dict(
                size=9,
                color="#edf3fb"
            ),
        ),
        hoverlabel=dict(
            bgcolor="#101a2a",
            font=dict(
                color="#ffffff",
                size=11
            )
        ),
        xaxis=dict(
            title=x_title,
            title_font=dict(
                size=9,
                color=EIXO
            ),
            tickfont=dict(
                size=8,
                color=EIXO
            ),
            gridcolor=GRID,
            zerolinecolor=GRID,
            linecolor=GRID,
            automargin=True,
        ),
        yaxis=dict(
            title=y_title,
            title_font=dict(
                size=9,
                color=EIXO
            ),
            tickfont=dict(
                size=8,
                color=EIXO
            ),
            gridcolor=GRID,
            zerolinecolor=GRID,
            linecolor=GRID,
            automargin=True,
        ),
        hovermode="closest",
    )

    return fig


fig1 = configurar_figura(
    fig1,
    "Salário médio por departamento",
    "Salário",
    "Departamento",
    False,
)


fig2 = configurar_figura(
    fig2,
    "Satisfação média por departamento",
    "Satisfação",
    "Departamento",
    False,
)


fig3 = configurar_figura(
    fig3,
    "Distribuição salarial por departamento",
    "Departamento",
    "Salário",
    True,
)


fig4 = configurar_figura(
    fig4,
    "Salário × Satisfação",
    "Salário",
    "Satisfação",
    True,
)


fig5 = configurar_figura(
    fig5,
    "Horas Trabalhadas × Salário",
    "Horas trabalhadas",
    "Salário",
    True,
)


fig1.update_xaxes(
    tickprefix="R$ ",
    separatethousands=True
)


fig3.update_yaxes(
    tickprefix="R$ ",
    separatethousands=True
)


fig5.update_yaxes(
    tickprefix="R$ ",
    separatethousands=True
)


fig4.update_xaxes(
    tickprefix="R$ ",
    separatethousands=True
)


config = {
    "displayModeBar": "hover",
    "displaylogo": False,
    "responsive": True,
    "scrollZoom": True,
    "modeBarButtonsToRemove": [
        "lasso2d",
        "select2d",
    ],
}


def gerar_grafico(fig):

    return fig.to_html(
        full_html=False,
        include_plotlyjs=False,
        config=config,
        default_height="100%",
        default_width="100%",
    )


grafico1 = gerar_grafico(fig1)
grafico2 = gerar_grafico(fig2)
grafico3 = gerar_grafico(fig3)
grafico4 = gerar_grafico(fig4)
grafico5 = gerar_grafico(fig5)


plotly_js = """
<script src="https://cdn.plot.ly/plotly-2.35.2.min.js"></script>
"""


html = f"""
<!DOCTYPE html>

<html>

<head>

<meta charset="UTF-8">

<style>

* {{
    box-sizing: border-box;
}}

html,
body {{
    width: 100%;
    height: 100%;
    margin: 0;
    padding: 0;
    overflow: hidden;
    background: #070c16;
    font-family: Arial, Helvetica, sans-serif;
}}

.dashboard {{
    width: 100%;
    height: 100vh;
    display: flex;
    flex-direction: column;
    gap: 8px;
    padding: 0 0 2px 0;
}}

.kpis {{
    width: 100%;
    display: grid;
    grid-template-columns:
        repeat(5, minmax(0, 1fr));
    gap: 8px;
    flex: 0 0 66px;
}}

.kpi {{
    min-width: 0;
    background: #0b1321;
    border: 1px solid #293b54;
    border-radius: 5px;
    padding: 9px 11px 7px 11px;
    display: flex;
    flex-direction: column;
    justify-content: center;
}}

.kpi-label {{
    color: #a6b5c9;
    font-size: 8px;
    font-weight: 700;
    letter-spacing: .2px;
    margin-bottom: 3px;
    white-space: nowrap;
}}

.kpi-value {{
    color: #00d9ff;
    font-size: 20px;
    font-weight: 800;
    line-height: 1;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}}

.charts {{
    width: 100%;
    min-height: 0;
    flex: 1 1 auto;
    display: grid;
    grid-template-columns:
        repeat(6, minmax(0, 1fr));
    grid-template-rows:
        minmax(0, 1fr)
        minmax(0, 1fr);
    gap: 8px;
}}

.chart-card {{
    min-width: 0;
    min-height: 0;
    overflow: hidden;
    background: #0b1321;
    border: 1px solid #293b54;
    border-radius: 5px;
    padding: 2px;
    position: relative;
}}

.chart-1 {{
    grid-column: span 2;
}}

.chart-2 {{
    grid-column: span 2;
}}

.chart-3 {{
    grid-column: span 2;
}}

.chart-4 {{
    grid-column: span 3;
}}

.chart-5 {{
    grid-column: span 3;
}}

.chart {{
    width: 100%;
    height: 100%;
    min-height: 0;
}}

.chart > div {{
    width: 100% !important;
    height: 100% !important;
}}

.js-plotly-plot,
.plot-container,
.svg-container {{
    width: 100% !important;
    height: 100% !important;
}}

@media (max-width: 1000px) {{

    .kpis {{
        grid-template-columns:
            repeat(5, minmax(0, 1fr));
    }}

    .kpi-value {{
        font-size: 16px;
    }}

    .charts {{
        gap: 5px;
    }}

}}

</style>

{plotly_js}

</head>

<body>

<div class="dashboard">

    <div class="kpis">
        {kpi_html}
    </div>

    <div class="charts">

        <div class="chart-card chart-1">
            <div class="chart">
                {grafico1}
            </div>
        </div>

        <div class="chart-card chart-2">
            <div class="chart">
                {grafico2}
            </div>
        </div>

        <div class="chart-card chart-3">
            <div class="chart">
                {grafico3}
            </div>
        </div>

        <div class="chart-card chart-4">
            <div class="chart">
                {grafico4}
            </div>
        </div>

        <div class="chart-card chart-5">
            <div class="chart">
                {grafico5}
            </div>
        </div>

    </div>

</div>

</body>

</html>
"""


components.html(
    html,
    height=650,
    scrolling=False,
)