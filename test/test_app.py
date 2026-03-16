def test_header_present(dash_duo):
    from app import app

    dash_duo.start_server(app)

    header = dash_duo.find_element("h1")

    assert header.text == "Pink Morsel Sales Analysis"


def test_visualisation_present(dash_duo):
    from app import app

    dash_duo.start_server(app)

    graph = dash_duo.find_element("#sales-chart")

    assert graph is not None


def test_region_picker_present(dash_duo):
    from app import app

    dash_duo.start_server(app)

    radio = dash_duo.find_element("#region-filter")

    assert radio is not None