from Base import Base
import json

def print_menu():
    print("\n" + "="*50)
    print("📊 СИСТЕМА УПРАВЛЕНИЯ БАЗОЙ ДАННЫХ")
    print("="*50)
    print("1. 📋 Показать все элементы")
    print("2. ➕ Добавить новый элемент")
    print("3. 🔍 Найти элемент по ID")
    print("4. ✏️ Обновить элемент по ID")
    print("5. 🗑 Удалить элемент по ID")
    print("6. 💾 Сохранить данные в файл")
    print("7. 📂 Загрузить данные из файла")
    print("8. 🚪 Выход")
    print("="*50)

def print_all_items(base):
    print("\n📋 ВСЕ ЭЛЕМЕНТЫ:")
    if not base.GetAll():
        print("   База данных пуста")
        return 0
    for item_id, item_data in base.GetAll().items():
        print(f"\n🔹 ID: {item_id}")
        for key, value in item_data.items():
            print(f"   {key}: {value}")

def add_item(base):
    print("\n➕ ДОБАВЛЕНИЕ НОВОГО ЭЛЕМЕНТА")
    print("Введите данные в формате JSON:")
    print('Пример: {"1": "Пример 1", "2": "Пример 2", "n": Пример n}')
    
    try:
        data_input = input("Данные: ")
        item_data = json.loads(data_input)
        item_id = base.Push(item_data)
        print(f"✅ Элемент добавлен с ID: {item_id}")
    except json.JSONDecodeError:
        print("❌ Ошибка: Неверный формат JSON")
    except Exception as e:
        print(f"❌ Ошибка: {e}")

def get_item(base):
    print("\n🔍 ПОИСК ЭЛЕМЕНТА ПО ID")
    try:
        item_id = input("Введите ID элемента: ")
        item = base.Get(item_id)
        if item:
            print(f"✅ Найден элемент ID: {item_id}")
            for key, value in item.items():
                print(f"   {key}: {value}")
        else:
            print(f"❌ Элемент с ID {item_id} не найден")
    except ValueError:
        print("❌ Ошибка: ID должен быть числом")
    except Exception as e:
        print(f"❌ Ошибка: {e}")

def update_item(base):
    print("\n✏️  ОБНОВЛЕНИЕ ЭЛЕМЕНТА")
    try:
        item_id = input("Введите ID элемента для обновления: ")
        print("Введите новые данные в формате JSON:")
        print('Пример: {"name": "Новое название", "rating": 5}')
        
        data_input = input("Новые данные: ")
        new_data = json.loads(data_input)
        
        if base.Update(item_id, new_data):
            print(f"✅ Элемент ID {item_id} успешно обновлен")
        else:
            print(f"❌ Элемент с ID {item_id} не найден")
    except json.JSONDecodeError:
        print("❌ Ошибка: Неверный формат JSON")
    except ValueError:
        print("❌ Ошибка: ID должен быть числом")
    except Exception as e:
        print(f"❌ Ошибка: {e}")

def delete_item(base):
    print("\n🗑️  УДАЛЕНИЕ ЭЛЕМЕНТА")
    try:
        item_id = input("Введите ID элемента для удаления: ")
        if base.Delete(item_id):
            print(f"✅ Элемент ID {item_id} успешно удален")
        else:
            print(f"❌ Элемент с ID {item_id} не найден")
    except ValueError:
        print("❌ Ошибка: ID должен быть числом")
    except Exception as e:
        print(f"❌ Ошибка: {e}")

def main():
    base = Base("data.json")
    print("🚀 База данных загружена")
    
    while True:
        print_menu()
        choice = input("Выберите действие (1-8): ")
        
        if choice == "1":
            print_all_items(base)
        elif choice == "2":
            add_item(base)
        elif choice == "3":
            get_item(base)
        elif choice == "4":
            update_item(base)
        elif choice == "5":
            delete_item(base)
        elif choice == "6":
            base.Save()
            print("✅ Данные сохранены в файл")
        elif choice == "7":
            base.Load()
            print("✅ Данные загружены из файла")
        elif choice == "8":
            print("👋 До свидания!")
            break
        else:
            print("❌ Неверный выбор. Попробуйте снова.")
        
        input("\nНажмите Enter чтобы продолжить...")

if __name__ == "__main__":
    main()
