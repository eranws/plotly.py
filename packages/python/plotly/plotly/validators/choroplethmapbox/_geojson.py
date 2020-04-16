import _plotly_utils.basevalidators


class GeojsonValidator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(self, plotly_name="geojson", parent_name="choroplethmapbox", **kwargs):
        super(GeojsonValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )
