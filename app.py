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

if __name__ == "__main__":
    print("Chào mừng đến với ứng dụng To-Do List!")
    add_task("Học bài Git và GitHub")
    add_task("Làm bài tập thực hành ở nhà")

    # Đánh dấu công việc đầu tiên là hoàn thành
    complete_task(0)

    # Liệt kê danh sách sau khi cập nhật trạng thái
    list_tasks()