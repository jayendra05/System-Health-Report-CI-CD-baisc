from app import generate_health_report


def test_health_report():

    report = generate_health_report()

    assert "Hostname" in report
    assert "Operating System" in report
    assert "OS Version" in report
    assert "Python Version" in report
    assert "Environment" in report
    assert "Report Generated" in report


def test_python_version():

    report = generate_health_report()

    assert report["Python Version"] != ""


def test_hostname():

    report = generate_health_report()

    assert report["Hostname"] != ""


def test_environment():

    report = generate_health_report()

    assert report["Environment"] != ""