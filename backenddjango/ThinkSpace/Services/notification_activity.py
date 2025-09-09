from datetime import datetime, timedelta, timezone
class NotificationActivity:
  def run(self):
    now = datetime.now(timezone.utc).astimezone()
    results = [{
        'uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
        'handle': 'Jon',
        'message': 'You are a wildling',
        'created_at': (now - timedelta(days=2)).isoformat(),
        'expires_at': (now + timedelta(days=5)).isoformat(),
        'likes_count': 5,
        'replies_count': 1,
        'reposts_count': 0,
        'replies': [{
            'uuid': '26e12864-1c26-5c3a-9658-97a10f8fea67',
            'reply_to_activity_uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
            'handle': 'Ygrette',
            'message': 'You know nothing Jon snow',
            'likes_count': 0,
            'replies_count': 0,
            'reposts_count': 0,
            'created_at': (now - timedelta(days=2)).isoformat()
        }],
    },

    ]
    return results