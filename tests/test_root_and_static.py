def test_root_redirects_and_static_served(client):
    # Arrange

    # Act: request root
    resp_root = client.get("/", follow_redirects=False)

    # Assert: redirection to /static/index.html
    assert resp_root.status_code in (307, 302)
    assert "/static/index.html" in resp_root.headers.get("location", "")

    # Act: fetch static index (follow)
    resp_index = client.get("/static/index.html")

    # Assert: static file served
    assert resp_index.status_code == 200
    assert "Mergington High School" in resp_index.text
