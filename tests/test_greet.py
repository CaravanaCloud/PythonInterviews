from pynterviews.greet import cli


def test_greet_cli(capsys):
    args = []
    cli(args)
    captured = capsys.readouterr()
    result = captured.out
    assert "Hello hello." in result