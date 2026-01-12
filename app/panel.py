import panel as pn

def build_panel_app(data):
    pn.extension()

    valid_columns = [col for col in data.get_column_names() if not data.to_point_gdf()[col].isna().all()]
    col_selector = pn.widgets.Select(name="Select column", options = valid_columns, value=valid_columns[0])

    def explore_plot(data, column):
        return pn.pane.plot.Folium(data.explore(column=column), min_width=800, min_height=600, sizing_mode="stretch_both")

    out_plt = pn.bind(explore_plot, data=data, column=col_selector)

    template = pn.template.MaterialTemplate(
        site="MoveApps",
        title="Testing Panel",
        sidebar=[col_selector],
        main=[out_plt],
    )

    return template

def serve_panel_app(template, port=5006):
    pn.serve(
        template,
        start=True,
        show=False,
        port=port,
        address="0.0.0.0",
        allow_websocket_origin=["*"]
    )