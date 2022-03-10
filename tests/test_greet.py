from pynterviews.greet import cli


def test_greet_cli(capsys):
    args = ["America/Argentina/San_Juan"]
    cli(args)
    captured = capsys.readouterr()
    result = captured.out
    assert "San Juan!" in result