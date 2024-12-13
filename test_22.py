import pytest



@pytest.fixture(scope="function")
def prepare_faces():
    print("^_^", "\n")
    yield
    print(":3", "\n")


@pytest.fixture(autouse=True)
def very_important_fixture():
    print(":)", "\n")


@pytest.fixture()
def print_smiling_faces():
    print(":-Р", "\n")


class TestPrintSmilingFaces():
    def test_first_smiling_faces(self, prepare_faces, very_important_fixture):
        pass
    def test_second_smiling_faces(self, prepare_faces,print_smiling_faces):
        pass