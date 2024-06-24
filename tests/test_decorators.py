from src.decorators import my_function


def test_file_log():
    """Тестирует логирование в файл"""
    my_function(1, 0)
    with open("mylog.txt", "r") as file:
        result = file.read()
        assert result == "my_function error: division by zero. Inputs: (1, 0), {}\n"


def test_console_log(capsys):
    """Тестирует логирование в консоль"""
    my_function(10, 5)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"
