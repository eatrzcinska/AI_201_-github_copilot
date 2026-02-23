def test_unregister_success_and_not_found(client):
    # Arrange
    activity_name = "Programming Class"
    email = "temp_student@mergington.edu"

    # Ensure the email is signed up first
    resp_signup = client.post(f"/activities/{activity_name}/signup", params={"email": email})
    assert resp_signup.status_code == 200

    # Act: unregister existing participant
    resp_del = client.delete(f"/activities/{activity_name}/participants", params={"email": email})

    # Assert successful removal
    assert resp_del.status_code == 200
    assert "Unregistered" in resp_del.json().get("message", "")

    # Act: attempt to delete again (should be not found)
    resp_del2 = client.delete(f"/activities/{activity_name}/participants", params={"email": email})

    # Assert not found
    assert resp_del2.status_code == 404
    assert "Participant not found" in resp_del2.json().get("detail", "")
