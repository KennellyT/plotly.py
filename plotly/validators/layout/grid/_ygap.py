import _plotly_utils.basevalidators


class YgapValidator(_plotly_utils.basevalidators.NumberValidator):

    def __init__(
        self, plotly_name='ygap', parent_name='layout.grid', **kwargs
    ):
        super(YgapValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='plot',
            max=1,
            min=0,
            role='info',
            **kwargs
        )