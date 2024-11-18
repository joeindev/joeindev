class Joe:
    def __init__(self):
        self.name = "Joe (HoangLH)"
        self.age = None
        self.profession = None
        self.learning = ["Python", "C#", "C++", "Java", "Node.js"]
        self.skills = {
            "blender": "Intermediate",
        }
        self.humor = 0
        self.intelligence = {
            "smart": False,
            "iq": 116.0,
        }
        self.looks = {
            "handsome": True,
            "rating": "10/10",
        }
        self.life_skills = {
            "cooking": True,
            "cooking_skill": "6/10",
        }
        self.eq = 70
        self.relationship = {
            "girlfriend": False,
            "status": "Forever alone" if not self.relationship.get("girlfriend") else "In love",
        }

    def introduce(self):
        print(f"👋 Hi, I'm {self.name}!")
        print(f"Age: {self.age if self.age else 'Mysterious'}")
        print(f"Profession: {self.profession if self.profession else 'Undefined'}")
        print(f"🔧 Currently learning: {', '.join(self.learning)}")
        print(f"🛠️ Skills: Blender knowledge - {self.skills['blender']}")
        print(f"😂 Humor level: {self.humor}")
        print(f"🧠 Intelligence: {self.intelligence['iq']} IQ - {'Smart' if self.intelligence['smart'] else 'Not so smart'}")
        print(f"😎 Handsome: {'Yes' if self.looks['handsome'] else 'No'} ({self.looks['rating']})")
        print(f"🍳 Cooking: {self.life_skills['cooking_skill']} (Knows how to cook? {'Yes' if self.life_skills['cooking'] else 'No'})")
        print(f"💖 EQ: {self.eq}")
        print(f"💔 Girlfriend: {'Yes' if self.relationship['girlfriend'] else 'No'} ({self.relationship['status']})")


joe = Joe()
joe.introduce()
