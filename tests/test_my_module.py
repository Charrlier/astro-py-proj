from src import my_module

def test_greet(capsys):
    my_module.greet("Tester")
    captured = capsys.readouterr()
    assert "Hello, Tester!" in captured.out

def test_display_chart():
    # Here you would add tests for display_chart functionality
    pass
