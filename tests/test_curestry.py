import pytest
from curestry.curestry import Curestry
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from unittest import mock

@pytest.fixture(scope="module")
def setup_engine():
    """Fixture to create a temporary SQLite engine for testing."""
    engine = create_engine("sqlite:///:memory:")
    Curestry.Session = sessionmaker(bind=engine)
    Curestry.engine = engine
    # Create all tables
    from curestry.data.data_models import Base
    Base.metadata.create_all(engine)
    yield engine

@pytest.fixture
def curestry_instance(setup_engine):
    """Fixture to provide a clean instance of Curestry for each test."""
    return Curestry()

def test_connect_project(curestry_instance):
    """Test connecting to an existing project."""
    project_name = "Connect Project"

    # Try creating the project; if it already exists, pass the exception
    try:
        curestry_instance.create_project(project_name)
    except ValueError as e:
        assert str(e) == f"Project '{project_name}' already exists."

    # Connect to the project (should succeed if already exists or just created)
    connected_id = curestry_instance.connect_project(project_name)
    assert connected_id == curestry_instance.project_id
    assert curestry_instance.project_name == project_name

def test_create_project(curestry_instance):
    """Test creating a new project."""
    project_name = "Test Project"

    # Create project
    try:
        project_id = curestry_instance.create_project(project_name)
        assert project_id is not None
        assert curestry_instance.project_name == project_name
    except:
        # Test for duplicate project creation
        with pytest.raises(ValueError, match=f"Project '{project_name}' already exists."):
            curestry_instance.create_project(project_name)

def test_list_projects(curestry_instance):
    """Test listing projects."""
    project_names = ["Project 1", "Project 2", "Project 3"]

    for name in project_names:
        try:
            curestry_instance.create_project(name)
        except ValueError as e:
            assert str(e) == f"Project '{name}' already exists."

    # List projects
    projects = Curestry.list_projects()
    assert len(projects) >= len(project_names)

    # Verify projects are listed
    project_names_in_list = [p["name"] for p in projects]
    for name in project_names:
        assert name in project_names_in_list

    # Test limiting the number of listed projects
    limited_projects = Curestry.list_projects(num_projects=2)
    assert len(limited_projects) == 2

@mock.patch("curestry.server.dashboard.launch_dashboard")
def test_launch_dashboard(mock_launch_dashboard):
    """Test launching the dashboard."""
    Curestry.launch_dashboard(port=4000)
    mock_launch_dashboard.assert_called_once_with(4000)
