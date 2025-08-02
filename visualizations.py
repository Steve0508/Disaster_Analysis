import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import analysis
import streamlit.components.v1 as components
import base64
from io import BytesIO

sns.set(style="whitegrid")

def fig_to_base64(fig):
    buf = BytesIO()
    fig.savefig(buf, format="png", bbox_inches='tight')
    buf.seek(0)
    img_bytes = buf.getvalue()
    base64_img = base64.b64encode(img_bytes).decode()
    return f"data:image/png;base64,{base64_img}"

def generate_chart_card(title, data, xlabel, ylabel):
    if not data:
        return ""

    labels, values = zip(*data)
    fig, ax = plt.subplots(figsize=(7, 4))
    sns.barplot(x=list(labels), y=list(values), ax=ax, palette="viridis")
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.tick_params(axis='x', rotation=45)
    img_uri = fig_to_base64(fig)
    plt.close(fig)

    return f"""
    <div class="card">
        <h4>{title}</h4>
        <img src="{img_uri}" alt="{title}" class="chart-img"/>
    </div>
    """

def show_all_visualizations():
    

    st.markdown("""
        <style>
            .slider-container {{
                display: flex;
                overflow-x: auto;
                gap: 16px;
                padding: 10px;
            }}
            .card {{
                flex: 0 0 auto;
                background: #f9f9f9;
                padding: 15px;
                border-radius: 12px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                width: 420px;
                min-height: 350px;
                text-align: center;
            }}
            .chart-img {{
                width: 100%;
                height: auto;
                border-radius: 8px;
            }}
        </style>
    """, unsafe_allow_html=True)

    cards_html = ""

    charts = [
        ("Top 5 Most Affected Regions", analysis.most_affected_area(), "Region", "Disaster Count"),
        ("Year-wise Disaster Count", analysis.year_wise_disaster_count(), "Year", "Count"),
        ("Disaster Type Frequency", analysis.disaster_types_frequency(), "Disaster Type", "Count"),
        ("Top 5 Regions by Economic Loss", analysis.top_countries_by_economic_loss(), "Region", "Total Loss (₹)"),
        ("Top 10 Disasters by Population Affected", analysis.population_affected_per_disaster(), "Disaster", "Population Affected"),
        ("Disasters per Country", analysis.total_disasters_per_country(), "Country", "Count"),
        ("Average Duration by Disaster Type", analysis.avg_duration_by_disaster_type(), "Disaster Type", "Avg Duration (Days)"),
        ("Monthly Disaster Distribution", analysis.monthly_disaster_count(), "Month", "Count"),
        ("Average Economic Loss by Region", analysis.avg_economic_loss_by_region(), "Region", "Avg Loss"),
        ("Countries with Most Floods", analysis.countries_with_most_floods(), "Country", "Flood Count"),
        ("Disaster Count by Severity Level", analysis.disaster_count_by_severity(), "Severity", "Count"),
    ]

    for title, data, xlabel, ylabel in charts:
        cards_html += generate_chart_card(title, data, xlabel, ylabel)

    full_html = f"""
    <div class="slider-container">
        {cards_html}
    </div>
    """

    components.html(full_html, height=600, scrolling=True)

# Run directly
if __name__ == "__main__":
    show_all_visualizations()