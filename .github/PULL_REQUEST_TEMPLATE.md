Description of PR that completes issue here...

## Changes
- Item 1
- Item 2
- Item 3

## Requests / Responses
If this PR contains code that defines a new request/response, or changes an existing one, please put the JSON representations here.

**Request**

POST `/characters` Creates a new character

```json
{
    "name": "Thorin Ironfoot",
    "race_id": 3,
    "class_id": 1,
    "level": 1,
    "background": "Soldier"
}
```

**Response**

HTTP/1.1 201 Created

```json
{
    "id": 42,
    "name": "Thorin Ironfoot",
    "race_id": 3,
    "class_id": 1,
    "level": 1,
    "background": "Soldier",
    "user_id": 7
}
```

## Testing
Description of how to test code...
- [ ] Run migrations
- [ ] Run test suite
- [ ] Seed database

## Related Issues
- Fixes #85
- Fixes #22