# WellNex – Day 2 ✅

## 🌤️ Mood Tracker API

### ✅ Implemented:
- `Mood` model with mood choices (happy, sad, angry, etc.)
- Linked mood to authenticated user
- Created `MoodSerializer`
- Created protected `MoodViewSet` for:
  - Create mood check-in
  - View all user moods
  - Update/delete mood entries
- Registered routes using DRF's `DefaultRouter`

### 🔐 Protected with JWT

| Endpoint            | Method | Description           |
|---------------------|--------|-----------------------|
| `/api/moods/`       | GET    | List user moods       |
| `/api/moods/`       | POST   | Create mood entry     |
| `/api/moods/<id>/`  | PUT    | Update mood entry     |
| `/api/moods/<id>/`  | DELETE | Delete mood entry     |

## 🧪 Tested With:
- Bearer Token Authorization (JWT)
- CRUD operations from Thunder Client

---

📁 Commit:  
`git commit -m "Day 2: Created Mood model, serializer, and CRUD API"`

🚀 Next: Setup React frontend + Bootstrap + Router
