def test_get_activities_returns_expected_fields(client):
    # Arrange: client fixture and existing activities from app

    # Act
    response = client.get("/activities")
    data = response.json()

    # Assert
    assert response.status_code == 200
    assert isinstance(data, dict)
    # Pick one activity and check fields
    any_activity = next(iter(data.values()))
    assert "participants" in any_activity
    assert "max_participants" in any_activity
