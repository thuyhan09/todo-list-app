# Danh sách lưu công việc, mỗi công việc là một dictionary
tasks = []

def add_task(task_name):
    """Thêm công việc mới vào danh sách"""
    new_task = {'name': task_name, 'completed': False}
    tasks.append(new_task)
    print(f"Đã thêm công việc: '{task_name}'")

def list_tasks():
    """Liệt kê tất cả các công việc với trạng thái"""
    if not tasks:
        print("Chưa có công việc nào.")
    else:
        print("Danh sách công việc:")
        for i, task in enumerate(tasks, start=1):
            status = "[x]" if task['completed'] else "[ ]"
            print(f"{i}. {status} {task['name']}")

def complete_task(task_index):
    """Đánh dấu công việc là hoàn thành"""
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
        print(f"✅ Đã hoàn thành: {tasks[task_index]['name']}")
    else:
        print("❌ Chỉ số công việc không hợp lệ.")
def delete_task(task_index):
    """Xóa công việc theo chỉ số (0-based)."""
    # kiểm tra chỉ số hợp lệ
    if not tasks:
        print("❌ Danh sách rỗng. Không có công việc để xóa.")
        return

    if not isinstance(task_index, int):
        print("❌ Chỉ số phải là số nguyên.")
        return

    if 0 <= task_index < len(tasks):
        removed = tasks.pop(task_index)
        print(f"🗑️ Đã xóa công việc: {removed['name']}")
    else:
        print("❌ Chỉ số công việc không hợp lệ. Vui lòng nhập số từ 0 đến", len(tasks)-1)

if __name__ == "__main__":
    print("Chào mừng đến với ứng dụng To-Do List!")
    add_task("Học bài Git và GitHub")
    add_task("Làm bài tập thực hành ở nhà")
    add_task("Luyện Python")

    print("\n--- Sau khi thêm ---")
    list_tasks()

    print("\n--- Đánh dấu hoàn thành công việc 0 ---")
    complete_task(0)
    list_tasks()

    print("\n--- Xóa công việc 1 (chỉ số 1) ---")
    delete_task(1)
    list_tasks()
