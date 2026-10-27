from quantflow.core.environment import Environment
from quantflow.core.settings import Settings


def test_production_disables_debug_and_docs() -> None:
    """Production settings disable unsafe developer conveniences."""
    settings = Settings(env=Environment.PRODUCTION, debug=True, enable_docs=True)

    assert settings.debug is False
    assert settings.enable_docs is False


def test_development_enables_docs() -> None:
    """Development settings expose API documentation."""
    settings = Settings(env=Environment.DEVELOPMENT, enable_docs=False)

    assert settings.enable_docs is True
