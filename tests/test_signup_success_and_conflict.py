def test_signup_success_and_conflict(client):
    # Arrange
    activity_name = "Chess Club"
    email = "test_student@mergington.edu"

    # Act: signup first time
    resp1 = client.post(f"/activities/{activity_name}/signup", params={"email": email})
    data1 = resp1.json()

    # Assert success
    assert resp1.status_code == 200
    assert "Signed up" in data1.get("message", "")

    # Act: signup same email again
    resp2 = client.post(f"/activities/{activity_name}/signup", params={"email": email})
    data2 = resp2.json()

    # Assert conflict
    assert resp2.status_code == 400
    assert "already signed up" in data2.get("detail", "")
