import pytest
from authenticator import Authenticator

@pytest.fixture
def authenticator():
    auth = Authenticator()
    yield auth

def test_register_success(authenticator):
    authenticator.register("username", "password")
    assert authenticator.users["username"] == "password"

def test_register_existing_user(authenticator):
    authenticator.register("username", "password")
    with pytest.raises(ValueError, match="エラー: ユーザーは既に存在します。"):
        authenticator.register("username", "password")

def test_login_success(authenticator):
    authenticator.register("username", "password")
    result = authenticator.login("username", "password")
    assert result == "ログイン成功"

def test_login_incorrect_password(authenticator):
    authenticator.register("username", "password")
    with pytest.raises(ValueError, match="エラー: ユーザー名またはパスワードが正しくありません。"):
        authenticator.login("username", "ng_password")
