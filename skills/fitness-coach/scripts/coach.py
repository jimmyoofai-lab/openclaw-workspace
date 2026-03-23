#!/usr/bin/env python3
"""
Fitness Coach - Personal trainer
"""

import json
import sys
import argparse
from datetime import datetime, timedelta
from pathlib import Path

# Data storage
DATA_DIR = Path.home() / ".openclaw" / "fitness"
PROFILE_FILE = DATA_DIR / "profile.json"
WORKOUTS_FILE = DATA_DIR / "workouts.json"

def ensure_dir():
    """Create data directory"""
    DATA_DIR.mkdir(parents=True, exist_ok=True)

def load_profile():
    """Load user profile"""
    if PROFILE_FILE.exists():
        with open(PROFILE_FILE) as f:
            return json.load(f)
    return None

def save_profile(profile):
    """Save user profile"""
    ensure_dir()
    with open(PROFILE_FILE, 'w') as f:
        json.dump(profile, f, indent=2)
    print("✅ Профиль сохранен")

def load_workouts():
    """Load workout history"""
    if WORKOUTS_FILE.exists():
        with open(WORKOUTS_FILE) as f:
            return json.load(f)
    return []

def save_workouts(workouts):
    """Save workout history"""
    ensure_dir()
    with open(WORKOUTS_FILE, 'w') as f:
        json.dump(workouts, f, indent=2)

def create_profile():
    """Interactive profile creation"""
    print("🏋️ Создание профиля тренера\n")
    
    levels = ["beginner", "intermediate", "advanced"]
    print("Уровень подготовки:")
    for i, l in enumerate(levels, 1):
        print(f"  {i}. {l}")
    level_choice = input("Выбери (1-3): ").strip()
    level = levels[int(level_choice) - 1] if level_choice.isdigit() else "beginner"
    
    print("\nЦели (через запятую: strength, endurance, weight_loss, health):")
    goals = [g.strip() for g in input("Цели: ").split(",")]
    
    print("\nВремя в день (минут):")
    time = int(input("Минут: ") or 45)
    
    print("\nМесто тренировок (home, gym, outdoor):")
    location = input("Место: ").strip() or "home"
    
    profile = {
        "level": level,
        "goals": goals,
        "time_available": time,
        "location": location,
        "created": datetime.now().isoformat(),
        "updated": datetime.now().isoformat()
    }
    
    save_profile(profile)
    return profile

def show_profile():
    """Display current profile"""
    profile = load_profile()
    if not profile:
        print("❌ Профиль не создан. Используй: чад fitness-coach profile create")
        return
    
    print("📋 Твой профиль:")
    print(f"  Уровень: {profile['level']}")
    print(f"  Цели: {', '.join(profile['goals'])}")
    print(f"  Время: {profile['time_available']} мин/день")
    print(f"  Место: {profile['location']}")

def generate_plan(profile, focus=None):
    """Generate weekly workout plan"""
    plans = {
        "beginner": {
            "upper": ["5x отжимания", "3x подтягивания (с помощью)", "3x планка 30сек"],
            "lower": ["3x приседания", "3x выпады", "3x икры"],
            "cardio": ["20мин бег", "100 прыжков на скакалке"],
            "rest": ["Йога или растяжка 15мин"]
        },
        "intermediate": {
            "upper": ["10x отжимания", "8x подтягивания", "3x планка 60сек", "3x отжимания на брусьях"],
            "lower": ["3x приседания 20", "3x выпады", "3x мертвая тяга", "3x румынская тяга"],
            "cardio": ["30мин интервальный бег", "200 прыжков на скакалке"],
            "rest": ["Пилатес или растяжка 20мин"]
        },
        "advanced": {
            "upper": ["15x отжимания", "12x подтягивания", "4x планка 90сек", "8x отжимания на брусьях", "8x отжимания в стойке"],
            "lower": ["4x приседания 25", "4x выпады", "4x мертвая тяга", "4x румынская тяга", "3x прыжковые выпады"],
            "cardio": ["40мин интервальный бег + спринты", "500 прыжков на скакалке"],
            "rest": ["Кроссфит или MMA 30мин"]
        }
    }
    
    level_plan = plans.get(profile["level"], plans["beginner"])
    
    print("📅 План тренировок на неделю:\n")
    week = ["Пн (Верх)", "Вт (Низ)", "Ср (Кардио)", "Чт (Отдых)", "Пт (Верх)", "Сб (Низ)", "Вс (Отдых)"]
    
    for day, (name, exercises) in enumerate(zip(week, ["upper", "lower", "cardio", "rest", "upper", "lower", "rest"])):
        print(f"{name}:")
        for ex in level_plan.get(exercises, []):
            print(f"  • {ex}")
        print()

def log_workout(exercise, reps=None, sets=None, distance=None, time_min=None):
    """Log a workout"""
    workouts = load_workouts()
    
    workout = {
        "date": datetime.now().isoformat(),
        "exercise": exercise,
        "reps": reps,
        "sets": sets,
        "distance": distance,
        "time": time_min
    }
    
    workouts.append(workout)
    save_workouts(workouts)
    
    print(f"✅ Залогировал: {exercise}")
    if reps and sets:
        print(f"   {reps} раз × {sets} подходов")
    elif distance:
        print(f"   {distance}км")
    
    # Show progress
    show_progress(exercise)

def show_progress(exercise=None):
    """Show workout progress"""
    workouts = load_workouts()
    
    if not workouts:
        print("📊 История тренировок пуста")
        return
    
    if exercise:
        filtered = [w for w in workouts if exercise.lower() in w["exercise"].lower()]
        if filtered:
            latest = filtered[-1]
            print(f"📈 Лучший результат: {latest['reps']} раз × {latest['sets']} подходов")
    else:
        # Overall stats
        today = datetime.now().date()
        streak = 0
        current_date = today
        
        # Calculate streak
        for i in range(len(workouts) - 1, -1, -1):
            workout_date = datetime.fromisoformat(workouts[i]["date"]).date()
            if workout_date == current_date:
                streak += 1
                current_date -= timedelta(days=1)
            else:
                break
        
        print(f"📊 Статистика:")
        print(f"  Всего тренировок: {len(workouts)}")
        print(f"  Текущая серия: {streak} дней ✅")
        if streak > 0:
            print(f"  🔥 Вперед! Не пропускай!")

def motivate(profile):
    """Motivational message"""
    messages = [
        "Ты сова - тренируйся вечером, когда энергия максимум! 🦉",
        "В морге весь день стоишь - физкультура вернет энергию 💪",
        "Здоровье это база для удаленки. Ты на правильном пути! 🚀",
        "Регулярность важнее интенсивности. Не пропускай!",
        "Каждая тренировка - это инвестиция в себя.",
        "Боль это только слабость, покидающая тело. Вперед! 💥",
        "Ты уже в пути. Не останавливайся!",
        "Мышцы растут на отдыхе. Спи хорошо после тренировки 😴",
    ]
    
    import random
    msg = random.choice(messages)
    print(f"💪 {msg}")

def main():
    parser = argparse.ArgumentParser(description="Fitness Coach")
    subparsers = parser.add_subparsers(dest="command")
    
    # Profile commands
    profile_parser = subparsers.add_parser("profile")
    profile_parser.add_argument("action", choices=["show", "create", "update"], default="show")
    
    # Plan
    plan_parser = subparsers.add_parser("plan")
    plan_parser.add_argument("--focus", choices=["upper", "lower", "cardio"])
    
    # Log workout
    log_parser = subparsers.add_parser("log")
    log_parser.add_argument("--exercise", required=True)
    log_parser.add_argument("--reps", type=int)
    log_parser.add_argument("--sets", type=int)
    log_parser.add_argument("--distance", type=str)
    log_parser.add_argument("--time", type=int)
    
    # Stats
    subparsers.add_parser("stats")
    subparsers.add_parser("motivate")
    
    args = parser.parse_args()
    ensure_dir()
    
    if args.command == "profile":
        if args.action == "create":
            create_profile()
        elif args.action == "update":
            print("Обновление профиля...")
            create_profile()
        else:
            show_profile()
    
    elif args.command == "plan":
        profile = load_profile()
        if not profile:
            print("❌ Сначала создай профиль: чад fitness-coach profile create")
            return
        generate_plan(profile, args.focus)
    
    elif args.command == "log":
        log_workout(
            args.exercise,
            reps=args.reps,
            sets=args.sets,
            distance=args.distance,
            time_min=args.time
        )
    
    elif args.command == "stats":
        show_progress()
    
    elif args.command == "motivate":
        profile = load_profile()
        motivate(profile or {})

if __name__ == "__main__":
    main()
