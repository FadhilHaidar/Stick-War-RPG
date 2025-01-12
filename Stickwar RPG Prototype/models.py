# models.py
from dataclasses import dataclass, field
from typing import List, Optional
from abc import ABC, abstractmethod
import random

@dataclass
class Skill:
    """Data class representing a character skill"""
    name: str
    description: str
    defeats: List[str]
    defeated_by: List[str]
    success_message: str

@dataclass
class Character(ABC):
    """Abstract base class for all game characters"""
    name: str
    max_health: int
    health: int
    base_attack: int
    skills: List[Skill] = field(default_factory=list)
    gold_gain: int = 0

    @abstractmethod
    def choose_skill(self) -> Skill:
        """Abstract method to choose a skill during combat"""
        pass

@dataclass
class Player(Character):
    """Player character class with inventory management"""
    inventory: List[str] = field(default_factory=lambda: ["club"])
    equipped_weapon: str = "club"
    pots: int = 0

    def choose_skill(self) -> Optional[Skill]:
        """Let player choose a skill"""
        if not self.skills:
            return None
        return random.choice(self.skills)

    @property
    def attack(self) -> int:
        """Calculate total attack power including weapon bonus"""
        weapon_bonus = {
            "club": 5,
            "Sword": 15,
            "Battle Axe": 20,
            "Magic Staff": 25
        }.get(self.equipped_weapon, 0)
        return self.base_attack + weapon_bonus

@dataclass
class Enemy(Character):
    """Enemy character class with basic AI behavior"""
    def choose_skill(self) -> Optional[Skill]:
        """AI chooses a skill randomly"""
        if not self.skills:
            return None
        return random.choice(self.skills)