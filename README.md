Testing through postman or cmd.

Run test app:
1. run below command on teminal:
   uvicorn test_app.app:app

   test_app is folder name and app is file name.
2. In postman:
   run GET method with this url: http://localhost:8000/test-jsonplaceholder?endpoint=posts
   run POST method with this URL: http://localhost:8000/test-post-endpoint and body 
   data: {
  "title": "foo",
  "body": "bar",
  "userId": 1
}

3. In CMD run below commands:
   curl -X GET "http://localhost:8000/test-jsonplaceholder?endpoint=posts&post_id=1"
   curl -X POST "http://localhost:8000/test-post-endpoint" -H "Content-Type: application/json" -d "{\"title\": \"foo\", \"body\": \"bar\", \"userId\": 1}"
