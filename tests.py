from main import app

with app.test_client as c:
  res = app.get("/")
  assert res.data == b'Hello from Flask!'
  assert res.status == 200

  

