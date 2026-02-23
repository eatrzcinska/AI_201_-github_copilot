def test_signup_nonexistent_activity_returns_404(client):
    # Arrange
    activity_name = "Nonexistent Activity"
    email = "someone@mergington.edu"

    # Act
    resp = client.post(f"/activities/{activity_name}/signup", params={"email": email})

    # Assert
    assert resp.status_code == 404
    assert "Activity not found" in resp.json().get("detail", "")
