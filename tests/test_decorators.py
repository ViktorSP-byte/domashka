from src.decorators import log

def test_decorators(capsys):
    @log
    def divider(x, y):
         return x / y
    divider(4, 2)
captured = capsys.readouterr()
assert '2' in captured.ou