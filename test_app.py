import os
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from dash.testing.application_runners import import_app

# Automatically download and manage chromedriver.
# This ensures the driver executable is available in the system's PATH.
# We get the directory of the driver and add it to the start of the PATH.
driver_path = ChromeDriverManager().install()
os.environ["PATH"] = os.path.dirname(driver_path) + os.pathsep + os.environ["PATH"]


# The app fixture imports the Dash app from your app.py file
@pytest.fixture
def app():
    app = import_app("app")
    return app

# The following tests use the default `dash_duo` fixture provided by the
# dash-pytest plugin. The fixture will now be able to find the chromedriver
# executable because its location is in the system's PATH.

def test_header_is_present(dash_duo, app):
    """
    Test 1: Verifies that the main H1 header is present and contains the correct text.
    """
    dash_duo.start_server(app)
    header = dash_duo.find_element("h1")
    assert header.text == "Soul Foods: Pink Morsel Sales Analysis"
    dash_duo.take_snapshot("test_header_is_present")

def test_visualization_is_present(dash_duo, app):
    """
    Test 2: Verifies that the graph visualization is rendered on the page.
    """
    dash_duo.start_server(app)
    graph = dash_duo.wait_for_element("#sales-line-chart")
    assert graph is not None
    dash_duo.take_snapshot("test_visualization_is_present")

def test_region_picker_is_present(dash_duo, app):
    """
    Test 3: Verifies that the region picker radio buttons are present.
    """
    dash_duo.start_server(app)
    radio_picker = dash_duo.wait_for_element("#region-radio-buttons")
    assert radio_picker is not None
    dash_duo.take_snapshot("test_region_picker_is_present")

