def test_activity_state_sequence_isolated(client):
    # Arrange
    activity_name = "Tennis Club"
    email = "isolation_test@mergington.edu"

    # Act: signup
    resp_signup = client.post(f"/activities/{activity_name}/signup", params={"email": email})
    assert resp_signup.status_code == 200

    # Assert: participant present in activities
    resp_activities = client.get("/activities")
    participants = resp_activities.json()[activity_name]["participants"]
    assert email in participants

    # Act: unregister
    resp_del = client.delete(f"/activities/{activity_name}/participants", params={"email": email})
    assert resp_del.status_code == 200

    # Assert: participant removed
    resp_activities2 = client.get("/activities")
    participants2 = resp_activities2.json()[activity_name]["participants"]
    assert email not in participants2
