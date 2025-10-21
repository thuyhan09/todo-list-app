# Danh sách để lưu các công việc
tasks = []
def add_task(task_name):
  """Thêm một công việc mới vào danh sách."""
  tasks.append(task_name)
  print(f"Đã thêm công việc: '{task_name}'")
# --- Điểm bắt đầu của chương trình ---
if __name__ == "__main__":
  print("Chào mừng đến với ứng dụng To-Do List!")
  add_task("Học bài Git và GitHub")
  add_task("Làm bài tập thực hành ở nhà")
def list_tasks():
    """Liệt kê tất cả các công việc hiện có"""
    if not tasks:
        print("Chưa có công việc nào.")
    else:
        print("Danh sách công việc:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

list_tasks()  # Gọi hàm in danh sách
