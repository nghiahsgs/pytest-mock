from main import total
import pytest

@pytest.mark.parametrize(
    "x,y,result",
    [
        (1,1,2),
        (1,2,3),
        (1,3,4),
        (1,4,5),
    ]
)
def test_total(mocker,x,y,result):
    _ = mocker.patch(
        "tests.test_main.total",
        return_value=x+y,
    )
    assert total(x,y)==result
    _.assert_called_once()