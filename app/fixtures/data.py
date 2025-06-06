# app/fixtures/data.py

from datetime import datetime, timedelta, date
from constants.roles import RouteRole

USERS_FIXTURES = [
    {
        # "id": 1,
        "telegram_id": 100001,
        "username": "alice_bot",
        "first_name": "Alice",
        "last_name": "Wonder",
        "language": "en",
        "is_premium": True,
        "is_bot": False,
    },
    {
        # "id": 2,
        "telegram_id": 100002,
        "username": "bob_travel",
        "first_name": "Bob",
        "last_name": "Builder",
        "language": "en",
        "is_premium": False,
        "is_bot": False,
    },
    {
        # "id": 3,
        "telegram_id": 100003,
        "username": "charlie",
        "first_name": "Charlie",
        "last_name": "Chaplin",
        "language": "en",
        "is_premium": False,
        "is_bot": True,
    },
    {
        # "id": 4,
        "telegram_id": 100004,
        "username": "diana_trips",
        "first_name": "Diana",
        "last_name": "Prince",
        "language": "fr",
        "is_premium": True,
        "is_bot": False,
    },
    {
        # "id": 5,
        "telegram_id": 100005,
        "username": "ed_explorer",
        "first_name": "Edward",
        "last_name": "Snow",
        "language": "de",
        "is_premium": False,
        "is_bot": False,
    },
]

AICACHE_FIXTURES = [
    {
        # "id": 1,
        "user_id": 1,
        "cache_key": "Paris:Paris:3:1500.0",
        "prompt_hash": "fa1d3b3c0cb23a1dd47ff2b8f8e1d3a4",  # условный md5
        "original_prompt": "Plan a 3-day trip to Paris for a couple interested in art and food.",
        "origin": "Paris",
        "destination": "Paris",
        "duration_days": 3,
        "budget": 1500.0,
        "interests": ["culture", "food", "museums"],
        "hit_count": 1,
        "source": "bot",
        "expires_at": datetime.now() + timedelta(days=30),
        "result": {
            "name": "Paris Adventure",
            "origin": "Paris",
            "destination": "Paris",
            "duration_days": 3,
            "budget": 1500.0,
            "interests": ["culture", "food", "museums"],
            "days": [
                {
                    "day_number": 1,
                    "description": "Arrival and city walk",
                    "date": "2025-04-15",
                    "activities": [
                        {
                            "name": "Check-in at hotel",
                            "description": "Drop off luggage at the hotel",
                            "start_time": "10:30",
                            "end_time": "11:00",
                            "location": "Hotel Le Meurice",
                            "cost": 0.0,
                            "notes": "Early check-in requested",
                            "activity_type": "Accommodation",
                            "external_link": "https://lemeurice.com",
                        },
                        {
                            "name": "Walk around Louvre",
                            "description": "Explore the outside area of the Louvre",
                            "start_time": "12:00",
                            "end_time": "14:00",
                            "location": "Louvre Museum",
                            "cost": 0.0,
                            "activity_type": "Sightseeing",
                        },
                    ],
                },
                {
                    "day_number": 2,
                    "description": "Museum and food day",
                    "date": "2025-04-16",
                    "activities": [
                        {
                            "name": "Visit Musée d'Orsay",
                            "start_time": "10:00",
                            "end_time": "13:00",
                            "location": "Musée d'Orsay",
                            "cost": 15.0,
                            "activity_type": "Museum",
                        },
                        {
                            "name": "Lunch at Café de Flore",
                            "start_time": "13:30",
                            "end_time": "14:30",
                            "location": "Café de Flore",
                            "cost": 35.0,
                            "activity_type": "Food",
                        },
                    ],
                },
                {
                    "day_number": 3,
                    "description": "Shopping and departure",
                    "date": "2025-04-17",
                    "activities": [
                        {
                            "name": "Champs-Élysées shopping",
                            "start_time": "10:00",
                            "end_time": "12:00",
                            "location": "Champs-Élysées",
                            "cost": 0.0,
                            "activity_type": "Shopping",
                        },
                        {
                            "name": "Flight home",
                            "start_time": "15:00",
                            "end_time": "18:00",
                            "location": "CDG Airport",
                            "cost": 0.0,
                            "activity_type": "Transportation",
                        },
                    ],
                },
            ],
        },
    },
    {
        # "id": 2,
        "user_id": 2,
        "cache_key": "Tokyo:Tokyo:5:2500.0",
        "prompt_hash": "b7b1cde442f4b3e732ada8d0f9c5d3a0",
        "original_prompt": "Plan a 5-day trip to Tokyo for a solo traveler interested in technology and anime.",
        "origin": "Tokyo",
        "destination": "Tokyo",
        "duration_days": 5,
        "budget": 2500.0,
        "interests": ["technology", "anime", "gaming"],
        "hit_count": 3,
        "source": "bot",
        "expires_at": datetime.now() + timedelta(days=25),
        "result": {
            "name": "Tech & Anime Tokyo",
            "origin": "Tokyo",
            "destination": "Tokyo",
            "duration_days": 5,
            "budget": 2500.0,
            "interests": ["technology", "anime", "gaming"],
            "days": [
                {
                    "day_number": 1,
                    "description": "Akihabara tour",
                    "date": "2025-05-01",
                    "activities": [
                        {
                            "name": "Visit Akihabara",
                            "start_time": "10:00",
                            "end_time": "13:00",
                            "location": "Akihabara",
                            "cost": 0.0,
                            "activity_type": "Sightseeing",
                        }
                    ],
                }
            ],
        },
    },
    {
        # "id": 3,
        "user_id": 3,
        "cache_key": "New York:New York:2:1000.0",
        "prompt_hash": "c99de9bc0b824af4a1c7d2be77c87651",
        "original_prompt": "Quick weekend getaway in New York focused on landmarks and nightlife.",
        "origin": "New York",
        "destination": "New York",
        "duration_days": 2,
        "budget": 1000.0,
        "interests": ["nightlife", "sightseeing"],
        "hit_count": 2,
        "source": "api",
        "expires_at": datetime.now() + timedelta(days=20),
        "result": {
            "name": "NYC Express",
            "origin": "New York",
            "destination": "New York",
            "duration_days": 2,
            "budget": 1000.0,
            "interests": ["nightlife", "sightseeing"],
            "days": [
                {
                    "day_number": 1,
                    "description": "Landmark hopping",
                    "date": "2025-05-10",
                    "activities": [
                        {
                            "name": "Visit Times Square",
                            "start_time": "12:00",
                            "end_time": "14:00",
                            "location": "Times Square",
                            "cost": 0.0,
                            "activity_type": "Sightseeing",
                        }
                    ],
                }
            ],
        },
    },
    {
        # "id": 4,
        "user_id": 1,
        "cache_key": "Barcelona:Barcelona:4:1800.0",
        "prompt_hash": "c1d224ffd93882cb11b0021c49977ab7",
        "original_prompt": "Plan a relaxed trip to Barcelona focused on beaches and local cuisine.",
        "origin": "Barcelona",
        "destination": "Barcelona",
        "duration_days": 4,
        "budget": 1800.0,
        "interests": ["beach", "food", "culture"],
        "hit_count": 5,
        "source": "bot",
        "expires_at": datetime.now() + timedelta(days=40),
        "result": {
            "name": "Barcelona Bliss",
            "origin": "Barcelona",
            "destination": "Barcelona",
            "duration_days": 4,
            "budget": 1800.0,
            "interests": ["beach", "food", "culture"],
            "days": [
                {
                    "day_number": 1,
                    "description": "Beach day",
                    "date": "2025-06-01",
                    "activities": [
                        {
                            "name": "Relax at Barceloneta",
                            "start_time": "11:00",
                            "end_time": "16:00",
                            "location": "Barceloneta Beach",
                            "cost": 0.0,
                            "activity_type": "Beach",
                        }
                    ],
                }
            ],
        },
    },
    {
        # "id": 5,
        "user_id": 4,
        "cache_key": "Rome:Rome:3:1300.0",
        "prompt_hash": "a14a2f63f7c9d35172906c5610b9943d",
        "original_prompt": "Family trip to Rome with historical attractions.",
        "origin": "Rome",
        "destination": "Rome",
        "duration_days": 3,
        "budget": 1300.0,
        "interests": ["history", "architecture"],
        "hit_count": 4,
        "source": "bot",
        "expires_at": datetime.now() + timedelta(days=35),
        "result": {
            "name": "Roman Holiday",
            "origin": "Rome",
            "destination": "Rome",
            "duration_days": 3,
            "budget": 1300.0,
            "interests": ["history", "architecture"],
            "days": [
                {
                    "day_number": 1,
                    "description": "Ancient sights",
                    "date": "2025-06-10",
                    "activities": [
                        {
                            "name": "Visit Colosseum",
                            "start_time": "10:00",
                            "end_time": "12:00",
                            "location": "Colosseum",
                            "cost": 16.0,
                            "activity_type": "Museum",
                        }
                    ],
                }
            ],
        },
    },
]


ROUTES_FIXTURES = [
    {
        # "id": 1,
        "name": "Romantic Paris",
        "share_code": "sharecode-paris-001",
        "is_public": True,
        "origin": "Paris",
        "destination": "Paris",
        "duration_days": 3,
        "budget": 1500.0,
        "interests": ["romance", "culture", "art"],
        "route_data": {
            "name": "Tokyo Explorer",
            "origin": "Tokyo",
            "destination": "Tokyo",
            "duration_days": 2,
            "budget": 1000.0,
            "interests": ["technology", "culture"],
            "days": [
                {
                    # "id": 1,
                    "day_number": 1,
                    "date": "2025-04-15",
                    "description": "Arrival and first walk",
                    "activities": [
                        {
                            # "id": 1,
                            "name": "Hotel check-in",
                            "start_time": "10:30",
                            "end_time": "11:00",
                            "location": "Hotel Le Meurice",
                            "cost": 0.0,
                            "notes": "Early check-in requested",
                            "activity_type": "Accommodation",
                            "external_link": "https://lemeurice.com",
                        },
                        {
                            # "id": 2,
                            "name": "Louvre outside walk",
                            "start_time": "12:00",
                            "end_time": "14:00",
                            "location": "Louvre Museum",
                            "cost": 0.0,
                            "activity_type": "Sightseeing",
                        },
                    ],
                },
                {
                    # "id": 2,
                    "day_number": 2,
                    "date": "2025-04-16",
                    "description": "Museums and food",
                    "activities": [
                        {
                            # "id": 3,
                            "name": "Musée d'Orsay visit",
                            "start_time": "10:00",
                            "end_time": "13:00",
                            "location": "Musée d'Orsay",
                            "cost": 15.0,
                            "activity_type": "Museum",
                        },
                        {
                            # "id": 4,
                            "name": "Lunch at Café de Flore",
                            "start_time": "13:30",
                            "end_time": "14:30",
                            "location": "Café de Flore",
                            "cost": 35.0,
                            "activity_type": "Food",
                        },
                    ],
                },
                {
                    # "id": 3,
                    "day_number": 3,
                    "date": "2025-04-17",
                    "description": "Shopping and return",
                    "activities": [
                        {
                            # "id": 5,
                            "name": "Shopping Champs-Élysées",
                            "start_time": "10:00",
                            "end_time": "12:00",
                            "location": "Champs-Élysées",
                            "cost": 0.0,
                            "activity_type": "Shopping",
                        },
                        {
                            # "id": 6,
                            "name": "Flight home",
                            "start_time": "15:00",
                            "end_time": "18:00",
                            "location": "CDG Airport",
                            "cost": 0.0,
                            "activity_type": "Transportation",
                        },
                    ],
                },
            ],
        },
        "owner_id": 1,
        "ai_cache_id": 1,
        "last_edited_by": 1,
        "created_at": datetime(2025, 4, 15, 10, 0),
        "updated_at": datetime(2025, 4, 16, 9, 0),
    },
    {
        # "id": 2,
        "name": "Tokyo Explorer",
        "share_code": "sharecode-tokyo-002",
        "is_public": False,
        "origin": "Tokyo",
        "destination": "Tokyo",
        "duration_days": 2,
        "budget": 1000.0,
        "interests": ["technology", "culture"],
        "route_data": {
            "name": "Tokyo Explorer",
            "origin": "Tokyo",
            "destination": "Tokyo",
            "duration_days": 2,
            "budget": 1000.0,
            "interests": ["technology", "culture"],
            "days": [
                {
                    "day_number": 1,
                    "description": "Akihabara tech tour",
                    "date": "2025-04-20",
                    "activities": [
                        {
                            "name": "Gadget shopping",
                            "start_time": "10:00",
                            "end_time": "12:30",
                            "location": "Akihabara",
                            "cost": 150.0,
                            "activity_type": "Shopping",
                        },
                        {
                            "name": "Anime museum",
                            "start_time": "14:00",
                            "end_time": "16:00",
                            "location": "Akihabara Culture Zone",
                            "cost": 20.0,
                            "activity_type": "Museum",
                        },
                    ],
                },
                {
                    "day_number": 2,
                    "description": "Shrines and street food",
                    "date": "2025-04-21",
                    "activities": [
                        {
                            "name": "Visit Meiji Shrine",
                            "start_time": "10:00",
                            "end_time": "11:30",
                            "location": "Shibuya",
                            "cost": 0.0,
                            "activity_type": "Sightseeing",
                        },
                        {
                            "name": "Street food at Harajuku",
                            "start_time": "12:00",
                            "end_time": "13:30",
                            "location": "Takeshita Street",
                            "cost": 25.0,
                            "activity_type": "Food",
                        },
                    ],
                },
            ],
        },
        "owner_id": 2,
        "ai_cache_id": 2,
        "last_edited_by": 2,
        "created_at": datetime(2025, 4, 18, 9, 0),
        "updated_at": datetime(2025, 4, 18, 12, 0),
        "days": [],
        "access_list": [],
        "exports": [],
    },
    {
        # "id": 3,
        "name": "NYC Foodie Trip",
        "share_code": "sharecode-nyc-003",
        "is_public": True,
        "origin": "New York",
        "destination": "New York",
        "duration_days": 1,
        "budget": 300.0,
        "interests": ["food", "urban"],
        "route_data": {
            "name": "NYC Foodie Trip",
            "origin": "New York",
            "destination": "New York",
            "duration_days": 1,
            "budget": 300.0,
            "interests": ["food", "urban"],
            "days": [
                {
                    "day_number": 1,
                    "description": "Best eats in Manhattan",
                    "date": "2025-04-22",
                    "activities": [
                        {
                            "name": "Bagels for breakfast",
                            "start_time": "08:30",
                            "end_time": "09:30",
                            "location": "Ess-a-Bagel",
                            "cost": 12.0,
                            "activity_type": "Food",
                        },
                        {
                            "name": "Chelsea Market lunch",
                            "start_time": "13:00",
                            "end_time": "14:30",
                            "location": "Chelsea Market",
                            "cost": 35.0,
                            "activity_type": "Food",
                        },
                        {
                            "name": "Times Square walk",
                            "start_time": "15:00",
                            "end_time": "16:00",
                            "location": "Times Square",
                            "cost": 0.0,
                            "activity_type": "Sightseeing",
                        },
                    ],
                }
            ],
        },
        "owner_id": 3,
        "ai_cache_id": 3,
        "last_edited_by": 3,
        "created_at": datetime(2025, 4, 19, 10, 0),
        "updated_at": datetime(2025, 4, 19, 11, 0),
        "days": [],
        "access_list": [],
        "exports": [],
    },
    {
        # "id": 4,
        "name": "Nature in Iceland",
        "share_code": "sharecode-iceland-004",
        "is_public": False,
        "origin": "Reykjavik",
        "destination": "Golden Circle",
        "duration_days": 4,
        "budget": 2000.0,
        "interests": ["nature", "adventure"],
        "route_data": {
            "name": "Nature in Iceland",
            "origin": "Reykjavik",
            "destination": "Golden Circle",
            "duration_days": 4,
            "budget": 2000.0,
            "interests": ["nature", "adventure"],
            "days": [
                {
                    "day_number": 1,
                    "description": "Arrival and Blue Lagoon",
                    "date": "2025-04-25",
                    "activities": [
                        {
                            "name": "Blue Lagoon spa",
                            "start_time": "13:00",
                            "end_time": "16:00",
                            "location": "Grindavík",
                            "cost": 60.0,
                            "activity_type": "Relaxation",
                        }
                    ],
                },
                {
                    "day_number": 2,
                    "description": "Golden Circle tour",
                    "date": "2025-04-26",
                    "activities": [
                        {
                            "name": "Thingvellir National Park",
                            "start_time": "10:00",
                            "end_time": "12:00",
                            "location": "Thingvellir",
                            "cost": 0.0,
                            "activity_type": "Nature",
                        },
                        {
                            "name": "Geysir & Gullfoss",
                            "start_time": "12:30",
                            "end_time": "14:30",
                            "location": "Golden Circle",
                            "cost": 0.0,
                            "activity_type": "Nature",
                        },
                    ],
                },
            ],
        },
        "owner_id": 4,
        "ai_cache_id": 4,
        "last_edited_by": 4,
        "created_at": datetime(2025, 4, 20, 14, 0),
        "updated_at": datetime(2025, 4, 21, 9, 30),
        "days": [],
        "access_list": [],
        "exports": [],
    },
    {
        # "id": 5,
        "name": "Weekend in Rome",
        "share_code": "sharecode-rome-005",
        "is_public": True,
        "origin": "Rome",
        "destination": "Rome",
        "duration_days": 2,
        "budget": 800.0,
        "interests": ["history", "food"],
        "route_data": {
            "name": "Weekend in Rome",
            "origin": "Rome",
            "destination": "Rome",
            "duration_days": 2,
            "budget": 800.0,
            "interests": ["history", "food"],
            "days": [
                {
                    "day_number": 1,
                    "description": "Ancient Rome tour",
                    "date": "2025-04-27",
                    "activities": [
                        {
                            "name": "Colosseum visit",
                            "start_time": "09:00",
                            "end_time": "11:00",
                            "location": "Colosseum",
                            "cost": 18.0,
                            "activity_type": "Museum",
                        },
                        {
                            "name": "Lunch at Trastevere",
                            "start_time": "13:00",
                            "end_time": "14:30",
                            "location": "Tonnarello",
                            "cost": 40.0,
                            "activity_type": "Food",
                        },
                    ],
                },
                {
                    "day_number": 2,
                    "description": "Vatican and goodbye",
                    "date": "2025-04-28",
                    "activities": [
                        {
                            "name": "St. Peter's Basilica",
                            "start_time": "10:00",
                            "end_time": "12:00",
                            "location": "Vatican City",
                            "cost": 0.0,
                            "activity_type": "Sightseeing",
                        },
                        {
                            "name": "Flight home",
                            "start_time": "16:00",
                            "end_time": "19:00",
                            "location": "FCO Airport",
                            "cost": 0.0,
                            "activity_type": "Transportation",
                        },
                    ],
                },
            ],
        },
        "owner_id": 5,
        "ai_cache_id": 5,
        "last_edited_by": 5,
        "created_at": datetime(2025, 4, 22, 10, 0),
        "updated_at": datetime(2025, 4, 22, 11, 0),
        "days": [],
        "access_list": [],
        "exports": [],
    },
]

ROUTE_DAYS_FIXTURES = [
    {
        # "id": 1,
        "route_id": 2,
        "day_number": 1,
        "description": "Akihabara tech tour",
        "date": date(2025, 4, 20),
    },
    {
        # "id": 2,
        "route_id": 2,
        "day_number": 2,
        "description": "Shrines and street food",
        "date": date(2025, 4, 21),
    },
    {
        # "id": 3,
        "route_id": 3,
        "day_number": 1,
        "description": "Best eats in Manhattan",
        "date": date(2025, 4, 22),
    },
    {
        # "id": 4,
        "route_id": 4,
        "day_number": 1,
        "description": "Arrival and Blue Lagoon",
        "date": date(2025, 4, 25),
    },
    {
        # "id": 5,
        "route_id": 4,
        "day_number": 2,
        "description": "Golden Circle tour",
        "date": date(2025, 4, 26),
    },
    {
        # "id": 6,
        "route_id": 5,
        "day_number": 1,
        "description": "Ancient Rome tour",
        "date": date(2025, 4, 27),
    },
    {
        # "id": 7,
        "route_id": 5,
        "day_number": 2,
        "description": "Vatican and goodbye",
        "date": date(2025, 4, 28),
    },
]

ACTIVITIES_FIXTURES = [
    {
        # "id": 1,
        "day_id": 1,
        "name": "Gadget shopping",
        "start_time": "10:00",
        "end_time": "12:30",
        "location": "Akihabara",
        "cost": 150.0,
        "activity_type": "Shopping",
    },
    {
        # "id": 2,
        "day_id": 1,
        "name": "Anime museum",
        "start_time": "14:00",
        "end_time": "16:00",
        "location": "Akihabara Culture Zone",
        "cost": 20.0,
        "activity_type": "Museum",
    },
    {
        # "id": 3,
        "day_id": 2,
        "name": "Visit Meiji Shrine",
        "start_time": "10:00",
        "end_time": "11:30",
        "location": "Shibuya",
        "cost": 0.0,
        "activity_type": "Sightseeing",
    },
    {
        # "id": 4,
        "day_id": 2,
        "name": "Street food at Harajuku",
        "start_time": "12:00",
        "end_time": "13:30",
        "location": "Takeshita Street",
        "cost": 25.0,
        "activity_type": "Food",
    },
    {
        # "id": 5,
        "day_id": 3,
        "name": "Bagels for breakfast",
        "start_time": "08:30",
        "end_time": "09:30",
        "location": "Ess-a-Bagel",
        "cost": 12.0,
        "activity_type": "Food",
    },
    {
        # "id": 6,
        "day_id": 3,
        "name": "Chelsea Market lunch",
        "start_time": "13:00",
        "end_time": "14:30",
        "location": "Chelsea Market",
        "cost": 35.0,
        "activity_type": "Food",
    },
    {
        # "id": 7,
        "day_id": 3,
        "name": "Times Square walk",
        "start_time": "15:00",
        "end_time": "16:00",
        "location": "Times Square",
        "cost": 0.0,
        "activity_type": "Sightseeing",
    },
    {
        # "id": 8,
        "day_id": 4,
        "name": "Blue Lagoon spa",
        "start_time": "13:00",
        "end_time": "16:00",
        "location": "Grindavík",
        "cost": 60.0,
        "activity_type": "Relaxation",
    },
    {
        # "id": 9,
        "day_id": 5,
        "name": "Thingvellir National Park",
        "start_time": "10:00",
        "end_time": "12:00",
        "location": "Thingvellir",
        "cost": 0.0,
        "activity_type": "Nature",
    },
    {
        # "id": 10,
        "day_id": 5,
        "name": "Geysir & Gullfoss",
        "start_time": "12:30",
        "end_time": "14:30",
        "location": "Golden Circle",
        "cost": 0.0,
        "activity_type": "Nature",
    },
    {
        # "id": 11,
        "day_id": 6,
        "name": "Colosseum visit",
        "start_time": "09:00",
        "end_time": "11:00",
        "location": "Colosseum",
        "cost": 18.0,
        "activity_type": "Museum",
    },
    {
        # "id": 12,
        "day_id": 6,
        "name": "Lunch at Trastevere",
        "start_time": "13:00",
        "end_time": "14:30",
        "location": "Tonnarello",
        "cost": 40.0,
        "activity_type": "Food",
    },
    {
        # "id": 13,
        "day_id": 7,
        "name": "St. Peter's Basilica",
        "start_time": "10:00",
        "end_time": "12:00",
        "location": "Vatican City",
        "cost": 0.0,
        "activity_type": "Sightseeing",
    },
    {
        # "id": 14,
        "day_id": 7,
        "name": "Flight home",
        "start_time": "16:00",
        "end_time": "19:00",
        "location": "FCO Airport",
        "cost": 0.0,
        "activity_type": "Transportation",
    },
]

ROUTE_ACCESS_FIXTURES = [
    {
        "user_id": 1,
        "route_id": 1,
        "role": RouteRole.CREATOR,
    },
    {
        "user_id": 2,
        "route_id": 2,
        "role": RouteRole.CREATOR,
    },
    {
        "user_id": 3,
        "route_id": 3,
        "role": RouteRole.CREATOR,
    },
    {
        "user_id": 4,
        "route_id": 4,
        "role": RouteRole.CREATOR,
    },
    {
        "user_id": 5,
        "route_id": 5,
        "role": RouteRole.CREATOR,
    },
    {
        "user_id": 1,
        "route_id": 2,
        "role": RouteRole.EDITOR,
    },
    {
        "user_id": 3,
        "route_id": 2,
        "role": RouteRole.VIEWER,
    },
    {
        "user_id": 2,
        "route_id": 3,
        "role": RouteRole.EDITOR,
    },
    {
        "user_id": 1,
        "route_id": 3,
        "role": RouteRole.VIEWER,
    },
    {
        "user_id": 2,
        "route_id": 4,
        "role": RouteRole.VIEWER,
    },
    {
        "user_id": 1,
        "route_id": 5,
        "role": RouteRole.EDITOR,
    },
]
